# React

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Use JSX text escaping. Introduce raw HTML only for an explicit product need with
appropriate sanitization; disable raw HTML in Markdown rendering by default.
Validate dynamic URLs rather than relying on HTML escaping for URL safety.
Client route guards do not authorize API access. Keep credentials out of public
bundles and persistent client storage. Couple ambient-cookie mutations with CSRF
protection. Avoid caching user-specific responses in shared/service-worker caches.
