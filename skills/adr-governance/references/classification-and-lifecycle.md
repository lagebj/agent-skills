# Classification and lifecycle

## ADR

Records a durable architectural decision and why it is authoritative.

Examples:

- use one shared command for a business operation;
- use relational constraints as the authoritative integrity boundary;
- retain separate fixture tables while sharing domain capabilities;
- adopt a specific identity or deployment architecture;
- defer consolidation until a prerequisite exists;
- accept a residual risk until a defined review trigger.

## ARR

Records a specific mismatch between intended architecture and current implementation.

Examples:

- two active representations of the same domain fact;
- duplicated implementations of one business operation;
- legacy fields still influencing behaviour after replacement;
- active paths bypassing an accepted boundary.

## Issue or implementation plan

Tracks execution after direction is known.

## Design or specification

Describes a proposed system in more implementation detail than an ADR. It may evolve while the ADR remains the durable decision boundary.

## Lifecycle test

Ask:

1. Will future work need this rationale to avoid reopening the choice?
2. Does the choice create a durable boundary, dependency, or compatibility promise?
3. Is reversal expensive or risky?
4. Does it affect more than one local implementation detail?
5. Is there actual authority to make the decision?

Create an ADR when several answers are yes. Do not create one as ceremony.

## Status transitions

Typical transitions:

```text
Proposed -> Accepted
Proposed -> Rejected
Accepted -> Deprecated
Accepted -> Superseded
```

Do not use status to describe implementation progress. Link implementation evidence separately.
