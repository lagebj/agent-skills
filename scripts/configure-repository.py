#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data):
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="GitHub OWNER/REPOSITORY")
    parser.add_argument("--author", required=True)
    args = parser.parse_args()

    if args.repo.count("/") != 1:
        parser.error("--repo must be OWNER/REPOSITORY")

    owner, repo = args.repo.split("/", 1)
    url = f"https://github.com/{owner}/{repo}"

    claude = ROOT / ".claude-plugin/plugin.json"
    data = load(claude)
    data["name"] = repo
    data["author"] = {"name": args.author}
    data["homepage"] = url
    data["repository"] = url
    save(claude, data)

    marketplace = ROOT / ".claude-plugin/marketplace.json"
    data = load(marketplace)
    data["name"] = f"{owner}-{repo}"
    data["owner"] = {"name": args.author, "url": f"https://github.com/{owner}"}
    plugin = data["plugins"][0]
    plugin["name"] = repo
    plugin["source"]["repo"] = args.repo
    plugin["homepage"] = url
    save(marketplace, data)

    codex = ROOT / ".codex-plugin/plugin.json"
    data = load(codex)
    data["name"] = repo
    data["author"] = {"name": args.author, "url": f"https://github.com/{owner}"}
    data["homepage"] = url
    data["repository"] = url
    save(codex, data)

    agents = ROOT / ".agents/plugins/marketplace.json"
    data = load(agents)
    data["name"] = f"{owner}-{repo}"
    data["owner"] = {"name": args.author, "url": f"https://github.com/{owner}"}
    plugin = data["plugins"][0]
    plugin["name"] = repo
    plugin["source"] = f"{url}.git"
    save(agents, data)

    generic = ROOT / "plugin.json"
    data = load(generic)
    data["name"] = repo
    save(generic, data)

    text_files = [
        ROOT / "README.md",
        ROOT / "docs/runtime-setup.md",
        ROOT / "docs/skill-anatomy.md",
        ROOT / "scripts/create-skill.sh",
        ROOT / ".github/CODEOWNERS",
        ROOT / "LICENSE",
        *sorted((ROOT / "skills").glob("*/SKILL.md")),
    ]
    replacements = [
        ("lagebj/engineering-agent-skills", args.repo),
        ("engineering-agent-skills", repo),
        ("owner: lagebj", f"owner: {owner}"),
        ("* @lagebj", f"* @{owner}"),
        ("Copyright (c) 2026 lagebj", f"Copyright (c) 2026 {args.author}"),
    ]
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        for old, new in replacements:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")

    print(f"Configured manifests and repository references for {args.repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
