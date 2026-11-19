#!/usr/bin/env python3
"""EC49FUG: exact uniform-in-width binomial endpoint minimax certificate.
Only standard library.  x and s denote the normalized bin width and E-e.
Uses integer bivariate polynomials and exact rational threshold brackets.
Author checked Python 3.11+; no floating point in any sign decision.
"""
from fractions import Fraction as F
from math import comb, factorial, lcm
import sys, time

E=F(1048576,18958647)
m=F(1469,64);L=F(951,1280);U=F(3,4);W=U-L
alpha=m*(L+U)/2; c0=m*U; c1=m*W/2
# polynomial keys: (degree_x, degree_s)
def val(z):return {(0,0):int(z)} if z else {}
def clean(p):return {k:v for k,v in p.items() if v}
def add(p,q):
 o=p.copy()
 for k,v in q.items():o[k]=o.get(k,0)+v
 return clean(o)
def neg(p):return {k:-v for k,v in p.items()}
def sub(p,q):return add(p,neg(q))
def mul(p,q):
 z={}
 for (x,s),v in p.items():
  for (xx,ss),vv in q.items():
   k=x+xx,s+ss;z[k]=z.get(k,0)+v*vv
 return clean(z)
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def powers(p,n):
 out=[val(1)]
 for k in range(n):out.append(mul(out[-1],p))
 return out
def make_pairs():
 # A=1-E alpha +s alpha. P=x(1-(E-s)(c0-c1*x)).
 ra={(0,0):1-E*alpha,(0,1):alpha}
 rp={(1,0):1-E*c0,(2,0):E*c1,(1,1):c0,(2,1):-c1}
 rb={(0,0):F(2630615040)-F(45529434409)*E,(0,1):F(45529434409)}
 rq={(0,0):F(575)*(F(2359296)-F(41217719)*E),(0,1):F(575*41217719)}
 def scale_pair(a,b):
  mulden=lcm(*[v.denominator for v in list(a.values())+list(b.values())])
  return ({k:int(v*mulden) for k,v in a.items()},{k:int(v*mulden) for k,v in b.items()})
 A,P=scale_pair(ra,rp);B,Q=scale_pair(rb,rq)
 return A,P,B,Q
A,P,B,Q=make_pairs();V=mul(A,B);J=sub(add(mul(P,B),mul(Q,A)),mul(P,Q))
assert all(k[0]==0 for k in V)

def end_probs(x):
 c=c0-c1*x
 p=x*(1-E*c)/(1-E*alpha)
 q=F(575)*(F(41217719)*E-F(2359296))/(F(45529434409)*E-F(2630615040))
 return p,p+q*(1-p)
def end_mass(n,k,x):
 p,r=end_probs(x)
 return comb(n,k)*(r**k*(1-r)**(n-k)-p**k*(1-p)**(n-k))
def brackets(n,den=100000):
 bounds=[(0,0)]
 for k in range(1,n):
  lo,hi=0,den-1
  assert end_mass(n,k,F(0))>0 and end_mass(n,k,F(hi,den))<0
  while hi-lo>1:
   mid=(lo+hi)//2
   if end_mass(n,k,F(mid,den))>0:lo=mid
   else:hi=mid
  assert end_mass(n,k,F(lo,den))>0 and end_mass(n,k,F(hi,den))<0
  bounds.append((lo,hi))
 bounds.append((den,den))
 assert all(bounds[k][1]<bounds[k+1][0] for k in range(1,n-1))
 return [(bounds[j-1][0],bounds[j][1]) for j in range(1,n+1)]

def bernstein_nonnegative(coeffs,lo,hi,den):
 # certifies C(x)>=0 on [lo/den,hi/den] by degree-d Bernstein coefficient signs.
 # Multiply by den^d * d!, yielding integer control coefficients.
 d=max(coeffs.keys(),default=0)
 if lo==hi:return sum(v*lo**k*den**(d-k) for k,v in coeffs.items())>=0
 delta=hi-lo
 beta=[0]*(d+1)
 for k,v in coeffs.items():
  for h in range(k+1):
   beta[h]+=v*comb(k,h)*(lo**(k-h))*(delta**h)*(den**(d-k))
 fact=[factorial(j) for j in range(d+1)]
 for i in range(d+1):
  num=sum(beta[h]*comb(i,h)*fact[h]*fact[d-h] for h in range(i+1))
  if num<0:return False
 return True

