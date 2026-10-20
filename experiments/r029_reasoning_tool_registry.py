#!/usr/bin/env python3
"""R029 typed reasoning-tool registry utilities.

Research-only infrastructure. The registry selects tools; it does not turn
diagnostics or philosophy lenses into theorem evidence.
"""
from __future__ import annotations
from pathlib import Path
import json
import re
from typing import Any, Dict, Iterable, List

TRUST_CLASSES = {
    "PROOF_PRESERVING",
    "EXACT_SEMANTIC_TRANSFORMATION",
    "ADVERSARIAL_DIAGNOSTIC",
    "INTERPRETIVE_LENS",
}
DISPOSITIONS = {"KEEP", "NARROW", "MERGE", "KILL", "INTERPRETIVE_ONLY"}
REQUIRED_TOOL_FIELDS = {
    "id","name","layer","status","disposition","trust_class",
    "input_types","output_types","preconditions","transformation_or_question",
    "preserves","may_destroy_or_not_preserve","trigger_signals",
    "required_evidence","kill_tests","known_counterexamples","prior_art_root",
    "project_specific_residue","composition_notes","executable_oracle",
    "lean_declaration","source_refs","examples","anti_examples",
    "quality_metrics",
}
STRUCTURAL_TAG_TO_LAYER = {
    "lean":"EPISTEMIC","validation":"EPISTEMIC","proof":"EPISTEMIC",
    "carrier":"ONTOLOGY","precision":"ONTOLOGY","projection":"ONTOLOGY",
    "runtime":"ONTOLOGY","resource":"ONTOLOGY","cache":"ONTOLOGY",
    "future":"MODAL","future-language":"MODAL","horizon":"MODAL","credit":"CAUSAL",
    "causal":"CAUSAL","counterexample":"GENERATOR","regime":"GENERATOR",
    "prior-art":"REDUCTION","novelty":"REDUCTION","rooting":"REDUCTION",
    "quotient":"DYNAMIC","composition":"DYNAMIC","brc":"DYNAMIC",
}

def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]

def default_registry_path() -> Path:
    return repo_root() / "reasoning_tools.json"

def load_registry(path: str | Path | None = None) -> Dict[str, Any]:
    p = Path(path) if path else default_registry_path()
    raw = json.loads(p.read_text(encoding="utf-8"))
    if raw.get("tool_shards"):
        rows = []
        for rel in raw["tool_shards"]:
            shard = json.loads((p.parent / rel).read_text(encoding="utf-8"))
            if shard.get("schema_version") != "R029_REASONING_TOOL_SHARD_V1":
                raise ValueError(f"bad reasoning-tool shard schema: {rel}")
            rows.extend(shard.get("compact_tools", []))
        raw = dict(raw)
        raw["compact_tools"] = rows
    defaults = raw.get("tool_defaults", {})
    profiles = raw.get("layer_profiles", {})
    if raw.get("compact_tools"):
        fields = raw.get("compact_tool_fields", [])
        unpacked = []
        for row in raw["compact_tools"]:
            item = {fields[i]: value for i, value in enumerate(row)}
            pats = item.pop("trigger_patterns", []) or []
            aliases = item.pop("trigger_aliases", []) or []
            reuse = item.pop("reuse", None)
            item["name"] = item["id"].replace("_", " ").title()
            item["trigger_signals"] = [{
                "claim_patterns": pats, "semantic_aliases": aliases,
                "structural_weight": 2, "keyword_weight": 1,
            }]
            if reuse is not None:
                item["quality_metrics"] = {"reuse": reuse}
            unpacked.append(item)
        raw = dict(raw)
        raw["tools"] = unpacked
    if defaults or profiles:
        expanded = []
        for item in raw.get("tools", []):
            tool = dict(defaults)
            tool.update(profiles.get(item.get("layer"), {}))
            tool.update(item)
            if "prior_art_root" in item:
                root = dict(defaults.get("prior_art_root", {}))
                root.update(item["prior_art_root"])
                tool["prior_art_root"] = root
            expanded.append(tool)
        raw = dict(raw)
        raw["tools"] = expanded
    return raw

