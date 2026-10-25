#!/usr/bin/env python3
"""Exact rational Bellman and ordered-history mass derivation for Stage106.
Declared model: external iid ternary observations, stopping by n<=14.
Author calculation, no native project mathematical admission.
"""
from fractions import Fraction as F
from collections import defaultdict
import json
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
K105=F(2212824096,1992661);K=F(107892,101);L=72+F(8,9)*K
A=(11,5,4);B=(12,0,1);OLD_A=(8,5,1)
alpha0=F(38038153259411651,109561042308169728)
V0=F(353483207227801957,27390260577042432)
s0=F(241563037007287,307200000000000)

def states():
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):yield n,a,b
def child(z):
 n,a,b=z;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def lr(z):return F(2**(z[1]+z[2]),3**z[1])
def bell(k):
 d={};ops={};gaps={};ell=72+F(8,9)*k
 for z in states():
  costs={'P':k*lr(z),'Q':ell}
  if z[0]<N:costs['C']=1+sum((P[i]*d[w] for i,w in enumerate(child(z))),F())
  best=min(costs.values());d[z]=best;ops[z]=tuple(a for a,c in costs.items() if c==best)
  gaps[z]={a:c-best for a,c in costs.items()}
 return d,ops,gaps
D,opts,gap=bell(K)
print('states',len(D),'comparisons',sum(len(x)-1 for x in gap.values()),'ties',[(s,o) for s,o in opts.items() if len(o)>1], 'positive',sum(v>0 for x in gap.values() for v in x.values()),'min positive',min(v for x in gap.values() for v in x.values() if v>0))
assert len(D)==680
assert {z for z in opts if len(opts[z])>1}=={A,B}
assert set(opts[A])=={'Q','C'} and set(opts[B])=={'Q','C'}
assert opts[OLD_A]==('P',)
assert sum(v>0 for x in gap.values() for v in x.values())==1238
policy={z:('Q' if z in (A,B) else opts[z][0]) for z in opts}
# check pinned strict policy remains optimal across dual segment K105..K106

def pinned_min(k):
 d={};ell=72+F(8,9)*k;g=[]
 for z in states():
  costs={'P':k*lr(z),'Q':ell}
  if z[0]<N:costs['C']=1+sum((P[i]*d[w] for i,w in enumerate(child(z))),F())
  act=policy[z];d[z]=costs[act];g.extend(c-d[z] for c in costs.values())
 return min(g)
assert pinned_min(K105)==pinned_min(K)==0

hits={(0,0,0):1};mp={(0,0,0):F(1)};mq={(0,0,0):F(1)}
for n in range(N):
 for a in range(n+1):
  for b in range(n-a+1):
   z=n,a,b
   if z not in hits or z in (A,B) or policy[z]!='C':continue
   for i,w in enumerate(child(z)):
    hits[w]=hits.get(w,0)+hits[z]
    mp[w]=mp.get(w,F(0))+mp[z]*P[i]
    mq[w]=mq.get(w,F(0))+mq[z]*Q[i]
assert A in hits and B in hits
assert A[1]>B[1] and A[0]<B[0]
# Exact forced continuation suffix under all strict actions.
strict={}
for z in states():
 act=policy[z]
 if act=='P':out=(F(0),F(1),F(0),F(0),1)
 elif act=='Q':out=(F(1),F(0),F(0),F(0),1)
 else:
  cs=[strict[w] for w in child(z)]
  out=(sum((P[i]*cs[i][0] for i in range(3)),F(0)),sum((Q[i]*cs[i][1] for i in range(3)),F(0)),
   1+sum((P[i]*cs[i][2] for i in range(3)),F(0)),1+sum((Q[i]*cs[i][3] for i in range(3)),F(0)),sum(t[4] for t in cs))
 strict[z]=out

def suffix(z):
 cs=[strict[w] for w in child(z)]
 return (sum((P[i]*cs[i][0] for i in range(3)),F(0)),sum((Q[i]*cs[i][1] for i in range(3)),F(0)),
  1+sum((P[i]*cs[i][2] for i in range(3)),F(0)),1+sum((Q[i]*cs[i][3] for i in range(3)),F(0)),sum(t[4] for t in cs))
RA,RB=suffix(A),suffix(B)
# u=probability to CONTINUE at new A; at u=0 choose Q there.
x=-mp[A]*(1-RA[0]);y=mq[A]*RA[1]
e=mp[B]*(1-RB[0]);f=-mq[B]*RB[1]
c=(y-x)/(e-f);eta=x+e*c
assert eta==y+f*c
s1=s0+c;alpha1=alpha0+eta;V1=V0-(K+L)*eta

