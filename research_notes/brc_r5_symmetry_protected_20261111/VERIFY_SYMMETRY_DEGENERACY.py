#!/usr/bin/env python3
"""Exact finite certificate for the R5 K4+double-edge symmetry discriminant.

Frozen seven target ratio NUMERATORS (2,10,15,20,25,30,38); scaling by 20
changes neither transfer row nullspaces nor zero patterns. Standard library.
The counterfactual spectra illustrate a separate algebraic theorem; they do
not replace the frozen scientific pins.
"""
from itertools import combinations, permutations
from collections import Counter

SOURCES=(1,2,3,5)
FROZEN=(2,10,15,20,25,30,38)
AP=(1,2,3,4,5,6,7)
ASYMMETRIC=(1,2,4,8,13,21,32)


def flows(r, p):
    a,b,c,d,e,f,g=(r[i] for i in p)
    ua=(b-c)*(d-e)
    ub=(c-a)*(d-e)
    uc=(a-b)*(d-e)
    ud=-(b-c)*(e-a)
    ue=-(b-c)*(a-d)
    delta=g-f
    vf=-ub*(b-g)-ud*(d-g)
    vg=-ub*(f-b)-ud*(f-d)
    return (ua*delta,ub*delta,uc*delta,ud*delta,ue*delta,vf,vg)


def conserved(r,p,v):
    A,B,C,D,E,F,G=p
    ua,ub,uc,ud,ue,vf,vg=v
    rows=( ((A,ua),(B,ub),(C,uc)),
           ((A,-ua),(D,ud),(E,ue)),
           ((B,-ub),(D,-ud),(F,vf),(G,vg)),
           ((C,-uc),(E,-ue),(F,-vf),(G,-vg)) )
    return all(sum(t for _,t in row)==0 and
               sum(r[i]*t for i,t in row)==0 for row in rows)


def structurally_forced(r,p):
    m=r[3]
    A,B,C,D,E,F,G=p
    return (r[A]!=m and r[A]+r[F]+r[G]==3*m and
            ((r[F]==m and r[G]==2*m-r[A]) or
             (r[G]==m and r[F]==2*m-r[A])) and
            r[B]+r[E]==2*m and r[C]+r[D]==2*m)


def census(r):
    assert len(set(r))==7
    per_low=[]
    zero_location=Counter(); total=full=degen=forced=extra=0
    for low in combinations(SOURCES,2):
        per_total=per_full=per_degen=per_forced=per_extra=0
        for p in permutations(range(7)):
            if p[5]>p[6]: continue  # exchange of indistinguishable F/G edges
            v=flows(r,p)
            assert conserved(r,p,v), (r,p)
            assert all(v[:5]), (r,p)
            z=(v[5]==0 or v[6]==0)
            f=structurally_forced(r,p)
            if f: assert z,(r,p,v)
            assert not (v[5]==0 and v[6]==0),(r,p)
            per_total+=1
            per_full+=not z
            per_degen+=z
            per_forced+=f
            per_extra+=z and not f
            if z:
                zero_location[p[5] if v[5]==0 else p[6]]+=1
        per_low.append((low,per_total,per_full,per_degen,per_forced,per_extra))
        total+=per_total;full+=per_full;degen+=per_degen
        forced+=per_forced;extra+=per_extra
    return (total,full,degen,forced,extra,per_low,dict(sorted(zero_location.items())))


def main():
    for label,r in (("FROZEN",FROZEN),("ARITHMETIC_PROGRESSION",AP),
                    ("GENERIC_NONSYMMETRIC_EXAMPLE",ASYMMETRIC)):
        n,full,deg,forced,extra,by_low,where=census(r)
        print(label, "RATIO_NUMERATORS",r)
        for row in by_low: print("  LOW",*row)
        print("  TOTAL",n,"FULL",full,"DEGENERATE",deg,
              "SYMMETRY_FORCED",forced,"EXTRA",extra,"ZERO_LABELS",where)
        assert n==15120
        if label=="FROZEN":
            assert (full,deg,forced,extra)==(14832,288,288,0)
            assert where=={3:288}
            assert all(x[2:]==(2472,48,48,0) for x in by_low)
        elif label=="ARITHMETIC_PROGRESSION":
            assert (full,deg,forced,extra)==(14256,864,288,576)
        else:
            assert (full,deg,forced,extra)==(15120,0,0,0)
    assert flows(FROZEN,(0,1,2,3,4,5,6))==(200,-520,320,920,-720,250,150)
    assert flows(FROZEN,(0,1,2,4,5,3,6))==(450,-1170,720,2520,-2070,0,1350)
    print("PASS_EXACT_R5_SYMMETRY_PROTECTED_288_AND_DISCRIMINANT_STRATA")


if __name__=="__main__": main()
