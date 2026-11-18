"""Stage201 exact dual scan after Stage200 R=(7,5,2), Z=(14,0,0)."""
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path
P=(F(3,24),F(1,24),F(20,24)); N=14
K=F(1358449620408,10345594439)
R=(7,5,2); Z=(14,0,0); START=(0,0,0)
S=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def next_(s,i):return (s[0]+1,s[1]+(i==0),s[2]+(i==1))
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
 d={'P':K*ratio(s),'Q':K}
 if s[0]<N:d['C']=1+sum(P[i]*bell(next_(s,i))[0] for i in range(3))
 m=min(d.values());return m,tuple(k for k,v in d.items() if v==m)
assert {s:bell(s)[1] for s in S if len(bell(s)[1])>1}=={R:('P','C'),Z:('P','Q')}
@lru_cache(None)
def selected(s):
 if s==R:return 'P'
 if s==Z:return 'Q'
 (a,)=bell(s)[1];return a
@lru_cache(None)
def coeff(s):return actcoeff(s,selected(s))
def actcoeff(s,a):
 if a=='P':return F(0),ratio(s),F(0)
 if a=='Q':return F(0),F(0),F(1)
 cs=[coeff(next_(s,i)) for i in range(3)]
 return tuple(F(j==0)+sum(P[i]*cs[i][j] for i in range(3)) for j in range(3))
def delta(a,b):return tuple(a[i]-b[i] for i in range(3))
def cost(x,k):return x[0]+k*(x[1]+x[2])
flats=[];changes=[];negative=[]
for s in S:
 for alt in ('P','Q')+(('C',) if s[0]<N else ()):
  if alt==selected(s):continue
  d=delta(actcoeff(s,alt),coeff(s));gap=cost(d,K);slope=d[1]+d[2]
  if gap<0:negative.append((s,alt,gap))
  if gap==0:flats.append((s,selected(s),alt,slope))
  elif slope>0:changes.append((gap/slope,s,selected(s),alt))
assert not negative and {v[0] for v in flats}=={R,Z}
step,s,old,new=min(changes)
K201=K-step
@lru_cache(None)
def nxtbell(s):
 d={'P':K201*ratio(s),'Q':K201}
 if s[0]<N:d['C']=1+sum(P[i]*nxtbell(next_(s,i))[0] for i in range(3))
 m=min(d.values());return m,tuple(k for k,v in d.items() if v==m),tuple(v-m for v in d.values() if v>m)
ties={str(s):nxtbell(s)[1] for s in S if len(nxtbell(s)[1])>1}
strict=[g for s in S for g in nxtbell(s)[2]]
result={'classification':'STAGE201_DUAL_ONLY_AUTHOR','K200':str(K),'K201':str(K201),'L201':str(K201),'H201':str(nxtbell(START)[0]),'step':str(step),'new_tie_state':list(s),'action_transition':[old,new], 'ties':{k:list(v) for k,v in ties.items()}, 'state_count':len(S),'strict_positive_gaps':len(strict),'min_positive_gap':str(min(strict)), 'r_coin_selected_at_right':'P','Z_selected':'Q'}
assert len(S)==680 and len(strict)==1238 and len(ties)==2, result
Path('/mnt/data/em_stage200_work/certificate201_dual.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
print('STAGE201_DUAL_SCAN_PASS')
