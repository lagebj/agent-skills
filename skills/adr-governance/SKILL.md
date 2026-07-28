---
name: adr-governance
description: Governs Architecture Decision Records by finding existing decisions, determining whether to follow, amend, supersede, reject, or create an ADR, and keeping implementation and durable documentation aligned. Use when work affects architecture, system boundaries, persistence, security, APIs, infrastructure, major dependencies, migration strategy, or another durable technical direction.
license: MIT
compatibility: Agent Skills standard; repository filesystem and Git access are required for repository changes.
metadata:
  owner: lagebj
  category: architecture-governance
---

# ADR Governance

Use this skill to govern architectural decisions before implementation turns an assumption into a permanent boundary.

An ADR records a decision and its rationale. It is not a design diary, issue tracker, implementation plan, or catalogue of architectural defects.

## Core contract

```text
Search before deciding.
Follow accepted decisions until they are deliberately changed.
Record durable decisions, not routine implementation detail.
Supersede history; do not erase it.
Ship the decision and the implementation together when practical.
Never invent architectural authority.
```

## Use this skill when

A task changes or decides any of the following:

- system or domain boundaries;
- ownership of shared business operations;
- public APIs, events, schemas, or compatibility guarantees;
- source-of-truth or persistence strategy;
- authentication, authorisation, tenancy, or security architecture;
- infrastructure, hosting, networking, deployment, or operational topology;
- major frameworks, databases, queues, identity providers, or other strategic dependencies;
- migration, deprecation, backward compatibility, or accepted residual risk;
- cross-cutting conventions that future implementation must follow;
- an existing ADR's applicability, status, consequences, or supersession.

## Do not create an ADR for

- a local implementation choice with no durable architectural consequence;
- routine dependency upgrades within an accepted strategy;
- bug fixes that restore already-decided behaviour;
- task breakdown, sequencing, or ownership;
- a specific implementation mismatch that exists now; use `architectural-residue-records`;
- a vulnerability or failed control; record the finding through the repository's security process;
- speculative alternatives with no decision.

## Load context selectively

Before deciding:

1. Read root and relevant nested agent instructions.
2. Find the repository's ADR location, naming, numbering, template, statuses, and index conventions.
3. Search titles and contents for related decisions, rejected alternatives, and constraints.
4. Read unresolved ARRs in the affected domain.
5. Inspect the current implementation, tests, public contracts, and relevant operations documentation.
6. Load only the references needed:
   - `references/classification-and-lifecycle.md`
   - `references/writing-and-supersession.md`
   - `references/review-and-verification.md`
7. Use `assets/ADR-template.md` only when the repository has no stronger template.

Do not impose this skill's filename or status conventions over established repository conventions.

## Decision classification

Classify the work before editing an ADR.

### Follow an existing ADR

Use the accepted ADR unchanged when it already covers the decision and the proposed implementation conforms to it.

Record no duplicate ADR. Link the implementation or PR to the existing decision where the repository normally does so.

### Amend an existing ADR

Amend only when adding factual clarification, implementation evidence, consequences discovered during delivery, or metadata that does not change the original decision.

Preserve a dated history entry when the repository supports history.

### Supersede an existing ADR

Create a new ADR and link both directions when the actual decision changes, including:

- selecting a different architecture;
- changing the authoritative source of truth;
- replacing a strategic dependency;
- changing a security or compatibility boundary;
- accepting consequences the original decision rejected;
- materially changing the migration strategy.

Do not rewrite an accepted historical decision to make it appear that the new direction was always intended.

### Create a new ADR

Create one when the repository is making a durable decision that future engineers and agents must understand to avoid reopening or contradicting it.

### Record no ADR

Record no ADR when the work is local, reversible, already governed, or purely operational without a durable architectural choice.

## Workflow

### 1. Discover repository conventions

Search for `ADR`, `architecture decision`, `decision record`, status headings, templates, indexes, and numbering. Derive conventions from active repository evidence.

### 2. Establish decision scope

Write a one-sentence decision question. Identify:

- the forces and constraints;
- affected boundaries and contracts;
- the authority making the decision;
- reversibility and migration cost;
- security and operational implications;
- existing decisions that constrain the choice.

If the question contains several independent choices, split them.

### 3. Search for prior decisions

