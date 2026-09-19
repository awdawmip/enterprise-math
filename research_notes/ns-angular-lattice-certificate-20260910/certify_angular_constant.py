#!/usr/bin/env python3
"""Exact angular lattice certificate. All far frequencies are bounded analytically.
The scalar parent is executed unchanged; its P6 population and symmetry classes
are reused. Floating-point fields in the JSON are display-only.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import contextlib, hashlib, io, json, math, runpy
ROOT=Path(__file__).resolve().parent
PARENT=next((p for p in [ROOT/'scalar_lattice_parent.py', ROOT.parent/'brc-critical-lattice-gram-newton-20260909/certify_lattice_constant.py'] if p.is_file()),None)
if PARENT is None:raise FileNotFoundError('Pinned scalar lattice checker is required')
EXPECTED_BLOB='4551bd83edab7453bda993582eed098cb8073519'
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
if not __debug__:raise RuntimeError('Run without -O; assertions form the certificate')
assert blob(PARENT.read_bytes())==EXPECTED_BLOB
with contextlib.redirect_stdout(io.StringIO()):parent=runpy.run_path(str(PARENT))
P=parent['P'];classes=parent['classes'];A6=parent['A6']
NEAR=F(19383,1000);C_INTERMEDIATE=F(4259,500);C_CS=F(3841,500);C_ANG=F(1521,200)
D=F(1351,1560);EPS=F(1561,10000);RS2=F(707107,1000000);PI=F(355,113)
rows=[];maxsq=F();arg=None
for a,b,c,n in classes:
 k=(a,b,c);raw=F()
 for p,pn in P:
  qn=sum((k[j]-p[j])**2 for j in range(3))
  if not qn:continue
  cross=n*pn-sum(p[j]*k[j] for j in range(3))**2
  assert cross>=0
  raw+=F(cross*(pn+qn),pn*pn*qn*qn)
 assert raw*raw<NEAR*NEAR*n
 value_sq=raw*raw/n
 if value_sq>maxsq:maxsq=value_sq;arg=k
 rows.append({'k':list(k),'K_squared':n,'K_times_near_sum':str(raw)})
# The octahedral moment laws used for all |k|>=13.
for j in range(3):
 assert sum((F(p[j]*p[j],pn*pn)for p,pn in P),F())==A6/3
 assert sum((F(p[j]*p[j],pn)for p,pn in P),F())==F(len(P),3)
for i,j in [(0,1),(0,2),(1,2)]:
 assert sum((F(p[i]*p[j],pn*pn)for p,pn in P),F())==0
 assert sum((F(p[i]*p[j],pn)for p,pn in P),F())==0
large=F(2,3)*(F(13,49)*A6+F(13,2401)*len(P))
assert large<NEAR
# D > sqrt(3)/2, EPS > D/sqrt(6(6-D)), RS2 > 1/sqrt(2).
assert 4*D*D>3 and 0<D<6
assert EPS*EPS*6*(6-D)>D*D
assert 2*RS2*RS2>1
scalar_far=(1+D/6)**4*PI**3
cs_angular_far=scalar_far*(RS2+EPS)**2
angular_far=(1+D/6)**4*(PI**3*(F(1,2)+EPS**2)+4*EPS*PI**2)
assert NEAR+cs_angular_far<C_CS*C_CS
assert angular_far<cs_angular_far
intermediate_sq=NEAR+scalar_far
total=NEAR+angular_far
assert intermediate_sq<C_INTERMEDIATE*C_INTERMEDIATE
assert total<C_ANG*C_ANG
result={
 'status':'PASS','scope':'all nonzero integer outputs; analytic infinite tail, no extrapolation',
 'parent_blob':EXPECTED_BLOB,'parent_executed_unchanged':True,
 'near_points':len(P),'output_classes':len(classes),'near_cap':str(NEAR),
 'max_near_class':list(arg),'max_near_readout':math.sqrt(float(maxsq)),
 'large_output_bound':str(large),'large_output_readout':float(large),
 'cube_radius_upper':str(D),'angular_chord_upper':str(EPS),'inverse_sqrt2_upper':str(RS2),
 'scalar_tail_upper':str(scalar_far),'angular_tail_upper':str(angular_far),
 'scalar_tail_readout':float(scalar_far),'angular_tail_readout':float(angular_far),
 'intermediate_constant':str(C_INTERMEDIATE),'angular_Cauchy_constant':str(C_CS),'certified_constant':str(C_ANG),
 'certified_constant_decimal':float(C_ANG),'total_squared_upper':str(total),
 'total_squared_readout':float(total),'squared_margin':str(C_ANG*C_ANG-total),
 'relative_improvement':str(1-C_ANG/F(9503,1000)),
 'continuum_integrals':{'I0':'pi^3/|k|','I2':'pi^3/(2|k|)','I1_exact':'2*pi^2/|k|'},
 'limits':['C=7.605 is valid, not claimed sharp.','Near arithmetic is exact; continuum-tail proof is in the note.',
           'First argument must be divergence free. Normalized T^3 Fourier convention.',
           'Not independent review or arbitrary-data regularity.'],
 'near_class_certificates':rows}
(ROOT/'output').mkdir(exist_ok=True)
(ROOT/'output/angular_constant.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k!='near_class_certificates'},indent=2))
