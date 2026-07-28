# Review and verification

## Review questions

- Does an existing accepted ADR already govern this change?
- Is the decision narrow enough to remain coherent?
- Are the constraints grounded in repository or provider evidence?
- Is the selected direction explicit and testable?
- Are alternatives credible?
- Are negative consequences and risks visible?
- Are migration, compatibility, rollback, and operations addressed?
- Are related ARRs and security findings linked?
- Does implementation conform to the decision?

## Evidence

Useful implementation evidence includes:

- architecture or import-boundary tests;
- schema constraints and migration verification;
- contract tests across adapters;
- deleted obsolete paths;
- provider configuration evidence;
- rollout and rollback records;
- linked pull requests or commits;
- updated diagrams and operating documentation.

## Conflict handling

When two accepted ADRs conflict:

1. Check dates, supersession links, and scope.
2. Check whether one is more specific to the affected domain.
3. Inspect implementation and later records for evidence of accepted precedence.
4. Repair missing links only when evidence is clear.
5. Otherwise stop and require an explicit governance decision.
