"""Exact rational witness for the five-monomial bypass no-go (author side).
The continuous all-real obstruction is proved in RESEARCH.md, not by this finite test.
"""
from fractions import Fraction as F
from itertools import product


def det(matrix):
    a = [[F(x) for x in row] for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    answer = F(1)
    for i in range(n):
        j = next((j for j in range(i, n) if a[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            a[i], a[j] = a[j], a[i]
            answer = -answer
        pivot = a[i][i]
        answer *= pivot
        for j in range(i + 1, n):
            factor = a[j][i] / pivot
            for k in range(i + 1, n):
                a[j][k] -= factor * a[i][k]
            a[j][i] = F(0)
    return answer


def barycentric(p):
    a, b, c, d, z = p
    return (1-a-z+b, z-b, a-b-c+d, c-d, b-d, d)


def project(p):
    a, b, c, d, z = p
    return (a, b, c, d+z)

FULL = sorted(set((x,x*u,x*vd,x*u*vy,z)
                  for x,u,vd,vy,z in product((0,1), repeat=5)))
LR = sorted(set((x,x*u,x*v,x*u*v,u)
                for x,u,v in product((0,1), repeat=3)))
assert len(FULL) == 14, (len(FULL), FULL)
assert len(LR) == 6, (len(LR), LR)
assert set(LR).issubset(set(FULL))
assert all(sum(barycentric(p)) == 1 for p in FULL + LR)
assert all(min(barycentric(p)) >= 0 for p in LR)
assert det([[F(v[i]) - F(LR[0][i]) for i in range(5)] for v in LR[1:]]) != 0
A=(1,0,0,0,1)
B=(1,1,1,1,0)
C=(1,1,0,1,1)
assert all(q in FULL for q in (A,B,C))
assert barycentric(A) == (-1,1,1,0,0,0)
assert barycentric(B) == (1,-1,0,0,0,1)
assert barycentric(C) == (0,0,1,-1,0,1)

# Four-observer affine example: O=(a,b,c,d+z).
# The signed functional -2*O_3+O_4 retains a gap despite the fifth monomial.
h=lambda p: -2*project(p)[2] + project(p)[3]
hF=max(map(h,FULL))
hL=max(map(h,LR))
assert (hF,hL,hF-hL) == (2,1,1)
assert h(C) == hF
# Four independent projected LR edges certify full affine rank four.
q0=project(LR[0]);rows=[[F(project(q)[i])-F(q0[i]) for i in range(4)] for q in LR[1:5]]
# Rank check over all 4-tuples, since sorted ordering is not a guaranteed basis.
from itertools import combinations
rank_cert = next(det([[F(project(q)[i])-F(q0[i]) for i in range(4)] for q in comb])
                for comb in combinations(LR[1:],4)
                if det([[F(project(q)[i])-F(q0[i]) for i in range(4)] for q in comb]))
assert rank_cert != 0
print('FULL_BINARY_POLYTOPE_VERTICES',len(FULL))
print('LR_BINARY_SIMPLEX_VERTICES',len(LR))
print('A_LAMBDA',barycentric(A))
print('B_LAMBDA',barycentric(B))
print('C_LAMBDA',barycentric(C))
print('SAMPLE_4D_LR_RANK_MINOR',rank_cert)
print('SAMPLE_SUPPORT_FULL_LR_GAP',hF,hL,hF-hL)
print('PASS_EXACT_R5_FIFTH_MONOMIAL_BYPASS_RANK4_NO_GO')
