# Skill orchestration

The skills are orthogonal controls around repository change.

```text
                         +----------------------+
                         | using-agent-skills   |
                         +----------+-----------+
                                    |
             +----------------------+----------------------+
             |                      |                      |
      +------v------+       +-------v--------+     +-------v--------+
      | ADR         |       | ARR            |     | Application    |
      | governance  |       | governance     |     | security       |
      +------+------+       +-------+--------+     +-------+--------+
             |                      |                      |
             +----------------------+----------------------+
                                    |
                         +----------v-----------+
                         | Git branch/commit/PR |
                         +----------------------+
```

## Ownership boundaries

### ADR governance

Owns authoritative direction, rationale, alternatives, consequences, status, and supersession.

### ARR governance

Owns evidence of a current architectural mismatch, containment, lifecycle, and objective resolution criteria.

### Application security

Owns actors, assets, trust boundaries, threats, controls, negative tests, provider verification, and residual risk evidence.

### Git delivery

Owns worktree safety, branching, intentional staging, repository checks, commit structure, push, PR evidence, and delivery reporting.

## Composition examples

### A duplicated authorisation path

- ARR records duplicated policy ownership and containment.
- ADR is required only if the authoritative owner is undecided.
- Application security defines deny-by-default behaviour and negative tests.
- Git delivery isolates and ships the verified consolidation.

### A deliberate legacy-field deferral

- ADR records the decision to defer removal, its reason, consequences, review trigger, and migration boundary.
- ARR records the active mismatch and containment while it remains.
- Git delivery links both records from the implementation PR.

### A dependency upgrade

- No ADR when the upgrade remains within an accepted dependency strategy.
- Application security applies when the upgrade addresses a vulnerability or changes trust boundaries.
- Git delivery runs repository checks and creates the PR.
