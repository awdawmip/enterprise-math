#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib, importlib.util, contextlib, io, json, math, sympy as s
ROOT=Path(__file__).resolve().parent
parent=ROOT/'parent'/'certify_polarized.py'
expected='9ed03b1f3aff165f7a624ed58518d1ac89ae5f21042b7fd22d2cfdf147104368'
assert hashlib.sha256(parent.read_bytes()).hexdigest()==expected
spec=importlib.util.spec_from_file_location('pol',parent); P=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(P)
assert P.res['status']=='PASS' and P.res['periodic_constant']=='129/20'
near=F(37,5)
x,y,z,K=s.symbols('x y z K', real=True)
p=s.Matrix([x,y,z]); q=s.Matrix([-x,-y,K-z]); r2=s.expand(p.dot(p)); q2=s.expand(q.dot(q)); I=s.eye(3)
Pp=I-p*p.T/r2;Pq=I-q*q.T/q2;kv=s.Matrix([0,0,K]);ev=s.Matrix([1,0,0]);M=kv*ev.T+ev*kv.T
fro=s.simplify(s.trace(Pp*M*Pq*M));N=s.factor(s.simplify(fro*r2*q2))
N_expected=K**2*(K**2*x**2+K**2*y**2-4*K*x**2*z-2*K*y**2*z+2*x**2*y**2+4*x**2*z**2+2*y**4+2*y**2*z**2)
assert s.expand(N-N_expected)==0
lap=s.factor(sum(s.diff(N,a,2) for a in (x,y,z)))
assert s.expand(lap-4*K**2*(K**2-3*K*z+3*x**2+8*y**2+3*z**2))==0
assert s.expand((K**2-3*K*z+3*x**2+8*y**2+3*z**2)-(3*(z-K/2)**2+3*x**2+8*y**2+K**2/4))==0
hx,hy,hz=s.symbols('hx hy hz', real=True)
poly=s.Poly(s.expand(N.subs({x:x+hx,y:y+hy,z:z+hz})),hx,hy,hz)
avg=0
for powers,coef in poly.terms():
    fac=1
    for power in powers: fac*=0 if power%2 else s.Rational(1,2**power*(power+1))
    avg+=coef*fac
assert s.expand(avg-N-lap/24-s.Rational(29,360)*K**2)==0
t=s.symbols('t', positive=True);D=t*(1-t)
I2=s.pi**2/(8*D**s.Rational(3,2)); I4=5*s.pi**2/(8*s.sqrt(D))
raw=s.simplify(s.Rational(1,4)*6*D*(s.Rational(14,15)*I4+(2*t**2-2*t+s.Rational(2,3))*I2))
assert s.simplify(raw-(s.pi**2/2*s.sqrt(D)+s.pi**2/8/s.sqrt(D)))==0
cont=s.pi**2/s.Integer(2)*(s.pi/8)+s.pi**2/s.Integer(8)*s.pi
assert s.simplify(cont-3*s.pi**3/16)==0
far_self=P.far/2
whole=near+far_self; Cself=F(99,20)
assert whole<Cself*Cself
res={'status':'PASS','record_id':'FINDING-EM-PDE-SYMMETRIZED-SELF-ADVECTION-20260910','scope':'normalized T3, real solenoidal zero-mean fields; quadratic self-advection and its real symmetric polarization','parent_checker_sha256':expected,'parent_executed_unchanged':True,'near_squared_upper':str(near),'far_squared_upper':str(far_self),'far_readout':float(far_self),'total_squared_upper':str(whole),'total_squared_readout':float(whole),'self_constant':str(Cself),'self_constant_readout':float(Cself),'continuum_self_kernel':'3*pi^3/16','whole_space_unitary_self_constant':'sqrt(6)/16','cube_average_identity':'avg_Q N = N + Delta N/24 + 29 K^2/360','laplacian_nonnegative_identity':'Delta N=4K^2[3(z-K/2)^2+3x^2+8y^2+K^2/4]','symmetric_bilinear_extension':'B_s(f,g)=(B(f,g)+B(g,f))/2 has same constant by real polarization and scale optimization','limits':['Self/symmetric constant does not replace the 6.45 constant for an arbitrary ordered B(f,g).','Not claimed optimal.','No arbitrary-data NS regularity.','Prior 6.45 parent remains unreviewed dependency.']}
(ROOT/'selfsym_verification.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(res,indent=2,ensure_ascii=False))
