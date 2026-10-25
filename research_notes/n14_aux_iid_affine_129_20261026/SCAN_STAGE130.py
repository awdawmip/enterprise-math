"""Stage130 next dual candidate only, ray scan from Stage129; does NOT prove primal."""
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6));N=14
K0,L0=F(14874456845932398,22082607358633),F(13896162810492616,22082607358633)
B,T=(11,0,1),(2,0,2)
def kids(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 n,a,b=s
 return F(2**(a+b),3**a)
V={};coefs={};actions={};offers={};alternatives={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);cost={'P':K0*ratio(s),'Q':L0}
   c={'P':(F(0),ratio(s),F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    ch=kids(s)
    cost['C']=1+sum(P[i]*V[ch[i]] for i in range(3))
    c['C']=tuple((F(1) if j==0 else F(0))+sum(P[i]*coefs[ch[i]][j] for i in range(3)) for j in range(3))
   opts=[op for op in cost if cost[op]==min(cost.values())]
   act='Q' if s in (B,T) else opts[0]
   assert act in opts
   actions[s]=act;V[s]=cost[act];coefs[s]=c[act];offers[s]=cost;alternatives[s]=c
m=alternatives[B]['C'][1]/(1-alternatives[B]['C'][2])
assert m==F(112,129)
events=[];gapcount=0
for s,costs in offers.items():
 act=actions[s]
 def slope(op):
  c=alternatives[s][op]
  return -c[1]-m*c[2]
 for alt,val in costs.items():
  if alt==act:continue
  gap=val-costs[act];dg=slope(alt)-slope(act)
  assert gap>=0
  if gap>0:
   gapcount+=1
   if dg<0:events.append((gap/(-dg),s,act,alt))
  elif s==T:assert dg==F(22082607358633,10905381526044672)
  elif s==B:assert dg==0
  else:raise AssertionError((s,act,alt))
assert gapcount==1238
t,s,old,new=min(events)
assert s==(14,7,4) and old=='Q' and new=='P'
assert t==F(386890102331824527,17710251101623666)
K1=K0-t;L1=L0-m*t
assert (K1,L1)==(F(522693,802),F(244736,401))
R={};ties={};positive=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b)
   v={'P':K1*ratio(s),'Q':L1}
   if n<N:v['C']=1+sum(P[i]*R[k] for i,k in enumerate(kids(s)))
   h=min(v.values());R[s]=h
   o=[x for x in v if v[x]==h]
   if len(o)>1:ties[s]=o
   positive.extend(x-h for x in v.values() if x>h)
assert ties=={B:['Q','C'],(14,7,4):['P','Q']}
assert len(R)==680 and len(positive)==1238
assert min(positive)==F(517,28872)
assert R[(0,0,0)]==F(52838467869186182216021,117157274574869495808)
print('PASS STAGE130 DUAL CANDIDATE ONLY', K1,L1,t,ties)
