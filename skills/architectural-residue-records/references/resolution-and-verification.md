# Resolution and verification

## Resolution paths

### Direct removal

Remove the obsolete or duplicate path and migrate all callers.

### Architectural decision

Link an ADR that chooses the authoritative architecture, then implement it.

### Accepted residue

An ADR may accept residue for a defined reason. The ARR may then be resolved only when the acceptance, consequences, containment, and review trigger are explicit.

### Supersession

Replace the record when the residue has been reframed materially.

### Invalidation

Close the record when investigation proves the mismatch did not exist.

## Evidence

Useful resolution evidence includes:

- schema migration and verified backfill;
- deleted legacy fields or code paths;
- one shared command or domain service used by all adapters;
- architecture or import-boundary tests;
- reconciliation command output;
- regression tests covering league, event, API, and UI callers;
- linked ADR;
- linked pull request or commit;
- updated agent and architecture documentation.

## Resolution criteria quality

Good:

```text
All match completion entry points call the shared completion command.
No route writes report, participation, goal, or assist records directly.
League and event adapter tests pass.
Legacy completion services are removed.
```

Weak:

```text
Code has been cleaned up.
Most callers use the new service.
Architecture is improved.
```

## Reopening

Do not reopen and rewrite a resolved ARR when materially different residue appears.

Create a new ARR and link it to the previous record when recurrence differs in scope, cause, or architecture.
