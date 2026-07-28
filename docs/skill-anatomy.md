# Skill anatomy

Every skill lives under:

```text
skills/<skill-name>/
├── SKILL.md
├── references/   # optional, explanatory material loaded on demand
├── assets/       # optional, templates and non-executable resources
└── scripts/      # optional, deterministic executable helpers
```

## Frontmatter

`SKILL.md` must begin at byte zero with YAML frontmatter:

```yaml
---
name: skill-name
description: Describes what the skill does. Use when the triggering conditions occur.
license: MIT
compatibility: Agent Skills standard.
metadata:
  owner: lagebj
  category: example
---
```

Requirements:

- `name` matches the directory name;
- lowercase letters, numbers, and single hyphens only;
- 1 to 64 characters;
- description is non-empty, no more than 1024 characters, and includes usage triggers;
- metadata values are strings for broad runtime compatibility.

## Required sections

Use sections appropriate to the workflow, normally including:

1. Overview or purpose.
2. When to use.
3. When not to use.
4. Context to load.
5. Step-by-step workflow.
6. Common rationalizations and rebuttals.
7. Red flags.
8. Verification checklist.
9. Stop or escalation conditions.

A skill is an executable process for an agent, not a general essay.

## Progressive disclosure

Keep `SKILL.md` under 500 lines. Move detailed classifications, examples, templates, and platform-specific material into direct references.

Every important reference must be linked directly from `SKILL.md`. Avoid chains where one reference points to another reference containing the actual rule.

## Assets

Use `assets/` for templates the agent copies or adapts. Templates must not contain live secrets, real credentials, or environment-specific sensitive values.

## Scripts

Add a script only when execution is more reliable than natural-language reasoning. Scripts must:

- be safe by default;
- validate inputs;
- fail clearly;
- avoid hidden network or destructive behaviour;
- emit useful machine-readable output when practical;
- document prerequisites in `SKILL.md`.

## Quality test

A skill is ready when:

- its description triggers on representative requests and avoids unrelated requests;
- steps have explicit checkpoints and exit criteria;
- an agent cannot satisfy it by merely asserting completion;
- records and outputs have clear ownership;
- failure states and missing authority are handled;
- references are necessary and discoverable;
- at least three realistic evaluation scenarios exist.
