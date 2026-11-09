#!/usr/bin/env python3
"""Exact native X6-BRC rank-16 inverse suffix pullback; pinned f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from fractions import Fraction as F
import importlib.util, pathlib, json
import sympy as s
p=pathlib.Path(__file__).with_name('PREFIX628_R2_full_suffix_checker.py')
spec=importlib.util.spec_from_file_location('native',str(p))
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
R=[0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54]
C=[0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68]
A0=s.zeros(96,96);E=s.zeros(96,96)
for dst,src,w,gated in native.A:
 if gated:E[dst,src]+=1
 else:A0[dst,src]+=int(w)
T=A0*A0;K=T.extract(R,C);V=E*A0
assert K.det()==-65536
G0=T[:,C];G1=V[:,C];Kinv=K.inv()
N0=Kinv*(A0*G0)[R,:];N1=Kinv*(A0*G1)[R,:]
assert len([v for v in N1 if v])==1 and N1[2,7]==s.Rational(1,2)
z=s.Symbol('z')
assert s.simplify((N0+z*N1).det()-16384*(z+3))==0
assert G0.extract(R,list(range(16)))==K
assert G1.extract(R,list(range(16)))==s.zeros(16,16)
assert A0*G0==G0*N0 and A0*G1==G0*N1
assert E*G0==G1*N0 and E*G1==G1*N1
def to_frac(xx):return tuple(F(int(v.p),int(v.q)) for v in xx)
def pullback(state,gate_previous):
 g=s.Rational(gate_previous.numerator,gate_previous.denominator)
 u=Kinv*s.Matrix([s.Rational(state[r].numerator,state[r].denominator) for r in R])
 x=(N0+g*N1).inv()*u
 return to_frac((G0+g*G1)*x)
tests=[]
for n,L in ((6,1),(6,2),(7,3),(9,3),(12,3),(18,5)):
 lam=F(5,3);gates=tuple(F(k%5+1,(k%3)+1) for k in range(1,n+1))
 states=native.evolve(gates,lam);r=tuple(states[-1])
 for k in range(n-1,n-L-1,-1):
  r=pullback(r,gates[k-1])
  assert r==tuple(states[k])
 tests.append({'n':n,'L':L,'pullback_steps':L,'all_96_ports_exact':True})
U=N0.inv();rank=s.simplify((N1*U).trace())
assert rank==s.Rational(1,3)
for g in (s.Rational(0),s.Rational(1),s.Rational(2),s.Rational(7,3)):
 direct=(N0+g*N1).inv()
 fast=U-(g/(1+g/3))*(U*N1*U)
 assert direct==fast
res={'schema':'PREFIX628_R2_NATIVE_16_STATE_BACKWARDS_PULLBACK','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','test_cases':tests,'rank_one_trace':str(rank),'determinant':'16384*(z+3)','fixed_K_determinant':str(K.det()),'status':'ALL_ASSERTIONS_PASS'}
pathlib.Path(__file__).with_name('PREFIX628_R2_16state_pullback_results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'status':res['status'],'tests':len(tests),'pullback_steps':sum(a['L'] for a in tests),'rank_one_trace':res['rank_one_trace']}))
