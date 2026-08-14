#!/usr/bin/env python3
"""Deterministic Research Context Compiler (R030 research prototype).

The compiler never treats keyword matches as theorem evidence. Structured/semantic
signature facts drive EXACT_REQUIRED selection; text triggers can only add
DIAGNOSTIC_SUGGESTED items.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

SCHEMA="ENTERPRISE_MATH_RESEARCH_CONTEXT_PACK_V1"
VERSION="R030.1"
UNKNOWN="UNKNOWN"

RISK_CAPABILITIES={
 "carrier_conflation":{"carrier_type_safety"},
 "support_count_provenance":{"carrier_observable_typing","carrier_type_safety"},
 "state_observation_risk":{"state_observation_typing"},
 "dynamic_reuse":{"dynamic_state_safety","static_dynamic_split"},
 "one_step_to_composition":{"composition_safety","one_step_composition_split"},
 "horizon_extension":{"composition_safety","future_modality"},
 "future_modality":{"future_modality","future_language_relativity"},
 "realized_vs_declared":{"future_modality","declared_realized_split"},
 "branch_token_state":{"branch_state_typing"},
 "certificate_heuristic":{"certificate_semantics"},
 "middle_incidence":{"middle_correlation"},
 "suffix_recoalescence":{"suffix_safety","future_modality","current_vs_suffix_safety"},
 "resource_semantic_equivalence":{"equal_semantic_contract"},
 "resource_metadata":{"resource_accounting"},
 "evidence_coverage":{"root_coverage","evidence_grade","actual_module_coverage","source_vs_coverage"},
 "evidence_grading":{"evidence_grade"},
 "exact_fallback_risk":{"exact_fallback"},
 "empirical_universal":{"evidence_grade","quantifier_scope","finite_evidence_boundary"},
 "bounded_minimality":{"minimality_scope"},
 "regime_boundaries":{"regime_boundary","quantifier_scope","counterexample_pressure","regime_partitioning"},
 "global_claim_risk":{"quantifier_scope"},
 "causal_attribution":{"causal_modal_split"},
 "prior_art":{"prior_art_rooting"},
 "complete_encoding_risk":{"complete_encoding"},
 "observational_equivalence":{"state_observation_typing"},
}

NON_IMPL={
 "STATIC_CORRECT_NOT_DYNAMIC_STATE":"static correctness ⇏ dynamically reusable state",
 "ONE_STEP_EXACT_NOT_COMPOSITION_SAFE":"one-step exactness ⇏ composition safety",
 "SUPPORT_COUNT_PROVENANCE_SPLIT":"Boolean support ≠ count ≠ provenance",
 "BRANCH_SELECTOR_NOT_FULL_STATE":"branch selector/token ≠ full semantic state",
 "DECLARED_VS_REALIZED_FUTURE":"declared future ≠ realized future/suffix",
 "MINIMAL_IN_DECLARED_CLASS_VS_GLOBAL_MINIMAL":"bounded/declaration-class minimality ⇏ global minimality",
 "RESOURCE_EQUAL_SEMANTIC_FIBRE_CHECK":"lower resource cost under a different semantic contract ⇏ Pareto improvement",
 "ROOT_COVERAGE_EVIDENCE_CHECK":"build PASS ⇏ coverage of a newly added module",
 "SOURCE_PROVENANCE_VS_COVERAGE_EVIDENCE":"source provenance ⇏ compiler/root coverage evidence",
 "FINITE_EVIDENCE_NOT_UNIVERSAL":"finite/exhaustive evidence on a bounded domain ⇏ universal theorem",
 "REGIME_EXHAUSTION":"numerical threshold evidence ⇏ complete regime classification; test equality, alignment, and degenerate regimes",
 "CURRENT_EQUALITY_NOT_SUFFIX_SAFE":"current coarse equality ⇏ suffix-safe forgetful recoalescence",
 "CERTIFICATE_HEURISTIC_SPLIT":"heuristic search quality ⇏ semantic certificate validity",
 "CAUSAL_PREDICTIVE_RETROSPECTIVE_SPLIT":"retrospective/predictive relevance ⇏ causal contribution",
}


def canon(x:Any)->bytes:
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

def sha(x:Any)->str:
    if isinstance(x,(bytes,bytearray)): b=bytes(x)
    elif isinstance(x,str): b=x.encode()
    else: b=canon(x)
    return hashlib.sha256(b).hexdigest()

def load_json(path:str|Path)->dict:
    return json.loads(Path(path).read_text())

def parse_header(text:str)->dict:
    m=re.search(r"<!--\s*ENTERPRISE_MATH_TASK_V1\s*(\{.*?\})\s*-->",text,re.S)
    if not m: return {}
    try: return json.loads(m.group(1))
    except json.JSONDecodeError: return {}

def _contains(text:str,*needles:str)->bool:
    t=text.casefold(); return any(n.casefold() in t for n in needles)

def _all(text:str,*needles:str)->bool:
    t=text.casefold(); return all(n.casefold() in t for n in needles)

def derive_signature(text:str, *, source_path:str|None=None)->dict:
    """Derive a conservative semantic signature. Unknowns stay UNKNOWN.

    Exact selection consumes only fields produced here. Keywords are used as
    evidence cues for typed facts, not directly as selected tool IDs.
    """
    h=parse_header(text)
    low=text.casefold()
    task_id=h.get("task_id", UNKNOWN)
    obj=[]; carriers=[]; sem=[]; facts=[]; risks=[]; evidence=[]
    def add(seq,v):
        if v not in seq: seq.append(v)
    for phrase,val in [
      ("fine state","fine state"),("fine point","fine point"),("fine relation","fine relation"),
      ("branch token","branch token"),("branch configuration","branch configuration"),
      ("checkpoint","checkpoint"),("lean module","Lean module"),("candidate law","candidate law"),
      ("precision scale","precision state"),("runtime representation","runtime representation")]:
        if phrase in low: add(obj,val)
    for phrases,val in [
      (("boolean support","result-support","result support","set-valued final support"),"Boolean support"),
      (("multiplicity","path-count","path count","witness count"),"count/multiplicity"),
      (("provenance","branch identity"),"provenance"),
      (("full fine state","exact fine state"),"full fine state"),
      (("branch token","selector token","branch discriminant"),"branch token"),
      (("cell label","quotient label","bracket/cell"),"cell/quotient label"),
      (("fine fibre","full fibre"),"fine fibre"),
      (("support interval","symbolic support"),"symbolic support"),
      (("n-count","counting carrier"),"N-count")]:
        if any(p in low for p in phrases):
            if val=="Boolean support" and any(n in low for n in ("no boolean result-support","no boolean result support","not a boolean result-support","not boolean support")):
                continue
            add(carriers,val)
    if any(x in low for x in ("relation","relational direct image","set-valued execution")): add(sem,"RELATIONAL")
    if any(x in low for x in ("stochastic","probability law","martingale","variance")): add(sem,"STOCHASTIC")
    if any(x in low for x in ("deterministic","function","functional")): add(sem,"DETERMINISTIC")
    if any(x in low for x in ("signed","amplitude","cancellation")): add(sem,"SIGNED")
    if any(x in low for x in ("arbitrary finite", "finite-word", "finite word", "depth `", "horizons at least")):
        horizon="FINITE_WORD"
    elif any(x in low for x in ("remaining suffix","residual language","suffix-safety","suffix safety")):
        horizon="REMAINING_SUFFIX"
    elif "one-step" in low or "one step" in low:
        horizon="ONE_STEP"
    else: horizon=UNKNOWN
    if any(x in low for x in ("declared future language","future language","residual future","remaining language")):
        future_language="DECLARED_LANGUAGE"
    elif "realized trace" in low or "realized suffix" in low:
        future_language="REALIZED_TRACE"
    elif horizon!=UNKNOWN:
        future_language="DECLARED_HORIZON"
    else: future_language=UNKNOWN
    if any(x in low for x in ("no new mathematics","shared-surface integration","exact integration delta")):
        claim_mode="INTEGRATION"
    elif any(x in low for x in ("empirical-law discovery","dataset schema","law mining")):
        claim_mode="EMPIRICAL_LAW_DISCOVERY"
    elif any(x in low for x in ("lean formalization","lean module","prove in lean")):
        claim_mode="FORMALIZATION"
    elif any(x in low for x in ("benchmark workload","runtime accelerator","executable validation only")):
        claim_mode="EXECUTABLE"
    else: claim_mode="MIXED"
    if any(x in low for x in ("within the declared", "declared exhaustive", "bounded", "small-domain", "small domain")) and "minimal" in low:
        minscope="DECLARED_CLASS"
    elif any(x in low for x in ("global minimality","globally minimal")):
        minscope="GLOBAL"
    elif "minimal" in low: minscope=UNKNOWN
    else: minscope="NONE"
    if any(x in low for x in ("suffix-safe","suffix safety","remaining suffix")): comp="SUFFIX_SAFE"
    elif horizon=="FINITE_WORD" or "composition" in low: comp="FINITE_WORD"
    elif horizon=="ONE_STEP": comp="ONE_STEP_ONLY"
    else: comp=UNKNOWN
    resource=any(x in low for x in ("pareto","storage","latency","memory","resource quantities","packed bytes","benchmark"))
    semantic_equal=(resource and (len(carriers)>=2 or any(x in low for x in ("exact semantic output","semantically distinct","same declared"))))
    if re.search(r"\blean\b", low): add(evidence,"LEAN")
    if any(x in low for x in ("root registration","root-import","root import","enterpriseMath.lean".casefold())): add(evidence,"ROOT_IMPORT_COVERAGE")
    if any(x in low for x in ("build", "warnings-fatal")): add(evidence,"BUILD")
    if any(x in low for x in ("exhaustive","exhaustiveness")): add(evidence,"BOUNDED_EXHAUSTIVE")
    if any(x in low for x in ("test", "mutation")): add(evidence,"EXECUTABLE_TEST")
    if "dataset" in low: add(evidence,"DATASET")
    if any(x in low for x in ("approximate root","exact fallback","exact verification")): add(evidence,"EXACT_FALLBACK")
    if len(carriers)>=2: add(risks,"carrier_conflation")
    if any(c in carriers for c in ("Boolean support","count/multiplicity","provenance","N-count")) and sum(c in carriers for c in ("Boolean support","count/multiplicity","provenance","N-count"))>=2:
        add(risks,"support_count_provenance")
    if any(x in low for x in ("statistic","summary")) and any(x in low for x in ("reused as input","reuse","composition","recursively executable","dynamic")): add(risks,"dynamic_reuse")
    if ("one-step" in low or "one step" in low) and (comp in ("FINITE_WORD","SUFFIX_SAFE") or "composition" in low): add(risks,"one_step_to_composition")
    if future_language!=UNKNOWN or any(x in low for x in ("declared", "realized", "hindsight", "residual language")): add(risks,"future_modality")
    if any(x in low for x in ("declared future", "realized suffix", "realized future", "hindsight")): add(risks,"realized_vs_declared")
    if "branch token" in low and "full fine state" in low: add(risks,"branch_token_state")
    if any(x in low for x in ("heuristic closeness","heuristic", "ranking")) and "certificate" in low: add(risks,"certificate_heuristic")
    if any(x in low for x in ("middle-incidence","middle incidence","middle witness")) and "composition" in low: add(risks,"middle_incidence")
    if any(x in low for x in ("suffix-safe","suffix safety","forgetful recoalescence")): add(risks,"suffix_recoalescence")
    if resource and semantic_equal: add(risks,"resource_semantic_equivalence")
    if resource and any(x in low for x in ("metadata","cache","dictionary","hazard","token")): add(risks,"resource_metadata")
    if "BUILD" in evidence and "ROOT_IMPORT_COVERAGE" in evidence: add(risks,"evidence_coverage")
    if evidence: add(risks,"evidence_grading")
    if "EXACT_FALLBACK" in evidence: add(risks,"exact_fallback_risk")
    if claim_mode=="EMPIRICAL_LAW_DISCOVERY" and any(x in low for x in ("theorem", "law", "universal", "always")): add(risks,"empirical_universal")
    if minscope=="DECLARED_CLASS": add(risks,"bounded_minimality")
    if any(x in low for x in ("candidate laws", "frozen candidate laws", "regime", "phase transition", "threshold")) and "exhaust" in low:
        add(risks,"regime_boundaries")
    if any(x in low for x in ("for all","always","universal","blanket")): add(risks,"global_claim_risk")
    if any(x in low for x in ("causal","predictive","retrospective")) and sum(x in low for x in ("causal","predictive","retrospective"))>=2: add(risks,"causal_attribution")
    if any(x in low for x in ("prior art","prior-art","rooting")): add(risks,"prior_art")
    if any(x in low for x in ("complete runtime encoding","hidden token","no-resurrection")): add(risks,"complete_encoding_risk")
    if any(x in low for x in ("same quotient label","observational equivalence","same current observable")): add(risks,"observational_equivalence")
    if re.search(r"\bn[_ ]?0\s*=\s*0",low) or "n_0 = 0" in low or "`n_0 = 0" in low: add(facts,"zero_state_in_domain")
    if any(x in low for x in ("p-power-aligned","perfect-pth-power refinement","r_t = a_t^p","r=a^p")): add(facts,"alignment_subregime_declared")
    if "2^p" in low or "2^p" in text: add(facts,"power_threshold_present")
    if claim_mode=="EMPIRICAL_LAW_DISCOVERY": add(facts,"candidate_laws_must_be_attacked")
    deps=[d.get("target") for d in h.get("dependencies",[]) if isinstance(d,dict) and d.get("target")]
    exclusions=[]
    for s in re.split(r"(?<=[.!?。；])\s+", text):
        ls=s.casefold()
        if any(x in ls for x in ("outside this", "does not", "do not", "不得", "不包括")) and len(s)<260:
            exclusions.append(s.strip())
            if len(exclusions)>=8: break
    unknown=[]
    for name,val in [("future_language",future_language),("future_horizon",horizon),("minimality_scope",minscope),("composition_requirement",comp)]:
        if val==UNKNOWN: unknown.append(name)
    return {
      "task_id":task_id,"object_types":obj,"carrier_types":carriers,"semantics":sem or [UNKNOWN],
      "current_observable":UNKNOWN,"future_language":future_language,"future_horizon":horizon,"claim_mode":claim_mode,
      "minimality_scope":minscope,"composition_requirement":comp,"resource_comparison":resource,
      "semantic_contract_equality_required":semantic_equal if resource else "NOT_APPLICABLE",
      "evidence_targets":evidence,"dependencies":deps,"exclusions":exclusions,"semantic_facts":facts,
      "risk_flags":risks,"unknown_fields":unknown,"source_path":source_path
    }


def _required(tool:dict,sig:dict)->bool:
    if tool.get("trust_class")=="INTERPRETIVE_LENS": return False
    rule=tool.get("required_when")
    if not rule: return False
    flags=set(sig.get("risk_flags",[]))
    return bool(flags.intersection(rule.get("risk_flags_any",[])))

def _diag_score(tool:dict,text:str)->int:
    low=text.casefold(); hits=sum(1 for s in tool.get("trigger_signals",[]) if s.casefold() in low)
    if hits==0: return 0
    return hits*10 + int(tool.get("priority",0))//10 - int(tool.get("cost",{}).get("false_positive_cost",1))

def required_capabilities(sig:dict)->set[str]:
    caps=set()
    for f in sig.get("risk_flags",[]): caps.update(RISK_CAPABILITIES.get(f,set()))
    return caps

def _sort_tools(tools:Iterable[dict])->List[dict]:
    return sorted(tools,key=lambda t:(-int(t.get("priority",0)),int(t.get("cost",{}).get("estimated_tokens",9999)),t["id"]))

def minimum_cover(candidates:Sequence[dict], caps:set[str])->Tuple[List[dict],set[str]]:
    """Exact weighted set cover for the small R030 registry.

    Objective: minimum estimated injected tokens, then minimum tool count, then
    lexicographic tool IDs. This is deterministic and inspectable. A dynamic
    program over the required-capability bitmask avoids a keyword/ranking
    heuristic in the critical channel.
    """
    req=sorted(caps)
    if not req: return [],set()
    bit={c:1<<i for i,c in enumerate(req)}; full=(1<<len(req))-1
    items=[]
    for t in candidates:
        mask=0
        for c in t.get("covers",[]):
            if c in bit: mask |= bit[c]
        if mask:
            items.append((t,mask,int(t.get("cost",{}).get("estimated_tokens",100))))
    dp={0:(0,0,tuple(),tuple())}
    for t,tm,cost in sorted(items,key=lambda z:z[0]["id"]):
        cur=list(dp.items())
        for mask,state in cur:
            nm=mask|tm
            if nm==mask: continue
            ids=tuple(sorted(state[2]+(t["id"],)))
            sel=state[3]+(t,)
            cand=(state[0]+cost,state[1]+1,ids,sel)
            old=dp.get(nm)
            if old is None or cand[:3] < old[:3]: dp[nm]=cand
    if full not in dp:
        best=max(dp, key=lambda m:(m.bit_count(),-dp[m][0],-dp[m][1]))
        missing={req[i] for i in range(len(req)) if not (best>>i)&1}
        return _sort_tools(dp[best][3]),missing
    return _sort_tools(dp[full][3]),set()

def relevant_common_surface_slice(common:dict|None,sig:dict)->dict:
    if not common: return {"schema":"NO_COMMON_SURFACE_SUPPLIED","selected_entry_ids":[],"entries":{}}
    wanted=set()
    risks=set(sig.get("risk_flags",[]))
    if risks & {"carrier_conflation","support_count_provenance","one_step_to_composition","suffix_recoalescence","middle_incidence"}: wanted.add("A4_BRC_semantic_core")
    if risks & {"dynamic_reuse","future_modality","complete_encoding_risk"}: wanted.update({"P023","future_safe","task_signature"})
    if risks & {"resource_semantic_equivalence","resource_metadata"}: wanted.update({"R014","resource","Pareto"})
    if risks & {"evidence_coverage"}: wanted.update({"A4_BRC_semantic_core","validation"})
    found={}
    def walk(x:Any,path:str=""):
        if isinstance(x,dict):
            for k,v in x.items():
                p=f"{path}.{k}" if path else str(k)
                if any(w.casefold() in str(k).casefold() for w in wanted): found[p]=v
                else: walk(v,p)
        elif isinstance(x,list):
            for i,v in enumerate(x): walk(v,f"{path}[{i}]")
    walk(common)
    return {"schema":common.get("schema",UNKNOWN) if isinstance(common,dict) else UNKNOWN,"selected_entry_ids":sorted(found),"entries":{k:found[k] for k in sorted(found)}}

def compile_signature(sig:dict, registry:dict, *, diagnostic_text:str="", strategy:str="MINIMUM_CRITICAL_COVER", top_k:int=3, common_surface:dict|None=None, source_snapshot:dict|None=None)->dict:
    tools=registry.get("tools",[])
    exact=_sort_tools([t for t in tools if _required(t,sig)])
    exact_ids={t["id"] for t in exact}
    diag_scored=[]
    for t in tools:
        if t["id"] in exact_ids: continue
        score=_diag_score(t,diagnostic_text)
        if score>0: diag_scored.append((score,t))
    diag_scored.sort(key=lambda x:(-x[0],-int(x[1].get("priority",0)),x[1]["id"]))
    diag=[t for _,t in diag_scored]
    caps=required_capabilities(sig)
    unresolved=set()
    if strategy=="ALL_MATCHES": sel_exact=exact; sel_diag=diag
    elif strategy=="TOP_K": sel_exact=exact; sel_diag=diag[:max(0,top_k)]
    elif strategy=="MINIMUM_CRITICAL_COVER":
        sel_exact,unresolved=minimum_cover(exact,caps)
        sel_diag=[]
        if unresolved:
            for t in diag:
                if unresolved.intersection(t.get("covers",[])):
                    sel_diag.append(t); unresolved-=set(t.get("covers",[]))
                    if not unresolved: break
    else: raise ValueError(f"unknown strategy {strategy}")
    sel_ids={t["id"] for t in sel_exact+sel_diag}
    reasons={}
    for t in sel_exact: reasons[t["id"]]={"channel":"EXACT_REQUIRED","matched_risk_flags":sorted(set(sig.get("risk_flags",[])).intersection((t.get("required_when") or {}).get("risk_flags_any",[]))),"covers":t.get("covers",[]),"scope":t.get("scope"),"evidence_grade":t.get("evidence_grade"),"source_refs":t.get("source_refs",[]),"why_selected":"contributes to the deterministic minimum cover of structured task risks","what_not_infer":t.get("may_destroy_or_not_preserve")}
    for t in sel_diag: reasons[t["id"]]={"channel":"DIAGNOSTIC_SUGGESTED","trigger_hits":[s for s in t.get("trigger_signals",[]) if s.casefold() in diagnostic_text.casefold()],"scope":t.get("scope"),"evidence_grade":t.get("evidence_grade"),"source_refs":t.get("source_refs",[]),"why_selected":"auxiliary textual/heuristic trigger under the diagnostic budget","what_not_infer":t.get("may_destroy_or_not_preserve")}
    common_slice=relevant_common_surface_slice(common_surface,sig)
    source_snapshot=source_snapshot or {"taskbook_semantic_digest":sha(sig),"taskbook_blob":UNKNOWN}
    reg_digest=sha(registry)
    common_digest=sha(common_slice)
    pinned=sorted({str(r) for t in sel_exact+sel_diag for r in t.get("source_refs",[])})
    digest_inputs={"taskbook":source_snapshot,"task_signature":sig,"registry_digest":reg_digest,"relevant_common_surface_digest":common_digest,"selected_source_refs":pinned}
    context_digest=sha(digest_inputs)
    alerts={"carrier":[],"modal":[],"quantifier":[],"evidence":[],"prior_art":[]}
    for tid in sorted(sel_ids):
        if any(x in tid for x in ("CARRIER","STATE_OBSERVATION","SUPPORT_COUNT","BRANCH_SELECTOR","OBJECT_IDENTITY")): alerts["carrier"].append(tid)
        if any(x in tid for x in ("FUTURE","HORIZON","SUFFIX","CURRENT_EQUALITY","CAUSAL")): alerts["modal"].append(tid)
        if any(x in tid for x in ("QUANTIFIER","MINIMAL","REGIME")): alerts["quantifier"].append(tid)
        if any(x in tid for x in ("EVIDENCE","ROOT_COVERAGE","FINITE_EVIDENCE","EXACT_FALLBACK")): alerts["evidence"].append(tid)
        if "PRIOR_ART" in tid: alerts["prior_art"].append(tid)
    omitted=[]
    exact_all={t["id"] for t in exact}; diag_all={t["id"] for t in diag}
    for t in tools:
        if t["id"] in sel_ids: continue
        if t["id"] in exact_all: reason="MINIMUM_COVER_REDUNDANT" if strategy=="MINIMUM_CRITICAL_COVER" else "STRATEGY_EXCLUDED"
        elif t["id"] in diag_all: reason="DIAGNOSTIC_BUDGET_OR_NONCRITICAL"
        elif t.get("trust_class")=="INTERPRETIVE_LENS": reason="INTERPRETIVE_LENS_NOT_REQUIRED"
        else: reason="NOT_REQUIRED_BY_SIGNATURE"
        omitted.append({"id":t["id"],"reason":reason})
    estimated_tokens=sum(int(t.get("cost",{}).get("estimated_tokens",0)) for t in sel_exact+sel_diag)
    pack={
      "schema":SCHEMA,"compiler_version":VERSION,"task_id":sig.get("task_id",UNKNOWN),"task_signature":sig,
      "source_snapshot":{**source_snapshot,"relevant_common_surface_digest":common_digest},
      "registry_snapshot":{"schema":registry.get("schema"),"status":registry.get("status"),"digest":reg_digest},
      "selection_strategy":strategy,"selected_exact_tools":[t["id"] for t in sel_exact],"selected_diagnostic_tools":[t["id"] for t in sel_diag],
      "selection_reasons":reasons,"carrier_alerts":alerts["carrier"],"modal_alerts":alerts["modal"],"quantifier_alerts":alerts["quantifier"],
      "evidence_alerts":alerts["evidence"],"negative_boundaries":[NON_IMPL[i] for i in sorted(sel_ids) if i in NON_IMPL],"prior_art_alerts":alerts["prior_art"],
      "required_source_refs":pinned,"known_non_implications":[NON_IMPL[i] for i in sorted(sel_ids) if i in NON_IMPL],"excluded_tools":omitted,
      "uncovered_required_capabilities":sorted(unresolved),
      "context_budget":{"selected_tool_count":len(sel_ids),"exact_tool_count":len(sel_exact),"diagnostic_tool_count":len(sel_diag),"estimated_tool_tokens":estimated_tokens,"estimated_tool_bytes":estimated_tokens*4,"source_ref_count":len(pinned)},
      "meta_tool_delta":{"unknown_signature_fields":list(sig.get("unknown_fields",[])),"uncovered_required_capabilities":sorted(unresolved),"exact_candidate_count":len(exact),"selected_exact_count":len(sel_exact),"omitted_exact_candidate_ids":sorted(exact_all-{t["id"] for t in sel_exact}),"diagnostic_candidate_count":len(diag),"selected_diagnostic_count":len(sel_diag),"diagnostic_candidate_ids":sorted(diag_all)},
      "digest_inputs":digest_inputs,"context_digest":context_digest
    }
    pack["context_budget"]["serialized_pack_bytes"]=len(canon(pack))
    pack["context_budget"]["serialized_pack_tokens_estimate"]=(pack["context_budget"]["serialized_pack_bytes"]+3)//4
    return pack

def compile_taskbook(taskbook_path:str, registry_path:str, common_surface_path:str|None=None, strategy:str="MINIMUM_CRITICAL_COVER",top_k:int=3)->dict:
    text=Path(taskbook_path).read_text()
    sig=derive_signature(text,source_path=taskbook_path)
    reg=load_json(registry_path); common=load_json(common_surface_path) if common_surface_path else None
    source={"taskbook_path":taskbook_path,"taskbook_content_sha256":sha(text),"taskbook_semantic_digest":sha(sig)}
    return compile_signature(sig,reg,diagnostic_text=text,strategy=strategy,top_k=top_k,common_surface=common,source_snapshot=source)

def render_human(pack:dict, registry:dict)->str:
    by={t["id"]:t for t in registry.get("tools",[])}
    lines=[f"# Research Context Pack — {pack['task_id']}","",f"Strategy: `{pack['selection_strategy']}`  ",f"Digest: `{pack['context_digest']}`","","## TASK SEMANTIC SIGNATURE","", "```json",json.dumps(pack["task_signature"],indent=2,ensure_ascii=False),"```","","## CRITICAL REASONING TOOLS",""]
    for tid in pack["selected_exact_tools"]:
        t=by[tid]; lines.append(f"- **{tid}** [{t['trust_class']}] — {t['name']}")
    lines += ["","## DIAGNOSTIC / SUGGESTED TOOLS",""]
    if pack["selected_diagnostic_tools"]:
        for tid in pack["selected_diagnostic_tools"]:
            t=by[tid]; lines.append(f"- **{tid}** [{t['trust_class']}] — {t['name']} *(not theorem evidence)*")
    else: lines.append("- None selected under the current budget.")
    lines += ["","## KNOWN NON-IMPLICATIONS",""] + [f"- {x}" for x in pack["known_non_implications"] or ["None compiled."]]
    lines += ["","## CARRIER / MODAL / QUANTIFIER ALERTS",""]
    for k in ("carrier_alerts","modal_alerts","quantifier_alerts"): lines.append(f"- {k}: {', '.join(pack[k]) or 'none'}")
    lines += ["","## EVIDENCE BOUNDARY",""] + [f"- {x}" for x in pack["evidence_alerts"] or ["No task-specific evidence alert compiled."]]
    lines += ["","## NEGATIVE BOUNDARIES",""] + [f"- {x}" for x in pack["negative_boundaries"] or ["None compiled."]]
    lines += ["","## PRIOR-ART ALERTS",""] + [f"- {x}" for x in pack["prior_art_alerts"] or ["None compiled."]]
    lines += ["","## SOURCE POINTERS",""] + [f"- {x}" for x in pack["required_source_refs"] or ["No additional tool source pointer selected."]]
    lines += ["","## WHAT WAS INTENTIONALLY OMITTED",""]
    for x in pack["excluded_tools"][:12]: lines.append(f"- {x['id']}: {x['reason']}")
    if len(pack["excluded_tools"])>12: lines.append(f"- … {len(pack['excluded_tools'])-12} more omitted tools are inspectable in JSON.")
    return "\n".join(lines)+"\n"

def audit_pack(pack:dict)->dict:
    expected=sha(pack.get("digest_inputs",{}))
    return {"schema_ok":pack.get("schema")==SCHEMA,"digest_ok":expected==pack.get("context_digest"),"expected_digest":expected,"recorded_digest":pack.get("context_digest"),"uncovered_required_capabilities":pack.get("uncovered_required_capabilities",[]),"pass":pack.get("schema")==SCHEMA and expected==pack.get("context_digest") and not pack.get("uncovered_required_capabilities")}

def main(argv:Sequence[str]|None=None)->int:
    p=argparse.ArgumentParser(prog="research_context.py")
    sp=p.add_subparsers(dest="cmd",required=True)
    c=sp.add_parser("compile"); c.add_argument("taskbook"); c.add_argument("--registry",required=True); c.add_argument("--common-surface"); c.add_argument("--strategy",choices=["ALL_MATCHES","TOP_K","MINIMUM_CRITICAL_COVER"],default="MINIMUM_CRITICAL_COVER"); c.add_argument("--top-k",type=int,default=3); c.add_argument("--output"); c.add_argument("--human-output")
    i=sp.add_parser("inspect"); i.add_argument("pack"); i.add_argument("--registry",required=True)
    a=sp.add_parser("audit"); a.add_argument("pack")
    b=sp.add_parser("backtest"); b.add_argument("--gold",required=True); b.add_argument("--registry",required=True); b.add_argument("--output"); b.add_argument("--strategy",choices=["ALL_MATCHES","TOP_K","MINIMUM_CRITICAL_COVER"],default="MINIMUM_CRITICAL_COVER"); b.add_argument("--top-k",type=int,default=3)
    ns=p.parse_args(argv)
    if ns.cmd=="compile":
        pack=compile_taskbook(ns.taskbook,ns.registry,ns.common_surface,ns.strategy,ns.top_k); out=json.dumps(pack,indent=2,ensure_ascii=False)+"\n"
        if ns.output: Path(ns.output).write_text(out)
        else: print(out,end="")
        if ns.human_output: Path(ns.human_output).write_text(render_human(pack,load_json(ns.registry)))
    elif ns.cmd=="inspect": print(render_human(load_json(ns.pack),load_json(ns.registry)),end="")
    elif ns.cmd=="audit":
        r=audit_pack(load_json(ns.pack)); print(json.dumps(r,indent=2)); return 0 if r["pass"] else 2
    elif ns.cmd=="backtest":
        sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
        from r030_context_backtest import run_backtest
        r=run_backtest(load_json(ns.gold),load_json(ns.registry),strategy=ns.strategy,top_k=ns.top_k)
        out=json.dumps(r,indent=2,ensure_ascii=False)+"\n"; Path(ns.output).write_text(out) if ns.output else print(out,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
