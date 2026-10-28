"""Parse the frozen checker as data; never import, compile, or execute it.

This is a syntactic coverage aid, not a replacement certificate checker.
Usage: python3 scan_finite_checker_static.py PATH_TO_CHECKER [OUTPUT_JSON]
"""
import ast
import hashlib
import json
from pathlib import Path
import sys

EXPECTED = "5689152e970b652a8e40c3c120eda3b45320c8745968a5cb416fa9b9dbdc5385"


def scan(path):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED:
        raise ValueError("Frozen checker bytes do not match the reviewed source")
    source = raw.decode("utf-8")
    tree = ast.parse(source, filename=str(path))
    findings = {"assertion_sites": [], "strict_comparison_calls": [],
                "near_calls": [], "sqrt_calls": []}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            findings["assertion_sites"].append({"line": node.lineno,
                "condition": ast.unparse(node.test)})
        if isinstance(node, ast.Call):
            name = ast.unparse(node.func)
            key = {"lt": "strict_comparison_calls", "near": "near_calls"}.get(name)
            if isinstance(node.func, ast.Attribute) and node.func.attr == "sqrt":
                key = "sqrt_calls"
            if key:
                findings[key].append({"line": node.lineno,
                    "expression": ast.get_source_segment(source, node)})
    for entries in findings.values():
        entries.sort(key=lambda x: x["line"])
    return {"schema": "STATIC_SOURCE_AUDIT_V1", "checker_sha256": digest,
        "checker_executed": False, "checker_imported": False,
        "counts_are_syntactic_sites_not_runtime_counts": True,
        "counts": {k: len(v) for k, v in findings.items()}, **findings}


if __name__ == "__main__":
    result = json.dumps(scan(sys.argv[1]), indent=2) + "\n"
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(result)
    else:
        print(result, end="")
