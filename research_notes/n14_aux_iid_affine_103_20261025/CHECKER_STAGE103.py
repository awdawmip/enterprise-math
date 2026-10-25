#!/usr/bin/env python3
"""Author rational certificate for the EXTERNAL iid N=14 Stage103.
No P000 or native BRC/X6 transfer, no Driver review. Standard library only.
"""
from fractions import Fraction as F
from functools import lru_cache
import json

P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(152847928260,128768917)
L=72+F(8,9)*K
K102=F(96424629120,78169393)
C=(6,2,3)
B=(12,0,1)
N=14
alpha102=F(2586593746940986327,7450150876955541504)
V102=F(751163408448101635,58204303726215168)
s102=F(16418222843481211,20889600000000000)

def ch(v):
 n,a,b=v
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def lik(v):return F(2**(v[1]+v[2]),3**v[1])

def bellman(k):
 lam=72+F(8,9)*k
 D={}; opts={};gap={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b)
    scores={'P':k*lik(v),'Q':lam}
    if n<N:scores['C']=1+sum((P[i]*D[w] for i,w in enumerate(ch(v))),F(0))
    q=min(scores.values());D[v]=q
    opts[v]=tuple(act for act,z in scores.items() if z==q)
    gap[v]={act:z-q for act,z in scores.items()}
 return D,opts,gap
D,opts,gap=bellman(K)
assert len(D)==680
assert sum(len(x)-1 for x in gap.values())==1240
assert sum(x<0 for gg in gap.values() for x in gg.values())==0
assert sum(x>0 for gg in gap.values() for x in gg.values())==1238
assert {v for v in opts if len(opts[v])>1}=={B,C}
minimum_slack=min(x for gg in gap.values() for x in gg.values() if x>0)
assert minimum_slack==F(1445880526288015,32810831006662656)

# First-hits under unique actions outside B,C; reuse state-count DP with integer multiplicities.
count={(0,0,0):1};p={(0,0,0):F(1)};q={(0,0,0):F(1)}
for n in range(N):
 for a in range(n+1):
  for b in range(n-a+1):
   v=(n,a,b)
   if v not in count or v in (B,C) or opts[v][0]!='C':continue
   for i,w in enumerate(ch(v)):
    count[w]=count.get(w,0)+count[v]
    p[w]=p.get(w,0)+p[v]*P[i]
    q[w]=q.get(w,0)+q[v]*Q[i]
assert (count[C],p[C],q[C])==(36,F(5,147456),F(5,41472))
assert (count[B],p[B],q[B])==(12,F(48828125,725594112),F(48828125,362797056))
assert C[1]>B[1] and C[0]<B[0]  # monotone a rules out ancestry

