#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/skills"
runtime="portable"
scope="user"
mode="link"
target=""
force="false"
declare -a selected_skills=()

usage() {
  cat <<'EOF'
Usage: scripts/install.sh [options]

Options:
  --runtime portable|opencode|claude|gemini|all
  --scope user|project
  --target PATH            Required for project scope unless run inside target
  --mode link|copy         Default: link
  --skill NAME             Repeat to install selected skills only
  --force                  Replace existing installation for selected names
  --list                   List available skills
  -h, --help

The "all" runtime installs into the portable .agents path and the Claude path.
OpenCode and Gemini discover the portable path, avoiding duplicate installations.
EOF
}

list_skills() {
  find "$skills_dir" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --runtime) runtime="$2"; shift 2 ;;
    --scope) scope="$2"; shift 2 ;;
    --target) target="$2"; shift 2 ;;
    --mode) mode="$2"; shift 2 ;;
    --skill) selected_skills+=("$2"); shift 2 ;;
    --force) force="true"; shift ;;
    --list) list_skills; exit 0 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

[[ "$runtime" =~ ^(portable|opencode|claude|gemini|all)$ ]] || { echo "Invalid runtime: $runtime" >&2; exit 2; }
[[ "$scope" =~ ^(user|project)$ ]] || { echo "Invalid scope: $scope" >&2; exit 2; }
[[ "$mode" =~ ^(link|copy)$ ]] || { echo "Invalid mode: $mode" >&2; exit 2; }

if [[ ${#selected_skills[@]} -eq 0 ]]; then
  while IFS= read -r name; do selected_skills+=("$name"); done < <(list_skills)
fi

for name in "${selected_skills[@]}"; do
  [[ -f "$skills_dir/$name/SKILL.md" ]] || { echo "Unknown skill: $name" >&2; exit 2; }
done

if [[ "$scope" == "project" ]]; then
  target="${target:-$PWD}"
  target="$(cd "$target" && pwd)"
fi

declare -a destinations=()
if [[ "$scope" == "user" ]]; then
  case "$runtime" in
    portable) destinations+=("$HOME/.agents/skills") ;;
    opencode) destinations+=("$HOME/.config/opencode/skills") ;;
    claude) destinations+=("$HOME/.claude/skills") ;;
    gemini) destinations+=("$HOME/.gemini/skills") ;;
    all) destinations+=("$HOME/.agents/skills" "$HOME/.claude/skills") ;;
  esac
else
  case "$runtime" in
    portable) destinations+=("$target/.agents/skills") ;;
    opencode) destinations+=("$target/.opencode/skills") ;;
    claude) destinations+=("$target/.claude/skills") ;;
    gemini) destinations+=("$target/.gemini/skills") ;;
    all) destinations+=("$target/.agents/skills" "$target/.claude/skills") ;;
  esac
fi

install_one() {
  local name="$1"
  local destination_root="$2"
  local source="$skills_dir/$name"
  local destination="$destination_root/$name"

  mkdir -p "$destination_root"

  if [[ -e "$destination" || -L "$destination" ]]; then
    if [[ "$force" != "true" ]]; then
      echo "Refusing to replace existing path: $destination (use --force)" >&2
      exit 1
    fi
    rm -rf "$destination"
  fi

  if [[ "$mode" == "link" ]]; then
    ln -s "$source" "$destination"
  else
    cp -R "$source" "$destination"
  fi

  echo "Installed $name -> $destination" >&2
}

for destination_root in "${destinations[@]}"; do
  for name in "${selected_skills[@]}"; do
    install_one "$name" "$destination_root"
  done
done
