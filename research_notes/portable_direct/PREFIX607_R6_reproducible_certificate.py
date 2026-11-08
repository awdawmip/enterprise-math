#!/usr/bin/env python3
"""Exact finite-sample certificate for PREFIX-607-R6; stdlib only."""
import hashlib, io, json
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
source=Path(__file__).with_name('PREFIX565_positive_marginal_certificate.py').read_bytes()
blob=hashlib.sha1(('blob %d\0'%len(source)).encode()+source).hexdigest()
assert blob=='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'
with redirect_stdout(io.StringIO()):
 from PREFIX565_positive_marginal_certificate import PHASES,NEXT,SCIENCE_PIN,ROOTS
 import PREFIX605_R6_binary_tag_certificate as prev
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(PHASES)==48 and len(ROOTS)==9
assert sorted(NEXT[p][0] for p in range(48))==list(range(48))
E=sorted({(a,abs(c)) for a,b,c in PHASES});assert len(E)==12
idx={v:i for i,v in enumerate(E)}
ei=[idx[(a,abs(c))] for a,b,c in PHASES]
assert all(ei.count(e)==4 for e in range(12))
def risk(pi,s):return sum(x*y-y*y for x,y in zip(s,pi))
def optimum(s):
 values=sorted(s,reverse=True)
 for m in range(1,len(s)+1):
  lam=(sum(values[:m])-2)/m
  if values[m-1]>lam and (m==len(s) or values[m]<=lam):break
 else:raise AssertionError('KKT')
 pi=[max(F(0),(x-lam)/2) for x in s]
 assert sum(pi)==1 and all((x-2*y==lam if y else x<=lam) for x,y in zip(s,pi))
 return risk(pi,s),pi
s0=[F(3)]*48
v0,p0=optimum(s0)
assert v0==F(143,48) and all(x==F(1,48) for x in p0)
assert optimum([F(1)]*48)[0]==F(47,48)
t=[F(i+1,i+2) for i in range(12)]
s=[1+2*t[e] for e in ei]
pi=[F(0)]*48
for i,p in zip((0,5,17,42),(F(1,6),F(1,3),F(1,4),F(1,4))):pi[i]=p
ids=[i for i,p in enumerate(pi) if p]
events=[(i,pi[i]/s[i]) for i in ids]
events.append((None,1-sum(p for _,p in events)))
assert all(p>=0 for _,p in events)
mean=[F(0)]*48; cross={(i,j):F(0) for i in ids for j in ids}; observed=F(0)
for a,pa in events:
 for b,pb in events:
  ct=Counter([a,b]);z=[F(ct[i])*s[i]/2 for i in range(48)]
  pr=pa*pb
  for i in range(48):mean[i]+=pr*z[i]
  for i,j in cross:cross[i,j]+=pr*z[i]*z[j]
  observed+=pr*sum((x-y)**2 for x,y in zip(z,pi))
assert mean==pi and observed==risk(pi,s)/2
assert all(cross[i,j]==pi[i]*pi[j]+((pi[i]*s[i] if i==j else 0)-pi[i]*pi[j])/2 for i,j in cross)
upper,opt=optimum(s);assert upper>=risk(pi,s)
e,f=prev.pairs[0];tw=[F(1)]*12;tw[e]=F(1,32);tw[f]=F(8)
assert 4*tw[e]*tw[f]==1
heavy=ei.index(f);point=[F(0)]*48;point[heavy]=F(1)
assert risk(point,[1+2*tw[h] for h in ei])==16
result={'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,'native_blob':blob,
 'original_worst_mse_factor':'143/48','all_zero_worst_mse_factor':'47/48',
 'asymmetric_n2_risk':str(observed),'asymmetric_n2_outcomes':25,
 'asymmetric_covariances_checked':16,'critical_x':'1/32',
 'critical_heavy_point_mass_risk_factor':'16',
 'no_slot0_hit_N16':str(F(16,17)**16),
 'claim':'Exact finite-N unbiased covariance and MSE for singleton slot0 estimator; KKT-sharp worst-case risk; one critical rare-event witness',
 'method':'48-phase native-slot permutation check, rational N=2 exhaustive enumeration, rational KKT cases',
 'stage':'AUTHOR_PROVED / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX607_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
