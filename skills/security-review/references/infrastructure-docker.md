# Container context

Modified synthesis of Sentry/OWASP and GitHub Awesome Copilot; CC BY-SA 4.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Check effective USER across stages and runtime overrides, capabilities, writable
mounts, host access, exposed ports and credential-bearing ARG/ENV/COPY layers.
Inspect the final image stage; build-stage root is not automatically runtime root.

Root without a concrete escalation/impact path is a hardening deviation, not an
automatic Critical finding. If an existing file-write/RCE path combines with a
privileged mount, explain the combined blast radius and avoid duplicate findings.
A non-root USER alone does not prove isolation.

Trace copied secrets through layers and build logs with redacted output. Review
base-image vulnerabilities using current advisories and actual image resolution;
a tag's age is not a vulnerability. Do not build untrusted Dockerfiles during audit.
