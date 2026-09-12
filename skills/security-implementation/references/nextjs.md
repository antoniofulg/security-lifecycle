# Next.js

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Treat Route Handlers, API Routes and Server Actions as callable endpoints: validate
input and enforce identity plus object/tenant authorization at each data boundary.
Check middleware/proxy matcher coverage; do not make it the sole assumed policy.
Keep server credentials out of client imports/public-prefixed environment values.
Scope caches by authorization context or keep private responses out of shared
caches. Verify webhook signatures over original bytes, constrain forwarded/Host
headers and keep uploads outside publicly served executable paths.
Verify version-specific APIs against current official docs before implementation.
