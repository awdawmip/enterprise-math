"""Exact Stage205 dual kink candidate from Stage204 right endpoint. Not a primal proof."""
from fractions import Fraction as F
from functools import cache
from pathlib import Path
from json import dumps
P=(F(3,24),F(1,24),F(20,24));N=14;K=F(6550632,53665)
U=(9,2,2);Z=(14,0,0);states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def bell(s):
 c={'P':K*lr(s),'Q':K}
 if s[0]<N:c['C']=1+sum(P[i]*bell(child(s,i))[0] for i in range(3))
 v=min(c.values());return v,tuple(a for a in c if c[a]==v)
@cache
def selected(s):
 if s in (U,Z):return 'Q'
 v=bell(s)[1];assert len(v)==1,(s,v)
 return v[0]
@cache
def coef(s):return byaction(s,selected(s))
def byaction(s,a):
 if a=='P':return F(0),lr(s),F(0)
 if a=='Q':return F(0),F(0),F(1)
 ch=[coef(child(s,i)) for i in range(3)]
 return tuple(F(j==0)+sum(P[i]*ch[i][j] for i in range(3)) for j in range(3))
def cost(c,k):return c[0]+k*(c[1]+c[2])
cands=[];flat=[]
for s in states:
 old=selected(s)
 for alt in ('P','Q')+(('C',) if s[0]<N else ()):
  if alt==old:continue
  ca=coef(s);cb=byaction(s,alt)
  d=tuple(cb[i]-ca[i] for i in range(3))
  gap=cost(d,K);slope=d[1]+d[2]
  assert gap>=0,(s,alt,gap)
  if gap==0:flat.append((s,old,alt,slope))
  if gap>0 and slope>0:cands.append((gap/slope,s,old,alt))
assert {x[0] for x in flat}=={U,Z}
assert all(x[3]<=0 for x in flat)
step,at,old,new=min(cands);newk=K-step
@cache
def nxt(s):
 c={'P':newk*lr(s),'Q':newk}
 if s[0]<N:c['C']=1+sum(P[i]*nxt(child(s,i))[0] for i in range(3))
 v=min(c.values());return v,tuple(a for a in c if c[a]==v),tuple(x-v for x in c.values() if x>v)
tie={str(s):nxt(s)[1] for s in states if len(nxt(s)[1])>1}
pos=[x for s in states for x in nxt(s)[2]]
assert newk==F(16200,137)
assert nxt((0,0,0))[0]==F(175689269891985199711,1876232849527406592)
assert len(pos)==1238 and min(pos)==F(69107093,19635830784)
assert set(tie)=={'(12, 3, 1)','(14, 0, 0)'}
data={'schema':'EM_STAGE205_DUAL_SCAN_V1','status':'DUAL_CANDIDATE_ONLY','K':str(newk),'L':str(newk),'H':str(nxt((0,0,0))[0]),'downstep':str(step),'first_state':list(at),'first_transition':[old,new],'ties':tie,'bellman_states':len(states),'positive_gaps':len(pos),'minimum_positive_gap':str(min(pos)),'source':'scan_stage205.py','parent':'Stage204 right endpoint'}
Path(__file__).with_name('certificate205_dual.json').write_text(dumps(data,indent=2)+'\n')
print('STAGE205_DUAL_SCAN_PASS',newk,step,at,old,new)
