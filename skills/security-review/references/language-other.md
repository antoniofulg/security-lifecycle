# Other language branches

Modified synthesis of Sentry/OWASP and GitHub Awesome Copilot; CC BY-SA 4.0.
See [provenance](../../../THIRD_PARTY_NOTICES.md).

Read only the section matching scoped code. Confirm current framework defaults
and advisory data when needed; the patterns below only identify investigation leads.

## Java

Trace concatenated JDBC/ORM queries, XML parser configuration and untrusted object
deserialization with usable classes. Check Spring authorization matchers and
management endpoint exposure. A permitAll rule needs a sensitive reachable target.

## PHP

Trace superglobal values into SQL, include/file paths, eval, unserialize and
upload destinations. Determine the downstream effect of extract or loose
comparisons before reporting. Prepared values do not authorize object access.

## Go

Trace SQL concatenation, shell invocation, paths and outbound requests. Establish
production use of disabled certificate verification or attacker-triggered
resource exhaustion. math/rand matters for security tokens, not simulations.

## Ruby

Inspect interpolated ActiveRecord queries, dynamic dispatch and unsafe YAML/Marshal
loads. Strong parameters limit assignments but do not implement object/tenant
authorization. Establish attacker-controlled redirect destination and actual impact.

## Rust

Inspect unsafe invariants and untrusted parser/resource boundaries. unsafe, unwrap,
expect or arithmetic syntax alone is not a vulnerability. Confirm input that
breaks an invariant, causes relevant availability loss or reaches memory misuse.
Use current RustSec data for resolved dependencies.
