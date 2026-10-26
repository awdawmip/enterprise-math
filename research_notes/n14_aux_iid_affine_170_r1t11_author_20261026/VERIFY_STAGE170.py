#!/usr/bin/env python3
"""Stage170 exact author checker: all 680 IID count states, all 4 coins,
independent ordered-history integer-numerator DFS. External N<=14 model only.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import product
N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
PN=(3,1,20); QN=(1,1,10)
K=F(4773735,18929); L=F(14183320,56787)
R=(10,0,1); T=(12,5,2)
A0=F(882433753904177815735,2530093150022563528704)
V0=F(4191297370163761372757,361441878574651932672)
A1=F(126062165849964145105,361441878574651932672)
V1=F(4191196473918241372757,361441878574651932672)
def ch(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
 o=[K*lr(s),L]
 if s[0]<N:o.append(1+sum(P[i]*bell(ch(s,i))[0] for i in range(3)))
 return min(o),o
policy={};ties={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,opts=bell(s);idx=[i for i,x in enumerate(opts) if x==v]
   if len(idx)>1:ties[s]=tuple('PQC'[i] for i in idx)
   else:policy[s]='PQC'[idx[0]]
   gaps.extend(x-v for x in opts if x>v)
H=bell((0,0,0))[0]
assert len(policy)+len(ties)==680 and len(gaps)==1238
assert min(gaps)==F(569,56787)
assert ties=={R:('Q','C'),T:('P','C')}
assert H==F(290341590799397120042729,1555410727388508585984)
def act(s,r,t):return ('Q' if r else 'C') if s==R else ('P' if t else 'C') if s==T else policy[s]
def suffix(r,t):
 @lru_cache(None)
 def go(s):
  k=act(s,r,t)
  if k=='P':return(F(0),F(1),F(0),F(0))
  if k=='Q':return(F(1),F(0),F(0),F(0))
  z=[go(ch(s,i)) for i in range(3)]
  return tuple([sum(P[i]*z[i][0] for i in range(3)),
                sum(Q[i]*z[i][1] for i in range(3)),
                1+sum(P[i]*z[i][2] for i in range(3)),
                1+sum(Q[i]*z[i][3] for i in range(3))])
 return go((0,0,0))
def ordered(r,t):
 sums=defaultdict(int); hits={R:[0,F(0),F(0)],T:[0,F(0),F(0)]};term=[0]
 def walk(n,a,b,p,q):
  s=(n,a,b)
  if s in hits:
   hits[s][0]+=1;hits[s][1]+=F(p,24**n);hits[s][2]+=F(q,12**n)
  k=act(s,r,t)
  if k!='C':
   term[0]+=1
   for name,w in [('pm',p),('qm',q),('tp',n*p),('tq',n*q)]:sums[n,name]+=w
   if k=='P':sums[n,'eq']+=q
   else:sums[n,'ep']+=p
   return
  for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*PN[i],q*QN[i])
 walk(0,0,0,1,1)
 def total(key,d):return sum((F(sums[n,key],d**n) for n in range(N+1)),F(0))
 assert total('pm',24)==total('qm',12)==1
 return (total('ep',24),total('eq',12),total('tp',24),total('tq',12)),hits,term[0]
corner={};first_hits=None;counts={}
for r,t in product((0,1),repeat=2):
 s=suffix(r,t);o,h,count=ordered(r,t)
 assert s==o,(r,t,s,o)
 assert first_hits is None or h==first_hits
 corner[r,t]=s;first_hits=h;counts[r,t]=count
assert first_hits[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert first_hits[T]==[5162,F(8065625,73383542784),F(8065625,139314069504)]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda k,a:tuple(k*x for x in a)
m=corner[0,0];dr=sub(corner[1,0],m);dt=sub(corner[0,1],m)
assert sub(sub(corner[1,1],corner[0,1]),dr)==(F(0),)*4
err=lambda v:v[0]-v[1]
r0=-err(m)/err(dr);rs=-err(dt)/err(dr)
assert r0==F(8976558429259453,11823616000000000)
assert rs==F(5541407,3694880000)
obs=lambda r,t:add(add(m,scale(r,dr)),scale(t,dt))
left,right=obs(r0,0),obs(r0+rs,1)
assert 0<r0<r0+rs<1
assert left[0]==left[1]==A0 and left[2]==V0 and left[2]>left[3]
assert right[0]==right[1]==A1 and right[2]==V1 and right[2]>right[3]
assert left[2]+K*left[1]+L*left[0]==H
assert right[2]+K*right[1]+L*right[0]==H
assert A1-A0==F(152674215625,274532676868767744)
assert V0-V1==(K+L)*(A1-A0)
assert R[0]<T[0] and T[1]-R[1]>T[0]-R[0] # disjoint prefix cones
print('PASS: Bellman 680 states, 1238 positive gaps, exactly R/T ties')
print('PASS: 4 corners by Fraction suffix and independent ordered integer DFS')
print('PASS: first hits',first_hits,'terminal DFS leaves',counts)
print('PASS: affine mixed term=0; balanced coins r(t)=',r0,'+',rs,'t')
print('PASS: inherited alpha/V',A0,V0)
print('PASS: right alpha/V',A1,V1,'width',A1-A0)
print('PASS: dual root',H,'slope',K+L,'min strict gap',min(gaps))
print('STATUS: AUTHOR_EXACT_STAGE170; NATIVE_REVIEW_PENDING; X6_TRANSFER_UNPROVED')
