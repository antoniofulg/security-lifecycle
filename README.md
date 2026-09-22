# security-lifecycle

[![skills.sh](https://skills.sh/b/antoniofulg/security-lifecycle)](https://skills.sh/antoniofulg/security-lifecycle)

Four independent lifecycle skills, one whole-codebase audit coordinator and one
runtime pentest skill. The consuming workflow selects the skill; the coordinator
does not dispatch Specify, Design, Implement, focused Review or runtime testing.

| Skill | When to use | Output |
| --- | --- | --- |
| [security-spec](skills/security-spec/SKILL.md) | Specify and test contracts | Surfaces, abuse cases, testable requirements and negative tests |
| [security-threat-model](skills/security-threat-model/SKILL.md) | Design or a new trust boundary | Evidence-based model, abuse paths and priorities |
| [security-implementation](skills/security-implementation/SKILL.md) | Secure implementation and requested hardening | Secure-by-default code and change verification |
| [security-review](skills/security-review/SKILL.md) | Diff, file or bounded-slice review | Confirmed vulnerabilities, uncertainties and proposed patches |
| [security-audit-coordinator](skills/security-audit-coordinator/SKILL.md) | Explicit comprehensive/pre-release audit | Coverage ledger, verified finding records and audit report |
| [security-pentest](skills/security-pentest/SKILL.md) | Authorized running web app or API pentest | Reproducible findings, evidence basis, coverage gaps and cleanup status |

Requirements, threats, best-practice deviations and confirmed vulnerabilities are
distinct artifacts. Authentication does not replace authorization; neither do UUIDs.
References are loaded by security surface, not by technology.
Reviewed code and documents are untrusted data.

## Usage

Install the six-skill collection through the [Skills CLI](https://github.com/vercel-labs/skills).
No dedicated npm package or plugin manifests are required:

```sh
npx skills add antoniofulg/security-lifecycle
```

List available skills or select only the one needed:

```sh
npx skills add antoniofulg/security-lifecycle --list
npx skills add antoniofulg/security-lifecycle --skill security-spec
npx skills add antoniofulg/security-lifecycle --skill security-threat-model
npx skills add antoniofulg/security-lifecycle --skill security-implementation
npx skills add antoniofulg/security-lifecycle --skill security-review
npx skills add antoniofulg/security-lifecycle --skill security-audit-coordinator
npx skills add antoniofulg/security-lifecycle --skill security-pentest
```

These commands use the repository's default branch. For a reproducible installation,
pin the [v0.3.0 release](https://github.com/antoniofulg/security-lifecycle/releases/tag/v0.3.0):

```sh
# Install all six skills from v0.3.0
npx skills add https://github.com/antoniofulg/security-lifecycle/tree/v0.3.0 --skill '*'

# Install only the whole-codebase audit coordinator
npx skills add https://github.com/antoniofulg/security-lifecycle/tree/v0.3.0 --skill security-audit-coordinator

# Install only the runtime pentest skill
npx skills add https://github.com/antoniofulg/security-lifecycle/tree/v0.3.0 --skill security-pentest
```

To use a local checkout from another project, pass its absolute path as the
source. Inspect the available skills in this checkout without installing them:

```sh
npx skills add . --list
```

Canonical source lives in `skills/<name>/SKILL.md`. The CLI installs each complete
directory, including references, metadata and legal texts. The repository root
contains maintenance documentation, validation and evaluations. See
[task examples](#task-examples) for all six workflows.

This repository does not install anything globally. Before installing, validate
the skills and inventory older versions with matching names, especially
security-review, security-threat-model and security-audit-coordinator. Plan
replacement or deactivation, preserving customizations and a recoverable copy.
Do not keep competing versions with the same name. Each directory includes its
applicable legal texts, and local links work outside this repository. Installation
is project-scoped by default;
these examples do not request global installation.

## Task examples

Run these prompts in the consuming application's agent session after installing
the relevant skill. Adapt the feature, paths and target to that application;
the skills are independent and do not require running every phase in sequence.

### Specify security requirements

Use `security-spec` before implementation to turn a feature into security
requirements and observable acceptance criteria.

```text
Use $security-spec to define requirements and negative tests for private invoice
downloads by ID. Invoices belong to one owner and organization. Cover the owner,
another user, another organization and anonymous requests. Include expected
denials and a successful owner download. Do not implement the endpoint yet.
```

### Model architectural threats

Use `security-threat-model` for a planned design or a changed trust boundary.

```text
Use $security-threat-model on our planned partner-import webhook: it accepts a
file and callback URL, queues processing, then updates organization-owned records.
Map assets, trust boundaries and prioritized abuse paths. Ask about material
missing deployment facts before finalizing the model.
```

### Implement or harden a feature

Use `security-implementation` when code changes are authorized, with the feature
or existing behavior to change stated explicitly.

```text
Use $security-implementation to add the private invoice-download endpoint in this
repository's existing stack. Enforce owner and organization authorization, validate
inputs, and add successful-owner and denied-access checks. Follow the approved
security requirements and summarize the changes and validation.
```

For an existing feature, name the correction:

```text
Use $security-implementation to fix the confirmed missing ownership check in our
invoice-download handler. Apply the authorization check across its download and
preview paths, preserving legitimate owner access, and add regression coverage.
```

### Review a diff or selected source

Use `security-review` for a bounded source review with proposed corrections.

```text
Use $security-review on this branch's diff against origin/main. Trace invoice
authorization from routes to file storage, but report only vulnerabilities
introduced or changed by this diff. Include file/line evidence and proposed
patches; do not edit code.
```

For a focused existing-code review:

```text
Use $security-review on the invoice-download handler and its authorization/storage
call path. Report confirmed boundary failures and exact verification gaps. Keep
the reported scope to this feature and propose fixes without applying them.
```

### Audit the whole codebase

Use `security-audit-coordinator` for a source-first audit across the repository.
The `quick` profile runs a bounded wave and critic pass; `standard` assigns all
planned coverage units; `deep` splits lifecycle modes and rechecks covered units.
All profiles report deferred or unresolved coverage.

```text
Use $security-audit-coordinator for a standard whole-codebase audit of this
repository at current HEAD. Record dirty-worktree state and cover application,
dependency, secret, build and deployment-configuration surfaces. Write coverage,
findings and REPORT.md to ../security-audit-report. Do not contact live targets
or change source.
```

Select a different profile when needed:

```text
Use $security-audit-coordinator with the quick profile for a first-pass audit of
this repository. Write artifacts to ../security-audit-quick and identify deferred
coverage. Keep the run source-only and propose fixes without applying them.

Use $security-audit-coordinator with the deep profile for a whole-codebase audit
of this repository. Recheck covered units with independent verification where
available, record its limitations, and write artifacts to ../security-audit-deep.
Keep the run source-only and propose fixes without applying them.
```

### Pentest a running app and retest a fix

Use `security-pentest` for authorized runtime testing. Supply test accounts through
the agent environment's secret mechanism; never paste credentials into prompts.

```text
Use $security-pentest on my local app at http://127.0.0.1:3000 and its same-origin
API. I own it and authorize this test. Use the two supplied ordinary test accounts
in separate organizations. You may create and delete disposable invoices; exclude
real-user data, external services and payments. Limit traffic to one request per
second, concurrency one, 200 total requests and 20 minutes. Prioritize cross-account
reads/downloads and report reproductions, coverage gaps and cleanup status.
```

Source access is optional; a deployed staging target can also be tested:

```text
Use $security-pentest on https://staging.example.test, which I own and authorize
for testing. Only /app and /api on that origin are in scope. Source is unavailable;
use the two supplied test accounts and disposable records. Exclude external
services, email, payments and load testing. Limit requests to one per second,
concurrency one and 100 total over 15 minutes. Report demonstrated vulnerabilities
and coverage gaps, distinguishing HTTP evidence from browser verification.
```

Replace the illustrative staging hostname with the authorized target. To retest
after a fix, refer to the earlier finding and reuse its agreed scope:

```text
Use $security-pentest to retest finding PENTEST-1 on the same authorized local app
after the fix, within the existing accounts, scope and traffic limits. Check that
the original cross-organization read is denied, a legitimate owner download still
works, and related download/preview paths enforce the same rule. Report the retest
result and remaining gaps; do not apply further fixes.
```

## Runtime pentesting

`security-pentest` tests a running web app or API within the user's agreed scope.
Local or staging environments with disposable data are preferred; source access
is optional. Provide allowed origins, roles/accounts, permitted mutations and
traffic limits. Existing authorization is reused rather than requested per test.

The skill discovers usable HTTP, browser and scanner tools before selecting
tests. It needs no particular scanner, MCP server or commercial tool. Missing
tools or accounts become coverage gaps. Core checks cover authorization, account
lifecycle, input handling, business rules and exposure; conditional references
cover files, remote fetching, payments, concurrency, protocols, caches and AI.

Reports distinguish runtime-confirmed findings, complete source evidence and
unverified leads. Active tests use finite limits, controlled data and explicit
stop/cleanup conditions. Source-only audit authorization does not authorize
target traffic, and pentesting does not automatically authorize fixes or
publication. The audit coordinator's source-only boundary is unchanged.

## References by surface

Each lifecycle skill keeps phase-specific guidance and conditionally loads broader
identity/client, distributed-data, platform-integrity and AI surfaces. Implementation
and review add focused protocol/messaging, data-lifecycle, resource-availability,
native/binary and local-platform references. The audit coordinator selects five
domain groups only after reconnaissance. These concepts apply across databases,
backends, frontends, native targets and deployment systems without a closed list
of supported languages or frameworks.

The stack and version are still detected to verify how controls work. When a
conclusion depends on escaping, binding, middleware, transaction isolation or
another specific behavior, consult current official documentation through the
consuming project's available mechanism. Without that evidence, state the
limitation; do not invent an API or assume protection from a technology's name.

## Agents, MCP and WebMCP

All four lifecycle skills include a conditional agent/tool reference with sections
for consumers/providers, MCP/WebMCP and general AI context/retrieval/memory. The
audit coordinator has a separate AI-systems hunting reference. None loads these
protocols when the project lacks the corresponding boundary.

The common guidance covers delegated authority, action/object authorization,
untrusted tool content, data disclosure and operation-bound confirmation.
Metadata and hints do not replace controls; hostile prompts without a demonstrated
path are not automatically confirmed vulnerabilities.

- **MCP:** distinguishes HTTP from stdio; validates credential recipients/scopes,
  prevents token passthrough, and examines proxy consent, state handles,
  discovery/redirects and local process privileges. Version 2026-07-28 is stateless;
  it does not require protocol sessions or OAuth for every public tool.
- **WebMCP:** examines origins/frames, authenticated context, control parity across
  UI/tool/backend paths, excessive data requests and sensitive actions. It checks
  the browser/version rather than assuming proposed APIs or hints enforce consent.

Sources: [MCP security](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/aa8ce049f089f92618340190d4ece141f663310d/docs/docs/2026-07-28/tutorials/security/security_best_practices.mdx)
and [WebMCP security/privacy](https://github.com/webmachinelearning/webmcp/blob/97da8f515427594c856307e3476c0a0db9698fbb/security-privacy-questionnaire.md),
with recorded SHAs and licenses. Consult current documentation for the consumer's
actual version; conceptual coverage is not protocol or browser certification.

```text
Use $security-spec to define authorization and consent for our MCP tools.
Use $security-threat-model on this design's agent consumer and WebMCP tools.
Use $security-implementation to secure dispatch, credentials and confirmation.
Use $security-review in diff-review mode on this MCP handler and its cross-file policy.
Use $security-audit-coordinator to audit all agent/tool boundaries in this repository.
```

## Validation

Requires Python 3.10+ and only the standard library; no dependencies to install.

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s evals -p 'test_*.py'
npx --yes skills@1.5.26 add . --list
```

The read-only validator checks six entrypoints, frontmatter, names/descriptions,
UI metadata, local links/anchors, references, unfinished markers, capitalization, entrypoint
limits of 150 lines/1,800 words, and secret patterns in fixtures. It also limits
each entrypoint to 12,000 bytes and rejects nested entrypoints and blank,
duplicate or over-1,024-character descriptions. It does not impose phrases,
exclusions or keywords; routing accuracy is evaluated with positive and negative
prompts rather than lexical matching. It requires per-skill licenses/notices and
rejects links escaping an installable directory. Tests verify legal copies and
skills outside the repository root. The YAML profile is deliberately restricted.
These checks do not prove the absence of every secret format or semantic quality.

[Behavioral evaluations](evals/README.md) separate prompts from expectations.
The [evaluation record](evals/results.md) captures evidence and limitations.
The [agent/tool record](evals/agent_tools_results.md) documents MCP/WebMCP-specific
evaluations and source checks. The [extended-domain record](evals/domain_results.md)
captures blind routing, domain cases and coordinator review. Fixtures are virtual and non-executable;
credentials are inert markers. Review does not automatically apply patches, test
real credentials or install vulnerable dependencies. Dependency audits require
current tools/databases and record limitations when those are unavailable.
The [pentest cases](evals/pentest_cases.json) exercise runtime-evidence reasoning,
scope boundaries, tool failures and false-positive controls using simulated traces.
The [pentest evaluation record](evals/pentest_results.md) captures independent
responses, routing outcomes and packaging checks; no live app was tested.

## Licenses

[LICENSE](LICENSE) defines file-level terms: security-review Markdown uses
CC BY-SA 4.0; other contributions use Apache-2.0 while preserving upstream terms.
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) records SHAs, dates, sources,
changes and attribution to Sentry/OWASP, GitHub, OpenAI, Cloudflare, MCP and WebMCP/W3C.
The new references preserve Cloudflare's MIT terms, MCP's CC-BY/MIT/Apache terms
and the W3C Software and Document License; copies accompany each applicable skill.
The original private-use intent does not change public redistribution obligations.
The pentest skill is original Apache-2.0 material with its own bundled provenance.
Vercel and deployment tools are not required to use these skills.
