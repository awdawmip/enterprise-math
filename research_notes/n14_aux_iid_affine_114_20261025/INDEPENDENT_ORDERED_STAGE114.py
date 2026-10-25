#!/usr/bin/env python3
"""Independent exact integer-carrier, literal ordered-prefix validation for N14 Stage114.
No imports from primary. P path numerators over 24^14; Q over 12^14.
"""
from fractions import Fraction as F
from functools import lru_cache
A=(10,3,0); D=(9,1,2); N=14
K=F(1903247523,2052316); L=F(443700120,513079)
qbr=(1,1,10); pbr=(3,1,20)
PN=24**N;QN=12**N

def move(state,symbol):
 n,a,b=state
 return n+1,a+(symbol==0),b+(symbol==1)

@lru_cache(None)
def B(state):
 n,a,b=state
 values=[K*F(2**(a+b),3**a),L]
 if n<N:values.append(F(1)+sum(F(weight,24)*B(move(state,i)) for i,weight in enumerate(pbr)))
 return min(values)

act={}
for n in range(15):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);opts=[('P',K*F(2**(a+b),3**a)),('Q',L)]
   if n<N:opts.append(('C',F(1)+sum(F(weight,24)*B(move(s,i)) for i,weight in enumerate(pbr))))
   choices=[label for label,v in opts if v==B(s)]
   if s==A:
    assert choices==['P','C']
   elif s==D:
    assert choices==['Q','C']
   else:
    assert len(choices)==1
   act[s]=choices[0]

def run(u_stop_A,w_stop_D):
 # first hit values of D invariant to parameters because A deeper and disjoint
 E_P=E_Q=T_P=T_Q=0
 touched_D=0; Dp=0;Dq=0
 leaves=0; nodes=0
 def dfs(n,a,b,pnum,qnum):
  nonlocal E_P,E_Q,T_P,T_Q,touched_D,Dp,Dq,leaves,nodes
  nodes+=1
  state=(n,a,b)
  if state==D:
   touched_D+=1
   Dp+=pnum*24**(N-n)
   Dq+=qnum*12**(N-n)
  action=('P' if u_stop_A else 'C') if state==A else ('Q' if w_stop_D else 'C') if state==D else act[state]
  if action != 'C':
   leaves+=1
   # scale rational prefix weights into fixed denominators
   px=pnum*24**(N-n)
   qx=qnum*12**(N-n)
   if action=='P':E_Q+=qx
   else:E_P+=px
   T_P+=n*px
   T_Q+=n*qx
   return
  assert n<N
  dfs(n+1,a+1,b,pnum*3,qnum*1)
  dfs(n+1,a,b+1,pnum*1,qnum*1)
  dfs(n+1,a,b,pnum*20,qnum*10)
 dfs(0,0,0,1,1)
 out=(F(E_P,PN),F(E_Q,QN),F(T_P,PN),F(T_Q,QN))
 return out,(touched_D,F(Dp,PN),F(Dq,QN),leaves,nodes)

corners={}
for u,w in [(0,0),(1,0),(0,1),(1,1)]:
 (mom,counts)=run(u,w)
 corners[(u,w)]=mom
 print(f'corner={u},{w} first_hit_D={counts[:3]} leaves={counts[3]} nodes={counts[4]} moment={mom}')

base=corners[(0,0)]
du=tuple(corners[(1,0)][i]-base[i] for i in range(4))
dw=tuple(corners[(0,1)][i]-base[i] for i in range(4))
mix=tuple(corners[(1,1)][i]-corners[(1,0)][i]-corners[(0,1)][i]+base[i] for i in range(4))
assert all(v==0 for v in mix),mix
assert du==(F(-248046875,990677827584),F(65234375,208971104256),F(-3012109375,41278242816),F(-417578125,17414258688))
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert counts[:3]==(172,F(671875,53747712),F(671875,20155392))
print('PASS_STAGE114_INDEPENDENT_LITERAL_ORDERED_DFS')
