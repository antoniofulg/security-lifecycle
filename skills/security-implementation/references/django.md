# Django

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Retain authentication and CSRF middleware; enforce object/tenant restrictions in
querysets and permission checks. Use ORM parameter binding and escaped templates;
raw SQL and safe-markup bypasses require separate handling. Production settings
need debug off, allowed hosts, an external signing key and verified proxy trust.
Separate uploaded media from static/application code and use safe redirects.
Run deployment checks against the intended settings when authorized; preserve
explicit local HTTP exceptions without weakening production cookies.
