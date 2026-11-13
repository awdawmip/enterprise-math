#!/usr/bin/env python3
"""PREFIX-606: exact, all-gate nonnegative 16-state BRC tail realization.

The original 48-phase native-derived Q(z) is reconstructed from its
four STAR triads, 96 input ports, and 576 tagged actions (phase quotient).
The 16 column rays are specified by a fixed nonoverlapping tiling of the
positive support of Q(1)^2. No approximate optimization occurs in checks.
"""
import json
from functools import reduce
from math import gcd
from pathlib import Path
import sympy as sp

SCIENCE_PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
assert len(phases)==48 and len(set(phases))==48
indices={x:i for i,x in enumerate(phases)}
def successor(i):
    a,p,c=phases[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(indices[x] for x in
        [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)])
N=[successor(i) for i in range(48)]
g=indices[(0,1,-3)]
assert g==4 and g not in N[g]

def Q(z):
    M=sp.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js:
            M[i,j]=1 if i==g else (3+z if j==g else 2)
    return M

S=Q(0);G=Q(1)-S; A=Q(1);M=A*A
assert G.rank()==1 and G*G==sp.zeros(48)
assert M.rank()==16

# Exact rank-one support rectangles, 0-based original native phase indices.
# Each pair (R,C) contains 3 row indices and 3 column indices.
RECTANGLES=[
 ([4,5,29],[32,40,44]),
 ([7,30,31],[10,18,22]),
 ([25,36,37],[0,9,33]),
 ([27,38,39],[2,11,35]),
 ([0,1,13],[21,36,45]),
 ([24,25,37],[12,21,45]),
 ([2,3,15],[23,38,47]),
 ([1,12,13],[9,24,33]),
 ([17,40,41],[4,8,20]),
 ([26,27,39],[14,23,47]),
 ([5,28,29],[8,16,20]),
 ([16,17,41],[28,32,44]),
 ([6,7,31],[34,42,46]),
 ([18,19,43],[30,34,46]),
 ([19,42,43],[6,10,22]),
 ([3,14,15],[11,26,35]),
]
assert len(RECTANGLES)==16
support=set((i,j) for i in range(48) for j in range(48) if M[i,j]!=0)
rectsupport=set()
E=sp.zeros(48,16)
D=sp.zeros(16,48)
for k,(R,C) in enumerate(RECTANGLES):
    cells={(i,j) for i in R for j in C}
    assert len(cells)==9 and not rectsupport.intersection(cells)
    rectsupport.update(cells)
    assert all(M[i,j]>0 for i,j in cells)
    block=M.extract(R,C)
    assert block.rank()==1
    raw=[int(M[i,C[0]]) for i in R]
    scale=reduce(gcd,raw)
    for i in R: E[i,k]=M[i,C[0]]/scale
    for j in C: D[k,j]=M[R[0],j]/E[R[0],k]
assert rectsupport==support and len(rectsupport)==144
assert E*D==M and E.rank()==16
assert all(bool(x.is_Integer) and x>=0 for x in E)
assert all(bool(x.is_Integer) and x>=0 for x in D)

# K is an auxiliary algebraic left inverse, not an input/output observer.
pivot_rows=list(E.T.rref()[1]);assert len(pivot_rows)==16
K=E.extract(pivot_rows,range(16)).inv()*sp.eye(48).extract(pivot_rows,range(48))
assert K*E==sp.eye(16)

# Two-step nonnegative input encoder, affine in both gate parameters:
# R(a,b) = R00 + a Ra + b Rb, for Q(a)Q(b).
R00=K*S*S
Ra=K*G*S
Rb=K*S*G
assert G*G==sp.zeros(48)
assert E*R00==S*S and E*Ra==G*S and E*Rb==S*G
for Z in (R00,Ra,Rb):
    assert all(x>=0 and bool(x.is_Integer) for x in Z)

