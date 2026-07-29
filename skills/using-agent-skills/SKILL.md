---
name: using-agent-skills
description: Discovers and composes this repository's governance, security, architecture-residue, and Git delivery skills. Use when starting repository work, deciding which skill applies, or handling a task that crosses architecture, security, migration, and pull-request boundaries.
license: MIT
compatibility: Agent Skills standard.
metadata:
  owner: lagebj
  category: orchestration
---

# Using Agent Skills

Use this dispatcher to select every applicable skill before implementation.

## Skill map

| Signal | Required skill |
|---|---|
| Durable architectural direction, boundaries, strategic dependencies, migration strategy, accepted risk, or an existing ADR | `adr-governance` |
| Current implementation conflicts with intended architecture, multiple sources of truth, duplicated domain behaviour, active legacy paths, or an existing ARR | `architectural-residue-records` |
| Authentication, authorisation, tenancy, APIs, data, secrets, browser controls, integrations, dependencies, provider controls, or security findings | `application-security-engineering` |
| Any repository work intended for branch, commit, push, or pull request | `git-branch-commit-pr` |

## Composition rules

Use all matching skills. They own different questions:

```text
ADR governance: What direction is authoritative and why?
ARR governance: Where does the implementation violate intended architecture?
Application security: Which trust boundaries and controls make the change safe?
Git delivery: How is the verified change isolated, committed, pushed, and reviewed?
```

Do not force one skill to absorb another's record type.

## Typical sequences

### Architecture-affecting feature

1. `git-branch-commit-pr` to inspect state and create the branch.
2. `adr-governance` to discover or record the governing decision.
3. `application-security-engineering` when security boundaries are affected.
4. Implement and verify.
5. `git-branch-commit-pr` to review, commit, push, and open the PR.

### Resolving architectural residue

1. `git-branch-commit-pr` to isolate the work.
2. `architectural-residue-records` to read containment and resolution criteria.
3. `adr-governance` only when a new direction or accepted deferral is required.
4. `application-security-engineering` when the residue affects trust, data, identity, or operations.
5. Implement, prove criteria, update records, and ship through `git-branch-commit-pr`.

### Security hardening

1. `git-branch-commit-pr` to isolate the work.
2. `application-security-engineering` to model threats and controls.
3. `adr-governance` for durable security architecture or accepted risk.
4. `architectural-residue-records` when an existing structural mismatch remains.
5. Verify negative paths and provider state, then ship.

## Shared operating rules

- Read repository instructions before acting.
- Search existing durable records before creating new ones.
- Prefer shared owners over route-specific logic.
- Preserve existing work and historical truth.
- Use progressive disclosure; read only relevant references.
- Never claim tests, provider settings, pushes, PRs, decisions, or assurance without evidence.
- Stop when required authority or material evidence is missing.

## Anti-rationalization

| Rationalization | Required response |
|---|---|
| "The task is too small for a skill." | Check the trigger conditions. Size does not remove architecture, security, or delivery risk. |
| "I will load skills after exploring." | Skill workflows define how exploration must occur. Select them first. |
| "One skill is close enough." | Compose skills when the task crosses record types or lifecycle phases. |
| "The repository has no formal process." | Derive conventions from evidence and use the skill defaults only where gaps remain. |

## Red flags

- Repository work begins without checking which skills apply.
- One skill is used to cover a concern owned by another skill.
- A task crosses architecture, security, residue, and delivery boundaries but only one workflow is loaded.
- A result is claimed without completing the verification gates of every invoked skill.

## Verification

Before implementation, name the applicable skills and execute their entry steps. Before completion, satisfy each invoked skill's verification checklist and report unresolved gates explicitly.
