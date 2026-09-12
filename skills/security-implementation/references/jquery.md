# jQuery

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Use text/value setters for untrusted text. HTML-accepting setters, string-based
construction, parseHTML and load require a deliberate trusted/sanitized content
contract. Avoid influenced getScript, JSONP and script-typed AJAX destinations.
Escape dynamic selector fragments and reject untrusted deep merges. Keep server
authorization independent of DOM state. Check the actual installed version
against current support/advisory information when choosing implementation APIs.
