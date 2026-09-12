"""Adversarial structural checks; writes only isolated temporary copies."""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_skills.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.skill = self.root / "skills/security-spec/SKILL.md"

    def reject(self, fragment):
        errors = VALIDATOR.validate(self.root)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_current_tree_passes(self):
        self.assertEqual([], VALIDATOR.validate(self.root))

    def test_frontmatter_missing(self):
        self.skill.write_text("# Empty skill\n")
        self.reject("frontmatter")

    def test_name_and_directory(self):
        self.skill.write_text(self.skill.read_text().replace("name: security-spec", "name: other"))
        self.reject("match directory")

    def test_duplicate_name(self):
        self.skill.write_text(self.skill.read_text().replace("name: security-spec", "name: security-review"))
        self.reject("duplicate skill name")

    def test_description_boundary(self):
        self.skill.write_text(self.skill.read_text().replace(" Excludes ", " Includes "))
        self.reject("Excludes boundary")

    def test_missing_reference_and_anchor(self):
        with self.skill.open("a") as file:
            file.write("\n[missing](references/no-file.md)\n[bad](#no-heading)\n")
        self.reject("broken local link")
        self.reject("broken heading anchor")

    def test_reference_style_and_bare_pointer(self):
        with self.skill.open("a") as file:
            file.write("\n[read][missing]\n`references/no-file.md`\n")
        self.reject("undefined link reference")
        self.reject("broken local link")

    def test_capitalization(self):
        self.skill.rename(self.skill.with_name("skill.md"))
        self.reject("capitalized")

    def test_placeholder(self):
        self.skill.write_text(self.skill.read_text() + "\n" + "TO" + "DO" + "\n")
        self.reject("placeholder")

    def test_portuguese_todo_is_not_placeholder(self):
        self.skill.write_text(self.skill.read_text() + "\nTodo o fluxo e todo contexto.\n")
        self.assertEqual([], VALIDATOR.validate(self.root))

    def test_env_fixture_secret(self):
        path = self.root / "evals/runtime.env"
        key = "PASS" + "WORD"
        path.write_text(key + '="' + "synthetic" + '-only"\n')
        self.reject("possible secret")

    def test_size_limit(self):
        self.skill.write_text(self.skill.read_text() + "\ntext" * 151)
        self.reject("exceeds")

    def test_secret_assignment_redacts_error(self):
        import json
        path = self.root / "evals/leak.json"
        value = "inert" + "-synthetic-test-only"
        key = "API_" + "KEY"
        path.write_text(json.dumps({"file": key + '="' + value + '"'}))
        errors = VALIDATOR.validate(self.root)
        self.assertTrue(any("possible secret" in error for error in errors))
        self.assertTrue(all(value not in error for error in errors))

    def test_known_token_shape(self):
        import json
        path = self.root / "evals/leak.json"
        path.write_text(json.dumps({"file": "gh" + "p_" + "A" * 36}))
        self.reject("possible secret")

    def test_ui_prompt(self):
        path = self.root / "skills/security-spec/agents/openai.yaml"
        path.write_text(path.read_text().replace("$security-spec", "$wrong-skill"))
        self.reject("invoke its skill")

    def test_nested_entrypoint(self):
        path = self.skill.parent / "references/nested/SKILL.md"
        path.parent.mkdir()
        path.write_text(self.skill.read_text())
        self.reject("exactly four entrypoints")

    def test_fenced_heading_is_not_anchor(self):
        self.skill.write_text(self.skill.read_text() + "\n```md\n# Ghost\n```\n[x](#ghost)\n")
        self.reject("broken heading anchor")

    def test_tilde_fence_example_is_not_link(self):
        self.skill.write_text(self.skill.read_text() + "\n~~~md\n[x](absent.md)\n~~~\n")
        self.assertEqual([], VALIDATOR.validate(self.root))

    def test_angle_link_with_spaces(self):
        self.skill.write_text(self.skill.read_text() + "\n[x](<references/no such.md>)\n")
        self.reject("broken local link")

    def test_python_unfinished_marker(self):
        (self.root / "scripts/example.py").write_text("# " + "TO" + "DO" + "\n")
        self.reject("unfinished placeholder")

    def test_python_fixture_token(self):
        (self.root / "evals/test_fixture.py").write_text('key = "' + "gh" + "p_" + "A" * 36 + '"')
        self.reject("possible secret")

    def test_slack_token(self):
        import json
        (self.root / "evals/slack.json").write_text(json.dumps("xo" + "xb-" + "1" * 30))
        self.reject("possible secret")

    def test_duplicate_generic_descriptions(self):
        for path in (self.root / "skills").glob("*/SKILL.md"):
            lines = path.read_text().splitlines()
            lines[2] = 'description: "Use when doing security work in this repository. Excludes other tasks."'
            path.write_text("\n".join(lines))
        self.reject("duplicate description")
        self.reject("distinct phase/task trigger")

    def test_long_single_token(self):
        self.skill.write_text(self.skill.read_text() + "\n" + "x" * 20000)
        self.reject("12000 bytes")


if __name__ == "__main__":
    unittest.main()
