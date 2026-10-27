#!/usr/bin/env python3
"""Stage195 independent compact exact reproduction, external ternary IID N14."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
N=14; P=(F(3,24),F(1,24),F(20,24)); Q=(F(2,24),F(2,24),F(20,24))
K=L=F(82768824,535283)
H=F(1748561457410484827718287,14661540852461004128256)
Y=(9,5,2); Z=(14,0,0)
alpha0=F(1849072830472476953,5258930030792146944)
V0=F(1153308642566039965,109561042308169728)
child=lambda s,i:(s[0]+1,s[1]+(i==0),s[2]+(i==1))
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
@lru_cache(None)
def bell(s):
 n,a,b=s; ell=F(2**(a+b),3**a)
 v={'P':K*ell,'Q':L}
 if n<N:v['C']=1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0))
 m=min(v.values())
 return m,tuple(k for k,c in v.items() if c==m),tuple(c-m for c in v.values() if c>m)
assert len(S)==680 and bell((0,0,0))[0]==H
assert {s:bell(s)[1] for s in S if len(bell(s)[1])>1}=={Y:('P','C'),Z:('P','Q')}
gaps=[q for s in S for q in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(3412925531,88797026304)
def action(s,y,z):
 if s==Y:return 'P' if y else 'C'
 if s==Z:return 'P' if z else 'Q'
 return bell(s)[1][0]
@lru_cache(None)
def obs(s,y,z):
 ac=action(s,y,z)
 if ac=='P':return (F(0),F(1),F(0),F(0))
 if ac=='Q':return (F(1),F(0),F(0),F(0))
 v=[obs(child(s,i),y,z) for i in range(3)]
 return tuple((1 if j>=2 else 0)+sum(((P if j in (0,2) else Q)[i]*v[i][j] for i in range(3)),F(0)) for j in range(4))
O={(y,z):obs((0,0,0),y,z) for y,z in product((0,1),repeat=2)}
B=O[0,0]; DY=tuple(O[1,0][i]-B[i] for i in range(4))
DZ=tuple(O[0,1][i]-B[i] for i in range(4))
assert tuple(O[1,1][i]-O[1,0][i]-O[0,1][i]+B[i] for i in range(4))==(F(0),)*4
def dfs(y,z):
 t=[0]*4; nodes=hy=hz=0; stack=[((0,0,0),1,1)]
 while stack:
  s,p,q=stack.pop(); nodes+=1; n=s[0]
  if s==Y:hy+=1
  if s==Z:hz+=1
  ac=action(s,y,z)
  if ac=='C':
   for i,(pi,qi) in enumerate(zip((3,1,20),(2,2,20))):stack.append((child(s,i),p*pi,q*qi))
  else:
   wt=24**(N-n)
   if ac=='Q':t[0]+=p*wt
   else:t[1]+=q*wt
   t[2]+=n*p*wt; t[3]+=n*q*wt
 return tuple(F(v,24**N) for v in t),nodes,hy,hz
nodes=0
for y,z in product((0,1),repeat=2):
 o,nn,hy,hz=dfs(y,z)
 assert o==O[y,z] and hy==144 and hz==1
 nodes+=nn
assert nodes==542392
z0=F(1525099996562693,81920000000000000)
zs=-F(1050385239,512000000000000)
for y in (F(0),F(1)):
 z=z0+zs*y
 assert 0<z<1
 o=tuple(B[i]+y*DY[i]+z*DZ[i] for i in range(4))
 assert o[0]==o[1] and o[2]>o[3] and o[2]+K*o[1]+L*o[0]==H
 assert o[0]==alpha0+F(13382075,676302730297344)*y
 assert o[2]==V0-F(9579725,1565515579392)*y
assert F(9579725,1565515579392)/F(13382075,676302730297344)==K+L
print('STAGE195_REFERENCE_FULL_REAL_PASS; 680 states; 1238 strict gaps; 542392 ordered DFS nodes')
