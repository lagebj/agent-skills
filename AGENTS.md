# AGENTS.md

This repository contains reusable Agent Skills. The canonical source for every skill is `skills/<skill-name>/`.

## Mandatory skill use

For every repository task:

1. Load `using-agent-skills`.
2. Invoke every matching domain skill.
3. Use `git-commit-branch-pr` for any change intended for commit or pull request.
4. Complete each invoked skill's verification checklist before reporting completion.

## Repository rules

- Commit skill source directories only. Do not commit ZIP files, tarballs, generated release bundles, or other archive artifacts.
- Keep each `SKILL.md` below 500 lines.
- Keep references one link deep from `SKILL.md`.
- Every skill directory name and frontmatter `name` must match and use lowercase kebab-case.
- Every description must state what the skill does and when it applies.
- Prefer process, checkpoints, and evidence over general advice.
- Include anti-rationalization, red flags, and verification criteria.
- Avoid duplicate guidance across skills. Link and compose instead.
- Preserve the distinction between ADRs, ARRs, security findings, implementation plans, and Git delivery.
- Do not add executable scripts inside a skill unless deterministic execution materially improves reliability.
- Never include secrets, credentials, private provider values, or repository-specific sensitive data.

## Required checks

After changing any source file:

```bash
python3 scripts/validate-skills.py
```

Review the complete Git diff before committing. Confirm that no archive artifact or generated runtime copy has entered the repository.

## Skill catalogue

- `using-agent-skills`: dispatch and orchestration.
- `adr-governance`: architecture decision governance.
- `architectural-residue-records`: architectural mismatch lifecycle.
- `application-security-engineering`: secure application and provider changes.
- `git-commit-branch-pr`: branch, commit, push, and PR delivery.
