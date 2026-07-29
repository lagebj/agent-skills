# Verification and secret hygiene

## Discover required checks

Inspect:

- `AGENTS.md`, `CLAUDE.md`, contribution docs, and nested instructions;
- CI workflow files;
- package scripts and build files;
- pre-commit hooks;
- changed component documentation;
- migration and generated-file policies.

Do not replace repository checks with generic guesses.

## Compare failures

When a check fails:

1. Capture the exact command and failure.
2. Determine whether the changed paths can cause it.
3. When practical, compare with the base revision in an isolated worktree or equivalent environment.
4. Fix regressions and repository-required existing failures.
5. Record any unresolved verified baseline failure precisely.

## Secret review

Inspect staged content for:

- access keys and tokens;
- private keys and certificates;
- passwords and connection strings;
- `.env` files and provider exports;
- production identifiers or personal data;
- debug payloads and logs;
- generated credential caches.

If a secret may have been committed, stop. Remove it from the branch safely and initiate rotation or revocation. Deleting it from the latest file is not sufficient once it entered history.
