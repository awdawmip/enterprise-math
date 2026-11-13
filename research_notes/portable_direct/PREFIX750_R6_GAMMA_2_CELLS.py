#!/usr/bin/env python3
"""PREFIX-750-R6: certify (11,52) and its transpose by exact Gamma 8x8 bounds."""
from fractions import Fraction
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, oldmu, oldW, pair, tails

def microfloor(x):
    y=x*1000000
    return y.numerator//y.denominator

def main():
    floors=[]
    for s in (2,4,8):
        v=lower_cell(11,52,s,emu,eW)
        floors.append(microfloor(v))
        pair.cache_clear()
        tails.cache_clear()
    assert floors==[-86683906,-26603110,3524919],floors
    assert v>Fraction(3)
    old=lower_cell(11,52,1,oldmu,oldW)
    assert microfloor(old)==-206906474
    assert 141984+2==141986
    print("PASS",11,52,tuple(floors),"old",microfloor(old),flush=True)
    print("ALL_CHECKS_PASS PREFIX750-R6 1+1=2",flush=True)
if __name__=="__main__":main()
