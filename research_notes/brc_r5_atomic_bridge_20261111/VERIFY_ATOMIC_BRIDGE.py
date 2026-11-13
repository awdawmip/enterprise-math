#!/usr/bin/env python3
"""R5 exact two-primitive residual bridge, and 9 exact one-atom no-go certificates.
Pure Python Fraction, no external solver. Reproduce: python3 VERIFY_ATOMIC_BRIDGE.py.
Provenance: source-3 R5 fixed auxiliary seven-ratio Blackwell fiber from PR #2068,
original frozen E0 / arcs from PR #2063's r5_prior_four.py.
Research date 2026-11-11; independent review and formal Source Result pending.
"""
from fractions import Fraction as F
R=(2,10,15,20,25,30,38)
S=(1,2,3,5)
ARCS=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
           if j not in (0,6) or i==j)
E0=tuple(map(F,(
 '219346331/10192753200,7664319/135903376,2813871/16987922,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,'
 '2500147/33975844,393042/8493961,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,7664319/135903376,451274777/3397584400').split(',')))
assert len(ARCS)==len(E0)==30 and min(E0)>0
V=tuple((i,j) for j in S for i in range(7))
idx={e:k for k,e in enumerate(V)}
M=[sum((z for (ii,j),z in zip(ARCS,E0) if ii==i and j in S),F(0)) for i in range(7)]
Q={j:sum((z for (i,jj),z in zip(ARCS,E0) if jj==j),F(0)) for j in S}
T={j:sum((R[i]*z for (i,jj),z in zip(ARCS,E0) if jj==j),F(0)) for j in S}
A=[[int(ii==i) for ii,jj in V] for i in range(7)]
A += [[int(jj==j) for ii,jj in V] for j in S]
A += [[R[ii]*int(jj==j) for ii,jj in V] for j in S]
b=M+[Q[j] for j in S]+[T[j] for j in S]
assert len(A)==len(b)==15 and len(V)==28
JA={1,3,4,6};JC={2,3,4,6};JUNION=JA|JC
def atom(other,third,normalize=False):
    assert other in (1,2,5) and third in (3,4,6)
    h=[F(0)]*28
    if normalize:
        alpha=F(R[third]-R[1],R[third]-R[2])
        row={1:-F(1),2:alpha,third:1-alpha}
    else:
        assert third==6
        row={1:F(-23),2:F(28),6:F(-5)}
    for i,v in row.items():
        h[idx[(i,3)]]=v
        h[idx[(i,other)]]=-v
    assert all(sum(F(A[r][k])*h[k] for k in range(28))==0
               for r in range(15))
    return h
# Sparse exact dual separators for all nine possible one-atom transitions.
# 0..14 are observation equalities; 15..42 are endpoint slack equalities;
# row 43 enforces the zero endpoint arc Y_(1,3).
SPARSE_CERTS={
  (1, 3): [(3, 234), (4, 169), (7, -28), (9, -494), (11, 14), (13, 13), (17, -182), (43, 364)],
  (1, 4): [(1, -3136), (2, -2576), (3, 414), (4, 299), (5, -896), (7, -784), (8, 4256), (9, -874), (10, 4256), (11, 392), (12, -112), (13, 23), (14, -112), (17, -2520), (43, 3780)],
  (1, 6): [(0, 4), (1, -140), (2, -115), (5, -40), (7, -40), (8, 190), (10, 190), (11, 18), (12, -5), (14, -5), (17, -115), (43, 140)],
  (2, 3): [(3, 270), (4, 195), (9, -570), (12, 14), (13, 15), (24, -210), (43, 420)],
  (2, 4): [(3, 810), (4, 585), (9, -1710), (12, 56), (13, 45), (24, -840), (43, 1260)],
  (2, 6): [(3, 270), (4, 195), (9, -570), (12, 23), (13, 15), (24, -345), (43, 420)],
  (5, 3): [(3, 414), (4, 299), (9, -874), (10, 532), (13, 23), (14, -14), (38, -322), (43, 644)],
  (5, 4): [(0, -448), (1, -2240), (2, -3360), (3, 13950), (4, 10075), (5, -6720), (9, -29450), (10, 31920), (11, 224), (12, 224), (13, 775), (14, -840), (38, -15960), (43, 23940)],
  (5, 6): [(0, -1288), (1, -6440), (2, -9660), (3, 31770), (4, 22945), (5, -19320), (9, -67070), (10, 91770), (11, 644), (12, 644), (13, 1765), (14, -2415), (38, -45885), (43, 55860)],
}
assert len(SPARSE_CERTS)==9
def dual_certificate(other,third):
    h=atom(other,third,normalize=True)
    allowed=[k for k,(i,j) in enumerate(V) if j!=3 or i in JA]
    tcol=len(allowed);n=tcol+1+28
    B=[[F(0)]*n for _ in range(44)]
    d=list(b)+[F(0)]*29
    for p,k in enumerate(allowed):
        for r in range(15): B[r][p]=F(A[r][k])
        B[15+k][p]=1
        if k==idx[(1,3)]: B[43][p]=1
    for k in range(28):
        B[15+k][tcol]=h[k]
        B[15+k][tcol+1+k]=-1
    B[43][tcol]=h[idx[(1,3)]]
    y=[F(0)]*44
    for i,coef in SPARSE_CERTS[(other,third)]:y[i]=F(coef)
    products=[sum(y[r]*B[r][k] for r in range(44)) for k in range(n)]
    gap=sum(y[r]*d[r] for r in range(44))
    assert min(products)>=0 and gap<0, (other,third,min(products),gap)
    return gap
for other in (1,2,5):
    for third in (3,4,6):
        gap=dual_certificate(other,third)
        print('ONE_ATOM_EXCLUDED',other,third,'y_dot_b',gap)
X=tuple(map(F,'4257955/58244304,42470639/475661816,16095404/195361103,0,0,0,202668635/32820665304,0,0,196521/2426846,0,0,0,0,0,63830689/475661816,0,377644447/2548188300,1544855/16987922,0,23445955/475661816,65507/101927532,0,3340857/390722206,0,0,2161731/33975844,171431819/9377332944'.split(',')))
t1=F('4023851/1367527721')
t2=F('196521/67951688')
H1=atom(1,6)
H2=atom(2,6)
W=tuple(a+t1*c for a,c in zip(X,H1))
Y=tuple(a+t1*c+t2*d for a,c,d in zip(X,H1,H2))
def check(p,expected):
    assert len(p)==28 and min(p)>=0
    assert all(sum(A[r][k]*p[k] for k in range(28))==b[r] for r in range(15))
    mask=tuple(i for i in range(7) if p[idx[(i,3)]]>0)
    assert mask==tuple(sorted(expected)),(mask,expected)
    return sum(z>0 for z in p)
print('BRIDGE_ENDPOINT_AND_MID_SUPPORT',check(X,JA),check(W,JUNION),check(Y,JC))
assert t1>0 and t2>0
assert all(X[k]+t1*H1[k]==W[k] for k in range(28))
assert all(W[k]+t2*H2[k]==Y[k] for k in range(28))
print('STEP_PARAMETERS',t1,t2)
print('PRIMITIVE_LENGTH_MINIMUM',2)
print('PASS_R5_EXACT_SHARP_TWO_ATOM_A_C_BRIDGE_9_NO_GO_CERTIFICATES')
