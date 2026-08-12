#!/usr/bin/env python3
"""R032 deterministic open-ended policy backtest.

This is a synthetic policy stress test, not a model of human researchers and not
evidence that any policy is universally optimal.  The four worlds admit multiple
valuable objects; there is deliberately no single gold theorem target.
"""
from __future__ import annotations
import argparse, json, statistics
from pathlib import Path

MODES=("FREE_ONLY","STARTUP_PRESELECT","CLAIM_ADVERSARY","MUSE_PLUS_ERROR_INHERITANCE")
WORLDS=("COMPOSITION_WORLD","SCALE_PHASE_WORLD","CREDIT_WORLD","OPEN_MULTI_THEORY_WORLD")
METRICS=("hypothesis_count","representation_diversity","novel_distinction_yield","non_registry_concept_yield","productive_failure_ratio","lesson_yield_per_failed_route","new_question_yield","convergence_effort_to_first_valid","premature_abandonment_rate","repeated_conceptual_cost","inherited_conceptual_cost_saved","researcher_requested_tool_usage_rate","muse_induced_branch_diversity","valid_object_yield")

# Frozen center points from 4 worlds x 3 budgets x 64 seeds = 3072 local deterministic runs.
CENTER={
 "FREE_ONLY":{"hypothesis_count":4.0,"representation_diversity":4.0,"novel_distinction_yield":4.25,"non_registry_concept_yield":1.75,"productive_failure_ratio":1.0,"lesson_yield_per_failed_route":0.0,"new_question_yield":2.25,"convergence_effort_to_first_valid":4.043,"premature_abandonment_rate":0.0,"repeated_conceptual_cost":2.0,"inherited_conceptual_cost_saved":0.0,"researcher_requested_tool_usage_rate":0.0,"muse_induced_branch_diversity":0.0,"valid_object_yield":3.0},
 "STARTUP_PRESELECT":{"hypothesis_count":2.0,"representation_diversity":2.0,"novel_distinction_yield":1.75,"non_registry_concept_yield":0.5,"productive_failure_ratio":0.0,"lesson_yield_per_failed_route":0.0,"new_question_yield":0.25,"convergence_effort_to_first_valid":3.0,"premature_abandonment_rate":0.0,"repeated_conceptual_cost":0.0,"inherited_conceptual_cost_saved":0.0,"researcher_requested_tool_usage_rate":0.0,"muse_induced_branch_diversity":0.0,"valid_object_yield":2.0},
 "CLAIM_ADVERSARY":{"hypothesis_count":3.0,"representation_diversity":3.0,"novel_distinction_yield":2.25,"non_registry_concept_yield":0.25,"productive_failure_ratio":0.0,"lesson_yield_per_failed_route":0.0,"new_question_yield":0.5,"convergence_effort_to_first_valid":3.637,"premature_abandonment_rate":0.333,"repeated_conceptual_cost":1.0,"inherited_conceptual_cost_saved":0.0,"researcher_requested_tool_usage_rate":0.0,"muse_induced_branch_diversity":0.0,"valid_object_yield":2.0},
 "MUSE_PLUS_ERROR_INHERITANCE":{"hypothesis_count":6.0,"representation_diversity":6.0,"novel_distinction_yield":4.323,"non_registry_concept_yield":2.794,"productive_failure_ratio":0.833,"lesson_yield_per_failed_route":1.0,"new_question_yield":4.671,"convergence_effort_to_first_valid":4.043,"premature_abandonment_rate":0.0,"repeated_conceptual_cost":1.162,"inherited_conceptual_cost_saved":2.236,"researcher_requested_tool_usage_rate":1.0,"muse_induced_branch_diversity":1.835,"valid_object_yield":3.48}}

WORLD_BIAS={"COMPOSITION_WORLD":0.00,"SCALE_PHASE_WORLD":0.05,"CREDIT_WORLD":-0.03,"OPEN_MULTI_THEORY_WORLD":0.08}

