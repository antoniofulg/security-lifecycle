# FastAPI

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Apply authentication through evidenced router/dependency boundaries and enforce
object/property authorization at resource access. Use narrow validated input and
response models; validation is not authorization. Verify token algorithms and
required issuer/audience/expiry claims. Bound multipart/body work, configure
host/proxy/CORS policy for actual deployment, and keep exception details private.
Authenticate WebSockets, check browser origin and cap messages/connections.
Public API documentation is a deployment choice, not automatically a vulnerability.
