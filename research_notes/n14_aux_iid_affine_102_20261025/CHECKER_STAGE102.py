#!/usr/bin/env python3
"""Stage102 portable exact checker: external 3-symbol finite iid N=14.
Author checker; exact fractions; no claim to P000/native Result.
Run: python CHECKER_STAGE102.py
"""
from fractions import Fraction as F
from math import comb

P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(96424629120,78169393)
L=F(91338977736,78169393)
A=(5,0,2); B=(12,0,1)
alpha=F(152150366213667431,438244169232678912)
v101=F(44227501292577155,3423782572130304)
s101=F(1033425075169483,1228800000000000)
def ch(v):
 n,a,b=v
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def likelihood(v):
 return F(2**(v[1]+v[2]),3**v[1])

D={}; best={}; gap={}
for n in range(14,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   v=(n,a,b)
   scores={'P':K*likelihood(v),'Q':L}
   if n<14:
    scores['C']=1+sum((P[i]*D[w] for i,w in enumerate(ch(v))),F(0))
   lo=min(scores.values())
   D[v]=lo
   best[v]=tuple(x for x in scores if scores[x]==lo)
   gap[v]={x:val-lo for x,val in scores.items()}
assert len(D)==680
assert sum(len(x)-1 for x in gap.values())==1240
assert sum(z>0 for row in gap.values() for z in row.values())==1238
assert {v for v,ops in best.items() if len(ops)>1}=={A,B}
assert D[0,0,0]==F(3626353483971594146819209007,4282160086838473289367552)
assert D[0,0,0]==v101+(K+L)*alpha

def policy_outcome(u,s):
 W={}
 for n in range(14,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b)
    acts=({'Q':u,'C':1-u} if v==A else
          {'Q':s,'C':1-s} if v==B else
          {best[v][0]:F(1)})
    out=[F(0)]*4
    for act,weight in acts.items():
     if act=='Q': part=(F(1),F(0),F(0),F(0))
     elif act=='P': part=(F(0),F(1),F(0),F(0))
     else:
      x=[W[w] for w in ch(v)]
      part=(sum((P[i]*x[i][0] for i in range(3)),F(0)),
            sum((Q[i]*x[i][1] for i in range(3)),F(0)),
            1+sum((P[i]*x[i][2] for i in range(3)),F(0)),
            1+sum((Q[i]*x[i][3] for i in range(3)),F(0)))
     for j in range(4):out[j]+=weight*part[j]
    W[v]=tuple(out)
 return W[(0,0,0)]

# First arrivals in the strict optimal prefix tree, with no tie descent.
fP={(0,0,0):F(1)};fQ={(0,0,0):F(1)};count={(0,0,0):1}
for n in range(14):
 for a in range(n+1):
  for b in range(n-a+1):
   v=(n,a,b)
   if v not in fP or v in (A,B) or best[v][0]!='C':continue
   for i,w in enumerate(ch(v)):
    fP[w]=fP.get(w,F(0))+fP[v]*P[i]
    fQ[w]=fQ.get(w,F(0))+fQ[v]*Q[i]
    count[w]=count.get(w,0)+count[v]
assert (count[A],fP[A],fQ[A])==(10,F(625,62208),F(625,15552))
assert (count[B],fP[B],fQ[B])==(12,F(48828125,725594112),F(48828125,362797056))
assert A[2]>B[2] and A[0]<B[0]  # no causal ancestry

def suffix(v):
 # Continue at v then take STRICT optimal actions (the other tie cannot be descended to).
 W={}
 for n in range(14,v[0]-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    x=(n,a,b); op=best[x][0]
    if op=='Q':out=(F(1),F(0),F(0),F(0))
    elif op=='P':out=(F(0),F(1),F(0),F(0))
    else:
     c=[W[y] for y in ch(x)]
     out=(sum((P[i]*c[i][0] for i in range(3)),F(0)),
          sum((Q[i]*c[i][1] for i in range(3)),F(0)),
          1+sum((P[i]*c[i][2] for i in range(3)),F(0)),
          1+sum((Q[i]*c[i][3] for i in range(3)),F(0)))
    W[x]=out
 c=[W[y] for y in ch(v)]
 return (sum((P[i]*c[i][0] for i in range(3)),F(0)),
         sum((Q[i]*c[i][1] for i in range(3)),F(0)),
         1+sum((P[i]*c[i][2] for i in range(3)),F(0)),
         1+sum((Q[i]*c[i][3] for i in range(3)),F(0)))
rA=suffix(A);rB=suffix(B)
assert rA==(F(8102662423,8153726976),F(1489889,1289945088),F(1650008497,1019215872),F(145197871,107495424))
assert rB==(F(63,64),F(1,144),F(9,8),F(13,12))
x=fP[A]*(1-rA[0]);y=fQ[A]*rA[1]
e=fP[B]*(1-rB[0]);h0=fQ[B]*rB[1]
h=(x+y)/(e+h0)
eta=x-e*h
assert h==F(1437504293,26112000000)
assert eta==F(48855870625,9700717287702528)>0
s_end=s101-h
assert 0<s_end<1
expected=((alpha,alpha,v101,F(449462455858132795,36520347436056576)),
          (F(2586593746940986327,7450150876955541504),F(2586593746940986327,7450150876955541504),F(751163408448101635,58204303726215168),F(22836431111877252545,1862537719238885376)))
for i,u in enumerate((F(0),F(1))):
 out=policy_outcome(u,s101-h*u)
 assert out==expected[i]
 assert out[0]==out[1]==alpha+eta*u
 assert out[2]+L*out[0]+K*out[1]==D[0,0,0]
 assert out[2]>out[3]
# Linear dependence on u follows from the proven disjoint first-hit cones.
assert policy_outcome(F(1,2),s101-h/2)[0]==alpha+eta/2
print('PASS: 680 Bellman states; 1240 gaps; 2 ties; exact real interval; sharpness algebra')
print('alpha102=',expected[1][0],'V102=',expected[1][2],'eta102=',eta)
