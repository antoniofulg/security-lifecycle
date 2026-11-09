# Third-party notices and provenance

Sources were retrieved on the dates stated below. SHAs resolved from each
repository's `main` before adaptation; Sentry, MCP and WebMCP were re-pinned
on 2026-11-09 (see the upstream refresh entry below). Links below are immutable snapshots.
This is an original, condensed rewrite: examples, routing, contracts and
evaluation fixtures were newly written. No upstream skill is vendored wholesale.

| Source | Pinned commit | License checked in repository | Reused topics and destination |
| --- | --- | --- | --- |
| [Sentry security-review](https://github.com/getsentry/skills/tree/e94f22214528d69899d09c627b3315ddc3544816/skills/security-review) | `e94f22214528d69899d09c627b3315ddc3544816` | [Root Apache-2.0](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/LICENSE); [specific reference CC BY-SA 4.0 notice](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/skills/security-review/LICENSE) | Only security-review: research/report scope, source-to-sink evidence, confidence, framework protections, contextual severity, false-positive suppression, topic/JS/Python/Docker guidance. |
| [GitHub Awesome Copilot security-review](https://github.com/github/awesome-copilot/tree/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/security-review) | `7568a482ce2df38f8965ab5336a3220db796a4ba` | [MIT](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/LICENSE) | Only security-review: audit sequence, dependency and secret sections, cross-file second pass, finding fields, proposed patches, seven language families, CI/IaC. |
| [OpenAI security-best-practices](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices) | `49f948faa9258a0c61caceaf225e179651397431` | [Local Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices/LICENSE.txt) | Only security-implementation: stack selection, secure defaults, passive high-impact warnings, documented exceptions, isolated fixes and regression checks; React, Vue, Next.js, Express, jQuery, Django, Flask, FastAPI, Go; TLS/cookie context. |
| [OpenAI security-threat-model](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model) | `49f948faa9258a0c61caceaf225e179651397431` | [Local Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt) | Only security-threat-model: repository evidence, separate execution planes, assets, boundaries, capabilities, abuse paths, prioritization, material-assumption check-in and Mermaid. |
| [Sentry secret-serialization](https://github.com/getsentry/skills/tree/473d2594cd91c96ac8348f297e016b631e842487/skills/secret-serialization) | `473d2594cd91c96ac8348f297e016b631e842487` | [Root Apache-2.0](https://github.com/getsentry/skills/blob/473d2594cd91c96ac8348f297e016b631e842487/LICENSE); no skill-local license | security-review, security-implementation and audit coordinator: credential holder plus wholesale serialization sink, partial exclusion of generated paths, raw attribute access, what not to report. Concept only; no tables or examples copied. |
| [Sentry security-model](https://github.com/getsentry/skills/tree/2960faf806231e253302a410b9e97e7682aa8b64/skills/security-model) | `2960faf806231e253302a410b9e97e7682aa8b64` | [Root Apache-2.0](https://github.com/getsentry/skills/blob/2960faf806231e253302a410b9e97e7682aa8b64/LICENSE); upstream itself adapts `define-security-policy` from [openai/codex-security](https://github.com/openai/codex-security) (Apache-2.0) | security-review, security-audit-coordinator and security-threat-model: consuming a repository policy as untrusted scope evidence, base-revision reading in diffs, enforced versus monitored controls, exclusion matching. Consumption rules only; authoring workflow and resolver script not adopted. |
| [Awesome Copilot threat-model-analyst](https://github.com/github/awesome-copilot/tree/421418928715158da3610571cb9e9cbb18d4747d/skills/threat-model-analyst) | `421418928715158da3610571cb9e9cbb18d4747d` | [MIT](https://github.com/github/awesome-copilot/blob/421418928715158da3610571cb9e9cbb18d4747d/LICENSE) | security-threat-model: update-tracking concepts (stable IDs, status reclassification, baseline verification, recorded disagreements). No templates, quotas, checklists or scripts adopted. |
| [Cloudflare security-audit](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit) | `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` | [MIT](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/LICENSE) | Four lifecycle skills and audit coordinator: original phase-specific coverage of identity protocols, distributed data, lifecycle, availability, operations, AI/RAG, native/binary and local platforms; audit coordinator: coverage ledger, bounded workers, independent verification, stable verdicts and additive reruns. |

The original security-spec core, structural validator and fixtures were written
for the requested contract. The new agent-tools reference also uses the official
protocol sources below. They do not combine Sentry and Copilot workflows.

## Studied files at the pinned commits

Sentry: SKILL.md; references/api-security.md, authentication.md, authorization.md,
business-logic.md, cryptography.md, csrf.md, data-protection.md, deserialization.md,
error-handling.md, file-security.md, injection.md, logging.md, misconfiguration.md,
modern-threats.md, ssrf.md, supply-chain.md, xss.md; languages/javascript.md,
languages/python.md; infrastructure/docker.md. These were condensed into the
review evidence/report contracts and concept references for access, data,
untrusted input, persistence, frontend, supply chain and runtime isolation.

Sentry secret-serialization (added 2026-11-09): SKILL.md, SPEC.md, SOURCES.md,
references/python.md and references/javascript-typescript.md. Only the holder/sink
model and exclusion semantics were kept; library tables were replaced by an
instruction to verify the installed library's generated paths in current docs.

Sentry security-model (added 2026-11-09): SKILL.md, SPEC.md, SOURCES.md,
references/consuming-policy.md and scripts/resolve_security_model.py. Only the
consumption contract was kept, with excluded findings reported under a separate
heading rather than suppressed.

Awesome Copilot threat-model-analyst (added 2026-11-09): SKILL.md and
references/orchestrator.md, incremental-orchestrator.md, analysis-principles.md,
verification-checklist.md and output-formats.md. Its finding quotas and
technology checklist conflict with this collection and were not adopted.

Awesome Copilot: SKILL.md; references/language-patterns.md, report-format.md,
secret-patterns.md, vuln-categories.md and vulnerable-packages.md. The package
watchlist was studied only to replace it with current advisory lookup instructions.

OpenAI best practices: SKILL.md and all ten references: general JavaScript
frontend, React, Vue, jQuery, Next.js, Express, Django, Flask, FastAPI and Go.
These informed the implementation-only guidance, now consolidated into five
surface-based references. Stack-specific APIs/defaults are verified on demand.
OpenAI threat model: SKILL.md, references/prompt-template.md and
references/security-controls-and-assets.md informed its two references.

Recursive source-tree checks found no relevant NOTICE file for these four skills:
Sentry has none; the GitHub and OpenAI NOTICE files belong to unrelated skills.

Cloudflare source and MIT license were checked 2026-09-19. Its repository contains
no separate NOTICE file. The source was studied as an audit architecture and attack-
surface taxonomy; no prompt, schema or implementation was copied verbatim. The
collection uses smaller phase-specific references, retains static evidence as a
valid confirmation method and implements one original Python-standard-library
artifact validator. Preserve [Cloudflare's MIT text](licenses/Cloudflare-MIT.txt).

## Changes from upstream

### Upstream refresh — 2026-11-09

Sentry, MCP and WebMCP were compared against their new HEAD commits. Licenses
were unchanged. Sentry's security-review removed routing to nonexistent language
and infrastructure guides (already absent here) and added routing for prototype
pollution, DOM clobbering, WebSocket and prompt-construction code; the review
frontend reference now names DOM clobbering explicitly. The released MCP
2026-07-28 specification had only editorial changes; the draft authorization pages
moved to Client ID Metadata Document draft 03 and a local server security tutorial
was added, both consistent with existing guidance. WebMCP replaced its unfinished same-origin
section with normative same-origin isolation, a two-sided cross-origin opt-in
(embedder `allow="tools"`, provider `exposedTo`, consumer `fromOrigins`), a
`Permissions-Policy: tools=()` mitigation, consequential/untrusted-content
annotations and agent-level guardrail guidance, and removed the declarative API
and the origin-keyed agent cluster requirement. The four agent-tools references
were rewritten to reflect those gates as specified behavior while keeping
confirmation prompts and agent guardrails as consumer responsibilities.
Sentry's new secret-serialization skill was adapted as a concept into the review
data reference, the implementation data reference and the audit coordinator's
seeded secret-discovery unit. Sentry's security-model consumption contract and
the update-tracking concepts of Awesome Copilot's threat-model-analyst were
adapted the same way; see the table above.

### Original runtime pentest skill — written 2026-09-22

`security-pentest` and its evaluation scenarios are original Apache-2.0 work.
They add authorized runtime testing, capability discovery, controlled evidence
collection and coverage reporting without adapting or vendoring upstream skill
text, code, documentation passages or payload catalogs. Conditional OWASP and
PortSwigger links are external further-reading references. Their inclusion does
not extend the older five skills' upstream derivation to this new skill.
Its [bundled provenance](skills/security-pentest/THIRD_PARTY_NOTICES.md) and the
canonical [Apache-2.0 text](licenses/Apache-2.0.txt) travel with the installation.

### Agent and tool security sources — checked 2026-09-12, re-pinned 2026-11-09

- [MCP snapshot](https://github.com/modelcontextprotocol/modelcontextprotocol/tree/394567887feccae8b3e27c7c84106edb5fbac116),
  SHA `394567887feccae8b3e27c7c84106edb5fbac116`: security best practices for
  protocol version 2026-07-28 plus authorization, transport and tools sections
  and the local server security tutorial.
  Reused in all four agent-tools references: caller/recipient binding, scoped
  authorization, token forwarding restrictions, untrusted tool content, sessions,
  local process and network boundaries. The [source license](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/394567887feccae8b3e27c7c84106edb5fbac116/LICENSE)
  explicitly describes a licensing transition: documentation excluding specs is
  CC-BY-4.0; new specification/code contributions are Apache-2.0; unconsented older
  contributions retain MIT. Preserve [the entire source notice](licenses/MCP-LICENSE.txt),
  not a blanket assertion that the whole source is MIT or Apache.
- [WebMCP snapshot](https://github.com/webmachinelearning/webmcp/tree/6cd745ac8a186122bd3f4aeaeb1d6cfa820251d2),
  SHA `6cd745ac8a186122bd3f4aeaeb1d6cfa820251d2`: security-privacy-questionnaire.md
  and index.bs security/privacy section. Reused in all four agent-tools references:
  tool metadata/output injection, over-parameterization, session context,
  application/backend parity, origin exposure and consequential actions.
  [Source license](https://github.com/webmachinelearning/webmcp/blob/6cd745ac8a186122bd3f4aeaeb1d6cfa820251d2/LICENSE.md):
  W3C Software and Document License (2023); retain [source declaration](licenses/WebMCP-LICENSE.txt)
  and [full terms](licenses/W3C-SOFTWARE-DOCUMENT.txt).

Original, phase-specific rewrites; no source implementation or attack payload was
copied. WebMCP's non-normative security discussion and unfinished proposals are
not represented as shipped browser guarantees. Source trees have no separate
NOTICE file. These new references preserve the collection's existing license
boundaries while retaining underlying CC-BY/MIT/Apache/W3C terms and attribution.

This documentation includes material derived from WebMCP Security and Privacy,
Copyright © 2026 World Wide Web Consortium and WebMCP Contributors. All Rights
Reserved. Distributed under the W3C Software and Document License, WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. Changes: condensed, reorganized by lifecycle phase and
distinguished draft recommendations from implementation evidence.

### Earlier adaptations

- Removed the authenticated-path exclusion: authenticated attackers can exploit IDOR.
- Replaced unconditional pattern flags with contextual exploitability checks.
- Replaced static vulnerable-package watchlists with current advisory/tool queries.
- Consolidated repeated categories and removed nonexistent reference pointers.
- Separated requirements, architectural threats, implementation hardening and confirmed findings.
- Added redaction before tool output, synthetic secret markers, and no automatic patches.
- Restricted implementation guidance to secure construction; no vulnerability-report mode.
- Reorganized technology guides into security concepts spanning data, backend,
  frontend and operation, preserving contextual checks against current docs.
- Added a separate whole-codebase audit coordinator without turning it into a
  dispatcher for the four lifecycle phases.
- Bundled skill-specific provenance and applicable license texts inside every
  installable skill, so installation does not depend on files outside its folder.

## Attribution and retained terms

Sentry: Copyright 2025 Functional Software, Inc. dba Sentry.
Reference material derives from the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/),
[OWASP Foundation](https://owasp.org/), under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
The original [Sentry reference notice](licenses/Sentry-reference-NOTICE.txt) is retained.
Our security-review Markdown is a modified synthesis distributed under CC BY-SA 4.0;
the original MIT/Apache notices also remain applicable to incorporated source material.

GitHub: Copyright GitHub, Inc. Full [MIT permission and disclaimer](licenses/GitHub-MIT.txt).

OpenAI: the two skill-local license files are identical Apache-2.0 texts;
the repository-root `LICENSE` does not exist at this SHA. Full
[Apache-2.0 terms](licenses/Apache-2.0.txt) are retained, including the upstream
license appendix verbatim (its bracketed sample copyright is license text).

Each adapted Markdown file carries a modification/provenance notice. Preserve
these notices and the applicable license files when redistributing individual skills.
Root legal texts are canonical; bundled copies are checked by the test suite.
See [LICENSE](LICENSE) for the file-level license boundary. Public availability
does not remove attribution or ShareAlike obligations.
