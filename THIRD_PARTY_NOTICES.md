# Third-party notices and provenance

Retrieved 2026-09-12 UTC. SHAs resolved from each repository's `main` using the
GitHub commits API before adaptation. Links below are immutable snapshots.
This is an original, condensed rewrite: examples, routing, contracts and
evaluation fixtures were newly written. No upstream skill is vendored wholesale.

| Source | Pinned commit | License checked in repository | Reused topics and destination |
| --- | --- | --- | --- |
| [Sentry security-review](https://github.com/getsentry/skills/tree/c2f99a5b04b4cd992ec3022d7c2c3e23e938d241/skills/security-review) | `c2f99a5b04b4cd992ec3022d7c2c3e23e938d241` | [Root Apache-2.0](https://github.com/getsentry/skills/blob/c2f99a5b04b4cd992ec3022d7c2c3e23e938d241/LICENSE); [specific reference CC BY-SA 4.0 notice](https://github.com/getsentry/skills/blob/c2f99a5b04b4cd992ec3022d7c2c3e23e938d241/skills/security-review/LICENSE) | Only security-review: research/report scope, source-to-sink evidence, confidence, framework protections, contextual severity, false-positive suppression, topic/JS/Python/Docker guidance. |
| [GitHub Awesome Copilot security-review](https://github.com/github/awesome-copilot/tree/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/security-review) | `7568a482ce2df38f8965ab5336a3220db796a4ba` | [MIT](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/LICENSE) | Only security-review: audit sequence, dependency and secret sections, cross-file second pass, finding fields, proposed patches, seven language families, CI/IaC. |
| [OpenAI security-best-practices](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices) | `49f948faa9258a0c61caceaf225e179651397431` | [Local Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices/LICENSE.txt) | Only security-implementation: stack selection, secure defaults, passive high-impact warnings, documented exceptions, isolated fixes and regression checks; React, Vue, Next.js, Express, jQuery, Django, Flask, FastAPI, Go; TLS/cookie context. |
| [OpenAI security-threat-model](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model) | `49f948faa9258a0c61caceaf225e179651397431` | [Local Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt) | Only security-threat-model: repository evidence, separate execution planes, assets, boundaries, capabilities, abuse paths, prioritization, material-assumption check-in and Mermaid. |

`security-spec`, structural validator and fixtures are original work based on the
requested behavioral contract. They do not combine Sentry and Copilot workflows.

## Studied files at the pinned commits

Sentry: SKILL.md; references/api-security.md, authentication.md, authorization.md,
business-logic.md, cryptography.md, csrf.md, data-protection.md, deserialization.md,
error-handling.md, file-security.md, injection.md, logging.md, misconfiguration.md,
modern-threats.md, ssrf.md, supply-chain.md, xss.md; languages/javascript.md,
languages/python.md; infrastructure/docker.md. These were condensed into the
review evidence/report contracts, three category references, three language
references and two infrastructure references.

Awesome Copilot: SKILL.md; references/language-patterns.md, report-format.md,
secret-patterns.md, vuln-categories.md and vulnerable-packages.md. The package
watchlist was studied only to replace it with current advisory lookup instructions.

OpenAI best practices: SKILL.md and all ten references: general JavaScript
frontend, React, Vue, jQuery, Next.js, Express, Django, Flask, FastAPI and Go.
These informed the implementation-only language/framework references.
OpenAI threat model: SKILL.md, references/prompt-template.md and
references/security-controls-and-assets.md informed its two references.

Recursive source-tree checks found no relevant NOTICE file for these four skills:
Sentry has none; the GitHub and OpenAI NOTICE files belong to unrelated skills.

## Changes from upstream

- Removed the authenticated-path exclusion: authenticated attackers can exploit IDOR.
- Replaced unconditional pattern flags with contextual exploitability checks.
- Replaced static vulnerable-package watchlists with current advisory/tool queries.
- Consolidated repeated categories and removed nonexistent reference pointers.
- Separated requirements, architectural threats, implementation hardening and confirmed findings.
- Added redaction before tool output, synthetic secret markers, and no automatic patches.
- Restricted implementation guidance to secure construction; no vulnerability-report mode.

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
See [LICENSE](LICENSE) for the file-level license boundary. Public availability
does not remove attribution or ShareAlike obligations.
