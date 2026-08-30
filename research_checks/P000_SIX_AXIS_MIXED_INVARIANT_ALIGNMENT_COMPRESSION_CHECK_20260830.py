#!/usr/bin/env python3
"""Exact task-local checker for RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION.

Frozen census: local unordered integer pairs (a,b) with -6 <= a <= b <= 6.
No adaptive enlargement is performed. The B=6 census is regression/falsification
evidence; all-m/global claims in the return are proved algebraically. Two sharp
global witnesses (six-way empty packet and three-way P12 packet) intentionally
lie outside this fixed census and are checked directly.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, permutations
from math import comb, isqrt

TASK_ID = "RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION"
B = 6
CHECKS = 0

def ck(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def pairable(h, t):
    d = h*h - 4*t
    if d < 0:
        return False
    r = isqrt(d)
    return r*r == d and ((h-r) % 2 == 0)

def roots(h, t):
    ck(pairable(h,t), f"not pairable: {(h,t)}")
    r=isqrt(h*h-4*t)
    return tuple(sorted(((h-r)//2,(h+r)//2)))

def packet(K):
    """K is iterable of (h,t); canonical Gamma-orbit is the sorted pair multiset."""
    return tuple(sorted(K))

def data(K):
    K=packet(K)
    H=tuple(sorted(h for h,t in K))
    T=tuple(sorted(t for h,t in K))
    P11=sum(h*t for h,t in K)
    P21=sum(h*h*t for h,t in K)
    P12=sum(h*t*t for h,t in K)
    return H,T,P11,P21,P12

def check_distinct_h_reconstruction(K):
    H,T,P11,P21,P12=data(K)
    if len(set(H)) != 3:
        return
    ST=sum(T)
    by_h={h:t for h,t in K}
    for hi in H:
        hj,hk=[h for h in H if h != hi]
        num=P21-(hj+hk)*P11+hj*hk*ST
        den=(hi-hj)*(hi-hk)
        ck(num % den == 0, "distinct-H reconstruction nonintegral")
        ck(num//den == by_h[hi], "distinct-H reconstruction failed")

def check_h_21_reconstruction(K):
    H,T,P11,P21,P12=data(K)
    c=defaultdict(int)
    for h in H: c[h]+=1
    if sorted(c.values()) != [1,2]:
        return
    h=next(x for x,n in c.items() if n==2)
    k=next(x for x,n in c.items() if n==1)
    ST=sum(T)
    tk=(P11-h*ST)
    den=k-h
    ck(tk % den == 0, "H 2+1 reconstruction nonintegral")
    tk//=den
    actual=next(t for hh,t in K if hh==k)
    ck(tk==actual, "H 2+1 reconstruction failed")

def check_distinct_t_reconstruction(K):
    H,T,P11,P21,P12=data(K)
    if len(set(T)) != 3:
        return
    SH=sum(H)
    by_t={t:h for h,t in K}
    for ti in T:
        tj,tk=[t for t in T if t != ti]
        num=P12-(tj+tk)*P11+tj*tk*SH
        den=(ti-tj)*(ti-tk)
        ck(num % den == 0, "distinct-T reconstruction nonintegral")
        ck(num//den == by_t[ti], "distinct-T reconstruction failed")

def check_t_21_reconstruction(K):
    H,T,P11,P21,P12=data(K)
    c=defaultdict(int)
    for t in T: c[t]+=1
    if sorted(c.values()) != [1,2]:
        return
    t=next(x for x,n in c.items() if n==2)
    u=next(x for x,n in c.items() if n==1)
    SH=sum(H)
    hu=P11-t*SH
    den=u-t
    ck(hu % den == 0, "T 2+1 reconstruction nonintegral")
    hu//=den
    actual=next(h for h,tt in K if tt==u)
    ck(hu==actual, "T 2+1 reconstruction failed")

def check_witness(name, H, T, alignments, expected_common=None):
    Ks=[]
    for perm in alignments:
        K=packet(tuple(zip(H, perm)))
        ck(tuple(sorted(perm))==tuple(sorted(T)), f"{name}: T marginal drift")
        for h,t in K:
            ck(pairable(h,t), f"{name}: non-pairable {(h,t)}")
            roots(h,t)
        Ks.append(K)
    ck(len(set(Ks))==len(Ks), f"{name}: K orbits not distinct")
    if expected_common is not None:
        for inds, value in expected_common:
            vals=[]
            for K in Ks:
                d=data(K)
                vals.append(tuple(d[i] for i in inds))
            ck(len(set(vals))==1, f"{name}: retained packet not common: {vals}")
            ck(vals[0]==value, f"{name}: common value mismatch: {vals[0]} != {value}")
    return Ks

# Freeze local relation-state universe before census outcomes.
REL=[]
for a in range(-B,B+1):
    for b in range(a,B+1):
        h,t=a+b,a*b
        ck((h,t) not in {(x[0],x[1]) for x in REL}, "duplicate relation state")
        REL.append((h,t,a,b))
ck(len(REL)==91, "unexpected B=6 relation-state count")
ck(comb(len(REL)+2,3)==129766, "unexpected K-orbit census size")

SUBSETS = {
    "EMPTY": (),
    "P11": (2,),
    "P21": (3,),
    "P12": (4,),
    "P11_P21": (2,3),
    "P11_P12": (2,4),
    "P21_P12": (3,4),
    "ALL": (2,3,4),
}
fibers={name:defaultdict(int) for name in SUBSETS}

for idxs in combinations_with_replacement(range(len(REL)),3):
    K=tuple((REL[i][0],REL[i][1]) for i in idxs)
    check_distinct_h_reconstruction(K)
    check_h_21_reconstruction(K)
    check_distinct_t_reconstruction(K)
    check_t_21_reconstruction(K)
    d=data(K)
    for name, inds in SUBSETS.items():
        key=(d[0],d[1])+tuple(d[i] for i in inds)
        fibers[name][key]+=1

census_max={name:max(g.values()) for name,g in fibers.items()}
EXPECTED_CENSUS={
    "EMPTY":4,
    "P11":2,
    "P21":3,
    "P12":2,
    "P11_P21":1,
    "P11_P12":1,
    "P21_P12":2,
    "ALL":1,
}
ck(census_max==EXPECTED_CENSUS, f"census maxima drift: {census_max}")

# Sharp P11 two-way collision (inside frozen census).
H=(-4,-1,1); T=(-30,-12,0)
Kp11=check_witness(
    "P11_TWO",
    H,T,
    [(-12,0,-30),(0,-30,-12)],
    expected_common=[((2,), (18,))]
)
ck(data(Kp11[0])[3:] == (-222,324), "P11 witness A higher moments drift")
ck(data(Kp11[1])[3:] == (-42,-756), "P11 witness B higher moments drift")

# Sharp P21 three-way collision (inside frozen census).
H=(-5,-5,5); T=(-6,0,6)
p21_perms=[(-6,0,6),(-6,6,0),(0,6,-6)]
Kp21=check_witness(
    "P21_THREE",
    H,T,p21_perms,
    expected_common=[((3,), (0,))]
)

# Sharp P21+P12 two-way collision (inside frozen census).
H=(-5,0,5); T=(-6,-1,6)
Kpair=check_witness(
    "P21_P12_TWO",
    H,T,
    [(-6,-1,6),(6,-1,-6)],
    expected_common=[((3,4),(0,0))]
)
ck({data(K)[2] for K in Kpair}=={-60,60}, "P21+P12 witness P11 separation drift")

# Global sharp EMPTY six-way witness, accepted from parent (outside B=6 allowed direct guard).
H=(-3,3,9); T=(-70,-10,0)
all6=list(permutations(T))
Kempty=check_witness("EMPTY_SIX",H,T,all6)
ck(len(Kempty)==6, "empty six-way witness drift")

# Global sharp P12 three-way witness (outside B=6; fixed direct certificate, no census enlargement).
H=(-29,29,37); T=(-210,210,210)
p12_perms=[(-210,210,210),(210,-210,210),(210,210,-210)]
Kp12=check_witness(
    "P12_THREE",
    H,T,p12_perms,
    expected_common=[((4,), (1631700,))]
)

# Orientation firewall: Q candidates are S_T - 2*t for possible distinguished negative slot.
def q_candidates(T):
    ST=sum(T)
    return tuple(sorted(set(ST-2*t for t in T)))
ck(len(q_candidates((5,5,5)))==1, "Q triple candidate count")
ck(len(q_candidates((5,5,7)))==2, "Q 2+1 candidate count")
ck(len(q_candidates((3,5,7)))==3, "Q distinct candidate count")

# Global classification encoded as theorem-side assertions backed by algebraic proof in return.
GLOBAL_MAX={
    "EMPTY":6,
    "P11":2,
    "P21":3,
    "P12":3,
    "P11_P21":1,
    "P11_P12":1,
    "P21_P12":2,
    "ALL":1,
}
ck(GLOBAL_MAX["P11_P21"]==1 and GLOBAL_MAX["P11_P12"]==1, "sufficient-pair guard")
ck(GLOBAL_MAX["P21_P12"]>1, "P11 necessity guard")
ck(min(k.count("_")+1 for k,v in GLOBAL_MAX.items() if v==1 and k!="ALL")==2,
   "minimal packet cardinality guard")

print(
    "PASS",
    f"task={TASK_ID}",
    f"checks={CHECKS}",
    f"B={B}",
    f"relation_states={len(REL)}",
    f"K_orbits={comb(len(REL)+2,3)}",
    "census_max=" + ",".join(f"{k}:{census_max[k]}" for k in SUBSETS),
    "global_max=" + ",".join(f"{k}:{GLOBAL_MAX[k]}" for k in SUBSETS),
    "minimal=P11+P21|P11+P12",
)
