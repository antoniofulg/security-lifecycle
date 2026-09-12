# JavaScript and TypeScript boundaries

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

TypeScript types and assertions do not validate external data at runtime. Validate
shape, type, size and allowed values at ingress, including duplicate query values.
Keep authorization server-side and scope object access by verified identity/tenant.

For browsers, use text rendering and safe DOM construction; constrain dynamic URL
schemes/origins and validate postMessage origin, source and payload. Web Storage
is user-controlled and inappropriate for durable secrets. Avoid string-to-code
APIs and untrusted object deep merges. For servers, parameterize query values,
allowlist identifiers, avoid shell interpretation and bound outbound requests.
Redact headers, tokens and sensitive fields before logging; return safe errors.
