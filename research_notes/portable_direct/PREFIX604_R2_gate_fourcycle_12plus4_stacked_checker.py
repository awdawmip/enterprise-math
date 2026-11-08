#!/usr/bin/env python3
"""Exact 12+4 simultaneous split of PREFIX-602's typed native X6-BRC 16D tail.
Requires PREFIX602_R2_stable16_native_BRC_checker.py in the same directory.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d
"""
import json, runpy
from pathlib import Path
import sympy as sp

source = runpy.run_path(str(Path(__file__).with_name('PREFIX602_R2_stable16_native_BRC_checker.py')))
T,H,E,K,Q = (source[key] for key in ('T1','H','E','K','Q'))
I = sp.eye(16)
assert H.rank()==1 and T**4==16*I
J = H*T-T*H
assert J.rank()==2
r,c = next((i,j) for i in range(16) for j in range(16) if H[i,j]!=0)
u = H[:,c]
h = H[r,:]/H[r,c]
assert H==u*h
W = sp.Matrix.hstack(u,T*u,T**2*u,T**3*u)
O = sp.Matrix.vstack(h,h*T,h*T**2,h*T**3)
M=O*W
assert M == sp.Matrix([[0,0,0,4],[0,0,4,0],[0,4,0,0],[4,0,0,0]])
assert M.det()==256
L=M.inv()*O
P=W*L
Z=sp.Matrix.hstack(*O.nullspace())
assert Z.cols==12 and W.row_join(Z).rank()==16
for m in (P*P-P,(I-P)*T*P,P*T*(I-P),(I-P)*H,H*(I-P)):
    assert m==sp.zeros(16)
assert O*T*Z==sp.zeros(4,12)
assert O*H*Z==sp.zeros(4,12)
z=sp.symbols('z')
B=L*(T+(z-1)*H)*W
assert B==sp.Matrix([[0,0,0,4*(z+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
a,b,c,d=sp.symbols('a b c d')
assert B.subs(z,d)*B.subs(z,c)*B.subs(z,b)*B.subs(z,a)==sp.diag(4*(d+3),4*(c+3),4*(b+3),4*(a+3))
rank_H=[sp.Matrix.hstack(*[T**i*H for i in range(k)]).rank() for k in range(1,5)]
rank_J=[sp.Matrix.hstack(*[T**i*J for i in range(k)]).rank() for k in range(1,4)]
assert rank_H==[1,2,3,4] and rank_J==[2,3,4]
assert sp.Matrix.hstack(W,J).rank()==4
# Full 48-phase observer checks from the exact two-step native-derived tail.
seqs=((),(0,),(2,1),(0,2,1,5),(2,0,4,1,3),(5,0,2,1,7,3,0,2),(1,2,3,4,5,0,7,2,9,1,3,6,0))
inputs=[sp.eye(48)[:,j] for j in range(48)]+[sp.ones(48,1),sp.Matrix([j%5 for j in range(48)]),sp.Matrix([(7*j+3)%11 for j in range(48)])]
checks=0
for gates in seqs:
    for v0 in inputs:
        y=Q(0)*Q(1)*v0
        v=K*y
        assert E*v==y
        w=L*v
        f=(I-P)*v
        Bproduct=sp.eye(4)
        for k,gate in enumerate(gates,1):
            y=Q(gate)*y
            v=(T+(gate-1)*H)*v
            Bproduct=B.subs(z,gate)*Bproduct
            fastv=W*Bproduct*w+16**(k//4)*(T**(k%4))*f
            assert v==fastv and E*fastv==y
            checks+=1
assert checks==1683
result={
 'schema':'PREFIX604_R2_GATE_FOURCYCLE_SPLIT_EXACT_V1',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'fixed_axis_weights':[1,1,1,1,0,0],
 'native_port_count':96,'native_tagged_actions':576,'phase_count':48,
 'full_phase_tail_dimension':16,'gate_sensitive_dimension':4,'gate_independent_dimension':12,
 'M_det':256,'H_reachability_ranks':rank_H,'J_reachability_ranks':rank_J,
 'B(z)':'[[0,0,0,4(z+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]]',
 'four_step_formula':'4*diag(z4+3,z3+3,z2+3,z1+3)',
 'gate_free_fourth_power':'T|Z^4=16I',
 'rank_two_order_defect_future_closure':4,
 'full_48_phase_exact_comparisons':checks,
 'scope':'After 2-step typed-native phase transient: arbitrary nonnegative gate sequences, complete 48-phase linear observer',
 'source_preservation':'Original tagged native paths and 96-bit-port history retain separate source carrier',
 'status':'AUTHOR_SIDE_EXACT_VERIFICATION; INDEPENDENT_REVIEW_PENDING',
}
Path(__file__).with_name('PREFIX604_R2_gate_fourcycle_12plus4_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('PREFIX604 PASSED exact 12+4 split', 'full_phase_checks=',checks,'detM=',M.det())
