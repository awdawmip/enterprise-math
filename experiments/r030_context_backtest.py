#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from copy import deepcopy
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from research_context import compile_signature, derive_signature, sha, required_capabilities, render_human

STRATEGIES=[('MINIMUM_CRITICAL_COVER',0),('TOP_K',1),('TOP_K',2),('TOP_K',3),('TOP_K',5),('TOP_K',8),('ALL_MATCHES',99)]

def distinction_covered(dist, selected:set[str])->bool:
    return any(set(s).issubset(selected) for s in dist.get('acceptable_tool_sets',[]))

def score_task(task:dict, registry:dict, strategy:str, top_k:int=3)->dict:
    sig=deepcopy(task['signature_fixture'])
    source={"taskbook_path":task['taskbook_path'],"taskbook_blob":task['taskbook_blob'],"taskbook_semantic_digest":sha(sig),"replay_mode":"POSTHOC_SIGNATURE_FIXTURE_NO_LATE_FACT_INJECTION"}
    pack=compile_signature(sig,registry,diagnostic_text=task.get('startup_excerpt',''),strategy=strategy,top_k=top_k,source_snapshot=source)
    human=render_human(pack,registry); pack['context_budget']['human_pack_bytes']=len(human.encode()); pack['context_budget']['human_pack_tokens_estimate']=(len(human.encode())+3)//4
    selected=set(pack['selected_exact_tools'])|set(pack['selected_diagnostic_tools'])
    covered=[d['id'] for d in task['distinctions'] if distinction_covered(d,selected)]
    gold_tool_ids={tid for d in task['distinctions'] for s in d.get('acceptable_tool_sets',[]) for tid in s}
    selected_gold=sorted(selected & gold_tool_ids)
    late=[d for d in task['distinctions'] if d.get('late_discovered')]
    recovered=[d['id'] for d in late if distinction_covered(d,selected)]
    strict_non_gold=sorted(selected-gold_tool_ids)
    # Structural overload is different from strict gold precision: gold is intentionally
    # a critical-distinction list, not an exhaustive relevance annotation. Count a
    # selected tool as overload when removing it still covers every structured required
    # capability. DIAGNOSTIC tools are evaluated by the same removal test.
    req=required_capabilities(sig)
    by_id={t['id']:t for t in registry['tools']}
    def covered_caps(ids):
        u=set()
        for tid in ids: u.update(by_id[tid].get('covers',[]))
        return u
    redundant=[]
    for tid in sorted(selected):
        if req.issubset(covered_caps(selected-{tid})): redundant.append(tid)
    wrong_route_risk=sum(int(by_id[x].get('cost',{}).get('false_positive_cost',1)) for x in pack['selected_diagnostic_tools'])
    return {
      "task":task['task'],"gold_count":len(task['distinctions']),"covered_gold":covered,
      "critical_tool_recall":len(covered)/max(1,len(task['distinctions'])),
      "selected_tool_count":len(selected),"selected_gold_tool_count":len(selected_gold),
      "critical_tool_precision":len(selected_gold)/max(1,len(selected)),"precision_note":"strict lower bound because the post-hoc gold lists only critical distinctions, not every relevant task obligation",
      "selected_gold_tools":selected_gold,"strict_non_gold_tools":strict_non_gold,"strict_non_gold_count":len(strict_non_gold),
      "overload_tools":redundant,"overload_tool_count":len(redundant),"wrong_route_risk":wrong_route_risk,
      "late_gold_count":len(late),"recovered_late":recovered,
      "recovered_late_count":len(recovered),"context_cost":pack['context_budget'],"pack":pack
    }

