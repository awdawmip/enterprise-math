#!/usr/bin/env python3
"""EC49V portable proof spot checks + exact cost-face certificate, stdlib only.
For exhaustive all-real envelope interval arithmetic see PROOF.md and evidence archive.
"""
from fractions import Fraction as F
from itertools import product
from EC49U_VERIFY import HIST, OBS, Z, OPTIONS, exact_support, delta, u_kernel, atom

def pref_J(p,eta):
    # J=alpha-beta-(C1-C2)/6. After buying A/B, S always dominates no S.
    s=F(0)
    for code in OPTIONS[1:]:
        fiber=[w for w in HIST if p[w]==code]
        if not fiber:continue
        b=sum(max(F(0),sum(delta(w,u,z,eta) for w in fiber))
              for u in OBS for z in Z)
        extra=F((1 if code[0]=='A' else 2)-1,6)*F(len(fiber),3)
        s+=b-extra
    return s

def deterministic_triplet(p,eta):
    c1=c2=d=F(0)
    for code in OPTIONS[1:]:
        fiber=[w for w in HIST if p[w]==code]
        if not fiber:continue
        c1+=F(len(fiber)*(1 if code[0]=='A' else 2),3)
        c2+=F(len(fiber),3)
        d+=sum(max(F(0),sum(delta(w,u,z,eta) for w in fiber))
               for u in OBS for z in Z)
    return c1,c2,d

def behavioral_witness(eta):
    choice={0:{('A',0):F(1)},1:{('A',1):F(1)},
            2:{None:F(3,8),('A',0):F(9,16),('B',0):F(1,16)}}
    masks={('A',0):{0,2},('A',1):{1},('B',0):{2}}
    c1=c2=a=b=F(0)
    for w in HIST:
        assert sum(choice[w].values())==1
        for code,prob in choice[w].items():
            if code is None:continue
            c1+=F(1,3)*prob*(1 if code[0]=='A' else 2)
            c2+=F(1,3)*prob
            for u in OBS:
                for z in masks[code]:
                    a+=prob*atom('P',w,u,z,eta)
                    b+=prob*atom('Q',w,u,z,eta)
    return c1,c2,a,b

def main():
    # Finite evaluations check hard points; the seven-fiber proof is all-real.
    for eta in [F(0),F(1,200),F(1,6),F(7,18),F(5,12),F(499,1000)]:
        predicted=max(F(1,27),eta/6-F(1,36))
        assert exact_support(eta)[0]==predicted,(eta,predicted)
    all_prefixes=list(product(OPTIONS,repeat=3))
    assert len(all_prefixes)==125
    for eta in [F(0),F(1,200),F(1,6)]:
        assert max(pref_J(p,eta) for p in all_prefixes)==F(1,9)
    eta=F(1,200)
    terms=[((None,('A',0),('A',1)),F(3,8)),
           ((('A',0),('A',0),('A',1)),F(9,16)),
           ((('A',0),('A',1),('B',0)),F(1,16))]
    mixed=tuple(sum(w*deterministic_triplet(p,eta)[i] for p,w in terms) for i in range(3))
    assert mixed==(F(43,48),F(7,8),F(11,96))
    c1,c2,a,b=behavioral_witness(eta)
    assert (c1,c2,a,b)==(F(43,48),F(7,8),F(109,192),F(67,144))
    assert a-b==F(59,576)
    assert F(7,48)-F(11,96)==F(1,32)
    print('PASS EC49V; H=max(1/27,eta/6-1/36), switch 7/18;')
    print('PASS J<=1/9 for eta<=1/6; cost-face delta in [59/576,11/96];')
    print('PASS convex-hull upper sharp, behavioral lower exactly attained; no formal admission')
if __name__=='__main__':main()
