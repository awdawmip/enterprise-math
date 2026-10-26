#!/usr/bin/env python3
"""Compact exact replayer of Stage166 author theorem: Fraction Bellman + two observers."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(310447538892,1139969309);L=F(912521643352,3419907927)
R=(10,0,1);Y=(7,4,1); ACT=('P','Q','C')
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
@lru_cache(None)
def bell(s):
 v=[K*ell(s),L]
 if s[0]<N:v.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
 m=min(v);return m,tuple(a for a,z in zip(ACT,v) if z==m),v
strict={};tie={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);m,w,v=bell(s)
   if len(w)>1:tie[s]=w
   else:strict[s]=w[0]
   gaps.extend(z-m for z in v if z>m)
assert tie=={R:('Q','C'),Y:('P','C')}
assert len(strict)==678 and len(gaps)==1238
assert min(gaps)==F(8257109179793,957355345452672)
H=bell((0,0,0))[0]
assert H==F(74798213336514089844785955701,374688677080092029648633856)
def action(s,r,y):
 if s==R:return 'Q' if r else 'C'
 if s==Y:return 'P' if y else 'C'
 return strict[s]
def suffix(r,y):
 @lru_cache(None)
 def calc(s):
  act=action(s,r,y)
  if act=='P':return(F(0),F(1),F(0),F(0))
  if act=='Q':return(F(1),F(0),F(0),F(0))
  c=[calc(child(s,i)) for i in range(3)]
  return(sum((P[i]*c[i][0] for i in range(3)),F(0)),
         sum((Q[i]*c[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*c[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*c[i][3] for i in range(3)),F(0)))
 return calc((0,0,0))
def dfs(r,y):
 pn=(3,1,20);qn=(1,1,10);acc=defaultdict(int);nodes=0
 hits={R:[0,F(0),F(0)],Y:[0,F(0),F(0)]}
 def walk(n,a,b,p,q):
  nonlocal nodes
  nodes+=1;s=(n,a,b)
  if s in hits:
   hits[s][0]+=1;hits[s][1]+=F(p,24**n);hits[s][2]+=F(q,12**n)
  z=action(s,r,y)
  if z=='C':
   for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
  else:
   acc[n,'ap']+=p;acc[n,'aq']+=q;acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
   if z=='P':acc[n,'eq']+=q
   else:acc[n,'ep']+=p
 walk(0,0,0,1,1)
 mass=lambda k,b:sum((F(acc[n,k],b**n) for n in range(N+1)),F(0))
 assert mass('ap',24)==mass('aq',12)==1
 return(mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes
C={};hits0=None;counts=[]
for r in (0,1):
 for y in (0,1):
  sv=suffix(r,y);dv,h,count=dfs(r,y)
  assert sv==dv
  C[r,y]=sv;counts.append(count)
  if hits0 is None:hits0=h
  else:assert hits0==h
assert counts==[408976,387997,408736,387757]
assert hits0[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert hits0[Y]==[63,F(175,393216),F(175,995328)]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=C[0,0];dr=sub(C[1,0],base);dy=sub(C[0,1],base)
assert sub(sub(C[1,1],C[1,0]),dy)==(F(0),)*4
D=lambda x:x[0]-x[1]
r0=-D(base)/D(dr);rs=-D(dy)/D(dr)
assert r0==F(3610801514373861,11823616000000000)
assert rs==F(33168957903,21113600000000)
v=lambda y:tuple(base[i]+(r0+rs*y)*dr[i]+y*dy[i] for i in range(4))
l=v(F(0));h=v(F(1))
assert 0<r0<r0+rs<1
assert l[0]==l[1]==F(881259282664541428015,2530093150022563528704)
assert l[2]==F(4277168009143268563157,361441878574651932672)
assert h[0]==h[1]==F(881262643750052083615,2530093150022563528704)
assert h[2]==F(4276909130601160631957,361441878574651932672)
assert h[0]-l[0]==F(370490025425,278890338406367232)
assert l[2]>l[3] and h[2]>h[3]
assert all(z[2]+K*z[1]+L*z[0]==H for z in (l,h))
assert h[2]-l[2]==-(K+L)*(h[0]-l[0])
print("STAGE166_AUTHOR_EXACT_PASS",len(strict)+len(tie),len(gaps),sum(counts))
print("alpha166",h[0],"V166",h[2],"width",h[0]-l[0])
