"""Independent exact backward moments and literal ordered first-hit DFS for Stage112."""
from fractions import Fraction as R
from functools import lru_cache
from collections import Counter
P=(R(1,8),R(1,24),R(5,6));Q=(R(1,12),R(1,12),R(5,6))
KK=R(50591871,53872);LL=R(2961024,3367)
A=(10,3,0);T=(14,7,4)
U0=R(199112072506703,211315200000000)
H1=R(306977,10565760000)
AL0=R(13084629088533672707,37682150988866125824)
V0=R(1930486964443856499985,150728603955464503296)
D=R(152537125,130840802044674048)

def next_states(s):
 n,a,b=s
 return (n+1,a+1,b),(n+1,a,b+1),(n+1,a,b)

def likelihood(s): return R(2**(s[1]+s[2]),3**s[1])

@lru_cache(None)
def solve(s):
 n=s[0]
 costs={'P':KK*likelihood(s),'Q':LL}
 if n<14:costs['C']=1+sum(p*solve(child)[0] for p,child in zip(P,next_states(s)))
 low=min(costs.values())
 minimizers=tuple(k for k,v in costs.items() if v==low)
 return low,minimizers

@lru_cache(None)
def moments(s,u,w):
 choices=solve(s)[1]
 def fixed(opt):
  if opt=='P':return (R(0),R(1),R(0),R(0))
  if opt=='Q':return (R(1),R(0),R(0),R(0))
  kids=[moments(k,u,w) for k in next_states(s)]
  return (sum(P[i]*kids[i][0] for i in range(3)),sum(Q[i]*kids[i][1] for i in range(3)),1+sum(P[i]*kids[i][2] for i in range(3)),1+sum(Q[i]*kids[i][3] for i in range(3)))
 def mix(op1,op2,p):
  a,b=fixed(op1),fixed(op2)
  return tuple(p*a[i]+(1-p)*b[i] for i in range(4))
 if s==A:
  assert choices==('P','C'),(s,choices)
  return mix('P','C',u)
 if s==T:
  assert choices==('P','Q'),(s,choices)
  return mix('Q','P',w)
 assert len(choices)==1,(s,choices)
 return fixed(choices[0])

def literal_hits():
 # Enumerate distinct ordered histories directly, no count aggregation.
 # A is forced to stop, which does not alter T due to (a+b) monotonicity.
 hits=Counter();seen=Counter(); stack=[(0,0,0)]
 while stack:
  s=stack.pop(); seen[s[0]]+=1
  if s==A:
   hits['A']+=1; continue
  if s==T:
   hits['T']+=1; continue
  opt=solve(s)[1]
  if len(opt)>1:raise RuntimeError((s,opt))
  if opt[0]=='C':stack.extend(next_states(s))
 rawP=R(hits['T'])*P[0]**7*P[1]**4*P[2]**3
 rawQ=R(hits['T'])*Q[0]**7*Q[1]**4*Q[2]**3
 return hits,rawP,rawQ,seen

def main():
 hits,p,q,seen=literal_hits()
 assert hits['A']==120 and hits['T']==10148
 assert (p,q)==(R(317125,37572373905408),R(317125,40122452017152)),(p,q)
 print('literal_first_hits',dict(hits),'T_P',p,'T_Q',q,'visited',sum(seen.values()))
 for w in (R(0),R(1,2),R(1)):
  u=U0+H1*w
  ep,eq,tp,tq=moments((0,0,0),u,w)
  assert ep==eq==AL0+D*w,(ep,eq,AL0+D*w)
  assert tp==V0-(KK+LL)*D*w
  assert tp>tq
  print('w',w,'u',u,'alpha',ep,'tp',tp,'tq',tq)
 print('PASS_STAGE112_INDEPENDENT_BACKWARD_AND_LITERAL_DFS')

if __name__=='__main__':main()
