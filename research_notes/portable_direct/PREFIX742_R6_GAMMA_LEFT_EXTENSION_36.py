#!/usr/bin/env python3
"""PREFIX-742-R6: exact 36-cell Gamma exclusion, based on frozen 189-row BRC kernel.
Science pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Run in research_notes/portable_direct: python PREFIX742_R6_GAMMA_LEFT_EXTENSION_36.py
Requires the published PREFIX741_R6_INNER_STRIP_194.py (same pinned kernel).
"""
from fractions import Fraction as F
from pathlib import Path
import json
from PREFIX741_R6_INNER_STRIP_194 import pair, tails, lower_cell, emu, eW

# Exact independent-run microfloors: row j, columns i=17,18,19.
EXPECTED = {
 40: (60540908, 66009435, 71447256),
 41: (47648822, 53255568, 58861163),
 42: (35162669, 40875269, 46614521),
 43: (23129965, 28917394, 34757418),
 44: (11594040, 17426771, 23336092),
 45: (593841, 6443978, 12392685),
}
OLD_EXPECTED = {
 40: (-36126720, -31222595, -26393026),
 41: (-51039437, -45952258, -40908053),
 42: (-65559205, -60322849, -55099571),
 43: (-79633855, -74280971, -68913085),
 44: (-93215419, -87777259, -82297935),
 45: (-106260360, -100766628, -95207569),
}

def microfloor(v):
    q = v * 1000000
    return q.numerator // q.denominator

def main():
    oldmu, oldm2 = pair(F(0), F(3,20))
    oldW = oldm2 - oldmu**2
    verified = []
    for j in range(40,46):
        for i in range(17,20):
            new = lower_cell(i,j,2,emu,eW)
            old = lower_cell(i,j,1,oldmu,oldW)
            x, y = microfloor(new), microfloor(old)
            assert x == EXPECTED[j][i-17], (i,j,x)
            assert y == OLD_EXPECTED[j][i-17], (i,j,y)
            assert new > F(1,2) and old < 0
            verified.append([i,j,x,y])
            print("PASS", i, j, x, y, flush=True)
        pair.cache_clear()
        tails.cache_clear()
    upper = {(i,j) for i,j,_,_ in verified}
    reflected = upper | {(j,i) for i,j in upper}
    assert len(upper)==18 and len(reflected)==36
    assert min(x[2] for x in verified)==593841
    assert all(min(i,j) in {17,18,19} and 40<=max(i,j)<=45
               for i,j in reflected)
    assert 141720+len(reflected)==141756
    out = {
      "schema": "PREFIX742_R6_EXACT_LEFT_EXTENSION_V1",
      "frozen_science_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
      "predecessor": "PREFIX-741",
      "witness": ["0","73/500"],
      "domain": "all real q>=2; 18 closed 384-grid cells and their 18 transposes",
      "strict_gap": "V_q(e)-V_q(p,z)>q^2/2",
      "checked_upper_cells": verified,
      "new_reflected_cells": sorted([list(v) for v in reflected]),
      "new_reflected_count": 36,
      "prior_author_union": 141720,
      "new_author_union": 141756,
      "total_grid_cells": 147456,
      "remaining": 5700,
      "grade": "AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"
    }
    Path(__file__).with_name("PREFIX742_R6_GAMMA_LEFT_EXTENSION_36_RESULTS.json").write_text(
        json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX742-R6 18+18=36")

if __name__=="__main__":
    main()
