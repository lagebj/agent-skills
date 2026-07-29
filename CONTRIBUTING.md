# Contributing

## Add or change a skill

1. Create a branch using `git-branch-commit-pr`.
2. Search existing skills to avoid overlapping ownership.
3. Create or edit `skills/<name>/` only.
4. Keep the main workflow under 500 lines and use direct references for detail.
5. Add or update realistic scenarios under `evals/`.
6. Validate:

   ```bash
   python3 scripts/validate-skills.py
   ```

7. Review the complete diff, including untracked files.
8. Confirm that no ZIP file, tarball, release bundle, generated runtime copy, secret, or local state is included.
9. Commit with a Conventional Commit and open a PR.

## Review criteria

A contribution must be:

- specific enough to trigger correctly;
- procedural rather than advisory;
- safe under ambiguous repository state;
- explicit about evidence and failure;
- composable with existing skills;
- free of secrets and environment-specific private data;
- accompanied by validation and relevant evaluation updates;
- source-only, with no generated archive artifacts committed.

## Versioning

Use semantic versioning for repository releases. Skill content changes are versioned with the repository until independent skill versioning becomes necessary.
