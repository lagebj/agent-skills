# Commit and pull-request format

## Conventional Commit types

- `feat`: new user or system capability
- `fix`: defect correction
- `security`: security hardening or vulnerability remediation
- `refactor`: internal restructuring without intended behaviour change
- `docs`: documentation-only change
- `test`: test-only change
- `perf`: performance improvement
- `ci`: CI workflow change
- `build`: build system or dependency packaging
- `chore`: maintenance that fits no stronger type

Use an imperative, lower-case summary without a trailing period.

## Breaking changes

Use the repository convention. Standard Conventional Commits allow:

```text
feat(api)!: replace legacy report endpoint
```

and a footer:

```text
BREAKING CHANGE: clients must use POST /reports/complete.
```

## Commit body

Explain why and consequential behaviour. Wrap when practical. Include issue or record footers only when valid.

## Pull request title

Use the dominant commit's intent, not a generic title such as "updates" or "misc fixes".

## Pull request body

A reviewer should be able to answer:

- What changed?
- Why is it correct?
- How was it verified?
- What is risky or irreversible?
- What must happen outside code?
- Which decisions and records govern it?
