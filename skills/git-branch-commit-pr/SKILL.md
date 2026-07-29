---
name: git-branch-commit-pr
description: Safely carries repository work from branch creation through intentional staging, required verification, Conventional Commits, push, and GitHub pull-request creation. Use when modifying a Git repository, or when the user asks to branch, commit, push, open a PR, prepare changes for review, or complete repository delivery.
license: MIT
compatibility: Agent Skills standard; requires Git and uses GitHub CLI when GitHub pull-request creation is requested.
metadata:
  owner: lagebj
  category: delivery
---

# Git Commit, Branch, and Pull Request

Use this skill as the delivery envelope for repository changes. Invoke it before edits when possible, then complete its final stages after implementation and verification.

## Core contract

```text
Protect existing work.
Never commit directly to the protected default branch.
Branch from the correct base.
Stage intentionally.
Verify before claiming readiness.
Use coherent Conventional Commits.
Open a reviewable PR with evidence.
Never invent test, push, or PR results.
```

## Use this skill when

- any repository change is intended to be committed;
- starting implementation that should occur on a feature branch;
- preparing, reviewing, splitting, or amending commits;
- pushing a branch;
- creating or updating a GitHub pull request;
- reporting delivery evidence after code changes.

## Load context selectively

Before changing Git state:

1. Read root and relevant nested agent instructions.
2. Read contribution, branch, commit, PR, release, and CI documentation.
3. Inspect repository status, remotes, default branch, current branch, upstream, and recent history.
4. Identify repository-required checks and generated-file policies.
5. Load references as needed:
   - `references/branch-and-worktree-safety.md`
   - `references/commit-and-pr-format.md`
   - `references/verification-and-secret-hygiene.md`
6. Use `assets/pull-request-template.md` when the repository has no stronger template.

Repository instructions override this skill's default naming and formatting conventions.

## Workflow

### 1. Inspect before acting

Run equivalent checks for:

```bash
git status --short --branch
git remote -v
git branch --show-current
git log --oneline --decorate -n 12
```

Determine the remote default branch from repository evidence, for example:

```bash
git symbolic-ref --quiet --short refs/remotes/origin/HEAD
```

Do not assume it is `main`.

Inspect tracked, untracked, and relevant ignored files. Identify intended changes, unrelated user work, generated files, local configuration, and possible secrets.

### 2. Protect existing work

Never discard, overwrite, reset, clean, or stash work merely to simplify the workflow.

- Preserve unrelated modifications.
- Do not include unrelated files in the commit.
- Do not run destructive commands such as `git reset --hard`, `git clean -fd`, or forced checkout without explicit authority and verified safety.
- Do not rewrite shared history.
- Do not use `git push --force`; use `--force-with-lease` only when history rewriting is explicitly required and safe.

If the current worktree cannot be isolated safely, stop and report the exact conflict.

### 3. Establish the correct branch

Before implementation, fetch the remote and create a new branch from the correct updated base.

Default branch format:

```text
<type>/<short-kebab-description>
```

Preferred types:

- `feat`
- `fix`
- `security`
- `refactor`
- `docs`
- `test`
- `perf`
- `ci`
- `build`
- `chore`

Examples:

```text
feat/add-opponent-history
security/harden-session-authorisation
refactor/centralise-match-completion
```

If intended edits already exist on the default branch, create the new branch at the current commit without losing the worktree changes. Do not commit them on the default branch.

### 4. Implement in coherent slices

Keep changes scoped to one reviewable purpose. Separate independent concerns into separate commits or PRs when that improves rollback and review.

Before adding new architecture, security, migration, or domain ownership, invoke the relevant governance skills.

Update tests and durable documentation as required by repository policy. Remove obsolete code and documentation made redundant by the change.

### 5. Review the complete diff

Inspect all intended changes before staging:

```bash
git diff --stat
git diff
git diff --check
git status --short
```

Review generated artifacts, migrations, lockfiles, documentation, and deleted files. Confirm no secret, credential, token, private key, personal data, build output, or local state is included.

### 6. Run required verification

Derive checks from repository instructions, CI, package manifests, build files, and changed components.

Run the smallest relevant checks early, then the full required gate before commit or PR. Typical checks include:

- formatting;
- linting;
- type checking;
- unit, integration, contract, and end-to-end tests;
- build or package verification;
- migration and generated-file checks;
- security, dependency, secret, and static analysis;
- documentation or schema validation;
- repository hygiene checks.

Fix failures when the repository requires them. If a required check remains failing, do not claim the change is ready. Distinguish a verified pre-existing failure from a regression and record exact evidence.

