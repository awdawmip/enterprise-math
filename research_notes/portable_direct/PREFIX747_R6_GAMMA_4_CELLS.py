#!/usr/bin/env python3
"""PREFIX-747-R6 exact Gamma 8x8 certificates, frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run in research_notes/portable_direct with PREFIX741_R6_INNER_STRIP_194.py present.
Usage: python PREFIX747_R6_GAMMA_4_CELLS.py [11,50 | 12,51]
No argument runs both original cells in separate fresh Python processes, avoiding
large exact-arithmetic cache retention. All comparisons use fractions.Fraction.
"""
import sys
import subprocess
from fractions import Fraction
CELLS = ((11,50, -74544460,-16501384,12610669),
         (12,51, -76791948,-17685531,11955704))
def microfloor(x):
    t=x*1000000
    return t.numerator//t.denominator
def single(i,j):
    from PREFIX741_R6_INNER_STRIP_194 import (lower_cell, emu,eW,pair,tails)
    expected=next((r for r in CELLS if r[:2]==(i,j)),None)
    assert expected is not None
    row=[]
    for s in (2,4,8):
        g=lower_cell(i,j,s,emu,eW)
        row.append(microfloor(g))
        if s<8:
            assert g<0
        pair.cache_clear();tails.cache_clear()
    assert tuple(row)==expected[2:],(i,j,row,expected)
    assert g>Fraction(11)
    print("PASS",i,j,tuple(row),flush=True)
if __name__=="__main__":
    if len(sys.argv)==1:
        for i,j,*_ in CELLS:
            subprocess.run([sys.executable,__file__,f"{i},{j}"],check=True)
        assert len({(i,j) for i,j,*_ in CELLS}|{(j,i) for i,j,*_ in CELLS})==4
        assert 141972+4==141976
        print("ALL_CHECKS_PASS PREFIX747-R6 2+2=4",flush=True)
    elif len(sys.argv)==2:
        i,j=map(int,sys.argv[1].split(","))
        single(i,j)
    else:raise SystemExit("usage: checker.py [11,50 | 12,51]")
