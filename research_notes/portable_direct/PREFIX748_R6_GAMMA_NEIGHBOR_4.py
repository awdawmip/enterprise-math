#!/usr/bin/env python3
"""PREFIX-748-R6. Exact 8x8 closed Gamma cell certificates, frozen f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run in research_notes/portable_direct next to PREFIX741_R6_INNER_STRIP_194.py.
No arguments check two original cells in separate fresh Python processes.
"""
import sys
import subprocess
from fractions import Fraction

CELLS = ((11,51,-80983623,-21911219,7714155),
         (12,52,-82633603,-22525720,7614806))

def microfloor(x):
    a = x*1000000
    return a.numerator//a.denominator

def single(i,j):
    from PREFIX741_R6_INNER_STRIP_194 import (lower_cell,emu,eW,pair,tails)
    expected = next((r for r in CELLS if r[:2]==(i,j)), None)
    assert expected is not None
    floors = []
    for split in (2,4,8):
        g = lower_cell(i,j,split,emu,eW)
        floors.append(microfloor(g))
        if split<8:
            assert g<0
        pair.cache_clear()
        tails.cache_clear()
    assert tuple(floors)==expected[2:],(i,j,floors,expected)
    assert g>Fraction(7)
    print("PASS",i,j,tuple(floors),flush=True)

if __name__=="__main__":
    if len(sys.argv)==1:
        for i,j,*_ in CELLS:
            subprocess.run([sys.executable,__file__,f"{i},{j}"],check=True)
        upper={(i,j) for i,j,*_ in CELLS}
        allcells=upper|{(j,i) for i,j in upper}
        assert len(allcells)==4
        assert 141976+len(allcells)==141980
        print("ALL_CHECKS_PASS PREFIX748-R6 2+2=4",flush=True)
    elif len(sys.argv)==2:
        i,j=map(int,sys.argv[1].split(","))
        single(i,j)
    else:
        raise SystemExit("usage: checker.py [11,51 | 12,52]")
