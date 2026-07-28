# Classification and boundaries

## ARR

An Architectural Residue Record describes a specific mismatch between intended architecture and current implementation.

Examples:

- two active representations of player positions;
- league and event routes implementing the same match completion rules separately;
- canonical opponent identity coexisting with independent free-text identities;
- route handlers containing rating calculations that should be shared;
- active JSON relationships that bypass required relational constraints;
- legacy policy fields still influencing current behaviour.

## ADR

An Architecture Decision Record describes a decision and its rationale.

Examples:

- choose one shared match lifecycle command with league and event adapters;
- retain separate fixture tables while sharing domain capabilities;
- accept a legacy field until a defined migration boundary;
- defer consolidation until a prerequisite is complete.

A deliberate deferral remains an ADR because it is a decision.

## Issue or implementation plan

Tracks execution after direction is known.

Examples:

- migrate all event reports to the shared completion command;
- remove legacy position columns;
- add reconciliation tests;
- backfill canonical opponent references.

## Direct refactor

Use a normal code change when the architectural mismatch can be removed completely and safely without a meaningful design choice or staged migration.

## Test

Ask these questions:

1. Does something architectural exist in two conflicting forms?
2. Can the mismatch alter business behaviour or integrity?
3. Will future work likely extend it accidentally?
4. Does removal require migration, containment, or a decision?
5. Is the finding specific enough to verify?

If most answers are no, do not create an ARR.
