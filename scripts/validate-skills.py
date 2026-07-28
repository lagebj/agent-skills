#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter must start at byte zero")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter closing delimiter not found")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, object] = {}
    stack: list[tuple[int, dict[str, object]]] = [(-1, data)]
    for number, line in enumerate(raw.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()
        if ":" not in content:
            raise ValueError(f"unsupported YAML at frontmatter line {number}: {content}")
        key, value = content.split(":", 1)
        key, value = key.strip(), value.strip()
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if value == "":
            child: dict[str, object] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            parent[key] = value
    return data, body


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]
    try:
        metadata, body = parse_frontmatter(skill_file)
    except Exception as exc:
        return [f"{skill_file.relative_to(ROOT)}: {exc}"]

    name = metadata.get("name")
    description = metadata.get("description")
    if name != skill_dir.name:
        errors.append(f"{skill_file.relative_to(ROOT)}: name must match directory ({skill_dir.name})")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(f"{skill_file.relative_to(ROOT)}: invalid name")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_file.relative_to(ROOT)}: description exceeds 1024 characters")
    elif "use when" not in description.lower():
        errors.append(f"{skill_file.relative_to(ROOT)}: description must include usage triggers ('Use when')")

    line_count = len(skill_file.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        errors.append(f"{skill_file.relative_to(ROOT)}: {line_count} lines exceeds 500")

    required_signals = ["verification", "red flags", "rationalization"]
    lower = body.lower()
    for signal in required_signals:
        if signal not in lower:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing {signal} section")

    for match in LINK_RE.finditer(body):
        target = match.group(1).split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (skill_dir / target).resolve()
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"{skill_file.relative_to(ROOT)}: link escapes skill directory: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{skill_file.relative_to(ROOT)}: broken link: {target}")

    return errors



FORBIDDEN_ARCHIVE_SUFFIXES = (".zip", ".tar", ".tar.gz", ".tgz", ".7z")


def validate_no_archives() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        lower_name = path.name.lower()
        if any(lower_name.endswith(suffix) for suffix in FORBIDDEN_ARCHIVE_SUFFIXES):
            errors.append(f"{relative}: archive artifacts must not be committed")
    return errors

def validate_json_files() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    return errors


def validate_evals(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    for name in sorted(skill_names):
        path = ROOT / "evals" / f"{name}.json"
        if not path.is_file():
            errors.append(f"evals/{name}.json: missing")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            cases = data.get("cases", [])
            if data.get("skill") != name:
                errors.append(f"{path.relative_to(ROOT)}: skill field must be {name}")
            if len(cases) < 3:
                errors.append(f"{path.relative_to(ROOT)}: at least three cases required")
            for index, case in enumerate(cases, 1):
                if not case.get("query") or not case.get("expected_behavior"):
                    errors.append(f"{path.relative_to(ROOT)}: incomplete case {index}")
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid evaluation file: {exc}")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    names = {path.name for path in skill_dirs}
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))
    errors.extend(validate_json_files())
    errors.extend(validate_no_archives())
    errors.extend(validate_evals(names))

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skill_dirs)} skills, manifests, evaluation files, links, and repository archive policy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
