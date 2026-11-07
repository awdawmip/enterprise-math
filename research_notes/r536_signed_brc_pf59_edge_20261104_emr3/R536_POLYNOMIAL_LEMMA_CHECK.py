"""R536: exact 580-point diagnostic for polynomial cancellation formula; no JS imports."""
from fractions import Fraction
from math import comb, factorial, prod
def bin(n,r): return comb(n,r) if n>=0 and 0<=r<=n else 0
def cat(k): return bin(2*k,k)//(k+1)
def H(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 return bin(r+t,2*t)*sum(bin(r-t,q)*(bin(2*t,r-2*q)-bin(2*t,r-2*q-1)) for q in range(r-t+1))
def P(k,t):
 if t<2:return Fraction(0)
 out=Fraction(0)
 for q in range((t-1)//2+1):
  factors=[a for a in range(2-t,t+2) if not (1-2*q<=a<=0)]
  assert len(factors)==2*t-2*q
  out+=Fraction(bin(t-1,2*q)*4**q*prod(2*k+a for a in factors)*prod((k-j)*(k+1-j) for j in range(q)),factorial(2*t))
 return out
checks=0
for k in range(1,21):
 for t in range(2,31):
  assert P(k,t)==Fraction(H(k,t),cat(k)),(k,t)
  checks+=1
print('R536_POLYNOMIAL_LEMMA_GRID_PASS',checks)
