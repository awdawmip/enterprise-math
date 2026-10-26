#!/usr/bin/env python3
"""Exact one-ray dual scan from Stage146 endpoint, external ternary N14.
Author-only dual discovery; does not establish a Stage147 primal interval.
"""
from fractions import Fraction as F
from collections import defaultdict
import json
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(580442338958517,1418470016864);L=F(52669253445512,132981564081)
T=(7,1,2);U=(8,6,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def ch(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
H={};gradient={};acts={};ties=[]
for s in reversed(S):
 cand={'P':K*ratio(s),'Q':L}
 grad={'P':(ratio(s),F()),'Q':(F(),F(1))}
 if s[0]<14:
  cand['C']=1+sum((P[i]*H[t] for i,t in enumerate(ch(s))),F())
  grad['C']=(sum((P[i]*gradient[t][0] for i,t in enumerate(ch(s))),F()),sum((P[i]*gradient[t][1] for i,t in enumerate(ch(s))),F()))
 low=min(cand.values());opt=tuple(a for a,c in cand.items() if c==low)
 if len(opt)>1:ties.append((s,opt))
 # Use strict-minimizer, ties choose Q at T, P at U
 chosen=opt[0];H[s]=low;gradient[s]=grad[chosen];acts[s]=chosen
assert set(ties)=={(T,('Q','C')),(U,('P','C'))}
# dK=-1, dL ratio such that T Q/C exact directional tie
Ct=tuple(sum((P[i]*gradient[t][j] for i,t in enumerate(ch(T))),F()) for j in (0,1))
dK=F(-1);dL=dK*Ct[0]/(1-Ct[1])
assert Ct[1]!=1 and dK<0 and dL<0
slopes={};closure=[];tiegrad=[]
for s in reversed(S):
 cand={'P':K*ratio(s),'Q':L}
 grads={'P':ratio(s)*dK,'Q':dL}
 if s[0]<14:
  cand['C']=1+sum((P[i]*H[t] for i,t in enumerate(ch(s))),F())
  grads['C']=sum((P[i]*slopes[t] for i,t in enumerate(ch(s))),F())
 choose=acts[s]
 slopes[s]=grads[choose]
 for action in cand:
  if action==choose:continue
  gap=cand[action]-H[s]
  dgap=grads[action]-slopes[s]
  if gap==0:
   tiegrad.append((s,choose,action,dgap))
   assert dgap>=0,(s,choose,action,dgap)
  elif dgap<0:closure.append((gap/(-dgap),s,choose,action,gap,dgap))
assert len(tiegrad)==2
# plus ensure T/Q tie derivative zero, U strict to P
assert any(s==T and d==0 for s,_,_,d in tiegrad)
assert any(s==U and d>0 for s,_,_,d in tiegrad)
clo=min(closure,key=lambda x:x[0]);lam=clo[0]
Knew=K+lam*dK;Lnew=L+lam*dL
assert Knew>0 and Lnew>0
H2={};ties2=[];gaps2=[]
for s in reversed(S):
 opt={'P':Knew*ratio(s),'Q':Lnew}
 if s[0]<14:opt['C']=1+sum((P[i]*H2[t] for i,t in enumerate(ch(s))),F())
 m=min(opt.values());ops=tuple(a for a,c in opt.items() if c==m)
 H2[s]=m
 if len(ops)>1:ties2.append((s,ops))
 gaps2.extend(c-m for c in opt.values() if c>m)
assert len(S)==680 and len(ties2)==2 and len(gaps2)==1238 and min(gaps2)>0
assert set(x[0] for x in ties2)=={T,clo[1]},ties2
cert={'schema':'EM_N14_STAGE147_AUTHOR_DUAL_CANDIDATE_V1','input':'STAGE146 author exact proof','dK':str(dK),'dL':str(dL),'dL_over_dK':str(dL/dK),'T_gradient_C':list(map(str,Ct)),'old_ties_dgap':[(list(s),c,a,str(d)) for s,c,a,d in tiegrad],'other_closures':len(closure),'first_lambda':str(lam),'first_state':list(clo[1]),'first_actions':[clo[2],clo[3]],'new_K':str(Knew),'new_L':str(Lnew),'new_Hroot':str(H2[(0,0,0)]),'new_ties':[(list(s),list(o)) for s,o in ties2],'states':680,'strict_positive_gaps':len(gaps2),'minimum_positive_gap':str(min(gaps2)),'negative_gaps':0,'primal_stage147':'UNPROVED_AUTHOR_DUAL_ONLY'}
with open('/mnt/data/EM_stage147_dual_candidate.json','w') as f:json.dump(cert,f,indent=2)
print(json.dumps(cert,indent=2))
print('PASS_STAGE147_DUAL_SCAN_EXACT')
