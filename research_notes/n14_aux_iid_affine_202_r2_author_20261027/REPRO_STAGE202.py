"""Independent compact Stage202 exact test: rational DAG + integer ordered DFS."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
P=tuple(map(lambda v:F(v,24),(3,1,20)))
Q=tuple(map(lambda v:F(v,24),(2,2,20)))
K=F(94363551,741293)
H=F(18568821153724089963922211,185638477110285856407552)
R=(6,0,1);Z=(14,0,0);S=(0,0,0)
def step(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def h(s):
 d={'P':K*lr(s),'Q':K}
 if s[0]<14:d['C']=1+sum(P[i]*h(step(s,i))[0] for i in range(3))
 v=min(d.values());return v,tuple(a for a in d if d[a]==v),tuple(t-v for t in d.values() if t>v)
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(states)==680 and h(S)[0]==H
assert {s:h(s)[1] for s in states if len(h(s)[1])>1}=={R:('Q','C'),Z:('P','Q')}
gaps=[g for s in states for g in h(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(16319029,1441073592)
def action(s,r,z):
 if s==R:return 'Q' if r else 'C'
 if s==Z:return 'P' if z else 'Q'
 return h(s)[1][0]
@lru_cache(None)
def obs(s,r,z):
 a=action(s,r,z)
 if a=='P':return F(0),F(1),F(0),F(0)
 if a=='Q':return F(1),F(0),F(0),F(0)
 cs=[obs(step(s,i),r,z) for i in range(3)]
 return tuple(sum((P if j%2==0 else Q)[i]*cs[i][j] for i in range(3))+int(j>=2) for j in range(4))
def integer_dfs(r,z):
 total=[0]*4;cnt=0;arrival=[0]*3
 def visit(s,p,q,hit=False):
  nonlocal cnt
  cnt+=1;n=s[0]
  if s==R:arrival[0]+=1;hit=True
  if s==Z:arrival[1]+=1;arrival[2]+=hit
  a=action(s,r,z)
  if a=='C':
   for i in range(3):visit(step(s,i),p*(3,1,20)[i],q*(2,2,20)[i],hit)
  else:
   m=24**(14-n)
   if a=='P':total[1]+=q*m
   else:total[0]+=p*m
   total[2]+=n*p*m;total[3]+=n*q*m
 visit(S,1,1)
 return tuple(F(v,24**14) for v in total),cnt,arrival
O={};visits=0
for r,z in product((0,1),repeat=2):
 k=f'{r}{z}';O[k]=obs(S,r,z)
 check,n,a=integer_dfs(r,z)
 assert check==O[k] and a==[6,1,0]
 visits+=n
assert visits==389800
v=O['00'];dr=tuple(O['10'][i]-v[i] for i in range(4))
dz=tuple(O['01'][i]-v[i] for i in range(4))
mix=tuple(O['11'][i]-O['10'][i]-O['01'][i]+v[i] for i in range(4))
assert mix==(0,0,0,0)
err=lambda t:t[0]-t[1]
z0=-err(v)/err(dz);zs=-err(dr)/err(dz)
assert z0==F(57523270994401049,819200000000000000)
assert zs==F(3361047,50000000)
assert 0<z0<z0+zs<1
def balanced(r):return tuple(v[i]+r*dr[i]+(z0+r*zs)*dz[i] for i in range(4))
l=balanced(F(0));u=balanced(F(1))
assert l[0]==l[1]==F(3705289910272792345,10517860061584293888)
assert l[2]==F(2265238509513884573,219122084616339456)
assert u[0]==u[1]==F(3712577116979992345,10517860061584293888)
assert u[2]==F(2226587199024284573,219122084616339456)
assert u[0]-l[0]==F(2316540625,3343537668096)
assert all(t[2]>t[3] and t[2]+K*(t[0]+t[1])==H for t in (l,u))
print('STAGE202_REFERENCE_FULL_REAL_PASS',len(states),len(gaps),visits)
