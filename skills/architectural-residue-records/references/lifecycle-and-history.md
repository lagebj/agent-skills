# Lifecycle and history

## States

### Identified

Observed, but verification or impact analysis is incomplete.

### Confirmed

Verified from implementation evidence. The original description, intended architecture, evidence, and impact become historically stable.

### Dispositioned

A direction exists:

- resolve directly;
- resolve through a linked ADR;
- accept through a linked ADR;
- invalidate after investigation;
- supersede with a more accurate ARR.

### Resolved

The residue is removed or explicitly accepted through an architectural decision, and resolution evidence satisfies the recorded criteria.

### Superseded

The record's meaning or scope was replaced by one or more newer ARRs.

### Invalidated

The original finding was incorrect or did not represent architectural residue.

## Append-only history

After confirmation, preserve the original finding. Record developments in dated history entries.

Example:

```markdown
## History

### 2026-07-19

Residue confirmed.

### 2026-08-04

ADR-0031 selected a shared match lifecycle command.

### 2026-09-12

Resolved by PR #184. Reconciliation and route-adapter tests pass.
```

## Supersession

Supersede when meaning changes, not when status changes.

Old record:

```markdown
## State

Superseded

## Superseded by

- ARR-0014: Fragmented match lifecycle ownership
```

New record:

```markdown
## Supersedes

- ARR-0007: Duplicate match completion workflows
- ARR-0009: Divergent event match reporting
```

## Invalidated versus superseded

Use `Invalidated` when the original claim was wrong.

Use `Superseded` when the original claim had value but a newer record describes the residue more accurately.
