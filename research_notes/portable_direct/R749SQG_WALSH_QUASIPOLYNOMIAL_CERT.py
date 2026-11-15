#!/usr/bin/env python3
"""R749SQG exact pole certificates for the inherited Walsh 23-source slack model.
Uses only Python stdlib integer and Fraction arithmetic; local independent check.
"""
from fractions import Fraction as Q
from math import comb, prod
import json

MULT={1:3,2:4,3:6,4:4,5:3,6:2,7:1}
WEIGHTS=[w for w,m in MULT.items() for _ in range(m)]
assert len(WEIGHTS)==23 and sum(WEIGHTS)==79
T=420

def multiply(a,b,L):
    out=[Q(0) for _ in range(L)]
    for i,v in enumerate(a[:L]):
        if not v:continue
        for j,w in enumerate(b[:L-i]):
            if w:out[i+j]+=v*w
    return out

def invert(a,L):
    assert a[0]
    out=[Q(1,a[0])]
    for n in range(1,L):
        out.append(-sum((a[j]*out[n-j] for j in range(1,min(n+1,len(a)))),Q(0))/a[0])
    return out

def at_one_factor(s,L):
    return [Q((-1)**j*comb(s,j+1)) if j<s else Q(0) for j in range(L)]

def at_minus_one_odd(s,L):
    return [Q(2) if j==0 else Q((-1)**j*comb(s,j)) if j<=s else Q(0) for j in range(L)]

G=[Q(1)]+[Q(0)]*23
for s in WEIGHTS:
    G=multiply(G,invert(at_one_factor(s,24),24),24)
H=[Q(1)]+[Q(0)]*9
H=multiply(H,invert([Q(2),Q(-1)],10),10)
for s in WEIGHTS:
    factor=at_one_factor(s,10) if s%2==0 else at_minus_one_odd(s,10)
    H=multiply(H,invert(factor,10),10)
W=prod(s for s in WEIGHTS)
A=Q(1,9*2**28)
assert G[0]==Q(1,W) and G[1]==Q(28,W), (G[0],G[1])
assert H[0]==A and H[1]==35*A, (H[0],H[1])

def P(r):
    return sum((g*comb(r+22-j,23-j) for j,g in enumerate(G)),Q(0))
def Q2(r):
    return sum((h*comb(r+8-j,9-j) for j,h in enumerate(H)),Q(0))

def source_counts(R):
    v=[0]*(R+1)
    v[0]=1
    for s in WEIGHTS:
        for d in range(s,R+1):v[d]+=v[d-s]
    c=[]
    total=0
    for d in range(R):
        total+=v[d]
        c.append(total)
    return c

# Check exact degree-7 remainder after stripping singularities at 1, -1.
# For each residue modulo 420, the 8th forward 420-step difference vanishes.
R=9*T
C=source_counts(R)
remainder=[Q(c)-P(i+1)-(-1)**i*Q2(i+1) for i,c in enumerate(C)]
for residue in range(T):
    arr=[remainder[residue+j*T] for j in range(9)]
    assert sum((-1)**(8-j)*comb(8,j)*arr[j] for j in range(9))==0,residue

poles={d:sum(m for w,m in MULT.items() if w%d==0) for d in range(1,8)}
assert poles=={1:23,2:10,3:8,4:4,5:3,6:2,7:1}
# At z=1 an extra cumulative-sum factor contributes 1 to pole order.
assert W==94058496000 and T==420
examples={}
for r in (1,4,8,10,20,40,80,120,420,840,1680,3780):
    examples[str(r)]={'C_r':str(C[r-1]),'P23':str(P(r)),
        'parity_Q9_signed':str((-1)**(r-1)*Q2(r)),
        'remaining_roots':str(remainder[r-1])}

out={
 'schema':'R749SQG_WALSH_SLACK_QUASIPOLYNOMIAL_V1', 'status':'PASS',
 'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'source_prior':'R749SQF@f52082a0613cdf4a3b88841467437ca30dd05d0d',
 'model':'auxiliary 16-atom Walsh source model, 23 positive-slack source letters, uniform source multisets',
 'weights_multiplicity':{str(s):m for s,m in MULT.items()},
 'period':T, 'weighted_product':str(W),
 'root_of_unity_pole_orders':{str(d):m+(d==1) for d,m in poles.items()},
 'pole_at_one': {'G_0':str(G[0]),'G_1':str(G[1]),'P_degree':23,
                 'leading_r23':'1/(23!*94058496000)',
                 'r22':'39/(22!*94058496000)'},
 'pole_at_minus_one': {'H_0':str(H[0]),'H_1':str(H[1]),'Q_degree':9,
                       'r9':'1/(9!*2415919104)','r8':'39/(8!*2415919104)'},
 'full_P23_binomial_coefficients':[str(v) for v in G],
 'full_Q9_binomial_coefficients':[str(v) for v in H],
 'exact_lattice_check':{'r_range':'1..3780','arithmetic':'integer + Fraction (no floats)',
      'residue_classes':420,'exact_420_step_eighth_difference_zero':True},
 'examples':examples,
 'theorem_scope':'AUTHOR_EXACT_NOT_REVIEWED; conditional on R749SQF weights; Laurent pole identity proves all r>=1; finite test is consistency check'
}
print(json.dumps(out,indent=2,ensure_ascii=False))
