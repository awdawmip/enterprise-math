#!/usr/bin/env python3
"""PREFIX-747-R6 exact 8x8 Gamma certificates; source f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run from research_notes/portable_direct; uses frozen integer kernel in PREFIX741_R6_INNER_STRIP_194.py.
With no args validates all 34 upper cells. Use two indices [start,end) for bounded replay.
"""
import sys
from fractions import Fraction
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, oldmu, oldW, pair, tails
CELLS = [[9,48,15911206],[10,49,13922282],[10,50,8455657],[11,50,12610669],[10,51,3704401],[11,51,7714155],[12,51,11955704],[11,52,3524919],[12,52,7614806],[15,52,21260726],[16,52,26263252],[17,52,31487037],[18,52,36926528],[19,52,42574625],[20,52,48422620],[21,52,54460143],[11,53,36384],[12,53,3971215],[13,53,8132839],[15,53,17138481],[16,53,21980739],[17,53,27046066],[18,53,32330365],[19,53,37828087],[20,53,43532154],[12,54,1016623],[13,54,5016999],[14,54,9241943],[15,54,13692179],[16,54,18367373],[17,54,23266037],[18,54,28385420],[19,54,33721422],[20,54,39268500]]

def microfloor(x):
    y = x * 1000000
    return y.numerator // y.denominator

def main():
    if len(sys.argv) == 1: start,end = 0,len(CELLS)
    elif len(sys.argv) == 3: start,end = map(int,sys.argv[1:])
    else: raise SystemExit("usage: PREFIX747_R6_GAMMA_68_EXACT.py [start_index end_index]")
    assert 0 <= start < end <= len(CELLS)
    for i,j,expected in CELLS[start:end]:
        bound = lower_cell(i,j,8,emu,eW)
        assert microfloor(bound) == expected, (i,j,expected,microfloor(bound))
        assert bound > Fraction(1,30), (i,j,"positive certificate")
        old = lower_cell(i,j,1,oldmu,oldW)
        assert old < 0, (i,j,"old witness overlap")
        print("PASS",i,j,"G8_microfloor",expected,"old_microfloor",microfloor(old),flush=True)
        pair.cache_clear();tails.cache_clear()
    if start == 0 and end == len(CELLS):
        pairs={(i,j) for i,j,_ in CELLS}
        both=pairs|{(j,i) for i,j in pairs}
        assert len(pairs)==34 and len(both)==68
        assert all(i<j and 9<=i<=21 and 48<=j<=54 for i,j in pairs)
        assert min(x[2] for x in CELLS)==36384
        assert 141972+len(both)==142040
    print("ALL_CHECKS_PASS PREFIX747",end-start,flush=True)

if __name__=="__main__":main()
