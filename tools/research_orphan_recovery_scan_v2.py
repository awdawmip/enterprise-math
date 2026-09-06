#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA="ENTERPRISE_MATH_RESEARCH_ORPHAN_RECOVERY_SCAN_V2"
PREFIXES=("research/","research-task/","free/")
TEXT_SUFFIXES={".json",".md",".txt",".yaml",".yml",".lean",".py"}
BRANCH_TOKEN_RE=re.compile(r"(?:free|research|research-task)/[A-Za-z0-9._/-]+")
SHA_RE=re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")


def run(args:list[str],check=True)->str:
    p=subprocess.run(args,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if check and p.returncode: raise RuntimeError(f"{args}: {p.stderr.strip()}")
    return p.stdout.strip()
def git(*a:str,check=True)->str:return run(["git",*a],check=check)

def parse_body(body:str)->dict[str,Any]|None:
    s=(body or "").strip(); choices=[s]
    m=re.search(r"```(?:json)?\s*(\{.*?\})\s*```",s,re.S)
    if m: choices.append(m.group(1))
    i,j=s.find("{"),s.rfind("}")
    if i>=0 and j>i: choices.append(s[i:j+1])
    for c in choices:
        try:v=json.loads(c)
        except Exception:continue
        if isinstance(v,dict):return v
    return None

def load_events(path:Path|None)->list[dict[str,Any]]:
    if not path:return []
    raw=json.loads(path.read_text()); out=[]
    for item in raw if isinstance(raw,list) else []:
        if not isinstance(item,dict):continue
        v=parse_body(str(item.get("body","")))
        if v:
            v=dict(v);v["_server_comment_id"]=item.get("id");v["_server_created_at"]=item.get("created_at");out.append(v)
    return out

def main_state_index()->tuple[set[str],set[str],int]:
    branch_tokens:set[str]=set();sha_tokens:set[str]=set();n=0
    for rel in git("ls-files").splitlines():
        p=Path(rel)
        if p.suffix.lower() not in TEXT_SUFFIXES:continue
        if not (rel.startswith("research_task_records/") or rel.startswith("research_result_records/") or rel.startswith("research_execution_records/") or rel.startswith("control_plane/") or rel.startswith("research_tasks/") or "candidate" in rel.lower()):continue
        try:t=p.read_text(errors="replace")
        except OSError:continue
        if len(t)>2_000_000:continue
        n+=1; branch_tokens.update(BRANCH_TOKEN_RE.findall(t)); sha_tokens.update(SHA_RE.findall(t))
    return branch_tokens,sha_tokens,n

def branches()->list[str]:
    out=[]
    for ref in git("for-each-ref","--format=%(refname:short)","refs/remotes/origin/").splitlines():
        if not ref.startswith("origin/") or ref=="origin/main" or ref.endswith("/HEAD"):continue
        b=ref[7:]
        if b.startswith(PREFIXES):out.append(b)
    return sorted(set(out))
def meta(b:str)->dict[str,Any]:
    tip=git("rev-parse",f"origin/{b}")
    s=git("show","-s","--format=%cI%x00%s",tip).split("\x00",1)
    ch=git("cherry","origin/main",f"origin/{b}",check=False)
    plus=[];minus=0
    for ln in ch.splitlines():
        if ln.startswith("+"):plus.append(ln[2:].strip())
        elif ln.startswith("-"):minus+=1
    return {"branch":b,"lane":"FREE_RESEARCH" if b.startswith("free/") else "TASK_RESEARCH","tip_sha":tip,"tip_at":s[0] if s else None,"tip_subject":s[1] if len(s)>1 else "","unmerged_patch_commits":len(plus),"patch_equivalent_commits":minus,"unique_commit_shas":plus}
def free_descendant_cover(rows:list[dict[str,Any]])->dict[str,str]:
    # Only exact ancestry is collapsed; names are never treated as semantic equivalence.
    live=[r for r in rows if r["lane"]=="FREE_RESEARCH" and r["unmerged_patch_commits"]>0]
    live.sort(key=lambda r:r.get("tip_at") or "")
    cover={}
    for i,r in enumerate(live):
        best=None
        for o in live[i+1:]:
            rc=subprocess.run(["git","merge-base","--is-ancestor",r["tip_sha"],o["tip_sha"]],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
            if rc==0:best=o
        if best:cover[r["branch"]]=best["branch"]
    return cover
def event_index(events:list[dict[str,Any]])->dict[str,list[dict[str,Any]]]:
    d=defaultdict(list)
    for e in events:
        b=e.get("execution_branch")
        if isinstance(b,str):d[b].append(e)
    return d

def classify(r,cover,ev_by_branch,branch_tokens,sha_tokens):
    x=dict(r); ev=ev_by_branch.get(r["branch"],[])
    x["main_reference"]={"branch_mentioned":r["branch"] in branch_tokens,"tip_mentioned":r["tip_sha"] in sha_tokens}
    x["control_events"]=[{"event":e.get("event"),"task_id":e.get("task_id"),"publication_id":e.get("publication_id"),"claim_id":e.get("claim_id"),"result_id":e.get("result_id"),"server_comment_id":e.get("_server_comment_id"),"at":e.get("at") or e.get("_server_created_at")} for e in ev]
    if r["unmerged_patch_commits"]==0:
        x.update(classification="INTEGRATED_OR_PATCH_EQUIVALENT",actionable=False);return x
    if r["branch"] in cover:
        x.update(classification="COVERED_BY_DESCENDANT_FREE_BRANCH",covered_by=cover[r["branch"]],actionable=False);return x
    if r["lane"]=="TASK_RESEARCH":
        if ev:
            x.update(classification="EXISTING_CONTROL_EVENT_LINEAGE",actionable=False,projection="PRESERVE_EXISTING_TASK_RUNTIME_STATE")
        else:
            x.update(classification="DANGLING_TASK_RESEARCH_FRONTIER",actionable=True,projection="BLOCKED_RECOVERY_CAPSULE_PENDING_EXACT_TASK_PROVENANCE",projected_dispatch_state="BLOCKED")
        return x
    refs=x["main_reference"]
    if refs["branch_mentioned"] or refs["tip_mentioned"]:
        x.update(classification="FREE_FRONTIER_WITH_MAIN_STATE_REFERENCE",actionable=False,projection="PRESERVE_EXISTING_FREE_CANDIDATE_OR_DURABLE_INTAKE")
    else:
        x.update(classification="DANGLING_FREE_RESEARCH_FRONTIER",actionable=True,projection="FREE_AXIOM_CANDIDATE_STATE_MACHINE",projected_candidate_state="DISCOVERY_IN_PROGRESS")
    return x

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--events",type=Path);ap.add_argument("--output",type=Path,required=True);a=ap.parse_args()
    branch_tokens,sha_tokens,corpus_files=main_state_index();events=load_events(a.events);ev_by_branch=event_index(events)
    rows=[meta(b) for b in branches()];cover=free_descendant_cover(rows)
    allrows=[classify(r,cover,ev_by_branch,branch_tokens,sha_tokens) for r in rows];action=[r for r in allrows if r.get("actionable")]
    counts=defaultdict(int)
    for r in allrows:counts[r["classification"]]+=1
    result={"schema":SCHEMA,"status":"AUDIT_ONLY_NOT_DISPATCH_NOT_CLAIM_AUTHORITY","generated_at":datetime.now(timezone.utc).isoformat(),"source_main_sha":git("rev-parse","origin/main"),"contracts":{"task_publication":"research_task_publication_contract_v2.json","free_candidate_state_machine":"research_axiom_candidate_state_machine.json"},"invariants":["BRANCH_PRESENCE != ORPHAN","PATCH_EQUIVALENT_TO_MAIN != ORPHAN","ANCESTRY_COVERED_FREE_BRANCH != ORPHAN","AUDIT_OUTPUT != TASK_AVAILABILITY","AUDIT_OUTPUT != CLAIM","DANGLING_FREE_RESEARCH != AUTOMATIC_EXPLICIT_TASK","FREE_RECOVERY_STARTS_AT_DISCOVERY_IN_PROGRESS_UNLESS_EXISTING_AUDIT_PROVES_STRONGER_STATE","DANGLING_TASK_WITHOUT_EXACT_PROVENANCE_FAILS_CLOSED_BLOCKED"],"inputs":{"remote_branch_prefixes":list(PREFIXES),"raw_issue_240_comments":len(json.loads(a.events.read_text())) if a.events else 0,"parsed_control_events":len(events),"main_state_corpus_files":corpus_files,"indexed_branch_refs":len(branch_tokens),"indexed_sha_refs":len(sha_tokens)},"summary":{"branches_scanned":len(allrows),"free_branches_scanned":sum(r["lane"]=="FREE_RESEARCH" for r in allrows),"task_branches_scanned":sum(r["lane"]=="TASK_RESEARCH" for r in allrows),"actionable_orphan_frontiers":len(action),"actionable_task_frontiers":sum(r["lane"]=="TASK_RESEARCH" for r in action),"actionable_free_frontiers":sum(r["lane"]=="FREE_RESEARCH" for r in action),"classification_counts":dict(sorted(counts.items()))},"actionable":action,"all_frontiers":allrows}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n");print(json.dumps(result["summary"],ensure_ascii=False,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
