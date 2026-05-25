#!/usr/bin/env python3
"""Validate the Lovable skill folders without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_SKILLS = (
    "security-scan-review",
    "lovable-plan-approval",
    "supabase-rls-audit",
    "financial-flow-review",
    "release-checklist",
    "mobile-ux-review",
    "sied-dev-review",
    "assessoria-dev-review",
    "scriptum-dev-review",
    "autoded-dev-review",
)

NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SUSPICIOUS_PATTERNS = (
    re.compile(r"service_role\s+key", re.IGNORECASE),
    re.compile(r"password\s*=", re.IGNORECASE),
    re.compile(r"token\s*=", re.IGNORECASE),
    re.compile(r"secret\s*=", re.IGNORECASE),
    re.compile(r"sk_live", re.IGNORECASE),
    re.compile(r"sk_test", re.IGNORECASE),
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if not key or not value or key in data:
            return None
        data[key] = value
    return data, "\n".join(lines[end + 1 :]).strip()


def validate_skill(root: Path, folder: str) -> list[str]:
    errors: list[str] = []
    path = root / folder / "SKILL.md"
    if not path.is_file():
        return [f"{folder}: SKILL.md ausente"]

    text = path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)
    if parsed is None:
        return [f"{folder}: frontmatter YAML ausente ou invalido"]

    metadata, body = parsed
    name = metadata.get("name", "")
    description = metadata.get("description", "")

    if set(metadata) != {"name", "description"}:
        errors.append(f"{folder}: frontmatter deve conter apenas name e description")
    if name != folder:
        errors.append(f"{folder}: name deve ser igual ao nome da pasta")
    if not NAME_PATTERN.fullmatch(name):
        errors.append(f"{folder}: name deve usar minusculas, numeros e hifens")
    if not description.startswith("Use when"):
        errors.append(f"{folder}: description deve comecar com 'Use when'")
    if not body or not re.search(r"^#\s+\S", body, re.MULTILINE):
        errors.append(f"{folder}: instrucoes Markdown ausentes")

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern.search(text):
            errors.append(f"{folder}: padrao suspeito encontrado: {pattern.pattern}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parent
    failures: list[str] = []
    for folder in EXPECTED_SKILLS:
        failures.extend(validate_skill(root, folder))

    if failures:
        print("VALIDACAO FALHOU")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"VALIDACAO OK: {len(EXPECTED_SKILLS)} skills verificadas.")
    print("- Todas possuem SKILL.md com frontmatter, name e description validos.")
    print("- Todas as descriptions comecam com 'Use when'.")
    print("- Nenhum padrao suspeito foi encontrado nos SKILL.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
