#!/usr/bin/env python3
"""All-mode symmetric convection polarization bound.
Exact near-field matrices, positive quartic cube average, analytic continuum tail.
No floating-point quantity is used as an acceptance predicate.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import contextlib, importlib.util, io, hashlib, json, math, time
import sympy as s
ROOT=Path(__file__).resolve().parent
if not __debug__:raise RuntimeError('Assertions must remain enabled')
source=next((p for p in [ROOT/'parent'/'parent'/'certify_angular_constant.py', ROOT.parent/'ns-tensor-cell-gram-20260910'/'parent'/'certify_angular_constant.py'] if p.is_file()),None)
if source is None:raise FileNotFoundError('Pinned angular checker is required')
assert hashlib.sha256(source.read_bytes()).hexdigest()=='40d41ab035fd4be7b6c271f3cb0144c9a4c2042e4268940c96613c240de89a50'
spec=importlib.util.spec_from_file_location('angular_parent',source)
Pmod=importlib.util.module_from_spec(spec)
t0=time.monotonic()
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(Pmod)
print('Parent checker rerun unchanged: PASS',flush=True)
P=Pmod.P; A6=Pmod.old.A6
BOUND=F(71,20);K0=24;scale=10**12
classes=[(a,b,c) for a in range(K0) for b in range(a,K0) for c in range(b,K0) if 0<a*a+b*b+c*c<K0*K0]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
maxread=(0.,None);mindet=None
for index,k in enumerate(classes):
 nk=dot(k,k)
 u=(-k[1],k[0],0) if k[0] or k[1] else (1,0,0)
 z=cross(k,u);su=dot(u,u);sz=dot(z,z)
 assert dot(k,u)==dot(k,z)==dot(u,z)==0 and sz==nk*su
 rad=F();t11=F();t12=F();t22=F()
 for p,np in P:
  q=tuple(ki-pi for ki,pi in zip(k,p));nq=dot(q,q)
  if not nq:continue
  cross2=np*nk-dot(p,k)**2
  if not cross2:continue
  multiplicity=1+int(nq>=36)
  d1=dot(p,u);d2=dot(p,z);den=4*np*np*nq*nq
  pk=dot(p,k);qk=nk-pk
  rad+=F(multiplicity*cross2*(np+nq),den)
  coeff=2*multiplicity*(cross2+pk*qk)
  t11+=F(coeff*d1*d1,den)
  t12+=F(coeff*d1*d2,den)
  t22+=F(coeff*d2*d2,den)
 KL=F(isqrt(nk*scale*scale),scale);assert KL*KL<=nk
 diag1=(BOUND*KL-rad)*su+t11;diag2=(BOUND*KL-rad)*sz+t22
 determinant=diag1*diag2-t12*t12
 assert diag1>0 and diag2>0 and determinant>0,(k,diag1,diag2,determinant)
 if mindet is None or determinant<mindet:mindet=determinant
 a=float(rad-t11/su);c=float(rad-t22/sz);b=-float(t12)/math.sqrt(su*sz)
 eig=(a+c+math.hypot(a-c,2*b))/(2*math.sqrt(nk))
 if eig>maxread[0]:maxread=(eig,k)
 if index%100==0:print('Exact near matrices',index+1,'/',len(classes),flush=True)
large=F(2,3)*(F(K0,(K0-6)**2)*A6+F(K0,(K0-6)**4)*len(P))
assert large<BOUND
# Exact rotated-cube identity; sign follows from the invariant proof in the note.
x,y,z0=s.symbols('x y z',real=True);h=s.symbols('h0:3',real=True)
mom=lambda n:s.Rational(1,(n+1)*2**n) if n%2==0 else s.S(0)
def cubeavg(poly):
 pol=s.Poly(s.expand(poly),*h);return s.expand(sum(coef*math.prod(mom(n) for n in powers) for powers,coef in pol.terms()))
k=s.Matrix([1,2,2]);zz=s.Matrix([2,-1,0]);pp=s.Matrix([x,y,z0]);hh=s.Matrix(h)
AA=(k.dot(k))*s.eye(3)-k*k.T;BB=zz.dot(zz)*s.eye(3)-zz*zz.T
q1=lambda v:(v.T*AA*v)[0];q2=lambda v:((v-k).T*BB*(v-k))[0]
expr=cubeavg(q1(pp+hh)*q2(pp+hh))-q1(pp)*q2(pp)
expected=q1(pp)*s.trace(BB)/12+q2(pp)*s.trace(AA)/12+(pp.T*AA*BB*(pp-k))[0]/3+cubeavg((hh.T*AA*hh)[0]*(hh.T*BB*hh)[0])
assert s.expand(expr-expected)==0
assert k.dot(zz)==0 and AA*BB==BB*AA
rad=s.simplify(s.Rational(8,15)*4*s.pi*s.Rational(1,2)*s.gamma(s.Rational(7,2))*s.gamma(s.Rational(1,2))/s.gamma(4))
I4=s.simplify(6*rad*s.gamma(s.Rational(3,2))**2/s.gamma(3))
assert rad==s.pi**2/3 and I4==s.pi**3/4
transverse=s.simplify(s.pi**3/2-I4/2)
assert transverse==3*s.pi**3/8
# Symmetric cross integral vanishes exactly after the Feynman shift.
jx=s.simplify(s.Rational(1,3)*4*s.pi*s.Rational(1,2)*s.gamma(s.Rational(5,2))*s.gamma(s.Rational(3,2))/s.gamma(4))
jxz=s.simplify(s.Rational(1,15)*4*s.pi*s.Rational(1,2)*s.gamma(s.Rational(7,2))*s.gamma(s.Rational(1,2))/s.gamma(4))
assert jx==jxz==s.pi**2/24
sym_transverse=s.simplify(transverse/2-3*(jx-jxz)*s.gamma(s.Rational(3,2))**2/s.gamma(3))
assert sym_transverse==3*s.pi**3/16
# Exact Gram identity for a rational non-collinear pair.
pp=s.Matrix([1,1,0]);qq=s.Matrix([1,0,2]);kk=pp+qq
proj=lambda a:s.eye(3)-a*a.T/(a.dot(a))
Pk=proj(kk);Pp=proj(pp);Pq=proj(qq)
pa=Pp*kk;qa=Pq*kk
TT=s.zeros(3,9)
for i in range(3):
 for aa in range(3):
  for bb in range(3):TT[i,3*aa+bb]=(pa[aa]*(Pk*Pq)[i,bb]+qa[bb]*(Pk*Pp)[i,aa])/2
cross2=pp.dot(pp)*kk.dot(kk)-pp.dot(kk)**2
pt=Pk*pp
expected=(cross2*(pp.dot(pp)+qq.dot(qq))*Pk-2*(cross2+pp.dot(kk)*qq.dot(kk))*pt*pt.T)/(4*pp.dot(pp)*qq.dot(qq))
assert s.simplify(TT*TT.T-expected)==s.zeros(3)
# Polynomial sum-of-squares in a frame adapted to k and the output polarization.
xx,yy,tt,KK=s.symbols('xx yy tt KK',real=True)
poly=(xx*xx+yy*yy)*(2*(xx*xx+yy*yy)+tt*tt+(KK-tt)**2)-2*((xx*xx+yy*yy)+tt*(KK-tt))*xx*xx
sos=2*(xx*yy)**2+2*yy**4+(xx*(2*tt-KK))**2+(yy*tt)**2+(yy*(KK-tt))**2
assert s.expand(poly-sos)==0
ar=1+Pmod.old.SQRT3_UPPER/12
far=ar**8*F(3,16)*Pmod.old.PI_UPPER**3;whole=BOUND+far
constant=F(909,200)
assert whole<constant**2
out={'status':'PASS','scope':'classical normalized T3; BOTH inputs zero-mean and solenoidal','constant':str(constant),'constant_readout':float(constant),'operator':'Bs(f,g)=(B(f,g)+B(g,f))/2; NOT the ordered B estimate','near_matrix_upper':str(BOUND),'near_points':len(P),'output_cutoff':K0,'exact_output_classes':len(classes),'near_max_diagnostic':maxread,'large_output_scalar_bound':str(large),'large_output_readout':float(large),'far_upper':str(far),'far_readout':float(far),'squared_total_upper':str(whole),'squared_total_readout':float(whole),'quartic_cell_identity_checked':True,'quartic_cell_nonnegativity':'SOS; each affine orthogonal product has unchanged cube mean; Jensen','continuous_matrix':'(3*pi^3/16)*P_k','R3_constant':'sqrt(6)/16 with unitary Fourier normalization','R3_squared_constant':'3/128','cross_integral': '0; cancellation after the Feynman shift','exact_Gram_identity':True,'positive_SOS_cell_identity':True,'limiting_matrix_statement':'Ms(k)-(3*pi^3/16)P_k -> 0 in operator norm; analytical Riemann-sum proof','parent_checker_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'parent_reexecuted_unchanged':True,'no_PDE_sampling':True,'independent_review':False,'elapsed_seconds':time.monotonic()-t0}
(ROOT/'symmetric_verification.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('PASS',json.dumps({k:out[k] for k in ['constant','exact_output_classes','near_max_diagnostic','far_readout','squared_total_readout','elapsed_seconds']}),flush=True)
