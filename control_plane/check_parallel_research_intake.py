#!/usr/bin/env python3
"""Validate non-destructive parallel research intake against single runtime authority."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK = "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE"
A = "TP2-A63015C2EB99D00F2500"
B = "TP2-9D0A43C4F217B6E8C531"
INTAKE_ID = "PI-R043C4-20260826-01"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def audit() -> list[str]:
    errors: list[str] = []
    contract = load("research_parallel_intake_contract.json")
    if contract.get("status") != "ACTIVE":
        errors.append("parallel research intake contract must be ACTIVE")
    runtime = contract.get("runtime_boundary", {})
    if runtime.get("operational_publication_implies_canonical_truth") is not False:
        errors.append("operational publication must not imply canonical truth")
    if runtime.get("operational_publication_implies_epistemic_preference") is not False:
        errors.append("operational publication must not imply epistemic preference")
    if runtime.get("parallel_nonoperational_publications_remain_research_assets") is not True:
        errors.append("parallel non-operational publications must remain research assets")

    resolution = load("research_task_publication_resolutions.json")
    matches = [r for r in resolution.get("resolutions", []) if r.get("task_id") == TASK]
    if len(matches) != 1:
        return errors + [f"expected exactly one operational resolution for {TASK}"]
    r = matches[0]
    if r.get("operational_publication_id") != A or r.get("canonical_publication_id") != A:
        errors.append("R043-C4 runtime operational publication must remain A630")
    if set(r.get("retained_parallel_publication_ids", [])) != {A, B}:
        errors.append("R043-C4 must retain both publication records as parallel research assets")
    if r.get("parallel_intake_id") != INTAKE_ID:
        errors.append("R043-C4 resolution must pin the parallel intake record")
    if r.get("working_truth_granted") is not False or r.get("canonical_promotion_granted") is not False:
        errors.append("R043-C4 operational resolution cannot grant truth or canonical promotion")

    intake_path = f"research_parallel_intake_records/{TASK}/{INTAKE_ID}.json"
    intake = load(intake_path)
    if intake.get("record_state") != "REFERENCE_COMPLETE_KEEP_PARALLEL":
        errors.append("parallel intake must complete both reference passes")
    if intake.get("current_disposition") != "KEEP_PARALLEL_AND_SELECT_OPERATIONAL":
        errors.append("parallel intake disposition must keep both and select one operationally")
    if intake.get("operational_binding", {}).get("publication_id") != A:
        errors.append("parallel intake operational binding must match A630")
    if intake.get("operational_binding", {}).get("epistemic_preference") is not False:
        errors.append("parallel intake operational binding cannot express epistemic preference")
    if intake.get("delete_or_rewrite_parallel_objects") is not False:
        errors.append("parallel objects may not be deleted or rewritten for single-valued runtime")
    publications = {
        obj.get("publication_id")
        for obj in intake.get("parallel_objects", [])
        if obj.get("object_kind") == "TASK_PUBLICATION"
    }
    if publications != {A, B}:
        errors.append("parallel intake publication set does not contain exactly both R043-C4 publications")

    p1 = load(f"research_parallel_reference_reviews/{INTAKE_ID}/PASS1-INDEPENDENT-REFERENCE.json")
    p2 = load(f"research_parallel_reference_reviews/{INTAKE_ID}/PASS2-CROSS-REFERENCE.json")
    if set(p1.get("survivor_publication_ids", [])) != {A, B}:
        errors.append("reference pass 1 must retain both publications")
    if p2.get("final_disposition") != "KEEP_PARALLEL_AND_SELECT_OPERATIONAL":
        errors.append("reference pass 2 must end KEEP_PARALLEL_AND_SELECT_OPERATIONAL")
    if p2.get("comparison", {}).get("mathematical_conflict") is not False:
        errors.append("R043-C4 pass 2 currently records no mathematical conflict")
    if p2.get("operational_binding", {}).get("epistemic_preference") is not False:
        errors.append("reference pass 2 operational binding cannot express epistemic preference")
    for obj in (contract, intake, p1, p2):
        if obj.get("working_truth_granted") is not False:
            errors.append("parallel-intake artifacts may not grant Working Truth")
        if obj.get("canonical_promotion_granted") is not False:
            errors.append("parallel-intake artifacts may not grant canonical promotion")
    return errors


if __name__ == "__main__":
    failures = audit()
    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)
    print("PASS: parallel research evidence is preserved while R043-C4 runtime authority remains single-valued.")
