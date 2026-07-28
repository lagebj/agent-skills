# Runtime setup

The repository keeps one canonical `skills/` tree. Installation either links or copies those directories into a runtime discovery path, or exposes the tree through a plugin manifest.

## Recommended portable installation

```bash
./scripts/install.sh --runtime portable --scope user
```

This installs into:

```text
~/.agents/skills/
```

OpenCode and Gemini CLI support this compatibility path. It also avoids maintaining duplicate runtime-specific copies in the repository.

For project-local use:

```bash
./scripts/install.sh --runtime portable --scope project --target /path/to/project
```

Destination:

```text
/path/to/project/.agents/skills/
```

## Installation modes

The installer defaults to symlinks:

```bash
./scripts/install.sh --runtime portable --scope user --mode link
```

Use copies for ephemeral or restricted runtimes:

```bash
./scripts/install.sh --runtime portable --scope user --mode copy
```

Use `--force` only to replace an existing installation of the same named skills. The installer never deletes unrelated skill directories.

Install one or more skills:

```bash
./scripts/install.sh --runtime portable --scope user \
  --skill adr-governance \
  --skill git-commit-branch-pr
```

## OpenCode

OpenCode discovers project or global skills from:

```text
.opencode/skills/
~/.config/opencode/skills/
.claude/skills/
~/.claude/skills/
.agents/skills/
~/.agents/skills/
```

Install directly into the OpenCode-specific global path:

```bash
./scripts/install.sh --runtime opencode --scope user
```

This clone also includes `opencode.json`, which adds `./skills` as an explicit source when OpenCode is launched inside the skill repository.

Avoid installing the same skill name into several discovered paths unless an override is intentional. Runtime precedence may select a different copy than expected.

## Claude Code

Install into the user skill path:

```bash
./scripts/install.sh --runtime claude --scope user
```

Destination:

```text
~/.claude/skills/
```

For plugin-based installation, create the GitHub repository first, then add it as a Claude Code marketplace using `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`.

## Gemini CLI

Install from GitHub:

```bash
gemini skills install https://github.com/lagebj/engineering-agent-skills.git --path skills
```

Install or link locally:

```bash
gemini skills install ./skills
gemini skills link ./skills
```

Gemini also discovers `~/.agents/skills` and workspace `.agents/skills`.

Verify in a Gemini session:

```text
/skills list
```

## Codex

The `.codex-plugin/plugin.json` manifest points Codex at `./skills/`. Install the repository as a plugin through the Codex plugin interface supported by the active Codex version.

For filesystem-based installations, prefer the current Agent Skills compatibility path exposed by the runtime. Do not maintain a second edited copy of the skills.

## Cursor and other agents

Use a project-local `.agents/skills` installation where supported:

```bash
./scripts/install.sh --runtime portable --scope project --target /path/to/project --mode copy
```

For agents that only support rule files, load the relevant `SKILL.md` explicitly rather than concatenating the entire library into every prompt. Progressive disclosure is part of the design.

## Updating

For linked installations:

```bash
cd /path/to/engineering-agent-skills
git pull --ff-only
python3 scripts/validate-skills.py
```

The linked runtime sees the new content immediately.

For copied installations, rerun `scripts/install.sh` with `--force` after pulling.
