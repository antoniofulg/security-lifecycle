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

Record each case as pass, fail or blocked, with evidence and gaps. Do not count
keyword presence or the structural validator as a behavioral pass. For failed
cases, fix only demonstrated defects and rerun the affected case.

Run structural checks and their adversarial tests from the repository root:

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s evals -p 'test_*.py'
```

The validator enforces this repository's documented single-line YAML profile,
local Markdown links/anchors, distinct phase vocabulary plus trigger/exclusion
syntax, and entrypoint size (150 lines, 1,800 words, 12,000 UTF-8 bytes).
Description semantics and security judgment remain behavioral checks.
Secret detection is heuristic and cannot prove the absence of arbitrary formats.

Installation is checked in CI with Skills CLI 1.5.26: discover four entrypoints,
install into a fresh temporary project using `--agent codex --copy --yes`, then
validate that installed `.agents` tree. No global agent directories are touched.
The structural suite also checks portable copies and rejects links escaping a
single skill directory, even if those links work in the source repository.
