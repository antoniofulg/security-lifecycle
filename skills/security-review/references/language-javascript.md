# JavaScript and TypeScript

Modified synthesis of Sentry/OWASP and GitHub Awesome Copilot; CC BY-SA 4.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Trace raw HTML, dynamic URLs, eval/Function, shell calls, query construction,
outbound fetches, filesystem paths and object merges from actual input sources.
Runtime validation must exist independently of static types and type assertions.

React JSX and Vue interpolation normally escape text; confirm bypasses before
reporting XSS. ORM parameterization blocks value SQLi, not authorization failures.
Prototype pollution needs controlled keys, a reachable merge and consequential use.
Express middleware order and Next.js endpoint/action authorization need cross-file
inspection; do not assume all routes share one guard. Review WebSocket identity,
origin and message limits when present. Consult version-specific official docs
when a framework default determines whether the path is exploitable.
