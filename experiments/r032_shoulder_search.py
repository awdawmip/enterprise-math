#!/usr/bin/env python3
"""R032 post-failure SHOULDER_SEARCH: actual failure structure only."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSONS_PATH=ROOT/"research_error_lessons.json"
FIELDS=("failure_class","minimal_witness","broken_implication","surviving_invariant","newly_exposed_object")
STOP={"the","a","an","to","of","and","or","is","are","in","under","same","different","one","step","route","claim","model","general"}

def load_lessons(path:Path=LESSONS_PATH)->list[dict]: return json.loads(path.read_text(encoding="utf-8"))["lessons"]
def _tokens(value)->set[str]:
    text=" ".join(map(str,value)) if isinstance(value,list) else str(value)
    toks={t.lower() for t in re.findall(r"[A-Za-z0-9_+><=-]+|[\u4e00-\u9fff]{2,}",text)}
    return {t for t in toks if t not in STOP and len(t)>1}
def validate_failure_structure(fs:dict)->None:
    extra=set(fs)-set(FIELDS); missing=set(FIELDS)-set(fs)
    if extra: raise ValueError(f"SHOULDER_QUERY_FORBIDS_NON_FAILURE_FIELDS:{sorted(extra)}")
    if missing: raise ValueError(f"SHOULDER_QUERY_MISSING_FIELDS:{sorted(missing)}")
    for f in FIELDS:
        if fs[f] in (None,"",[]): raise ValueError(f"SHOULDER_QUERY_EMPTY_FIELD:{f}")
def similarity(query:dict,candidate:dict)->tuple[float,dict]:
    cfs=candidate["failure_structure"]; weights={"failure_class":1.0,"minimal_witness":2.0,"broken_implication":3.0,"surviving_invariant":2.5,"newly_exposed_object":3.0}; details={}; total=0.0
    for field,weight in weights.items():
        qa,cb=_tokens(query[field]),_tokens(cfs[field]); score=1.0 if field=="failure_class" and str(query[field])==str(cfs[field]) else (0.0 if field=="failure_class" else len(qa&cb)/max(1,len(qa|cb)))
        details[field]=round(score,6); total+=weight*score
    return total/sum(weights.values()),details
def shoulder_search(failure_structure:dict,*,top_k:int=3,exclude_lesson_id:str|None=None)->dict:
    validate_failure_structure(failure_structure); ranked=[]
    for lesson in load_lessons():
        if lesson["lesson_id"]==exclude_lesson_id: continue
        score,details=similarity(failure_structure,lesson); ranked.append((score,lesson,details))
    ranked.sort(key=lambda x:(-x[0],x[1]["lesson_id"])); results=[]
    for score,lesson,details in ranked[:top_k]:
        results.append({"lesson_id":lesson["lesson_id"],"similarity":round(score,6),"match_breakdown":details,"prior_failure":lesson["what_failed"],"prior_surviving_structure":lesson["what_survived"],"possible_transfer":lesson["new_objects_or_coordinates"]+lesson["new_tool_candidate"],"non_transfer_warning":lesson["what_should_NOT_be_inferred"],"questions_generated_then":lesson["new_questions_generated"]})
    return {"query_source":"ACTUAL_FAILURE_STRUCTURE_ONLY","query_fields":list(FIELDS),"results":results,"anti_fence":"A matching historical failure does not forbid retrying the route under changed semantics, carrier, horizon, assumptions, or a direct boundary attack."}
def fixture_results()->dict:
    fixtures={
      "hidden_join_coordinate":{"failure_class":"MIS_TYPED_ROUTE","minimal_witness":["same one-step counts but different composed support due to hidden middle join identity"],"broken_implication":["one-step exact statistic => composition-safe dynamic state"],"surviving_invariant":["one-step statistic remains exact under its local observable"],"newly_exposed_object":["middle incidence coordinate and composition defect"]},
      "phase_after_scaling_failure":{"failure_class":"FALSE_ROUTE","minimal_witness":["scaling covariance fails in a small integer fixture"],"broken_implication":["global scaling law => policy-independent dynamics"],"surviving_invariant":["aligned regime remains exact and a bounded phase correction survives"],"newly_exposed_object":["microphase and alignment phase atlas"]},
      "scalar_credit_order_failure":{"failure_class":"FALSE_ROUTE","minimal_witness":["same feature receives different marginal credit after acquisition order changes"],"broken_implication":["marginal credit => intrinsic order-independent scalar"],"surviving_invariant":["ordered telescoping and typed pair coverage survive"],"newly_exposed_object":["typed credit vector and Pareto frontier"]},
      "generic_novelty_absorbed":{"failure_class":"PRIOR_ART_ABSORBED_ROUTE","minimal_witness":["generic mechanism reduces to known search and set cover structures"],"broken_implication":["useful mechanism => novel generic algorithm"],"surviving_invariant":["exact certificate interface remains useful"],"newly_exposed_object":["project-specific certificate calculus and distinction cover"]}}
    return {name:shoulder_search(fs,top_k=2) for name,fs in fixtures.items()}
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--fixtures",action="store_true"); a=p.parse_args(); out=fixture_results(); print(json.dumps(out if a.fixtures else out["hidden_join_coordinate"],indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
