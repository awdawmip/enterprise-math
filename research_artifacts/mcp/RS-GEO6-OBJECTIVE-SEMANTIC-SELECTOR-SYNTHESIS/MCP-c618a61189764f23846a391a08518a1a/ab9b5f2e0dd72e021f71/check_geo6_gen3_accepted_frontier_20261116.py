#!/usr/bin/env python3
"""Check the precise frozen GEO6 selector atlas plus accepted status-stage consistency.
Author regression only. Reads JSON beside this file. Not a full Source admission checker.
"""
from __future__ import annotations
import json
from pathlib import Path

def main():
    a=json.loads((Path(__file__).parent/"geo6_gen3_accepted_frontier_rebase_20261116.json").read_text(encoding="utf-8"))
    f=a["frozen_math"]
    assert len(f["selectors"])==12==len(set(f["selectors"]))
    rows=f["upper_rows"]
    assert len(rows)==11 and [len(r) for r in rows]==list(range(11,0,-1))
    assert sum(len(r) for r in rows)==66
    assert all(set(row)<=set("ODXSU") and "S" not in row for row in rows)
    assert len(f["dependency_dag"])==7 and len(f["roots"])==6
    assert f["dependency_dag"]==[[3,5],[1,6],[6,7],[8,9],[8,10],[8,11],[6,11]]
    assert f["roots"]==[0,1,2,3,4,8]
    assert f["recommendation_count"]==3 and f["full_resolvers"]==[]
    ss=a["stages"]
    assert len(ss)==3
    assert [s["partial_indices"] for s in ss]==[[0,2,7],[0,2,6,7,11],[0,2,3,4,5,6,7,8,11]]
    assert [s["counts"] for s in ss]==[
      {"R":0,"P":3,"U":9,"D":0},
      {"R":0,"P":5,"U":7,"D":0},
      {"R":0,"P":9,"U":3,"D":0}]
    for s in ss:
        p=s["partial_indices"]
        assert sorted(set(p))==p and all(0<=x<12 for x in p)
        assert s["counts"]["P"]==len(p)
        assert sum(s["counts"].values())==12
    assert set(ss[0]["partial_indices"])<=set(ss[1]["partial_indices"])<=set(ss[2]["partial_indices"])
    previous=set(ss[1]["partial_indices"])
    delta=set(ss[2]["partial_indices"])-previous
    added={i for review in a["terminal_review_bindings"] for i in review["new_partial_indices"]}
    assert added==delta=={3,4,5,8}
    assert all(review["disposition"]=="ACCEPTED" for review in a["terminal_review_bindings"])
    assert a["parent"]["current_status"]=="CLOSED"
    print("PASS: 12 selectors; 66 pairs; 7 edges; 6 roots; accepted 3->5->9 partial; CLOSED parent")

if __name__=="__main__":
    main()
