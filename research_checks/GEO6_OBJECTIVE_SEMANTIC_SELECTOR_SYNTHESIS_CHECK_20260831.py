#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter, defaultdict, deque

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/"research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas.json"
M=ROOT/"research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/accepted_resolver_manifest.json"
TASK="RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS"
PUB="TP2-6866CB3F890F6563C474"
RID="EM-G6OBJS1-74C2D9"
SNAP="228446b2d797372b2d18503116f612ba03701184"
SEL=["CONTACT_SELECTOR","LOCALITY_REFINEMENT_SELECTOR","ROTATION_CLOSURE_SELECTOR","TRANSLATION_ACTION_SELECTOR","NONOVERLAP_SELECTOR","TRANSLATION_FOLNER_SELECTOR","PHYSICAL_REFINEMENT_SELECTOR","MIXED_DIRECTION_SELECTOR","SUPPORT_RELATION_SELECTOR","SELF_DUAL_IDENTIFICATION_SELECTOR","COMPLEXITY_FUNCTIONAL_SELECTOR","REFINEMENT_TRANSPORT_SELECTOR"]
ROOTS={0,1,2,3,4,8}
PARTIAL={0,2,7}
LANES={
 "F":["FIRSTWAVE","RR-547A186EBDE5EE6CD8A3","DR-CE3F008C48F9EBBFF9FA"],
 "K":["PACKING_KAKEYA","RR-B5DB25EC13BF1C42DC9B","DR-4187E7655E4E30A30253"],
 "M":["MAHLER","RR-EC0502A82AD5DC3995F4","DR-6A6587387463AE326117"]}
STATUS={"R":"RESOLVED_BY_ACCEPTED_DATUM","P":"PARTIALLY_CONSTRAINED_BY_ACCEPTED_DATUM","U":"UNRESOLVED","D":"DUPLICATE_SELECTOR"}
PAIR={"O":"ORTHOGONAL","D":"STRICT_DEPENDENCY_EARLIER_TO_LATER","X":"OVERLAP_NOT_EQUIVALENT","S":"SAME_SELECTOR","U":"UNRESOLVED_RELATION"}

def load(p):
    with p.open(encoding="utf-8") as f:return json.load(f)

def acyclic(n,edges):
    out=defaultdict(list); indeg=[0]*n
    for a,b in edges:
        assert 0<=a<n and 0<=b<n and a!=b
        out[a].append(b); indeg[b]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0); seen=0
    while q:
        x=q.popleft(); seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert seen==n

def main():
    a,m=load(A),load(M)
    for o in (a,m):
        assert o["task_id"]==TASK and o["publication_id"]==PUB and o["researcher_id"]==RID and o["snapshot"]==SNAP
    assert a["schema"]=="GEO6_OBJECTIVE_SEMANTIC_SELECTOR_ATLAS_V1"
    assert m["schema"]=="GEO6_ACCEPTED_RESOLVER_MANIFEST_V1"
    assert a["lane_legend"]==LANES and a["status_legend"]==STATUS
    rows=a["selectors"]; assert [r["id"] for r in rows]==SEL and len(rows)==12
    assert Counter(r["status"] for r in rows)==Counter({"P":3,"U":9})
    assert {i for i,r in enumerate(rows) if r["status"]=="P"}==PARTIAL
    assert a["counts"]=={"R":0,"P":3,"U":9,"D":0} and a["duplicate_pairs"]==[]
    pm=a["pair_matrix"]; assert pm["order"]==SEL and pm["encoding"]==PAIR
    assert len(pm["upper_rows"])==11
    assert [len(x) for x in pm["upper_rows"]]==list(range(11,0,-1))
    chars="".join(pm["upper_rows"]); assert len(chars)==66 and set(chars)<=set(PAIR)
    assert "S" not in chars
    assert set(a["roots"])==ROOTS; acyclic(12,a["dependency_dag"])
    assert len(a["recommendations"])<=3 and a["parent_decision"]=="MINIMAL_SUCCESSOR_TASKSET_JUSTIFIED"
    assert a["promotion"]=={"working_truth":False,"foundation":False,"canonical":False,"novelty":False}
    assert m["authority"]=="ACCEPTED_DRIVER_REVIEW+BOUND_RESULT+EXACT_TYPE_MAP_REQUIRED"
    assert all(c[3]=="ACCEPTED" for c in m["candidates"])
    assert m["full_resolvers"]==[]
    assert m["conclusion"]=={"resolved":0,"partial":3,"unresolved":9,"duplicate":0}
    bindings={int(k):v for k,v in m["partial_bindings"].items()}
    for i,r in enumerate(rows):
        assert bindings.get(i,[])==r["resolvers"]
    print("PASS GEO6_OBJECTIVE_SELECTOR_ATLAS")
    print("selectors=12 pairs=66 resolved=0 partial=3 unresolved=9 duplicate=0 roots=6 recommendations=3")

if __name__=="__main__": main()