### 7. Stage intentionally

Stage explicit paths or reviewed hunks:

```bash
git add path/to/file another/path
git diff --cached --stat
git diff --cached
```

Avoid `git add .` or `git add -A` unless the entire worktree has been reviewed and every change belongs to the commit.

The staged diff is the commit contract. Re-run relevant checks if staging changes the verified content.

### 8. Commit coherently

Use strict Conventional Commits unless the repository defines another convention:

```text
<type>(<optional-scope>): <imperative summary>
```

Examples:

```text
feat(opponents): create canonical records from reports
fix(events): allow reassignment between event teams
security(auth): enforce resource ownership on mutations
```

Commit body should explain why, important behaviour, migration or compatibility notes, and verification when useful. Do not add AI attribution or fabricated co-authors.

Before committing, inspect the staged diff once more. After committing, inspect the created commit:

```bash
git show --stat --oneline --decorate HEAD
git status --short --branch
```

### 9. Push safely

Push the branch and establish upstream:

```bash
git push --set-upstream origin <branch>
```

Never claim the push succeeded without command evidence. If hooks or remote checks fail, fix the issue and retry without bypassing policy.

### 10. Create the pull request

Use the repository PR template when present. Otherwise use `assets/pull-request-template.md` with these sections:

```text
## Summary
## Changes
## Verification
## Notes
```

The title should be concise and usually follow Conventional Commit style.

Create the PR with GitHub CLI when authenticated and requested:

```bash
gh pr create --base <default-branch> --head <branch> --title "<title>" --body-file <file>
```

Include:

- behavioural summary;
- significant implementation details;
- exact commands and outcomes for verification;
- migrations, rollout, rollback, or provider actions;
- linked ADRs, ARRs, issues, and security findings;
- known limitations or follow-up work;
- screenshots only when they add review evidence.

Inspect the created PR and its checks. Do not fabricate a URL, status, or reviewer state.

### 11. Report delivery evidence

Report only verified facts:

- branch name;
- commit hash and subject;
- checks executed and outcomes;
- push result;
- PR number and URL;
- remaining failures, manual actions, or provider changes.

## Commit splitting test

Split a commit when changes:

- have different purposes;
- can be reverted independently;
- mix mechanical movement with behaviour changes;
- mix generated updates with unrelated logic;
- require different reviewers;
- conceal a risky change inside broad cleanup.

Keep one commit when splitting would create broken intermediate states or artificial noise. Every commit should remain understandable and preferably verifiable.

## Common rationalizations

| Rationalization | Required response |
|---|---|
| "It is only one small change." | Small changes still require a branch, reviewed diff, and repository-required checks. |
| "I will inspect after committing." | Inspect before staging, before commit, and after commit. |
| "`git add .` is faster." | Stage only reviewed content unless the entire worktree is known and intended. |
| "The failing test is probably unrelated." | Reproduce or compare against the base and record evidence. Do not guess. |
| "The PR body can repeat the commit title." | Give reviewers behaviour, verification, risks, and linked records. |
| "Force push is harmless on my branch." | Preserve shared review history; rewrite only with explicit justification and lease protection. |
| "The user can clean up the branch later." | Leave a coherent, reviewable branch now. |

## Red flags

- Work starts on the protected default branch without immediately creating a feature branch.
- Unrelated user changes are staged or discarded.
- The commit contains secrets, local environment files, build caches, or temporary artifacts.
- Required checks are skipped or described without execution evidence.
- A broad commit mixes architecture, feature behaviour, formatting, and unrelated cleanup.
- The PR omits migration, rollback, provider, or security implications.
- History is rewritten after review without explicit need.
- The reported branch, hash, push, or PR cannot be verified.

## Verification checklist

Before completion:

- repository instructions and default branch were discovered;
- existing work was preserved;
- the branch is correctly based and named;
- the complete diff was reviewed;
- staged content is intentional and secret-free;
- required checks were executed and their real outcomes recorded;
- commits are coherent and convention-compliant;
- push succeeded and upstream is correct;
- the PR targets the correct base and contains review evidence;
- ADRs, ARRs, security records, issues, and provider actions are linked where relevant;
- no result or assurance was invented.

## Stop or escalate

Stop and report when:

- intended and unrelated work cannot be distinguished safely;
- the correct base branch or remote cannot be established;
- credentials or a suspected secret are exposed;
- repository policy requires checks that cannot be run;
- a protected or shared history rewrite would be required without authority;
- GitHub authentication or permissions prevent the requested push or PR;
- required verification remains failing.
