#!/usr/bin/env python3
"""PREFIX625 additive universal-horizon rank certificate for native X6-BRC.
Run alongside PREFIX625_native_two_generation_path_checker.py with SymPy.
Reuses the original 48-phase/96-port/576-action operator, frozen science
f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from pathlib import Path
import json
import sympy as S
from PREFIX625_native_two_generation_path_checker import (matrix,actions,R,C,K,Ki,live)

A0=matrix(S.Integer(0)); E=matrix(S.Integer(1))-A0
T=A0*A0; U=A0*E; V=E*A0
assert E*E==S.zeros(96)
G0=T[:,C]; G1=V[:,C]
N0=Ki*(A0*G0)[R,:]
N1=Ki*(A0*G1)[R,:]
# Complete finite coefficient checks imply A(c)G(b)=G(c)(N0+b*N1)
assert A0*G0==G0*N0
assert A0*G1==G0*N1
assert E*G0==G1*N0
assert E*G1==G1*N1==S.zeros(96,16)
assert N0.det(method='bareiss')==49152
assert N1.rank()==1
assert [(i,j,str(N1[i,j])) for i in range(16) for j in range(16) if N1[i,j]!=0]==[(2,7,'1/2')]
assert (N0+N1).det(method='bareiss')==65536
# Affinity follows because N1 has one nonzero matrix entry:
# determinant of (N0+z*N1) = 16384*(z+3) for all scalars z.

# At zero gates, every live source has an outgoing positive edge reaching a
# live port, giving arbitrarily long nonzero source-tagged paths by induction.
positive0=list(actions(S.Integer(0)))
live_set=set(live)
forward={src for dst,src,w,label in positive0 if w>0 and dst in live_set}
assert forward==live_set

D=tuple(sorted(live_set-set(C)))
assert len(D)==48
checks=[]
for gates in ((S.Integer(0),S.Integer(0)),
              (S.Integer(1),S.Integer(1),S.Integer(1)),
              (S.Integer(0),S.Rational(7,3),S.Integer(2),S.Integer(0)),
              (S.Integer(2),S.Integer(1),S.Integer(0),S.Rational(7,3),S.Integer(1)),
              (S.Integer(0),S.Integer(0),S.Integer(0),S.Integer(0),S.Integer(0),S.Integer(0))):
    n=len(gates)
    F=S.eye(96)
    for z in gates: F=matrix(z)*F
    product=S.eye(16)
    for z in reversed(gates[1:-1]): product=product*(N0+z*N1)
    G=G0+gates[-1]*G1
    H=T[R,:]+gates[0]*U[R,:]
    assert F==G*product*Ki*H
    assert F.extract(R,C)==K*product
    expected_det=S.Integer(-65536)
    for z in gates[1:-1]: expected_det *= S.Integer(16384)*(z+3)
    observed_det=F.extract(R,C).det(method='bareiss')
    assert observed_det==expected_det and observed_det!=0
    # Exact input recovery from the same 48 supplementary source readings
    r=S.Matrix([S.Rational((13*i+17)%29+1,i%7+1) for i in range(96)])
    y=F*r
    rec=S.zeros(96,1)
    known_vals=r.extract(D,[0])
    solved=F.extract(R,C).LUsolve(y.extract(R,[0])-F.extract(R,D)*known_vals)
    for idx,j in enumerate(C): rec[j]=solved[idx]
    for j in D: rec[j]=r[j]
    assert all(rec[j]==r[j] for j in live) and F*rec==y
    checks.append({'n':n,'gates':[str(x) for x in gates],'minor_determinant':str(observed_det),'recovery_exact':True})

result={
 'schema':'PREFIX625_NATIVE_X6_ANY_FINITE_HORIZON_RANK16_V1',
 'date':'2026-11-09',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'theorem_domain':'all finite n>=2, all sequences of nonnegative real gates, arbitrary nonnegative precursor 96-port state',
 'endpoint_rank_all_n_ge_2':16,
 'complete_ordered_tagged_path_rank_all_n_ge_1':64,
 'minimal_extra_linear_scalar_precursor_observations_all_n_ge_2':48,
 'same_fixed_extra_source_ports_all_horizons':list(D),
 'fixed_16_minor_rows':list(R),'fixed_16_minor_columns':list(C),
 'minor_formula':'-65536*16384**(n-2)*product_{j=2}^{n-1}(g_j+3)',
 'N0_det':str(N0.det(method='bareiss')),'N1_rank':N1.rank(),
 'N1_only_nonzero_entry':{'row':2,'column':7,'value':'1/2'},
 'det_N_symbolic':'16384*(z+3)',
 'four_complete_96_by_16_coefficient_identity_checks':True,
 'each_live_source_has_positive_live_successor_at_zero_gate':True,
 'exact_positive_rational_horizon_checks':checks,
 'arithmetic':'original typed BRC action arithmetic; exact SymPy rational/integer; no classical surrogate',
 'review':'AUTHOR_SIDE_UNREVIEWED','status':'ALL_ASSERTIONS_PASS'}
out=Path(__file__).with_name('PREFIX625_any_horizon_rank_results.json')
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'endpoint_rank':16,'tagged_path_rank':64,'extra':48,'checked_lengths':[x['n'] for x in checks]},ensure_ascii=False))
