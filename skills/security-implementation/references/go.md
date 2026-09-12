# Go

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Use explicit HTTP server time/header/body limits appropriate to the endpoint;
bound HTTP client time and response reads and close response bodies. Keep
diagnostics internal and trust forwarded headers only from known proxies.
Use html/template for HTML, parameterized SQL, constrained paths and shell-free
commands with validated arguments. Enforce object/tenant authorization separately
from parsing and login. Use crypto/rand for security tokens and an established
password hashing scheme. Preserve module checksum verification and verify current
APIs/advisories when choosing dependencies. Return safe errors and redact logs.
