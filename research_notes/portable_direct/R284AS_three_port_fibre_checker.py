#!/usr/bin/env python3
"""Exact verifier for R284AS three-port principal-minor fibre classification.
Python 3 stdlib only. No floating-point arithmetic and no network access.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from collections import defaultdict
import json

PERMS=list(permutations(range(3)))

def det3(A):
    out=Q(0)
    for p in PERMS:
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term=Q((-1)**inv)
        for i in range(3): term *= A[i][p[i]]
        out += term
    return out

def diagonal_polynomial(A,d):
    T=[[Q(d[i])*(i==j)-A[i][j] for j in range(3)] for i in range(3)]
    return det3(T)

def probe(A,u,v,d,s):
    T=[[Q(d[i])*(i==j)-A[i][j]-(Q(s) if (i,j)==(u,v) else 0) for j in range(3)] for i in range(3)]
    return det3(T)

def invariants(A):
    a=A[0][1]*A[1][2]*A[2][0]
    b=A[0][2]*A[2][1]*A[1][0]
    p12=A[0][1]*A[1][0]
    p23=A[1][2]*A[2][1]
    p13=A[0][2]*A[2][0]
    return (A[0][0],A[1][1],A[2][2],p12,p23,p13,a+b)

def gauge_canonical(A):
    a=A[0][1]*A[1][2]*A[2][0]
    alpha,beta,gamma,p12,p23,p13,s=invariants(A)
    return ((alpha,Q(1),p13/a),(p12,beta,Q(1)),(a,p23,gamma))

def transpose(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))

def one_probe_coeffs(A,u,v):
    w=next(i for i in range(3) if i not in (u,v))
    return A[v][u], A[v][w]*A[w][u]

def reconstruct(A):
    alpha,beta,gamma,p12,p23,p13,z=invariants(A)
    c12,q12=one_probe_coeffs(A,1,0)
    c23,_=one_probe_coeffs(A,2,1)
    b=(p12/c12)*q12
    a=z-b
    c31=a/(c12*c23)
    c21=p12/c12
    c32=p23/c23
    c13=p13/c31
    return ((alpha,c12,c13),(c21,beta,c23),(c31,c32,gamma))

def as_fr(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def main():
    ex_count=0
    grouped=defaultdict(set)
    distinct_two_classes=0
    probes_checked=0
    for vals in product((Q(1),Q(2),Q(3)),repeat=9):
        A=tuple(tuple(vals[i*3+j] for j in range(3)) for i in range(3))
        key=invariants(A)
        K=gauge_canonical(A)
        assert invariants(K)==key
        assert reconstruct(A)==A
        grouped[key].add(K)
        # Three representative ordered interventions; independent exact determinant checks.
        if vals[0] <= Q(2):
            for u,v in ((1,0),(2,1),(0,2)):
                w=next(i for i in range(3) if i not in (u,v))
                c,q=one_probe_coeffs(A,u,v)
                d=(Q(2),Q(3),Q(5)); t=Q(1,7)
                got=probe(A,u,v,d,t)-diagonal_polynomial(A,d)
                assert got == -t*(c*(d[w]-A[w][w])+q)
                probes_checked+=1
        ex_count+=1
    for key, Ks in grouped.items():
        assert len(Ks)<=2
        for K in Ks:
            KT=gauge_canonical(transpose(K))
            assert all(H==K or H==KT for H in Ks)
        if len(Ks)==2:
            distinct_two_classes+=1
    eps=Q(1,100)
    A=tuple(tuple(eps*x for x in row) for row in ((1,2,1),(1,1,2),(2,1,1)))
    AT=transpose(A)
    assert invariants(A)==invariants(AT)
    d=(Q(1),)*3;s=eps
    assert diagonal_polynomial(A,d)==diagonal_polynomial(AT,d)
    gap=probe(A,1,0,d,s)-probe(AT,1,0,d,s)
    assert gap==Q(-3,31250)
    H_A=one_probe_coeffs(A,1,0)
    H_AT=one_probe_coeffs(AT,1,0)
    assert H_A[1]/H_A[0] != H_AT[1]/H_AT[0]
    scale=(Q(1),Q(1),Q(2))
    A_t=tuple(tuple(scale[i]*A[i][j]/scale[j] for j in range(3)) for i in range(3))
    assert A_t != A and invariants(A_t)==invariants(A)
    assert one_probe_coeffs(A_t,1,0)==one_probe_coeffs(A,1,0)
    assert one_probe_coeffs(A_t,2,1)!=one_probe_coeffs(A,2,1)
    assert probe(A_t,1,0,d,s)==probe(A,1,0,d,s)
    assert reconstruct(A_t)==A_t
    output={
      'schema':'R284AS_EXACT_VERIFICATION_V1',
      'status':'PASS',
      'arithmetic':'Python standard library fractions.Fraction; integer determinant expansion',
      'exhaustive_positive_integer_matrices_3x3_entries_1_to_3':ex_count,
      'distinct_diagonal_polynomial_fibres':len(grouped),
      'fibres_containing_two_observed_gauge_classes':distinct_two_classes,
      'max_observed_gauge_classes_in_any_fibre':max(map(len,grouped.values())),
      'exact_two_probe_reconstruction_checks':ex_count,
      'exact_offdiagonal_cofactor_identity_checks':probes_checked,
      'transpose_ambiguity_difference_at_d111_s001':as_fr(gap),
      'one_probe_cannot_recover_all_entries_example':{'scale_diagonal':['1','1','2'],'same_F':True,'same_E21_probe':True,'different_E32_probe':True},
      'limitations':'Finite verification supports the mathematical proof. Independent peer review and native X6 interpretation not performed.',
      'sources':['R284AR_MINIMAL_POSITIVE_TRANSPOSE_OBSERVER_AMBIGUITY_20261119.md','R284AQ_RANK_ONE_DIAGONAL_GAUGE_AND_OFFDIAGONAL_PORT_WITNESSES_20261119.md']
    }
    print(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__': main()
