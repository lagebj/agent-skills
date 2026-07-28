---
name: architectural-residue-records
description: Identifies, records, contains, supersedes, and resolves specific mismatches between intended architecture and current implementation. Use when work exposes multiple sources of truth, duplicated domain behaviour, active legacy structures, staged migration residue, violated architectural boundaries, or an existing ARR.
license: MIT
compatibility: Agent Skills standard; repository filesystem access is required for implementation and verification work.
metadata:
  owner: lagebj
  category: architecture-governance
---

# Architectural Residue Records

Use this skill to identify, record, maintain, supersede, and resolve Architectural Residue Records (ARRs).

An ARR records an observable mismatch between the intended architecture and the current implementation. It does not make an architectural decision. Architectural decisions, including deliberate deferrals, belong in ADRs.

## Use this skill when

Use this skill when a task involves one or more of the following:

- multiple active sources of truth;
- duplicated business behaviour across routes, services, match types, clients, or persistence paths;
- route-specific implementations of a common operation;
- legacy structures that remain active after a replacement was introduced;
- temporary migration states that must not become permanent;
- architectural constraints that are currently violated;
- residue that must be contained while a staged migration proceeds;
- reviewing, changing, resolving, invalidating, or superseding an existing ARR;
- determining whether a finding belongs in an ARR, ADR, issue, or ordinary code change.

## Do not use this skill for

Do not create an ARR for:

- a normal bug with no architectural consequence;
- cosmetic inconsistency;
- a small local refactor that can be completed immediately;
- duplicated syntax that does not duplicate domain meaning;
- a feature request;
- a decision that has not yet been made;
- a deliberate architectural deferral, which belongs in an ADR;
- general technical debt without a specific architectural mismatch.

## Load context selectively

Before acting:

1. Read the repository's root and relevant nested agent instructions.
2. Read the repository's ADR conventions and ADRs affecting the domain.
3. Read existing unresolved, resolved, superseded, and invalidated ARRs affecting the domain.
4. Inspect the implementation and tests that demonstrate the residue.
5. Load only the references needed:
   - `references/classification-and-boundaries.md`
   - `references/lifecycle-and-history.md`
   - `references/resolution-and-verification.md`
6. Use `assets/ARR-template.md` only when creating a new ARR.

Do not create a catalogue, registry, generated index, schema, CI workflow, or validation framework unless the repository already requires one.

## Core distinction

Use this model:

```text
ARR describes an architectural mismatch that exists.
ADR records an architectural decision.
Implementation changes the system.
Tests and reconciliation prove the result.
```

A typical chain is:

```text
ARR -> ADR when a decision is required -> implementation -> verification -> ARR resolved
```

Not every ARR needs an ADR. Straightforward removal of residue may be implemented directly.

## Classification workflow

Classify the finding before writing anything.

### Create or update an ARR when

The mismatch:

- creates conflicting sources of truth;
- causes equivalent operations to diverge;
- weakens data integrity or historical integrity;
- repeatedly produces defects or inconsistent behaviour;
- blocks an intended architectural boundary;
- requires staged migration or explicit containment;
- is likely to be extended accidentally unless documented;
- remains after the current change cannot safely remove it.

### Create an ADR when

The repository must decide:

- which architecture to adopt;
- which source of truth will remain;
- whether to merge or retain parallel models;
- whether to accept residue for a defined reason;
- whether to defer a decision;
- which migration strategy or boundary becomes authoritative.

### Use an issue or implementation plan when

The direction is already decided and the remaining work is execution.

### Fix directly when

The residue is local, unambiguous, and can be removed completely in the current change without a meaningful architectural decision.

## ARR lifecycle

Use these states unless the repository defines stricter equivalents:

- `Identified`: observed but not fully verified.
- `Confirmed`: verified and understood as architectural residue.
- `Dispositioned`: a resolution direction has been chosen.
- `Resolved`: removed, contained by an accepted decision, or otherwise closed with evidence.
- `Superseded`: replaced by one or more newer ARRs because the meaning or scope changed materially.
- `Invalidated`: the original finding was incorrect or no longer describes the system.

State transitions update the existing ARR. Do not create a new ARR merely because its state changed.

## Update versus supersede

Treat confirmed ARRs as append-only architectural records.

Update the existing ARR for:

- state changes;
- dated history entries;
- new supporting evidence;
- links to ADRs, issues, pull requests, commits, or tests;
- containment updates that do not change the meaning;
- resolution evidence;
- minor factual corrections that preserve the original finding.

Create a new ARR and supersede the old one when:

- the original residue was materially misunderstood;
- the scope changes significantly;
- several ARRs are discovered to be one larger residue;
- one ARR splits into distinct architectural problems;
- the intended architecture changes;
- the original containment no longer applies;
- a resolved residue reappears in a materially different form.

Use explicit bidirectional links:

