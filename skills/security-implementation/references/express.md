# Express

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Validate params/query/body at runtime, including arrays where scalars are expected.
Bound body parsers and uploads; apply authorization before resource reads/writes.
Configure proxy trust to the known topology, not an arbitrary forwarded header.
Use production session storage, rotate identity sessions after privilege changes
and protect cookie-authenticated mutations against CSRF. Parameterize SQL; avoid
passing raw user objects to query operators. Constrain templates, file roots,
redirects, commands and outbound destinations. Centralize safe error responses
and redact sensitive request metadata before logging.
