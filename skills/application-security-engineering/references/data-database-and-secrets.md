# Data, database and secrets

## Data minimisation

Collect, expose, log and retain only what is needed. Treat exports and logs as concentrated data stores.

## Database

Use least-privilege runtime and separate migration roles where possible. Prefer ORM or typed queries. Forbid SQL concatenation and unsafe raw methods. Use transactions, constraints and RLS for important invariants.

## Files and exports

Authorise generation and retrieval. Use private storage, safe names, content controls, expiry and audit. Protect spreadsheets from formula injection.

## Secrets

Never commit, log or expose secrets to clients. Separate environments. Use write-only or sensitive provider storage. Prefer workload identity. Maintain rotation and revocation procedures without storing values in documentation.
