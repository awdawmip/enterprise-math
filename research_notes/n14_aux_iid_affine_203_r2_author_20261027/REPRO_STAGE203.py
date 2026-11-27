"""Stage203 portable exact external N14 IID verifier. No native P000 CLAIM."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
N=14;P=(F(3,24),F(1,24),F(20,24));Q=(F(2,24),F(2,24),F(20,24))
K=F(17496,139);T=(13,6,4);Z=(14,0,0);S=(0,0,0)
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
 c={'P':K*lr(s),'Q':K}
 if s[0]<N:c['C']=1+sum(P[i]*bell(child(s,i))[0] for i in range(3))
 v=min(c.values());return v,tuple(a for a in c if c[a]==v),tuple(x-v for x in c.values() if x>v)
assert len(states)==680
assert bell(S)[0]==F(188497771183924373447,1903623110104449024)
assert {s:bell(s)[1] for s in states if len(bell(s)[1])>1}=={T:('Q','C'),Z:('P','Q')}
gaps=[x for s in states for x in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(16319029,830103552)
def act(s,t,z):return ('Q' if t else 'C') if s==T else ('P' if z else 'Q') if s==Z else bell(s)[1][0]
@lru_cache(None)
def dp(s,t,z):
 a=act(s,t,z)
 if a=='P':return F(0),F(1),F(0),F(0)
 if a=='Q':return F(1),F(0),F(0),F(0)
 cs=[dp(child(s,i),t,z) for i in range(3)]
 return tuple(F(j>=2)+sum((P if j%2==0 else Q)[i]*cs[i][j] for i in range(3)) for j in range(4))
def dfs(t,z):
 sums=[0]*4;nodes=0;joint=0
 def visit(s,p,q,seen=False):
  nonlocal nodes,joint
  nodes+=1
  if s==T:seen=True
  if s==Z:joint+=int(seen)
  a=act(s,t,z)
  if a=='C':
   for i in range(3):visit(child(s,i),p*(3,1,20)[i],q*(2,2,20)[i],seen)
  else:
   m=24**(N-s[0]);n=s[0]
   sums[0]+=int(a=='Q')*p*m;sums[1]+=int(a=='P')*q*m
   sums[2]+=n*p*m;sums[3]+=n*q*m
 visit(S,1,1)
 return tuple(F(x,24**N) for x in sums),nodes,joint
cs={};total=0
for t,z in product((0,1),repeat=2):
 x=dp(S,t,z);y,n,j=dfs(t,z)
 assert x==y and j==0
 cs[t,z]=x;total+=n
O=cs[0,0];DT=tuple(cs[1,0][i]-O[i] for i in range(4))
DZ=tuple(cs[0,1][i]-O[i] for i in range(4))
assert tuple(cs[1,1][i]-cs[1,0][i]-cs[0,1][i]+O[i] for i in range(4))==(F(0),)*4
err=lambda a:a[0]-a[1]
z0=-err(O)/err(DZ);zs=-err(DT)/err(DZ)
assert z0==F(112590665042401049,819200000000000000) and zs==F(121121,10240000000000)
assert 0<z0<z0+zs<1
def balance(t):return tuple(O[i]+DT[i]*t+DZ[i]*(z0+zs*t) for i in range(4))
a,b=balance(F(0)),balance(F(1))
assert a[0]==a[1]==F(3712577116979992345,10517860061584293888)
assert a[2]==F(2226587199024284573,219122084616339456)
assert b[0]==b[1]==F(1237525705766008115,3505953353861431296)
assert b[2]==F(2226587197356332573,219122084616339456)
assert a[2]>a[3] and b[2]>b[3] and b[0]>a[0]
assert a[2]+K*(a[0]+a[1])==b[2]+K*(b[0]+b[1])==bell(S)[0]
assert total==378760
print('STAGE203_REFERENCE_EXACT_PASS',total,'width',b[0]-a[0],'slope',2*K)
