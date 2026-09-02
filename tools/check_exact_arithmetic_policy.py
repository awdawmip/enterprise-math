#!/usr/bin/env python3
"""Static gate for the Enterprise Math exact-arithmetic runtime policy.

The checker is intentionally scoped to files supplied on the command line.  It
is designed for new or materially modified research-calculation paths so the
historical repository can migrate incrementally instead of being retroactively
reclassified in one step.
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path


BRC_FACADE = Path("src/enterprise_math/exact_arithmetic.py")
DIRECT_DIVISION_PRIMITIVES = {
    "division_gap",
    "euclidean_state",
    "integer_quotient",
    "multiple_collapse",
}
FORBIDDEN_CALLS = {"divmod", "float", "Decimal", "Fraction"}
FORBIDDEN_MODULES = {"decimal", "fractions"}


def _relative_display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)


def _call_name(node: ast.Call) -> str | None:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return None


def check_python_file(path: Path) -> list[str]:
    display = _relative_display(path)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=display)
    violations: list[str] = []
    facade = Path(display) == BRC_FACADE

    for node in ast.walk(tree):
        line = getattr(node, "lineno", 0)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            violations.append(f"{display}:{line}: native '/' division is forbidden")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.FloorDiv):
            violations.append(
                f"{display}:{line}: direct '//' quotient materialization must use BRC facade"
            )
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
            violations.append(
                f"{display}:{line}: direct '%' remainder/divisibility materialization must use BRC facade"
            )
        elif isinstance(node, ast.Constant) and isinstance(node.value, float):
            violations.append(f"{display}:{line}: float literal is forbidden in native exact arithmetic")
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".", 1)[0]
                if root in FORBIDDEN_MODULES:
                    violations.append(
                        f"{display}:{line}: {root} is not a native exact-arithmetic carrier"
                    )
        elif isinstance(node, ast.ImportFrom):
            module = (node.module or "").split(".", 1)[0]
            if module in FORBIDDEN_MODULES:
                violations.append(
                    f"{display}:{line}: {module} is not a native exact-arithmetic carrier"
                )
        elif isinstance(node, ast.Call):
            name = _call_name(node)
            if name in FORBIDDEN_CALLS:
                violations.append(
                    f"{display}:{line}: direct {name} materialization bypasses BRC runtime"
                )
            if not facade and name in DIRECT_DIVISION_PRIMITIVES:
                violations.append(
                    f"{display}:{line}: direct P007 primitive {name} bypasses BRC facade"
                )

    return violations


def expand_paths(raw_paths: list[str]) -> list[Path]:
    result: list[Path] = []
    for raw in raw_paths:
        path = Path(raw)
        if path.is_dir():
            result.extend(sorted(path.rglob("*.py")))
        elif path.suffix == ".py":
            result.append(path)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="+",
        help="new or materially modified governed Python files/directories",
    )
    args = parser.parse_args()

    paths = expand_paths(args.paths)
    if not paths:
        parser.error("no Python files selected")

    violations: list[str] = []
    for path in paths:
        violations.extend(check_python_file(path))

    if violations:
        print("EXACT_ARITHMETIC_POLICY: FAIL")
        for violation in violations:
            print(violation)
        return 1

    print(f"EXACT_ARITHMETIC_POLICY: PASS ({len(paths)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
