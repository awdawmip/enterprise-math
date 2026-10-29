#!/usr/bin/env python3
"""Exact signed twelve-term BRC recursion, locally recomputed coranks 301 and 302.
No native X6 claim. Conditional infinite-strip claim requires unreviewed R330.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,K,J,add,mul,forward_differences,eval_newton
from math import comb
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,time
BASE=Path(__file__).parent
R346_Q301='242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484'

def run():
 t0=time.monotonic(); rmax=303;smax=3*rmax+2;lim=2*rmax+2
 kk=[None]+[K(i) for i in range(1,13)]
 B=[[1,1]]
 for s in range(1,smax+1):
  z=J(s)
  for i in range(1,min(s,12)+1):z=add(z,mul(kk[i],B[s-i],lim),lim)
  B.append(z)
 print('B',len(B),'elapsed',round(time.monotonic()-t0,2),flush=True)
 H={};L={}
 for r in range(300,304):
  v=[]
  for u in range(r+2):
   q=r+u
   D=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
   v.append(Fraction(D,5**u))
  d=forward_differences(v)
  assert d[-1]==0,(r,'H degree bound fails at r+1')
  d=d[:-1]; assert len(d)==r+1 and d[-1]==6**r and all(x>0 for x in d)
  scaled=[x*5**r for x in d]
  assert all(x.denominator==1 for x in scaled)
  H[r]=d;L[r]=eval_newton([int(x) for x in scaled],607)
  print('H',r,'elapsed',round(time.monotonic()-t0,2),flush=True)
 summaries=[]; q302lines=[]
 for r in [301,302]:
  v=[L[r][u+1]*L[r][u+2]-L[r-1][u+2]*L[r+1][u+1] for u in range(2*r+1)]
  d=forward_differences(v)
  assert len(d)==2*r+1
  assert d[-1]==30**(2*r)*comb(2*r,r)//(r+1),(r,'Catalan top mismatch')
  coeffs=''.join(f'{r},{u},{x}\n' for u,x in enumerate(d))
  digest=sha256(coeffs.encode()).hexdigest()
  assert all(x>0 for x in d),(r,'nonpositive Q coefficient')
  if r==301:assert digest==R346_Q301,(digest,R346_Q301)
  if r==302:
   q302lines=coeffs
   (BASE/'R347_Q302_COEFFICIENTS.txt').write_text(coeffs)
  summaries.append(dict(r=r,count=len(d),sha256=digest,all_positive=True,zero_count=0,negative_count=0,min_coefficient_index=min(range(len(d)),key=lambda i:d[i]),min_coefficient_digits=len(str(min(d))),first_coefficient_digits=len(str(d[0])),last_coefficient_digits=len(str(d[-1])),catalan_top_match=True))
  print('Q',r,'count',len(d),'digest',digest,'elapsed',round(time.monotonic()-t0,2),flush=True)
 out=dict(schema='R347_Q302_BRC_EXACT_FOUR_ROW_V1',status='AUTHOR_SIDE_EXACT_COMPUTATION',scientific_scope='signed twelve term ordered hex BRC auxiliary combinatorial model',smax=smax,poly_truncation_degree=lim-1,H_range=[300,303],Q_checked=[301,302],r346_q301_anchor_digest=R346_Q301,R330_dependency='Universal extraction D_{r+u,u}=5^u H_r(u) and deg(H_r)<=r unreviewed',results=summaries,verified_unbounded_band_conditional='r=302 from Newton positive coefficients, if R330 extraction/degree lemma true',digit_exact=True,floating_point_sign_tests=False,elapsed_seconds=round(time.monotonic()-t0,3),prior_reference='https://github.com/awdawmip/enterprise-math/blob/37516cc5bb8d72098ce25f2d64881ec5da4279cd/research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_PROOF.zh-CN.md')
 (BASE/'R347_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('RESULT',json.dumps(out,ensure_ascii=False),flush=True)
if __name__=='__main__':run()