# Common 16-state nonnegative transfer: T(z)=T0+z H.
T0=K*S*E
H=K*G*E
assert S*E==E*T0 and G*E==E*H
assert all(x>=0 and bool(x.is_Integer) for x in T0)
assert all(x>=0 and bool(x.is_Integer) for x in H)
assert sum(x!=0 for x in T0)==16
assert sum(x!=0 for x in H)==1
assert len(set(j for i in range(16) for j in range(16) if T0[i,j]))==16
assert len(set(i for i in range(16) for j in range(16) if T0[i,j]))==16
assert all((T0+z*H).rank()==16 for z in (0,1,2,sp.Rational(3,2)))

# Native input/output exact reconstruction on different nonstationary gate words.
# Gate word [z1,...,zn] acts as Q(zn)...Q(z1).
words=[(0,0), (1,1), (2,3), (sp.Rational(1,2),sp.Rational(7,3)),
       (0,1,2,4), (2,0,5,1,3), (3,1,4,1,5,9,2,6),
       tuple(sp.Rational((5*k+3)%17,(k%3)+1) for k in range(13))]
checks=0
for word in words:
    native=Q(word[1])*Q(word[0])
    compact=E*(R00+word[1]*Ra+word[0]*Rb)
    assert native==compact
    checks+=48  # checks all original 48 input basis vectors
    for z in word[2:]:
        native=Q(z)*native
        compact=E*(T0+z*H)*K*compact  # K E = I, exact for this reachable state
        assert native==compact
        checks+=48
    # Equivalently, propagate only 16 coordinates for one mixed positive input.
    v=sp.Matrix([((11*i+3)%13)+1 for i in range(48)])
    c=(R00+word[1]*Ra+word[0]*Rb)*v
    for z in word[2:]: c=(T0+z*H)*c
    assert native*v==E*c
    assert all(x>=0 for x in c)

nnz=lambda X:sum(int(x!=0) for x in X)
result={
 'schema':'ENTERPRISE_MATH_PREFIX606_POSITIVE_16_TAIL_EXACT_V1',
 'scientific_pin':SCIENCE_PIN,
 'scope':'Original 48-phase native-derived BRC Q(z), axis weights (1,1,1,1,0,0); nonnegative phase input; arbitrary variable z>=0; full 48-phase output at horizons >=2',
 'model':{'native_phases':48,'native_ports':96,'tagged_actions':576,'gate_target_phase':g},
 'positive_realization':{'dimension':16,'E_nonzero':nnz(E),'T0_nonzero':nnz(T0),'H_nonzero':nnz(H),
  'R00_nonzero':nnz(R00),'Ra_nonzero':nnz(Ra),'Rb_nonzero':nnz(Rb),'M_nonzero':nnz(M),
  'M_rank':M.rank(),'E_rank':E.rank(),'rectangles':RECTANGLES,'pivot_rows':pivot_rows,
  'T0_entries':[(i,j,int(T0[i,j])) for i in range(16) for j in range(16) if T0[i,j]],
  'H_entries':[(i,j,int(H[i,j])) for i in range(16) for j in range(16) if H[i,j]],
  'all_integer_and_nonnegative':True},
 'verified_exact':{'two_step_factorization_coefficients':3,'transition_intertwining_coefficients':2,
  'phase_basis_output_comparisons':checks,'gate_words':len(words),
  'word_lengths':[len(w) for w in words],'arithmetic':'SymPy exact integer/rational'},
 'minimality':'rank Q(1)^2=16 implies every linear 48-output realization after two steps has dimension>=16',
 'research_status':'AUTHOR_SIDE_EXACT_PROOF_AND_EXECUTED_CHECKS; INDEPENDENT_REVIEW_PENDING'
}
out=Path(__file__).with_name('PREFIX606_R2_positive16_exact_results.json')
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PREFIX606 PASSED; rank',M.rank(), 'all-gate positive 16D; phase basis checks',checks,
      'sparse nz',nnz(T0),nnz(H),'input nz',nnz(R00),nnz(Ra),nnz(Rb))
