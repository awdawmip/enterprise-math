#!/usr/bin/env python3
"""Stage116 independent ordered-word integer DFS (no primary checker imports)."""
from fractions import Fraction as F
from functools import lru_cache
N=14; K=F(37550061,41440); L=F(3296576,3885)
PN=(3,1,20); QN=(1,1,10)
D=(9,1,2);T=(14,7,4)
def kids(n,a,b):return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
@lru_cache(None)
def B(n,a,b):
 v={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:
  ss=kids(n,a,b)
  v['C']=1+sum(F(PN[i],24)*B(*ss[i])[0] for i in range(3))
 best=min(v.values())
 return best,tuple(t for t,x in v.items() if x==best)
DP=24**N;DQ=12**N;powp=[24**i for i in range(N+1)];powq=[12**i for i in range(N+1)]
def run(w,u):
 tot=[0,0,0,0];hits={D:[0,0,0],T:[0,0,0]}
 stack=[(0,0,0,1,1)]
 prefixes=0
 while stack:
  n,a,b,p,q=stack.pop();prefixes+=1;s=(n,a,b)
  if w==0 and s in hits:
   hits[s][0]+=1
   hits[s][1]+=p*powp[N-n]
   hits[s][2]+=q*powq[N-n]
  actions=B(n,a,b)[1]
  if s==D:
   assert actions==('Q','C');act='Q' if w else 'C'
  elif s==T:
   assert actions==('P','Q');act='P' if u else 'Q'
  else:
   assert len(actions)==1,(s,actions)
   act=actions[0]
  if act=='C':
   for c,pn,qn in zip(kids(n,a,b),PN,QN):
    stack.append((*c,p*pn,q*qn))
  else:
   pp=p*powp[N-n];qq=q*powq[N-n]
   if act=='Q':tot[0]+=pp
   else:tot[1]+=qq
   tot[2]+=n*pp;tot[3]+=n*qq
 return (F(tot[0],DP),F(tot[1],DQ),F(tot[2],DP),F(tot[3],DQ)),prefixes,{s:(x,F(y,DP),F(z,DQ)) for s,(x,y,z) in hits.items()}
corners={}
for w,u in ((0,0),(1,0),(0,1),(1,1)):
 value,visited,hits=run(w,u)
 print('corner',w,u,'ordered_prefixes',visited)
 corners[(w,u)]=value
 if (w,u)==(0,0):
  assert hits[D]==(172,F(671875,53747712),F(671875,20155392))
  assert hits[T]==(9830,F(614375,75144747810816),F(614375,80244904034304))
b=corners[(0,0)]
dw=tuple(corners[(1,0)][i]-b[i] for i in range(4))
du=tuple(corners[(0,1)][i]-b[i] for i in range(4))
assert corners[(1,1)]==tuple(b[i]+dw[i]+du[i] for i in range(4))
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),
           F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert du==(F(-614375,75144747810816),F(614375,80244904034304),F(0),F(0))
w0=F(374236473161181,1042086080000000);gamma=F(118943,1488694400)
def mix(u):return tuple(b[i]+(w0+gamma*u)*dw[i]+u*du[i] for i in range(4))
v0=mix(0);v1=mix(1)
assert v0[:3]==(F(900390060440962701793,2592933255351443128320),
                F(900390060440962701793,2592933255351443128320),
                F(132635694365041929281069,10371733021405772513280))
assert v1[:3]==(F(900390062503198401793,2592933255351443128320),
                F(900390062503198401793,2592933255351443128320),
                F(132635679890866772493569,10371733021405772513280))
assert v0[2]>v0[3] and v1[2]>v1[3]
print('PASS_STAGE116_INDEPENDENT_INTEGER_ORDERED_DFS')
