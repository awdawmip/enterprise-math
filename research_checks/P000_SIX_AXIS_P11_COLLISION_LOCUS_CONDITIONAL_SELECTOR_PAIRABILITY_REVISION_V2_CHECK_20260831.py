#!/usr/bin/env python3
"""V2: filter the retained P11 collision/resolvent candidates by exact pairability."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import isqrt
from pathlib import Path
import runpy

G = runpy.run_path(Path(__file__).with_name(
    "P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_CHECK_20260831.py"))
PERMS, C1, C2 = G["PERMS"], G["C1_PAIR"], G["C2_PAIR"]
moment, classes = G["moment"], G["collision_classes"]
q21, q12 = G["q21_coeffs"], G["q12_coeffs"]
class_pair, rootbox = G["class_pair"], G["class_witnesses_at_B"]
distinct_matchings = G["distinct_matchings"]


def pairable(h,t):
    d=h*h-4*t
    if d<0: return False
    s=isqrt(d)
    return s*s==d and (s-h)%2==0


def adm(H,T,p): return all(pairable(H[i],T[p[i]]) for i in range(3))

def fibres(H,T):
    F=defaultdict(list)
    for p,K in distinct_matchings(H,T):
        if adm(H,T,p): F[moment(H,T,p,1,1)].append((p,K))
    return F

def count(H,T,c): return sum(adm(H,T,p) for p in class_pair(c))


def solve3(M,b):
    A=[[Fraction(M[i][j]) for j in range(3)]+[Fraction(b[i])] for i in range(3)]
    for c in range(3):
        r=next(r for r in range(c,3) if A[r][c])
        A[c],A[r]=A[r],A[c]
        q=A[c][c]; A[c]=[x/q for x in A[c]]
        for r in range(3):
            if r!=c and A[r][c]:
                q=A[r][c]; A[r]=[A[r][j]-q*A[c][j] for j in range(4)]
    return tuple(A[i][3] for i in range(3))

def recT(H,T,p11,p21): return solve3([[1,1,1],list(H),[h*h for h in H]],[sum(T),p11,p21])
def recH(H,T,p11,p12): return solve3([[1,1,1],list(T),[t*t for t in T]],[sum(H),p11,p12])


def main():
    V=range(-4,5); valid=levels=repeated=mx=0; hist={0:0,1:0,2:0}
    for H in combinations_with_replacement(V,3):
      for T in combinations_with_replacement(V,3):
        F=fibres(H,T)
        if not F: continue
        valid+=1; m=max(map(len,F.values())); mx=max(mx,m); assert m<=2
        if len(set(H))<3 or len(set(T))<3: repeated+=1; assert m==1
        for c in classes(H,T):
            l,r=class_pair(c); z=moment(H,T,l,1,1); assert z==moment(H,T,r,1,1)
            n=count(H,T,c); hist[n]+=1; levels+=1; assert len(F.get(z,[]))==n
    assert hist[0] and hist[1]

    R=Q=0; W=range(-3,4)
    for H in combinations(W,3):
      for T in combinations(W,3):
       for c in classes(H,T):
        l,r=class_pair(c); p11=moment(H,T,l,1,1); assert p11==moment(H,T,r,1,1)
        xs=sorted(moment(H,T,p,2,1) for p in (l,r)); a,b,d,_=q21(H,T,p11)
        assert xs[0]!=xs[1] and b==-a*sum(xs) and d==a*xs[0]*xs[1]
        for p in (l,r):
            x=moment(H,T,p,2,1); assert a*x*x+b*x+d==0
            u=recT(H,T,p11,x); assert u==tuple(Fraction(T[p[i]]) for i in range(3))
            assert all(pairable(H[i],int(u[i])) for i in range(3))==adm(H,T,p); Q+=1
        R+=1
        ys=sorted(moment(H,T,p,1,2) for p in (l,r)); a,b,d,_=q12(H,T,p11)
        assert ys[0]!=ys[1] and b==-a*sum(ys) and d==a*ys[0]*ys[1]
        for p in (l,r):
            y=moment(H,T,p,1,2); assert a*y*y+b*y+d==0
            u=recH(H,T,p11,y); inv=[0]*3
            for i,j in enumerate(p): inv[j]=i
            assert u==tuple(Fraction(H[inv[j]]) for j in range(3))
            assert all(pairable(int(u[j]),T[j]) for j in range(3))==adm(H,T,p); Q+=1
        R+=1

    # Mandatory Driver falsifier: both algebraic doubles are admissible singletons.
    H=(-2,0,2); T=(-1,0,1); assert classes(H,T)=={"C1","C2"}
    assert count(H,T,"C1")==count(H,T,"C2")==1
    assert adm(H,T,(1,0,2)) and not adm(H,T,(0,2,1))
    assert adm(H,T,(2,0,1)) and not adm(H,T,(1,2,0))

    # Simultaneous algebraic doubles can filter to different cardinalities.
    H=T=(-2,-1,0); assert classes(H,T)=={"C1","C2"} and (count(H,T,"C1"),count(H,T,"C2"))==(0,1)
    H=(1,4,7); T=(-60,-30,0); assert classes(H,T)=={"C1","C2"}
    assert (count(H,T,"C1"),count(H,T,"C2"))==(1,2)
    assert len(fibres(H,T)[-270])==1 and len(fibres(H,T)[-450])==2

    # Retained SAME/OPPOSITE P21/P12 root ordering.
    B=0
    for A in range(1,9):
     for E in range(1,9):
      for C in range(1,9):
       for D in range(1,9):
        H=(0,A,A+E); T=(0,C,C+D)
        if A*C==E*D:
            l,r=C1; assert moment(H,T,l,2,1)<moment(H,T,r,2,1) and moment(H,T,l,1,2)<moment(H,T,r,1,2); B+=1
        if A*D==E*C:
            l,r=C2; assert moment(H,T,l,2,1)<moment(H,T,r,2,1) and moment(H,T,l,1,2)>moment(H,T,r,1,2); B+=1
    assert B==320

    # Retain B=6 minimal genuine two-admissible witnesses and scaling.
    ns={"C1":[],"C2":[]}; roots={}
    for box in range(1,7):
      for c in ("C1","C2"):
        W,_=rootbox(box,c); ns[c].append(len(W))
        if box<6: assert not W
        else: assert len(W)==1; roots[c]=W[0]
    assert ns=={"C1":[0,0,0,0,0,1],"C2":[0,0,0,0,0,1]}
    assert roots=={"C1":((-1,1,4),(-30,-12,0)),"C2":((-4,-1,1),(-30,-12,0))}
    S=0
    for c,(H0,T0) in roots.items():
      for m in range(1,13):
        H=tuple(m*h for h in H0); T=tuple(m*m*t for t in T0)
        assert c in classes(H,T) and count(H,T,c)==2; S+=1

    total=valid+levels+R+Q+B+S
    print("PASS P000_P11_PAIRABILITY_FILTERED_REVISION_V2 "
          f"checks={total} valid_inputs={valid} filtered_levels={levels} "
          f"class_hist=0:{hist[0]},1:{hist[1]},2:{hist[2]} resolvent={R} reconstruction={Q} "
          f"branch={B} scale={S} repeated_valid={repeated} control_max={mx} "
          "rootbox=C1:0,0,0,0,0,1|C2:0,0,0,0,0,1 "
          "adm_fibre_max=2 selector_bits=log2|F_adm|=0_or_1 simultaneous_levels=cardinality_can_differ")

if __name__=="__main__": main()
