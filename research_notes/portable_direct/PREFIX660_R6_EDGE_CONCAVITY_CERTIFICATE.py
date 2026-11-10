#!/usr/bin/env python3
"""PREFIX-660 exact BRC boundary moving-max certificate.
Frozen scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Uses integer and Fraction arithmetic only.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N,DEN,S=189,2**18,2**216
Q=F(19,128);DELTA=F(1,4096);checks=0

def check(ok,msg):
 global checks
 assert ok,msg
 checks+=1

@lru_cache(None)
def inside(n,k,a):
 return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n

@lru_cache(None)
def wide(n,k):
 if k>n//2:return wide(n,n-k)
 mid=k*DEN//n
 assert inside(n,k,mid)
 if k==0:ll=lh=0
 else:
  lo,hi=0,mid
  while hi-lo>1:
   m=(lo+hi)//2
   if inside(n,k,m):hi=m
   else:lo=m
  ll,lh=lo,hi
 lo,hi=mid,DEN
 while hi-lo>1:
  m=(lo+hi)//2
  if inside(n,k,m):lo=m
  else:hi=m
 rl,rh=lo,hi
 if 4*(rl-lh)>DEN:return True
 if 4*(rh-ll)<DEN:return False
 raise AssertionError(('ambiguous frozen predicate',n,k))

def make_rows():
 state={0:1};rows=[state.copy()]
 for n in range(1,N+1):
  nxt=defaultdict(int)
  for k,v in state.items():nxt[k]+=v;nxt[k+1]+=v
  state={k:v for k,v in nxt.items() if wide(n,k)}
  rows.append(state.copy())
 return rows

def shift(poly,q):
 out=[F(poly[-1])]
 for c in reversed(poly[:-1]):
  v=[q*out[0]+c]
  v.extend(out[i-1]+q*out[i] for i in range(1,len(out)))
  v.append(out[-1]);out=v
 return out

def evaluate(b,h,d):
 if d==0:return sum(b[k]*h**k for k in range(len(b)))/S**2
 if d==1:return sum(k*b[k]*h**(k-1) for k in range(1,len(b)))/S**2
 if d==2:return sum(k*(k-1)*b[k]*h**(k-2) for k in range(2,len(b)))/S**2
 raise ValueError('derivative order')

def curvature_tail(b,d):
 return sum(k*(k-1)*abs(b[k])*d**(k-2) for k in range(3,len(b)))/S**2

def dec(x,n=12,up=False):
 a=(x.numerator*10**n+(x.denominator-1 if up else 0))//x.denominator
 return str(a//10**n)+'.'+str(a%10**n).zfill(n)

def main():
 rows=make_rows()
 check(len(rows)==190 and not rows[-1],'extinction at level 189')
 check(all(sum(rows[n].values())==2**n for n in range(25)), 'full survival through level 24')
 check(sum(rows[25].values())==2**25-2,'first removal at 25')
 check(all(rows[n].get(0,0)==0 for n in range(25,190)),'gamma boundary path')
 check(all(0<=v<=comb(n,k) for n,row in enumerate(rows[:N]) for k,v in row.items()),'Bernstein fractions')
 A=[];B=[]
 for m in range(N):
  a=F(1);b=F(m+1)
  for n in range(25):
   w=F(comb(n+m,n),2**(n+m+1))
   a-=w;b-=F(n+m+1,2)*w
  A.append(a);B.append(b)
 check(all((x*S).denominator==1 for x in A+B),'dyadic scale is exact')
 M=[0]*N;H=[0]*N
 for m,row in enumerate(rows[:N]):
  a,b=int(A[m]*S),int(B[m]*S)
  for j,aj in row.items():
   for k in range(j,m+1):
    term=aj*(-1)**(k-j)*comb(m-j,k-j)
    M[k]+=a*term;H[k]+=b*term
 M[0]+=25*S;H[0]+=325*S
 check(M[0]>=0 and H[0]>=0,'boundary constant terms')
 center={}
 for q in (12,24):
  p=[0]*(2*N-1)
  for j in range(N):
   p[j]+=(2*q*q*H[j]-q*M[j])*S
   for k in range(N):p[j+k]-=q*q*M[j]*M[k]
  center[q]=shift(p,Q)
  check(len(center[q])==377,'maximal polynomial degree')
 bounds={12:(-13000000,-12800000),24:(-52000000,-51500000)}
 results={}
 for q in (12,24):
  b=center[q]
  c=evaluate(b,F(0),2);tail=curvature_tail(b,DELTA)
  lo,hi=bounds[q]
  check(F(lo)<c-tail<c+tail<F(hi),'uniform negative second derivative')
  left,right=F(-1,4096),F(1,4096)
  slopes=[evaluate(b,x,1) for x in (left,right)]
  if q==12:check(slopes[0]>2700 and slopes[1]<-3600,'12 endpoint slopes')
  else:check(slopes[0]>24000 and slopes[1]<-1200,'24 endpoint slopes')
  ticks=(-584,-583) if q==12 else (3682,3683)
  low=F(ticks[0],2**24);high=F(ticks[1],2**24)
  check(-DELTA<low<high<DELTA,'tight root bracket inside band')
  check(evaluate(b,low,1)>0 and evaluate(b,high,1)<0,'unique interior root bracket')
  vlow,vhigh=evaluate(b,low,0),evaluate(b,high,0)
  peaklower=max(vlow,vhigh)
  peakupper=peaklower+F(-lo,8)*(high-low)**2
  base=evaluate(b,F(0),0)
  check(peaklower>base+(F(78,10000) if q==12 else F(12445,10000)),'new strict variance competitor')
  results[str(q)]={'V_at_Q':dec(base,12),'V_prime_at_Q':dec(evaluate(b,F(0),1),9),
   'V_double_prime_at_Q':dec(c,6),'uniform_curvature_interval':[str(lo),str(hi)],
   'curvature_deviation_upper_decimal':dec(tail,7),
   'band_endpoint_slopes':[dec(x,6) for x in slopes],
   'stationary_offset_bracket':[str(low),str(high)],
   'stationary_z_bracket':[str(Q+low),str(Q+high)],
   'max_value_strict_interval_decimal':[dec(peaklower,10),dec(peakupper,10,up=True)],
   'variance_gain_lower_decimal':dec(peaklower-base,10)}
 l12,h12=bounds[12];l24,h24=bounds[24]
 w2lo=(F(l24,24)-F(h12,12))/12
 w2hi=(F(h24,24)-F(l12,12))/12
 check(-92000<w2lo<w2hi<-88000,'W curvature derived from two slots')
 w1=(evaluate(center[24],F(0),1)/24-evaluate(center[12],F(0),1)/12)/12
 check(42<w1<43,'positive W prime at Q')
 check(w1-92000*DELTA>19,'W prime positive throughout band')
 output={'schema':'EM_PREFIX660_R6_MOVING_EDGE_MAX_V1','date':'2026-11-10',
  'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'layer_count':189,'edge':'p=0','z_band':[str(Q-DELTA),str(Q+DELTA)],
  'exact_global_band_conclusion':'for every real 12<=q<=24 unique stationary point; strict concave max; z*(q) strictly increasing',
  'W_prime_uniform_lower':'>19','q_values':results,'checks_passed':checks,
  'verification':'stdlib integer/Fraction, exact polynomial Taylor majorant, no floating-point proof comparisons',
  'status':'AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED',
  'open_problem':'certify inward p derivative near entire moving z*(q), then global triangular-region Bernstein elimination'}
 print(json.dumps(output,indent=2,ensure_ascii=False))
 print('ALL_CHECKS_PASS',checks)

if __name__=='__main__':main()
