"""Check this one source substitution and its metadata; never run a spectrum."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


METHOD = "candidate.x6.shortest_path_valuation_spectrum"
SHARD = "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json"
MODULE = "research_notes/owner_arithmetic_20260907.py"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def raw_methods(data: bytes) -> dict[str, str]:
    text = data.decode("utf-8")
    position = text.index("[", text.index('"methods"')) + 1
    decoder = json.JSONDecoder()
    result = {}
    while True:
        while text[position].isspace() or text[position] == ",":
            position += 1
        if text[position] == "]":
            return result
        value, end = decoder.raw_decode(text, position)
        result[value["method_id"]] = text[position:end]
        position = end


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    package = Path(__file__).resolve().parent
    old_data = package.joinpath("frozen", SHARD).read_bytes()
    new_data = root.joinpath(SHARD).read_bytes()
    old, new = json.loads(old_data), json.loads(new_data)
    before, after = ({row["method_id"]: row for row in value["methods"]} for value in (old, new))
    assert list(before) == list(after) and len(before) == 19
    old_raw, new_raw = raw_methods(old_data), raw_methods(new_data)
    protected = {}
    for mid in before:
        if mid != METHOD:
            assert before[mid] == after[mid] and old_raw[mid] == new_raw[mid], mid
            protected[mid] = sha(old_raw[mid].encode())
    assert {k: v for k, v in old.items() if k not in {"methods", "provenance"}} == {
        k: v for k, v in new.items() if k not in {"methods", "provenance"}}
    assert set(new["provenance"]) == set(old["provenance"]) | {"valuation_digits_brc_checkpoint"}
    assert all(new["provenance"][key] == value for key, value in old["provenance"].items())
    old_target, target = before[METHOD], after[METHOD]
    allowed = {"source_sha256", "validation_refs", "partial_runtime_evidence"}
    assert {k: v for k, v in old_target.items() if k not in allowed} == {
        k: v for k, v in target.items() if k not in allowed}
    assert set(target) == set(old_target) | {"partial_runtime_evidence"}
    assert target["validation_refs"][:len(old_target["validation_refs"])] == old_target["validation_refs"]
    for path, pin in old_target["source_sha256"].items():
        if path != MODULE:
            assert target["source_sha256"][path] == pin
    pins = target["source_sha256"]
    assert set(pins) == set(target["source_refs"] + target["validation_refs"])
    for path, pin in pins.items():
        assert sha(root.joinpath(path).read_bytes()) == pin, path
    source = root.joinpath(MODULE).read_bytes()
    assert source == package.joinpath("owner_arithmetic_20260907.candidate.py").read_bytes()
    assert sha(source) == "209c5f38dee8dcd0f61b895ef3c2b1e3d4e2b46724bb3bf7326dd210f813b2ce"
    prior = package.joinpath("frozen", MODULE).read_bytes()
    marker = b"@lru_cache(maxsize=256)"
    assert prior[prior.index(marker):] == source[source.index(marker):]
    tree = ast.parse(source)
    helper = next(item for item in tree.body if getattr(item, "name", None) == "digits_lsd")
    assert not [item for item in ast.walk(helper) if isinstance(item, (ast.Div, ast.FloorDiv, ast.Mod))
                or isinstance(item, ast.Name) and item.id in {"divmod", "Fraction", "Decimal"}]
    boundary = target["partial_runtime_evidence"]
    assert boundary["whole_runtime_certified"] is False and boundary["public_api_returns_or_persists_digit_trace"] is False
    assert boundary["historical_full_spectrum_validation"]["source_commit"] == "909ed4c3c81adca8d5d653994a83df316faf1365"
    loader = root.joinpath("tools/enterprise_toolbox.py")
    spec = importlib.util.spec_from_file_location("valuation_metadata_toolbox", loader)
    toolbox = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(toolbox)
    inventory = toolbox.load_method_inventory()
    assert [row for row in inventory["methods"] if row["method_id"] == METHOD] == [target]
    queries = []
    for query, mode in ((target["triggers"][0], "existing English trigger"),
                        (METHOD + " " + target["triggers"][-1], "exact method ID plus existing Chinese trigger")):
        hits = toolbox.method_suggestions(query, inventory=inventory)
        assert METHOD in {row["method_id"] for row in hits}
        queries.append({"query": query, "mode": mode, "target_hit": True})
    package_manifest = json.loads(package.joinpath("package_manifest.json").read_text(encoding="utf-8"))
    for path, pin in package_manifest["archived_files"].items():
        assert sha(package.joinpath(path).read_bytes()) == pin["sha256"], path
    assert "enterprise_math" not in sys.modules
    result = {
        "status": "PASS_SOURCE_PIN_METADATA_AND_HELPER_STATIC_ONLY",
        "executed_utc": datetime.now(timezone.utc).isoformat(),
        "argv": [sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()),
                 "--root", str(root), "--receipt", str(args.receipt)],
        "executed_script_sha256": sha(Path(__file__).read_bytes()),
        "source_module_sha256": sha(source), "source_shard_sha256": sha(new_data),
        "historical_shard_sha256": sha(old_data),
        "protected_other_eighteen_raw_objects_sha256": protected,
        "unchanged_public_api_carry_output_suffix_sha256": sha(source[source.index(marker):]),
        "canonical_loader_path": str(loader), "canonical_loader_sha256": sha(loader.read_bytes()),
        "target_occurrences": 1, "queries": queries, "target_pins_checked": pins,
        "query_boundary": "The existing ASCII tokenizer does not support the bare Han-only trigger. Its exact-ID-anchored query is verified here; loader and original triggers are unchanged.",
        "helper_static_scope": "Only digits_lsd AST; no whole-file/transitive compliance claim.",
        "history": "The archived 288-facade-call receipt remains byte-identical; not rerun by this metadata validation.",
        "runtime_executed": False, "whole_runtime_certified": False,
        "formal_acceptance": None, "main_admission": "NOT_PERFORMED",
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    if args.receipt.exists():
        raise SystemExit("refusing to overwrite an existing validation receipt")
    args.receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "other_raw_objects_preserved": len(protected),
                      "target_occurrences": 1, "queries": len(queries),
                      "receipt_sha256": sha(args.receipt.read_bytes())}))


if __name__ == "__main__":
    main()
