#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
import json
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=14
K=F(2212824096,1992661)
L=F(72)+F(8,9)*K
A=(8,5,1);B=(12,0,1)
a104=F(646648471503178867,1862537719238885376)
v104=F(6009287153480025269,465634429809721344)
s104=F(4103853056103079,5222400000000000)
K104=F(4881384,4373)

def children(z):
 n,a,b=z;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def likelihood(z):return F(2**(z[1]+z[2]),3**z[1])
def bell(k):
 l=F(72)+F(8,9)*k;D={};O={};G={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    z=(n,a,b);cost={'P':k*likelihood(z),'Q':l}
    if n<N:cost['C']=1+sum((P[i]*D[w] for i,w in enumerate(children(z))),F(0))
    lo=min(cost.values());D[z]=lo;O[z]=tuple(a for a,v in cost.items() if v==lo);G[z]={a:v-lo for a,v in cost.items()}
 return D,O,G
D,O,gap=bell(K)
print('states',len(D),'comparisons',sum(len(g)-1 for g in gap.values()),'tied',[(z,oo) for z,oo in O.items() if len(oo)>1]);print('positive',sum(v>0 for g in gap.values() for v in g.values()),'minimum',min(v for g in gap.values() for v in g.values() if v>0));print('L,K,D0',L,K,D[0,0,0]);print('D0 - V104 - alpha104*(L+K)',D[0,0,0]-v104-a104*(L+K))
assert {z for z,o in O.items() if len(o)>1}=={A,B}
policy={z:('C' if z in (A,B) else o[0]) for z,o in O.items()}
# Mass of reached ordered words before either tie, using distinct paths only.
nh={(0,0,0):1};mp={(0,0,0):F(1)};mq={(0,0,0):F(1)}
for n in range(N):
 for a in range(n+1):
  for b in range(n-a+1):
   z=(n,a,b)
   if z not in nh or z in (A,B) or policy[z]!='C':continue
   for i,w in enumerate(children(z)):
    nh[w]=nh.get(w,0)+nh[z];mp[w]=mp.get(w,F(0))+mp[z]*P[i];mq[w]=mq.get(w,F(0))+mq[z]*Q[i]
print('hitsA',nh.get(A,0),mp.get(A),mq.get(A));print('hitsB',nh.get(B,0),mp.get(B),mq.get(B))
# All strict Bellman actions below tie states; continued B and A  policy.
strict={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   z=(n,a,b);act=policy[z]
   if act=='P':strict[z]=(F(0),F(1),F(0),F(0),1)
   elif act=='Q':strict[z]=(F(1),F(0),F(0),F(0),1)
   else:
    w=[strict[t] for t in children(z)]
    strict[z]=(sum((P[i]*w[i][0] for i in range(3)),F(0)),sum((Q[i]*w[i][1] for i in range(3)),F(0)),1+sum((P[i]*w[i][2] for i in range(3)),F(0)),1+sum((Q[i]*w[i][3] for i in range(3)),F(0)),sum(v[4] for v in w))
def suffix(z):
 w=[strict[t] for t in children(z)]
 return (sum((P[i]*w[i][0] for i in range(3)),F(0)),sum((Q[i]*w[i][1] for i in range(3)),F(0)),1+sum((P[i]*w[i][2] for i in range(3)),F(0)),1+sum((Q[i]*w[i][3] for i in range(3)),F(0)),sum(v[4] for v in w))
rA=suffix(A);rB=suffix(B)
print('suffixA',rA,'suffixB',rB)
# new P early instead of continuation => d error P = -mp*continuation P-error, Q = mq*(1-continuation Q-error)
x=-mp[A]*rA[0];y=mq[A]*(1-rA[1]);e=mp[B]*(1-rB[0]);f=-mq[B]*rB[1]
c=(y-x)/(e-f);eta=x+e*c
print('x,y,e,f',x,y,e,f);print('compensation c',c,'eta',eta,'etaQ',y+f*c,'s105',s104+c)
a105=a104+eta;v105=v104-(K+L)*eta
print('alpha105',a105,'V105',v105,'gamma',K+L)
assert eta>0 and 0<s104<s104+c<1
assert eta==y+f*c
assert D[0,0,0]==v104+(L+K)*a104

def moments(u,s):
 W={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    z=(n,a,b)
    acts=({'P':u,'C':1-u} if z==A else {'Q':s,'C':1-s} if z==B else {policy[z]:F(1)})
    m=[F(0)]*4
    for act,weight in acts.items():
     if act=='Q':v=(F(1),F(0),F(0),F(0))
     elif act=='P':v=(F(0),F(1),F(0),F(0))
     else:
      w=[W[q] for q in children(z)]
      v=(sum((P[i]*w[i][0] for i in range(3)),F(0)),sum((Q[i]*w[i][1] for i in range(3)),F(0)),1+sum((P[i]*w[i][2] for i in range(3)),F(0)),1+sum((Q[i]*w[i][3] for i in range(3)),F(0)))
     for j in range(4):m[j]+=weight*v[j]
    W[z]=tuple(m)
 return W[0,0,0]
o0=moments(F(0),s104);o1=moments(F(1),s104+c);om=moments(F(1,2),s104+c/2)
print('endpoint0',o0);print('endpoint1',o1);print('midpoint',om)
assert o0[:3]==(a104,a104,v104)
assert o1[:3]==(a105,a105,v105)
assert o0[2]>o0[3] and o1[2]>o1[3]
assert om==tuple((q+r)/2 for q,r in zip(o0,o1))
# Check fixed policy pencil from K105 to K104 inclusive.
def pin_gap(k):
 l=F(72)+F(8,9)*k;d={};lowest=F(0)
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    z=n,a,b; costs={'P':k*likelihood(z),'Q':l}
    if n<N:costs['C']=1+sum((P[i]*d[w] for i,w in enumerate(children(z))),F(0))
    d[z]=costs[policy[z]]
    lowest=min(lowest,*(v-d[z] for v in costs.values()))
 return lowest
assert pin_gap(K104)==pin_gap(K)==0
# Find first new tie below K105 after setting A=P
post={**policy,A:'P'};co={};cf={};cand=[]
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
   for op in (('P','Q','C') if n<N else ('P','Q')):
    if op=='P':d0,d1=F(0),likelihood(z)
    elif op=='Q':d0,d1=F(72),F(8,9)
    else:
     d0=1+sum((P[i]*co[w] for i,w in enumerate(children(z))),F(0))
     d1=sum((P[i]*cf[w] for i,w in enumerate(children(z))),F(0))
    h0,h1=d0-c0,d1-c1
    if h1>0 and -h0/h1<K and h0+h1*K>0:cand.append((-h0/h1,z,op))
print('candidate nearest',max(cand) if cand else None)
print('other top candidates',sorted(cand,reverse=True)[:5])
# One verified portable structured certificate.
def s(x):return str(x)
cert={'scope':'AUTHOR_EXACT_EXTERNAL_IID_N14','stage':105,'dual':{'K105':s(K),'lambdaP':s(L),'gamma':s(K+L),'root':s(D[0,0,0]),'states':len(D),'comparisons':sum(len(g)-1 for g in gap.values()),'strict_positive':sum(v>0 for g in gap.values() for v in g.values()),'negative':sum(v<0 for g in gap.values() for v in g.values()),'ties':{str(z):list(acts) for z,acts in O.items() if len(acts)>1},'min_strict_positive_gap':s(min(v for g in gap.values() for v in g.values() if v>0))},'first_hits':{str(z):{'state':list(z),'count':nh[z],'P':s(mp[z]),'Q':s(mq[z]),'continuation_suffix':[s(x) for x in suffix(z)]} for z in (A,B)},'responses':{'x':s(x),'y':s(y),'e':s(e),'f':s(f)},'primal':{'alpha104':s(a104),'alpha105':s(a105),'eta105':s(eta),'V104':s(v104),'V105':s(v105),'s104':s(s104),'s105':s(s104+c),'compensation_per_u':s(c),'endpoints':[[s(v) for v in o] for o in (o0,o1)],'tP_gt_tQ_endpoints':True},'next_dual_only':{'K106':s(max(cand)[0]),'state':list(max(cand)[1]),'new_tie_action':max(cand)[2]},'verified':{'Bellman':True,'primal':True,'pencil_gap_at_K104_K105':True,'full_real_interval_via_cone_disjointness':True,'sharp_right_support_via_exact_two_ties':True},'scientific_scope':'author exact proof external iid only; native claim and Driver review unverified'}
with open('/mnt/data/EM_N14_STAGE105_WORK/certificate105.json','w') as f:json.dump(cert,f,ensure_ascii=False,indent=2)
print('STAGE105 PASS')
