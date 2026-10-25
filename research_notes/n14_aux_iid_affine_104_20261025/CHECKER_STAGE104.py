#!/usr/bin/env python3
"""Portable exact Fraction checker for AUTHOR-only external iid N14 Stage104.
All operations are rational; no native P000/X6 theorem or Driver admission.
"""
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=14
K=F(4881384,4373)
L=72+F(8,9)*K
A=(11,8,3);B=(12,0,1)
a103=F(2586593886011416687,7450150876955541504)
v103=F(3004643576828511655,232817214904860672)
s103=F(16415412204181171,20889600000000000)
def children(v):
 n,a,b=v
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def likelihood(v):return F(2**(v[1]+v[2]),3**v[1])
def bell(k):
 l=72+F(8,9)*k; d={};o={};g={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    z=n,a,b;cost={'P':k*likelihood(z),'Q':l}
    if n<N:cost['C']=1+sum((P[i]*d[w] for i,w in enumerate(children(z))),F(0))
    best=min(cost.values());d[z]=best
    o[z]=tuple(t for t,q in cost.items() if q==best)
    g[z]={t:q-best for t,q in cost.items()}
 return d,o,g
D,O,gap=bell(K)
assert len(D)==680 and sum(len(g)-1 for g in gap.values())==1240
assert sum(v>0 for g in gap.values() for v in g.values())==1238
assert sum(v<0 for g in gap.values() for v in g.values())==0
assert {z for z,x in O.items() if len(x)>1}=={A,B}
assert set(O[A])=={'P','C'} and set(O[B])=={'Q','C'}
assert min(v for g in gap.values() for v in g.values() if v>0)==F(2872871,362714112)
assert D[0,0,0]==F(92221588169006115988373,119777609503406555136)
policy={z:('C' if z==A else o[0]) for z,o in O.items()}
assert policy[(6,2,3)]=='Q'
# genuine first hits: record ordered word multiplicity as well as full P,Q mass
hits={(0,0,0):1};mp={(0,0,0):F(1)};mq={(0,0,0):F(1)}
for n in range(N):
 for a in range(n+1):
  for b in range(n-a+1):
   z=n,a,b
   if z not in hits or z in (A,B) or policy[z]!='C':continue
   for i,w in enumerate(children(z)):
    hits[w]=hits.get(w,0)+hits[z]
    mp[w]=mp.get(w,F(0))+mp[z]*P[i]
    mq[w]=mq.get(w,F(0))+mq[z]*Q[i]
assert (hits[A],mp[A],mq[A])==(66,F(11,38654705664),F(11,123834728448))
assert (hits[B],mp[B],mq[B])==(12,F(48828125,725594112),F(48828125,362797056))
assert A[0]<B[0] and A[1]>B[1]
# conditional continuation output eP,eQ,timeP,timeQ,terminal word count
strict={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   z=n,a,b;act=policy[z]
   if act=='P':out=(F(0),F(1),F(0),F(0),1)
   elif act=='Q':out=(F(1),F(0),F(0),F(0),1)
   else:
    w=[strict[q] for q in children(z)]
    out=(sum((P[i]*w[i][0] for i in range(3)),F(0)),
         sum((Q[i]*w[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*w[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*w[i][3] for i in range(3)),F(0)),
         sum(q[4] for q in w))
   strict[z]=out
def suffix(z):
 w=[strict[q] for q in children(z)]
 return (sum((P[i]*w[i][0] for i in range(3)),F(0)),
         sum((Q[i]*w[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*w[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*w[i][3] for i in range(3)),F(0)),
         sum(q[4] for q in w))
rA=suffix(A);rB=suffix(B)
assert rA==(F(41,13824),F(569,576),F(69,64),F(167,144),9)
assert rB==(F(63,64),F(1,144),F(9,8),F(13,12),5)
def moments(u,s):
 W={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    z=n,a,b
    acts=({'P':u,'C':1-u} if z==A else
          {'Q':s,'C':1-s} if z==B else {policy[z]:F(1)})
    m=[F(0)]*4
    for act,weight in acts.items():
     if act=='Q':v=(F(1),F(0),F(0),F(0))
     elif act=='P':v=(F(0),F(1),F(0),F(0))
     else:
      w=[W[q] for q in children(z)]
      v=(sum((P[i]*w[i][0] for i in range(3)),F(0)),
         sum((Q[i]*w[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*w[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*w[i][3] for i in range(3)),F(0)))
     for j in range(4):m[j]+=weight*v[j]
    W[z]=tuple(m)
 return W[0,0,0]
x=-mp[A]*rA[0];y=mq[A]*(1-rA[1])
e=mp[B]*(1-rB[0]);f=-mq[B]*rB[1]
c=(y-x)/(e-f)
eta=x+e*c
assert (x,y,e,f)==(F(-451,534362651099136),F(77,71328803586048),F(48828125,46438023168),F(-48828125,52242776064))
assert c==F(1348743,1392640000000000) and eta==F(48103,275931513961316352)
assert eta==y+f*c and eta>0
s104=s103+c
a104=a103+eta
v104=v103-(K+L)*eta
assert (s104,a104,v104)==(F(4103853056103079,5222400000000000),F(646648471503178867,1862537719238885376),F(6009287153480025269,465634429809721344))
assert 0<s103<s104<1
o0=moments(F(0),s103);o1=moments(F(1),s104)
assert o0==(a103,a103,v103,F(22836168034496950505,1862537719238885376))
assert o1==(a104,a104,v104,F(5709042008510518661,465634429809721344))
assert o0[2]>o0[3] and o1[2]>o1[3]
assert moments(F(1,2),(s103+s104)/2)==tuple((a+b)/2 for a,b in zip(o0,o1))
assert o0[2]+L*o0[0]+K*o0[1]==o1[2]+L*o1[0]+K*o1[1]==D[0,0,0]
# Verify every fixed-policy gap at both ends of the dual pencil; each is affine.
def pinned_gaps(k):
 l=72+F(8,9)*k;d={};g=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    z=n,a,b;cost={'P':k*likelihood(z),'Q':l}
    if n<N:cost['C']=1+sum((P[i]*d[w] for i,w in enumerate(children(z))),F(0))
    d[z]=cost[policy[z]]
    g.extend(q-d[z] for q in cost.values())
 return min(g)
assert pinned_gaps(F(152847928260,128768917))==pinned_gaps(K)==0
# Find the first lower K at which the post-Stage104 strict policy develops a new tie.
post={**policy,A:'P'};co={};cf={};candidate=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   z=n,a,b;act=post[z]
   if act=='P':c0,c1=F(0),likelihood(z)
   elif act=='Q':c0,c1=F(72),F(8,9)
   else:
    c0=1+sum((P[i]*co[w] for i,w in enumerate(children(z))),F(0))
    c1=sum((P[i]*cf[w] for i,w in enumerate(children(z))),F(0))
   co[z],cf[z]=c0,c1
   for option in (('P','Q','C') if n<N else ('P','Q')):
    if option=='P':d0,d1=F(0),likelihood(z)
    elif option=='Q':d0,d1=F(72),F(8,9)
    else:
     d0=1+sum((P[i]*co[w] for i,w in enumerate(children(z))),F(0))
     d1=sum((P[i]*cf[w] for i,w in enumerate(children(z))),F(0))
    a0,a1=d0-c0,d1-c1
    if a1>0 and -a0/a1<K and a0+a1*K>0:candidate.append((-a0/a1,z,option))
assert max(candidate)==(F(2212824096,1992661),(8,5,1),'P')
print('PASS_STAGE104 exact 680 states / 1240 comparisons; alpha104=',a104,'V104=',v104,'next K105=',max(candidate)[0])