def aggregate(rows:list[dict],strategy:str,top_k:int)->dict:
    gold=sum(r['gold_count'] for r in rows); covered=sum(len(r['covered_gold']) for r in rows)
    selected=sum(r['selected_tool_count'] for r in rows); selected_gold=sum(r['selected_gold_tool_count'] for r in rows)
    late=sum(r['late_gold_count'] for r in rows); recovered=sum(r['recovered_late_count'] for r in rows)
    tokens=sum(r['context_cost']['estimated_tool_tokens'] for r in rows); pack_tokens=sum(r['context_cost']['serialized_pack_tokens_estimate'] for r in rows); human_tokens=sum(r['context_cost']['human_pack_tokens_estimate'] for r in rows)
    strict_non_gold=sum(r['strict_non_gold_count'] for r in rows)
    overload=sum(r['overload_tool_count'] for r in rows); wrong_risk=sum(r['wrong_route_risk'] for r in rows)
    return {
      "strategy":strategy,"top_k":top_k if strategy=='TOP_K' else None,"task_count":len(rows),"gold_count":gold,"covered_gold":covered,
      "critical_tool_recall":covered/max(1,gold),"selected_tool_count":selected,"selected_gold_tool_count":selected_gold,
      "critical_tool_precision":selected_gold/max(1,selected),"critical_tool_precision_note":"strict post-hoc gold-hit density; conservative lower bound because gold is not an exhaustive relevance label set",
      "late_gold_count":late,"recovered_late_distinctions":recovered,
      "recovered_late_rate":recovered/max(1,late),"estimated_tool_tokens":tokens,"serialized_pack_tokens_estimate":pack_tokens,"human_pack_tokens_estimate":human_tokens,"mean_human_pack_tokens_estimate":human_tokens/max(1,len(rows)),
      "strict_non_gold_tool_count":strict_non_gold,"overload_tool_count":overload,"overload_ratio":overload/max(1,selected),"diagnostic_wrong_route_risk":wrong_risk
    }

def dominates(a,b)->bool:
    # a at least as good on quality, no worse on costs, and strictly better somewhere.
    q=['critical_tool_recall','critical_tool_precision','recovered_late_rate']; c=['estimated_tool_tokens','overload_tool_count','diagnostic_wrong_route_risk']
    no_worse=all(a[x]>=b[x]-1e-12 for x in q) and all(a[x]<=b[x] for x in c)
    strict=any(a[x]>b[x]+1e-12 for x in q) or any(a[x]<b[x] for x in c)
    return no_worse and strict

def pareto(points):
    return [p for p in points if not any(dominates(q,p) for q in points if q is not p)]

def run_keyword_attacks(registry):
    cases=[
      {"id":"NO_FUTURE_WORD_EXPLICIT_HORIZON","text":"<!-- ENTERPRISE_MATH_TASK_V1 {\"task_id\":\"K1\"} -->\nThe declared horizon is arbitrary finite word length 3. Compare one-step exactness with composition.","expect_exact_any":["ONE_STEP_EXACT_NOT_COMPOSITION_SAFE","HORIZON_RELATIVITY_CHECK"],"forbid_signature":[]},
      {"id":"SUPPORT_WORD_NON_BOOLEAN","text":"<!-- ENTERPRISE_MATH_TASK_V1 {\"task_id\":\"K2\"} -->\nCarrier: N-count. Report support cost of storing the integer count; no Boolean result-support is an observable.","expect_exact_any":[],"forbid_signature":["Boolean support"]},
      {"id":"MINIMAL_BOUNDED_CLASS","text":"<!-- ENTERPRISE_MATH_TASK_V1 {\"task_id\":\"K3\"} -->\nFind the minimal counterexample within the declared exhaustive class; do not claim global minimality.","expect_exact_any":["MINIMAL_IN_DECLARED_CLASS_VS_GLOBAL_MINIMAL"],"forbid_signature":[]},
      {"id":"PROOF_WORD_EXECUTABLE_ONLY","text":"<!-- ENTERPRISE_MATH_TASK_V1 {\"task_id\":\"K4\"} -->\nThis is executable validation only: tests and bounded exhaustive checks; the word proof appears only as a claim to avoid.","expect_exact_any":["CLAIM_EVIDENCE_GRADE_CHECK","FINITE_EVIDENCE_NOT_UNIVERSAL"],"forbid_signature":[]},
      {"id":"CAUSAL_WORD_PREDICTIVE_SEMANTICS","text":"<!-- ENTERPRISE_MATH_TASK_V1 {\"task_id\":\"K5\"} -->\nA predictive score is called a causal proxy in prose, but retrospective relevance and causal contribution must be separated.","expect_exact_any":["CAUSAL_PREDICTIVE_RETROSPECTIVE_SPLIT"],"forbid_signature":[]},
      {"id":"SAME_MEANS_OBSERVATIONAL","text":"<!-- ENTERPRISE_MATH_TASK_V1 {\"task_id\":\"K6\"} -->\nTwo objects have the same quotient label / same current observable; this is observational equivalence, not literal identity.","expect_exact_any":["OBJECT_IDENTITY_VS_OBSERVATIONAL_EQUIVALENCE"],"forbid_signature":[]},
    ]
    out=[]
    for c in cases:
        sig=derive_signature(c['text'])
        pack=compile_signature(sig,registry,diagnostic_text=c['text'],strategy='MINIMUM_CRITICAL_COVER')
        sel=set(pack['selected_exact_tools'])
        ok=(not c['expect_exact_any'] or any(x in sel for x in c['expect_exact_any'])) and all(x not in sig.get('carrier_types',[]) for x in c['forbid_signature'])
        # Naive keyword baseline: any trigger hit, irrespective of channel/type.
        naive=[]; low=c['text'].casefold()
        for t in registry['tools']:
            if any(s.casefold() in low for s in t.get('trigger_signals',[])): naive.append(t['id'])
        out.append({"id":c['id'],"signature":sig,"exact_selected":sorted(sel),"naive_keyword_selected":sorted(naive),"pass":ok,"naive_extra_count":len(set(naive)-sel)})
    return {"cases":out,"pass":all(x['pass'] for x in out),"naive_extra_total":sum(x['naive_extra_count'] for x in out)}

