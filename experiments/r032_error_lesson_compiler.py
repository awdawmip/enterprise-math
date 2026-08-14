#!/usr/bin/env python3
"""R032 Post-Error Lesson Compiler: only after researcher-accepted failure."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from r032_shoulder_search import shoulder_search

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FAILURES={"FALSE_ROUTE","OVERSTRONG_ROUTE","MIS_TYPED_ROUTE","PRIOR_ART_ABSORBED_ROUTE","UNPRODUCTIVE_ROUTE"}
REQUIRED_NONEMPTY=("what_survived","new_questions_generated")

def _nonempty_list(event:dict,field:str)->list[str]:
    value=event.get(field)
    if not isinstance(value,list) or not value or any(not str(x).strip() for x in value): raise ValueError(f"LESSON_REQUIRED_NONEMPTY:{field}")
    return [str(x) for x in value]

def compile_lesson(event:dict,*,run_shoulders:bool=True)->dict:
    if not event.get("researcher_accepted_failure",False): raise PermissionError("LESSON_COMPILER_PREMATURE:researcher_has_not_accepted_failure")
    failure_class=event.get("failure_class")
    if failure_class not in ALLOWED_FAILURES: raise ValueError(f"LESSON_BAD_FAILURE_CLASS:{failure_class}")
    for field in REQUIRED_NONEMPTY: _nonempty_list(event,field)
    fs=event.get("failure_structure")
    if not isinstance(fs,dict): raise ValueError("LESSON_FAILURE_STRUCTURE_REQUIRED")
    required=["lesson_id","source_route","original_question","original_claim_or_model","what_failed","minimal_witness_or_failure_evidence","unexpected_structure_revealed","new_distinctions","new_objects_or_coordinates","new_tool_candidate","new_negative_boundary","analogous_prior_failures","how_prior_failures_helped","what_should_NOT_be_inferred","novelty_status","confidence_evidence_grade"]
    missing=[f for f in required if f not in event]
    if missing: raise ValueError(f"LESSON_MISSING_FIELDS:{missing}")
    lesson=dict(event); lesson["compiler_state"]="POST_ERROR_ONLY"; lesson["directive_policy"]="SHOULDERS_NOT_FENCES"
    if run_shoulders: lesson["shoulder_search"]=shoulder_search(fs,top_k=3,exclude_lesson_id=event.get("lesson_id"))
    return lesson

def validate_frozen_lessons()->dict:
    payload=json.loads((ROOT/"research_error_lessons.json").read_text(encoding="utf-8")); compiled=[compile_lesson(x) for x in payload["lessons"]]
    return {"lesson_count":len(compiled),"all_have_survivors":all(x["what_survived"] for x in compiled),"all_have_new_questions":all(x["new_questions_generated"] for x in compiled),"all_have_anti_fence":all("anti_fence" in x["shoulder_search"] for x in compiled),"failure_classes":sorted({x["failure_class"] for x in compiled}),"lesson_ids":[x["lesson_id"] for x in compiled]}

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--validate",action="store_true"); p.parse_args(); print(json.dumps(validate_frozen_lessons(),indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
