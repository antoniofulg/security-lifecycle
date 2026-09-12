# Flask

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Keep debugger and development server out of production. Store signing keys
externally; default signed sessions are readable, so keep sensitive data out.
Retain Jinja escaping and avoid user-controlled template source. Protect ambient
cookie mutations against CSRF. Set body/form limits and precise host/proxy trust.
Use server-generated upload names inside controlled storage and authorize access.
Centralize safe errors/redaction and parameterize database calls.