def tool_index(registry: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {t["id"]: t for t in registry["tools"]}

def validate_registry(registry: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    if registry.get("schema_version") != "R029_REASONING_TOOLS_V1":
        errors.append("bad schema_version")
    ids: List[str] = []
    for i, tool in enumerate(registry.get("tools", [])):
        missing = sorted(REQUIRED_TOOL_FIELDS - set(tool))
        if missing:
            errors.append(f"tool[{i}] {tool.get('id')} missing fields: {missing}")
        tid = tool.get("id")
        if not tid or not re.fullmatch(r"[A-Z0-9_]+", tid):
            errors.append(f"tool[{i}] invalid id: {tid!r}")
        ids.append(tid)
        if tool.get("trust_class") not in TRUST_CLASSES:
            errors.append(f"{tid}: invalid trust_class")
        if tool.get("disposition") not in DISPOSITIONS:
            errors.append(f"{tid}: invalid disposition")
        if not tool.get("preconditions"):
            errors.append(f"{tid}: missing preconditions")
        if not tool.get("preserves"):
            errors.append(f"{tid}: missing preserves")
        if not tool.get("may_destroy_or_not_preserve"):
            errors.append(f"{tid}: missing non-preservation boundary")
        if not tool.get("kill_tests"):
            errors.append(f"{tid}: missing kill_tests")
        if not tool.get("anti_examples"):
            errors.append(f"{tid}: missing anti_examples")
        root = tool.get("prior_art_root") or {}
        if not root.get("family") or not root.get("references"):
            errors.append(f"{tid}: incomplete prior_art_root")
        if tool.get("trust_class") == "INTERPRETIVE_LENS" and tool.get("disposition") != "INTERPRETIVE_ONLY":
            errors.append(f"{tid}: interpretive lens must be INTERPRETIVE_ONLY")
        if tool.get("disposition") == "MERGE" and not tool.get("merge_target"):
            errors.append(f"{tid}: MERGE without merge_target")
    if len(ids) != len(set(ids)):
        errors.append("duplicate tool id")
    index = tool_index(registry)
    for tool in registry.get("tools", []):
        if tool.get("merge_target") and tool["merge_target"] not in index:
            errors.append(f"{tool['id']}: unknown merge_target {tool['merge_target']}")
    return errors

def can_contribute_theorem_evidence(tool: Dict[str, Any], *, certificate_present: bool = False) -> bool:
    """Registry class alone never creates evidence.

    PROOF_PRESERVING and EXACT_SEMANTIC_TRANSFORMATION can contribute only when
    the corresponding proof/certificate is actually present.
    """
    tc = tool["trust_class"]
    return bool(certificate_present and tc in {"PROOF_PRESERVING","EXACT_SEMANTIC_TRANSFORMATION"})

def _norm_text(metadata: Dict[str, Any]) -> str:
    chunks = [
        str(metadata.get("claim_text","")),
        " ".join(map(str, metadata.get("task_tags",[]))),
        " ".join(map(str, metadata.get("semantic_hints",[]))),
        " ".join(map(str, metadata.get("input_types",[]))),
    ]
    return " ".join(chunks).lower()

def _layer_hints(metadata: Dict[str, Any]) -> set[str]:
    layers: set[str] = set()
    for tag in metadata.get("task_tags", []):
        key = str(tag).lower()
        if key in STRUCTURAL_TAG_TO_LAYER:
            layers.add(STRUCTURAL_TAG_TO_LAYER[key])
    return layers

def score_tool(tool: Dict[str, Any], metadata: Dict[str, Any]) -> tuple[int, List[str]]:
    text = _norm_text(metadata)
    layers = _layer_hints(metadata)
    score = 0
    reasons: List[str] = []
    if tool["layer"] in layers:
        score += 5
        reasons.append("structural-layer-match")
    for trigger in tool.get("trigger_signals", []):
        for alias in trigger.get("semantic_aliases", []):
            if alias.lower() in text:
                score += int(trigger.get("structural_weight",2))
                reasons.append(f"semantic:{alias}")
        hits = 0
        for pat in trigger.get("claim_patterns", []):
            if pat.lower() in text:
                hits += 1
        if hits:
            add = min(3, hits) * int(trigger.get("keyword_weight",1))
            score += add
            reasons.append(f"keyword-hits:{hits}")
    # Type compatibility is stronger than wording.
    required_inputs = {str(x).lower() for x in metadata.get("input_types", [])}
    tool_inputs = {str(x).lower() for x in tool.get("input_types", [])}
    if required_inputs and tool_inputs & required_inputs:
        score += 4
        reasons.append("input-type-match")
    # The theorem-evidence lane prefers tools that can carry certified evidence,
    # but diagnostics are still useful as guards.
    if metadata.get("evidence_goal") == "theorem" and tool["trust_class"] in {
        "PROOF_PRESERVING","EXACT_SEMANTIC_TRANSFORMATION"
    }:
        score += 2
        reasons.append("evidence-lane-compatible")
    # Suppress a canonical keyword false positive: validation prose is not
    # automatically a mathematical universal claim.
    claim = str(metadata.get("claim_text","")).lower().strip()
    tags = {str(x).lower() for x in metadata.get("task_tags",[])}
    if tool["id"] == "QUANTIFIER_SCOPE_CHECK" and "all tests passed" in claim and not (
        {"theorem","minimality","exhaustive"} & tags
    ):
        score -= 5
        reasons.append("validation-all-suppression")
    # Merged aliases should not compete with their canonical target.
    if tool.get("disposition") == "MERGE":
        score -= 2
        reasons.append("alias-penalty")
    # Interpretive lenses stay opt-in unless philosophy/ontology/explanation is explicit.
    if tool["trust_class"] == "INTERPRETIVE_LENS" and not (
        {"philosophy","ontology","foundation"} & tags or
        any(w in claim for w in ("explains","ontolog","reduces to","primitive"))
    ):
        score -= 4
        reasons.append("lens-sparsity-penalty")
    return score, reasons

def rank_tools(registry: Dict[str, Any], metadata: Dict[str, Any],
               *, max_advisory: int | None = None) -> Dict[str, Any]:
    max_advisory = max_advisory or int(registry["selection_policy"]["max_default_advisory_tools"])
    rows = []
    for tool in registry["tools"]:
        score, reasons = score_tool(tool, metadata)
        if score > 0:
            rows.append({"id":tool["id"],"score":score,"trust_class":tool["trust_class"],
                         "disposition":tool["disposition"],"reasons":reasons})
    rows.sort(key=lambda r:(-r["score"], r["id"]))
    exact = [r for r in rows if r["trust_class"] in {"PROOF_PRESERVING","EXACT_SEMANTIC_TRANSFORMATION"}
             and r["disposition"] not in {"MERGE","KILL","INTERPRETIVE_ONLY"}]
    advisory = [r for r in rows if r["trust_class"] in {"ADVERSARIAL_DIAGNOSTIC","INTERPRETIVE_LENS"}
                and r["disposition"] not in {"MERGE","KILL"}][:max_advisory]
    return {
        "required_exact_or_proof_preserving": exact,
        "advisory_diagnostic_or_generator": advisory,
        "all_positive_candidates": rows,
    }

def resolve_alias(registry: Dict[str, Any], tool_id: str) -> str:
    t = tool_index(registry)[tool_id]
    return t.get("merge_target") or tool_id

def main() -> int:
    reg = load_registry()
    errors = validate_registry(reg)
    if errors:
        print(json.dumps({"ok":False,"errors":errors},indent=2))
        return 1
    print(json.dumps({
        "ok":True,
        "tool_count":len(reg["tools"]),
        "trust_counts":{tc:sum(t["trust_class"]==tc for t in reg["tools"]) for tc in sorted(TRUST_CLASSES)},
    },indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
