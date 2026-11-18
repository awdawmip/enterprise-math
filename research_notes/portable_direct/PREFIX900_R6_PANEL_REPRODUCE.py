#!/usr/bin/env python3
"""PREFIX-900 complete 64-row collision census; exact integers only.

Compile:
  g++ -O3 -std=c++17 -Wall -Wextra PREFIX900_R6_64ROW_FF_COMPLETE.cpp -o /tmp/prefix900
Run:
  python3 PREFIX900_R6_PANEL_REPRODUCE.py /tmp/prefix900 > PREFIX900_R6_PANEL_RESULTS.json
"""
import json, math, subprocess, sys
from collections import Counter

N=1<<32
T=33*N
A,B=262145,524287
ROWS=[510001+194*j for j in range(64)]
S={262147,280001,300001,320003,340007,360007,380003,
   400009,420001,440003,460001,480007,500383,510007,520001,524285}
AX={q for q in range(A,B+1,2)
    if any(((1<<h)-1)%q==0 or ((1<<h)+1)%q==0 for h in range(1,32))}
U=S|AX|{400011+2*j for j in range(256)}|{480011+2*j for j in range(256)}
assert len(U)==552
assert all(q not in U for q in ROWS)

def old(a,b):
    return (a*b<T or a in U or b in U or a//math.gcd(a,b)*b<N
            or 33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a)

def verified_witness(a,b,w):
    x,y,i,j=(w[t] for t in ("x","y","i","j"))
    assert 0<=x<N and 0<=y<N and 0<=i<32 and 0<=j<32
    assert (x!=y or i!=j)
    assert x%a==y%a and (x^(1<<i))%b==(y^(1<<j))%b

def census(exe):
    results=[]
    for a in ROWS:
        result=json.loads(subprocess.check_output([exe,str(a)],text=True))
        assert result["q1"]==a and result["q_count"]==131072
        fields=["old_four_family","zf_new","anchored_ff_new","general_ff_new","unresolved"]
        assert sum(result[x] for x in fields)==131072
        for w in result["general_witnesses"]+result["anchored_examples"]:
            verified_witness(a,w["q2"],w)
        results.append(result)

    counts={key:sum(r[key] for r in results) for key in fields}
    assert counts==dict(old_four_family=507393,zf_new=3484675,
                        anchored_ff_new=4396091,general_ff_new=449,unresolved=0)
    assert [(r["q1"],r["old_four_family"],r["zf_new"],
             r["anchored_ff_new"],r["general_ff_new"]) for r in results[:2]]==[
                 (510001,9041,66268,55759,4),
                 (510195,12738,29929,88402,3)]
    old_rr=sum(old(a,b) for a in ROWS for b in ROWS)
    outside_rr=len(ROWS)**2-old_rr
    assert (old_rr,outside_rr)==(64,4032)
    row_uncovered=len(ROWS)*131072-counts["old_four_family"]
    symmetric_non_old=2*row_uncovered-outside_rr
    novel_after_898=symmetric_non_old-6967420
    novel_after_899=novel_after_898-288336
    total=7574587634+novel_after_898
    assert (row_uncovered,symmetric_non_old,novel_after_898,novel_after_899,total)==(
        7881215,15758398,8790978,8502642,7583378612)
    return dict(schema="PREFIX900_R6_64ROW_EXACT_FF_CERT_V1",
      science_pin="f42f2906d77f24085c123f3ccfe9667d41caa96d",
      domain=dict(p=32,q_min=A,q_max=B,q_step=2,q_count=131072),
      panel_rule="a=510001+194*j for j=0..63",
      checked_row_pairs=64*131072,
      priority_classes=counts,
      previous_four_family_coverage_in_rows=counts["old_four_family"],
      old_uncovered_R_by_R=outside_rr,
      complete_row_column_new_outside_four_family=symmetric_non_old,
      net_new_relative_PREFIX898=novel_after_898,
      net_new_relative_PREFIX899=novel_after_899,
      certified_total_after_PREFIX900=total,
      unresolved_after_PREFIX900=131072**2-total,
      rows=results,
      mathematical_review="NOT_INDEPENDENTLY_REVIEWED")

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: script.py /path/to/compiled/checker")
    print(json.dumps(census(sys.argv[1]),ensure_ascii=False,indent=2))
