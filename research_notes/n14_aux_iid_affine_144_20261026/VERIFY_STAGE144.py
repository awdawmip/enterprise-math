#!/usr/bin/env python3
"""Portable Stage144 author verifier: exact N=14 Bellman, ordered literal DFS and full-real interval. External iid auxiliary model only."""
from fractions import Fraction as F
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K,L=F(412200,991),F(401944,991)
B,R=(11,0,1),(11,2,0)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def ch(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def r(s):return F(2**(s[1]+s[2]),3**s[1])
H={};action={};ties=[];gaps=[]
for s in reversed(S):
 d={'P':K*r(s),'Q':L}
 if s[0]<14:d['C']=1+sum((P[i]*H[t] for i,t in enumerate(ch(s))),F())
 v=min(d.values());o=tuple(k for k,x in d.items() if x==v)
 H[s]=v;action[s]=o[0]
 if len(o)>1:ties.append((s,o))
 gaps.extend(x-v for x in d.values() if x>v)
assert len(S)==680
assert set(ties)=={(B,('Q','C')),(R,('P','C'))}
assert len(gaps)==1238 and min(gaps)==F(392134385,79895973888)
assert H[(0,0,0)]==F(1347680099447446704127,4523958038641508352)
def decision(s,w,z):
 return ('Q' if w else 'C') if s==B else ('P' if z else 'C') if s==R else action[s]
def backward(w,z):
 A={}
 for s in reversed(S):
  m=decision(s,w,z)
  if m=='P':v=(F(),F(1),F(),F())
  elif m=='Q':v=(F(1),F(),F(),F())
  else:
   assert s[0]<14
   C=[A[t] for t in ch(s)]
   v=tuple((F(1) if k>=2 else F())+sum(((P if k%2==0 else Q)[i]*C[i][k] for i in range(3)),F()) for k in range(4))
  A[s]=v
 return A[(0,0,0)]
def literal(w,z):
 accum=[0,0,0,0];count=0;hit=defaultdict(lambda:[0,F(),F()])
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,x,y=stack.pop();count+=1;s=(n,a,b)
  if s in (B,R):
   hit[s][0]+=1;hit[s][1]+=F(x,24**n);hit[s][2]+=F(y,12**n)
  m=decision(s,w,z)
  if m=='C':
   assert n<14
   stack.extend(((n+1,a+1,b,x*3,y),(n+1,a,b+1,x,y),(n+1,a,b,x*20,y*10)))
  else:
   xx=x*24**(14-n);yy=y*12**(14-n)
   if m=='Q':accum[0]+=xx
   if m=='P':accum[1]+=yy
   accum[2]+=n*xx;accum[3]+=n*yy
 return (F(accum[0],24**14),F(accum[1],12**14),F(accum[2],24**14),F(accum[3],12**14)),count,hit
M={}
for w,z,expected in ((0,0,608608),(1,0,608476),(0,1,607948),(1,1,607816)):
 value,visit,hits=literal(w,z)
 assert value==backward(w,z) and visit==expected
 assert hits[B]==[11,F(107421875,1451188224),F(107421875,725594112)]
 assert hits[R]==[55,F(107421875,644972544),F(107421875,1451188224)]
 M[w,z]=value
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
M0=M[0,0];dB=sub(M[1,0],M0);dR=sub(M[0,1],M0)
assert sub(sub(M[1,1],M[1,0]),dR)==(F(),)*4
w0=(M0[1]-M0[0])/(dB[0]-dB[1]);ws=(dR[1]-dR[0])/(dB[0]-dB[1])
assert w0==F(6345912551670737,10179840000000000)
assert ws==F(1159,2892)
zmax=(1-w0)/ws
assert zmax==F(3833927448329263,4079680000000000)
assert 0<zmax<1 and w0+ws*zmax==1
def mix(z):return tuple(M0[i]+(w0+ws*z)*dB[i]+z*dR[i] for i in range(4))
lo,hi=mix(F()),mix(zmax)
assert lo[0]==lo[1]==F(1529836197244652353,4400701866044817408)
assert lo[2]==F(1503998623662640921,122241718501244928)
assert hi[0]==hi[1]==F(11043651203155499027,31745312008792178688)
assert hi[2]==F(192050982046273350485,15872656004396089344)
assert hi[0]-lo[0]==F(3799422101294299633,15301240388237830127616)
assert lo[2]-lo[3]==F(80069565131574865,154712174978138112)>0
assert hi[2]-hi[3]==F(2427895767318664589,5290885334798696448)>0
for v in (lo,hi):assert v[2]+L*v[0]+K*v[1]==H[(0,0,0)]
assert lo[2]-hi[2]==(K+L)*(hi[0]-lo[0])
print('PASS_STAGE144: 680 exact Bellman states, 1238 strict gaps, 4 integer DFS corners, full-real affine endpoints')
