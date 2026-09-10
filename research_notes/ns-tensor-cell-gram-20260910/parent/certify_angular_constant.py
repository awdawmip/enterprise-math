#!/usr/bin/env python3
"""Exact finite angular lattice certificate, plus analytic all-frequency tail.

The PDE reduction, large-output bound, and cube/Riesz proof are in RESEARCH_NOTE.md.
No finite Fourier truncation is substituted for the infinite lattice sum.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import contextlib, hashlib, importlib.util, io, json, math

ROOT=Path(__file__).resolve().parent
if not __debug__: raise RuntimeError('Do not disable proof assertions with -O')
parent=next((p for p in [ROOT/'inherited_lattice.py',ROOT.parent/'brc-critical-lattice-gram-newton-20260909'/'certify_lattice_constant.py'] if p.is_file()),None)
if parent is None:raise FileNotFoundError('Pinned lattice checker dependency is required')
data=parent.read_bytes()
assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()=='4551bd83edab7453bda993582eed098cb8073519'
spec=importlib.util.spec_from_file_location('inherited_lattice',parent)
old=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(old)
P=old.P
assert len(P)==894

# Cubic symmetry identities, checked exactly; no isotropic continuum replacement.
for i in range(3):
 for j in range(3):
  T=sum((F(p[i]*p[j],n*n) for p,n in P),F())
  U=sum((F(p[i]*p[j],n) for p,n in P),F())
  assert T==(old.A6/3 if i==j else 0)
  assert U==(F(len(P),3) if i==j else 0)

NEAR=F(10); CSTAR=F(159,20); K0=16
classes=[(a,b,c,a*a+b*b+c*c) for a in range(K0) for b in range(a,K0)
         for c in range(b,K0) if 0<a*a+b*b+c*c<K0*K0]
max_square=F(); max_k=None; max_sum=None
for a,b,c,nk in classes:
 k=(a,b,c);rad=F()
 for p,np in P:
  nq=sum((k[j]-p[j])**2 for j in range(3))
  if nq==0: continue
  pk=sum(p[j]*k[j] for j in range(3));cross2=np*nk-pk*pk
  assert cross2>=0
  # First summand: |p|<6. Second: |q|<6, |p|>=6, after relabelling.
  rad+=F(cross2,np*np*nq)
  if nq>=36: rad+=F(cross2,np*nq*nq)
 val_square=rad*rad/nk
 assert val_square<NEAR*NEAR
 if val_square>max_square:max_square,max_k,max_sum=val_square,k,rad

# For K>=16, both K/(K-6)^2 and K/(K-6)^4 are decreasing.
large=F(2,3)*(F(K0,(K0-6)**2)*old.A6+F(K0,(K0-6)**4)*len(P))
assert large<NEAR
# Independently check the rational pi upper bound by the Machin identity.
def atan_interval(x, pairs=5):
 lower=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(2*pairs)),F())
 upper=lower+x**(4*pairs+1)/F(4*pairs+1)
 return lower,upper
l5,u5=atan_interval(F(1,5));l239,u239=atan_interval(F(1,239))
pi_lo=16*l5-4*u239;pi_hi=16*u5-4*l239
assert 3<pi_lo<pi_hi<old.PI_UPPER
assert old.SQRT3_UPPER**2>3
far=(1+old.SQRT3_UPPER/12)**4*old.PI_UPPER**3
whole=NEAR+far
assert whole<CSTAR*CSTAR

# Exact vanishing of the retained geometric factor on every tested collinear pair.
collinear=0
for a in range(-6,7):
 for b in range(-6,7):
  if a*b*(a+b)==0:continue
  p=(a,a,0);q=(b,b,0);k=tuple(x+y for x,y in zip(p,q))
  assert sum(x*x for x in p)*sum(x*x for x in k)-sum(x*y for x,y in zip(p,k))**2==0
  collinear+=1

result={
 'status':'PASS', 'scope':'classical normalized T3, f divergence-free; all Fourier frequencies',
 'inherited_source_git_blob':'4551bd83edab7453bda993582eed098cb8073519',
 'inherited_checker_executed_unchanged':True,
 'angular_kernel':'sum_{p!=0,k} |p cross k|^2/(|k| |p|^4 |k-p|^2)',
 'near_union_disjoint':True,'near_radius':6,'near_points':len(P),
 'output_radius_cutoff':K0,'output_symmetry_classes':len(classes),
 'near_upper':str(NEAR),'near_max_class':max_k,
 'near_max_radial_sum':str(max_sum),'near_max_readout':math.sqrt(float(max_square)),
 'large_output_upper':str(large),'large_output_readout':float(large),
 'far_upper':str(far),'far_upper_readout':float(far),
 'all_mode_squared_upper':str(whole),'all_mode_squared_upper_readout':float(whole),
 'certified_constant':str(CSTAR),'certified_constant_readout':float(CSTAR),
 'constant_reduction_fraction':str(1-CSTAR/old.CSTAR),
 'constant_reduction_readout':float(1-CSTAR/old.CSTAR),
 'tensor_symmetry_identities_exact':True,'collinear_checks':collinear,
 'pi_upper_checked_by_Machin':True,'Machin_pi_upper':str(pi_hi),
 'tail':'all remaining pairs have both radii >=6; analytic cube comparison plus Riesz integral',
 'limits':['No sharpness claim.','No arbitrary-data regularity.','Not independently reviewed.',
           'Angular structure retained only in the finite near part; far part is a scalar majorant.']}
(ROOT/'angular_constant_verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2,ensure_ascii=False))
