# Identity, authorisation and tenancy

## Authentication

Authentication establishes identity. It does not grant resource authority.

Verify provider issuer, audience, redirect, state and nonce through established libraries. Keep sessions secure and revocable.

## Authorisation

Deny by default. Evaluate actor, action, resource, current state and ownership server-side.

Do not trust IDs, slugs, hidden fields or client roles.

Centralise policies and add negative tests for every sensitive operation.

## Tenancy

Use multiple layers:

- trusted tenant context;
- tenant-scoped commands and repositories;
- tenant-consistent constraints;
- RLS where appropriate;
- tenant-aware caches, artifacts and jobs;
- cross-tenant negative tests.

Test with the real runtime database role and connection-pool path.

## Machine identity

Keep machine principals separate from human users. Use short-lived, audience-bound, scoped credentials. Prevent tenant switching and impersonation. Add revocation and audit.
