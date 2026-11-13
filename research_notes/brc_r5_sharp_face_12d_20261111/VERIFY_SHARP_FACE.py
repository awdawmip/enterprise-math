#!/usr/bin/env python3
"""R5: independent exact rational reproduction of sharp-edge localization and
12-dimensional fixed-fiber carrier. Requires Python 3 and SymPy (rank only).
Frozen data: enterprise-math PR #2017 witness, PR #2045 circuit labels,
PR #2049 exact fixed-fiber incidence; no task input is repinned.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations
from sympy import Matrix

R = (2, 10, 15, 20, 25, 30, 38)
S = (1, 2, 3, 5)
ARCS = tuple((i, j) for j in (0, 1, 2, 3, 5, 6) for i in range(7)
             if j not in (0, 6) or i == j)
E0 = tuple(map(F, (
    '219346331/10192753200,7664319/135903376,'
    '2813871/16987922,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,196521/33975844,'
    '196521/33975844,393042/8493961,196521/33975844,'
    '196521/33975844,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,196521/33975844,'
    '5251441/33975844,166713611/1274094150,2500147/33975844,'
    '393042/8493961,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,7664319/135903376,'
    '451274777/3397584400').split(',')))
assert len(E0) == len(ARCS) == 30 and min(E0) > 0
M = tuple(sum((v for (i, j), v in zip(ARCS, E0)
               if i == k and j in S), F(0)) for k in range(7))
Q = {j: sum((v for (i, jj), v in zip(ARCS, E0) if j == jj), F(0)) for j in S}
T = {j: sum((R[i]*v for (i, jj), v in zip(ARCS, E0) if j == jj), F(0)) for j in S}
assert Q[3] == F('1076926147/2548188300') and T[3] == 20*Q[3]

def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def minus(a,b): return (a[0]-b[0],a[1]-b[1])
def times(a,v): return (a[0]*v,a[1]*v)
def over(a,v): return (a[0]/v,a[1]/v)
def const(a): return (a,F(0))

def edge_coefficients(labels):
    a,b,c,d,e,f,g = (R[i] for i in labels)
    ua=(b-c)*(d-e); ub=(c-a)*(d-e); uc=(a-b)*(d-e)
    ud=-(b-c)*(e-a); ue=-(b-c)*(a-d)
    vf=-ub*(b-g)-ud*(d-g)
    vg=-ub*(f-b)-ud*(f-d)
    return tuple(k*(g-f) for k in (ua,ub,uc,ud,ue))+(vf,vg)

def affine(low,labels):
    p,q=low
    h,k=(j for j in S if j not in low)
    A,B,C,D,E,FF,G=labels
    a,b,c,d,e,f,g=(R[i] for i in labels)
    z=(F(0),F(1))
    xA=z
    xB=over(minus(const(T[p]-c*Q[p]),times(z,a-c)),b-c)
    xC=minus(minus(const(Q[p]),z),xB)
    xD=over(plus(const(T[q]-e*Q[q]+(e-a)*M[A]),times(z,a-e)),d-e)
    xE=minus(plus(const(Q[q]-M[A]),z),xD)
    H0=plus(const(Q[h]-M[B]-M[D]),plus(xB,xD))
    H1=plus(const(T[h]-b*M[B]-d*M[D]),plus(times(xB,b),times(xD,d)))
    xF=over(minus(times(H0,g),H1),g-f)
    xG=minus(H0,xF)
    return xA,xB,xC,xD,xE,xF,xG

def feasible_open_interval(labels,x):
    low=high=None
    for i,(a,b) in zip(labels,x):
        if not b:
            if not 0<a<M[i]: return None
            continue
        l=min(-a/b,(M[i]-a)/b)
        h=max(-a/b,(M[i]-a)/b)
        low=l if low is None else max(low,l)
        high=h if high is None else min(high,h)
        if low>=high: return None
    return low,high

def observer(e):
    return (tuple(sum((v for (i,j),v in zip(ARCS,e) if i==k),F(0)) for k in range(7)),
            tuple(sum((v for (i,j),v in zip(ARCS,e) if j==k),F(0)) for k in range(7)),
            tuple(sum((R[i]*v for (i,j),v in zip(ARCS,e) if j==k),F(0)) for k in range(7)))

OBS0=observer(E0)

def build(low,labels,t):
    p,q=low; h,k=(j for j in S if j not in low)
    pairs=((p,q),(p,h),(p,k),(q,h),(q,k),(h,k),(h,k))
    a=affine(low,labels)
    x={(0,0):E0[0],(6,6):E0[-1]}
    for ((s,ss),i),(v,w) in zip(zip(pairs,labels),a):
        mass=v+w*t
        assert 0<=mass<=M[i]
        x[(i,s)]=mass
        x[(i,ss)]=M[i]-mass
    result=tuple(x.get(arc,F(0)) for arc in ARCS)
    assert min(result)>=0 and observer(result)==OBS0
    return result

# Independent single-row capacity/moment census: all 35 four-target masks.
# The greedy exchange argument gives exact attainable moment endpoints.
row3_masks=[]
row3_rejections=Counter()
for J in combinations(range(7),4):
    if sum((M[i] for i in J),F(0))<Q[3]:
        row3_rejections['capacity']+=1
        continue
    def greedy(reverse):
        remaining=Q[3]
        score=F(0)
        for i in sorted(J,key=lambda i:R[i],reverse=reverse):
            portion=min(M[i],remaining)
            score+=R[i]*portion
            remaining-=portion
        assert remaining==0
        return score
    minimum,maximum=greedy(False),greedy(True)
    if minimum<T[3]<maximum:
        assert Q[3]<sum((M[i] for i in J),F(0))
        row3_masks.append(J)
    elif minimum<=T[3]<=maximum:
        row3_rejections['moment_boundary']+=1
    else:
        row3_rejections['moment']+=1
assert row3_rejections=={'capacity':9,'moment':19}
assert row3_masks==[(1,2,3,6),(1,2,4,6),(1,3,4,6),
                    (1,3,5,6),(1,4,5,6),(2,3,4,5),(2,3,4,6)]

# Independent complete 6*7!/2 exact enumeration, not reading stored output counts.
count=complete=0
feasible=[]
for low in combinations(S,2):
    p,q=low; h,k=(j for j in S if j not in low)
    pairs=((p,q),(p,h),(p,k),(q,h),(q,k),(h,k),(h,k))
    for labels in permutations(range(7)):
        if labels[5]>labels[6]: continue
        count+=1
        if edge_coefficients(labels)[-1]*edge_coefficients(labels)[-2]==0:continue
        complete+=1
        I=feasible_open_interval(labels,affine(low,labels))
        if I is None:continue
        J=tuple(sorted(i for i,pair in zip(labels,pairs) if 3 in pair))
        feasible.append((low,labels,I,J,build(low,labels,(I[0]+I[1])/2)))
assert count==15120 and complete==14832 and len(feasible)==49
by_source=Counter(rec[0] for rec in feasible)
assert by_source=={(1,2):15,(1,5):15,(2,5):19}
Jcounts=Counter(rec[3] for rec in feasible)
assert Jcounts=={(2,3,4,5):49}

# Exact edge endpoints and source-3 minimal support attainment.
endpoints=set()
for low,labels,I,J,_ in feasible:
    for t in I:
        vec=build(low,labels,t)
        assert sum(z>0 for z in vec)==15
        assert tuple(i for (i,j),z in zip(ARCS,vec) if j==3 and z>0)==(2,3,4,5)
        endpoints.add(vec)
assert len(endpoints)==58

# Average 49 strictly positive edge interior points: support exactly 26 arcs.
Ebar=tuple(sum((rec[4][k] for rec in feasible), F(0))/len(feasible)
           for k in range(len(ARCS)))
assert observer(Ebar)==OBS0 and min(Ebar)>=0
support={arc for arc,v in zip(ARCS,Ebar) if v>0}
missing=set(ARCS)-support
assert missing=={(0,3),(1,3),(6,3),(6,1)} and len(support)==26

# Explicit signed K_{2,3} residual between ports 1 and 2 at targets 4,5,6.
# At source 1: (+8,-13,+5), source 2: (-8,+13,-5).
# Both 8-13+5=0 and 25*8-30*13+38*5=0.
H={(4,1):F(8),(5,1):F(-13),(6,1):F(5),
   (4,2):F(-8),(5,2):F(13),(6,2):F(-5)}
# exact row and target conservation checks
for j in S:
    assert sum((v for (i,jj),v in H.items() if jj==j),F(0))==0
    assert sum((R[i]*v for (i,jj),v in H.items() if jj==j),F(0))==0
for i in range(7):
    assert sum((v for (ii,j),v in H.items() if ii==i),F(0))==0
positions={a:i for i,a in enumerate(ARCS)}
eps=min(Ebar[positions[(5,1)]]/26,
        Ebar[positions[(4,2)]]/16,
        Ebar[positions[(6,2)]]/10)
assert eps>0
Eprime=tuple(Ebar[k]+eps*H.get(arc,F(0)) for k,arc in enumerate(ARCS))
assert observer(Eprime)==OBS0 and min(Eprime)>=0
absent={(0,3),(1,3),(6,3)}
assert {arc for arc,v in zip(ARCS,Eprime) if v==0}==absent
assert len([v for v in Eprime if v>0])==27

# Exactly 15 independent restrictions remain: the face dimension is 27-15=12.
C=Matrix.hstack(*(Matrix([int(i==ii) for ii in range(7)]
                  +[int(j==jj) for jj in range(7)]
                  +[R[i] if j==jj else 0 for jj in range(7)])
                  for i,j in ARCS))
rank_full=C.rank()
rank_face=C[:,[k for k,arc in enumerate(ARCS) if arc not in absent]].rank()
assert rank_full==rank_face==15
assert len(ARCS)-len(absent)-rank_face==12
print('SCIENTIFIC_INPUTS',R)
print('CANDIDATES',count,'COMPLETE',complete)
print('SOURCE3_FOUR_MASKS_TESTED',35)
print('SOURCE3_ROW_ONLY_STRICT_FEASIBLE_MASKS',row3_masks)
print('SOURCE3_ROW_ONLY_REJECTIONS',sorted(row3_rejections.items()))
print('PHYSICALLY_REALIZED_SHARP_EDGES',len(feasible))
print('BY_LOW_PAIR',sorted(by_source.items()))
print('SOURCE3_SHARP_TARGETS',sorted(Jcounts.items()))
print('MEAN_INTERIOR_SUPPORT',len(support))
print('MEAN_MISSING_ARCS',sorted(missing))
print('REPAIR_CIRCUIT_TARGETS',(4,5,6),'SOURCE_PAIR',(1,2))
print('EXACT_REPAIR_EPSILON',eps)
print('REPAIRED_STRICT_FACE_SUPPORT',sum(v>0 for v in Eprime))
print('FIXED_FIBER_RANK',rank_full,'RESTRICTED_FACE_RANK',rank_face)
print('SHARP_CARRIER_FACE_DIMENSION',len(ARCS)-len(absent)-rank_face)
print('SHARP_EDGE_UNIQUE_ENDPOINTS',len(endpoints))
print('SOURCE3_MIN_BRANCHES',4,'WITNESS_ATTAINS_BOUND',True)
print('PASS_R5_EXACT_SHARP_FACE_12_DIM')
