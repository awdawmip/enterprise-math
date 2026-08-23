#!/usr/bin/env python3
"""Search the Enterprise Math shared toolbox before inventing new machinery.

This router is deliberately lightweight. It reads the curated tool-family registry,
the base harvested method inventory plus dated addenda, and (when available) the
current executable Python surface. It never imports source modules while searching,
so discovery has no runtime side effects.

FREE axiom-discovery Phase A must not use this catalog as a discovery prior. The
control-plane timing rule lives in ``tool_invocation_policy.json``.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "enterprise_toolbox_registry.json"
METHOD_INVENTORY_PATH = ROOT / "research_method_inventory.json"
METHOD_INVENTORY_ADDENDA_ROOT = ROOT / "research_method_inventory_addenda"
SOURCE_ROOT = ROOT / "src" / "enterprise_math"

TOKEN_RE = re.compile(r"[A-Za-z0-9_+.-]+")
SYNONYMS: dict[str, tuple[str, ...]] = {
    "count": ("count", "enumeration", "cardinality", "scale", "shell", "valuation"),
    "growth": ("growth", "scale", "shell", "difference", "enumeration"),
    "glue": ("glue", "gluing", "compatibility", "holonomy", "cocycle", "transport"),
    "gluing": ("glue", "gluing", "compatibility", "holonomy", "cocycle", "transport"),
    "path": ("path", "provenance", "circuit", "brc", "transition", "trace", "closure", "bellman"),
    "quotient": ("quotient", "projection", "collapse", "fiber", "predictive", "descent"),
    "coarse": ("coarse", "precision", "projection", "refinement", "quotient"),
    "precision": ("precision", "refinement", "coarse", "fine", "carry", "borrow", "detail"),
    "symmetry": ("symmetry", "group", "orbit", "stabilizer", "equivariant", "relabeling"),
    "canonical": ("canonical", "choice", "symmetry", "fixed", "equivariant"),
    "relation": ("relation", "correspondence", "support", "spectrum", "observable", "multivalued"),
    "collision": ("collision", "fiber", "capacity", "overlap", "witness", "spectrum"),
    "constraint": ("constraint", "certificate", "compatibility", "helly", "obstruction", "feasible"),
    "cycle": ("cycle", "circuit", "cocircuit", "holonomy", "loop", "provenance", "toppling"),
    "stabilize": ("stabilize", "stabilization", "toppling", "odometer", "least action"),
    "stabilization": ("stabilize", "stabilization", "toppling", "odometer", "least action"),
    "morse": ("morse", "acyclic", "matching", "chain", "homotopy", "critical"),
    "energy": ("energy", "dirichlet", "thomson", "resistance", "weighted", "quadratic"),
    "tropical": ("tropical", "min-plus", "max-plus", "idempotent", "kleene", "bellman", "residuation"),
    "voronoi": ("voronoi", "delaunay", "nearest", "empty ball", "dual cell"),
    "conformal": ("conformal", "circle packing", "circle pattern", "curvature", "vertex scaling"),
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_method_inventory() -> dict[str, Any]:
    """Return base method inventory plus all dated addenda, preserving base compatibility."""
    base = load_json(METHOD_INVENTORY_PATH)
    methods = list(base.get("methods", []))
    addenda: list[str] = []
    if METHOD_INVENTORY_ADDENDA_ROOT.exists():
        for path in sorted(METHOD_INVENTORY_ADDENDA_ROOT.glob("*.json")):
            shard = load_json(path)
            methods.extend(shard.get("methods", []))
            addenda.append(str(path.relative_to(ROOT)))
    ids = [str(method.get("method_id", "")) for method in methods]
    if len(ids) != len(set(ids)):
        duplicates = sorted({method_id for method_id in ids if ids.count(method_id) > 1})
        raise ValueError(f"duplicate method_id across inventory/addenda: {duplicates}")
    return {**base, "methods": methods, "loaded_addenda": addenda}


def _tokens(text: str) -> set[str]:
    base = {token.lower() for token in TOKEN_RE.findall(text.replace("/", " "))}
    expanded = set(base)
    for token in tuple(base):
        expanded.update(SYNONYMS.get(token, ()))
    return expanded


def _record_text(record: dict[str, Any]) -> str:
    fields = [
        record.get("id", ""),
        record.get("method_id", ""),
        record.get("name", ""),
        record.get("description", ""),
        record.get("scope", ""),
        record.get("hard_boundary", ""),
        record.get("note", ""),
        " ".join(record.get("triggers", [])),
        " ".join(record.get("capabilities", [])),
        " ".join(record.get("api", [])),
        " ".join(record.get("tags", [])),
        " ".join(record.get("reusable_for", [])),
    ]
    return " ".join(str(field) for field in fields)


def _score(query: str, record: dict[str, Any]) -> int:
    need = _tokens(query)
    hay = _tokens(_record_text(record))
    if not need:
        return 0
    overlap = need & hay
    score = 3 * len(overlap)
    q = query.lower()
    for trigger in record.get("triggers", []):
        if str(trigger).lower() in q:
            score += 4
    identifier = str(record.get("id", record.get("method_id", ""))).lower()
    if identifier and identifier in q:
        score += 8
    return score


def tool_suggestions(
    query: str, *, registry: dict[str, Any] | None = None, limit: int = 8
) -> list[dict[str, Any]]:
    registry = registry or load_json(REGISTRY_PATH)
    scored = [(_score(query, tool), tool) for tool in registry.get("tools", [])]
    return [
        {"score": score, **tool}
        for score, tool in sorted(scored, key=lambda item: (-item[0], item[1].get("id", "")))
        if score > 0
    ][:limit]


def method_suggestions(
    query: str, *, inventory: dict[str, Any] | None = None, limit: int = 12
) -> list[dict[str, Any]]:
    inventory = inventory or load_method_inventory()
    scored = [(_score(query, method), method) for method in inventory.get("methods", [])]
    return [
        {"score": score, **method}
        for score, method in sorted(
            scored, key=lambda item: (-item[0], item[1].get("method_id", ""))
        )
        if score > 0
    ][:limit]


def _module_record(path: Path) -> dict[str, Any] | None:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, UnicodeError):
        return None
    doc = ast.get_docstring(tree) or ""
    functions = [
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    ]
    classes = [
        node.name for node in tree.body if isinstance(node, ast.ClassDef) and not node.name.startswith("_")
    ]
    if not functions and not classes:
        return None
    return {
        "id": f"module:{path.stem}",
        "name": path.name,
        "description": doc.split("\n\n", 1)[0],
        "source_ref": str(path.relative_to(ROOT)),
        "api": functions + classes,
        "triggers": [path.stem.replace("_", " ")],
        "status": "CURRENT_EXECUTABLE_SOURCE_DISCOVERY",
    }


def module_suggestions(query: str, *, root: Path = SOURCE_ROOT, limit: int = 12) -> list[dict[str, Any]]:
    if not root.exists():
        return []
    records = [record for path in sorted(root.glob("*.py")) if (record := _module_record(path))]
    scored = [(_score(query, record), record) for record in records]
    return [
        {"score": score, **record}
        for score, record in sorted(scored, key=lambda item: (-item[0], item[1]["id"]))
        if score > 0
    ][:limit]


def coverage(query: str) -> dict[str, Any]:
    tools = tool_suggestions(query)
    methods = method_suggestions(query)
    modules = module_suggestions(query)
    if tools or methods or modules:
        verdict = "REUSE_CANDIDATE_FOUND"
        rule = "Inspect semantic preconditions and hard boundaries before deciding REUSE / COMPOSE / EXTEND_EXISTING_TOOL."
    else:
        verdict = "CAPABILITY_GAP_CANDIDATE_NOT_CONFIRMED"
        rule = "No lexical/semantic catalog match was found. Confirm the exact missing input/output capability before creating a new tool family."
    return {
        "query": query,
        "verdict": verdict,
        "tool_families": tools,
        "methods": methods,
        "executable_modules": modules,
        "next_rule": rule,
    }


def _print(data: Any, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    if isinstance(data, list):
        for item in data:
            key = item.get("id", item.get("method_id", "?"))
            print(f"{item.get('score', '-'):>3}  {key}  {item.get('name', '')}")
        return
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="list curated tool families")
    show = sub.add_parser("show", help="show one tool family")
    show.add_argument("tool_id")
    suggest = sub.add_parser("suggest", help="suggest tool families for a need")
    suggest.add_argument("query", nargs="+")
    method = sub.add_parser("methods", help="search harvested methods and dated addenda")
    method.add_argument("query", nargs="+")
    modules = sub.add_parser("modules", help="search current executable source without importing it")
    modules.add_argument("query", nargs="+")
    cov = sub.add_parser("coverage", help="run the full reuse-before-invention coverage lookup")
    cov.add_argument("query", nargs="+")

    args = parser.parse_args(list(argv) if argv is not None else None)
    registry = load_json(REGISTRY_PATH)
    if args.command == "list":
        _print(registry.get("tools", []), args.json)
    elif args.command == "show":
        match = next((tool for tool in registry.get("tools", []) if tool.get("id") == args.tool_id), None)
        if match is None:
            parser.error(f"unknown tool id: {args.tool_id}")
        _print(match, True if args.json else False)
    else:
        query = " ".join(args.query)
        if args.command == "suggest":
            _print(tool_suggestions(query), args.json)
        elif args.command == "methods":
            _print(method_suggestions(query), args.json)
        elif args.command == "modules":
            _print(module_suggestions(query), args.json)
        elif args.command == "coverage":
            _print(coverage(query), True if args.json else False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())