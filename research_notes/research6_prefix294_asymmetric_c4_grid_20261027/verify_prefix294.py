#!/usr/bin/env python3
"""PREFIX-294: exact ordered-source C4-BRC checks and determinant certificates.

This program checks a declared auxiliary Q(i) BRC source model.  It does not
simulate the native X6 H_n detector or physical time dynamics.
"""
import itertools
import json
from math import isqrt

ZERO = (0, 0)
ONE = (1, 0)
I = (0, 1)

def add(x, y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0], -x[1])
def scale(x, n): return (n*x[0], n*x[1])
def conj(x): return (x[0], -x[1])
def mul(x, y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def norm(x): return x[0]*x[0] + x[1]*x[1]
def summ(xs):
    v=ZERO
    for x in xs: v=add(v,x)
    return v

def rows(q):
    """Six BRC provenance rows, all numerators of common denominator 8."""
    q2=mul(q,q)
    return [
        [(4,0),scale(q,4),ZERO],
        [ZERO,(-4,0),scale(q,4)],
        [(4,0),mul((1,1),q),mul((5,1),q2)],
        [(4,0),mul((-5,-1),q),mul((-1,-1),q2)],
        [(4,0),ZERO,scale(q2,-4)],
        [ZERO,scale(q,2),scale(q2,2)],
    ]

def ordered_brc(row, a, b):
    """Sum all nine ordered source-leg pairs before observing their result."""
    x=[mul(u,v) for u,v in zip(row,a)]
    y=[mul(u,v) for u,v in zip(row,b)]
    return summ(mul(j,conj(k)) for j in x for k in y)

def hdet(a,b,c,u,v,w):
    """Hermitian 3x3 determinant for offdiagonals (01,02,12)."""
    return a*b*c + 2*mul(mul(u,w),conj(v))[0] - a*norm(w) - b*norm(v) - c*norm(u)

def sum_two_integer_squares(n):
    """Exact finite decision for n >= 0, not a numerical approximation."""
    for x in range(isqrt(n)+1):
        y2=n-x*x
        y=isqrt(y2)
        if y*y==y2:return (x,y)
    return None

PHASES=[ONE,I,(-1,0),(0,-1)]
S=[ZERO, ONE, (-1,0), I, (0,-1), (1,1)]
bin_reads=0
pairs=0
mass_checks=0
basis_gram_checks=0
min_loss_at_basis_certificates=[]
for q in PHASES:
    R=rows(q)
    basis=[(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE)]
    for j in range(3):
        for k in range(3):
            value=summ(ordered_brc(row,basis[j],basis[k]) for row in R)
            assert value == ((64 if j==k else 0),0), (q,j,k,value)
            basis_gram_checks+=1
    for a in itertools.product(S,repeat=3):
        Z=sum(norm(x) for x in a)
        observed=[ordered_brc(row,a,a) for row in R]
        assert all(z[1]==0 and z[0]>=0 for z in observed)
        assert sum(z[0] for z in observed)==64*Z
        # sixth row retains exactly the rank-one leakage of PREFIX-293.
        q2=mul(q,q)
        leakage_leg=add(mul(q,a[1]),mul(q2,a[2]))
        assert observed[5][0]==4*norm(leakage_leg)
        assert observed[5][0]*8<=64*Z  # sharp L <= 1/8
        mass_checks+=1
        bin_reads+=6
        pairs+=6*9
    witness=(ZERO,conj(q),conj(mul(q,q)))
    mass=ordered_brc(R[5],witness,witness)[0]
    z=sum(norm(x) for x in witness)
    assert (mass,z)==(16,2), (q,mass,z)
    min_loss_at_basis_certificates.append({'phase':str(q),'leak_numerator':mass,'input_norm':z})

# For D=8 and leakage norm strictly below 2/64, the residual integer
# Hermitian matrix must be diagonal with entries 0 or 1.  All seven possible
# nonzero patterns contradict the Gaussian determinant norm condition.
H=((3,-1,0),(-1,2,1),(0,1,3))
possible_det=[]
for v in itertools.product((0,1), repeat=3):
    if not any(v):continue
    a,b,c=48-v[0],32-v[1],48-v[2]
    d=hdet(a,b,c,(-16,0),ZERO,(16,0))
    assert d>0
    assert sum_two_integer_squares(d) is None,(v,d)
    possible_det.append({'residual_diagonal':list(v),'det_8sqG_minus_diag':d,'sum_two_squares':False})

q=I
R=rows(q)
a=(ONE,I,ONE)
b=(ONE,(-0,-1),ONE)
ZA=sum(norm(x) for x in a)
ZB=sum(norm(x) for x in b)
e_a=sum(ordered_brc(row,a,a)[0] for row in R[:2])
e_b=sum(ordered_brc(row,b,b)[0] for row in R[:2])
assert (e_a,64*ZA,e_b,64*ZB)==(0,192,128,192)

out={
 'schema':'ENTERPRISE_MATH_PREFIX294_EXACT_CHECK_V1',
 'status':'PASS',
 'scope':'auxiliary C4 Q(i) ordered-source BRC model; linear five-bin contractions with fixed J0,J1',
 'source_pin':'enterprise-math@42bb3b9183ba71e95e90722769274ee1d9a446d7',
 'global_pin':'chatgpt-global-knowledge@93755c1673bf4ba017acc56f5a7608a8cc730409',
 'input_set': 'each of three source positions in {0,1,-1,i,-i,1+i}',
 'phase_cases':len(PHASES),
 'input_packets_per_phase':len(S)**3,
 'input_phase_cases':mass_checks,
 'direct_brc_bin_readouts':bin_reads,
 'ordered_source_pair_products':pairs,
 'cross_input_standard_basis_gram_checks':basis_gram_checks,
 'residual_rank_one_witnesses':min_loss_at_basis_certificates,
 'denominator':8,
 'universal_lower_bound_worst_leak':'1/32',
 'reference_constructor_worst_leak':'1/8',
 'seven_determinant_obstructions':possible_det,
 'phase_partner_event_probs':['0','2/3'],
 'native_detector_run':False,
 'formal_independent_review':False
}
print(json.dumps(out,ensure_ascii=False,indent=2))
