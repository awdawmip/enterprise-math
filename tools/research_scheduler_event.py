#!/usr/bin/env python3
"""Emit canonical Enterprise Math Scheduler V2 event JSON.

This helper prevents hand-written event-shape drift. It emits one JSON object to
stdout; callers append that exact object as one Issue #240 comment. Cross-layer
APPROVE/REVIEW evidence is emitted here and checked by tools/research_control.py.
"""
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

try:
    from tools import research_scheduler as rs
except ModuleNotFoundError:
    import research_scheduler as rs  # type: ignore[no-redef]


def emit(event: dict[str, Any]) -> None:
    print(json.dumps(event, ensure_ascii=False, separators=(",", ":")))


def base(args: argparse.Namespace, kind: str) -> dict[str, Any]:
    return {"schema": rs.V2_SCHEMA, "event": kind, "task_id": args.task_id, "at": args.at}


def parse_taskbook(path: pathlib.Path) -> dict[str, Any]:
    meta = rs.split_taskbook_metadata(path.read_text(encoding="utf-8"))
    if not isinstance(meta, dict) or not isinstance(meta.get("task_id"), str):
        raise SystemExit("taskbook must contain ENTERPRISE_MATH_TASK_V1 frontmatter with task_id")
    return meta


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Emit Enterprise Math Scheduler V2 event JSON")
    sp = p.add_subparsers(dest="cmd", required=True)

    pub = sp.add_parser("publish-taskbook")
    pub.add_argument("path", type=pathlib.Path); pub.add_argument("--taskbook-ref", required=True)
    pub.add_argument("--publisher-id", required=True); pub.add_argument("--publisher-role", choices=["RESEARCHER","RESEARCH_DRIVER","FOUNDATION_STEWARD"], required=True); pub.add_argument("--at", required=True)

    prop = sp.add_parser("publish-proposal")
    prop.add_argument("--task-id", required=True); prop.add_argument("--title", required=True); prop.add_argument("--publisher-id", required=True); prop.add_argument("--publisher-role", choices=["RESEARCHER","RESEARCH_DRIVER","FOUNDATION_STEWARD"], required=True); prop.add_argument("--at", required=True)
    prop.add_argument("--kind", default="RESEARCH"); prop.add_argument("--owner", default="proposal/unassigned"); prop.add_argument("--priority", default="P1"); prop.add_argument("--leverage", default="MEDIUM"); prop.add_argument("--frontier", required=True); prop.add_argument("--next-action", required=True); prop.add_argument("--publication-ref")

    rc = sp.add_parser("review-claim"); rc.add_argument("--task-id", required=True); rc.add_argument("--reviewer-id", required=True); rc.add_argument("--review-claim-id", required=True); rc.add_argument("--at", required=True); rc.add_argument("--lease-minutes", type=int)
    ap = sp.add_parser("approve"); ap.add_argument("--task-id", required=True); ap.add_argument("--reviewer-id", required=True); ap.add_argument("--review-claim-id", required=True); ap.add_argument("--taskbook-ref", required=True); ap.add_argument("--review-ref", required=True); ap.add_argument("--taskbook-audit", choices=["PASS"], required=True); ap.add_argument("--policy-digest", required=True); ap.add_argument("--at", required=True)
    cl = sp.add_parser("claim"); cl.add_argument("--task-id", required=True); cl.add_argument("--execution-id", required=True); cl.add_argument("--claim-id", required=True); cl.add_argument("--at", required=True); cl.add_argument("--lease-minutes", type=int); cl.add_argument("--actor")
    ad = sp.add_parser("adopt"); ad.add_argument("--task-id", required=True); ad.add_argument("--execution-id", required=True); ad.add_argument("--claim-id", required=True); ad.add_argument("--recovery-ref", required=True); ad.add_argument("--at", required=True); ad.add_argument("--lease-minutes", type=int); ad.add_argument("--actor")
    pr = sp.add_parser("progress"); pr.add_argument("--task-id", required=True); pr.add_argument("--execution-id", required=True); pr.add_argument("--claim-id", required=True); pr.add_argument("--progress-ref", required=True); pr.add_argument("--next-action", required=True); pr.add_argument("--at", required=True); pr.add_argument("--lease-minutes", type=int)
    su = sp.add_parser("submit"); su.add_argument("--task-id", required=True); su.add_argument("--execution-id", required=True); su.add_argument("--claim-id", required=True); su.add_argument("--return-ref", required=True); su.add_argument("--evidence-ref", action="append", default=[]); su.add_argument("--at", required=True)
    rv = sp.add_parser("review"); rv.add_argument("--task-id", required=True); rv.add_argument("--reviewer-id", required=True); rv.add_argument("--review-claim-id", required=True); rv.add_argument("--verdict", required=True); rv.add_argument("--review-ref", required=True); rv.add_argument("--next-action"); rv.add_argument("--finding", action="append", default=[]); rv.add_argument("--at", required=True)
    rv.add_argument("--method-harvest", required=True, choices=["GLOBAL_TOOL_FAMILY","GLOBAL_SUBTOOL","DOMAIN_FACADE","DOMAIN_OPERATOR","RESULT_ONLY","CANDIDATE_NOT_TOOL","DUPLICATE_ALIAS","NO_TOOL_PAYLOAD"])
    rv.add_argument("--evidence-class", required=True, choices=["SOURCE_ONLY","BLIND_REPLICATION","STATEMENT_EXPOSED_AUDIT","MIXED_INDEPENDENT_EVIDENCE","FORMAL_KERNEL","BENCHMARK","GOVERNANCE","NEGATIVE_OBSTRUCTION"])
    rv.add_argument("--route-disposition", required=True, choices=["CONTINUE_SAME_TASK","OPEN_CONTINUATION","OPEN_INDEPENDENT_REPLICATION_CHILD","ROUTE_TO_FOUNDATION","ROUTE_TO_FORMALIZATION","ROUTE_TO_PROMOTION","PARK","CLOSE"])
    rv.add_argument("--route-ref"); rv.add_argument("--successor-gate-ref"); rv.add_argument("--child-task-id"); rv.add_argument("--child-task-ref"); rv.add_argument("--independence-protocol")
    oo = sp.add_parser("orphan"); oo.add_argument("--task-id", required=True); oo.add_argument("--driver-id", required=True); oo.add_argument("--reason", required=True); oo.add_argument("--evidence-ref"); oo.add_argument("--at", required=True)
    mi = sp.add_parser("migrate"); mi.add_argument("--task-id", required=True); mi.add_argument("--driver-id", required=True); mi.add_argument("--migration-ref", required=True); mi.add_argument("--target-state", required=True); mi.add_argument("--at", required=True); mi.add_argument("--taskbook", type=pathlib.Path); mi.add_argument("--execution-id"); mi.add_argument("--claim-id"); mi.add_argument("--return-ref"); mi.add_argument("--lease-minutes", type=int); mi.add_argument("--actor")

    args = p.parse_args(argv)
    if args.cmd == "publish-taskbook":
        task = parse_taskbook(args.path); event = {"schema":rs.V2_SCHEMA,"event":"PUBLISH","task_id":task["task_id"],"at":args.at,"publisher_id":args.publisher_id,"publisher_role":args.publisher_role,"taskbook_ref":args.taskbook_ref,"publication_ref":args.taskbook_ref,"task":task}; emit(event); return 0
    if args.cmd == "publish-proposal":
        task = {"task_id":args.task_id,"title":args.title,"kind":args.kind,"owner":args.owner,"base_state":"DRAFT","priority":args.priority,"leverage":args.leverage,"frontier":args.frontier,"next_action":args.next_action,"dependencies":[],"source_refs":[args.publication_ref] if args.publication_ref else [],"last_progress_ref":args.publication_ref,"last_progress_at":args.at,"hard_block":None}
        event = {"schema":rs.V2_SCHEMA,"event":"PUBLISH","task_id":args.task_id,"at":args.at,"publisher_id":args.publisher_id,"publisher_role":args.publisher_role,"publication_ref":args.publication_ref,"task":task}; emit(event); return 0
    if args.cmd == "review-claim":
        event=base(args,"REVIEW_CLAIM"); event.update(reviewer_id=args.reviewer_id,review_claim_id=args.review_claim_id)
        if args.lease_minutes: event["lease_minutes"]=args.lease_minutes
        emit(event); return 0
    if args.cmd == "approve":
        if not args.policy_digest.startswith("sha256:"):
            raise SystemExit("--policy-digest must use sha256:<digest>")
        event=base(args,"APPROVE"); event.update(reviewer_id=args.reviewer_id,review_claim_id=args.review_claim_id,taskbook_ref=args.taskbook_ref,review_ref=args.review_ref,taskbook_audit=args.taskbook_audit,policy_digest=args.policy_digest); emit(event); return 0
    if args.cmd in {"claim","adopt"}:
        event=base(args,"ADOPT" if args.cmd=="adopt" else "CLAIM"); event.update(execution_id=args.execution_id,claim_id=args.claim_id,actor_role="RESEARCHER")
        if args.actor: event["actor"]=args.actor
        if args.lease_minutes: event["lease_minutes"]=args.lease_minutes
        if args.cmd=="adopt": event["recovery_ref"]=args.recovery_ref
        emit(event); return 0
    if args.cmd == "progress":
        event=base(args,"PROGRESS"); event.update(execution_id=args.execution_id,claim_id=args.claim_id,progress_ref=args.progress_ref,next_action=args.next_action)
        if args.lease_minutes: event["lease_minutes"]=args.lease_minutes
        emit(event); return 0
    if args.cmd == "submit":
        event=base(args,"SUBMIT"); event.update(execution_id=args.execution_id,claim_id=args.claim_id,return_ref=args.return_ref,evidence_refs=args.evidence_ref); emit(event); return 0
    if args.cmd == "review":
        if args.verdict == "REQUEST_INDEPENDENT_REPLICATION":
            raise SystemExit("REQUEST_INDEPENDENT_REPLICATION is forbidden in V2 cross-layer control; PARK parent and open a distinct independent-replication child task")
        if args.route_disposition == "OPEN_INDEPENDENT_REPLICATION_CHILD":
            if args.verdict != "PARK" or not all((args.child_task_id,args.child_task_ref,args.independence_protocol)):
                raise SystemExit("OPEN_INDEPENDENT_REPLICATION_CHILD requires verdict=PARK plus child task id/ref and independence protocol")
            if args.child_task_id == args.task_id:
                raise SystemExit("independent replication child task_id must differ from parent task_id")
        if args.route_disposition == "OPEN_CONTINUATION" and not args.successor_gate_ref:
            raise SystemExit("OPEN_CONTINUATION requires --successor-gate-ref")
        if args.route_disposition in {"OPEN_CONTINUATION","ROUTE_TO_FOUNDATION","ROUTE_TO_FORMALIZATION","ROUTE_TO_PROMOTION"} and not args.route_ref:
            raise SystemExit(f"{args.route_disposition} requires --route-ref")
        event=base(args,"REVIEW"); event.update(reviewer_id=args.reviewer_id,review_claim_id=args.review_claim_id,verdict=args.verdict,review_ref=args.review_ref,findings=args.finding,method_harvest=args.method_harvest,evidence_class=args.evidence_class,route_disposition=args.route_disposition)
        if args.next_action: event["next_action"]=args.next_action
        for name in ("route_ref","successor_gate_ref","child_task_id","child_task_ref","independence_protocol"):
            value=getattr(args,name)
            if value: event[name]=value
        emit(event); return 0
    if args.cmd == "orphan":
        event=base(args,"ORPHAN"); event.update(driver_id=args.driver_id,reason=args.reason)
        if args.evidence_ref: event["evidence_ref"]=args.evidence_ref
        emit(event); return 0
    if args.cmd == "migrate":
        event=base(args,"MIGRATE"); event.update(driver_id=args.driver_id,migration_ref=args.migration_ref,target_state=args.target_state)
        if args.taskbook: event["task"]=parse_taskbook(args.taskbook)
        for name in ("execution_id","claim_id","return_ref","lease_minutes","actor"):
            value=getattr(args,name)
            if value is not None: event[name]=value
        if args.execution_id and args.target_state=="RETURN_REVIEW": event["submitted_by"]=args.execution_id
        emit(event); return 0
    raise AssertionError(args.cmd)

if __name__ == "__main__": raise SystemExit(main())
