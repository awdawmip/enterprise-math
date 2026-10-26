#!/usr/bin/env python3
"""Stage183 exact finite-state Bellman primal analysis, independent full ordered history DFS. The second coin variable u denotes Stage183 X=(11,5,2), deciding P/C."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(2983556187,15076502);L=F(1477646456,7538251)
H_EXPECTED=F(61508771764230260243523613,412949318370301380132864)
S=(9,0,1);U=(11,5,2)
EXPECTED={S:('Q','C'),U:('P','C')};A=('P','Q','C')
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(st):return F(2)**(st[1]+st[2])/F(3)**st[1]
def child(st,i):return(st[0]+1,st[1]+int(i==0),st[2]+int(i==1))
@lru_cache(None)
def bell(st):
 vals=[K*ell(st),L]
 if st[0]<N:vals.append(1+sum((P[i]*bell(child(st,i))[0] for i in range(3)),F(0)))
 m=min(vals);return m,tuple(a for a,w in zip(A,vals) if w==m),vals
strict={};ties={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   st=(n,a,b);v,acts,vals=bell(st)
   if len(acts)>1:ties[st]=acts
   else:strict[st]=acts[0]
   gaps.extend(w-v for w in vals if w>v)
assert len(strict)+len(ties)==680,(len(strict),len(ties))
assert ties==EXPECTED,(ties,EXPECTED)
assert len(gaps)==1238,len(gaps)
H=bell((0,0,0))[0]
assert H==H_EXPECTED,(H,H_EXPECTED)
def is_ancestor(s1,s2):
 return s1[0]<s2[0] and s1[1]<=s2[1] and s1[2]<=s2[2] and (s2[1]-s1[1])+(s2[2]-s1[2])<=s2[0]-s1[0]
assert not is_ancestor(S,U) and not is_ancestor(U,S)
def action(st,s,u):
 if st==S:return 'Q' if s else 'C'
 if st==U:return 'P' if u else 'C'
 return strict[st]
def suffix(s,u):
 @lru_cache(None)
 def rec(st):
  act=action(st,s,u)
  if act=='P':return F(0),F(1),F(0),F(0)
  if act=='Q':return F(1),F(0),F(0),F(0)
  z=[rec(child(st,i)) for i in range(3)]
  return (sum((P[i]*z[i][0] for i in range(3)),F(0)),sum((Q[i]*z[i][1] for i in range(3)),F(0)),1+sum((P[i]*z[i][2] for i in range(3)),F(0)),1+sum((Q[i]*z[i][3] for i in range(3)),F(0)))
 return rec((0,0,0))
def ordered_dfs(s,u):
 pn=(3,1,20);qn=(1,1,10)
 counts=defaultdict(int);hits={S:[0,F(0),F(0)],U:[0,F(0),F(0)]};nodes=0
 def walk(n,a,b,p,q):
  nonlocal nodes
  nodes+=1;st=(n,a,b)
  if st in hits:
   h=hits[st];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
  act=action(st,s,u)
  if act=='C':
   assert n<N
   for i in range(3):walk(n+1,a+int(i==0),b+int(i==1),p*pn[i],q*qn[i])
  else:
   for tag,val in (('ap',p),('aq',q),('tp',n*p),('tq',n*q)):counts[n,tag]+=val
   if act=='P':counts[n,'eq']+=q
   else:counts[n,'ep']+=p
 walk(0,0,0,1,1)
 mass=lambda tag,den:sum((F(counts[n,tag],den**n) for n in range(N+1)),F(0))
 assert mass('ap',24)==mass('aq',12)==1
 return(mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes
corners={};nodes={};hits=None
for s in (0,1):
 for u in (0,1):
  v=suffix(s,u);w,h,n=ordered_dfs(s,u)
  print('corner',s,u,'nodes',n,'agrees',v==w,flush=True)
  assert v==w,(s,u,v,w)
  corners[s,u]=v;nodes[f'{s}{u}']=n
  if hits is None:hits=h
  else:assert h==hits,(h,hits)
assert hits[S][0]>0 and hits[U][0]>0
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];dS=sub(corners[1,0],base);dU=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dU)
assert mixed==(F(0),)*4,mixed
D=lambda v:v[0]-v[1]
D0,Ds,Du=map(D,(base,dS,dU))
assert Ds!=0
s0=-D0/Ds;su=-Du/Ds
legal=(F(0),F(1))
if su>0:legal=(max(legal[0],-s0/su),min(legal[1],(1-s0)/su))
elif su<0:legal=(max(legal[0],(1-s0)/su),min(legal[1],-s0/su))
lo,hi=legal
print('BALANCE s(u)=',fmt(s0),fmt(su),'LEGAL u=',fmt(lo),fmt(hi),flush=True)
assert lo<=hi
vec=lambda u:tuple(base[i]+(s0+su*u)*dS[i]+u*dU[i] for i in range(4))
prior_alpha=F(6293781278910356391787,17990936586642819907584)
prior_V=F(50134637360540821877021,4497734146660704976896)
prior_smax=F(6103153750279349,37833811200000000)+F(411561059,985255500)
v0,v1=vec(lo),vec(hi)
left,right=(v0,v1) if v0[0]<v1[0] else(v1,v0)
checks={
 'prior_endpoint_u0':vec(F(0))[0]==vec(F(0))[1]==prior_alpha and vec(F(0))[2]==prior_V,
 'prior_s_coin_u0':s0==prior_smax,
 'bal_errors':all(x[0]==x[1] for x in (left,right)),
 'timeP_dominates':all(x[2]>=x[3] for x in (left,right)),
 'tight_dual':all(x[2]+K*x[1]+L*x[0]==H for x in (left,right)),
 'alpha_inc':right[0]>left[0],
 'time_dec':right[2]<left[2],
 'slope':right[2]-left[2]==-(K+L)*(right[0]-left[0]),
 'disjoint_tie_cones':mixed==(F(0),)*4,
 'all_others_strict':min(gaps)>0,
 'legal_both':0<=lo<=hi<=1 and 0<=s0+su*lo<=1 and 0<=s0+su*hi<=1
}
print('CHECKS',checks,flush=True)
print('BOUNDARY_LEFT',list(map(fmt,left)),'BOUNDARY_RIGHT',list(map(fmt,right)),flush=True)
print('WIDTH',fmt(right[0]-left[0]),'SLOPE',fmt(K+L),'H',fmt(H),'MIN_GAP',fmt(min(gaps)),flush=True)
print('HITS',{str(k):list(map(fmt,v)) for k,v in hits.items()},'NODES',nodes,flush=True)
print('BASE',list(map(fmt,base)),'dS',list(map(fmt,dS)),'dU',list(map(fmt,dU)),flush=True)
print('TIME_MARGINS',fmt(left[2]-left[3]),fmt(right[2]-right[3]),flush=True)
cert={'schema':'EM_N14_STAGE183_REFERENCE_EXACT_V1','status':'AUTHOR_EXACT_FULL_REAL_VERIFIED','model':{'N':N,'P':list(map(fmt,P)),'Q':list(map(fmt,Q)),'scope':'EXTERNAL_TERNARY_IID_FULL_ORDERED_HISTORIES'},'sources':{'global_snapshot':'8ec98188025f60aafe48055520ba3a57c29cdb2c','em_initial_snapshot':'fd157124db7dde6d7a07566e4004fb5286240e03','stage182_commit':'1dcd2cabc6e6e8ddf70628c68c7cf2dbede4e23a'},'dual':{'K':fmt(K),'L':fmt(L),'sum':fmt(K+L),'H':fmt(H),'states':680,'ties':{str(k):list(v) for k,v in ties.items()},'positive_gaps':len(gaps),'min_gap':fmt(min(gaps))},'corners':{f'{s}{u}':list(map(fmt,m)) for(s,u),m in corners.items()},'base':list(map(fmt,base)),'dS':list(map(fmt,dS)),'dU':list(map(fmt,dU)),'mixed':list(map(fmt,mixed)),'first_hit':{str(st):{'ordered_paths':h[0],'P':fmt(h[1]),'Q':fmt(h[2])} for st,h in hits.items()},'ordered_dfs_nodes':nodes,'balance':{'D0':fmt(D0),'Ds':fmt(Ds),'Du':fmt(Du),'s0':fmt(s0),'su':fmt(su),'u_min':fmt(lo),'u_max':fmt(hi),'s_min':fmt(s0+su*lo),'s_max':fmt(s0+su*hi)},'left':{'alpha':fmt(left[0]),'V':fmt(left[2]),'tP_minus_tQ':fmt(left[2]-left[3])},'right':{'alpha':fmt(right[0]),'V':fmt(right[2]),'tP_minus_tQ':fmt(right[2]-right[3])},'width':fmt(right[0]-left[0]),'slope':fmt(K+L),'checks':checks}
Path(__file__).with_name('certificate183_reference.json').write_text(json.dumps(cert,indent=2)+'\n')
if not all(checks.values()):
 print('STAGE183_PRIMAL_CANDIDATE_OBSTRUCTED',flush=True)
 raise SystemExit(3)
print('STAGE183_AUTHOR_EXACT_FULL_REAL_PASS',flush=True)
