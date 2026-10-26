#!/usr/bin/env python3
"""Stage152 external ternary iid N=14. Exact Bellman plus two distinct
four-observer calculations, including literal integer-weight ordered DFS.
Python 3 stdlib only; no floating point, no native X6 transfer.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(12844717560,36346217);L=F(12768141608,36346217)
B=(11,0,1);W=(8,3,3)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680
def nex(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def likelihood(s):return F(2**(s[1]+s[2]),3**s[1])
H={};A={};ties=[];gaps=[]
for s in reversed(S):
 opts={'P':K*likelihood(s),'Q':L}
 if s[0]<N:opts['C']=1+sum((P[i]*H[nex(s)[i]] for i in range(3)),F())
 best=min(opts.values()); choices=tuple(x for x in opts if opts[x]==best)
 if len(choices)>1:ties.append((s,choices))
 A[s]=('Q' if s in (B,W) else choices[0]);assert A[s] in choices
 H[s]=best;gaps.extend(x-best for x in opts.values() if x>best)
assert set(ties)=={(B,('Q','C')),(W,('Q','C'))}
assert len(gaps)==1238 and min(gaps)==F(204027667,1130512733568)
assert H[0,0,0]==F(341463027624594134301829727,1327376472826305935572992)
def act(s,b,w):
 if s==B:return 'Q' if b else 'C'
 if s==W:return 'Q' if w else 'C'
 return A[s]
def backwards(b,w):
 obs={}
 for s in reversed(S):
  z=act(s,b,w)
  if z=='Q':v=(F(1),F(),F(),F())
  elif z=='P':v=(F(),F(1),F(),F())
  else:
   assert s[0]<N
   child=nex(s)
   v=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*obs[child[i]][j] for i in range(3)),F()) for j in range(4))
  obs[s]=v
 return obs[0,0,0]
def ordered_dfs(b,w):
 total=[0]*4;first=defaultdict(lambda:[0,F(),F()]);seen=0
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,c,x,y=stack.pop();seen+=1;s=(n,a,c)
  if s in (B,W):
   first[s][0]+=1;first[s][1]+=F(x,24**n);first[s][2]+=F(y,12**n)
  z=act(s,b,w)
  if z=='C':
   assert n<N
   stack.extend(((n+1,a+1,c,3*x,y),(n+1,a,c+1,x,y),(n+1,a,c,20*x,10*y)))
  else:
   xx=x*24**(N-n); yy=y*12**(N-n)
   if z=='Q':total[0]+=xx
   else:total[1]+=yy
   total[2]+=n*xx;total[3]+=n*yy
 return tuple(F(total[j],(24 if j%2==0 else 12)**N) for j in range(4)),seen,first
corners={};visits=[]
for b,w in product((0,1),repeat=2):
 v,count,first=ordered_dfs(b,w)
 assert v==backwards(b,w)
 corners[b,w]=v;visits.append(count)
 assert tuple(first[B])==(11,F(107421875,1451188224),F(107421875,725594112))
 assert tuple(first[W])==(224,F(175,7962624),F(175,3359232))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
M=corners[0,0];dB=sub(corners[1,0],M);dW=sub(corners[0,1],M)
assert sub(sub(corners[1,1],corners[1,0]),dW)==(F(),)*4
b0=(M[1]-M[0])/(dB[0]-dB[1]);db=(dW[1]-dW[0])/(dB[0]-dB[1])
assert b0==F(8061971501813291,8143872000000000)
assert db==-F(797257531,6362400000000)
assert 0<b0+db<b0<1
def obs(w):
 return add(add(M,tuple((b0+db*w)*x for x in dB)),tuple(w*x for x in dW))
lo,hi=obs(F()),obs(F(1))
assert lo[0]==lo[1] and hi[0]==hi[1]
assert lo[0]==F(18373001785623238325,52808422392537808896)
assert lo[2]==F(318746112099955105013,26404211196268904448)
assert hi[0]==F(18373003413933759925,52808422392537808896)
assert hi[2]==F(318745538371909741813,26404211196268904448)
assert lo[2]>lo[3] and hi[2]>hi[3]
assert all(z[2]+L*z[0]+K*z[1]==H[0,0,0] for z in (lo,hi))
assert hi[0]-lo[0]==F(6360587975,206282899970850816)
assert (lo[2]-hi[2])/(hi[0]-lo[0])==K+L==F(25612859168,36346217)
# For every real 0<=w<=1, b(w)=b0+db*w stays legal.
# The four observers are affine, both errors equal, tP>tQ.
# Bellman support is attained at both endpoints and thus at all real w.
# Right sharpness: any support attainer must choose minimizers only and
# equalize both errors (K,L>0); B/W are the only ties. Their path cones are
# incomparable (W has 3 first symbols, B has 0), so history-dependent coins
# can be replaced by effective coins preserving P,Q masses and four observers.
# Balance forces b(w), and common error<=hi[0]. Compactness of the finite
# randomized-policy space rules out equality with this support to the right.
print('PASS_STAGE152 680 states 1238 strict gaps; four exact corners twice')
print('first-hit B=11,W=224; ordered DFS visits',visits,'mixed=0')
print('alpha152',hi[0],'V152',hi[2],'eta',hi[0]-lo[0],'slope',K+L)
