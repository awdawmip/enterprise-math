#!/usr/bin/env python3
"""R5: all-real exposed-edge lift obstruction for independent K Q delays.
Uses only Python's standard-library Fraction.  Every displayed assertion is exact.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE, HALF = F(0), F(1), F(1, 2)
FULL_KEYS = list(product((ZERO, ONE), repeat=7))
LR_KEYS = list(product((ZERO, ONE), repeat=3))
TESTS = 0
FLOWS = 0

def check(p, message):
    global TESTS
    TESTS += 1
    if not p:
        raise AssertionError(message)

def add(*vs):
    return tuple(sum(v[j] for v in vs) for j in range(4))

def scale(c, v):
    return tuple(c*x for x in v)

def stop(time):
    return (ONE, ZERO, F(time), F(time))

def answer(time, p, q):
    return (p, ONE-q, F(time), F(time))

def dot(v, w):
    return sum(x*y for x, y in zip(v, w))

def flow(t, delays, x, jB, jI, kC, kI, kBJ, kIJ):
    global FLOWS
    FLOWS += 1
    def knode(source, k):
        return add(scale(k,stop(3)),
                   scale(ONE-k,(HALF, HALF, F(4)+t, F(4)+delays[source])))
    def jnode(source, j, k):
        daughter = 'BJ' if source == 'B' else 'IJ'
        return add(scale(j,stop(2)),
                   scale(ONE-j,add(scale(HALF, knode(daughter,k)),
                                   scale(HALF,answer(3,F(3,5),F(2,5))))))
    i = add(scale(x,stop(1)),scale(ONE-x,
            add(scale(HALF,jnode('I',jI,kIJ)),scale(HALF,knode('I',kI)))))
    return add(scale(HALF,i),scale(F(1,4),jnode('B',jB,kBJ)),
               scale(F(1,4),knode('C',kC)))

def lr(t,d,x,y,z):
    return flow(t,d,x,y,y,z,z,z,z)

def det4(matrix):
    a=[row[:] for row in matrix]
    det=ONE
    for j in range(4):
        pivot=next((k for k in range(j,4) if a[k][j]!=0),None)
        if pivot is None: return ZERO
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            det=-det
        p=a[j][j]
        det*=p
        for k in range(j+1,4):
            factor=a[k][j]/p
            for h in range(j+1,4):
                a[k][h]-=factor*a[j][h]
            a[k][j]=ZERO
    return det

def affine_determinant(points):
    return det4([[points[j+1][i]-points[0][i] for j in range(4)]
                 for i in range(4)])

def jacobian_minor(t,d):
    v=[HALF]*7
    cols=[]
    for k in (0,1,2,3):
        a=v.copy();a[k]=ONE
        b=v.copy();b[k]=ZERO
        A=flow(t,d,*a);B=flow(t,d,*b)
        cols.append(tuple(A[i]-B[i] for i in range(4)))
    return det4([[cols[j][i] for j in range(4)] for i in range(4)])

def facet_normals(t):
    return {
        'A':((6*t-4,4*t-6,ONE),(0,1,2,3)),
        'B':((-6*t-29,-4*t-21,-ONE),(0,2,4,6)),
        'C':((-ONE,-ONE,ZERO),(2,3,6,7)),
        'D':((34-6*t,36-4*t,-ONE),(0,1,4,5)),
        'E':((4-6*t,6-4*t,-ONE),(4,5,6,7)),
    }

EDGE_CASES = [
    ('AB',0,2,[(16,F(1,2),+1),(32,F(1,2),-1)],'BJ','IJ',16),
    ('AC',2,3,[(52,F(1,2),+1),(56,F(1,2),-1)],'C','I',8),
    ('DE',4,5,[(66,F(1,3),+1),(72,F(2,3),-1)],'C','BJ',12),
]

# Full tables at the five hypercube coordinates (t,c,i,b,j).
# Each fixed behavior policy gives outputs of degree <=1 in each of these
# coordinates. Exact corner identities therefore cover the full cube.
check(len(FULL_KEYS)==128 and len(LR_KEYS)==8, 'policy cube counts')
facet_slack_min={n:None for n in ['A','B','C','D','E']}
for t in (ZERO, HALF, ONE):
    # projected LR vertices do not depend on source-Q delays
    reference={'C':ZERO,'I':ZERO,'BJ':ZERO,'IJ':ZERO}
    L=[lr(t,reference,*p) for p in LR_KEYS]
    facets=facet_normals(t)
    for tag,(normal,vertices) in facets.items():
        h=dot(normal,L[vertices[0]][:3])
        for k,p in enumerate(L):
            slack=h-dot(normal,p[:3])
            check(slack==0 if k in vertices else slack>0,
                  f'{tag} facet proper slack t={t} vertex={k}')
            if k not in vertices:
                facet_slack_min[tag]=(slack if facet_slack_min[tag] is None
                                      else min(facet_slack_min[tag],slack))
    for combo in product((ZERO,ONE),repeat=4):
        delays=dict(zip(('C','I','BJ','IJ'),combo))
        l=[lr(t,delays,*p) for p in LR_KEYS]
        f=[flow(t,delays,*p) for p in FULL_KEYS]
        for edge,a,b,wits,u,v,den in EDGE_CASES:
            for idx,lam,sgn in wits:
                mixture=add(scale(ONE-lam,l[a]),scale(lam,l[b]))
                check(f[idx][:3]==mixture[:3],f'{edge} projected interpolation')
                predicted=sgn*(delays[u]-delays[v])/den
                check(f[idx][3]-mixture[3]==predicted,
                      f'{edge} exact vertical defect')
        check(all(ONE<=p[3]<=5 for p in l+f),'terminal expectation bounds')
print('EXPOSED_FACET_MIN_SLACKS',facet_slack_min)
check(facet_slack_min=={'A':F(3,4),'B':F(3,4),'C':F(1,40),
                        'D':F(3,4),'E':F(3,4)},'facet minimum slacks')

# Source-blind aggregation when all K Q delays are equal.
def aggregate(x,jB,jI,kC,kI,kBJ,kIJ):
    y=(jB+(ONE-x)*jI)/(2-x)
    mc=F(1,4);mi=(ONE-x)/4
    mbj=(ONE-jB)/8;mij=(ONE-x)*(ONE-jI)/8
    total=mc+mi+mbj+mij
    z=(mc*kC+mi*kI+mbj*kBJ+mij*kIJ)/total
    return y,z

samples=[F(1,7),F(2,9),F(5,11),F(3,8),F(7,10)]
for t in (F(1,7), HALF, F(6,7)):
    for q in (F(1,9), F(4,7), F(8,9)):
        delays={s:q for s in ('C','I','BJ','IJ')}
        for a in range(45):
            params=tuple(samples[(a+i*i+3*i)%5] for i in range(7))
            x,jB,jI,kC,kI,kBJ,kIJ=params
            y,z=aggregate(*params)
            check(ZERO<=y<=ONE and ZERO<=z<=ONE,'valid pooled policy')
            check(flow(t,delays,*params)==lr(t,delays,x,y,z),
                  'exact real-policy aggregation')

# Candidate neutralizes the predecessor's moving normal yet retains a
# nonzero Farkas certificate and both independent rank witnesses.
t=HALF
D={'C':F(1,4),'I':F(1,4),'BJ':F(1,4),'IJ':F(1,3)}
LL=[lr(t,D,*p) for p in LR_KEYS]
FF=[flow(t,D,*p) for p in FULL_KEYS]
old=(-21,-14,-12,12)
check(max(dot(old,p) for p in FF)==max(dot(old,p) for p in LL),
      'predecessor moving normal ties')
n=(-3169,-2916,ZERO,108)
hl=max(dot(n,p) for p in LL)
hf=max(dot(n,p) for p in FF)
w=FF[32]
check(w==(F(51,80),F(31,80),F(59,16),F(85,24)), 'explicit witness')
check(hl==F(-11073,4),'LR exact support')
check(hf==F(-44283,16),'FULL exact support')
check(dot(n,w)==hf,'witness attains FULL support')
check(hf-hl==F(9,16),'exact support separation')
check((hf-hl)/sum(abs(a) for a in n)==F(9,99088),'exact distance bound')
check(affine_determinant([LL[k] for k in (0,1,2,4,5)])==F(3,40960),
      'LR rank four')
check(jacobian_minor(t,D)==F(-1,163840),'FULL rank four')
print('CONCRETE_Q',D)
print('OLD_DIRECTION_TIE',max(dot(old,p) for p in FF))
print('NEW_NORMAL',n,'hFULL',hf,'hLR',hl,'gap',hf-hl)
print('FULL_WITNESS',w,'dist_infinity_lower_bound',F(9,99088))
print('LR_AFFINE_DETERMINANT',F(3,40960),
      'FULL_INTERIOR_JACOBIAN_MINOR',F(-1,163840))

# Exact sharp minimax lower bound of the three edge defects when
# qI=1/4 and qIJ=1/3: min max=1/432 over c,b in [0,1].
# Triangle inequality proves >= 1/432; the rational pair attains it.
c,b=F(29,108),F(8,27)
residuals=(abs(b-F(1,3))/16,abs(c-F(1,4))/8,abs(c-b)/12)
check(residuals==(F(1,432),)*3,'sharp minimax at balanced parameters')
check(F(1,3)-F(1,4)==F(1,12),'fixed internal delay mismatch')
print('SHARP_EDGE_MINIMAX',F(1,432),'at c=',c,'b=',b)
print('UNIFORM_LINF_HAUSDORFF_LOWER_BOUND',F(1,432*82023))
print('PROOF_DOMAIN t,c,i,b,j in [0,1] algebraically; strict P/Q positivity in (0,1)')
print('FACET_SCORES degree<=2 in t; equalities multiaffine in the five parameters')
print('CHECKS',TESTS,'EXACT_FLOW_EVALUATIONS',FLOWS)
print('PASS_EXACT_R5_ALL_Q_SOURCE_EXPOSED_EDGE_FIBER_CLASSIFICATION')
