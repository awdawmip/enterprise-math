#!/usr/bin/env python3
"""Exact residual-row mass table for the R4 five-tail branch omitting h=2.

This verifies finite geometry used with the all-order bound in tail_proof.md.
It does not use a prime magnitude cutoff or perform a native BRC execution.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

B={0,3,5,8,10,15,21,23,26,28,30,31,33}
ROWS=sorted({w%7 for w in B})
CHOICES=[("none",0,F(0)),("246241",1,F(1,3)),
         ("487824887233",1,F(1,4)),("both",2,F(1,2))]


def main():
    assert ROWS==[0,1,2,3,5]
    summaries=[]
    cases=[]
    for name,a,p in CHOICES:
        for m in range(6-a):
            if a==0 and m==5:
                continue
            group=[]
            for deleted in combinations(ROWS,m):
                R=sorted(w for w in B if w%7 not in deleted)
                r=len(R)
                assert r>0
                c5=max(Counter(w%5 for w in R).values())
                c7=max(Counter(w%7 for w in R).values())
                E=max(F(r,9),F(c5,3),F(c7,2),F(1))
                remaining=5-a-m
                U=p*r+remaining*E
                assert U<r,(name,deleted,U,r)
                # Direct full-period checks of the fixed union proportion,
                # including the overlap when both small channels are selected.
                total=0
                fixed_hits=0
                for w in range(420):
                    if w%35 not in R:
                        continue
                    total+=1
                    hit=((name in ["246241","both"] and w%3==1)
                         or (name in ["487824887233","both"] and w%4==2))
                    fixed_hits+=hit
                assert F(fixed_hits,total)==p
                row={"selected_fixed":name,"fixed_count":a,
                     "fixed_union_proportion":str(p),"deleted_mod7_rows":deleted,
                     "residual_B":R,"residual_mass":r,"c5":c5,"c7":c7,
                     "generic_single_channel_mass":str(E),"remaining_generic_slots":remaining,
                     "total_union_upper_bound":str(U),"relative_upper_bound":str(U/r),
                     "absolute_uncovered_mass_lower_bound":str(r-U),
                     "fixed_union_check_period":420,"fixed_union_hit_count":fixed_hits,
                     "fixed_union_target_count":total}
                group.append(row)
                cases.append(row)
            summaries.append({"selected_fixed":name,"m":m,"case_count":len(group),
                              "maximum_relative_union_bound":str(max(F(x["relative_upper_bound"]) for x in group)),
                              "minimum_absolute_uncovered_mass":str(min(F(x["absolute_uncovered_mass_lower_bound"]) for x in group))})
    assert len(cases)==119
    # The only surviving no-h2 pattern covers all five complete mod-seven rows.
    assert all(any(w%7==c for c in ROWS) for w in range(35) if w%35 in B)
    output={"schema":"riesel-r4-five-tail-without-h2-residual-mass-table-v1",
            "status":"PASS_AUTHOR_EXACT_GEOMETRY_NOT_INDEPENDENT_REVIEW",
            "residual_B":sorted(B),"occupied_mod7_rows":ROWS,
            "all_order_generic_bound":"E=max(r/9,c5/3,c7/2,1) after h7 and selected h3/h4 are removed",
            "case_count":len(cases),"summary":summaries,"cases":cases,
            "only_unexcluded_pattern":{"selected_fixed":"none","h7_count":5,
                                        "h7_phases":ROWS,"remaining_residual_mass":0},
            "native_BRC_execution_claimed":False,"independent_project_review_claimed":False}
    target=Path(__file__).with_name("no_h2_mass_certificate.json")
    target.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":"PASS","certificate":str(target),"case_count":len(cases),
                      "table":summaries}))


if __name__=="__main__":
    main()
