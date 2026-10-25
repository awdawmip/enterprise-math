#!/usr/bin/env python3
"""Stage117 independent literal ordered-history integer mass certificate."""
from fractions import Fraction as F
from collections import defaultdict

N=14
K=F(7703713039590,8727240137); L=F(7249159245096,8727240137)
D=(9,1,2); X=(7,5,1)
Pcounts=(3,1,20); Qcounts=(1,1,10)
P=(F(3,24),F(1,24),F(20,24))
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
H={}; policy={}; ties={}
for state in reversed(states):
 n,a,b=state
 r=F(2**(a+b),3**a)
 cand={'P':K*r,'Q':L}
 if n<N:
  cand['C']=1+P[0]*H[n+1,a+1,b]+P[1]*H[n+1,a,b+1]+P[2]*H[n+1,a,b]
 best=min(cand.values()); H[state]=best
 winners=[key for key,v in cand.items() if v==best]
 policy[state]=winners[0]
 if len(winners)>1:ties[state]=winners
assert len(states)==680
assert ties=={X:['P','C'],D:['Q','C']}
def dfs(w,y):
 """Accumulate integer path numerators, then reconstruct rational observers."""
 assert w in (0,1) and y in (0,1)
 hist=[defaultdict(int) for _ in range(N+1)]
 seen={D:[0,0,0],X:[0,0,0]}
 prefixes=0
 stack=[((0,0,0),1,1)]
 while stack:
  (n,a,b),pm,qm=stack.pop(); prefixes+=1
  state=(n,a,b)
  if state in seen:
   row=seen[state];row[0]+=1;row[1]+=pm;row[2]+=qm
  act=policy[state]
  if state==D:act='Q' if w else 'C'
  if state==X:act='P' if y else 'C'
  if act!='C':
   hist[n][act,pm,qm]+=1
   continue
  assert n<N
  stack.append(((n+1,a,b),pm*20,qm*10))
  stack.append(((n+1,a,b+1),pm,qm))
  stack.append(((n+1,a+1,b),pm*3,qm))
 eP=eQ=tP=tQ=F(0)
 for n,bucket in enumerate(hist):
  for (decision,pm,qm),count in bucket.items():
   massP=F(count*pm,24**n);massQ=F(count*qm,12**n)
   if decision=='Q':eP+=massP
   else:eQ+=massQ
   tP+=n*massP;tQ+=n*massQ
 first={s:(row[0],F(row[1],24**s[0]),F(row[2],12**s[0])) for s,row in seen.items()}
 return (eP,eQ,tP,tQ),prefixes,first
values={}
for w in (0,1):
 for y in (0,1):
  value,visits,first=dfs(w,y);values[w,y]=value
  print('CORNER',w,y,'VISITS',visits,'FIRST',first)
  assert first[D]==(172,F(671875,53747712),F(671875,20155392))
  assert first[X]==(28,F(35,1179648),F(35,4478976))
assert [dfs(w,y)[1] for w,y in ((0,0),(0,1),(1,0),(1,1))]==[862459,852463,854719,844723]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
B=values[0,0];W=sub(values[1,0],B);Y=sub(values[0,1],B)
assert values[1,1]==tuple(B[i]+W[i]+Y[i] for i in range(4))
assert W==(F(593265625,5283615080448),F(-430671875,5015306502144),F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert Y==(F(-816010405,5410421842378752),F(3257975,17832200896512),F(-8114835365,225434243432448),F(-151243295,13374150672384))
w0=F(374319733261181,1042086080000000)
gamma=F(12528414549,7443472000000)
alpha0=F(900390062503198401793,2592933255351443128320)
V0=F(132635679890866772493569,10371733021405772513280)
eta=F(8727240137,228653726221467648)
assert -(Y[0]-Y[1])/(W[0]-W[1])==gamma
assert Y[0]+gamma*W[0]==eta
assert Y[2]+gamma*W[2]==-(K+L)*eta
assert 0<w0<w0+gamma<1
beg=tuple(B[i]+w0*W[i] for i in range(4))
end=tuple(B[i]+(w0+gamma)*W[i]+Y[i] for i in range(4))
assert beg[0]==beg[1]==alpha0 and beg[2]==V0
assert end[0]==end[1]==alpha0+eta
assert end[2]==V0-(K+L)*eta
assert beg[2]>beg[3] and end[2]>end[3]
print('PASS_STAGE117_INDEPENDENT_ORDERED_INTEGER_DFS')
