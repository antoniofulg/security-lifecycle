# Security review report

Modified synthesis of Sentry/OWASP and GitHub Awesome Copilot; CC BY-SA 4.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Start with mode, requested scope, snapshot/base/head and counts by severity
(Critical/High/Medium/Low), counting only confirmed findings.

For each confirmed finding include:
- Stable finding ID and short title.
- Severity with contextual rationale; High confidence with supporting evidence.
- File and line (changed line for diff), plus redacted snippet where useful.
- Attacker role, input origin, transformations/control checks and sink.
- Concrete impact, exploit preconditions and evidence of control failure.
- Verification method: static trace, test or observed reproduction.
- Mitigation and regression test; related candidates deduplicated by root cause.

Before finalizing, verify every cited line against the exact reviewed source
snapshot. For virtual files embedded in JSON, decode the file and count its own
lines; JSON container lines and remembered offsets are not source locations.

Keep **Dependencies** and **Secrets** as distinct audit sections. Reference IDs
from the confirmed-finding list instead of counting them twice. Dependencies
include package, resolved version, current advisory URL/ID, affected range,
lookup date and reachability status. Secrets include location and credential
type only, exposure evidence and containment/rotation proposal—never values,
partial values, fingerprints or value-bearing before snippets. An inert fixture
marker is not a live credential finding.

Then include **Needs verification**, **Hardening recommendations**, and
**Coverage and limitations**. For each gap state the omitted check and consequence.
Report inspected paths/surfaces, tools and versions/date, failed/unavailable checks,
runtime versus build/test coverage, network restrictions and exclusions.

For full-audit Critical/High findings, provide proposed before/after patches and
why they block the path. Redact secrets in both. Include a valid-use regression
test and negative test. State whether anything was changed; review alone must
leave source untouched. If missing context prevents a safe patch, show the
concrete proposed change at the known boundary and name the blocking detail.

With zero confirmed findings, say “No confirmed vulnerabilities found in the
examined scope,” followed by actual coverage and limitations. Never imply an
unperformed dependency audit or blanket security guarantee.
