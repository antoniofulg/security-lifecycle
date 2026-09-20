"""Adversarial tests for the audit artifact validator."""

import contextlib
import io
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "skills/security-audit-coordinator/scripts/validate_audit.py"
SPEC = importlib.util.spec_from_file_location("audit_validator", VALIDATOR_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def coverage(status="complete"):
    return {
        "source_ref": "abc123",
        "scope": ["src"],
        "profile": "standard",
        "run_status": status,
        "independent_verification": True,
        "units": [
            {
                "coverage_id": "api::owner::documents::access",
                "surface": "Document API",
                "boundary": "Object ownership",
                "subsystem": "API",
                "attack_class": "Access control",
                "starting_paths": ["src/documents.py"],
                "status": "candidate",
                "agent_id": "hunter-1",
                "reviewed_paths": ["src/documents.py"],
                "candidate_fingerprints": ["documents-owner-check"],
                "unresolved": [],
            }
        ],
    }


def findings(verdict="confirmed"):
    common = {
        "verdict": verdict,
        "fingerprint": "documents-owner-check",
        "title": "Document lookup omits owner scope",
        "trace": [
            {"file": "src/documents.py", "line": 10,
             "description": "A caller selects an arbitrary document identifier."}
        ],
        "evidence": [
            {"file": "src/documents.py", "line": 12,
             "description": "The query filters by identifier without owner."}
        ],
    }
    if verdict == "confirmed":
        common.update({
            "impact": "A valid user can read another owner's document.",
            "severity": "high",
            "confidence": "high",
            "verification_method": "static",
            "remediation": "Filter the lookup by current owner and tenant.",
            "regression_test": "Reject another owner's identifier and allow the owner's identifier.",
        })
    elif verdict == "needs_validation":
        common.update({
            "blockers": ["Deployment policy is not present in the repository."],
            "validation_plan": "Ask the owner to inspect the active policy without sending audit traffic.",
        })
    else:
        common["reason"] = "Shared repository policy applies the owner filter."
    return [common]


class AuditValidatorTests(unittest.TestCase):
    def test_complete_pair_passes(self):
        self.assertEqual([], VALIDATOR.validate_coverage(coverage()))
        self.assertEqual([], VALIDATOR.validate_findings(findings()))
        self.assertEqual([], VALIDATOR.validate_pair(coverage(), findings()))

    def test_all_verdicts_pass(self):
        for verdict in ("confirmed", "needs_validation", "rejected"):
            self.assertEqual([], VALIDATOR.validate_findings(findings(verdict)), verdict)

    def test_unsafe_source_path_rejected(self):
        value = findings()
        value[0]["trace"][0]["file"] = "../outside.py"
        self.assertTrue(any("unsafe" in error for error in VALIDATOR.validate_findings(value)))

    def test_windows_absolute_source_path_rejected(self):
        value = findings()
        value[0]["trace"][0]["file"] = "C:/outside.py"
        self.assertTrue(any("unsafe" in error for error in VALIDATOR.validate_findings(value)))

    def test_windows_drive_relative_source_path_rejected(self):
        value = findings()
        value[0]["trace"][0]["file"] = "C:../outside.py"
        self.assertTrue(any("unsafe" in error for error in VALIDATOR.validate_findings(value)))

    def test_needs_validation_cannot_have_severity(self):
        value = findings("needs_validation")
        value[0]["severity"] = "high"
        self.assertTrue(any("unexpected field" in error for error in VALIDATOR.validate_findings(value)))

    def test_nonstring_result_arrays_reject_without_exception(self):
        value = coverage()
        value["units"][0]["reviewed_paths"] = [{"path": "src/documents.py"}]
        value["units"][0]["candidate_fingerprints"] = [["nested"]]
        errors = VALIDATOR.validate_coverage(value)
        self.assertTrue(any("reviewed_paths" in error for error in errors))
        self.assertTrue(any("candidate_fingerprints" in error for error in errors))

    def test_unhashable_enums_reject_without_exception(self):
        value = coverage()
        value["profile"] = []
        value["units"][0]["status"] = {}
        errors = VALIDATOR.validate_coverage(value)
        self.assertTrue(any("profile" in error for error in errors))
        self.assertTrue(any("status" in error for error in errors))

    def test_booleans_do_not_pass_integer_fields(self):
        coverage_value = coverage()
        coverage_value["budget"] = True
        finding_value = findings()
        finding_value[0]["trace"][0]["line"] = True
        self.assertTrue(any("budget" in error
                            for error in VALIDATOR.validate_coverage(coverage_value)))
        self.assertTrue(any("positive integer" in error
                            for error in VALIDATOR.validate_findings(finding_value)))

    def test_starting_paths_are_required(self):
        value = coverage("in_progress")
        del value["units"][0]["starting_paths"]
        errors = VALIDATOR.validate_coverage(value)
        self.assertTrue(any("starting_paths" in error for error in errors))

    def test_complete_run_requires_candidate_record(self):
        self.assertTrue(any("every candidate" in error
                            for error in VALIDATOR.validate_pair(coverage(), [])))

    def test_partial_run_may_retain_unvalidated_candidate(self):
        value = coverage("partial")
        self.assertEqual([], VALIDATOR.validate_pair(value, []))

    def test_complete_run_rejects_needs_validation_record(self):
        value = findings("needs_validation")
        errors = VALIDATOR.validate_pair(coverage(), value)
        self.assertTrue(any("needs_validation" in error for error in errors))

    def test_complete_run_rejects_unresolved_candidate_evidence(self):
        coverage_value = coverage()
        coverage_value["units"][0]["unresolved"] = ["One condition is still unknown."]
        errors = VALIDATOR.validate_pair(coverage_value, findings())
        self.assertTrue(any("unresolved candidate" in error for error in errors))

    def test_complete_run_rejects_deferred_unit(self):
        value = coverage()
        unit = value["units"][0]
        unit.update({
            "status": "deferred",
            "agent_id": None,
            "reviewed_paths": [],
            "candidate_fingerprints": [],
            "unresolved": ["Budget ended before assignment."],
        })
        errors = VALIDATOR.validate_coverage(value)
        self.assertTrue(any("unfinished units" in error for error in errors))

    def test_cli_rejects_symlink_input(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            real = directory / "coverage-real.json"
            linked = directory / "coverage.json"
            output = directory / "findings.json"
            real.write_text(json.dumps(coverage()))
            linked.symlink_to(real)
            output.write_text(json.dumps(findings()))
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(1, VALIDATOR.main([str(linked), str(output)]))

    def test_cli_rejects_json_null_documents(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            coverage_path = directory / "coverage.json"
            findings_path = directory / "findings.json"
            coverage_path.write_text("null")
            findings_path.write_text("null")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(1, VALIDATOR.main([str(coverage_path), str(findings_path)]))


if __name__ == "__main__":
    unittest.main()
