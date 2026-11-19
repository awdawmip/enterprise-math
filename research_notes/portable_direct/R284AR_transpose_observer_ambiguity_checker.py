#!/usr/bin/env python3
"""Exact smallest nongauge diagonal-Port observer ambiguity check (stdlib only)."""
from fractions import Fraction as F
from itertools import permutations, product
import json

def det(A):
    n = len(A)
    ans = F(0)
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F(-1 if inv % 2 else 1)
        for i in range(n):
            term *= A[i][p[i]]
        ans += term
    return ans

def pencil(C, d, s=0):
    n = len(C)
    A = [[(d[i] if i == j else F(0)) - C[i][j] for j in range(n)] for i in range(n)]
    A[1][0] -= s
    return A

def run():
    # Every 2x2 positive integer matrix has its gauge class determined by diagonal and bc.
    groups = {}
    for a,b,c,d in product(range(1,5), repeat=4):
        groups.setdefault((a,d,b*c), []).append((a,b,c,d))
    gauge_pairs = 0
    for group in groups.values():
        for M,N in product(group, repeat=2):
            a,b,c,d=M; a2,b2,c2,d2=N
            assert a==a2 and d==d2 and b*c==b2*c2
            # Gauge S=diag(lambda,1), lambda=b2/b, then c2=c/lambda.
            lam=F(b2,b)
            assert F(c)/lam==c2
            gauge_pairs += 1
    e=F(1,100)
    A=[[1,2,1],[1,1,2],[2,1,1]]
    C=[[e*x for x in row] for row in A]
    Ct=[[C[j][i] for j in range(3)] for i in range(3)]
    assert det(C)==4*e**3
    assert max(sum(row) for row in C)<1 and max(sum(row) for row in Ct)<1
    assert A[0][1]*A[1][2]*A[2][0]==8
    assert A[1][0]*A[2][1]*A[0][2]==1
    count=0
    for d in product((F(1),F(2),F(3)), repeat=3):
        baseline=det(pencil(C,d)); baseline_t=det(pencil(Ct,d))
        expected=d[0]*d[1]*d[2]-e*(d[0]*d[1]+d[0]*d[2]+d[1]*d[2])-e**2*sum(d)-4*e**3
        assert baseline==baseline_t==expected
        for s in (F(0),e,2*e):
            diff=det(pencil(C,d,s))-det(pencil(Ct,d,s))
            assert diff==e*s*(4*e-d[2])
            count+=1
    assert det(pencil(C,[F(1)]*3,e))==F(969497,1000000)
    assert det(pencil(Ct,[F(1)]*3,e))==F(969593,1000000)
    return {
        'record':'R284AR', 'status':'PASS', 'arithmetic':'exact Python Fraction + Leibniz',
        'two_by_two_positive_integer_matrices':256,
        'two_by_two_same_principal_minors_gauge_pair_checks':gauge_pairs,
        'three_by_three_exact_full_diagonal_probe_grid':27,
        'three_by_three_offdiagonal_probe_grid':count,
        'rank_three_example_determinant':str(det(C)),
        'directed_cycle_product_forward':8,
        'directed_cycle_product_reverse':1,
        'diagonal_det_at_identity':'30303/31250',
        'E21_probe_s':'1/100',
        'response_C':'969497/1000000',
        'response_C_transpose':'969593/1000000',
        'response_difference':'-3/31250'
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
