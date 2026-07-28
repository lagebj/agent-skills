# Engineering Agent Skills

Reusable engineering workflows for AI coding agents, organised using the Agent Skills `SKILL.md` format and the repository conventions popularised by `addyosmani/agent-skills`.

The repository contains five skills:

| Skill | Purpose |
|---|---|
| `using-agent-skills` | Dispatches and composes the other skills. |
| `adr-governance` | Governs architectural decisions and ADR lifecycle. |
| `architectural-residue-records` | Records and resolves mismatches between intended architecture and implementation. |
| `application-security-engineering` | Applies proportionate application-security engineering across code and provider boundaries. |
| `git-commit-branch-pr` | Safely carries repository work from branch creation to a verified GitHub pull request. |

## Repository structure

```text
engineering-agent-skills/
├── skills/                  # Canonical, cloneable skill source directories
│   └── <skill>/
│       ├── SKILL.md
│       ├── references/      # Loaded on demand
│       └── assets/          # Templates and non-executable resources
├── docs/                    # Runtime and authoring guides
├── scripts/                 # Validation, installation, configuration, and scaffolding
├── evals/                   # Behavioural scenarios for manual or automated evaluation
├── .claude-plugin/          # Claude Code plugin and marketplace metadata
├── .codex-plugin/           # Codex plugin metadata
├── .agents/plugins/         # Agent/Antigravity marketplace metadata
├── .github/                 # Validation workflow and contribution templates
├── AGENTS.md                # Instructions for agents modifying this repository
├── CLAUDE.md                # Claude Code repository entry point
├── opencode.json            # OpenCode source configuration for this clone
└── plugin.json              # Generic plugin metadata
```

`skills/<name>/` is the only source of truth. The committed repository is source-only. ZIP files, tarballs, generated release bundles, and copied runtime installations are deliberately excluded.

## Quick start

### Clone and install through the portable path

The `.agents/skills` path is supported by OpenCode and Gemini CLI and is designed as a cross-agent compatibility path.

```bash
git clone https://github.com/lagebj/engineering-agent-skills.git
cd engineering-agent-skills
./scripts/install.sh --runtime portable --scope user
```

The default installation mode uses symlinks. A later `git pull` updates the installed skills immediately.

### OpenCode

```bash
./scripts/install.sh --runtime opencode --scope user
```

Project-local installation:

```bash
./scripts/install.sh --runtime portable --scope project --target /path/to/project
```

### Claude Code

```bash
./scripts/install.sh --runtime claude --scope user
```

The repository also includes Claude Code marketplace metadata under `.claude-plugin/`.

### Gemini CLI

```bash
gemini skills install https://github.com/lagebj/engineering-agent-skills.git --path skills
```

or use the portable installer.

### Codex

The repository includes `.codex-plugin/plugin.json`, which exposes the root `skills/` directory when installed as a Codex plugin. The portable `.agents/skills` installation can also be used by runtimes that support the Agent Skills compatibility path.

See `docs/runtime-setup.md` for detailed options and precedence guidance.

## Validation

```bash
python3 scripts/validate-skills.py
```

This validates frontmatter, names, descriptions, links, line limits, JSON files, evaluation files, and the source-only repository policy. Validation fails when an archive artifact is present anywhere in the repository tree.

## Add a skill

```bash
./scripts/create-skill.sh my-new-skill "What the skill does. Use when ..."
```

Then complete the workflow, references, assets, anti-rationalization, red flags, and verification criteria. See `docs/skill-anatomy.md`.

## Create the GitHub repository

After extracting the transport bundle, enter the `engineering-agent-skills` directory and run:

```bash
git init -b main
python3 scripts/validate-skills.py
git add .
git commit -m "feat: add reusable engineering agent skills"
gh repo create lagebj/engineering-agent-skills --source=. --remote=origin --push
```

Choose repository visibility through the GitHub CLI prompt. If a different owner or repository name is used, run:

```bash
python3 scripts/configure-repository.py --repo OWNER/REPOSITORY --author "AUTHOR NAME"
```

The downloaded transport archive is not part of the repository. Extract it first and commit only the files inside the repository directory.

## Licence

MIT. See `LICENSE`.
