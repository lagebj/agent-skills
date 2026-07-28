# Writing and supersession

## Write the decision first

A reader should understand the authoritative direction from the title and Decision section without reconstructing it from context.

Good title:

```text
Use a shared opponent identity with free-text ingestion
```

Weak title:

```text
Opponent model
```

## Preserve historical truth

After acceptance, avoid rewriting context, decision, rationale, or rejected alternatives to match later events. Add dated history and implementation evidence.

Correct a material error explicitly. Do not silently alter the record.

## Supersession

Create a new ADR when the authoritative direction changes. Link both directions.

Old ADR:

```markdown
## Status

Superseded

## Superseded by

- ADR-0042: Use one shared match lifecycle command
```

New ADR:

```markdown
## Supersedes

- ADR-0017: Keep separate league and event completion services
```

Partial supersession must state exactly which decision clauses remain authoritative.

## Consequences

Record operational and organisational consequences, not only code structure. Include ongoing ownership, failure modes, data migration, observability, provider configuration, and user impact when relevant.

## Alternatives

Record alternatives that were genuinely viable. Explain why they lost under current constraints. Avoid generic claims such as "too complex" without naming the complexity and its cost.
