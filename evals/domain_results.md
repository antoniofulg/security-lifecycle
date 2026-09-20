# Extended-domain and audit-coordinator evaluation — 2026-09-20

An independent GPT-6 Astra evaluator reviewed the uncommitted source snapshot
without modifying it. Before reading routing/domain expectations or earlier results,
it received only the five skill names/descriptions and routing prompts, then each
domain case with the named skill and conditionally relevant references. Fixtures
remained virtual and were not executed.

## Blind routing

All ten selections matched the separate oracle: two each for spec, threat model,
implementation and review/audit, plus two unrelated controls selecting no skill.
The pre-release whole-codebase prompt selected `security-audit-coordinator`; the
bounded diff prompt selected `security-review`.

## Blind domain cases

- **D01 passed:** message requirements covered producer/tenant binding, replay,
  ordering, idempotency, commit/acknowledgment, retry/dead-letter limits and a valid
  control without inventing undecided product policy.
- **D02 passed provisionally:** the threat model covered primary, cache/search,
  export, backup and restore boundaries, keeping ACL propagation, tombstones and
  restore authority as material questions.
- **D03 passed:** SDK-independent recovery/linking guidance bound identity,
  provider, session and action; used one-time atomic recovery state; and included
  valid, swap, replay, stale and cross-account tests.
- **D04 passed:** review confirmed only the missing installers-group authorization
  at the privileged local-IPC boundary. It did not invent traversal, signature or
  code-execution findings from absent evidence.
- **D05 passed evidence discipline and remained partial:** independent hunter,
  verifier and coverage critic retained API tenant lookup, consumer tenant binding
  and replay/object-generation as `needs_validation`. The source omitted caller,
  database, broker and lifecycle semantics. A non-delete/poison-message path was
  deferred. The expectation was clarified so complete static evidence is required
  before confirmation.

## Independent worktree review

The first bounded review found one Major and seven Minor defects, primarily in the
new JSON validator: JSON `null` bypass, unhashable enum crashes, boolean integers,
Windows paths, optional starting paths and complete runs with unresolved evidence.
It also found unreachable AI/RAG guidance for tool-free systems and lost mandatory
redacted secret discovery after moving whole audits out of `security-review`.

All eight were fixed with regression tests. Thirteen concrete wording/contract
advisories were also resolved. A focused Astra re-review returned **SHIP** with two
remaining path/completeness variants; both were then fixed and covered by tests.
No Critical or Major defect remained at that verdict. The formal deep-review merge
was bounded before two polish jobs completed, so its first-pass report was not a
claim of exhaustive defect discovery.

## Verification

- `python3 scripts/validate_skills.py`: passed for five skills.
- `python3 -m unittest discover -s evals -p 'test_*.py'`: 48 tests passed after
  final regression fixes.
- `git diff --check`: clean.
- Skills CLI 1.5.26 discovered and copied all five skills into an isolated project;
  the installed tree passed the repository validator.
- Both metadata validators passed the new coordinator and changed review metadata.
- The optional upstream `quick_validate.py` could not run because its undeclared
  `PyYAML` import is unavailable. No dependency was installed; the repository's
  standard-library structural suite remained authoritative.

These evaluations demonstrate routing, selected domain behavior, artifact-validator
regressions and packaging for the supplied cases. They do not establish a false-
negative rate or prove complete security-domain coverage.
