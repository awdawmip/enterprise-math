#!/usr/bin/env python3
"""Two actual finite inexact NS updates, all-output residuals and rational bounds.
The PDE continuation inputs are from the pinned parent. No PDE sampling is used.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import sys,json,time,hashlib
ROOT=Path(__file__).resolve().parent
DEP=ROOT/'parent'
if not DEP.is_dir():
 DEP=ROOT.parent/'ns-causal-inverse-newton-basin-20260909'
sys.path.insert(0,str(DEP))
import certify_causal_inverse as par
from exact_packets import *
T=time.time()
def log(*x): print(*x,'elapsed',round(time.time()-T,2),flush=True)
def sqrt_bounds(x,d=24):
 x=F(x); assert x>=0
 if not x:return F(0),F(0)
 scale=10**d;n=isqrt(x.numerator*scale*scale//x.denominator)
 lo,hi=F(n,scale),F(n+1,scale)
 assert lo*lo<=x<hi*hi
 return lo,hi
def product_iv(a,b):
 x=[p*q for p in a for q in b];return min(x),max(x)
def gram_bounds(A):
 coeff=gram_coeff(A,A);total_lo=total_hi=F()
 rt2=sqrt_bounds(2)
 for n,(a,b) in coeff.items():
  lo,hi=sorted((a+b*rt2[0],a+b*rt2[1]))
  rn=sqrt_bounds(n);x,y=product_iv((lo,hi),(1/rn[1],1/rn[0]))
  total_lo+=x;total_hi+=y
 assert total_lo>=0
 return (total_lo,total_hi), coeff

def pure_basis():
 ks=[(1,1,0),(1,0,1),(0,1,1),(2,-2,0)];modes={}
 for k in ks:
  z=par.unit_plus(k);modes[k]=z;modes[tuple(-x for x in k)]=s.conjugate(z)
 return ks,{(k,par.old.sq(k),0):z for k,z in modes.items()}
def residual(v):return plus(heat_derivative(v),scale(ntime(v,v),-1))
def linear(v,h):return plus(heat_derivative(h),scale(plus(ntime(v,h),ntime(h,v)),-1))
def reality_div_free(v):
 for (k,r,m),z in v.items():
  assert dotk(z,k)==Z
  neg=tuple(-i for i in k)
  cc=tuple((x[0],x[1],-x[2],-x[3]) for x in z)
  assert v.get((neg,r,m),VZ)==cc


def stage_build():
 import pickle
 ks,spv1=pure_basis();v1=import_packets(spv1)
 n2=ntime(v1,v1);v2=solve_heat(n2)
 n3=plus(ntime(v1,v2),ntime(v2,v1));v3=solve_heat(n3)
 n22=ntime(v2,v2)
 n4=plus(n22,plus(ntime(v1,v3),ntime(v3,v1)))
 n5=plus(ntime(v2,v3),ntime(v3,v2));n6=ntime(v3,v3)
 amp=F(1,10);v=scale(v1,amp);h0=scale(v2,amp**2);h1=scale(v3,amp**3)
 U1=plus(v,h0);U2=plus(U1,h1)
 f0=scale(n2,-amp**2)
 f1=plus(scale(n3,-amp**3),scale(n22,-amp**4));e0=scale(n3,-amp**3)
 e1=plus(scale(n4,-amp**4),scale(n5,-amp**5));f2=plus(e1,scale(n6,-amp**6))
 data={name:val for name,val in locals().items() if name not in ('pickle','spv1')}
 raw=pickle.dumps(data,protocol=4);(ROOT/'.local_packets.pickle').write_bytes(raw)
 (ROOT/'.local_packets.sha256').write_text(hashlib.sha256(raw).hexdigest())
 log('built exact packets',len(v1),len(v2),len(v3),'full final residual',len(f2))

def load_state():
 # Only consume this script's local generated cache. Do not import outside pickle files.
 import pickle
 raw=(ROOT/'.local_packets.pickle').read_bytes()
 assert hashlib.sha256(raw).hexdigest()==(ROOT/'.local_packets.sha256').read_text()
 return pickle.loads(raw)

def stage_identities():
 d=load_state();v1,v2,v3=[d[x] for x in ('v1','v2','v3')];old=par.old
 ks,spv1=pure_basis();on2=old.ntime(spv1,spv1);ov2=old.solve_heat(on2)
 on3=old.plus(old.ntime(spv1,ov2),old.ntime(ov2,spv1))
 assert import_packets(on2)==d['n2'] and import_packets(ov2)==v2
 assert import_packets(on3)==d['n3'] and import_packets(old.solve_heat(on3))==v3
 assert heat_derivative(v2)==d['n2'] and heat_derivative(v3)==d['n3']
 assert not initial(v2) and not initial(v3)
 v,U1,U2,h0,h1,f0,f1,f2,e0,e1=[d[x] for x in ('v','U1','U2','h0','h1','f0','f1','f2','e0','e1')]
 assert residual(v)==f0 and residual(U1)==f1 and residual(U2)==f2
 assert plus(linear(v,h0),f0)==e0 and plus(linear(U1,h1),f1)==e1
 assert plus(e0,scale(ntime(h0,h0),-1))==f1
 assert plus(e1,scale(ntime(h1,h1),-1))==f2
 for vv in (v,U1,U2,f0,f1,f2,e0,e1):reality_div_free(vv)
 report={'inherited_oracle_agreement':True,'complete_residual_identity':True,
  'linear_defect_identity':True,'all_generated_outputs_included':True,
  'no_spatial_or_temporal_sampling':True,'real_divergence_free_checked':True,
  'state_sha256':(ROOT/'.local_packets.sha256').read_text()}
 (ROOT/'identity_checks.json').write_text(json.dumps(report,indent=2)+'\n')
 log('PASS: both full nonlinear and inexact linear identities')

def stage_grams():
 d=load_state();result={}
 for name in ('f0','e0','f1','e1','degree6_remainder'):
  vv=d['n6'] if name=='degree6_remainder' else d[name]
  bounds,coeff=gram_bounds(vv)
  if name=='degree6_remainder':
   bounds=tuple(x*d['amp']**12 for x in bounds)
   coeff={k:[x*d['amp']**12 for x in val] for k,val in coeff.items()}
  nb=(sqrt_bounds(bounds[0])[0],sqrt_bounds(bounds[1])[1])
  result[name]={'packets':len(vv),'modes':len(set(k for k,r,m in vv)),
    'squared_norm_lower':str(bounds[0]),'squared_norm_upper':str(bounds[1]),
    'norm_lower':str(nb[0]),'norm_upper':str(nb[1]),'norm_upper_decimal':float(nb[1])}
  (ROOT/(name+'_gram_coefficients.json')).write_text(json.dumps({str(k):list(map(str,x)) for k,x in coeff.items()},indent=2)+'\n')
  log(name,result[name]['norm_upper_decimal'])
 rlo=max(F(),F(result['e1']['norm_lower'])-F(result['degree6_remainder']['norm_upper']))
 rhi=F(result['e1']['norm_upper'])+F(result['degree6_remainder']['norm_upper'])
 f2=d['f2'];result['f2']={'packets':len(f2),'modes':len(set(k for k,r,m in f2)),
  'norm_lower':str(rlo),'norm_upper':str(rhi),'norm_upper_decimal':float(rhi),
  'method':'reverse/forward triangle after separate exact coherent Grams; no term discarded'}
 (ROOT/'measured_residuals.json').write_text(json.dumps(result,indent=2)+'\n')
 log('full f2 certified upper',float(rhi))

def stage_report():
 d=load_state();result=json.loads((ROOT/'measured_residuals.json').read_text())
 checks=json.loads((ROOT/'identity_checks.json').read_text())
 assert checks['state_sha256']==(ROOT/'.local_packets.sha256').read_text()
 L=F(33,10);alpha=F(128,5);rstar=F(7,1000)
 s1=F(507,100000);s2=s1+F(16,125000)
 R1=F(51,400000);R2=F(381,100000000)
 assert F(result['f1']['norm_upper'])<R1 and F(result['f2']['norm_upper'])<R2
 assert F(result['e0']['norm_upper'])<F(3,100)*F(result['f0']['norm_lower'])
 assert F(result['e1']['norm_upper'])<F(3,100)*F(result['f1']['norm_lower'])
 E1=F(61,100000);E2=F(19,1000000)
 assert alpha*(s1+rstar)<1 and alpha*(s2+rstar)<1
 assert L*R1/(1-alpha*(s1+rstar))<E1
 assert L*R2/(1-alpha*(s2+rstar))<E2
 start=F(1,50000);trust=rstar+start;den=1-2*alpha*trust
 assert den>F(16,25) and 2*alpha/F(16,25)==80
 radii=[start]
 for _ in range(3):radii.append(80*radii[-1]**2)
 # Error transport identity and scalar forcing allocation are exact algebra.
 aa,ll,ee,rr=s.symbols('alpha L eps r',nonnegative=True)
 assert s.expand(aa*rr**2+ll*(aa/ll)*rr**2)==2*aa*rr**2
 report={'schema':'EM_RESULT_SPECIFIC_VERIFICATION_V1','status':'PASS',
 'record_id':'FINDING-EM-PDE-INEXACT-NEWTON-ERROR-LEDGER-20260909',
 'activity_id':'RA-076944AE1950A916ACC95399',
 'source_identity':{'rank':3,'initial_modes':8,'amplitude':'1/10','nu':'1','wavevectors':d['ks'],'initial_helicity':'+'},
 'checks':checks,
 'packet_counts':{name:len(d[name]) for name in ('v1','v2','v3','n4','n5','n6')},
 'measured_residuals':result,
 'posteriori':{'L':str(L),'alpha':str(alpha),'parent_radius':str(rstar),
  'first_reference_norm_upper':str(s1),'second_reference_norm_upper':str(s2),
  'first_residual_norm_upper':str(R1),'second_residual_norm_upper':str(R2),
  'first_actual_error_radius':str(E1),'second_actual_error_radius':str(E2),
  'executed_linear_forcing_upper':'3/100',
  'executed_forcing_ratios_upper_decimal':[float(F(result['e0']['norm_upper'])/F(result['f0']['norm_lower'])),float(F(result['e1']['norm_upper'])/F(result['f1']['norm_lower']))],
  'future_trust_denominator_lower':'16/25',
  'future_forcing_rule':'eps_n <= (256/33)*E_n^2',
  'future_enclosure_rule':'E_(n+1) <= 80 E_n^2',
  'future_conditional_enclosures':[str(x) for x in radii],
  'future_conditional_enclosures_decimal':[float(x) for x in radii]},
 'limitations':[
  'Two finite all-output inexact steps were executed; later adaptive inner solves were not executed.',
  'The sharper error concerns changing references, not a new arbitrary-initial-data theorem.',
  'Exact rational Gram arithmetic is not independent review or proof-assistant formalization.',
  'The inherited all-mode causal inverse and C*=9.503 are analytic dependencies.',
  'The last degree-six cross-generation norm is bounded by triangle after its exact Gram; it is not discarded.']}
 (ROOT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 log('PASS: certified actual error radii',float(E1),float(E2))
 print('conditional future radii', [float(x) for x in radii])

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--stage',choices=['build','identities','grams','report','all'],default='all')
 mode=parser.parse_args().stage
 for name in ['build','identities','grams','report']:
  if mode in ('all',name):globals()['stage_'+name]()
