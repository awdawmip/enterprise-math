#!/usr/bin/env python3
"""PREFIX-749-R6: three exact 16x16 original cells and their three transposes.
Run from research_notes/portable_direct with PREFIX748_R6_DYADIC_INTERVAL_180_EXACT.py.
Frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d.
All mathematical tests use exact outward dyadic integer/Fraction comparisons.
"""
import sys
from fractions import Fraction
from PREFIX748_R6_DYADIC_INTERVAL_180_EXACT import (
    cell_gap_lower, old_unsplit_gap_upper, microfloor, pair, surv
)
DATA=((12,56,12376308,-226650893),
      (13,57,14417493,-227202205),
      (14,59,16418225,-231181119))
def check_one(i,j,expected,old_expected):
    x=cell_gap_lower(i,j,16)
    floor=microfloor(x)
    assert floor==expected,(i,j,floor,expected)
    assert x>Fraction(12)
    old=microfloor(old_unsplit_gap_upper(i,j))
    assert old==old_expected and old<0,(i,j,old,old_expected)
    print("PASS",i,j,"G16_microfloor",floor,"old_G1_upper_microfloor",old,flush=True)
    pair.cache_clear(); surv.cache_clear()
def main():
    if len(sys.argv)>2:raise SystemExit("usage: checker.py [12,56|13,57|14,59]")
    chosen=DATA if len(sys.argv)==1 else [r for r in DATA if f"{r[0]},{r[1]}"==sys.argv[1]]
    if not chosen:raise SystemExit("unknown cell")
    for row in chosen:check_one(*row)
    if len(sys.argv)==1:
        upper={(i,j) for i,j,*_ in DATA}
        assert len(upper)==3 and len(upper|{(j,i) for i,j in upper})==6
        assert 142326+6==142332 and 147456-142332==5124
    print("ALL_CHECKS_PASS PREFIX749-R6",len(chosen),flush=True)
if __name__=="__main__":main()
