#!/usr/bin/env python3
"""PREFIX-746 exact Gamma 8x8 certificate, frozen f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run from research_notes/portable_direct; requires PREFIX741_R6_INNER_STRIP_194.py.
Optional two arguments: first_j last_j_exclusive, e.g. 47 49.
"""
import sys
from fractions import Fraction
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, oldmu, oldW, pair, tails
CELLS = [[9,47,22680239,-168971108],[10,47,27002790,-164850312],[10,48,20105480,-175568312],[11,48,24535826,-171331230],[11,49,18217896,-181385295],[12,49,22747775,-177040130],[13,49,27509360,-172487371],[12,50,16999301,-186435764],[13,50,21620243,-181990942],[14,50,26470862,-177340583],[13,51,16428868,-190736413],[14,51,21132267,-186200483],[15,51,26063219,-181461078],[13,52,11934432,-198718120],[14,52,16483549,-194306447]]

def floor_micro(x):
    y=x*1000000
    return y.numerator//y.denominator

def main():
    if len(sys.argv)==1: start,end=47,53
    elif len(sys.argv)==3: start,end=map(int,sys.argv[1:])
    else: raise SystemExit("usage: script.py [first_j last_j_exclusive]")
    assert 47<=start<end<=53
    seen=[]
    for i,j,expected,old_expected in CELLS:
        if not(start<=j<end): continue
        a=lower_cell(i,j,8,emu,eW)
        b=lower_cell(i,j,1,oldmu,oldW)
        assert floor_micro(a)==expected,(i,j,"8x8",floor_micro(a))
        assert floor_micro(b)==old_expected,(i,j,"old",floor_micro(b))
        assert a>Fraction(11)
        assert b<0
        seen.append((i,j))
        print("PASS",i,j,expected,old_expected,flush=True)
        pair.cache_clear();tails.cache_clear()
    assert len(seen)==sum(start<=j<end for i,j,*_ in CELLS)
    if (start,end)==(47,53):
        assert len(seen)==15 and len(set(seen))==15
        both=set(seen)|{(j,i) for i,j in seen}
        assert len(both)==30 and min(c[2] for c in CELLS)==11934432
        assert 141942+len(both)==141972
    print("ALL_CHECKS_PASS PREFIX746",len(seen),flush=True)

if __name__=="__main__": main()
