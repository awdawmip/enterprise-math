#!/usr/bin/env python3
"""PREFIX-743-R6 exact 30-cell Gamma comparison certificate.

Science pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Source dependency: PREFIX741_R6_INNER_STRIP_194.py from same directory.
Execute: python PREFIX743_R6_GAMMA_LEFT_EXTENSION_30.py
"""
from fractions import Fraction as F
from pathlib import Path
import json
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, oldmu, oldW, pair, tails

# [i, j, floor(1e6 * new exact lower), floor(1e6 * old exact lower)]
EXPECTED = [[14,40,44249754,-50971250],[15,40,49632601,-46031393],[16,40,55072219,-41073324],[14,41,31102949,-66260451],[15,41,36545914,-61222046],[16,41,42069797,-56139115],[14,42,18447719,-81066300],[15,42,23924235,-75957526],[16,42,29503816,-70779891],[14,43,6327117,-95340836],[15,43,11812152,-90188404],[16,43,17420361,-84944813],[15,44,249834,-103869726],[16,44,5861201,-98587394],[19,46,1965070,-107599732]]

def microfloor(v):
    x=v*1000000
    return x.numerator//x.denominator

def main():
    checked=[]
    for i,j,new_micro,old_micro in EXPECTED:
        new=lower_cell(i,j,2,emu,eW)
        old=lower_cell(i,j,1,oldmu,oldW)
        assert microfloor(new)==new_micro, (i,j,"new")
        assert microfloor(old)==old_micro, (i,j,"old")
        assert new>F(1,5) and old<=0, (i,j)
        checked.append([i,j,new_micro,old_micro])
        print("PASS",i,j,new_micro,old_micro,flush=True)
    reflected={(i,j) for i,j,_,_ in checked}|{(j,i) for i,j,_,_ in checked}
    assert len(checked)==15 and len(reflected)==30
    assert min(r[2] for r in checked)==249834
    assert all(14<=min(i,j)<=19 and max(i,j)<=46 for i,j in reflected)
    assert 141756+len(reflected)==141786
    out={"schema":"PREFIX743_R6_GAMMA_LEFT_EXTENSION_V1",
         "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
         "predecessor":"PREFIX-742",
         "witness":["0","73/500"],
         "domain":"all real q>=2; 15 closed cells and 15 coordinate transposes",
         "strict_gap":"V_q(e)-V_q(p,z)>q^2/5",
         "checked_upper_cells":checked,
         "new_reflected_cells":sorted([list(v) for v in reflected]),
         "new_reflected_count":30,
         "prior_author_union":141756,
         "new_author_union":141786,
         "total_grid_cells":147456,
         "remaining":5670,
         "grade":"AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"}
    Path(__file__).with_name("PREFIX743_R6_GAMMA_LEFT_EXTENSION_30_RESULTS.json").write_text(
        json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX743-R6 15+15=30")
if __name__=="__main__":
    main()
