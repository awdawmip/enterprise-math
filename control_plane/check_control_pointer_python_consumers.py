#!/usr/bin/env python3
"""Find production Python consumers of migratable control-pointer keys.

This is a semantic-safety helper for gradual control migration. It does not
search prose/string mentions. It looks for AST operations that actually read a
mapping key, such as ``value['canonical_dispatch']`` or
``value.get('canonical_dispatch')``.

The question answered here is deliberately narrow: can a runtime/production
Python path depend on the old key value? Tests and checker/validator programs are
excluded because they may assert or compare the field without using it as
runtime routing authority. Those validators remain independently active in CI.
A pointer may be mechanically migrated only when this production-consumer census
is empty or every production consumer is deliberately updated in the same
bounded change.
"""
from __future__ import annotations

import ast
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_ROOTS = {
    ".git",
    ".lake",
    ".venv",
    "venv",
    "node_modules",
    "tests",
}


class PointerConsumerError(ValueError):
    pass


def _is_validator(path: Path) -> bool:
    """Return True for repository validators, not runtime/production tools."""
    return path.name.startswith("check_")


def python_files(root: Path = ROOT) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_ROOTS for part in rel.parts):
            continue
        if _is_validator(path):
            continue
        yield path


def _constant_string(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def mapping_key_reads(path: Path, key: str) -> list[int]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, UnicodeError, SyntaxError) as exc:
        raise PointerConsumerError(f"cannot parse {path}: {exc}") from exc
    lines: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            if _constant_string(node.slice) == key:
                lines.add(node.lineno)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in {"get", "pop", "setdefault"} and node.args:
                if _constant_string(node.args[0]) == key:
                    lines.add(node.lineno)
    return sorted(lines)


def consumers(key: str, root: Path = ROOT) -> dict[str, list[int]]:
    out: dict[str, list[int]] = {}
    for path in python_files(root):
        hits = mapping_key_reads(path, key)
        if hits:
            out[path.relative_to(root).as_posix()] = hits
    return out


def main() -> int:
    key = "canonical_dispatch"
    try:
        hits = consumers(key)
    except PointerConsumerError as exc:
        print(f"ERROR: {exc}")
        return 1
    if hits:
        print(f"BLOCKED: production Python consumers read mapping key {key!r}:")
        for path, lines in sorted(hits.items()):
            print(f" - {path}: lines {lines}")
        return 2
    print(
        f"PASS: no production Python consumer reads mapping key {key!r}; "
        "tests/checkers are validated separately."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
