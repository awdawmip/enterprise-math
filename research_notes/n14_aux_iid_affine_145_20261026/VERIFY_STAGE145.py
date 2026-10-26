#!/usr/bin/env python3
"""Portable exact author reproducer, external ternary iid N14 Stage145, not native P000/Driver proof."""
from fractions import Fraction as F
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K,L=F(72079793676,175207181),F(69677182536,175207181)
R,T=(11,2,0),(7,1,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
 n,a,b=s
 return((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
H={};act={};tie=[];gap=[]
for s in reversed(S):
 d={'P':K*ratio(s),'Q':L}
 if s[0]<14:d['C']=1+sum((P[i]*H[t] for i,t in enumerate(child(s))),F())
 value=min(d.values());ops=tuple(k for k,x in d.items() if x==value)
 H[s]=value;act[s]=ops[0]
 if len(ops)>1:tie.append((s,ops))
 gap.extend(x-value for x in d.values() if x>value)
assert len(S)==680 and set(tie)=={(R,('P','C')),(T,('Q','C'))}
assert len(gap)==1238 and min(gap)==F(13737326062879,1569497517453312)
assert H[(0,0,0)]==F(704405532029576180110108633,2399485171279518914052096)
def choose(s,u,v):return ('P' if u else 'C') if s==R else ('Q' if v else 'C') if s==T else act[s]
def backward(u,v):
 memo={}
 for s in reversed(S):
  mode=choose(s,u,v)
  if mode=='P':obs=(F(),F(1),F(),F())
  elif mode=='Q':obs=(F(1),F(),F(),F())
  else:
   assert s[0]<14
   vals=[memo[t] for t in child(s)]
   obs=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*vals[i][j] for i in range(3)),F()) for j in range(4))
  memo[s]=obs
 return memo[(0,0,0)]
def literal(u,v):
 sums=[0,0,0,0];visits=0;first=defaultdict(lambda:[0,F(),F()])
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,x,y=stack.pop();visits+=1;s=(n,a,b)
  if s in (R,T):first[s][0]+=1;first[s][1]+=F(x,24**n);first[s][2]+=F(y,12**n)
  mode=choose(s,u,v)
  if mode=='C':
   assert n<14
   stack.extend(((n+1,a+1,b,x*3,y),(n+1,a,b+1,x,y),(n+1,a,b,x*20,y*10)))
  else:
   xx=x*24**(14-n);yy=y*12**(14-n)
   if mode=='Q':sums[0]+=xx
   if mode=='P':sums[1]+=yy
   sums[2]+=n*xx;sums[3]+=n*yy
 return tuple(F(sums[j],(24 if j%2==0 else 12)**14) for j in range(4)),visits,first
corners={}
for u,v,n in ((0,0,608476),(1,0,607816),(0,1,592726),(1,1,592066)):
 a,visits,first=literal(u,v)
 assert a==backward(u,v) and visits==n
 assert first[R]==[55,F(107421875,644972544),F(107421875,1451188224)]
 assert first[T]==[70,F(21875,2985984),F(21875,1119744)]
 corners[u,v]=a
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
M=corners[0,0];dR=sub(corners[1,0],M);dT=sub(corners[0,1],M)
assert sub(sub(corners[1,1],corners[1,0]),dT)==(F(),)*4
u0=(M[1]-M[0])/(dR[0]-dR[1])
us=(dT[1]-dT[0])/(dR[0]-dR[1])
assert u0==F(3833927448329263,4079680000000000)
assert us==F(1449219877,10199200000)
vmax=(1-u0)/us
assert vmax==F(245752551670737,579687950800000) and 0<vmax<1
def mix(v):return tuple(M[i]+(u0+us*v)*dR[i]+v*dT[i] for i in range(4))
lo,hi=mix(F()),mix(vmax)
assert lo[0]==lo[1]==F(11043651203155499027,31745312008792178688)
assert lo[2]==F(192050982046273350485,15872656004396089344)
assert hi[0]==hi[1]==F(61650988568176660266901,177207634216336528244736)
assert hi[2]==F(34260854261470059183743591,2835322147461384451915776)
assert hi[0]-lo[0]==F(14352537267262223320799,730252970868387684393418752)
assert lo[2]-hi[2]==(K+L)*(hi[0]-lo[0])
assert lo[2]-lo[3]==F(2427895767318664589,5290885334798696448)>0
assert hi[2]-hi[3]==F(434302292346744026388749,945107382487128150638592)>0
for x in (lo,hi):assert x[2]+L*x[0]+K*x[1]==H[(0,0,0)]
print("PASS_STAGE145_ALL_EXACT_RATIONAL")
