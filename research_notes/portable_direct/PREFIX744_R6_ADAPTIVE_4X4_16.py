#!/usr/bin/env python3
"""PREFIX-744-R6: exact 4x4 adaptive Gamma bounds for 16 closed 384-grid cells.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Run alongside PREFIX741_R6_INNER_STRIP_194.py with Python 3 standard library.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, oldmu, oldW

EXPECTED=[[13,44,41218899,-114080286],[14,44,46656522,-109040668],[14,45,36791209,-122127135],[15,45,42349288,-116961187],[16,45,48077835,-111665694],[17,46,44552341,-118729709],[18,46,50543385,-113208439],[19,47,47771633,-119436584]]
def mf(x):
    y=x*1000000
    return y.numerator//y.denominator

def main():
    checked=[]
    for i,j,new_micro,old_micro in EXPECTED:
        new=lower_cell(i,j,4,emu,eW)
        old=lower_cell(i,j,1,oldmu,oldW)
        assert mf(new)==new_micro, (i,j,new_micro)
        assert mf(old)==old_micro, (i,j,old_micro)
        assert new>36 and old<=0
        checked.append([i,j,new_micro,old_micro])
        print("PASS",i,j,new_micro,old_micro,flush=True)
    fresh={(i,j) for i,j,_,_ in checked}
    both=fresh | {(j,i) for i,j in fresh}
    assert len(fresh)==8 and len(both)==16
    assert min(r[2] for r in checked)==36791209
    assert 141786+len(both)==141802
    result={"schema":"PREFIX744_R6_GAMMA_ADAPTIVE_4X4_V1",
         "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
         "predecessor":"PREFIX-743",
         "witness":["0","73/500"],
         "domain":"all real q>=2, eight closed 384-grid cells and their eight transposes",
         "strict_gap":"V_q(e)-V_q(p,z)>36*q^2",
         "checked_upper_cells":checked,
         "new_reflected_cells":sorted([list(v) for v in both]),
         "new_reflected_count":16,
         "prior_author_union":141786,
         "new_author_union":141802,
         "total_grid_cells":147456,
         "remaining":5654,
         "grade":"AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"}
    Path(__file__).with_name("PREFIX744_R6_ADAPTIVE_4X4_16_RESULTS.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX744-R6 8+8=16")
if __name__=="__main__": main()
