# Python boundaries

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Validate request data at entry and authorize resource access with verified actor
and tenant policy. A schema validator does not provide authorization or sanitize
SQL/HTML. Bind SQL values, constrain identifiers, use shell-free subprocess calls
with allowed arguments and constrain file destinations after resolution.
Use safe data formats/loaders for untrusted bytes and bound parsing/request work.
Return non-sensitive error messages; redact credentials and personal data before
logs or exception telemetry. Operator-owned fixed URLs are not user input unless
the surrounding flow proves influence. Detect the actual framework before reading
an overlay or choosing APIs.
