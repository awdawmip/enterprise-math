"""Standalone exact Stage196 checker (finite external IID N14, no native-X6 claim)."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
N=14
P=(F(3,24),F(1,24),F(20,24));Q=(F(2,24),F(2,24),F(20,24))
K=L=F(253368,1735)
H=F(168137908605541983707,1485065690661519360)
U=(10,2,2);Z=(14,0,0)
A195=F(1849072934531492153,5258930030792146944)
V195=F(1153307972138565565,109561042308169728)

def child(s,i):
 n,a,b=s
 return (n+1,a+(i==0),b+(i==1))
@lru_cache(None)
def bell(s):
 n,a,b=s
 v={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:v['C']=1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0))
 m=min(v.values())
 return m,tuple(k for k,q in v.items() if q==m),tuple(q-m for q in v.values() if q>m)
ss=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
assert len(ss)==680 and bell((0,0,0))[0]==H
assert {s:bell(s)[1] for s in ss if len(bell(s)[1])>1}=={U:('Q','C'),Z:('P','Q')}
gaps=[x for s in ss for x in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(9719,249840)
def act(s):
 if s==U or s==Z:raise ValueError('tie site')
 assert len(bell(s)[1])==1
 return bell(s)[1][0]
@lru_cache(None)
def out(s,u,z):
 n=s[0]
 if s==Z:return (1-F(z),F(z),F(0),F(0))
 a=('Q' if u else 'C') if s==U else act(s)
 if a=='P':return (F(0),F(1),F(0),F(0))
 if a=='Q':return (F(1),F(0),F(0),F(0))
 assert n<N
 v=[out(child(s,i),u,z) for i in range(3)]
 return tuple(sum(((P if j in (0,2) else Q)[i]*v[i][j] for i in range(3)),F(0))+(1 if j>=2 else 0) for j in range(4))
c={(u,z):out((0,0,0),u,z) for u,z in product((0,1),repeat=2)}
B=c[0,0];DU=tuple(c[1,0][i]-B[i] for i in range(4));DZ=tuple(c[0,1][i]-B[i] for i in range(4))
assert tuple(c[1,1][i]-c[1,0][i]-c[0,1][i]+B[i] for i in range(4))==(0,0,0,0)
assert DU==(F(15859375,110075314176),-F(45390625,417942208512),-F(213828125,41278242816),-F(32265625,3869835264))
assert DZ==(-F(6103515625,78364164096),F(6103515625,78364164096),F(0),F(0))

def dfs(u,z):
 v=[0]*4; nodes=0;hitsU=0;hitsZ=0;intersect=0
 def walk(s,p,q,priorU=False):
  nonlocal nodes,hitsU,hitsZ,intersect
  nodes+=1;n,a,b=s
  if s==U:hitsU+=1;priorU=True
  if s==Z:
   hitsZ+=1
   if priorU:intersect+=1
  x=('Q' if u else 'C') if s==U else ('P' if z else 'Q') if s==Z else act(s)
  if x=='C':
   for i,(pi,qi) in enumerate(zip((3,1,20),(2,2,20))):walk(child(s,i),p*pi,q*qi,priorU)
  else:
   scale=24**(N-n)
   if x=='Q':v[0]+=p*scale
   else:v[1]+=q*scale
   v[2]+=n*p*scale;v[3]+=n*q*scale
 walk((0,0,0),1,1)
 return tuple(F(q,24**N) for q in v),(nodes,hitsU,hitsZ,intersect)
nodecounts=[]
for u,z in product((0,1),repeat=2):
 o,counts=dfs(u,z)
 assert o==c[u,z]
 assert counts[1:]==(420,1,0)
 nodecounts.append(counts[0])
assert nodecounts==[132142,132142,123322,123322]
delta0=B[0]-B[1];du=DU[0]-DU[1];dz=DZ[0]-DZ[1]
z0=-delta0/dz;zs=-du/dz
assert z0==F(1524931934924453,81920000000000000)
assert zs==F(259539,160000000)
assert 0<z0<z0+zs<1
O=lambda u:tuple(B[i]+u*DU[i]+(z0+u*zs)*DZ[i] for i in range(4))
left=O(F(0));right=O(F(1))
assert left[0]==left[1]==A195 and left[2]==V195
assert right[0]==right[1] and all(x[2]>x[3] for x in (left,right))
Da=right[0]-left[0];Dt=right[2]-left[2]
assert Da==F(948828125,53496602689536) and Dt<0 and -Dt/Da==K+L
assert right[0]==F(1849166208131492153,5258930030792146944)
assert right[2]==F(1152740427818565565,109561042308169728)
assert left[2]-left[3]==F(3030601257510677,12173449145352192)
assert right[2]-right[3]==F(3069039657510677,12173449145352192)
for e in (left,right):assert e[2]+K*e[1]+L*e[0]==H
print('STAGE196_REFERENCE_ALL_REAL_PASS',sum(nodecounts),'nodes',Da,'delta')
