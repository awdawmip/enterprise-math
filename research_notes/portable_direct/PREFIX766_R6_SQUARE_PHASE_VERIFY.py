"""Exact author certificate for PREFIX-766 in the frozen BRC/Gamma auxiliary model."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb

N,W=189,1<<18
@lru_cache(None)
def inside(n,k,x):return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n

@lru_cache(None)
def wide(n,k):
 if k>n//2:return wide(n,n-k)
 m=k*W//n
 assert inside(n,k,m)
 if k==0:lo=hi=0
 else:
  a,b=0,m
  while b-a>1:
   t=(a+b)//2
   if inside(n,k,t):b=t
   else:a=t
  lo,hi=a,b
 a,b=m,W
 while b-a>1:
  t=(a+b)//2
  if inside(n,k,t):a=t
  else:b=t
 if 4*(a-hi)>W:return True
 if 4*(b-lo)<W:return False
 raise ArithmeticError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
 c=defaultdict(int)
 for k,v in rows[-1].items():c[k]+=v;c[k+1]+=v
 rows.append({k:v for k,v in c.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529

def scaled_survivors(x):
 powers=[1]; rev=[1]
 for _ in range(N):powers.append(powers[-1]*x);rev.append(rev[-1]*(1024-x))
 nums=[sum(v*powers[k]*rev[n-k] for k,v in row.items()) for n,row in enumerate(rows[:N])]
 assert all(nums[n]==1024**n for n in range(25))
 assert nums[25]==1024**25-x**25-(1024-x)**25
 return [v<<(10*(188-i)) for i,v in enumerate(nums)]

a,b=scaled_survivors(51),scaled_survivors(52)
d=[x-y for x,y in zip(b,a)]
E=1<<4137; scale=1<<2257
Caa=Cab=Cbb=Cdd=Ldd=0
for i in range(N):
 for j in range(i,N):
  w=comb(i+j,i)<<(376-i-j)
  factor=1 if i==j else 2
  Caa+=factor*w*a[i]*a[j]
  Cab+=w*(a[i]*b[j] if i==j else a[i]*b[j]+a[j]*b[i])
  Cbb+=factor*w*b[i]*b[j]
  Cdd+=factor*w*d[i]*d[j]
  Ldd+=factor*w*(i+j+1)*d[i]*d[j]
maa=2*sum(a)*scale-Caa
mab=(sum(a)+sum(b))*scale-Cab
mbb=2*sum(b)*scale-Cbb
dmu=-Cdd
dvar=-Ldd*E-(mbb*mbb-2*mab*mab+maa*maa)
assert dmu==mbb-2*mab+maa
assert dmu<0 and dvar<0
# Exact rational ratio q_R=(dmu/E)/(dvar/E^2).
num,den=-dmu*E,-dvar
assert 28519*den<1000000*num<28520*den
q=Fraction(num,den)
assert Fraction(28520,1000000)**2 * Fraction(dvar,E*E)-Fraction(28520,1000000)*Fraction(dmu,E)<0
print('ALL_CHECKS_PASS PREFIX766')
print('q_R',format(float(q),'.17g'))
print('Delta_mu',format(float(Fraction(dmu,E)),'.17g'))
print('Delta_variance',format(float(Fraction(dvar,E*E)),'.17g'))