```text
ARR-0007: Superseded by ARR-0014
ARR-0014: Supersedes ARR-0007
```

Do not rewrite the original residue, intended architecture, initial evidence, or impact after confirmation. Add dated history instead.

## Creating an ARR

1. Search existing ARRs for the same underlying mismatch.
2. Confirm the finding from code, schema, tests, documentation, or runtime evidence.
3. Choose the next repository-consistent identifier.
4. Use a narrow title describing the mismatch, not the solution.
5. State the intended architecture without making an undecided design choice.
6. Record concrete evidence with file paths, model names, commands, or behavioural examples.
7. Explain the impact in operational and architectural terms.
8. Add immediate containment rules when the residue cannot be removed now.
9. Define objective resolution criteria.
10. Leave the disposition pending unless a decision already exists.
11. Link related ADRs and implementation work.
12. Add the record using the repository's normal documentation location.

Preferred filename pattern:

```text
ARR-0001-duplicate-player-position-representations.md
```

## Containment rules

Containment prevents residue from spreading before it is resolved.

Good containment is explicit and testable:

```text
Do not add new reads or writes to the legacy position fields.
All new match completion behaviour must use the shared command.
Do not add another opponent string field.
```

Avoid vague containment:

```text
Be careful.
Prefer the new model.
Clean this up later.
```

A staged migration may temporarily increase residue only when:

- the temporary state is necessary;
- the ARR documents the temporary mismatch;
- containment prevents further expansion;
- resolution criteria are explicit;
- the implementation leaves a clear next step.

## Working with existing ARRs

Before changing a domain:

1. Read related ADRs.
2. Read unresolved ARRs.
3. Respect containment rules.
4. Do not extend documented residue.
5. Update the ARR when evidence, disposition, implementation, or state changes.
6. Resolve only when every resolution criterion is verified.
7. Supersede rather than rewrite when the meaning changes.
8. Invalidate only when the original finding was wrong, not merely inconvenient.

## Resolution

An ARR may be resolved by:

- removing the duplicate or legacy implementation;
- establishing one authoritative source of truth;
- routing all callers through one owning operation;
- completing a staged migration;
- accepting the residue through an ADR with explicit consequences and containment;
- proving the mismatch no longer exists.

Resolution must include evidence such as:

- tests covering all callers;
- reconciliation checks;
- schema constraints;
- removed fields or code paths;
- migration results;
- import or architecture checks;
- linked pull request or commit;
- relevant ADR.

Do not mark an ARR resolved because implementation started.

## Centralisation principle

When residue concerns duplicated operations, apply:

```text
One business operation, one owning implementation, multiple adapters.
```

Routes, server actions, controllers, commands, background jobs, and UI entry points may adapt inputs and outputs. They must not independently reimplement common domain behaviour.

Before adding a new operation:

1. Search for an existing owner.
2. Extend the owner when behaviour is genuinely shared.
3. Add an adapter when transport or context differs.
4. Migrate existing callers.
5. Remove obsolete implementations.
6. Test the owner and every adapter boundary.

Do not centralise unrelated behaviour merely because the code looks similar.

## Verification checklist

Before finishing an ARR task:

- the finding was correctly classified;
- no duplicate ARR was created;
- ADR and ARR responsibilities remain distinct;
- original confirmed meaning was not rewritten;
- supersession links are bidirectional;
- containment is explicit;
- resolution criteria are objective;
- related code and documentation agree;
- state is supported by evidence;
- no significant new residue was introduced silently;
- repository lint, tests, type checks, build, and hygiene checks pass where applicable.

## Stop or escalate

Stop and report the limitation when:

- the intended architecture cannot be determined from repository evidence;
- two active ADRs conflict;
- an ARR would require inventing evidence;
- resolution requires an unavailable owner or external decision;
- the repository has incompatible ARR conventions that cannot be reconciled safely.

Do not invent an architectural decision to close an ARR.

## Common rationalizations

| Rationalization | Required response |
|---|---|
| "This is only technical debt." | Classify the concrete mismatch. If it can change behaviour, integrity, or future architecture, treat it as residue rather than a vague debt label. |
| "We can document it after the migration." | Record containment before the temporary state spreads. |
| "The implementation has started, so the ARR is resolved." | Resolution requires every recorded criterion and supporting evidence. |
| "A new ARR is cleaner than updating the old one." | Update state and history unless the meaning or scope changed materially. |
| "The ADR already explains this." | The ADR records the decision; the ARR records the implementation mismatch and its evidence. Keep both roles explicit. |

## Red flags

- The record proposes a solution while the architectural direction is undecided.
- The evidence contains no concrete paths, models, commands, tests, or runtime observations.
- Containment uses vague language that cannot be tested.
- A confirmed finding is rewritten instead of extended through history.
- An ARR is marked resolved while legacy callers, fields, or data paths remain active.
- A broad technical-debt catalogue is being created instead of a specific record.
