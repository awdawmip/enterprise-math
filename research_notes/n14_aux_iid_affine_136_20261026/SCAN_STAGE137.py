#!/usr/bin/env python3
"""Exact one-sided dual-ray scan from Stage136; Stage137 remains candidate only."""
from fractions import Fraction as F
N=14
P=(F(1,8),F(1,24),F(5,6))
K=F(840571992,1526537);L=F(797676584,1526537)
dK=F(-1);dL=F(-112,129)
B=(11,0,1);D=(10,6,2)
def states(n):
 return ((n,a,b) for a in range(n+1) for b in range(n-a+1))
def ch(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={};DH={};costs={};slope={};selected={};closures=[]
for n in range(N,-1,-1):
 for s in states(n):
  n,a,b=s;r=F(2**(a+b),3**a)
  vals={'P':K*r,'Q':L}; der={'P':dK*r,'Q':dL}
  if n<N:
   vals['C']=F(1)+sum((P[i]*H[c] for i,c in enumerate(ch(s))),F(0))
   der['C']=sum((P[i]*DH[c] for i,c in enumerate(ch(s))),F(0))
  m=min(vals.values());active=[a for a,v in vals.items() if v==m]
  dm=min(der[a] for a in active)
  chosen=[a for a in active if der[a]==dm]
  H[s]=m;DH[s]=dm;costs[s]=vals;slope[s]=der;selected[s]=chosen
  for a,v in vals.items():
   gap=v-m;dgap=der[a]-dm
   if gap>0 and dgap<0:
    closures.append((gap/(-dgap),s,a,chosen,gap,dgap))
   elif gap==0 and dgap<0:raise ValueError((s,a,'invalid_direction'))
closures.sort(key=lambda x:x[0]);t=closures[0][0]
print('origin root',H[(0,0,0)],'slope',DH[(0,0,0)])
print('current ties rightward:',[(s,costs[s],slope[s],selected[s]) for s in (B,D)])
print('first closures:')
for row in closures[:10]:print(row)
print('number closures',len(closures),'first candidate K,L',K+dK*t,L+dL*t)
Kn=K+dK*t;Ln=L+dL*t
Hn={};ties=[];strict=[]
for n in range(N,-1,-1):
 for s in states(n):
  nn,a,b=s;r=F(2**(a+b),3**a)
  v={'P':Kn*r,'Q':Ln}
  if n<N:v['C']=1+sum((P[i]*Hn[c] for i,c in enumerate(ch(s))),F(0))
  m=min(v.values());Hn[s]=m
  ts=[k for k,z in v.items() if z==m]
  if len(ts)>1:ties.append((s,ts))
  for k,z in v.items():
   if z>m:strict.append(z-m)
print('vertex ties',ties,'min strict',min(strict),'num',len(strict),'root',Hn[(0,0,0)])
assert Hn[(0,0,0)]==H[(0,0,0)]+t*DH[(0,0,0)]
assert t==F(9892799730,612141337)
assert Kn==F(214326,401) and Ln==F(203912,401)
assert set((s,tuple(a)) for s,a in ties)=={((13,6,4),('Q','C')),(B,('Q','C'))}
assert len(strict)==1238
print('PASS_STAGE137_DUAL_CANDIDATE_ONLY')
