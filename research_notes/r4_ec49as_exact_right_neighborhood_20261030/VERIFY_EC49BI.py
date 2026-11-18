#!/usr/bin/env python3
"""EC49BI exact Gaussian-rational check; auxiliary labeled BRC observer, not native BRC.
No floats, numpy, SymPy, random numbers, or physics interpretation.
"""
from fractions import Fraction as Q
from itertools import product
import json

ZERO=(Q(0), Q(0)); ONE=(Q(1), Q(0)); I=(Q(0),Q(1))
def g(a=0,b=0):return (Q(a),Q(b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(q,a):return (q*a[0],q*a[1])
def summ(xs):
    out=ZERO
    for a in xs:out=add(out,a)
    return out
def show(a):return [str(a[0]),str(a[1])]

def P(eta,u,w):return Q(1,2)+(2*u-1)*(1-w)*eta
def observe(eta,A):return tuple(summ(scale(P(eta,u,w),A[w]) for w in range(3)) for u in (0,1))
def K(r,v,u):return Q(1,2)*(1+r if v==u else 1-r)
def residual(A):return add(sub(A[0],scale(2,A[1])),A[2])
def diff(A):return sub(A[0],A[2])
def reconstruct(eta,B,R):
    assert eta>0
    S=add(B[0],B[1]); D=scale(Q(1)/(2*eta),sub(B[1],B[0]))
    A1=scale(Q(1,3),sub(S,R))
    A0=scale(Q(1,6),add(add(scale(2,S),R),scale(3,D)))
    A2=scale(Q(1,6),sub(add(scale(2,S),R),scale(3,D)))
    return (A0,A1,A2)
def diag(d,A):return tuple(mul(d[j],A[j]) for j in range(3))

n=(ONE,g(-2),ONE)
A=(ONE,ZERO,ONE)
Ap=(add(ONE,I),g(0,-2),add(ONE,I))
D=(ONE,I,g(-1))

test_etas=[Q(0),Q(1,8),Q(1,4),Q(1,2)]
for eta in test_etas:
    assert observe(eta,n)==(ZERO,ZERO)
    assert observe(eta,A)==observe(eta,Ap)==(ONE,ONE)

# Rank-2 inversion is exact for all nonzero tested etas and all deliberately varied amplitude triples.
inputs=[A,Ap,n,(g(Q(3,5),Q(-2,7)),g(-7,4),g(Q(4,3),Q(5,6)))]
reconstruction_checks=0
for eta in test_etas[1:]:
    for X in inputs:
        assert reconstruct(eta,observe(eta,X),residual(X))==X
        reconstruction_checks+=1

# A single residual coordinate is insufficient at eta=0: m lies in kernel of observation AND of R.
m=(ONE,ZERO,g(-1))
assert observe(Q(0),m)==(ZERO,ZERO) and residual(m)==ZERO
assert diff(m)==g(2)

# Blackwell simulation identity in Q (rational checks; proof symbolic in manuscript).
garbling_checks=0
for hi in test_etas[1:]:
    for lo in test_etas:
        if lo>hi:continue
        r=lo/hi
        for v,w in product((0,1),range(3)):
            assert P(lo,v,w)==sum(P(hi,u,w)*K(r,v,u) for u in (0,1))
            garbling_checks+=1
        for X in inputs:
            target=observe(lo,X)
            source=observe(hi,X)
            for v in (0,1):
                assert target[v]==summ(scale(K(r,v,u),source[u]) for u in (0,1))

# Explicit witness for noncommutation with a branch-dependent Gaussian-unit operation.
eta=Q(1,4)
before=observe(eta,A); before_alt=observe(eta,Ap)
after=observe(eta,diag(D,A)); after_alt=observe(eta,diag(D,Ap))
assert before==before_alt==(ONE,ONE)
assert after==(g(Q(-1,2)),g(Q(1,2)))
assert after_alt==(g(Q(1,2),Q(-1,2)),g(Q(3,2),Q(1,2)))
assert residual(A)==g(2) and residual(Ap)==g(2,6)

# Verify the general diagonal-descend necessity on a finite spanning grid:
# if diag(d)*n belongs to span(n), it requires d0=d1=d2 (proved symbolically in manuscript).
def in_kernel_nonzero_eta(X):return observe(Q(1,4),X)==(ZERO,ZERO)
diag_examples=[(ONE,ONE,ONE),(ONE,I,g(-1)),(g(2),g(2),g(2)),(g(1),g(2),g(1))]
for d in diag_examples:
    assert in_kernel_nonzero_eta(diag(d,n))==(d[0]==d[1]==d[2])

report={
 "case":"EC49BI auxiliary signed/complex BRC observer sufficiency",
 "arithmetic":"Gaussian rationals Q(i) represented by pairs of Python fractions; exact equality",
 "eta_witness":"1/4",
 "present_A":[show(x) for x in before],
 "present_Aprime":[show(x) for x in before_alt],
 "future_A":[show(x) for x in after],
 "future_Aprime":[show(x) for x in after_alt],
 "provenance_R_A":show(residual(A)),
 "provenance_R_Aprime":show(residual(Ap)),
 "garbling_scalar_equalities":garbling_checks,
 "nonzero_eta_exact_reconstruction_instances":reconstruction_checks,
 "eta0_second_lost_mode":"(1,0,-1) gives O_0=0, R=0, but A0-A2=2",
 "universal_proof_basis":"symbolic S,D,R formulas and ker-invariance criterion; finite program checks examples only",
 "result":"PASS"
}
print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