def moments(u,s):
 M={}
 for z in states():
  mix=({'Q':1-u,'C':u} if z==A else {'Q':s,'C':1-s} if z==B else {policy[z]:F(1)})
  m=[F(0)]*4
  for act,weight in mix.items():
   if weight==0:continue
   if act=='P':out=(F(0),F(1),F(0),F(0))
   elif act=='Q':out=(F(1),F(0),F(0),F(0))
   else:
    kids=[M[w] for w in child(z)]
    out=(sum((P[i]*kids[i][0] for i in range(3)),F(0)),sum((Q[i]*kids[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*kids[i][2] for i in range(3)),F(0)),1+sum((Q[i]*kids[i][3] for i in range(3)),F(0)))
   for j in range(4):m[j]+=weight*out[j]
  M[z]=tuple(m)
 return M[0,0,0]

out0=moments(F(0),s0)
assert out0[0]==out0[1]==alpha0 and out0[2]==V0, ('previous Stage105 endpoint mismatch',out0)
# Feasible upper u bound from s in [0,1], and/or from P-time domination switch.
u_end=min(F(1),(-s0/c if c<0 else (1-s0)/c if c>0 else F(1)))
s_end=s0+c*u_end
out1=moments(u_end,s_end)
assert out1[0]==out1[1]==alpha0+eta*u_end
assert out1[2]==V0-(K+L)*eta*u_end
assert moments(u_end/2,s0+c*u_end/2)==tuple((a+b)/2 for a,b in zip(out0,out1))
assert 0<=s_end<=1 and eta>0
print('K,L,gamma',K,L,K+L)
print('Droot',D[(0,0,0)],'old dual equality',D[(0,0,0)]-V0-(K+L)*alpha0)
assert D[0,0,0]==V0+(K+L)*alpha0
for z in (A,B):print('HIT',z,hits[z],mp[z],mq[z],'suffix',suffix(z))
print('x,y,e,f',x,y,e,f)
print('c,eta,s_end,u_end',c,eta,s_end,u_end)
print('a_end,V_end',alpha0+eta*u_end,V0-(K+L)*eta*u_end)
print('out0,out1',out0,out1)
print('time dominance:',out0[2]-out0[3],out1[2]-out1[3])
if not (out0[2]>out0[3] and out1[2]>out1[3]):print('WARNING T DOMINANCE NOT VALID')
# candidate lower K: after u_end==1, switch to C at A; if truncated u_end<1, do not assume next breakpoint.
nextcandidate=None
if u_end==1:
 post={**policy,A:'C'};co={};cf={};candidates=[]
 for z in states():
  act=post[z]
  if act=='P':h0,h1=F(0),lr(z)
  elif act=='Q':h0,h1=F(72),F(8,9)
  else:
   h0=1+sum((P[i]*co[w] for i,w in enumerate(child(z))),F(0))
   h1=sum((P[i]*cf[w] for i,w in enumerate(child(z))),F(0))
  co[z],cf[z]=h0,h1
  for alt in (['P','Q']+(['C'] if z[0]<N else [])):
   if alt=='P':k0,k1=F(0),lr(z)
   elif alt=='Q':k0,k1=F(72),F(8,9)
   else:
    k0=1+sum((P[i]*co[w] for i,w in enumerate(child(z))),F(0))
    k1=sum((P[i]*cf[w] for i,w in enumerate(child(z))),F(0))
   g0,g1=k0-h0,k1-h1
   if g1>0 and -g0/g1<K and g0+g1*K>0:candidates.append((-g0/g1,z,alt))
 nextcandidate=max(candidates) if candidates else None
 print('NEXT DUAL ONLY CANDIDATE',nextcandidate)

def ffmt(x):return str(x)
cert={
 'scope':'AUTHOR_EXACT_EXTERNAL_IID_N14_STAGE106',
 'pins':{'global_main':'04aa116d3c89bc5fee453d6467cd87eed27221fe','enterprise_source':'7166bbdfc462e38336b46d55485f8e2cdf2f0b96','predecessor':'research_notes/n14_aux_iid_affine_105_20261025/PROOF_STAGE105.md'},
 'dual':{'K':ffmt(K),'L':ffmt(L),'Gamma':ffmt(K+L),'Droot':ffmt(D[0,0,0]),'states':len(D),'comparisons':sum(len(gs)-1 for gs in gap.values()),'positive':sum(v>0 for gs in gap.values() for v in gs.values()),'negative':0,'ties':{str(z):list(opts[z]) for z in (A,B)},'min_positive':str(min(v for gs in gap.values() for v in gs.values() if v>0)),'K105_to_K106_fixed_policy_gaps':'NONNEGATIVE'},
 'first_hit':{str(z):{'count':hits[z],'P':str(mp[z]),'Q':str(mq[z]),'forced_continue':list(map(str,suffix(z)))} for z in (A,B)},
 'primal':{'alpha_previous':ffmt(alpha0),'V_previous':ffmt(V0),'s_previous':str(s0),'x':str(x),'y':str(y),'e':str(e),'f':str(f),'compensation_c':str(c),'eta_per_unit_u':str(eta),'u_end':str(u_end),'s_end':str(s_end),'alpha_end':str(alpha0+eta*u_end),'V_end':str(V0-(K+L)*eta*u_end),'root0':[str(x) for x in out0],'root1':[str(x) for x in out1],'tP_ge_tQ_at_both_endpoints':out0[2]>=out0[3] and out1[2]>=out1[3]},
 'next_dual_only':{'K':str(nextcandidate[0]),'state':nextcandidate[1],'alt':nextcandidate[2]} if nextcandidate else None,
 'scope_limit':'author proof only; no independent Driver/native CLAIM, no native X6 correspondence'
}
with open('/mnt/data/EM_R1_N14_Stage106_20261025/certificate106.json','w') as fp:json.dump(cert,fp,indent=2,ensure_ascii=False)
print('CERTIFICATE_WRITTEN')
