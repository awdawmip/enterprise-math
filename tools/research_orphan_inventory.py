#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
SCHEMA="ENTERPRISE_MATH_RESEARCH_ORPHAN_INVENTORY_V1"
PREFIXES=("research/","research-task/","free/")
SUFFIXES={".json",".md",".txt",".yaml",".yml",".lean",".py"}
BRE=re.compile(r"(?:free|research|research-task)/[A-Za-z0-9._/-]+")
SRE=re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")

def run(a,check=True):
 p=subprocess.run(a,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if check and p.returncode: raise RuntimeError(f"{a}: {p.stderr.strip()}")
 return p.stdout.strip()
def git(*a,check=True): return run(["git",*a],check=check)
def parse(body):
 s=(body or "").strip(); xs=[s]; m=re.search(r"```(?:json)?\s*(\{.*?\})\s*```",s,re.S)
 if m: xs.append(m.group(1))
 i,j=s.find("{"),s.rfind("}")
 if i>=0 and j>i: xs.append(s[i:j+1])
 for x in xs:
  try:v=json.loads(x)
  except Exception:continue
  if isinstance(v,dict):return v
 return None
def events(path):
 if not path:return []
 raw=json.loads(path.read_text());out=[]
 for x in raw:
  if not isinstance(x,dict):continue
  v=parse(str(x.get("body","")))
  if v:
   v=dict(v);v["_id"]=x.get("id");v["_created"]=x.get("created_at");out.append(v)
 return out
def main_index():
 branches=set();shas=set();n=0
 prefixes=("research_task_records/","research_result_records/","research_execution_records/","research_tasks/","driver_reviews/","control_plane/")
 for rel in git("ls-tree","-r","--name-only","origin/main").splitlines():
  p=Path(rel)
  if p.suffix.lower() not in SUFFIXES:continue
  if "research_orphan_recovery" in rel or "research_orphan_inventory" in rel:continue
  if not (rel.startswith(prefixes) or "candidate" in rel.lower()):continue
  text=git("show",f"origin/main:{rel}",check=False)
  if not text or len(text)>2_000_000:continue
  n+=1;branches.update(BRE.findall(text));shas.update(SRE.findall(text))
 return branches,shas,n
def refs():
 out=[]
 for r in git("for-each-ref","--format=%(refname:short)","refs/remotes/origin/").splitlines():
  if not r.startswith("origin/") or r=="origin/main" or r.endswith("/HEAD"):continue
  b=r[7:]
  if b.startswith(PREFIXES):out.append(b)
 return sorted(set(out))
def meta(b):
 tip=git("rev-parse",f"origin/{b}"); fields=git("show","-s","--format=%cI%x00%s",tip).split("\x00",1)
 ch=git("cherry","origin/main",f"origin/{b}",check=False); plus=[];minus=0
 for ln in ch.splitlines():
  if ln.startswith("+"):plus.append(ln[2:].strip())
  elif ln.startswith("-"):minus+=1
 return {"branch":b,"tip_sha":tip,"tip_at":fields[0] if fields else None,"tip_subject":fields[1] if len(fields)>1 else "","unmerged_patch_commits":len(plus),"patch_equivalent_commits":minus,"unique_commit_shas":plus}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--events",type=Path);ap.add_argument("--output",type=Path,required=True);a=ap.parse_args()
 bs,ss,n=main_index();ev=events(a.events);by=defaultdict(list)
 for e in ev:
  b=e.get("execution_branch")
  if isinstance(b,str):by[b].append(e)
 rows=[]
 for b in refs():
  r=meta(b);r["main_reference"]={"branch_mentioned":b in bs,"tip_mentioned":r["tip_sha"] in ss}
  r["control_events"]=[{"event":e.get("event"),"task_id":e.get("task_id"),"publication_id":e.get("publication_id"),"claim_id":e.get("claim_id"),"result_id":e.get("result_id"),"server_comment_id":e.get("_id"),"at":e.get("at") or e.get("_created")} for e in by.get(b,[])]
  rows.append(r)
 result={"schema":SCHEMA,"status":"RAW_INVENTORY_NOT_STATE_NOT_DISPATCH_NOT_CLAIM","generated_at":datetime.now(timezone.utc).isoformat(),"source_main_sha":git("rev-parse","origin/main"),"inputs":{"raw_issue_240_comments":len(json.loads(a.events.read_text())) if a.events else 0,"parsed_control_events":len(ev),"main_state_corpus_files":n},"summary":{"branches_scanned":len(rows),"live_unmerged_frontiers":sum(r["unmerged_patch_commits"]>0 for r in rows)},"all_frontiers":rows}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n");print(json.dumps(result["summary"],indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