# Conditional continuation suffixes, each computed from the strict continuation policy.
strict={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   v=(n,a,b); act=opts[v][0]
   if act=='Q':z=(F(1),F(0),F(0),F(0),1)
   elif act=='P':z=(F(0),F(1),F(0),F(0),1)
   else:
    ww=[strict[w] for w in ch(v)]
    z=(sum((P[i]*ww[i][0] for i in range(3)),F(0)),
       sum((Q[i]*ww[i][1] for i in range(3)),F(0)),
       1+sum((P[i]*ww[i][2] for i in range(3)),F(0)),
       1+sum((Q[i]*ww[i][3] for i in range(3)),F(0)),
       sum(x[4] for x in ww))
   strict[v]=z

def suffix(v):
 ww=[strict[w] for w in ch(v)]
 return (sum((P[i]*ww[i][0] for i in range(3)),F(0)),
         sum((Q[i]*ww[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*ww[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*ww[i][3] for i in range(3)),F(0)),
         sum(x[4] for x in ww))
rC=suffix(C);rB=suffix(B)
assert rC==(F(1352536571,1358954496),F(381917,429981696),F(267429265,169869312),F(47809387,35831808),279)
assert rB==(F(63,64),F(1,144),F(9,8),F(13,12),5)

# Exact policy moments at root; coordinates are (eP,eQ,tP,tQ).
def moments(u,s):
 W={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b)
    acts=({'Q':u,'C':1-u} if v==C else
          {'Q':s,'C':1-s} if v==B else {opts[v][0]:F(1)})
    y=[F(0)]*4
    for act,wt in acts.items():
     if act=='Q':z=(F(1),F(0),F(0),F(0))
     elif act=='P':z=(F(0),F(1),F(0),F(0))
     else:
      ww=[W[w] for w in ch(v)]
      z=(sum((P[i]*ww[i][0] for i in range(3)),F(0)),
         sum((Q[i]*ww[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*ww[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*ww[i][3] for i in range(3)),F(0)))
     for j in range(4):y[j]+=wt*z[j]
    W[v]=tuple(y)
 return W[0,0,0]

x=p[C]*(1-rC[0]);y=q[C]*rC[1];e=p[B]*(1-rB[0]);h=q[B]*rB[1]
comp=-(x+y)/(e+h)
eta=x+e*comp
s103=s102+comp
alpha103=alpha102+eta
G=L+K
V103=V102-G*eta
assert (comp,eta,s103)==(F(-23421994167,174080000000000),F(643844585,34491439245164544),F(16415412204181171,20889600000000000))
assert alpha103==F(2586593886011416687,7450150876955541504)
assert V103==F(3004643576828511655,232817214904860672)
assert 0<s103<s102<1 and eta>0
out0=moments(F(0),s102);out1=moments(F(1),s103)
assert out0==(alpha102,alpha102,V102,F(22836431111877252545,1862537719238885376))
assert out1==(alpha103,alpha103,V103,F(22836168034496950505,1862537719238885376))
assert out0[2]>out0[3] and out1[2]>out1[3]
assert out0[2]+L*out0[0]+K*out0[1]==D[0,0,0]
assert out1[2]+L*out1[0]+K*out1[1]==D[0,0,0]
assert moments(F(1,2),(s102+s103)/2)==tuple((a+b)/2 for a,b in zip(out0,out1))

# Same post-Stage102 strict policy is affine in K on [K103,K102].
def pinned_gap_at(kk):
 lam=72+F(8,9)*kk; d={}; diffs=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b)
    # At the new tie C, choose continue for the upper-K side.
    act='C' if v==C else opts[v][0]
    scores={'P':kk*lik(v),'Q':lam}
    if n<N:scores['C']=1+sum((P[i]*d[w] for i,w in enumerate(ch(v))),F(0))
    d[v]=scores[act]
    diffs.extend(z-d[v] for z in scores.values())
 return diffs
assert min(pinned_gap_at(K102))==min(pinned_gap_at(K))==0
# All fixed-policy gap expressions are affine, so endpoint nonnegativity is enough.

# Next lower K root under post-Stage103 policy: affine exact (constant, K coefficient).
const={};coeff={}; candidates=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   v=(n,a,b);act=opts[v][0]
   if act=='P':c,t=F(0),lik(v)
   elif act=='Q':c,t=F(72),F(8,9)
   else:
    c=1+sum((P[i]*const[w] for i,w in enumerate(ch(v))),F(0))
    t=sum((P[i]*coeff[w] for i,w in enumerate(ch(v))),F(0))
   const[v],coeff[v]=c,t
   for candidate in ('P','Q','C') if n<N else ('P','Q'):
    if candidate=='P':cc,tt=F(0),lik(v)
    elif candidate=='Q':cc,tt=F(72),F(8,9)
    else:
     cc=1+sum((P[i]*const[w] for i,w in enumerate(ch(v))),F(0))
     tt=sum((P[i]*coeff[w] for i,w in enumerate(ch(v))),F(0))
    dc,dt=cc-c,tt-t
    if dt>0 and -dc/dt<K and dc+dt*K>0:candidates.append((-dc/dt,v,candidate))
K104,v104,act104=max(candidates)
assert (K104,v104,act104)==(F(4881384,4373),(11,8,3),'P')

f=lambda z:str(z)
record={
 'scope':'AUTHOR_EXACT_EXTERNAL_IID_N14','P':[f(x) for x in P],'Q':[f(x) for x in Q],
 'dual':{'K103':f(K),'lambdaP':f(L),'root':f(D[0,0,0]),'gamma':f(G),'states':len(D),'comparisons':1240,'strict_positive':1238,'negative':0,'ties':['(6,2,3):Q/C','(12,0,1):Q/C'],'minimum_strict_positive_gap':f(minimum_slack)},
 'first_hits':{'C':{'state':list(C),'count':count[C],'P':f(p[C]),'Q':f(q[C]),'suffix':[f(x) for x in rC]},'B':{'state':list(B),'count':count[B],'P':f(p[B]),'Q':f(q[B]),'suffix':[f(x) for x in rB]}},
 'primal':{'alpha102':f(alpha102),'alpha103':f(alpha103),'eta103':f(eta),'V102':f(V102),'V103':f(V103),'s102':f(s102),'s103':f(s103),'s_change_per_u':f(comp),'root_outcomes':[list(map(f,x)) for x in (out0,out1)],'tP_gt_tQ_endpoints':True},
 'next_dual_only':{'K104':f(K104),'state':list(v104),'new_tie_action':act104},
 'checks':{'endpoint_gap_pencil_K102_K103':'PASS','Bellman':'PASS','primal':'PASS','sharp_right_support':'PROVED_BY_ONLY_TWO_TIES_AND_POSITIVE_MULTIPLIERS'},
 'scientific_scope':'author check only; no independent Driver acceptance; no native BRC/X6/P000 correspondence',
}
print(json.dumps(record,ensure_ascii=False,indent=2))
