#!/usr/bin/env python3
"""Exact author-side certificate for the R5 delay-interpolation stopping model.
Uses Fraction only; no floating-point or non-BRC physical evolution.
"""
from fractions import Fraction as Q
from itertools import product

Z, ONE, H = Q(0), Q(1), Q(1,2)
KERNEL = {
    'C':  (Q(3,4), Q(1,4), Q(1,4), Q(3,4), Q(1,8)),
    'I':  (Q(1,4), Q(3,4), Q(3,4), Q(1,4), Q(1,4)),
    'BJ': (Q(2,3), Q(1,3), Q(1,3), Q(2,3), Q(1,6)),
    'IJ': (Q(1,3), Q(2,3), Q(2,3), Q(1,3), Q(1,3)),
}
J_FINAL = {'B': (Q(2,5), Q(3,5)), 'I': (Q(3,5), Q(2,5))}
checks=0
flows=0

def check(ok, name):
    global checks
    checks+=1
    if not ok: raise AssertionError(name)

def add(*V):
    return tuple(sum(v[i] for v in V) for i in range(4))
def sc(a,v):
    return tuple(a*t for t in v)
def stop(t):
    return ONE,Z,Q(t),Q(t)
def answer(t,p,q):
    return p,ONE-q,Q(t),Q(t)
def phys(lam,x,jb,ji,kc,ki,kbj,kij):
    global flows
    flows+=1
    def knode(source,k):
        p,q,dp,dq0,dq1=KERNEL[source]
        dq=(ONE-lam)*dq0+lam*dq1
        return add(sc(k,stop(3)),sc(ONE-k,(p,ONE-q,Q(4)+dp,Q(4)+dq)))
    def jnode(source,j,k):
        p,q=J_FINAL[source]
        origin='BJ' if source=='B' else 'IJ'
        c=add(sc(H,knode(origin,k)),sc(H,answer(3,p,q)))
        return add(sc(j,stop(2)),sc(ONE-j,c))
    i=add(sc(x,stop(1)),sc(ONE-x,add(sc(H,jnode('I',ji,kij)),sc(H,knode('I',ki)))))
    return add(sc(H,i),sc(Q(1,4),jnode('B',jb,kbj)),sc(Q(1,4),knode('C',kc)))
def lr(lam,x,y,z):
    return phys(lam,x,y,y,z,z,z,z)
def dot(n,v):
    return sum(Q(n[i])*v[i] for i in range(4))
def det(a):
    m=[row[:] for row in a]
    n=len(m)
    sign=ONE
    for j in range(n):
        pivot=next((i for i in range(j,n) if m[i][j]),None)
        if pivot is None: return Z
        if pivot!=j:
            m[j],m[pivot]=m[pivot],m[j]
            sign=-sign
        p=m[j][j]
        sign*=p
        for i in range(j+1,n):
            scale=m[i][j]/p
            for k in range(j+1,n):
                m[i][k]-=scale*m[j][k]
            m[i][j]=Z
    return sign

def time_gap(lam):
    if lam<=Q(2,3): return Q(1,6)-Q(7,32)*lam
    if lam<=Q(4,5): return Q(1,8)-Q(5,32)*lam
    return Z

