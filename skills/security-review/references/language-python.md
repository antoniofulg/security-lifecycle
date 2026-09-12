# Python

Modified synthesis of Sentry/OWASP and GitHub Awesome Copilot; CC BY-SA 4.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Trace request fields, uploads and earlier untrusted database writes into raw SQL,
template source, unsafe markup, shell commands, object loaders, paths and URLs.
Inspect yaml loaders and versions instead of treating every load call as RCE.
Pydantic validates data shape; it is not SQL sanitization or object authorization.

Django/SQLAlchemy bound queries and ordinary template autoescaping are valid
counterevidence. Check route/decorator/dependency policy and query scoping across
files. requests.get(settings.INTERNAL_URL) alone is not SSRF if operators own the
setting and no attacker-controlled composition or redirect path is established.
MD5 checksums without a security purpose are not crypto findings.
