#!/usr/bin/env python3
"""Exact task-local checker for RS-P000-SIX-AXIS-JOHNSON-TROPICAL-ARITHMETIC-INTEGRATION.

Pure standard library. No floating point. This is a certificate checker, not a new general-purpose tool.
"""
from itertools import product, permutations
from collections import defaultdict
from math import isqrt

LABELS=("AB","AC","AD","BC","BD","CD")
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
INDEX={e:i for i,e in enumerate(EDGES)}
PAIRS=((0,5),(1,4),(2,3))
CHECKS=0

def ck(cond, msg="check failed"):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def edge_perm(pi):
    out=[]
    for u,v in EDGES:
        a,b=pi[u],pi[v]
        if a>b: a,b=b,a
        out.append(INDEX[(a,b)])
    return tuple(out)

def compose(p,q):
    return tuple(p[q[i]] for i in range(6))

def apply_perm(p,x):
    y=[0]*6
    for i,j in enumerate(p):
        y[j]=x[i]
    return tuple(y)

S4=set()
for pt in permutations(range(4)):
    S4.add(edge_perm({i:pt[i] for i in range(4)}))
C=(5,4,3,2,1,0)
GAMMA=set(S4)|{compose(C,p) for p in S4}

WREATH=set()
for sigma in permutations(range(3)):
    for sw in product((0,1), repeat=3):
        p=[None]*6
        for j,(a,b) in enumerate(PAIRS):
            c,d=PAIRS[sigma[j]]
            if sw[j]:
                p[a],p[b]=d,c
            else:
                p[a],p[b]=c,d
        WREATH.add(tuple(p))
ck(len(S4)==24)
ck(len(GAMMA)==48)
ck(all(compose(C,p)==compose(p,C) for p in S4))
ck(GAMMA==WREATH)

def tvals(x):
    return (x[0]*x[5], x[1]*x[4], x[2]*x[3])

def hsums(x):
    return (x[0]+x[5], x[1]+x[4], x[2]+x[3])

def qscalar(x):
    t1,t2,t3=tvals(x)
    return t1-t2+t3

def qorbit(x):
    t=tvals(x)
    S=sum(t)
    return tuple(sorted(S-2*z for z in t))

