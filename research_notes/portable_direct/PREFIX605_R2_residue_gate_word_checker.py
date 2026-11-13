#!/usr/bin/env python3
"""PREFIX-605: exact residue-class sufficient statistics for the native X6-BRC 12+4 tail.
Only the frozen native-derived Q(g) operator in PREFIX602 is used.
Standalone native-derived phase observer checker, including original STAR reconstruction.
"""
import json
from pathlib import Path
import sympy as sp

# Reconstruct the exact native-derived 48-phase observer from the frozen
# native X6 STAR/axis/branch specification (as in PREFIX-602/604).
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
assert len(phases)==48 and len(set(phases))==48
index={q:i for i,q in enumerate(phases)}
def successor(i):
    a,p,c=phases[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(index[q] for q in
       ([(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]))
N=[successor(i) for i in range(48)]
g=index[(0,1,-3)]
assert g==4 and g not in N[g]
def Q(gate):
    M=sp.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js:
            M[i,j]=1 if i==g else (3+gate if j==g else 2)
    return M
A=Q(sp.Integer(1)); G=Q(sp.Integer(2))-A
assert G.rank()==1 and G*G==sp.zeros(48)
A2=A*A
cols=list(A2.rref()[1]);assert len(cols)==16
E=A2[:,cols]
rows=list(E.T.rref()[1]);assert len(rows)==16
K=E.extract(rows,range(16)).inv()*sp.eye(48).extract(rows,range(48))
T=K*A*E;H=K*G*E
assert A*E==E*T and G*E==E*H
assert E.shape==(48,16) and K*E==sp.eye(16)
I=sp.eye(16)
assert T**4==16*I and H.rank()==1
r,c=next((i,j) for i in range(16) for j in range(16) if H[i,j]!=0)
u=H[:,c]; h=H[r,:]/H[r,c]
W=sp.Matrix.hstack(u,T*u,T**2*u,T**3*u)
O=sp.Matrix.vstack(h,h*T,h*T**2,h*T**3)
L=(O*W).inv()*O
P=W*L
assert L*W==sp.eye(4) and P**2==P
assert W.rank()==4 and E.rank()==16
assert (I-P)*H==sp.zeros(16) and H*(I-P)==sp.zeros(16)
assert (I-P)*T*P==sp.zeros(16) and P*T*(I-P)==sp.zeros(16)

z=sp.symbols('z')
B=lambda zz: sp.Matrix([[0,0,0,4*(zz+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert L*(T+(z-1)*H)*W==B(z)

def products(gates):
    p=[sp.Integer(1)]*4
    for k,q in enumerate(gates):p[k%4]*=sp.sympify(q)+3
    return tuple(map(sp.expand,p))

def transfer(gates):
    n=len(gates);p=products(gates)
    mat=sp.zeros(4)
    for col in range(4):
        residue=(3-col)%4  # initial coordinate col crosses edge 3->0 at steps residue+1 mod 4
        count=len(range(residue,n,4))
        mat[(col+n)%4,col]=4**count*p[residue]
    return mat

def stepwise(gates):
    out=sp.eye(4)
    for q in gates:out=B(q)*out
    return out

# All-length exact symbolic monomial identity, independently checked on 0..13 symbolic gates.
symbolic_count=0
for n in range(14):
    gates=sp.symbols('q1:'+str(n+1)) if n else ()
    got=stepwise(gates)
    want=transfer(gates)
    assert (got-want).applyfunc(sp.expand)==sp.zeros(4),('symbolic',n)
    symbolic_count+=1

# Exact arbitrary rational gate values and nonstationary 16D/48D BRC observer.
checks=0
seqs=[]
for n in range(15):
    seqs.append(tuple(sp.Rational((7*k+3)%19, (k%3)+1) for k in range(n)))
    seqs.append(tuple(sp.Integer((11*k+5)%13) for k in range(n)))
for gates in seqs:
    assert stepwise(gates)==transfer(gates)
    if len(gates)<=10:
        state=sp.Matrix([i%7+1 for i in range(4)])
        assert transfer(gates)*state==stepwise(gates)*state
    checks+=1

# Smooth endpoint-summary lower bound: independent Jacobian rank min(n,4)
# when 0 < all varying gate values; later parameters are fixed nonnegative.
jacobian_ranks={}
for n in (1,2,3,4,7,10):
    rank=min(n,4)
    vars=sp.symbols('h0:'+str(rank))
    gates=list(vars)+[sp.Integer(2)]*(n-rank)
    proj=sp.Matrix(products(gates))
    J=proj.jacobian(vars)
    assert J.rank()==rank
    jacobian_ranks[str(n)]=int(J.rank())

# Invariant under within-residue permutation; swapping across residues breaks the full operator.
original=(0,2,1,5,3,4,7,6)
within=(3,2,1,5,0,4,7,6) # 1-based positions 1,5 exchanged
across=(2,0,1,5,3,4,7,6) # positions 1,2 exchanged
assert products(original)==products(within)
assert products(original)!=products(across)
assert transfer(original)==transfer(within)
assert transfer(original)!=transfer(across)

# Projection to the authentic 48 native-derived phases after the two transient gates:
# equality must hold for every one-hot original phase input, not a selected output.
def native_tail(gates):
    Z=Q(0)*Q(1)  # original typed BRC-derived first two gates
    for gate in gates:Z=Q(gate)*Z
    return Z
M0=native_tail(original)
M1=native_tail(within)
M2=native_tail(across)
assert M0==M1
assert M0!=M2
nz=[(i,j,int((M0-M2)[i,j])) for i in range(48) for j in range(48) if (M0-M2)[i,j]!=0]
assert nz
example=nz[0]
# Native-to-reduced bridge on all 48 input basis vectors for this specific word.
R=K*Q(0)*Q(1)
assert E*R==Q(0)*Q(1)
assert M0==E*(W*transfer(original)*L+T**(len(original)%4)*16**(len(original)//4)*(I-P))*R
checks+=48*3

out={
  'schema':'PREFIX605_R2_GATE_RESIDUE_WORD_EXACT_V1',
  'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'inherited_native_model':'48 phases; 96 ports; 576 tagged actions; axis weights (1,1,1,1,0,0); gate target 4',
  'source_dependency':'PREFIX602, PREFIX604; native-derived Q(g), E,K,T,H,W,L',
  'exact_identity':'B(q_n)...B(q_1) e_j =4^N_j * product_{t: (t-1)%4=(3-j)%4}(q_t+3) e_{(j+n)%4} (zero-based j)',
  'full_48_phase_operator_equality':'For fixed n after any common two-step transient: iff four residue products agree',
  'symbolic_lengths_verified':symbolic_count,
  'minimal_smooth_endpoint_statistic_jacobian_ranks':jacobian_ranks,
  'rational_integer_sequences_checked':checks-144,
  '48_phase_basis_comparisons':144,
  'baseline_gate_word':original,
  'same_residue_permutation':within,
  'across_residue_permutation':across,
  'example_nonzero_difference':{'row_zero_based':example[0],'input_phase_zero_based':example[1],'baseline_minus_across_value':example[2]},
  'status':'AUTHOR_SIDE_EXACT_PROOF_AND_EXECUTED_CHECKS; INDEPENDENT_REVIEW_PENDING',
  'boundary':'Complete 48 phase linear endpoint readout after the 2-step transient; not a lossless source for typed paths or intermediate-time observations.'
}
path=Path(__file__).with_name('PREFIX605_R2_residue_gate_word_results.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('PREFIX605 PASSED', 'symbolic_lengths', symbolic_count, 'rational_seqs',checks-144,'full_48_tests',144,'counterexample',example)