FULL_KEYS=list(product((Z,ONE),repeat=7))
LR_KEYS=list(product((Z,ONE),repeat=3))
check(len(FULL_KEYS)==128 and len(LR_KEYS)==8,'corner cardinalities')
for lam in (Z,Q(1,5),H,Q(2,3),Q(3,4),Q(4,5),Q(9,10),ONE):
    allf={p:phys(lam,*p) for p in FULL_KEYS}
    alll={p:lr(lam,*p) for p in LR_KEYS}
    check(all(Z<t<ONE for row in KERNEL.values() for t in
          (row[0],row[1],row[2],(ONE-lam)*row[3]+lam*row[4])), 'positive K probabilities')
    for w in list(allf.values())+list(alll.values()):
        check(Z<=w[0]<=ONE and Z<=w[1]<=ONE, 'answer range')
    df=max(v[2]-v[3] for v in allf.values())
    dl=max(v[2]-v[3] for v in alll.values())
    if lam<=Q(2,3): expect_full=Q(1,6)
    elif lam<=Q(4,5): expect_full=Q(1,8)+lam/Q(16)
    else: expect_full=Q(7,32)*lam
    check(df==expect_full and dl==Q(7,32)*lam and df-dl==time_gap(lam), 'time facet envelopes')
    efmin=min(v[0]+v[1] for v in allf.values())
    elmin=min(v[0]+v[1] for v in alll.values())
    efmax=max(v[0]+v[1] for v in allf.values())
    elmax=max(v[0]+v[1] for v in alll.values())
    check((efmin,elmin,efmax,elmax)==(Q(5,6),Q(39,40),Q(7,6),Q(137,120)), 'answer facets')
    w=phys(lam,Z,Z,Z,ONE,Z,ONE,Z)
    check(w==(Q(29,48),Q(11,48),Q(175,48),Q(167,48)), 'fixed FULL counterexample witness')
    keys=[(Z,Z,Z),(Z,Z,ONE),(Z,ONE,Z),(ONE,Z,Z),(ONE,Z,ONE)]
    base=alll[keys[0]]
    col=[[alll[key][i]-base[i] for key in keys[1:]] for i in range(4)]
    check(det(col)==(ONE-lam)*Q(1,5120)+lam*Q(401,98304),'LR affine determinant')
    print('lambda',str(lam),'hF_D',str(df),'hLR_D',str(dl),'delta_D',str(df-dl),
          'min_FULL_answer',str(efmin),'min_LR_answer',str(elmin),'LR_rank_det',str(det(col)))

# FULL interior four-column Jacobian in columns (x,jB,jI,kC)
# Other three coordinates kI,kBJ,kIJ held at 1/2.
allmid=[H]*7

def minor(lam):
    columns=[]
    for j in (0,1,2,3):
        plus=allmid.copy();minus=allmid.copy()
        plus[j]=ONE;minus[j]=Z
        f1=phys(lam,*plus);f0=phys(lam,*minus)
        columns.append([f1[i]-f0[i] for i in range(4)])
    return det([[columns[j][i] for j in range(4)] for i in range(4)])
for lam in (Z,H,Q(4,5),ONE):
    check(minor(lam)==(ONE-lam)*(-Q(1,5120))+lam*(-Q(109,3932160)),'FULL interior Jacobian minor')

# Nonbinary regression: the full stopping formula is explicitly multi-affine,
# and its time contrast has the proven provenance-weight expression.
for lam in (Q(1,7),Q(5,8),Q(5,6)):
    for vals in product((Q(1,3),Q(2,3)),repeat=7):
        x,jb,ji,kc,ki,kbj,kij=vals
        v=phys(lam,*vals)
        dc=Q(-1,8)+Q(5,32)*lam
        dbj=Q(-1,24)+lam/Q(16)
        d=(dc*(ONE-kc)+Q(1,8)*(ONE-x)*(ONE-ki)
            +dbj*(ONE-jb)*(ONE-kbj)
            +Q(1,24)*(ONE-x)*(ONE-ji)*(ONE-kij))
        check(v[2]-v[3]==d,'interior time provenance identity')

print('FULL vertex count=128 LR vertex count=8; fixed answer gap=17/120')
print('D gap positive for 0<=lambda<4/5, zero for 4/5<=lambda<=1')
print('hull separation persists for all lambda in [0,1], infinity lower bound=17/240')
print('all-real argument: multi-affine strategy interpolation + exact affine-in-lambda coefficients')
print('checks=',checks,'physical_evaluations=',flows)
print('PASS_EXACT_R5_TEMPORAL_FACET_TRANSFER_AND_ANSWER_RESIDUAL')