def mutation_suite(registry,gold):
    by={t['task']:t for t in gold['tasks']}
    cases=[]
    def run_case(id,base_sig,mut_sig,base_text='',mut_text='',strategy='MINIMUM_CRITICAL_COVER',expected_added=(),expected_removed=()):
        b=compile_signature(base_sig,registry,diagnostic_text=base_text,strategy=strategy,top_k=1)
        m=compile_signature(mut_sig,registry,diagnostic_text=mut_text,strategy=strategy,top_k=1)
        bs=set(b['selected_exact_tools'])|set(b['selected_diagnostic_tools']); ms=set(m['selected_exact_tools'])|set(m['selected_diagnostic_tools'])
        added=sorted(ms-bs); removed=sorted(bs-ms)
        ok=(bool(added or removed) and all(x in ms for x in expected_added) and all(x not in ms for x in expected_removed))
        cases.append({"id":id,"strategy":strategy,"added":added,"removed":removed,"base_warnings":b['known_non_implications'],"mutated_warnings":m['known_non_implications'],"pass":ok})
    # 1 carrier declaration removal
    b=deepcopy(by['R020']['signature_fixture']); m=deepcopy(b); m['carrier_types']=[]; m['risk_flags']=[x for x in m['risk_flags'] if x not in ('carrier_conflation','support_count_provenance')]
    run_case('REMOVE_CARRIER_DECLARATION',b,m,expected_removed=('CARRIER_TYPE_SPLIT',))
    # 2 Boolean support -> N-count with similar words
    b={"task_id":"M2","risk_flags":[],"carrier_types":["Boolean support"],"semantic_facts":[]}; m=deepcopy(b); m['carrier_types']=['N-count','provenance']; m['risk_flags']=['support_count_provenance','carrier_conflation']
    run_case('BOOLEAN_SUPPORT_TO_N_COUNT',b,m,expected_added=('SUPPORT_COUNT_PROVENANCE_SPLIT',))
    # 3 one step -> arbitrary finite words
    b={"task_id":"M3","risk_flags":[],"future_horizon":"ONE_STEP"}; m=deepcopy(b); m['future_horizon']='FINITE_WORD'; m['risk_flags']=['one_step_to_composition','horizon_extension']
    run_case('ONE_STEP_TO_ARBITRARY_FINITE_WORDS',b,m,expected_added=('ONE_STEP_EXACT_NOT_COMPOSITION_SAFE',))
    # 4 declared -> realized trace
    b={"task_id":"M4","risk_flags":['future_modality'],"future_language":"DECLARED_LANGUAGE"}; m=deepcopy(b); m['future_language']='REALIZED_TRACE'; m['risk_flags'].append('realized_vs_declared')
    run_case('DECLARED_FUTURE_TO_REALIZED_TRACE',b,m,expected_added=('DECLARED_VS_REALIZED_FUTURE',))
    # 5 bounded -> global minimality
    b={"task_id":"M5","risk_flags":['bounded_minimality'],"minimality_scope":"DECLARED_CLASS"}; m={"task_id":"M5","risk_flags":['global_claim_risk'],"minimality_scope":"GLOBAL"}
    run_case('BOUNDED_TO_GLOBAL_MINIMALITY',b,m,expected_removed=('MINIMAL_IN_DECLARED_CLASS_VS_GLOBAL_MINIMAL',))
    # 6 actual module coverage removed while build remains PASS
    b={"task_id":"M6","risk_flags":['evidence_grading'],"evidence_targets":['BUILD','ROOT_IMPORT_COVERAGE_CONFIRMED']}; m={"task_id":"M6","risk_flags":['evidence_grading','evidence_coverage'],"evidence_targets":['BUILD','ROOT_IMPORT_COVERAGE_REQUIRED_BUT_UNCONFIRMED']}
    run_case('BUILD_PASS_MODULE_COVERAGE_REMOVED',b,m,expected_added=('ROOT_COVERAGE_EVIDENCE_CHECK',))
    # 7 equal semantic contract -> different carrier/resource basis
    b={"task_id":"M7","risk_flags":['resource_metadata'],"resource_comparison":True}; m=deepcopy(b); m['risk_flags'].append('resource_semantic_equivalence')
    run_case('EQUAL_CONTRACT_TO_DIFFERENT_CARRIER',b,m,expected_added=('RESOURCE_EQUAL_SEMANTIC_FIBRE_CHECK',))
    # 8 interpretive lens signal must affect only diagnostic channel
    b={"task_id":"M8","risk_flags":[]}; m=deepcopy(b)
    run_case('ADD_LOW_EVIDENCE_INTERPRETIVE_LENS',b,m,'plain task','ontology possible actual world lens',strategy='TOP_K',expected_added=('INTERPRETIVE_ONTOLOGY_LENS',))
    # 9 finite evidence -> universal claim
    b={"task_id":"M9","risk_flags":['evidence_grading']}; m={"task_id":"M9","risk_flags":['evidence_grading','empirical_universal','global_claim_risk']}
    run_case('FINITE_EVIDENCE_TO_UNIVERSAL_CLAIM',b,m,expected_added=('FINITE_EVIDENCE_NOT_UNIVERSAL',))
    # 10 remove suffix horizon
    b={"task_id":"M10","risk_flags":['suffix_recoalescence','future_modality']}; m={"task_id":"M10","risk_flags":[]}
    run_case('REMOVE_SUFFIX_HORIZON',b,m,expected_removed=('CURRENT_EQUALITY_NOT_SUFFIX_SAFE',))
    return {"cases":cases,"pass":all(x['pass'] for x in cases),"changed_count":sum(bool(x['added'] or x['removed']) for x in cases)}

