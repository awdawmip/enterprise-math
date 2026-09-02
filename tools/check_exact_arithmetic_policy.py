#!/usr/bin/env python3
"""Static gate for the Enterprise Math exact-arithmetic runtime policy.

The checker is intentionally scoped to files supplied on the command line. It
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
DIRECT_ROOT_PRIMITIVES = {
    "integer_nth_root",
    "collapse",
    "scaled_root",
}
FORBIDDEN_CALLS = {"divmod", "float", "Decimal", "Fraction", "sqrt", "isqrt"}
FORBIDDEN_MODULES = {"decimal", "fractions"}
FLOAT_LOG_MODULES = {"math", "cmath"}
FLOAT_LOG_CALLS = {"log", "log2", "log10", "log1p"}


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


def _floating_log_aliases(tree: ast.AST) -> tuple[set[str], set[str]]:
    """Return imported module aliases and direct-name aliases for float logs."""
    module_aliases: set[str] = set()
    direct_aliases: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".", 1)[0]
                if root in FLOAT_LOG_MODULES:
                    module_aliases.add(alias.asname or root)
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".", 1)[0]
            if root not in FLOAT_LOG_MODULES:
                continue
            for alias in node.names:
                if alias.name in FLOAT_LOG_CALLS:
                    direct_aliases.add(alias.asname or alias.name)
    return module_aliases, direct_aliases


def _is_floating_log_call(
    node: ast.Call,
    module_aliases: set[str],
    direct_aliases: set[str],
) -> bool:
    if isinstance(node.func, ast.Name):
        return node.func.id in direct_aliases
    if not isinstance(node.func, ast.Attribute):
        return False
    if node.func.attr not in FLOAT_LOG_CALLS:
        return False
    return isinstance(node.func.value, ast.Name) and node.func.value.id in module_aliases


def check_python_file(path: Path) -> list[str]:
    display = _relative_display(path)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=display)
    violations: list[str] = []
    facade = Path(display) == BRC_FACADE
    floating_log_modules, floating_log_names = _floating_log_aliases(tree)

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
            if _is_floating_log_call(node, floating_log_modules, floating_log_names):
                violations.append(
                    f"{display}:{line}: floating logarithm materialization bypasses BRC runtime"
                )
            if not facade and name in DIRECT_DIVISION_PRIMITIVES:
                violations.append(
                    f"{display}:{line}: direct P007 primitive {name} bypasses BRC facade"
                )
            if not facade and name in DIRECT_ROOT_PRIMITIVES:
                violations.append(
                    f"{display}:{line}: direct root primitive {name} bypasses BRC facade"
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
