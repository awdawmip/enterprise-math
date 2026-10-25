#!/usr/bin/env python3
"""Portable author reproducer: Stage143 exact iid Bellman + independent literal DFS.
External N=14 model, no native P000/Driver authority implied.
"""
from fractions import Fraction as F
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(19411949464309662,45614547809953)
L=F(18882041753802888,45614547809953)
B=(11,0,1);C=(3,3,0)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 n,a,b=s
 return F(2**(a+b),3**a)
H={};action={};tie=[];gap=[]
for s in reversed(S):
 costs={'P':K*ratio(s),'Q':L}
 if s[0]<14:costs['C']=1+sum((P[i]*H[ch] for i,ch in enumerate(child(s))),F())
 z=min(costs.values());modes=[k for k,v in costs.items() if v==z]
 H[s]=z;action[s]=modes[0]
 if len(modes)>1:tie.append((s,tuple(modes)))
 gap += [x-z for x in costs.values() if x>z]
assert len(S)==680 and len(gap)==1238 and min(gap)==F(1685757022745149,59116453961699088)
assert set(tie)=={(B,('Q','C')),(C,('P','C'))}
assert H[(0,0,0)]==F(42222189293875024646776690163383,138821594513174762290616991744)
def obs(w,z):
 M={}
 for s in reversed(S):
  mode=('Q' if w else 'C') if s==B else ('P' if z else 'C') if s==C else action[s]
  if mode=='P':v=(F(0),F(1),F(0),F(0))
  elif mode=='Q':v=(F(1),F(0),F(0),F(0))
  else:
   ch=[M[t] for t in child(s)]
   v=(sum((P[i]*ch[i][0] for i in range(3)),F()),
      sum((Q[i]*ch[i][1] for i in range(3)),F()),
      F(1)+sum((P[i]*ch[i][2] for i in range(3)),F()),
      F(1)+sum((Q[i]*ch[i][3] for i in range(3)),F()))
  M[s]=v
 return M[(0,0,0)]
def literal(w,z):
 total=[0,0,0,0];hit=defaultdict(lambda:[0,F(0),F(0)]);visited=0
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,x,y=stack.pop();visited+=1;s=(n,a,b)
  if s in (B,C):
   hit[s][0]+=1;hit[s][1]+=F(x,24**n);hit[s][2]+=F(y,12**n)
  mode=('Q' if w else 'C') if s==B else ('P' if z else 'C') if s==C else action[s]
  if mode=='C':
   assert n<14
   stack.extend([(n+1,a+1,b,x*3,y),(n+1,a,b+1,x,y),(n+1,a,b,x*20,y*10)])
  else:
   xx=x*24**(14-n);yy=y*12**(14-n)
   if mode=='Q':total[0]+=xx
   if mode=='P':total[1]+=yy
   total[2]+=n*xx;total[3]+=n*yy
 return (F(total[0],24**14),F(total[1],12**14),F(total[2],24**14),F(total[3],12**14)),visited,hit
corners={(w,z):obs(w,z) for w in (0,1) for z in (0,1)}
for w,z,count in [(0,0,621718),(1,0,621586),(0,1,608608),(1,1,608476)]:
 v,visited,hit=literal(w,z)
 assert v==corners[(w,z)] and visited==count
 assert hit[B]==[11,F(107421875,1451188224),F(107421875,725594112)]
 assert hit[C]==[1,F(1,512),F(1,1728)]
M=corners[(0,0)]
diff=lambda x,y:tuple(a-b for a,b in zip(x,y))
dB=diff(corners[(1,0)],M);dC=diff(corners[(0,1)],M)
assert diff(diff(corners[(1,1)],corners[(1,0)]),dC)==(F(0),)*4
w0=F(50180601034414837,81438720000000000)
ws=F(17778769059123,2467840000000000)
assert (w0,ws)==((M[1]-M[0])/(dB[0]-dB[1]),(dC[1]-dC[0])/(dB[0]-dB[1]))
assert 0<w0<1 and 0<w0+ws<1
def mix(z):return tuple(M[i]+(w0+ws*z)*dB[i]+z*dC[i] for i in range(4))
lo=mix(F(0));hi=mix(F(1))
assert lo[0]==lo[1]==F(12238552734313788965,35205614928358539264)
assert hi[0]==hi[1]==F(1529836197244652353,4400701866044817408)
assert lo[2]==F(24070360310471940161,1955867496019918848)
assert hi[2]==F(1503998623662640921,122241718501244928)
assert hi[0]-lo[0]==F(45614547809953,11735204976119513088)
assert lo[2]-lo[3]==F(82155858325532762167,158425267177613426688)>0
assert hi[2]-hi[3]==F(80069565131574865,154712174978138112)>0
for v in (lo,hi):assert v[2]+L*v[0]+K*v[1]==H[(0,0,0)]
print('PASS_STAGE143: exact Bellman(680), gaps(1238), 4 literal DFS corners, full-real endpoints')
