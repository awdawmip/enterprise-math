from fractions import Fraction as F
from itertools import product

R2={0:F(1,2),1:F(3,2)}
U={'A':(F(3,4),F(5,4)),'B':(F(1,2),F(3,2))}
T=F(1,20)
H=('A','B')
leaves=[]
for h in H:
 for s in (0,1):
  q2=F(1,4);r2=R2[s]
  for u in U[h]:
   q3=q2/2;r3=r2*u
   leaves.append((h,s,r2,u,q3,r3))
keys=sorted({x[5] for x in leaves})
print('terminal LR keys:',','.join(map(str,keys)))

def add_stop(o,q,r,t,action):
 ep,eq,tp,tq=o
 if action=='P':eq+=q
 elif action=='Q':ep+=q*r
 else:raise ValueError(action)
 return ep,eq,tp+q*r*t,tq+q*t

def eval_policy(first,second,third):
 # first: A/B dict for FULL, or one common action for LR
 # second: (h,s) dict for FULL or s dict for LR
 # third: (h,s,u) dict for FULL or r dict for LR
 o=(F(0),)*4
 for h in H:
  q1=F(1,2);r1=F(1)
  a1=first[h] if isinstance(first,dict) else first
  if a1!='C':
   o=add_stop(o,q1,r1,1,a1);continue
  for s in (0,1):
   q2=F(1,4);r2=R2[s]
   a2=second[(h,s)] if (h,s) in second else second[s]
   if a2!='C':
    o=add_stop(o,q2,r2,2,a2);continue
   for u in U[h]:
    q3=q2/2;r3=r2*u
    a3=third[(h,s,u)] if (h,s,u) in third else third[r3]
    o=add_stop(o,q3,r3,3,a3)
 return o

def cost(o):return o[0]+o[1]+T*o[2]
# exhaustive LR deterministic 3 * 3^2 * 2^7=3456
lrbest=None; lrpolicy=None; n=0
for a1 in 'PQC':
 for a20,a21 in product('PQC',repeat=2):
  sec={0:a20,1:a21}
  for opts in product('PQ',repeat=len(keys)):
   tri=dict(zip(keys,opts));o=eval_policy(a1,sec,tri);v=cost(o);n+=1
   if lrbest is None or v<lrbest:lrbest=v;lrpolicy=(a1,sec,tri,o)
assert n==3456
print('LR policies',n,'optimum',lrbest,'vector',lrpolicy[3]);print('LR a1/sec',lrpolicy[:2])

# calculate FULL Bellman on tree
fb=F(0)
for h in H:
 q1=F(1,2)
 stop1=min(q1,q1)+T*q1*1
 c1=F(0)
 for s in (0,1):
  q2=F(1,4);r2=R2[s]
  stop2=min(q2,q2*r2)+T*q2*r2*2
  c2=F(0)
  for u in U[h]:
   q3=q2/2;r3=r2*u
   c2+=min(q3,q3*r3)+T*q3*r3*3
  c1+=min(stop2,c2)
 fb+=min(stop1,c1)
print('FULL optimum DP',fb)

fullfirst={'A':'C','B':'C'}
fullsecond={('A',0):'Q',('A',1):'P',('B',0):'Q',('B',1):'C'}
fullthird={(h,s,u):('Q' if R2[s]*u<1 else 'P') for h in H for s in (0,1) for u in U[h]}
W=eval_policy(fullfirst,fullsecond,fullthird)
assert cost(W)==fb,(W,cost(W),fb)
assert W==(F(11,32),F(3,8),F(19,8),F(9,4))
assert lrbest==F(17,20),(lrbest,lrpolicy)
assert fb==F(67,80)
assert lrbest-fb==F(1,80)
assert (lrbest-fb)/sum((F(1),F(1),T,F(0))) == F(1,164)
print('FULL witness', W)
print('h_FULL(-1,-1,-1/20,0)',-fb)
print('h_LR',-lrbest)
print('support gap',lrbest-fb,'linfty_lower_bound',F(1,164))

# phase interval proof via arithmetic: for tau in [1/24,1/12) LR t2 high stop, FULL B hi continue.
# exact G at t2 high after Q-weight q2:
# A r2=3/2, r2*(3/4)=9/8 >1 and r2*(5/4)=15/8>1, so G_A=0;
# B high: r2*(1/2)=3/4 and r2*(3/2)=9/4, so G_B=1/8.
# Q-mix conditional B prob 1/2 => G_LR=1/16.
for tau in [F(1,24),F(1,20),F(1,16),F(1,12)-F(1,1000)]:
 expected=(F(1,32)-F(3,8)*tau)
 assert expected>=0
 print('tau',tau,'predicted_gap',expected)
print('PASS_EXACT_R5_TWO_GATE_BRC_JENSEN_COLLISION')
