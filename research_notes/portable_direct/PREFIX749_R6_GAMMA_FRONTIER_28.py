#!/usr/bin/env python3
"""PREFIX-749-R6: 14 new closed Gamma cells, plus transposes.

Run beside PREFIX741_R6_INNER_STRIP_194.py, optionally with 'i,j' to
check a single original cell. Standard-library exact fractions only.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
import subprocess
import sys

# (i,j, floor(10**6 G_2), floor(10**6 G_4), floor(10**6 G_8),
#  floor(10**6 G_1 for the old e=(0,3/20))).
ROWS = (
 (7,47,-67306677,-12668452,14749094,-176559258),
 (7,48,-75490081,-19738993,8233883,-186976616),
 (8,48,-71824562,-16036330,11954081,-183393977),
 (8,49,-79372852,-22496035,6037447,-193128641),
 (8,50,-86167146,-28221013,845704,-202072414),
 (9,49,-75599055,-18687609,9862147,-189432721),
 (9,50,-82520043,-24545578,4534353,-198489866),
 (10,50,-78645845,-20639281,8455657,-194688514),
 (10,51,-84950051,-25907227,3704401,-203076218),
 (11,52,-86683906,-26603110,3524919,-206906474),
 (11,53,-91649342,-30582793,36384,-213856733),
 (12,53,-87744789,-26657420,3971215,-210001739),
 (12,54,-92131325,-30088112,1016623,-216314021),
 (13,53,-83619058,-22507063,8132839,-205933937),
)

def floor_micro(q):
    x=10**6*q
    return x.numerator//x.denominator

def check_one(i,j):
    from PREFIX741_R6_INNER_STRIP_194 import lower_cell,emu,eW,oldmu,oldW,pair,tails
    row=next((r for r in ROWS if r[:2]==(i,j)),None)
    assert row is not None,(i,j)
    out=tuple(floor_micro(lower_cell(i,j,s,emu,eW)) for s in (2,4,8))
    old=floor_micro(lower_cell(i,j,1,oldmu,oldW))
    assert out==tuple(row[2:5]) and old==row[5],(i,j,out,old,row)
    assert out[2]>=36384 and out[2]>1000000//30
    assert old<=0
    print("PASS",i,j,out,old,flush=True)
    pair.cache_clear();tails.cache_clear()

if __name__=="__main__":
    if len(sys.argv)==1:
        for i,j,*_ in ROWS:
            subprocess.run([sys.executable,__file__,f"{i},{j}"],check=True)
        upper={(i,j) for i,j,*_ in ROWS}
        both=upper|{(j,i) for i,j in upper}
        assert len(upper)==14 and len(both)==28
        assert min(r[4] for r in ROWS)==36384
        assert 141980+len(both)==142008
        print("ALL_CHECKS_PASS PREFIX749-R6 14+14=28",flush=True)
    elif len(sys.argv)==2:
        check_one(*map(int,sys.argv[1].split(",")))
    else:
        raise SystemExit("usage: checker.py [i,j]")
