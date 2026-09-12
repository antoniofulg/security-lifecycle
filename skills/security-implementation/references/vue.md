# Vue

Modified synthesis of OpenAI security-best-practices; Apache-2.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Use escaped interpolation. Treat v-html and untrusted templates as separate trust
boundaries; avoid compiling user-controlled templates. Mount into a controlled
root, constrain dynamic URL/style values and serialize SSR state safely.
Router guards are presentation logic; authorize every server object operation.
Keep secrets out of client builds and avoid shared caches for private state.
