# Behavioral evaluations

[cases.json](cases.json) contains nine prompts with small virtual repository files.
The technology-specific examples exercise concept-based routing; they do not
require local framework guides. Case 03 now selects identity/input/persistence
guidance and verifies framework details from current documentation when needed.
These are intentionally incomplete application slices with explicit wiring/context,
not runnable services. Do not install dependencies or execute vulnerable examples.
The only credential representation is the inert `[REDACTED_TEST_SECRET]` marker.
No real or realistic credential values are committed.

Give an independent agent the selected case prompt/files and its skill entrypoint.
Allow only relevant references and read-only context gathering. Do not give that
agent [expectations.json](expectations.json), prior findings or proposed fixes.
Record actual output, references read, tool limitations and source snapshot.
Then compare behavior to the expectations; semantic judgments require a reviewer.

For case 02, the evaluator must first ask its material questions. Only then act
as the evaluation user: confirm public multi-tenant ingress, signed events with
a replay window but no deduplication, worker access to internal network/metadata,
XML parsing possible, and extraction/expanded-size controls not yet designed.
These are evaluation answers, not deployment facts about this repository.
Require a final model after that response. A premature final is a failure.

Case 06 uses a historical resolved lodash version. Query an advisory database at
run time; do not treat an expected CVE string as a test oracle. The secret section
must recognize the inert marker while demonstrating redacted reporting. A real
secret exposure cannot be simulated by committing a real credential.

## Agent and tool cases

[agent_tools_cases.json](agent_tools_cases.json) adds fourteen cases across all
four skills. Keep [agent_tools_expectations.json](agent_tools_expectations.json)
hidden from evaluators. Evaluate against an isolated installed copy to exercise
reference portability as well as behavior. Pseudocode/adapters are explicitly
fixture contracts, not claims about SDK or browser API signatures.

AT01–AT03 exercise requirements, threat modeling and implementation. For AT02,
wait for material questions before supplying these simulated design facts: all
first-party components are owned; upstream is an internal separate API; third-party
tool results are untrusted. MCP uses 2026-07-28 HTTP OAuth without session/handles;
ingress validates recipient/scopes/tenant, but the design forwards its token to
an upstream accepting the issuer without audience validation. The consumer has
read-only, non-disclosure delegation but no independent dispatch/disclosure gate.
WebMCP intends same-origin use, browser/version not chosen; deletion confirmation
exists only in the UI, not at the backend. Require a final conditional model.

AT04–AT14 pair vulnerable and protected object access, credential forwarding,
consumer injection and WebMCP deletion, with stdio, stateless public HTTP and
unknown-browser controls. A supplied synthetic planner trace supports static
analysis in AT09; it is not a measured attack on a real model. Never execute the
hostile text, send data or contact fixture URLs. Review unconfirmed paths as gaps,
and retain legitimate previously delegated actions in protected cases.
See [agent and tool results](agent_tools_results.md) for the recorded run and its
limits; these results must not be provided to future independent evaluators.

Record each case as pass, fail or blocked, with evidence and gaps. Do not count
keyword presence or the structural validator as a behavioral pass. For failed
cases, fix only demonstrated defects and rerun the affected case.

## Extended-domain cases

[domain_cases.json](domain_cases.json) adds five phase-specific cases for message
delivery, data lifecycle, account recovery/linking, privileged local IPC and the
whole-codebase audit coordinator. Keep [domain_expectations.json](domain_expectations.json)
hidden from evaluators. The audit case is a virtual quick/source-only run: return
coverage/finding records without writing into this repository or executing fixtures.
Compare actual output to the separate oracle and record reference selection,
independence limits and any deferred units.
See the [independent evaluation record](domain_results.md) for the blind run,
review findings, fixes and limitations.

## Runtime pentest cases

[pentest_cases.json](pentest_cases.json) contains six virtual cases for
`security-pentest`. Give an independent evaluator an isolated copy of that skill
and the selected prompt/files only. Keep
[pentest_expectations.json](pentest_expectations.json) and prior results hidden.
The evaluator may read the skill and relevant references, but must not execute
fixture code, launch tools against targets or contact fixture URLs. Trace data
simulates prior observations; it is not a measured live pentest.

The cases cover authorized cross-organization access with a protected field
control, missing authority, scope/redirect and instruction-injection boundaries,
scanner false positives and lost sessions, source/deployment drift, and feature
selection under traffic/tool constraints. Record actual responses, reference
selection and limitations before comparing them with the separate expectations.
Evaluate R11-R15 alongside existing routing controls using metadata only.
See [pentest evaluation results](pentest_results.md) for actual-output excerpts,
oracle comparisons, the evaluated snapshot and limits of the simulated run.

Run structural checks and their adversarial tests from the repository root:

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s evals -p 'test_*.py'
```

The validator enforces this repository's documented single-line YAML profile,
local Markdown links/anchors, nonblank unique descriptions up to 1,024 characters,
and entrypoint size (150 lines, 1,800 words, 12,000 UTF-8 bytes).
Description semantics and security judgment remain behavioral checks.
Secret detection is heuristic and cannot prove the absence of arbitrary formats.

Installation is checked in CI with Skills CLI 1.5.26: discover six entrypoints,
install into a fresh temporary project using `--agent codex --copy --yes`, then
validate that installed `.agents` tree. No global agent directories are touched.
The structural suite also checks portable copies and rejects links escaping a
single skill directory, even if those links work in the source repository.

## Description routing

For [routing_cases.json](routing_cases.json), give an independent evaluator only
the six names/descriptions and the prompts. Ask it to choose one skill or none
without reading skill bodies. Compare against [routing_expectations.json](routing_expectations.json)
afterward. The controls include unrelated refactoring and a typo fix; generic
programming work must not activate a security skill merely because code is present.

For disclosure changes, run a scoped review and a whole-codebase audit separately,
recording which files were actually read. The focused review must not load audit
coordination instructions; the coordinator must preserve independent validation,
coverage state and report/patch authorization boundaries.
