# License and provenance

Copyright 2026 security-lifecycle contributors. Modified documentation under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode);
see [LICENSE](LICENSE). Sources and licenses checked on 2026-09-12; Sentry, MCP
and WebMCP re-checked on 2026-11-09.

## Sentry and OWASP

[Source snapshot](https://github.com/getsentry/skills/tree/e94f22214528d69899d09c627b3315ddc3544816/skills/security-review),
commit `e94f22214528d69899d09c627b3315ddc3544816`.
Copyright 2025 Functional Software, Inc. dba Sentry.
Reference material derives from the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
and [OWASP Foundation](https://owasp.org/), licensed CC BY-SA 4.0.

The [specific source notice](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/skills/security-review/LICENSE)
is preserved [locally](licenses/Sentry-reference-NOTICE.txt). Sentry's root Apache-2.0
license is preserved as [full terms](licenses/Apache-2.0.txt).
Reused principles: researched versus reported scope, source-to-sink evidence,
confidence, contextual severity and suppression of false positives.
Topic, language and container material was consolidated into surface-based guidance.

## Sentry secret-serialization

[Source snapshot](https://github.com/getsentry/skills/tree/473d2594cd91c96ac8348f297e016b631e842487/skills/secret-serialization),
commit `473d2594cd91c96ac8348f297e016b631e842487`, checked 2026-11-09. Copyright Functional
Software, Inc. dba Sentry; licensed under Sentry's root Apache-2.0, preserved as
[full terms](licenses/Apache-2.0.txt). Reused concept: credential-bearing fields on
auto-serializing types, wholesale serialization sinks, partial exclusion of
generated paths and raw attribute access. No table, example or finding format
was copied; the review Markdown remains CC BY-SA 4.0 with Apache-2.0 terms retained.

## Sentry security-model

[Source snapshot](https://github.com/getsentry/skills/tree/2960faf806231e253302a410b9e97e7682aa8b64/skills/security-model),
commit `2960faf806231e253302a410b9e97e7682aa8b64`, checked 2026-11-09. Copyright Functional
Software, Inc. dba Sentry; Apache-2.0 ([full terms](licenses/Apache-2.0.txt)).
Upstream adapts `define-security-policy` from openai/codex-security, also
Apache-2.0. Reused concept: a repository security policy as untrusted scope
evidence read at the base revision, enforced versus monitored controls and
exclusion matching. Excluded findings are reported here, not suppressed. No text
was copied; the review Markdown remains CC BY-SA 4.0.

## Cloudflare security-audit

[Source snapshot](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit),
commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`, checked 2026-09-19.
Copyright (c) 2025-2026 Cloudflare, Inc.; source licensed MIT with the
[full permission and disclaimer](licenses/Cloudflare-MIT.txt).

Reused topics: identity/HTTP protocols, RPC/messaging, data lifecycle, resource
availability, native/binary and local-platform attack surfaces plus broader AI,
browser, release and cloud review. Changes: original condensed review guidance,
static evidence retained as sufficient for complete paths, and whole-codebase
orchestration moved to a separate skill. No source prompt or schema was copied.

## GitHub Awesome Copilot

[Source snapshot](https://github.com/github/awesome-copilot/tree/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/security-review),
commit `7568a482ce2df38f8965ab5336a3220db796a4ba`. Copyright GitHub, Inc.
[Source MIT license](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/LICENSE);
[full permission and disclaimer](licenses/GitHub-MIT.txt).

Reused principles: scope, dependencies, secrets, cross-file scan, self-verification,
severity/confidence reporting and proposed patches. Language patterns were
reorganized by surface; the static package watchlist was replaced by live queries.

## Changes and redistribution

Original condensed synthesis. Removed authenticated-path exclusions and unconditional
flags; separated hardening/uncertainty from confirmed findings. Added safe secret
handling and exact source-location verification. Technology defaults are verified
on demand instead of stored as separate language/framework guides.

No relevant upstream NOTICE file exists beyond the retained Sentry reference notice.
Preserve this attribution, modification notice and bundled license texts with
redistributed copies; ShareAlike applies to adapted review documentation.

## Agent and tool sources

Modified original synthesis, checked 2026-11-09:

- [MCP security best practices, 2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/394567887feccae8b3e27c7c84106edb5fbac116/docs/docs/2026-07-28/tutorials/security/security_best_practices.mdx),
  SHA `394567887feccae8b3e27c7c84106edb5fbac116`, with related authorization,
  transport and tools specification sections and the local server security
  tutorial added upstream in 2026-10. Copyright (c) 2024-2025 Model
  Context Protocol a Series of LF Projects, LLC. Documentation: CC-BY-4.0;
  specification contributions: Apache-2.0 or retained MIT as described by the
  [full source licensing notice](licenses/MCP-LICENSE.txt).
- [WebMCP security questionnaire](https://github.com/webmachinelearning/webmcp/blob/6cd745ac8a186122bd3f4aeaeb1d6cfa820251d2/security-privacy-questionnaire.md)
  and index.bs security/privacy discussion, SHA
  `6cd745ac8a186122bd3f4aeaeb1d6cfa820251d2`, including the same-origin
  isolation, two-sided cross-origin opt-in and Permissions Policy sections.
  [Source declaration](licenses/WebMCP-LICENSE.txt);
  [W3C Software and Document License, full terms](licenses/W3C-SOFTWARE-DOCUMENT.txt).

Reused topics: tool authority, recipient/scope/session binding, untrusted tool
content, information disclosure, browser origins and consequential actions.
Changes: concise phase-specific guidance, no copied implementation, clear
separation of protocol requirements, application recommendations and unverified
browser behavior. No separate upstream NOTICE files were found.

This document includes material derived from WebMCP Security and Privacy.
Copyright © 2026 World Wide Web Consortium and WebMCP Contributors. All Rights
Reserved. Distributed under the W3C Software and Document License, WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. Preserve the bundled terms and attribution.
