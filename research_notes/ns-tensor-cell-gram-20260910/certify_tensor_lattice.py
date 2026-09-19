#!/usr/bin/env python3
"""All-mode tensor lattice bound: exact finite core and analytic centered-cube tail.
NumPy/SciPy are NOT used for proof acceptance. See RESEARCH_NOTE.md for the analytic proof.
"""
from fractions import Fraction as F
from pathlib import Path
import math,json,time,hashlib,runpy,contextlib,io
ROOT=Path(__file__).resolve().parent
if not __debug__:raise RuntimeError('Assertions required')
PAR=ROOT/'parent';start=time.monotonic()
assert hashlib.sha256((PAR/'certify_angular_constant.py').read_bytes()).hexdigest()=='40d41ab035fd4be7b6c271f3cb0144c9a4c2042e4268940c96613c240de89a50'
with contextlib.redirect_stdout(io.StringIO()): old=runpy.run_path(str(PAR/'certify_angular_constant.py'))
P=old['P'];A6=old['old'].A6
PI=F(355,113);delta=F(1351,1560);scale=1+delta/6
SCALAR=F(1339,200);CSTAR=F(6447,1000);NEAR=F(737,100);K0=17
scalar_far=scale**6*PI**3/2
assert 10+scalar_far<SCALAR**2
classes=[(a,b,c)for a in range(K0) for b in range(a,K0) for c in range(b,K0) if 0<a*a+b*b+c*c<K0*K0]
def mul(A,B):return [[sum((A[i][r]*B[r][j]for r in range(3)),F())for j in range(3)]for i in range(3)]
def trace(A):return sum((A[i][i]for i in range(3)),F())
def eig_below(t,d,n,b):
    # Two transverse eigenvalues are (t +- sqrt(d))/2.
    assert t>=0 and d>=0 and 4*b*b*n>t*t
    left=4*b*b*n+t*t-d
    assert left>0 and left*left>16*b*b*n*t*t
maxread=-1;maxdata=None
print('Inherited disjoint-near check passed. Exact tensor classes:',len(classes),flush=True)
for num,k in enumerate(classes):
 n=sum(x*x for x in k);T0=[[F()for j in range(3)]for i in range(3)];total=F()
 for p,pn in P:
  q=tuple(k[j]-p[j]for j in range(3));qn=sum(x*x for x in q)
  if not qn:continue
  cross=pn*n-sum(p[j]*k[j]for j in range(3))**2
  assert cross>=0
  if not cross:continue
  w=F(cross,pn*pn*qn);w2=F(cross,pn*qn*qn)if qn>=36 else F()
  total+=w+w2;f1=w/qn;f2=w2/pn
  for i in range(3):
   for j in range(i,3):T0[i][j]-=f1*q[i]*q[j]+f2*p[i]*p[j]
 for i in range(3):
  T0[i][i]+=total
  for j in range(i):T0[i][j]=T0[j][i]
 pk=[[F(i==j)-F(k[i]*k[j],n)for j in range(3)]for i in range(3)]
 T=mul(mul(pk,T0),pk)
 assert all(T[i][j]==T[j][i]for i in range(3)for j in range(3))
 assert all(sum(T[i][j]*k[j]for j in range(3))==0 for i in range(3))
 tr=trace(T);dis=2*trace(mul(T,T))-tr*tr;eig_below(tr,dis,n,NEAR)
 read=(float(tr)+math.sqrt(max(0,float(dis))))/(2*math.sqrt(n))
 if read>maxread:maxread=read;maxdata={'k':k,'trace_exact':str(tr),'discriminant_exact':str(dis)}
 if (num+1)%100==0:print('Checked',num+1,'tensor output classes',flush=True)
large=F(2,3)*(F(K0,(K0-6)**2)*A6+F(894*K0,(K0-6)**4));assert large<NEAR
far=scale**8*3*PI**3/8;whole=NEAR+far;assert whole<CSTAR*CSTAR
assert F(1,12)==F(2,3)*F(1,2)**3
assert F(1,80)==F(2,5)*F(1,2)**5
import sympy as s
assert s.simplify(s.beta(s.Rational(3,2),s.Rational(3,2)).rewrite(s.gamma)-s.pi/8)==0
radial=s.pi**s.Rational(3,2)*s.gamma(s.Rational(7,2))*s.gamma(s.Rational(1,2))/(s.gamma(s.Rational(3,2))*s.gamma(4))
assert s.simplify(radial-5*s.pi**2/8)==0
assert s.Rational(4,15)*s.Rational(5,8)*6*s.Rational(1,8)==s.Rational(1,8)
result={'status':'PASS','record_id':'FINDING-EM-PDE-TENSOR-CELL-GRAM-20260910',
 'scope':'normalized T3; mean zero; BOTH inputs solenoidal for tensor constant',
 'scalar_first_input_only_constant':str(SCALAR),'scalar_far_upper':str(scalar_far),
 'near_lattice_points':len(P),'tensor_output_radius_cutoff':K0,'tensor_output_classes':len(classes),
 'tensor_near_upper':str(NEAR),'near_maximum_readout':maxread,'near_maximum_exact_data':maxdata,
 'large_output_bound':str(large),'large_output_readout':float(large),
 'cube_side':1,'cube_covariance':'I/12','cube_fourth_moment':'1/80',
 'far_rational_upper':str(far),'far_readout':float(far),
 'complete_squared_upper':str(whole),'complete_squared_upper_readout':float(whole),
 'certified_constant':str(CSTAR),'certified_constant_readout':float(CSTAR),
 'strict_squared_margin':str(CSTAR*CSTAR-whole),
 'previous_canonical_constant':'1521/200','reduction_fraction':str(1-CSTAR/F(1521,200)),
 'continuum_transverse_scalar':'pi^3/2','continuum_both_solenoidal_tensor':'3*pi^3/8',
 'infinite_tail':'centered PSD numerator cell average plus uniform denominator distortion',
 'proof_acceptance':'Fraction comparisons, exact gamma identities, analytic all-mode proof; no float eigenvalue acceptance',
 'PDE_simulation':False,'independent_review':False,'optimal_constant_claim':False,'elapsed_seconds':time.monotonic()-start}
(ROOT/'tensor_lattice_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS all modes C=',CSTAR,'squared=',float(whole),'time=',time.monotonic()-start,flush=True)
