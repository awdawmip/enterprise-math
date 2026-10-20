#!/usr/bin/env python3
"""R032 pull-based Exploration Muse.

Tools are dormant until the researcher explicitly requests inspiration. Retrieval
optimizes shelf and representation diversity rather than correctness ranking.
"""
from __future__ import annotations
import argparse, json, math, random
from collections import Counter
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "research_muse_registry.json"
ALLOWED = {"STUCK","NEED_NEW_IDEAS","SEARCH_TOOL_LIBRARY","EXPLICIT_ANALOGY_REQUEST","EXPLICIT_DIFFERENT_DIRECTIONS_REQUEST"}

def load_registry(path: Path = REGISTRY_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def startup_payload(registry: dict | None = None) -> dict:
    registry = registry or load_registry()
    return {"state": registry["default_state"], "recommended_tools": [], "recommended_analogies": [], "recommended_mutations": [], "historical_warnings": []}

def _tags(item: dict) -> set[str]:
    raw = item.get("tags", [])
    if raw: return set(raw)
    text = " ".join(str(item.get(k,"")) for k in ("id","layer","question","prompt","domain")).lower()
    return set(text.replace("_"," ").split())

def _overlap_score(item: dict, context_tags: set[str]) -> int:
    return len(_tags(item) & {x.lower() for x in context_tags})

def _round_robin_diverse(items: list[dict], context_tags: set[str], key: str, limit: int) -> list[dict]:
    remaining, selected, used = list(items), [], Counter()
    while remaining and len(selected) < limit:
        ranked = sorted(remaining, key=lambda x: (-(_overlap_score(x, context_tags)*10 - 7*used[x.get(key,"UNKNOWN")]), x.get("id","")))
        pick = ranked[0]; selected.append(pick); used[pick.get(key,"UNKNOWN")] += 1; remaining.remove(pick)
    return selected

def semantic_nearest_tool_control(context_tags: Iterable[str], limit: int = 4, registry: dict | None = None) -> list[dict]:
    registry = registry or load_registry(); tags = set(context_tags)
    return sorted(registry["tool_shelf"], key=lambda x: (-_overlap_score(x,tags), x["id"]))[:limit]

def request_muse(trigger: str, context_tags: Iterable[str], *, seed: int = 0, registry: dict | None = None) -> dict:
    registry = registry or load_registry()
    if trigger not in ALLOWED: raise PermissionError(f"MUSE_TRIGGER_FORBIDDEN:{trigger}")
    tags, rng = set(context_tags), random.Random(seed)
    tools = _round_robin_diverse(registry["tool_shelf"], tags, "layer", 4)
    analogies = _round_robin_diverse(registry["analogy_shelf"], tags, "domain", 3)
    mutations = list(registry["mutation_shelf"]); rng.shuffle(mutations); mutations = mutations[:3]
    strange_ranked = sorted(registry["strange_tools"], key=lambda x: (_overlap_score(x,tags), rng.random()))
    return {"trigger":trigger,"selection_objective":"EXPLORATION_BRANCH_DIVERSITY_NOT_CORRECTNESS_RANKING","tool_shelf":tools,"analogy_shelf":analogies,"mutation_shelf":mutations,"strange_tool":strange_ranked[:1],"disclaimer":"ANALOGY_IS_GENERATOR_NOT_EVIDENCE","ranking_disclaimer":"Shelf order is not a claim that the first item is best or historically correct."}

def shannon_entropy(values: Iterable[str]) -> float:
    counts=Counter(values); n=sum(counts.values())
    return 0.0 if not n else -sum((c/n)*math.log2(c/n) for c in counts.values())

def retrieval_diversity_evidence(queries: list[list[str]] | None = None, seeds: int = 32) -> dict:
    queries = queries or [["future","composition","state"],["scalar","credit","order"],["phase","regime","threshold"],["evidence","proof","scope"],["carrier","support","count"]]
    reg=load_registry(); rows=[]
    for qi,tags in enumerate(queries):
        nearest=semantic_nearest_tool_control(tags,4,reg); near_layers=[x["layer"] for x in nearest]; diversified_layers=[]; strange_domains=set()
        for seed in range(seeds):
            out=request_muse("NEED_NEW_IDEAS",tags,seed=qi*1000+seed,registry=reg)
            diversified_layers.extend(x["layer"] for x in out["tool_shelf"]); strange_domains.update(x["domain"] for x in out["strange_tool"])
        rows.append({"tags":tags,"semantic_nearest_unique_layers":len(set(near_layers)),"semantic_nearest_layer_entropy":shannon_entropy(near_layers),"muse_unique_layers_across_draws":len(set(diversified_layers)),"muse_layer_entropy_across_draws":shannon_entropy(diversified_layers),"strange_domains_seen":sorted(strange_domains)})
    return {"queries":rows,"all_muse_queries_have_at_least_as_many_layers_as_nearest":all(r["muse_unique_layers_across_draws"]>=r["semantic_nearest_unique_layers"] for r in rows),"note":"Deterministic registry-geometry check, not evidence of human scientific productivity."}

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--demo",action="store_true"); a=p.parse_args()
    print(json.dumps(request_muse("STUCK",["scalar","future","composition"],seed=7) if a.demo else retrieval_diversity_evidence(),indent=2)); return 0

if __name__ == "__main__": raise SystemExit(main())