Search by domain terms, technologies, boundary names, rejected alternatives, and consequences. Read the whole relevant ADR, not only its title.

Resolve apparent conflicts before implementation. A newer accepted ADR may supersede an older one even when links are incomplete; repair the links when evidence is clear.

### 4. Separate decision from residue and execution

Use this model:

```text
ADR: what direction is authoritative and why.
ARR: where the current system violates intended architecture.
Issue or plan: how and when implementation work will be delivered.
Code and migration: change the system.
Tests and evidence: prove the result.
```

A deliberate deferral or accepted risk is still a decision and belongs in an ADR. The mismatch that remains may also require an ARR.

### 5. Evaluate options proportionally

For non-trivial choices, record the viable alternatives and the specific reason each was not selected. Avoid ceremonial option lists where only one path is technically possible.

Assess:

- consistency and integrity;
- coupling and ownership;
- security and privacy;
- operational burden and failure recovery;
- migration and rollback;
- compatibility and user impact;
- future optionality;
- cost of reversal.

### 6. Write or update the ADR

Use repository conventions. When none exist, use `assets/ADR-template.md` and a filename such as:

```text
ADR-0001-use-shared-match-lifecycle-command.md
```

Use a title that states the decision, not the topic:

```text
Use one shared match lifecycle command
```

Avoid:

```text
Match lifecycle architecture
```

### 7. Align implementation and durable documentation

Update affected architecture docs, diagrams, API contracts, security documentation, migration docs, agent instructions, and ARRs. Remove or mark obsolete material rather than leaving two active truths.

### 8. Verify before completion

Check the ADR against implementation and tests. Confirm links, status, alternatives, consequences, migration, rollback, and follow-up records are accurate.

Do not mark a decision accepted, implemented, or superseded without repository evidence or the required authority.

## Status handling

Use repository-defined statuses. When none exist, prefer:

- `Proposed`: under review and not authoritative.
- `Accepted`: authoritative for new work.
- `Rejected`: considered and explicitly not selected.
- `Deprecated`: retained for history but no longer recommended.
- `Superseded`: replaced by a linked newer ADR.

Implementation state is separate from decision status. An accepted ADR may be only partially implemented; record that through implementation links, ARRs, or history rather than inventing a hybrid status.

## Common rationalizations

| Rationalization | Required response |
|---|---|
| "The change is obvious." | If it creates a durable boundary or costly reversal, record why it is obvious now. |
| "We can document it after implementation." | The decision must constrain implementation, not rationalise it afterward. |
| "There is already an ADR with a similar title." | Read it and determine whether it governs, conflicts, or must be superseded. |
| "Updating the old ADR is simpler." | Supersede when the decision changes; preserve historical truth. |
| "This is technical debt, not architecture." | Separate an existing mismatch into an ARR and any required direction into an ADR. |
| "The framework chose for us." | Record the decision only when adopting the framework or constraint is itself durable and consequential. |

## Red flags

- Implementation begins before related accepted ADRs are read.
- Two accepted ADRs prescribe incompatible active architectures.
- The ADR title names a topic rather than a decision.
- Alternatives are strawmen or lack repository-specific trade-offs.
- Consequences contain only benefits.
- A superseded ADR is edited to hide the former decision.
- Status claims exceed available authority or evidence.
- The ADR duplicates an issue, design document, or ARR.

## Verification checklist

Before completion:

- the relevant ADR set was searched and read;
- the work is correctly classified as follow, amend, supersede, create, or no ADR;
- ADR, ARR, finding, issue, and implementation responsibilities are distinct;
- repository conventions are followed;
- the decision question and authoritative direction are explicit;
- alternatives and trade-offs are credible;
- security, operations, migration, compatibility, and rollback are addressed where relevant;
- supersession links are bidirectional;
- implementation and durable documentation agree;
- required repository checks pass;
- no decision status or assurance was invented.

## Stop or escalate

Stop and report the limitation when:

- the decision authority is unavailable or ambiguous;
- active ADRs conflict and repository evidence cannot resolve precedence;
- the intended architecture cannot be established;
- required provider or runtime state is unavailable and changes the decision;
- accepting material risk requires authority not present in the task.

Do not silently choose an architecture merely to keep implementation moving.
