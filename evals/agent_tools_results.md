# Agent and tool security evaluation — 2026-09-12

Scope: new conditional agent-tools references in the four existing skills, source
attribution/portable legal bundles, and fourteen virtual behavior cases. No SDK
implementation, server, browser extension or new skill was created.

## Source and structural verification

MCP source pinned at aa8ce049f089f92618340190d4ece141f663310d, using stable
2026-07-28 security/authorization/transport/tool documentation; no draft rules
silently substituted. WebMCP source pinned at
97da8f515427594c856307e3476c0a0db9698fbb, questionnaire and index.bs security/privacy.
An independent source reviewer checked all four references against MCP and found
one overly broad proxy-consent condition. It was narrowed to static upstream
client ID plus dynamically registered MCP clients; the reviewer confirmed the fix.

`python3 scripts/validate_skills.py` and 29 unittest checks passed. The tests verify
portable links, license copies and correspondence between cases and their separate
expectations, in addition to the existing adversarial structural checks.
Skills CLI 1.5.26 installed all four into a temporary project using copy mode for
Codex. The installed tree passed validation; every bundled file matched source
bytes (implementation 13, review 20, spec 10, threat model 10). No global skill
directory was changed. Source/legal copies remain available after installation.

## Independent review cases

AT01 passed as a specification: seven output sections, EARS requirements,
stable ABUSE/SEC links and negative/authorized controls for tenant access,
delegation, disclosure, token audience, approval and origin. It did not produce
code findings or require an SDK/browser API; unspecified limits stayed open.

AT02 completed the material-assumption check-in before its final model. The
simulated answers established owned components, a stateless MCP HTTP flow with
inbound token passthrough, absent consumer mediation, and UI-only deletion
confirmation; browser support remained unknown. The model separated runtime,
CI and tests and linked seven threats to boundaries/assets with a Mermaid flow.
The initial output assumed deletion was irreversible without evidence. The
reference was narrowed to require evidence of retention/restore before making
that claim; a focused rerun removed it and made impact/priority conditional on
recovery capability. AT02 passed after this demonstrated correction.

AT03 passed as an implementation proposal: SDK-neutral contracts validate MCP
recipient/scopes and scoped data access with a distinct upstream credential;
consumer dispatch/disclosure is bounded outside model text. WebMCP delegates to
backend enforcement with trusted confirmation, actor/tenant/object/action binding,
expiry and atomic one-use consumption. It proposed replay, concurrency, failure
and valid-use checks, without asserting an available browser confirmation API.
The proposal is not executable SDK code and its tests were not run.

Evaluators received only selected input cases and the installed skill/reference
files, never the expectation files or previous outputs. Results below are static
reasoning over virtual code and declared complete-path contracts, not live exploit
reproduction or a benchmark of model robustness.

| Case | Result | Decisive evidence |
| --- | --- | --- |
| AT04 | Pass: High/high-confidence IDOR | tool.py line 3 changes to ID-only lookup after scope-only check; known foreign-tenant ID and absent RLS confirmed in context. |
| AT05 | Pass: no confirmed finding | Both method names alias the owner/tenant-scoped query. |
| AT06 | Pass: High/high-confidence credential boundary failure | auth.py line 2 disables audience; line 4 forwards inbound token; context establishes unauthorized upstream private-data access. |
| AT07 | Pass: no confirmed finding | Recipient/scope/ownership checks and separate upstream credential are enforced. |
| AT08 | Pass: no confirmed finding | Pipe-only, sandboxed local stdio with no HTTP/private-data surface does not need HTTP OAuth. |
| AT09 | Pass: High/high-confidence unauthorized disclosure path | Supplied synthetic planner trace reaches unconditional send at consumer.py line 3 outside the user's local-only delegation. |
| AT10 | Pass: no confirmed finding | Independent policy gate denies send regardless of hostile result text. |
| AT11 | Pass: High/high-confidence destructive consent bypass | Misleading read-only tool reaches deletion at api.py line 4; explicit required confirmation exists only in UI. |
| AT12 | Pass: no confirmed finding | Backend atomically consumes actor/object/action-bound, expiring, one-use approval; no extra browser dialog is required. |
| AT13 | Pass: Needs verification, no confirmed finding | Registration alone does not establish purchase policy, backend behavior or browser safeguards. |
| AT14 | Pass: no confirmed finding | Intentionally public stateless MCP 2026-07-28 arithmetic needs neither protocol session ID nor OAuth; network schema resolution is correctly disabled. |

The review agents loaded the installed entrypoint, evidence/report and agent-tools
references, with access guidance where needed. They did not execute payloads,
contact fixture URLs, test credentials or treat a synthetic marker as a live secret.
Protected cases use explicitly supplied control contracts; their unseen runtime
implementations were not independently verified. Browser guarantees remained
unknown where the case withheld implementation/version evidence.
