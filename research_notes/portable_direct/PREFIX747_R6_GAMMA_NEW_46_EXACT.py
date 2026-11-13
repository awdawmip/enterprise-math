#!/usr/bin/env python3
"""PREFIX-747-R6 exact 8x8 Gamma bound verification (23 originals + 23 mirrors).

Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Requires sibling PREFIX741_R6_INNER_STRIP_194.py with its published regression checks.
Usage: python PREFIX747_R6_GAMMA_NEW_46_EXACT.py [first_j last_j_exclusive]
Default checks j=45..52. Python standard library exact Fraction only.
"""
import sys
from fractions import Fraction as F
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, oldmu, oldW, pair, tails

EXPECTED=[[7,45,29948255,-153399057],[7,46,21989561,-165361995],[8,46,25957289,-161583445],[7,47,14749094,-176559258],[8,47,18595376,-172875253],[9,47,22680239,-168971108],[7,48,8233883,-186976616],[8,48,11954081,-183393977],[9,48,15911206,-179590475],[10,48,20105480,-175568312],[8,49,6037447,-193128641],[9,49,9862147,-189432721],[10,49,13922282,-185517458],[11,49,18217896,-181385295],[10,50,8455657,-194688514],[11,50,12610669,-190669616],[12,50,16999301,-186435764],[12,51,11955704,-195063463],[13,51,16428868,-190736413],[14,51,21132267,-186200483],[13,52,11934432,-198718120],[14,52,16483549,-194306447],[15,52,21260726,-189687999]]
def floor_micro(x):
    y=x*1000000
    return y.numerator//y.denominator

def main():
    if len(sys.argv)==1:
        a,b=45,53
    elif len(sys.argv)==3:
        a,b=map(int,sys.argv[1:])
    else:
        raise SystemExit("usage: checker.py [first_j last_j_exclusive]")
    assert 45<=a<b<=53
    checked=[]
    for i,j,new_floor,old_floor in EXPECTED:
        if not a<=j<b:
            continue
        new=lower_cell(i,j,8,emu,eW)
        old=lower_cell(i,j,1,oldmu,oldW)
        assert floor_micro(new)==new_floor,(i,j,"new")
        assert floor_micro(old)==old_floor,(i,j,"PREFIX712 original comparator")
        assert new>F(6),(i,j,"uniform strict bound")
        assert old<0,(i,j,"previous sufficient predicate")
        checked.append((i,j,new_floor))
        print("PASS",i,j,new_floor,old_floor,flush=True)
        pair.cache_clear(); tails.cache_clear()
    assert len(checked)==sum(a<=row[1]<b for row in EXPECTED)
    if (a,b)==(45,53):
        assert len(checked)==23
        originals={(i,j) for i,j,_ in checked}
        assert len(originals)==23
        assert all(i<j for i,j in originals)
        both=originals|{(j,i) for i,j in originals}
        assert len(both)==46
        assert min(k for _,_,k in checked)==6037447
        assert 142056+len(both)==142102
    print("ALL_CHECKS_PASS PREFIX747-R6",len(checked),"original cells",flush=True)
if __name__=="__main__":
    main()
