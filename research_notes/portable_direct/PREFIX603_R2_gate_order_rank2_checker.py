#!/usr/bin/env python3
"""Exact native X6-BRC variable gate ordering defect; preserves phased source.
Depends on PREFIX602_R2_stable16_native_BRC_checker.py, which rebuilds
48 original phase successors from frozen 96-port/576-action substrate.
"""
import json, runpy
from pathlib import Path
import sympy as sp
p=Path(__file__).with_name('PREFIX602_R2_stable16_native_BRC_checker.py')
s=runpy.run_path(str(p))
A,G,E,K,T1,H,Q=s['A'],s['G'],s['E'],s['K'],s['T1'],s['H'],s['Q']
C=G*A-A*G
J=H*T1-T1*H
assert G*G==sp.zeros(48) and H*H==sp.zeros(16)
assert C.rank()==2 and J.rank()==2
assert C*E==E*J
assert sum(v!=0 for v in C)==12
assert sum(v!=0 for v in J)==5
a,b=sp.symbols('a b')
assert Q(a)*Q(b)-Q(b)*Q(a)==(a-b)*C
# Exact nonnegative stable-image source witness, 10th column of E.
k=9
v=E[:,k]
assert all(q>=0 for q in v)
d=(Q(2)*Q(1)-Q(1)*Q(2))*v
assert d==C*v
assert [(i,int(d[i])) for i in range(48) if d[i]!=0]==[(3,4),(14,4),(15,4)]
assert sum(d)==12
assert (T1+H)*T1[:,k]-T1*(T1+H)[:,k]==J[:,k]
checks=0
for aa,bb in [(0,1),(2,1),(1,3),(5,0)]:
    for source in range(48):
        e=sp.eye(48)[:,source]
        assert (Q(aa)*Q(bb)-Q(bb)*Q(aa))*e==(aa-bb)*C*e
        checks+=1
result={
'schema':'PREFIX603_R2_TYPED_BRC_GATE_ORDER_DEFECT_V1',
'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'fixed_axes':[1,1,1,1,0,0],
'gate_order_identity':'Q(a)Q(b)-Q(b)Q(a)=(a-b)*(GA-AG)',
'full_phase_commutator_rank':2,'full_phase_commutator_nnz':12,
'stable_16_commutator_identity':'J=HT1-T1H, (GA-AG)E=EJ',
'stable_16_commutator_rank':2,'stable_16_commutator_nnz':5,
'G_squared_zero':True,'H_squared_zero':True,
'witness_stable_basis_index':k,'native_origin_source_phase_index':s['cols'][k],
'witness_gate_pair':[2,1],
'witness_full_phase_difference':[[i,int(d[i])] for i in range(48) if d[i]!=0],
'witness_full_phase_total_difference':12,
'exact_finite_source_gate_pair_checks':checks,
'scope':'native zero-axis 48-phase observer and its exact 16D stable compression, arbitrary real a,b algebraically; native BRC gates >=0; time/order not identified with physical heartbeat interval',
'warning':'Gate sequence order is observable; same gate multiset does not determine phase output or total mass. Not individual path provenance reconstruction.',
'status':'AUTHOR_SIDE_EXACT_ALGEBRA_AND_CHECKS_PASSED; DRIVER_REVIEW_PENDING'}
Path(__file__).with_name('PREFIX603_R2_gate_order_rank2_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('PREFIX603 CERTIFICATE PASSED','rank2 on 48 and 16',
      'witness',result['witness_full_phase_difference'],'sum',sum(d))
