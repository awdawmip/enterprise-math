"""Exact local dual scan to next kink from proven Stage202 right-end policy.
Candidate only: no primal proof for Stage203.
"""
from fractions import Fraction as F
from functools import cache
from json import dumps
from pathlib import Path
P=(F(3,24),F(1,24),F(20,24)); Q=(F(2,24),F(2,24),F(20,24))
K=F(94363551,741293);N=14;R=(6,0,1);Z=(14,0,0)
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s,i):
 n,a,b=s;return n+1,a+(i==0),b+(i==1)
def lr(s):
 _,a,b=s;return F(2**(a+b),3**a)
@cache
def bell(s):
 c={'P':K*lr(s),'Q':K}
 if s[0]<N:c['C']=1+sum(P[i]*bell(child(s,i))[0] for i in range(3))
 v=min(c.values());return v,tuple(a for a in ('P','Q','C') if a in c and c[a]==v)
@cache
def selected(s):
 if s==R:return 'Q'
 if s==Z:return 'Q'
 t=bell(s)[1];assert len(t)==1,(s,t)
 return t[0]
@cache
def coeff(s):return action_coeff(s,selected(s))
def action_coeff(s,a):
 if a=='P':return F(0),lr(s),F(0)
 if a=='Q':return F(0),F(0),F(1)
 children=[coeff(child(s,i)) for i in range(3)]
 return tuple(F(int(j==0))+sum(P[i]*children[i][j] for i in range(3)) for j in range(3))
def cost(c,k):return c[0]+k*(c[1]+c[2])
def minus(a,b):return tuple(a[j]-b[j] for j in range(3))
changes=[];flat=[]
for s in states:
 old=selected(s)
 for alt in ('P','Q')+(('C',) if s[0]<N else ()):
  if alt==old:continue
  d=minus(action_coeff(s,alt),action_coeff(s,old))
  gap=cost(d,K);slope=d[1]+d[2]
  assert gap>=0,(s,alt,gap)
  if gap==0:flat.append((s,old,alt,slope))
  if gap>0 and slope>0:changes.append((gap/slope,s,old,alt))
assert {x[0] for x in flat}=={R,Z},flat
assert all(slope<=0 for _,_,_,slope in flat),flat
changes.sort()
step,at,old,new=changes[0]
newk=K-step
@cache
def nb(s):
 cs={'P':newk*lr(s),'Q':newk}
 if s[0]<N:cs['C']=1+sum(P[i]*nb(child(s,i))[0] for i in range(3))
 v=min(cs.values());return v,tuple(a for a in ('P','Q','C') if a in cs and cs[a]==v),tuple(t-v for t in cs.values() if t>v)
ties={str(s):nb(s)[1] for s in states if len(nb(s)[1])>1}
strict=[j for s in states for j in nb(s)[2]]
assert len(ties)==2,(ties,step)
assert len(strict)==1238,len(strict)
res={'schema':'EM_STAGE203_EXACT_DUAL_CANDIDATE_V1','classification':'DUAL_ONLY_PRIMAL_UNPROVED','K203':str(newk),'L203':str(newk),'H203':str(nb((0,0,0))[0]),'downward_step':str(step),'first_new_tie':at,'first_new_transition':[old,new],'ties':ties,'bellman_states':len(states),'positive_gaps':len(strict),'min_positive_gap':str(min(strict)),'source': 'REPRO_STAGE203_DUAL.py', 'stage202_right_alpha':'3712577116979992345/10517860061584293888'}
Path(__file__).resolve().with_name('certificate203_dual.json').write_text(dumps(res,indent=2)+'\n')
print(dumps(res,indent=2))
print('STAGE203_DUAL_SCAN_PASS')
