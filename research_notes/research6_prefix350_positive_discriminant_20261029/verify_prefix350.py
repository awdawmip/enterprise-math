#!/usr/bin/env python3
"""Exact auxiliary C^3 five-port certificates, no floating point or native X6 claim.

All ordered path pairs retain (port, source_k, source_l) labels.
No trig, pi, matrix exponential or approximated complex phase operations.
"""
from fractions import Fraction as F
from itertools import permutations, combinations, product
from pathlib import Path
import json

def z(a=0,b=0): return (a,b)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def n2(a): return mul(a,conj(a))[0]
def scale(n,a): return (n*a[0],n*a[1])
def vsum(seq):
    v=z()
    for x in seq:v=add(v,x)
    return v

A=[
    [z(4),z(4),z()],
    [z(),z(-4),z(4)],
    [z(-5,3),z(),z(-3,1)],
    [z(-2,-2),z(4,4),z(2,2)],
    [z(-2),z(),z(5,2)],
]
source=[z(4),z(5,-2),z(7,-4)]
raw=[1360,128,2330,1864,1261]
q0=[F(2125,3721),F(200,3721),F(29125,29768),F(5825,7442),F(31525,59536)]
q1=[F(4),F(1),F(1),F(1),F(1)]

def det3(m):
    total=z()
    for pi in permutations(range(3)):
        term=mul(m[0][pi[0]],mul(m[1][pi[1]],m[2][pi[2]]))
        inv=sum(pi[i]>pi[j] for i in range(3) for j in range(i+1,3))
        total=add(total,neg(term) if inv%2 else term)
    return total

minors={"".join(str(i+1) for i in rows):det3([A[i] for i in rows]) for rows in combinations(range(5),3)}
assert len(minors)==10 and all(t!=z() for t in minors.values())
gram=[[vsum(mul(conj(A[j][k]),A[j][l]) for j in range(5)) for l in range(3)] for k in range(3)]
assert gram==[[z(62),z(),z()],[z(),z(64),z()],[z(),z(),z(63)]]

alpha=[z(-39,-4),z(-36,-20),z(5,-9)]
assert all(scale(53,A[0][k])==vsum(mul(alpha[t],A[t+1][k]) for t in range(3)) for k in range(3))
assert [n2(v) for v in alpha]==[1537,1696,106]
assert sum(n2(v) for v in alpha)==3339==63*53

terms=[]
for j in range(5):
    path=[mul(A[j][k],source[k]) for k in range(3)]
    ordered=[]
    for k,l in product(range(3),repeat=2):
        v=mul(path[k],conj(path[l]))
        ordered.append(v)
        terms.append({"port":j+1,"source_k":k+1,"source_l":l+1,"real":v[0],"imag":v[1]})
    assert vsum(ordered)==z(raw[j])
assert len(terms)==45
assert all(q0[j]==F(10,61)**2*F(raw[j],64) for j in range(5))

D=lambda q:q[0]-F(63,53)*(q[1]+q[2]+q[3])
d0,d1=D(q0),D(q1)
assert d0==F(-2502575,1577704)
assert d1==F(23,53)
t0=-d0/(d1-d0)
assert t0==F(2502575,3187239) and 0<t0<1
qt=lambda t:[(1-t)*q0[j]+t*q1[j] for j in range(5)]
qstar=qt(t0)
assert D(qstar)==0
assert q0[3]>F(3,4) and q1[3]>F(3,4)
assert q0[2]<1 and q1[2]<=1
assert qstar[3]>F(3,4) and qstar[2]<=1
assert F(106,1696)==F(1,16)
assert qstar[3]>qstar[2]/16

def as_ratio(x):return f"{x.numerator}/{x.denominator}"
res={
 "status":"PASS_AUTHOR_SIDE_EXACT_AUXILIARY_POSITIVE_DISCRIMINANT_CERTIFICATES",
 "scope":"Auxiliary five-port C^3, no native X6 dynamics or independent Driver review",
 "input_A_gaussian_pairs":A,
 "third_order_minors":minors,
 "gram_diagonal_exact":[62,64,63],
 "gram_full_exact_gaussian_pairs":gram,
 "ordered_source_path_pairs":terms,
 "path_pairs_count":len(terms),
 "raw_intensities":raw,
 "q0":list(map(as_ratio,q0)),
 "q_plus":list(map(as_ratio,q1)),
 "row_identity_alpha_gaussian_pairs":alpha,
 "row_identity_denominator":53,
 "sum_norm_alpha_squared":3339,
 "cauchy_coefficient":as_ratio(F(63,53)),
 "exclusion_gap_at_q_plus":as_ratio(D(q1)),
 "D0":as_ratio(d0),"Dplus":as_ratio(d1),
 "path_exclusion_parameter":as_ratio(t0),
 "D_path_at_t0":as_ratio(D(qstar)),
 "q4_over_q3_at_t0":as_ratio(qstar[3]/qstar[2]),
 "cs_saturation_required_q4_over_q3":as_ratio(F(1,16)),
 "previous_root_box_status":"inherited PREFIX-342 checker separately rerun, not native or independent review",
 "theory_status":"exact no-real-source wedge unconditional; six-real-branch neighborhood and forced real discriminant conditional on PREFIX349 six simple roots and degree-6 proof",
}
Path('RESULTS_PREFIX350.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
print(res['status'])
print('minors=10 nonzero; BRC ordered source-labeled products=45, reference raw=',raw)
print('row identity 53*y1 = (-39-4i)y2 + (-36-20i)y3 + (5-9i)y4')
print('q+=(4,1,1,1,1) excluded, D=',as_ratio(d1))
print('t0=',as_ratio(t0),'(positive intensity segment excluded for t>=t0)')
print('at t0 Cauchy equality would force q4/q3=1/16; actual=',as_ratio(qstar[3]/qstar[2]))
