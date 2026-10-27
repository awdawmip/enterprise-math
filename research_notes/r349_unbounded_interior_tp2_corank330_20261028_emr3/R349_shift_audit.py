#!/usr/bin/env python3
"""Shifted Newton-product kernel and componentwise-sign no-go in signed BRC model.
Full exact integer proof for the small r=1 witness; finite sign survey r<=64.
"""
from pathlib import Path
import sys, json,time
from fractions import Fraction
from math import comb,factorial
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,K,J,add,mul,forward_differences
BASE=Path(__file__).parent

def run(max_r=64, product_crosscheck_r=10):
  t=time.monotonic()
  lim=2*(max_r+2)+2
  kk=[None]+[K(i) for i in range(1,13)];B=[[1,1]]
  for s in range(1,3*(max_r+1)+3):
    z=J(s)
    for i in range(1,min(s,12)+1):z=add(z,mul(kk[i],B[s-i],lim),lim)
    B.append(z)
  a={}
  for r in range(max_r+2):
    v=[]
    for u in range(r+2):
      q=r+u
      D=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
      v.append(Fraction(D,5**u))
    d=forward_differences(v)
    assert d[-1]==0,(r,'extra finite degree check failed')
    a[r]=[int(x*5**r) for x in d[:-1]]
  def ashr(r,i,s):
    return sum(C(s,j)*a[r][i+j] for j in range(s+1) if i+j<len(a[r]))
  def T(r,i,j):
    return ashr(r,i,1)*ashr(r,j,2)-ashr(r-1,i,2)*ashr(r+1,j,1)
  assert a[0]==[1] and a[1]==[30,30] and a[2]==[800,1980,900]
  assert T(1,0,1)==-1080
  rows=[]; violation=[]; total=0
  for r in range(1,max_r+1):
    counts={'+':0,'-':0,'0':0}
    for i in range(r+2):
      for j in range(r+2):
        z=T(r,i,j);total+=1
        sign='+' if z>0 else '-' if z<0 else '0'
        counts[sign]+=1
        expect='0' if i==r+1 or (i==r and j==r+1) else ('+' if j<=i else '-')
        if sign!=expect:violation.append([r,i,j,sign,expect,str(z)])
    assert counts['+']+counts['-']+counts['0']==(r+2)**2
    rows.append(dict(r=r,negative=counts['-'],positive=counts['+'],zero=counts['0'],matches_oriented_pattern=(counts['-']==r*(r+3)//2 and counts['+']==(r+1)*(r+2)//2 and counts['0']==r+3)))
  # Product of binomial/Newton series has a strictly positive intersection-size kernel.
  # Validate exact expansion for the first product rows, without floating point.
  kernel_checks=0
  for r in range(1,product_crosscheck_r+1):
    d=[sum(T(r,i,j)*factorial(n)//(factorial(i+j-n)*factorial(n-j)*factorial(n-i))
           for i in range(r+2) for j in range(r+2)
           if 0<=i+j-n<=min(i,j)) for n in range(2*r+1)]
    # Construct Q directly from unshifted L coefficients, not from T.
    def evalL(rr,v):return sum(a[rr][i]*C(v,i) for i in range(len(a[rr])))
    qv=[evalL(r,v+1)*evalL(r,v+2)-evalL(r-1,v+2)*evalL(r+1,v+1) for v in range(2*r+1)]
    real=forward_differences(qv)
    assert d==real,(r,'weighted convolution mismatch')
    kernel_checks+=len(d)
  evidence={'schema':'R349_BRC_SHIFTED_NEWTON_KERNEL_NO_GO_V1','model':'full signed 12-term K/J auxiliary BRC recurrence','exact_small_arrays':{str(k):a[k] for k in (0,1,2)},'no_go_componentwise_witness':{'r':1,'i':0,'j':1,'A_r1_i0':ashr(1,0,1),'A_r2_j1':ashr(1,1,2),'A_rminus1_2_i0':ashr(0,0,2),'A_rplus1_1_j1':ashr(2,1,1),'T':T(1,0,1)},'finite_sign_survey_r_max':max_r,'tested_component_brackets':total,'sign_pattern_violations':len(violation),'first_violations':violation[:10],'observed_sign_pattern':'T_{r,i,j}>0 for 0<=j<=i<=r; T_{r,i,j}<0 for 0<=i<r and i<j<=r+1; otherwise T=0; FINITE OBSERVATION ONLY','product_kernel_verified_r_max':product_crosscheck_r,'product_kernel_exact_difference_checks':kernel_checks,'rows_summary':rows,'arithmetic':'exact integers and Fraction, no floating-point sign comparisons','elapsed_seconds':round(time.monotonic()-t,3)}
  (BASE/'R349_SHIFT_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
  print(json.dumps({k:v for k,v in evidence.items() if k!='rows_summary'},ensure_ascii=False))
  return evidence
if __name__=='__main__':run()
