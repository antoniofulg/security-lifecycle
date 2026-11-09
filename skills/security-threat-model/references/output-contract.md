# Threat model output

Modified synthesis of OpenAI security-threat-model; Apache-2.0.
See [provenance](../THIRD_PARTY_NOTICES.md).

Deliver Markdown with:

- Scope, evidence snapshot and exclusions.
- System model grouped into runtime, CI/build/dev and tests.
- Assets/objectives and attacker capabilities/non-capabilities.
- Entry points and trust boundaries with file/line or confirmed-user evidence.
- Compact Mermaid data-flow diagram; label trust crossings and mark unknowns.
- Threat table: THREAT ID, actor, entrypoint, abuse path, asset, existing control
  and evidence, likelihood/reason, impact/reason, priority, linked assumption.
- Recommended mitigations: threat ID, owner component/boundary, change and
  verification idea. Keep recommendations separate from existing controls.
- Validated assumptions, unresolved questions, conditional rankings and coverage.

Use paths and line numbers when the repository provides them; cite a design
paragraph when there is no implementation. Do not manufacture code evidence.
Mark a draft as provisional when a material user answer is pending.
Trace each discovered boundary to a threat or a documented reason for exclusion.

## Updating a prior model

When the user supplies a prior model and a baseline revision, pin baseline and
target. Keep every prior THREAT ID; continue numbering for new threats and never
reuse a retired ID. Reclassify each prior threat against current evidence as
present, mitigated (cite the change), partially mitigated, removed with its
component, or new. Verify a threat found in unchanged code against the baseline
revision before calling it pre-existing. Regenerate carried-forward entries from
current paths rather than copying prose. Where current evidence contradicts a
prior ranking or classification, keep the prior value in the table and list the
disagreement under unresolved questions. Summarize counts by status and state the
direction of change with its reason.

A diagram should clarify the actual system; for an archive webhook the useful
edges might be external sender → ingress → queue → parser → storage and worker
→ remote URL, provided those components are evidenced. Do not introduce a queue
or worker merely because this example mentions one.