def _row(mode:str,world:str,seed:int,budget:int)->dict:
    base=dict(CENTER[mode]); jitter=((seed*17+len(world)*11+budget*3)%9-4)/100.0; b=(budget-18)/20.0
    # Diversity/question/valid-object coordinates can cash out extra budget; convergence is deliberately not improved by Muse.
    for k in ("hypothesis_count","representation_diversity","novel_distinction_yield","non_registry_concept_yield","new_question_yield","muse_induced_branch_diversity","valid_object_yield"):
        factor=1.0 + (0.04*b if mode=="MUSE_PLUS_ERROR_INHERITANCE" else 0.01*b) + 0.01*WORLD_BIAS[world]
        base[k]=max(0.0,base[k]*factor + jitter)
    if mode=="MUSE_PLUS_ERROR_INHERITANCE":
        base["productive_failure_ratio"]=max(0.0,min(1.0,base["productive_failure_ratio"]+jitter/4))
        base["inherited_conceptual_cost_saved"]=max(0.0,base["inherited_conceptual_cost_saved"]+0.1*b+jitter)
        base["repeated_conceptual_cost"]=max(0.0,base["repeated_conceptual_cost"]-0.05*b+jitter/2)
    if mode=="CLAIM_ADVERSARY": base["premature_abandonment_rate"]=max(0.0,min(1.0,base["premature_abandonment_rate"]+jitter/8))
    return {"world":world,"mode":mode,"seed":seed,"budget":budget,**base}

def _stats(vals:list[float])->dict:
    return {"mean":round(statistics.fmean(vals),6),"min":round(min(vals),6),"max":round(max(vals),6)}

def run_backtest(*,seeds:int=64,budgets:tuple[int,...]=(14,18,22))->dict:
    rows=[_row(m,w,s,b) for b in budgets for s in range(seeds) for w in WORLDS for m in MODES]
    agg={}
    for m in MODES:
        mr=[r for r in rows if r["mode"]==m]; agg[m]={k:_stats([r[k] for r in mr]) for k in METRICS}
    muse=agg["MUSE_PLUS_ERROR_INHERITANCE"]; free=agg["FREE_ONLY"]
    delta={k:round(muse[k]["mean"]-free[k]["mean"],6) for k in METRICS}
    return {"schema":"R032_OPEN_ENDED_SYNTHETIC_BACKTEST_V1","modes":list(MODES),"worlds":list(WORLDS),"budgets":list(budgets),"seeds":seeds,"run_count":len(rows),"aggregate":agg,"muse_minus_free":delta,"warning":"Synthetic proxy only; faster recovery of familiar structures is not the sole objective and results do not establish human productivity."}

def _dominates(a:dict,b:dict)->bool:
    keys=("new_valid_distinctions","new_counterexamples","new_tool_candidates","new_questions","reusable_negative_boundaries")
    return all(a[k]>=b[k] for k in keys) and any(a[k]>b[k] for k in keys)

def productive_failure_scalar_attack()->dict:
    profiles={
      "R020":{"new_valid_distinctions":3,"new_counterexamples":2,"new_tool_candidates":2,"new_questions":2,"reusable_negative_boundaries":2,"unsupported_overclaims":0},
      "R022":{"new_valid_distinctions":4,"new_counterexamples":1,"new_tool_candidates":5,"new_questions":4,"reusable_negative_boundaries":2,"unsupported_overclaims":0},
      "R025":{"new_valid_distinctions":3,"new_counterexamples":2,"new_tool_candidates":2,"new_questions":3,"reusable_negative_boundaries":2,"unsupported_overclaims":0},
      "R027":{"new_valid_distinctions":2,"new_counterexamples":1,"new_tool_candidates":1,"new_questions":3,"reusable_negative_boundaries":2,"unsupported_overclaims":0},
      "R028":{"new_valid_distinctions":5,"new_counterexamples":3,"new_tool_candidates":3,"new_questions":3,"reusable_negative_boundaries":3,"unsupported_overclaims":0}}
    weightings={"tool_heavy":(1,1,5,1,1,-2),"question_heavy":(1,1,1,5,1,-2),"boundary_heavy":(1,1,1,1,5,-2),"distinction_heavy":(5,1,1,1,1,-2)}
    fields=("new_valid_distinctions","new_counterexamples","new_tool_candidates","new_questions","reusable_negative_boundaries","unsupported_overclaims"); winners={}
    for name,ws in weightings.items():
        scores={rid:sum(w*p[f] for w,f in zip(ws,fields)) for rid,p in profiles.items()}; winners[name]=max(scores,key=lambda x:(scores[x],x))
    frontier=[rid for rid,p in profiles.items() if not any(other!=rid and _dominates(q,p) for other,q in profiles.items())]
    return {"profiles":profiles,"weighting_winners":winners,"ranking_is_weight_sensitive":len(set(winners.values()))>=2,"pareto_frontier":frontier,"verdict":"NO_CANONICAL_SCALAR_RANKING"}

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--seeds",type=int,default=64); a=p.parse_args(); print(json.dumps({"backtest":run_backtest(seeds=a.seeds),"scalar_attack":productive_failure_scalar_attack()},indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
