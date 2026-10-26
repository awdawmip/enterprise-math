#!/usr/bin/env python3
"""Stage170 dual-only tangent scan from fully verified author Stage169.
No primal theorem is inferred from this finite exact dual scan.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6))
R=(10,0,1);Y=(6,4,1)
K=F(100796326719840,394715670863)
L=F(298940013781960,1184147012589)
dK=F(-1);dL=F(-10592,12501)

def fmt(x):return str(x.numerator)+(('/'+str(x.denominator)) if x.denominator!=1 else '')
def ell(s):return F(2**(s[1]+s[2]),3**s[1])
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def val(s):
 o=[K*ell(s),L]
 if s[0]<N:o.append(1+sum(P[i]*val(child(s,i))[0] for i in range(3)))
 return min(o),o
@lru_cache(None)
def derivative(s):
 v,o=val(s)
 winning=[i for i,x in enumerate(o) if x==v]
 if s==R:ix=1
 elif s==Y:ix=0
 else:
  assert len(winning)==1,(s,winning)
  ix=winning[0]
 od=[dK*ell(s),dL]
 if s[0]<N:od.append(sum(P[i]*derivative(child(s,i))[0] for i in range(3)))
 return od[ix],od,ix
all_states=[];closures=[];kept=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b); v,o=val(s);dv,do,ix=derivative(s)
   for i in range(len(o)):
    gap=o[i]-v;dergap=do[i]-dv
    if gap==0 and dergap<0:raise ValueError(('BAD TIE DIRECTION',s,i,dergap))
    if gap==0:kept.append((s,i,dergap))
    elif dergap<0:all_states.append((gap/-dergap,s,i,gap,dergap))
assert all_states
all_states.sort(key=lambda x:x[0]);tt=all_states[0][0]
closures=[{'state':str(s),'action':'PQC'[i],'initial_gap':fmt(g),'direction_gap':fmt(d)} for t,s,i,g,d in all_states if t==tt]
Knew=K+dK*tt;Lnew=L+dL*tt
@lru_cache(None)
def check(s):
 o=[Knew*ell(s),Lnew]
 if s[0]<N:o.append(1+sum(P[i]*check(child(s,i))[0] for i in range(3)))
 return min(o),o
newties={};positive=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,o=check(s); win=[i for i,x in enumerate(o) if x==v]
   if len(win)>1:newties[str(s)]=['PQC'[i] for i in win]
   positive.extend(x-v for x in o if x>v)
assert len(newties)==2 and str(R) in newties and len(positive)==1238
assert min(positive)>0
report={'stage':170,'status':'DUAL_ONLY','previous_stage':169,'global_snapshot':'97fddf10a23d1b365a89029b1a7bdee752b84d24','em_snapshot':'02755d46a9afc42afcf841ba643d27daec5fa20b',
'K169':fmt(K),'L169':fmt(L),'dK':fmt(dK),'dL':fmt(dL),'first_t':fmt(tt),'K170':fmt(Knew),'L170':fmt(Lnew),'slope170':fmt(Knew+Lnew),
'new_closures':closures,'ties170':newties,'states':680,'strict_gaps':len(positive),'min_gap':fmt(min(positive)),'root':fmt(check((0,0,0))[0]),'primal':'UNPROVED'}
Path(__file__).with_name('candidate170.json').write_text(json.dumps(report,indent=2)+'\n')
for k,v in report.items():print(k,v)
