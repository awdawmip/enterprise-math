#!/usr/bin/env python3
"""R029 reasoning-tool registry oracle and mutation runner."""
from __future__ import annotations
from pathlib import Path
import json
from typing import Any, Dict, List

from r029_reasoning_tool_registry import load_registry, tool_index, validate_registry, rank_tools

ROOT = Path(__file__).resolve().parents[1]
COMPOSITION = ROOT / "R029_TOOL_COMPOSITION_MATRIX.json"
KILLS = ROOT / "R029_UNIVERSAL_REASONING_KILL_FIXTURES.json"

def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def validate_composition_matrix(matrix: Dict[str, Any], registry: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    allowed = {"ALWAYS_SAFE","SAFE_WITH_PRECONDITIONS","DIAGNOSTIC_ONLY","KNOWN_INVALID"}
    index = tool_index(registry)
    for i, rule in enumerate(matrix.get("rules", [])):
        for side in ("left","right"):
            if rule.get(side) not in index:
                errors.append(f"rule[{i}] unknown {side}: {rule.get(side)}")
        if rule.get("class") not in allowed:
            errors.append(f"rule[{i}] invalid class")
        if rule.get("class") == "SAFE_WITH_PRECONDITIONS" and not rule.get("conditions"):
            errors.append(f"rule[{i}] conditional rule has no conditions")
        if rule.get("class") == "KNOWN_INVALID" and not rule.get("minimal_counterexample"):
            errors.append(f"rule[{i}] invalid composition missing counterexample")
    pipeline = matrix.get("recommended_pipeline",{}).get("steps",[])
    for tid in pipeline:
        if tid not in index:
            errors.append(f"pipeline unknown tool: {tid}")
    return errors

def validate_kill_fixtures(kills: Dict[str, Any], registry: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    index = tool_index(registry)
    expected_ids = {
        "LOGIC_TOOL_IS_ALWAYS_PROOF_PRESERVING",
        "PHILOSOPHY_LENS_CAN_BE_USED_AS_THEOREM",
        "MORE_CONTEXT_ALWAYS_HELPS",
        "EVERY_HISTORICAL_DISTINCTION_SHOULD_BE_INJECTED_EVERYWHERE",
        "ONE_UNIVERSAL_REASONING_CHECKLIST_SUITS_ALL_TASKS",
        "TRIGGER_KEYWORD_MATCH_IS_SEMANTICALLY_COMPLETE",
        "A_TOOL_THAT_HELPED_ONCE_IS_REUSABLE",
        "TOOL_COMPOSITION_IS_AUTOMATICALLY_SAFE",
        "PRIOR_ART_ROOTING_DESTROYS_PROJECT_SPECIFIC_VALUE",
        "THE_RESEARCH_REASONING_KERNEL_SHOULD_BECOME_A_NEW_MATHEMATICAL_FOUNDATION_PRIMITIVE",
    }
    got = {x.get("id") for x in kills.get("claims",[])}
    if got != expected_ids:
        errors.append(f"kill fixture ids mismatch missing={sorted(expected_ids-got)} extra={sorted(got-expected_ids)}")
    for row in kills.get("claims",[]):
        if row.get("verdict") != "KILLED":
            errors.append(f"{row.get('id')}: verdict not KILLED")
        if not row.get("counterexample") or not row.get("survival_condition"):
            errors.append(f"{row.get('id')}: missing counterexample/survival condition")
        for tid in row.get("killed_by",[]):
            if tid not in index:
                errors.append(f"{row.get('id')}: unknown killed_by tool {tid}")
    return errors

def trigger_mutation_results(registry: Dict[str, Any]) -> Dict[str, bool]:
    def ids(meta):
        ranked = rank_tools(registry, meta, max_advisory=12)
        return {r["id"] for r in ranked["all_positive_candidates"]}
    return {
        # False positive guard: "all" in validation sentence is not by itself a theorem quantifier.
        "keyword_false_positive_guard":
            "QUANTIFIER_SCOPE_CHECK" not in ids({"claim_text":"all tests passed","task_tags":["validation"]}),
        # False negative guard: semantic continuation language without literal word "future".
        "semantic_alias_future_trigger":
            "FUTURE_LANGUAGE_RELATIVITY" in ids({
                "claim_text":"the quotient must be closed under arbitrary continuations",
                "task_tags":["precision"]
            }),
        "root_coverage_trigger":
            "ROOT_COVERAGE_EVIDENCE_CHECK" in ids({
                "claim_text":"Lean build pass is claimed to validate the module; check root import coverage",
                "task_tags":["Lean","validation"]
            }),
        "one_step_composition_trigger":
            "ONE_STEP_EXACT_NOT_COMPOSITION_SAFE" in ids({
                "claim_text":"the one-step exact quotient is reused for two-step composition",
                "task_tags":["quotient","composition"]
            }),
        "retrospective_credit_trigger":
            "DECLARED_VS_REALIZED_FUTURE" in ids({
                "claim_text":"feature had zero hindsight credit on the realized path and may be deleted",
                "task_tags":["credit","causal"]
            }),
        "prior_art_trigger":
            "PRIOR_ART_REDUCTION" in ids({
                "claim_text":"is this new or equivalent to a known algorithm?",
                "task_tags":["prior-art","novelty"]
            }),
    }

def run_all() -> Dict[str, Any]:
    reg = load_registry()
    comp = load_json(COMPOSITION)
    kills = load_json(KILLS)
    registry_errors = validate_registry(reg)
    composition_errors = validate_composition_matrix(comp,reg)
    kill_errors = validate_kill_fixtures(kills,reg)
    mutations = trigger_mutation_results(reg)
    return {
        "ok": not registry_errors and not composition_errors and not kill_errors and all(mutations.values()),
        "registry_errors":registry_errors,
        "composition_errors":composition_errors,
        "kill_errors":kill_errors,
        "trigger_mutations":mutations,
        "tool_count":len(reg["tools"]),
        "composition_rule_count":len(comp.get("rules",[])),
        "kill_fixture_count":len(kills.get("claims",[])),
    }

def main() -> int:
    result = run_all()
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
