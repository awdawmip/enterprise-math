#!/usr/bin/env python3
"""Portable independent exact Stage116 dual/primal certificate (standard library)."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K0=F(2533113,2734); L0=F(1181272,1367)
K=F(37550061,41440); L=F(3296576,3885)
D=(9,1,2); E=(12,4,1); T=(14,7,4)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def R(s):return F(2**(s[1]+s[2]),3**s[1])
def kids(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def make_bell(k,l):
 @lru_cache(None)
 def H(s):
  v=[k*R(s),l]
  if s[0]<N:v.append(1+sum(p*H(c) for p,c in zip(P,kids(s))))
  return min(v)
 acts={}
 gaps=[]
 for s in S:
  v={'P':k*R(s),'Q':l}
  if s[0]<N:v['C']=1+sum(p*H(c) for p,c in zip(P,kids(s)))
  acts[s]=[a for a,x in v.items() if x==H(s)]
  gaps+=list(x-H(s) for x in v.values() if x>H(s))
 return H,acts,gaps
H0,A0,G0=make_bell(K0,L0)
assert {s:a for s,a in A0.items() if len(a)>1}=={D:['Q','C'],E:['P','C']}
@lru_cache(None)
def affine(s):return action(s,A0[s][0])
def action(s,a):
 if a=='P':return (F(0),R(s),F(0))
 if a=='Q':return (F(0),F(0),F(1))
 c=[affine(t) for t in kids(s)]
 return tuple(F(i==0)+sum(P[j]*c[j][i] for j in range(3)) for i in range(3))
def diff(x,y):return tuple(a-b for a,b in zip(x,y))
def eval3(v,k,l):return v[0]+v[1]*k+v[2]*l
dg=diff(action(D,'C'),action(D,'Q'))
m=-dg[1]/dg[2]
assert m==F(164096,214569)
walls=[]
for s in S:
 for a in (['P','Q','C'] if s[0]<N else ['P','Q']):
  if a==A0[s][0]:continue
  gap=diff(action(s,a),affine(s))
  v=eval3(gap,K0,L0)
  slope=-gap[1]-m*gap[2]
  assert v>=0
  if v>0 and slope<0:walls.append((-v/slope,s,a))
wall=min(walls)
assert wall==(F(1155167973,56648480),T,'P')
assert sum(x==wall[0] for x,s,a in walls)==1
assert (K,L)==(K0-wall[0],L0-m*wall[0])
H,A,G=make_bell(K,L)
assert len(S)==680 and len(G)==1238
assert min(G)==F(200314681163,7919307325440)
assert {s:a for s,a in A.items() if len(a)>1}=={D:['Q','C'],T:['P','Q']}
assert A[E]==['P']
@lru_cache(None)
def moment(s,w,u):
 if s==T:return (1-u,u,F(0),F(0))
 if s==E:return (F(0),F(1),F(0),F(0))
 a=A[s][0]
 def cont():
  zz=[moment(c,w,u) for c in kids(s)]
  return (sum(p*z[0] for p,z in zip(P,zz)),
          sum(q*z[1] for q,z in zip(Q,zz)),
          1+sum(p*z[2] for p,z in zip(P,zz)),
          1+sum(q*z[3] for q,z in zip(Q,zz)))
 if s==D:
  t=cont()
  return tuple(w*x+(1-w)*y for x,y in zip((F(1),F(0),F(0),F(0)),t))
 if a=='P':return (F(0),F(1),F(0),F(0))
 if a=='Q':return (F(1),F(0),F(0),F(0))
 return cont()
def root(w,u):return moment((0,0,0),w,u)
b=root(F(0),F(0))
dw=diff(root(F(1),F(0)),b);du=diff(root(F(0),F(1)),b)
assert root(F(1),F(1))==tuple(b[i]+dw[i]+du[i] for i in range(4))
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),
           F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert du==(F(-614375,75144747810816),F(614375,80244904034304),F(0),F(0))
w0=F(374236473161181,1042086080000000)
alpha0=F(900390060440962701793,2592933255351443128320)
V0=F(132635694365041929281069,10371733021405772513280)
gamma=-(du[0]-du[1])/(dw[0]-dw[1])
assert gamma==F(118943,1488694400)
w1=w0+gamma;eta=du[0]+gamma*dw[0]
alpha1=alpha0+eta;V1=V0-(K+L)*eta
assert eta==F(22731875,28581715777683456)
assert alpha1==F(900390062503198401793,2592933255351443128320)
assert V1==F(132635679890866772493569,10371733021405772513280)
assert 0<w0<w1<1
v0=root(w0,F(0));v1=root(w1,F(1))
assert v0[:3]==(alpha0,alpha0,V0) and v1[:3]==(alpha1,alpha1,V1)
assert v0[2]>v0[3] and v1[2]>v1[3]
assert H((0,0,0))==V0+(K+L)*alpha0
front={(0,0,0):(1,F(1),F(1))}; first={}
for depth in range(15):
 for s in (D,T):
  if depth==s[0] and s in front:first[s]=front[s]
 if depth==14:break
 nxt=defaultdict(lambda:(0,F(0),F(0)))
 for s,(count,pm,qm) in front.items():
  if A[s][0]=='C' or s==D:
   for ch,p,q in zip(kids(s),P,Q):
    n,pp,qq=nxt[ch]
    nxt[ch]=(n+count,pp+pm*p,qq+qm*q)
 front=nxt
assert first[D]==(172,F(671875,53747712),F(671875,20155392))
assert first[T]==(9830,F(614375,75144747810816),F(614375,80244904034304))
assert T[1]-D[1]>T[0]-D[0]
print('PASS_STAGE116_PORTABLE_EXACT_FULL_REAL')
