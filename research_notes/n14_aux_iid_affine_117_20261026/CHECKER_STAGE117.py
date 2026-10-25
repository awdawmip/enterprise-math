#!/usr/bin/env python3
"""Exact Stage117 dual wall, all-state Bellman, BRC first hits, primal affine proof."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=14
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
D=(9,1,2);T=(14,7,4);X=(7,5,1)
K0=F(37550061,41440);L0=F(3296576,3885)
K1=F(7703713039590,8727240137);L1=F(7249159245096,8727240137)
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
def children(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def bell(k,l):
 @lru_cache(None)
 def value(s):
  v=[k*ratio(s),l]
  if s[0]<N:v.append(1+sum(p*value(t) for p,t in zip(P,children(s))))
  return min(v)
 winners={}; gaps=[]
 for s in S:
  vals={'P':k*ratio(s),'Q':l}
  if s[0]<N:vals['C']=1+sum(p*value(t) for p,t in zip(P,children(s)))
  winners[s]=[a for a,z in vals.items() if z==value(s)]
  gaps.extend(z-value(s) for z in vals.values() if z>value(s))
 return value,winners,gaps
V0,A0,G0=bell(K0,L0)
assert {s:x for s,x in A0.items() if len(x)>1}=={D:['Q','C'],T:['P','Q']}
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def evaluate(v,k,l):return v[0]+v[1]*k+v[2]*l
def coefficients(actions):
 @lru_cache(None)
 def chosen(s):return act(s,actions[s][0])
 def act(s,a):
  if a=='P':return (F(0),ratio(s),F(0))
  if a=='Q':return (F(0),F(0),F(1))
  suffix=[chosen(t) for t in children(s)]
  return tuple(F(i==0)+sum(P[j]*suffix[j][i] for j in range(3)) for i in range(3))
 return chosen,act
chosen0,act0=coefficients(A0)
dg=minus(act0(D,'C'),act0(D,'Q'))
m=-dg[1]/dg[2]
assert m==F(164096,214569)
walls=[]
for s in S:
 for a in (('P','Q','C') if s[0]<N else ('P','Q')):
  if a==A0[s][0]:continue
  diff=minus(act0(s,a),chosen0(s))
  intercept=evaluate(diff,K0,L0)
  velocity=-diff[1]-m*diff[2]
  assert intercept>=0
  if intercept>0 and velocity<0:walls.append((-intercept/velocity,s,a))
assert min(walls)==(F(172786349905893,7380751658720),X,'P')
assert sum(row[0]==min(walls)[0] for row in walls)==1
assert K1==K0-min(walls)[0] and L1==L0-m*min(walls)[0]
V1,A1,G1=bell(K1,L1)
assert len(S)==680 and len(G1)==1238
assert min(G1)==F(273655643173420723,6671206249789390848)
assert {s:a for s,a in A1.items() if len(a)>1}=={X:['P','C'],D:['Q','C']}
assert A1[T]==['P']
alpha0=F(900390062503198401793,2592933255351443128320)
Vstart=F(132635679890866772493569,10371733021405772513280)
assert V1((0,0,0))==Vstart+(K1+L1)*alpha0
@lru_cache(None)
def moments(s,w,y):
 def stopP():return (F(0),F(1),F(0),F(0))
 def stopQ():return (F(1),F(0),F(0),F(0))
 def cont():
  zz=[moments(t,w,y) for t in children(s)]
  return (sum(p*z[0] for p,z in zip(P,zz)),
          sum(q*z[1] for q,z in zip(Q,zz)),
          1+sum(p*z[2] for p,z in zip(P,zz)),
          1+sum(q*z[3] for q,z in zip(Q,zz)))
 if s==X:
  c=cont();p=stopP()
  return tuple(y*p[i]+(1-y)*c[i] for i in range(4))
 if s==D:
  c=cont();q=stopQ()
  return tuple(w*q[i]+(1-w)*c[i] for i in range(4))
 a=A1[s][0]
 return stopP() if a=='P' else stopQ() if a=='Q' else cont()
def root(w,y):return moments((0,0,0),w,y)
B=root(F(0),F(0))
dW=minus(root(F(1),F(0)),B)
dY=minus(root(F(0),F(1)),B)
assert root(F(1),F(1))==tuple(B[i]+dW[i]+dY[i] for i in range(4))
assert dW==(F(593265625,5283615080448),F(-430671875,5015306502144),F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert dY==(F(-816010405,5410421842378752),F(3257975,17832200896512),F(-8114835365,225434243432448),F(-151243295,13374150672384))
w0=F(374319733261181,1042086080000000)
gamma=-(dY[0]-dY[1])/(dW[0]-dW[1])
eta=dY[0]+gamma*dW[0]
assert gamma==F(12528414549,7443472000000)
assert eta==F(8727240137,228653726221467648)
assert 0<w0<w0+gamma<1
assert dY[2]+gamma*dW[2]==-(K1+L1)*eta
start=root(w0,F(0));end=root(w0+gamma,F(1))
assert start[0]==start[1]==alpha0 and start[2]==Vstart
assert start[2]>start[3] and end[2]>end[3]
assert end[0]==end[1]==F(900390161470101555373,2592933255351443128320)
assert end[2]==F(132635001628579939136609,10371733021405772513280)
front={(0,0,0):(1,F(1),F(1))};first={}
for depth in range(N+1):
 for s in (X,D):
  if depth==s[0] and s in front:first[s]=front[s]
 if depth==N:break
 follow=defaultdict(lambda:(0,F(0),F(0)))
 for s,(cnt,pm,qm) in front.items():
  if A1[s][0]=='C' or s in (X,D):
   for t,p,q in zip(children(s),P,Q):
    count,cp,cq=follow[t]
    follow[t]=(count+cnt,cp+pm*p,cq+qm*q)
 front=follow
assert first[X]==(28,F(35,1179648),F(35,4478976))
assert first[D]==(172,F(671875,53747712),F(671875,20155392))
assert X[1]>D[1] and X[0]<D[0]
# Candidate Stage118 wall after X saturates at P and D remains mixed.
chosen1,act1=coefficients(A1)
dg1=minus(act1(D,'C'),act1(D,'Q'))
m1=-dg1[1]/dg1[2]
walls2=[]
for s in S:
 for a in (('P','Q','C') if s[0]<N else ('P','Q')):
  if a==A1[s][0]:continue
  diff=minus(act1(s,a),chosen1(s))
  v=evaluate(diff,K1,L1);vel=-diff[1]-m1*diff[2]
  assert v>=0
  if v>0 and vel<0:walls2.append((-v/vel,s,a))
assert min(walls2)==(F(59905896822963,2583263080552),(13,6,4),'C')
K2=K1-min(walls2)[0];L2=L1-m1*min(walls2)[0]
assert (K2,L2)==(F(254421,296),F(90232,111))
print('PASS_STAGE117_DUAL_PRIMAL_680_STATE_EXACT')
print('ALPHA117',end[0],'V117',end[2],'ETA',eta)
print('STAGE118_CANDIDATE',K2,L2,(13,6,4))