def products_from_qorbit(q):
    S=sum(q)
    numer=tuple(S-z for z in q)
    ck(all(n%2==0 for n in numer), "Q_orb parity inversion")
    return tuple(sorted(n//2 for n in numer))

def rho(x):
    return ((x[0]-x[5])%2,(x[1]-x[4])%2,(x[2]-x[3])%2,sum(x)%3)

def rho_orbit(x):
    r=rho(x)
    return tuple(sorted(r[:3]))+(r[3],)

def delta(v):
    s=sorted(v)
    return s[1]-s[0]

def tie_type(v):
    s=sorted(v)
    if s[0]<s[1]:
        return "UNIQUE_MIN"
    if s[0]==s[1]<s[2]:
        return "TWO_MIN"
    return "TRIPLE_MIN"

def pair_packet(x):
    return tuple(sorted(zip(hsums(x),tvals(x))))

def canon_gamma(x):
    return min(apply_perm(g,x) for g in GAMMA)

def roots_ht(h,t):
    D=h*h-4*t
    if D<0: return None
    d=isqrt(D)
    if d*d!=D or (h-d)%2:
        return None
    return tuple(sorted(((h-d)//2,(h+d)//2)))

def completion_packets(H,T):
    H=tuple(sorted(H)); T=tuple(sorted(T))
    out=set()
    for tp in set(permutations(T)):
        if all(roots_ht(h,t) is not None for h,t in zip(H,tp)):
            out.add(tuple(sorted(zip(H,tp))))
    return out

def state_from_packet(pp):
    x=[0]*6
    for (i,j),(h,t) in zip(PAIRS,pp):
        a,b=roots_ht(h,t)
        x[i],x[j]=a,b
    return tuple(x)

# Q_orb is equivalent to the unordered complementary-product triple.
packet_to_orbit={}
for x in product(range(-2,3), repeat=6):
    q=qorbit(x)
    ck(products_from_qorbit(q)==tuple(sorted(tvals(x))), "Q_orb inversion mismatch")
    # rho is already encoded by the raw complementary-pair sums H:
    h=hsums(x)
    r=rho(x)
    ck(tuple(z%2 for z in h)==r[:3], "rho parity not H mod 2")
    ck(sum(h)%3==r[3], "rho mod-3 sum not H total")
    pp=pair_packet(x)
    c=canon_gamma(x)
    old=packet_to_orbit.setdefault(pp,c)
    ck(old==c, "pair packet not Gamma-complete on B=2 census")
ck(len(packet_to_orbit)==680)

# Symbolic representability gate and Gamma-completeness:
# each (h,t) gives the unordered roots of z^2-hz+t, so an aligned pair packet
# is a complete invariant under C2 wr S3 = <S4,C>.
for h in range(-8,9):
    for t in range(-16,17):
        r=roots_ht(h,t)
        if r is not None:
            a,b=r
            ck(a+b==h and a*b==t)

# Accepted raw-W_COORD matched control: raw pair sums add information beyond Q_orb/rho.
x=(-2,-2,0,2,1,1)
y=(-2,-1,-1,2,2,0)
ck(qorbit(x)==qorbit(y)==(-4,0,0))
ck(rho_orbit(x)==rho_orbit(y)==(0,1,1,0))
ck(delta(hsums(x))==0 and delta(hsums(y))==3)
ck(pair_packet(x)!=pair_packet(y))

# Alignment is a genuine missing coordinate after separately quotienting H and T.
xa=(-2,-2,1,0,1,-2)
ya=(-2,-1,-1,0,2,-2)
ck(tuple(sorted(hsums(xa)))==tuple(sorted(hsums(ya)))==(-4,-1,1))
ck(tuple(sorted(tvals(xa)))==tuple(sorted(tvals(ya)))==(-2,0,4))
ck(qorbit(xa)==qorbit(ya)==(-6,2,6))
ck(rho_orbit(xa)==rho_orbit(ya)==(0,1,1,2))
ck(delta(hsums(xa))==delta(hsums(ya))==3)
ck(pair_packet(xa)!=pair_packet(ya))
ck(canon_gamma(xa)!=canon_gamma(ya))

# The exact 6-orbit upper bound is attained.
H6=(-3,3,9)
T6=(-70,-10,0)
packs=completion_packets(H6,T6)
ck(len(packs)==6)
reps=[state_from_packet(pp) for pp in packs]
ck(len({canon_gamma(z) for z in reps})==6)
for z in reps:
    ck(tuple(sorted(hsums(z)))==H6)
    ck(tuple(sorted(tvals(z)))==T6)

def vp(n,p):
    if n==0:
        return None
    n=abs(n); k=0
    while n%p==0:
        n//=p; k+=1
    return k

def alpha(x,p):
    return tuple(vp(t,p) for t in tvals(x))

# W_VP delta/order/tie is redundant with Q_orb on D_p: Q_orb recovers |{t_i}|.
NZ=(-2,-1,1,2)
for p in (2,3,5):
    for x in product(NZ, repeat=6):
        T=products_from_qorbit(qorbit(x))
        a1=tuple(sorted(vp(t,p) for t in T))
        a2=tuple(sorted(alpha(x,p)))
        ck(a1==a2)
        ck(delta(a1)==delta(a2))
        ck(tie_type(a1)==tie_type(a2))

# Exact valuation facts: unique minimum is always safe; at p=2 a triple minimum is also safe.
TV=[z for z in range(-16,17) if z]
for p in (2,3,5):
    for t1 in TV:
        for t2 in TV:
            for t3 in TV:
                A=(vp(t1,p),vp(t2,p),vp(t3,p))
                q=t1-t2+t3
                typ=tie_type(A)
                m=min(A)
                if typ=="UNIQUE_MIN":
                    ck(q!=0 and vp(q,p)==m, "unique-min valuation law")
                if p==2 and typ=="TRIPLE_MIN":
                    ck(q!=0 and vp(q,2)==m, "2-adic triple-tie law")

# Two-minimum cancellation ambiguity survives even the complete Gamma-invariant pair packet.
for p,a in ((2,2),(3,6),(5,10)):
    b=1; c=1-a
    x=(a,a,a,a,b,c)
    y=(a,a,a,a,c,b)
    ck(pair_packet(x)==pair_packet(y))
    ck(qorbit(x)==qorbit(y))
    ck(rho_orbit(x)==rho_orbit(y))
    ck(tuple(sorted(alpha(x,p)))==tuple(sorted(alpha(y,p))))
    ck(tie_type(alpha(x,p))=="TWO_MIN")
    ck(qscalar(x)==0)
    ck(qscalar(y)==2*a*a)
    ck(vp(qscalar(y),p) is not None)

# For odd p, triple ties also admit cancellation ambiguity.
for p in (3,5,7):
    a=2; b=1; c=-1
    x=(a,a,a,a,b,c)
    y=(a,a,a,a,c,b)
    ck(pair_packet(x)==pair_packet(y))
    ck(tie_type(alpha(x,p))=="TRIPLE_MIN")
    ck(qscalar(x)==0 and qscalar(y)==8)
    ck(vp(qscalar(y),p)==0)

# Exact 2-primary interaction between Johnson parity residue and product valuation.
possible=defaultdict(set)
for a in range(-64,65):
    if a==0: continue
    for b in range(-64,65):
        if b==0: continue
        al=vp(a*b,2)
        if al<=6:
            possible[al].add((a-b)%2)
expected={0:{0},1:{1},2:{0,1},3:{0,1},4:{0,1},5:{0,1},6:{0,1}}
ck(dict(possible)==expected)

# The Z/3 residue does not select a 3-adic tie regime: for fixed parity-orbit
# representatives, every total residue 0,1,2 occurs in each U/T2/T3 regime.
REGRESSION_3={
 "UNIQUE_MIN":[
  (-10,-8,10,-1,-9,-12),
  (6,-1,1,12,-2,6),
  (3,-5,11,11,6,12)],
 "TWO_MIN":[
  (-7,-4,3,11,8,-2),
  (12,4,-1,7,-4,1),
  (12,-2,-8,-8,10,7)],
 "TRIPLE_MIN":[
  (2,10,-1,-4,4,4),
  (-5,-2,-2,-8,-1,1),
  (5,4,4,-7,-2,-5)]
}
for typ,rows in REGRESSION_3.items():
    ck({sum(x)%3 for x in rows}=={0,1,2})
    ck(all(tie_type(alpha(x,3))==typ for x in rows))

print(f"LOCAL_DETERMINISTIC_PASS checks={CHECKS}")
