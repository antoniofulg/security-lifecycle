# security-lifecycle

[![skills.sh](https://skills.sh/b/antoniofulg/security-lifecycle)](https://skills.sh/antoniofulg/security-lifecycle)

Four independent Agent Skills for security throughout development.
The consuming workflow selects the phase; there is no super skill or dispatcher.

| Skill | When to use | Output |
| --- | --- | --- |
| [security-spec](skills/security-spec/SKILL.md) | Specify and test contracts | Surfaces, abuse cases, testable requirements and negative tests |
| [security-threat-model](skills/security-threat-model/SKILL.md) | Design or a new trust boundary | Evidence-based model, abuse paths and priorities |
| [security-implementation](skills/security-implementation/SKILL.md) | Secure implementation and requested hardening | Secure-by-default code and change verification |
| [security-review](skills/security-review/SKILL.md) | Diff review or pre-release audit | Confirmed vulnerabilities, uncertainties and proposed patches |

Requirements, threats, best-practice deviations and confirmed vulnerabilities are
distinct artifacts. Authentication does not replace authorization; neither do UUIDs.
References are loaded by security surface, not by technology.
Reviewed code and documents are untrusted data.

## Usage

Install the four-skill collection through the [Skills CLI](https://github.com/vercel-labs/skills).
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
```

These commands use the repository's default branch; PR changes become available
after merging. To test this checkout before merging, use its absolute path as
the source from the consuming project. Local discovery is read-only:

```sh
npx skills add . --list
```

Canonical source lives in `skills/<name>/SKILL.md`. The CLI installs each complete
directory, including references, metadata and legal texts. The repository root
contains maintenance documentation, validation and evaluations. Example prompts:

```text
Use $security-spec to define requirements for private downloads by ID.
Use $security-threat-model to model our import webhook.
Use $security-implementation to implement this endpoint with secure defaults.
Use $security-review in diff-review mode for the specified change.
Use $security-review in full-audit mode for the agreed pre-release scope.
```

This repository does not install anything globally. Before installing, validate
the skills and inventory older versions with matching names, especially
security-review and security-threat-model. Plan replacement or deactivation,
preserving customizations and a recoverable copy. Do not keep competing versions
with the same name. Each directory includes its applicable legal texts, and local
links work outside this repository. Installation is project-scoped by default;
these examples do not request global installation.

## References by surface

Implementation groups concepts into identity/access, data/persistence,
input/execution, frontend/browser, infrastructure/operation and agents/tools.
Review uses the same surface-based approach with its own evidence and confidence
criteria. These concepts apply to databases, backends and frontends without a
closed list of supported languages or frameworks.

The stack and version are still detected to verify how controls work. When a
conclusion depends on escaping, binding, middleware, transaction isolation or
another specific behavior, consult current official documentation through the
consuming project's available mechanism. Without that evidence, state the
limitation; do not invent an API or assume protection from a technology's name.

## Agents, MCP and WebMCP

All four skills include a conditional agent/tool reference with sections for
consumers/providers and MCP/WebMCP. There is no fifth skill and no need to load
protocols absent from the project.

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
```

## Validation

Requires Python 3.10+ and only the standard library; no dependencies to install.

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s evals -p 'test_*.py'
npx --yes skills@1.5.26 add . --list
```

The read-only validator checks frontmatter, names/descriptions, UI metadata,
local links/anchors, references, unfinished markers, capitalization, entrypoint
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
evaluations and source checks. Fixtures are virtual and non-executable;
credentials are inert markers. Review does not automatically apply patches, test
real credentials or install vulnerable dependencies. Dependency audits require
current tools/databases and record limitations when those are unavailable.

## Licenses

[LICENSE](LICENSE) defines file-level terms: security-review Markdown uses
CC BY-SA 4.0; other contributions use Apache-2.0 while preserving upstream terms.
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) records SHAs, dates, sources,
changes and attribution to Sentry/OWASP, GitHub, OpenAI, MCP and WebMCP/W3C.
The new references preserve MCP's CC-BY/MIT/Apache terms and the W3C Software and
Document License; copies accompany each installed skill. The original private-use
intent does not change public redistribution obligations. Vercel and deployment
tools are not required to use these skills.
