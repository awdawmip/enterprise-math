#!/usr/bin/env python3
"""R245: exact rational verification of first two-Perron-mode error crossings.
All final PASS comparisons use Fraction and integer arithmetic. numpy/scipy not needed.
R243, R244 provide the block spectral nonnegativity and dominance facts.
"""
from fractions import Fraction as F
from math import lcm
from hashlib import sha256
import json, sys
sys.set_int_max_str_digits(1000000)
W=(144,576,1440,4320,17280,86400,518400)
ANCHORS=(F(39,100),F(2,5),F(41,100))
# Candidate crossings are independently bracketed by exact comparisons below.
# The time-monotonicity theorem makes two checks per threshold sufficient.
CANDIDATES={'39/100':(262,381),'2/5':(266,390),'41/100':(270,403)}

def params(s):
 t=(1691*s-2615)/(2615*s-3539)
 a=(F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t)
 b=(F(13,60),)+tuple(F(5,18)*abs(F(1,2)-v) for v in a[1:])
 pi=tuple(v/(1-x) for x,v in zip(a,b))
 assert sum(pi)==1 and all(x>0 for x in b) and all(0<x<1 for x in a)
 Z=sum((v/(1-x)**2 for x,v in zip(a,b)),F(0))
 rho=tuple(v/(1-x)**2/Z for x,v in zip(a,b))
 return a,b,pi,Z,rho

def mask_ids(mask):
 return [0]+[j for j in range(1,7) if mask&(1<<(j-1))]

def secular(x,a,b,ids):
 return sum((b[i]/(x-a[i]) for i in ids),F(0))-1

def root_interval(a,b,mask):
 ids=mask_ids(mask)
 lo=max(a[i] for i in ids)
 hi=F(1)
 assert secular(hi,a,b,ids)<0
 for _ in range(100):
  mid=(lo+hi)/2
  if secular(mid,a,b,ids)>0:lo=mid
  else:hi=mid
 assert lo<hi and secular(lo,a,b,ids)>0 and secular(hi,a,b,ids)<0
 return lo,hi

def amplitude_bounds(lo,hi,a,b,Z,mask):
 ids=mask_ids(mask)
 def S(x):return sum((b[i]/((1-a[i])*(x-a[i])) for i in ids),F(0))
 def Q(x):return sum((b[i]/(x-a[i])**2 for i in ids),F(0))
 w=W[mask.bit_count()]
 return w*S(hi)**2/(Z*Q(lo)),w*S(lo)**2/(Z*Q(hi))

def exact_phi_at_ks(s,ks):
 a,b,pi,Z,rho=params(s)
 P=[[a[i]*(i==j)+(1-a[i])*pi[j] for j in range(7)] for i in range(7)]
 d=lcm(*(q.denominator for row in P for q in row))
 M=[[int(q*d) for q in row] for row in P]
 rhoden=lcm(*(q.denominator for q in rho))
 rnum=[int(q*rhoden) for q in rho]
 sums={k:0 for k in ks}
 max_k=max(ks)
 for mask in range(63):
  ids=mask_ids(mask)
  weight=W[mask.bit_count()]
  v=[1]*len(ids)
  for k in range(max_k+1):
   if k in sums:
    sums[k]+=weight*sum(rnum[i]*v[u] for u,i in enumerate(ids))
   if k<max_k:
    v=[sum(M[i][j]*v[u] for u,j in enumerate(ids)) for i in ids]
 return {k:F(v,rhoden*d**k) for k,v in sums.items()},(a,b,Z)

def sign_digest(x):
 assert x!=0
 num=x.numerator
 return {'sign':1 if num>0 else -1,
         'numerator_bits':abs(num).bit_length(),
         'denominator_bits':x.denominator.bit_length(),
         'sha256':sha256((str(num)+'/'+str(x.denominator)).encode()).hexdigest()}

def validate_anchor(s):
 a,b,pi,Z,rho=params(s)
 r0,r1=root_interval(a,b,59)
 t0,t1=root_interval(a,b,55)
 assert t1<r0
 A0,A1=amplitude_bounds(r0,r1,a,b,Z,59)
 B0,B1=amplitude_bounds(t0,t1,a,b,Z,55)
 assert 0<A0<A1 and 0<B0<B1
 n01,n001=CANDIDATES[str(s)]
 ks={n01-2,n01-1,n001-2,n001-1}
 phi_vals,_=exact_phi_at_ks(s,ks)
 checks=[]
 for d,n in ((100,n01),(1000,n001)):
  for N,expected_sign in ((n-1,1),(n,-1)):
   k=N-1
   phi=phi_vals[k]
   Xlow=A0*r0**k+B0*t0**k
   Xhigh=A1*r1**k+B1*t1**k
   margin_lo=d*phi-(d+1)*Xhigh
   margin_hi=d*phi-(d+1)*Xlow
   assert margin_lo<margin_hi
   if expected_sign==1:assert margin_lo>0,(s,d,N,'previous',float(margin_lo))
   else:assert margin_hi<0,(s,d,N,'success',float(margin_hi))
   margin=margin_lo if expected_sign==1 else margin_hi
   checks.append({'target':f'1/{d}','n':N,'expected': 'above' if expected_sign>0 else 'below',
                  'certified_margin':sign_digest(margin),
                  'diagnostic_error_lower':float(phi/Xhigh-1),
                  'diagnostic_error_upper':float(phi/Xlow-1)})
 return {'s':str(s),'first_1_percent':n01,'first_0_1_percent':n001,
         'root_interval_bits':100,'main_root_bracket':[str(r0),str(r1)],
         'second_root_bracket':[str(t0),str(t1)],
         'main_amplitude_bounds':[str(A0),str(A1)],
         'second_amplitude_bounds':[str(B0),str(B1)],
         'comparisons':checks}

def main():
 rows=[validate_anchor(s) for s in ANCHORS]
 print(json.dumps({'schema':'EM_R245_EXACT_TWO_MODE_ANCHORS_V1',
   'status':'PASS','method':'rational-kernel integer propagation + 100 dyadic root bisections + rational amplitude enclosures',
   'scope':'3 anchors, two targets and their predecessor times, all comparisons exact',
   'prior_source':'R243/R244 certified all-real positivity/spectral tier premises',
   'frozen_scientific_commit':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
   'anchors':rows,'review':'NOT_REVIEWED', 'native_BRC':'NOT_EXECUTED'},
   ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
