#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
name="${1:-}"
description="${2:-}"

if [[ -z "$name" || -z "$description" ]]; then
  echo 'Usage: scripts/create-skill.sh <kebab-case-name> "Description. Use when ..."' >&2
  exit 2
fi

if [[ ! "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || [[ ${#name} -gt 64 ]]; then
  echo "Invalid skill name: $name" >&2
  exit 2
fi

skill_dir="$repo_root/skills/$name"
if [[ -e "$skill_dir" ]]; then
  echo "Skill already exists: $skill_dir" >&2
  exit 1
fi

mkdir -p "$skill_dir/references" "$skill_dir/assets"
cat > "$skill_dir/SKILL.md" <<EOF
---
name: $name
description: $description
license: MIT
compatibility: Agent Skills standard.
metadata:
  owner: lagebj
  category: unclassified
---

# $(echo "$name" | tr '-' ' ')

## Overview

Define the workflow and its outcome.

## Use this skill when

- Add concrete triggers.

## Do not use this skill for

- Add exclusions.

## Workflow

1. Add ordered, verifiable steps.

## Common rationalizations

| Rationalization | Required response |
|---|---|
| "Add an excuse." | Add the required correction. |

## Red flags

- Add signs the workflow is being violated.

## Verification checklist

- Add objective evidence requirements.

## Stop or escalate

Stop when required evidence or authority is missing. Do not invent completion.
EOF

touch "$skill_dir/references/.gitkeep" "$skill_dir/assets/.gitkeep"
echo "Created skills/$name" >&2