def run_n(n, verbose=True):
 t=time.time();bounds=brackets(n)
 js=powers(J,n); oth=powers(sub(V,J),n);ps=powers(P,n);aoth=powers(sub(A,P),n)
 b_n=powers(B,n)[n];v_n=powers(V,n)[n]
 v0=V.get((0,0))
 FJ={};FP={}
 for j in range(n,0,-1):
  FJ=add(FJ,scale(mul(js[j],oth[n-j]),comb(n,j)))
  FP=add(FP,scale(mul(ps[j],aoth[n-j]),comb(n,j)))
  D=sub(FJ,mul(FP,b_n))
  D0={(i,0):c for (i,h),c in D.items() if h==0}
  H=sub(scale(D,v0**n),mul(D0,v_n))
  assert not any(h==0 for (i,h) in H)
  lo,hi=bounds[j-1]; bad=[]; cnt=0
  for h in range(1,2*n+1):
   poly={i:c for (i,hh),c in H.items() if hh==h}
   assert max(poly,default=0)==2*n, (n,j,h,max(poly,default=0))
   if not bernstein_nonnegative(poly,lo,hi,100000):bad.append(h)
   cnt+=1
  if bad:
   print('FAILED',n,j,lo,hi,bad,flush=True)
   return False
  if verbose:print('PASS n',n,'j',j,'xbox',f'{lo}/100000..{hi}/100000','s-coeff',cnt,'elapsed',round(time.time()-t,2),flush=True)
 if verbose:print('ALL_PASS_n',n,'elapsed',round(time.time()-t,2),flush=True)
 return True

def binomial_one_or_more(n,e,x):
 c=c0-c1*x
 p=x*(1-e*c)/(1-e*alpha)
 q=F(575)*(F(41217719)*e-F(2359296))/(F(45529434409)*e-F(2630615040))
 return (1-p)**n*(1-(1-q)**n)

def univariate_mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,aa in enumerate(a):
  for j,bb in enumerate(b):z[i+j]+=aa*bb
 return z

def witness_interval():
 n=15; lo=F(1,3500);hi=F(29,100000)
 # Endpoint Bayes threshold is K>=1 across interval: likelihood ratio
 # increases in k, and mass(k=1) is strictly positive at the upper edge.
 assert end_mass(15,1,hi)>0
 for x in (lo,hi):
  assert end_mass(15,0,x)<0
  assert all(end_mass(15,k,x)>0 for k in range(1,16))
  assert binomial_one_or_more(15,F(-1),x)<binomial_one_or_more(15,E,x)

 def delta_poly(e):
  # p_e(x)=a*x+b*x*x; one-minus-p is a quadratic polynomial.
  a=(1-e*c0)/(1-e*alpha);b=e*c1/(1-e*alpha)
  one_minus_p=[F(1),-a,-b]
  value=[F(1)]
  for _ in range(n):value=univariate_mul(value,one_minus_p)
  q=F(575)*(F(41217719)*e-F(2359296))/(F(45529434409)*e-F(2630615040))
  return [v*(1-(1-q)**n) for v in value]
 dminus=delta_poly(F(-1));dend=delta_poly(E)
 diff=[a-b for a,b in zip(dminus,dend)]
 deg=len(diff)-1;assert deg==30
 # Bernstein coefficient sign of Delta(-1,x)-Delta(E,x) on [lo,hi]
 tcoef=[sum(diff[k]*comb(k,h)*lo**(k-h)*(hi-lo)**h for k in range(h,deg+1)) for h in range(deg+1)]
 bcoef=[sum(tcoef[h]*F(comb(i,h),comb(deg,h)) for h in range(i+1)) for i in range(deg+1)]
 assert len(bcoef)==31 and all(b<0 for b in bcoef)
 print('PASS n15 rational-width failure: x in [1/3500,29/100000], e=-1; 31/31 negative Bernstein coefficients; unique endpoint Bayes threshold K>=1',flush=True)
 print('WITNESS x=1/3500 diff=',float(binomial_one_or_more(n,F(-1),lo)-binomial_one_or_more(n,E,lo)),flush=True)
 return True

if __name__=='__main__':
 for n in map(int,sys.argv[1:] or range(1,15)):
  if not run_n(n):sys.exit(1)

 if list(map(int,sys.argv[1:] or range(1,15)))==list(range(1,15)):
  assert witness_interval()
  print('PASS full first transition at 15, verified 2030 coefficient polynomials and 46130 nonnegative Bernstein controls plus 31 strict negative width-witness controls')
