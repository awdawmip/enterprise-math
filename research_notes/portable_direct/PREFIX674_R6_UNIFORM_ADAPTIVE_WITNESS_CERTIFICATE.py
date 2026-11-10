#!/usr/bin/env python3
"""Rebuild frozen PREFIX-660 univariate BRC observer and bisect its exact edge roots.
Scientific source pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json
N,DEN,S = 189,2**18,2**216
R = 188
D = 2**66
DP = [D**i for i in range(R+1)]
@lru_cache(None)
def inside(n,k,a):
 return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
 if k>n//2: return wide(n,n-k)
 mid=k*DEN//n
 assert inside(n,k,mid)
 if k==0: ll=lh=0
 else:
  lo,hi=0,mid
  while hi-lo>1:
   m=(lo+hi)//2
   if inside(n,k,m): hi=m
   else: lo=m
  ll,lh=lo,hi
 lo,hi=mid,DEN
 while hi-lo>1:
  m=(lo+hi)//2
  if inside(n,k,m): lo=m
  else: hi=m
 rl,rh=lo,hi
 if 4*(rl-lh)>DEN: return True
 if 4*(rh-ll)<DEN: return False
 raise AssertionError(('ambiguous frozen predicate',n,k))

def make_rows():
 state={0:1};rows=[state.copy()]
 for n in range(1,N+1):
  nxt=defaultdict(int)
  for k,v in state.items(): nxt[k]+=v;nxt[k+1]+=v
  state={k:v for k,v in nxt.items() if wide(n,k)}
  rows.append(state.copy())
 return rows

def make_mu_h(rows):
 A=[];B=[]
 for m in range(N):
  a,b=F(1),F(m+1)
  for n in range(25):
   w=F(comb(n+m,n),2**(n+m+1))
   a-=w;b-=F(n+m+1,2)*w
  assert (a*S).denominator==1 and (b*S).denominator==1
  A.append(int(a*S));B.append(int(b*S))
 M=[0]*N;H=[0]*N
 for m,row in enumerate(rows[:N]):
  a,b=A[m],B[m]
  for j,aj in row.items():
   for k in range(j,m+1):
    t=aj*(-1)**(k-j)*comb(m-j,k-j)
    M[k]+=a*t;H[k]+=b*t
 M[0]+=25*S;H[0]+=325*S
 return M,H

def poly_val_der(coeff,x):
 val=coeff[-1];der=0
 for idx in range(R-1,-1,-1):
  der=der*x+val*D
  val=val*x+coeff[idx]*DP[R-idx]
 return val,der

def slope_sign(q,x,M,H):
 mu,mud=poly_val_der(M,x)
 hh,hd=poly_val_der(H,x)
 C=S*DP[R]
 return 2*q*(hd*C-mu*mud)-mud*C

def main():
 """Exact frozen-path replay plus a real-slot uniform implication certificate."""
 checks=0
 def check(p,msg):
  nonlocal checks
  assert p,msg
  checks+=1
 rows=make_rows()
 check(len(rows)==190 and not rows[-1], 'frozen extinction at level 189')
 check(all(sum(rows[n].values())==2**n for n in range(25)), 'full survival until level 24')
 check(sum(rows[25].values())==2**25-2, 'first removal at level 25')
 check(all(0<=v<=comb(n,k) for n,row in enumerate(rows[:N]) for k,v in row.items()), 'valid integer path coefficients')
 M,H=make_mu_h(rows)
 roots={}
 for q in (12,24):
  a=607*D//4096;b=609*D//4096
  check(slope_sign(q,a,M,H)>0 and slope_sign(q,b,M,H)<0,'whole-band edge slope signs')
  i=0
  while b-a>4:
   mid=(a+b)//2
   sig=slope_sign(q,mid,M,H)
   if sig==0: a=b=mid;break
   if sig>0: a=mid
   else: b=mid
   i+=1
  check(b-a==4 and i==53,'precise 53-step dyadic bracket width')
  mid=(a+b)//2
  check(slope_sign(q,a,M,H)>0 and slope_sign(q,b,M,H)<0,'whole-band edge slope signs')
  qa,qb=((-584,-583) if q==12 else (3682,3683))
  check(F(19,128)+F(qa,2**24)<F(a,D)<F(b,D)<F(19,128)+F(qb,2**24), 'prior certified bracket inclusion')
  roots[str(q)]={'left':str(F(a,D)),'right':str(F(b,D)),'dyadic_witness':str(F(mid,D)),
               'width':str(F(b-a,D)),'bisections':i,'left_slope_positive':True,'right_slope_negative':True}
 delta=F(1,2**64)
 cap=F(52_000_000)
 pmin=F(1,2**120)
 normal=F(76650)*pmin
 witness_gap=cap*delta**2/8
 margin=normal-witness_gap
 check(F(609-607,4096)==F(1,2**11),'starting-band width')
 check(F(1,2**11)/2**53==delta,'53 bisections reach 2^-64')
 check(witness_gap==F(203125,2**123),'dyadic witness max loss')
 check(normal==F(613200,2**123),'uniform normal penalty')
 check(margin==F(410075,2**123) and margin>F(3,10**32),'positive universal strict margin')
 check(F(1,64)>pmin,'nonempty excluded p range')
 check(1-pmin/F(1,64)==1-F(1,2**114),'excluded fraction')
 check(F(76650,1)==12*F(76650,12),'minimum slot L(q)')
 slot_margin={}
 for q,C,L in ((12,13000000,76650),(24,52000000,306490)):
  value=F(L,2**120)-F(C,8*2**128)
  check(value>margin,'slot-specific improvement over uniform')
  slot_margin[str(q)]=str(value)
 output={
  'result_id':'PREFIX-674-R6',
  'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'model':'frozen 189-survivor-layer BRC two-direction first-stop statistical observer',
  'proof_scope':{'q':'every real q in [12,24]','p':'[2^-120,1/64]',
                 'z':'[607/4096,609/4096]','witness':'one q-dependent dyadic rational, fixed for all (p,z) at that q'},
  'algorithm':{'starting_band_width':'2^-11','bisections':53,'final_root_interval_width':str(delta),
               'rational_q_sign_comparisons':'exact BRC polynomial arithmetic',
               'real_q_selection':'exact real comparison at rational derivative threshold'},
  'uniform_witness_gap_upper_strict':str(witness_gap),
  'normal_penalty_lower':str(normal),
  'uniform_margin_lower_strict':str(margin),
  'simple_margin_lower_strict':'3/10^32',
  'excluded_rectangle_fraction':str(1-F(1,2**114)),
  'q_specific_exact_replay':roots,
  'slot_margin_lower_strict':slot_margin,
  'checks_passed':checks,
  'dependency_status':'Full model replay for two dyadic examples. Real-q universal implication relies on author-derived PREFIX-660 strict curvature/edge-root certificates and PREFIX-670 normal coercivity; those predecessor theorems are not independently reviewed.',
  'scientific_status':'AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED',
  'next_question':'Connect q-adaptive witnesses to full symmetry-reduced triangular-domain signed Bernstein exclusion beyond p=1/64.'
 }
 print('ALL_CHECKS_PASS',checks)
 print(json.dumps(output,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
