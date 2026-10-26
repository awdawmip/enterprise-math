#!/usr/bin/env python3
"""Exact Stage177 external IID primal: independent Fraction suffix DP and unmerged ordered DFS."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(1870855299,8461318);L=F(911522328,4230659)
H_EXPECTED=F(148336146012983121522325,905303534551638736896)
T=(8,2,0);U=(12,5,2)
A=('P','Q','C');EXPECTED={T:('P','C'),U:('P','C')}
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def bell(s):
    options=[K*ell(s),L]
    if s[0]<N:options.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(options);return m,tuple(a for a,v in zip(A,options) if v==m),options
strict={};ties={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,w,opts=bell(s)
   if len(w)>1:ties[s]=w
   else:strict[s]=w[0]
   gaps.extend(v2-v for v2 in opts if v2>v)
assert len(strict)+len(ties)==680,(len(strict),len(ties))
assert ties==EXPECTED,(ties,EXPECTED)
assert len(gaps)==1238
H=bell((0,0,0))[0];assert H==H_EXPECTED,(H,H_EXPECTED)
def is_ancestor(s1,s2):
 return (s1[0]<s2[0] and s1[1]<=s2[1] and s1[2]<=s2[2] and
  (s2[1]-s1[1])+(s2[2]-s1[2]) <=s2[0]-s1[0])
assert not is_ancestor(T,U) and not is_ancestor(U,T)
def action(s,t,u):
 if s==T:return 'P' if t else 'C'
 if s==U:return 'P' if u else 'C'
 return strict[s]
def suffix(t,u):
 @lru_cache(None)
 def rec(s):
  ac=action(s,t,u)
  if ac=='P':return (F(0),F(1),F(0),F(0))
  if ac=='Q':return (F(1),F(0),F(0),F(0))
  o=[rec(child(s,i)) for i in range(3)]
  return (sum((P[i]*o[i][0] for i in range(3)),F(0)),
    sum((Q[i]*o[i][1] for i in range(3)),F(0)),
    1+sum((P[i]*o[i][2] for i in range(3)),F(0)),
    1+sum((Q[i]*o[i][3] for i in range(3)),F(0)))
 return rec((0,0,0))
def ordered_dfs(t,u):
 pn=(3,1,20);qn=(1,1,10)
 acc=defaultdict(int);hits={T:[0,F(0),F(0)],U:[0,F(0),F(0)]};nodes=0
 def walk(n,a,b,p,q):
  nonlocal nodes
  nodes+=1;s=(n,a,b)
  if s in hits:
   h=hits[s];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
  ac=action(s,t,u)
  if ac=='C':
   assert n<N
   for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
  else:
   acc[n,'ap']+=p;acc[n,'aq']+=q;acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
   if ac=='P':acc[n,'eq']+=q
   else:acc[n,'ep']+=p
 walk(0,0,0,1,1)
 mass=lambda tag,den:sum((F(acc[n,tag],den**n) for n in range(N+1)),F(0))
 assert mass('ap',24)==mass('aq',12)==1
 return (mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes
corners={};nodes={};hits0=None
for t in (0,1):
 for u in (0,1):
  v=suffix(t,u);w,h,n=ordered_dfs(t,u)
  print('corner',t,u,'nodes',n,'agrees',v==w,flush=True)
  assert v==w,(t,u,v,w)
  corners[t,u]=v;nodes[f'{t}{u}']=n
  if hits0 is None:hits0=h
  else:assert hits0==h,(hits0,h)
assert hits0[T][0]>0 and hits0[U][0]>0
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];dT=sub(corners[1,0],base);dU=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dU)
print('mixed',list(map(fmt,mixed)))
assert mixed==(F(0),)*4
D=lambda v:v[0]-v[1]
D0,Dt,Du=map(D,(base,dT,dU))
assert Dt!=0
t0=-D0/Dt
ts=-Du/Dt
vec=lambda u:tuple(base[i]+(t0+ts*u)*dT[i]+u*dU[i] for i in range(4))
legal=(F(0),F(1))
if ts>0:legal=(max(legal[0],-t0/ts),min(legal[1],(1-t0)/ts))
elif ts<0:legal=(max(legal[0],(1-t0)/ts),min(legal[1],-t0/ts))
lo,hi=legal
print('balance t(u):',fmt(t0),fmt(ts),'legal u:',fmt(lo),fmt(hi),'t_ends:',fmt(t0+ts*lo),fmt(t0+ts*hi))
assert lo<=hi
alpha176=F(5148159682306058186075,14750257906470044565504)
V176=F(338735964098497111620725,29500515812940089131008)
t176=F(1768756796217217,3860125696000000)+F(4588038935639,193006284800000)
print('at u=1',list(map(fmt,vec(F(1)))),'t176',fmt(t176),'matches:',fmt(t0+ts)==fmt(t176))
p0,p1=vec(lo),vec(hi)
left,right=(p0,p1) if p0[0]<p1[0] else (p1,p0)
checks={
 'left_prev':left[0]==left[1]==alpha176 and left[2]==V176,
 'stage176_at_u1':vec(F(1))[0]==alpha176 and vec(F(1))[2]==V176 and t0+ts==t176,
 'balanced':left[0]==left[1] and right[0]==right[1],
 'timeP_dominates':left[2]>=left[3] and right[2]>=right[3],
 'dual_tightness':all(v[2]+K*v[1]+L*v[0]==H for v in (left,right)),
 'increasing_alpha':right[0]>left[0],
 'decreasing_time':right[2]<left[2],
 'slope':right[2]-left[2]==-(K+L)*(right[0]-left[0]),
 'two_tie_cones_disjoint':mixed==(F(0),)*4,
 'strict_all_other_gaps':min(gaps)>0,
}
for k,v in checks.items():print('check',k,v)
print('BOUNDARY left',list(map(fmt,left)))
print('BOUNDARY right',list(map(fmt,right)))
print('WIDTH',fmt(right[0]-left[0]),'SLOPE',fmt(K+L),'H',fmt(H),'MIN_GAP',fmt(min(gaps)))
print('HITS',{str(k):list(map(fmt,v)) for k,v in hits0.items()},'NODES',nodes)
print('BASE',list(map(fmt,base)),'dT',list(map(fmt,dT)),'dU',list(map(fmt,dU)))
cert={
 'schema':'EM_N14_STAGE177_AUTHOR_EXACT_V1','status':'AUTHOR_EXACT_NOT_NATIVE_ADMITTED',
 'model':{'N':N,'P':list(map(fmt,P)),'Q':list(map(fmt,Q)),'scope':'EXTERNAL_TERNARY_IID_FULL_ORDERED_HISTORIES'},
 'sources':{'stage176_author_commit':'1198e05fe284be7143682dd68dba389d50c4925e','global_snapshot':'c255c049665e04da1b3f7b5f3b6f36e8594a22e7','em_scientific_snapshot':'2145832abbeece95c8e7a847204c1884b8689878'},
 'dual':{'K':fmt(K),'L':fmt(L),'sum':fmt(K+L),'H':fmt(H),'states':680,'ties':{str(k):list(v) for k,v in ties.items()},'positive_gaps':len(gaps),'min_gap':fmt(min(gaps))},
 'corners':{f'{t}{u}':list(map(fmt,m)) for (t,u),m in corners.items()},
 'base':list(map(fmt,base)),'dT':list(map(fmt,dT)),'dU':list(map(fmt,dU)),'mixed':list(map(fmt,mixed)),
 'first_hit':{str(s):{'ordered_paths':h[0],'P':fmt(h[1]),'Q':fmt(h[2])}for s,h in hits0.items()},
 'ordered_dfs_nodes':nodes,
 'balance':{'D0':fmt(D0),'Dt':fmt(Dt),'Du':fmt(Du),'t0':fmt(t0),'ts':fmt(ts),'u0':fmt(lo),'u1':fmt(hi),'t_at_u0':fmt(t0+ts*lo),'t_at_u1':fmt(t0+ts*hi)},
 'left':{'alpha':fmt(left[0]),'V':fmt(left[2]),'tP_minus_tQ':fmt(left[2]-left[3])},
 'right':{'alpha':fmt(right[0]),'V':fmt(right[2]),'tP_minus_tQ':fmt(right[2]-right[3])},
 'width':fmt(right[0]-left[0]),'slope':fmt(K+L),'checks':checks}
Path(__file__).with_name('certificate177.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
assert all(checks.values()),'Stage177 proof failed; retain candidate/obstruction, do not claim theorem'
print('STAGE177_AUTHOR_EXACT_FULL_REAL_PASS')
