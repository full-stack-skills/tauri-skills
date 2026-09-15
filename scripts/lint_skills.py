"""Lint gate for skill packages: every skills/<name>/SKILL.md must be well-formed.

Rules (exit 1 on any violation):
- every directory under skills/ contains SKILL.md
- frontmatter has a `name` equal to its directory name
- `description` is present, single-line (block scalars break some hosts), 20-1024 chars
- skill names are lowercase kebab-case without a `codex-` prefix
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
        elif line.startswith(" ") or line.startswith("-"):
            # continuation of a block scalar or list: mark parent as multiline
            if fields:
                last = next(reversed(fields))
                fields[last] = fields[last] + "\n" + line
    return fields


def main() -> int:
    errors = []
    skills_dir = ROOT / "skills"
    dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not dirs:
        errors.append("skills/ has no skill directories")
    for skill_dir in dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        fm = frontmatter(skill_md.read_text())
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if not name:
            errors.append(f"{skill_dir.name}: frontmatter missing name")
        elif name != skill_dir.name:
            errors.append(f"{skill_dir.name}: name '{name}' != directory name")
        if not NAME_RE.match(skill_dir.name):
            errors.append(f"{skill_dir.name}: not lowercase kebab-case")
        if skill_dir.name.startswith("codex-"):
            errors.append(f"{skill_dir.name}: host-prefixed names are not allowed in source packages")
        if not desc:
            errors.append(f"{skill_dir.name}: frontmatter missing description")
        else:
            if "\n" in desc or desc in ("|", ">", "|-", ">-", "|+", ">+"):
                errors.append(f"{skill_dir.name}: description must be single-line (no block scalars)")
            elif not (20 <= len(desc) <= 1024):
                errors.append(f"{skill_dir.name}: description length {len(desc)} outside 20..1024")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"lint_skills: {len(dirs)} skills, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
