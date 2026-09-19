#!/usr/bin/env python3
"""Bounded AST inventory, NOT a whole-program no-float proof.

True division of Fraction/symbolic values can be exact: it is REVIEW, not ERROR.
Use on the full checkout before migrating consumers. Aliasing, native extensions,
dynamic dispatch and values loaded from data still need separate inspection.
"""
from __future__ import annotations
import argparse
import ast
import json
from pathlib import Path

APPROX_CALLS = {"sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "atan2", "exp", "log", "log2", "log10", "hypot"}


def scan_file(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(path))
    imports: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name.split(".")[0]] = alias.name
        elif isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                imports[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    findings: list[dict[str, object]] = []
    def emit(node: ast.AST, rule: str, severity: str) -> None:
        findings.append({"line": getattr(node, "lineno", None), "rule": rule, "severity": severity,
                         "expression": (ast.get_source_segment(text, node) or "")[:180]})
    def qualified(node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return imports.get(node.id, node.id)
        if isinstance(node, ast.Attribute):
            return qualified(node.value) + "." + node.attr
        return ""
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            emit(node, "APPROXIMATE_NUMERIC_LITERAL", "ERROR")
        if isinstance(node, ast.Name) and node.id in {"float", "complex"}:
            emit(node, "BINARY_NUMERIC_TYPE", "ERROR")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            emit(node, "TYPECHECK_TRUE_DIVISION", "REVIEW")
        if isinstance(node, ast.Call):
            name = qualified(node.func)
            if name.startswith(("math.", "cmath.", "numpy.")) and name.rsplit(".", 1)[-1] in APPROX_CALLS:
                emit(node, "ANALYTIC_APPROXIMATION_CALL", "ERROR")
            if name.rsplit(".", 1)[-1] in {"isclose", "allclose", "round"}:
                emit(node, "TOLERANCE_OR_ROUNDING_OBSERVER", "REVIEW")
            if name.startswith("numpy.") and "float" in name:
                emit(node, "NUMPY_FLOAT_CONSTRUCTION", "ERROR")
            for keyword in node.keywords:
                if keyword.arg == "dtype" and isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str) and ("float" in keyword.value.value or "complex" in keyword.value.value):
                    emit(node, "APPROXIMATE_DTYPE", "ERROR")
    return {"path": str(path), "findings": sorted(findings, key=lambda x: (x["line"], x["rule"])),
            "exact_rational_import_present": any(v == "fractions.Fraction" for v in imports.values())}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    files = sorted({p for root in args.paths for p in (root.rglob("*.py") if root.is_dir() else [root])})
    rows = [scan_file(p) for p in files]
    summary = {"schema": "EM_NUMERIC_AST_INVENTORY_V1", "scope": "EXACTLY_LISTED_FILES_ONLY",
               "whole_program_proof": False, "files_scanned": len(rows),
               "errors": sum(f["severity"] == "ERROR" for row in rows for f in row["findings"]),
               "reviews": sum(f["severity"] == "REVIEW" for row in rows for f in row["findings"]), "files": rows}
    content = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    print(content, end="")
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
