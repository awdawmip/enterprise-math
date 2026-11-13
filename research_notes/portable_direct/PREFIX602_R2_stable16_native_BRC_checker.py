#!/usr/bin/env python3
"""PREFIX-602 exact native STAR X6-BRC zero-axis 16D tail certificates.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Original native source labels/gates are retained in source Q construction.
The 16D representation is a signed observable coordinate, NOT an all-positive
or provenance-injective native-path carrier.
"""
import json
from pathlib import Path
import sympy as sp
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
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
z=sp.Symbol('z')
def Q(gate):
    M=sp.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js:
            M[i,j]=1 if i==g else ((3+gate) if j==g else 2)
    return M
A=Q(sp.Integer(1)); G=Q(sp.Integer(2))-A
assert G.rank()==1 and G*G==sp.zeros(48)
A2=A*A
cols=list(A2.rref()[1]); assert len(cols)==16
E=A2[:,cols]
rows=list(E.T.rref()[1]); assert len(rows)==16
ER=E.extract(rows,range(16))
K=ER.inv()*sp.eye(48).extract(rows,range(48))
assert K*E==sp.eye(16)
matrices={'A2':A2,'A_G':A*G,'G_A':G*A,'G2':G*G,'A_E':A*E,'G_E':G*E}
inclusions={}
for name,M in matrices.items():
    assert E*(K*M)==M,name
    inclusions[name]={'rank':int(M.rank()),'nonzero_entries':sum(x!=0 for x in M)}
T1=K*A*E; H=K*G*E
assert A*E==E*T1 and G*E==E*H and H.rank()==1
Tz=T1+(z-1)*H
assert Q(z)*E==E*Tz
a,b=sp.symbols('a b')
assert E*(K*(A2+(b-1)*A*G+(a-1)*G*A))==(A2+(b-1)*A*G+(a-1)*G*A)
# Rank-one increments -> selected 16x16 minor is bilinear in a,b.
def minor(qa,qb):return (Q(qa)*Q(qb)).extract(rows,cols).det(method='domain-ge')
dets={f'{i},{j}':str(minor(i,j)) for i in (0,1) for j in (0,1)}
assert dets=={'0,0':str(-2**28*9),'0,1':str(-2**28*12),
              '1,0':str(-2**28*12),'1,1':str(-2**28*16)}
# Rank-one pencil H => entire characteristic polynomial affine in z.
t=sp.Symbol('t')
expect=lambda zz: sp.expand((t**4-16)**3*(t**4-4*zz-12))
for zz in (0,1):
    assert sp.expand((T1+(zz-1)*H).charpoly(t).as_expr()-expect(zz))==0
assert sp.simplify(Tz.det()-2**14*(z+3))==0
assert sum(v!=0 for v in Tz)==36
assert sum(v!=0 for v in E)==72
K_nnz=sum(x!=0 for x in K)
sequences=((0,2,1,5,3,0),(1,0,2,4,1,7),(2,3,0,1,0,6))
inputs=[sp.eye(48)[:,j] for j in range(48)]+[
 sp.ones(48,1), sp.Matrix([j%5 for j in range(48)]),
 sp.Matrix([(7*j+3)%11 for j in range(48)])]
comparisons=0
for gates in sequences:
    for v0 in inputs:
        y0=Q(gates[0])*v0
        y2=Q(gates[1])*y0
        w=K*y2
        assert E*w==y2
        for gg in gates[2:]:
            y2=Q(gg)*y2
            w=(T1+(gg-1)*H)*w
            assert E*w==y2
            comparisons+=1
result={
 'schema':'PREFIX602_R2_NATIVE_BRC_STABLE_16_V1',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'axis_weights':[1,1,1,1,0,0],
 'phase_count':48,'native_ports':96,'typed_native_actions':576,'gate_target':g,
 'basis_source':'E=16 pivot columns of Q(1)^2, deterministic zero-based ordering',
 'basis_cols':cols,'basis_rows':rows,
 'V_dim':16,'common_inclusions':inclusions,
 'G_rank':1,'G_square_zero':True,
 'two_step_minor_formula':'-2^28*(a+3)*(b+3)',
 'two_step_minor_grid':dets,
 'T_characteristic_polynomial':'(t^4-16)^3*(t^4-4*z-12)',
 'T_determinant':'2^14*(z+3)',
 'Tz_nonzero_entries':36,'E_nonzero_entries':72,'K_nonzero_entries':K_nnz,
 'sequences':sequences,'exact_full_phase_comparisons':comparisons,
 'scope':'arbitrary nonnegative gate sequence after two steps, full 48-phase tail output; positive 96-port bridge from PREFIX596 only',
 'warning':'T has negative entries; signed exact linear coordinate, not a positive native-path replacement or typed-branch history equivalent',
 'status':'AUTHOR_SIDE_EXACT_CHECKS_PASSED; DRIVER_REVIEW_PENDING'}
path=Path(__file__).with_name('PREFIX602_R2_stable16_native_BRC_results.json')
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('CERTIFICATE PASSED','rank',16,'Tnnz',36,
      'full_phase_checks',comparisons,'minor_grid',dets)