def run_backtest(gold:dict,registry:dict,*,strategy='MINIMUM_CRITICAL_COVER',top_k=3)->dict:
    rows=[score_task(t,registry,strategy,top_k) for t in gold['tasks']]
    agg=aggregate(rows,strategy,top_k)
    return {"schema":"R030_CONTEXT_BACKTEST_RESULT_V1","registry_status":registry.get('status'),"scoring_boundary":"Late facts are used only to define gold labels/evidence. Selection sees startup semantic fixtures plus the current reasoning registry, not post-hoc factual conclusions.","aggregate":agg,"tasks":[{k:v for k,v in r.items() if k!='pack'} for r in rows],"keyword_attacks":run_keyword_attacks(registry),"mutation_suite":mutation_suite(registry,gold)}

def run_sweep(gold,registry):
    points=[]; details={}
    for s,k in STRATEGIES:
        rows=[score_task(t,registry,s,k) for t in gold['tasks']]
        a=aggregate(rows,s,k); points.append(a); details[f"{s}:{k}"]=rows
    front=pareto(points)
    return points,front,details

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--gold',default=str(ROOT/'R030_HISTORICAL_CONTEXT_GOLD.json')); ap.add_argument('--registry',default=str(ROOT/'research_reasoning_tools_seed.json')); ap.add_argument('--out',default=str(ROOT/'experiments/r030_context_backtest_results.json')); ap.add_argument('--pareto-out',default=str(ROOT/'experiments/r030_context_budget_pareto.json')); ap.add_argument('--mutation-out',default=str(ROOT/'experiments/r030_context_mutations.json'))
    ns=ap.parse_args(); gold=json.load(open(ns.gold)); reg=json.load(open(ns.registry))
    result=run_backtest(gold,reg); Path(ns.out).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    points,front,details=run_sweep(gold,reg); pdata={"schema":"R030_CONTEXT_BUDGET_PARETO_V1","points":points,"pareto_front":front}; Path(ns.pareto_out).write_text(json.dumps(pdata,indent=2,ensure_ascii=False)+'\n')
    muts=result['mutation_suite']; Path(ns.mutation_out).write_text(json.dumps({"schema":"R030_MUTATION_SUITE_V1",**muts},indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({"aggregate":result['aggregate'],"pareto_front":front,"keyword_pass":result['keyword_attacks']['pass'],"mutation_pass":muts['pass']},indent=2))
if __name__=='__main__': main()
