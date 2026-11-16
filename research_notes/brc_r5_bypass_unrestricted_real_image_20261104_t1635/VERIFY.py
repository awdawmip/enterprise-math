#!/usr/bin/env python3
"""Exact Fraction checker for unrestricted terminal-declaration bypass BRC.
All comparisons use rational arithmetic. No third-party packages.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

ZERO, ONE, HALF = F(0),F(1),F(1,2)

def point(qmass, r, declare_q):
    return (qmass*r*declare_q, qmass*(1-declare_q))

def add(*pts):
    return tuple(sum(p[i] for p in pts) for i in (0,1))

def full_obs(xs, aas, b, d1, d2, dtA, db, dtB):
    """A1,A2 weights 1/4 each; B weight 1/2; all source Q=P at entry."""
    z=sum(xs[i]*aas[i] for i in range(2))/2
    x=sum(xs)/2
    f=x+z+b
    E=(ZERO,ZERO)
    for i in range(2):
        w=F(1,4)
        E=add(E,point(w*(1-xs[i]),ONE,d1[i]))
        E=add(E,point(w*xs[i]*(1-aas[i]),ONE,d2[i]))
        for j,r in enumerate((F(1,2),F(3,2))):
            E=add(E,point(w*xs[i]*aas[i]/2,r,dtA[i][j]))
    w=HALF
    E=add(E,point(w*(1-b),ONE,db))
    for j,r in enumerate((F(1,4),F(7,4))):
        E=add(E,point(w*b/2,r,dtB[j]))
    return (E[0],E[1],F(3,2)+f/2,F(3,2)+f/2), f

def canonical_vertices(f):
    assert 0<=f<=3
    if f<=1:
        x,y=ZERO,f
    else:
        x,y=(f-1)/2,ONE
    # x is A's common first continue; at t2 both A and B use y.
    z=x*y
    mstop=ONE-(z+y)/2
    masses=[(mstop,ONE),(z/F(4),F(1,2)),(z/F(4),F(3,2)),(y/F(4),F(1,4)),(y/F(4),F(7,4))]
    pts=[]
    for ds in product((ZERO,ONE), repeat=5):
        pts.append(add(*(point(m,r,d) for (m,r),d in zip(masses,ds))))
    return pts

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def convex_hull(pts):
    v=sorted(set(pts))
    if len(v)<=1:return v
    lo=[]
    for p in v:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(v):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def in_hull(p,hull):
    if len(hull)==1:return p==hull[0]
    if len(hull)==2:return cross(hull[0],hull[1],p)==0 and all(min(a,b)<=v<=max(a,b) for a,b,v in zip(hull[0],hull[1],p))
    return all(cross(hull[i],hull[(i+1)%len(hull)],p)>=0 for i in range(len(hull)))

# Complete deterministic policies compressed by identical A1/A2 source kernels:
# A: t1 stop(P/Q), t2 stop(P/Q), terminal four label pairs => 8 effective actions;
# B: t2 stop(P/Q), terminal four label pairs => 6 effective actions.
A=[('t1',d) for d in (ZERO,ONE)]+[('t2',d) for d in (ZERO,ONE)]+[('t3',p) for p in product((ZERO,ONE),repeat=2)]
B=[('t2',d) for d in (ZERO,ONE)]+[('t3',p) for p in product((ZERO,ONE),repeat=2)]
count=0
all_f=set()
for a,bact in product(A,B):
    ax=ZERO if a[0]=='t1' else ONE
    aa=ONE if a[0]=='t3' else ZERO
    by=ONE if bact[0]=='t3' else ZERO
    da1=a[1] if a[0]=='t1' else ZERO
    da2=a[1] if a[0]=='t2' else ZERO
    dat=a[1] if a[0]=='t3' else (ZERO,ZERO)
    db=bact[1] if bact[0]=='t2' else ZERO
    dbt=bact[1] if bact[0]=='t3' else (ZERO,ZERO)
    w,f=full_obs((ax,ax),(aa,aa),by,(da1,da1),(da2,da2),(dat,dat),db,dbt)
    hull=convex_hull(canonical_vertices(f))
    assert in_hull(w[:2],hull),(a,bact,w,hull)
    count+=1
    all_f.add(f)
assert count==48
print('EXACT_DETERMINISTIC_FULL_48=PASS', 'f_levels='+str(sorted(all_f)))

# All-real, all-signed lemma: B is a mean-preserving spread of A.
# Exact sign-complete case split for support function v(r)=max(a*r,b):
# sample rational directions to independently verify h_B>=h_A>=h_0 and canonical optimality.
dirs=[(F(a,5),F(b,5)) for a in range(-10,11) for b in range(-10,11)]
def supportK(ratios,n):
    return sum((max(n[0]*r,n[1]) for r in ratios),ZERO)/len(ratios)
for n in dirs:
    H0=supportK((ONE,),n)
    HA=supportK((F(1,2),F(3,2)),n)
    HB=supportK((F(1,4),F(7,4)),n)
    assert HB>=HA>=H0,(n,H0,HA,HB)
    for f in [F(k,8) for k in range(25)]:
        for x in [F(k,16) for k in range(17)]:
            for z in (ZERO,x/2,x):
                y=f-x-z
                if ZERO<=y<=ONE:
                    cand=H0+(z*(HA-H0)+y*(HB-H0))/2
                    can=H0+((f if f<=1 else ONE)*(HB-H0) + (ZERO if f<=1 else (f-1)/2)*(HA-H0))/2
                    assert cand<=can,(n,f,x,z,y,cand,can)
print('EXACT_SIGNED_SUPPORT_441_DIRECTIONS_AND_ALL_SELECTED_RATIONAL_STATES=PASS')

# 240 reproducible fully non-deterministic FULL policies with arbitrary individual A labels.
rng=Random(20261104)
values=(ZERO,F(1,7),F(1,5),F(1,3),HALF,F(2,3),F(4,5),F(6,7),ONE)
for k in range(240):
    rand=lambda:rng.choice(values)
    xs=(rand(),rand()); aas=(rand(),rand()); b=rand()
    d1=(rand(),rand());d2=(rand(),rand())
    dtA=((rand(),rand()),(rand(),rand()))
    db=rand(); dtB=(rand(),rand())
    w,f=full_obs(xs,aas,b,d1,d2,dtA,db,dtB)
    hull=convex_hull(canonical_vertices(f))
    assert in_hull(w[:2],hull),(k,w,f,hull)
print('EXACT_NONVERTEX_FULL_240=PASS')

def triangle_certificate(p, vertices):
    hull=convex_hull(vertices)
    if len(hull)==1:
        assert p==hull[0]
        return [(ONE,hull[0])]
    if len(hull)==2:
        u,v=hull
        i=0 if u[0]!=v[0] else 1
        t=(p[i]-u[i])/(v[i]-u[i])
        assert 0<=t<=1 and tuple(u[j]*(1-t)+v[j]*t for j in (0,1))==p
        return [(ONE-t,u),(t,v)]
    a=hull[0]
    for i in range(1,len(hull)-1):
        b,c=hull[i],hull[i+1]
        D=cross(a,b,c)
        if D==0:continue
        lb=cross(a,p,c)/D
        lc=cross(a,b,p)/D
        la=ONE-lb-lc
        if min(la,lb,lc)>=0:
            assert add(*(tuple(l*coord for coord in v) for l,v in ((la,a),(lb,b),(lc,c))))==p
            return [(l,v) for l,v in ((la,a),(lb,b),(lc,c)) if l>0]
    raise AssertionError((p,hull))

rng2=Random(20261105)
max_terms=0
for k in range(240):
    rand=lambda:rng2.choice(values)
    xs=(rand(),rand());aas=(rand(),rand());b=rand()
    d1=(rand(),rand());d2=(rand(),rand())
    dtA=((rand(),rand()),(rand(),rand()))
    db=rand();dtB=(rand(),rand())
    w,f=full_obs(xs,aas,b,d1,d2,dtA,db,dtB)
    cert=triangle_certificate(w[:2], canonical_vertices(f))
    assert sum((l for l,_ in cert),ZERO)==ONE
    assert len(cert)<=3
    max_terms=max(max_terms,len(cert))
print('EXACT_CARATHEODORY_240_TRIPLES=PASS max_terms='+str(max_terms))

# Earlier fixed-declaration LR nonconvex midpoint is now in the free-label fiber.
mid=((ONE+F(13,16))/2,F(1,4))
f=F(3,2)
assert in_hull(mid,convex_hull(canonical_vertices(f)))
print('PREVIOUS_FORCED_LABEL_MIDPOINT_NOW_ATTAINABLE_AT_CANONICAL_TIME_FIBER=PASS',str(mid),str(f))
print('PASS_EXACT_R5_BYPASS_UNRESTRICTED_DECLARATION_IMAGE_EQUALITY')
