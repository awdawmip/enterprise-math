#!/usr/bin/env python3
"""Stage142 finite ternary iid author portable checker: exact Fraction DP and independent ordered integer DFS."""
from collections import defaultdict
from fractions import Fraction as F
N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(395290882339224,875825669873)
L=F(54591710813272,125117952839)
B=(11,0,1);J=(4,3,0)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 n,a,b=s
 return F(2**(a+b),3**a)
v={};act={};ties=[];gaps=[]
for s in reversed(S):
 c={'P':K*ratio(s),'Q':L}
 if s[0]<N:c['C']=1+sum((P[i]*v[t] for i,t in enumerate(child(s))),F())
 z=min(c.values());sel=[a for a in c if c[a]==z]
 v[s]=z;act[s]=sel[0]
 if len(sel)>1:ties.append((s,sel))
 gaps.extend([x-z for x in c.values() if x>z])
assert len(S)==680 and len(gaps)==1238
assert set((s,tuple(a)) for s,a in ties)=={(B,('Q','C')),(J,('P','C'))}
assert min(gaps)==F(145705394717149261,3309864318741169728)
assert v[(0,0,0)]==F(20527217718648439652667729706057,63970915514357897417453469696)
def calc(w,h):
 m={}
 for s in reversed(S):
  choices=({'Q':w,'C':1-w} if s==B else
           {'P':h,'C':1-h} if s==J else {act[s]:F(1)})
  z=[F()]*4
  for a,coin in choices.items():
   if coin==0:continue
   if a=='P':q=(F(0),F(1),F(0),F(0))
   elif a=='Q':q=(F(1),F(0),F(0),F(0))
   else:
    ch=[m[t] for t in child(s)]
    q=(sum((P[i]*ch[i][0] for i in range(3)),F()),
       sum((Q[i]*ch[i][1] for i in range(3)),F()),
       1+sum((P[i]*ch[i][2] for i in range(3)),F()),
       1+sum((Q[i]*ch[i][3] for i in range(3)),F()))
   for i in range(4):z[i]+=coin*q[i]
  m[s]=tuple(z)
 return m[(0,0,0)]
def dfs(w,h):
 assert w in (0,1) and h in (0,1)
 tP=defaultdict(int);tQ=defaultdict(int)
 count=defaultdict(int);hitP=defaultdict(int);hitQ=defaultdict(int)
 nvisited=0;stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,p,q=stack.pop();nvisited+=1;s=(n,a,b)
  if s in (B,J):count[s]+=1;hitP[s]+=p;hitQ[s]+=q
  choice=('Q' if w else 'C') if s==B else ('P' if h else 'C') if s==J else act[s]
  if choice!='C':tP[(n,choice)]+=p;tQ[(n,choice)]+=q;continue
  assert n<N
  stack.extend(((n+1,a+1,b,p*3,q),(n+1,a,b+1,p,q),(n+1,a,b,p*20,q*10)))
 return (
  sum((F(p,24**n) for (n,a),p in tP.items() if a=='Q'),F()),
  sum((F(q,12**n) for (n,a),q in tQ.items() if a=='P'),F()),
  sum((F(n*p,24**n) for (n,a),p in tP.items()),F()),
  sum((F(n*q,12**n) for (n,a),q in tQ.items()),F())
 ),nvisited,count,{s:F(hitP[s],24**s[0]) for s in (B,J)},{s:F(hitQ[s],12**s[0]) for s in (B,J)}
a=calc(F(0),F(0));b=calc(F(1),F(0));c=calc(F(0),F(1));d=calc(F(1),F(1))
sub=lambda x,y:tuple(i-j for i,j in zip(x,y))
add=lambda x,y:tuple(i+j for i,j in zip(x,y))
mult=lambda x,t:tuple(i*t for i in x)
db=sub(b,a);dj=sub(c,a)
assert sub(sub(d,b),sub(c,a))==(F(0),)*4
for (w,h,z,vis) in [(0,0,a,643270),(1,0,b,643138),(0,1,c,621718),(1,1,d,621586)]:
 q,visited,count,mp,mq=dfs(w,h)
 assert q==z and visited==vis
 assert count[B]==11 and count[J]==4
 assert mp[B]==F(107421875,1451188224) and mq[B]==F(107421875,725594112)
 assert mp[J]==F(5,768) and mq[J]==F(5,2592)
gap=lambda z:z[0]-z[1]
w0=-gap(a)/gap(db)
sl=-gap(dj)/gap(db)
assert w0==F(48289749016996117,81438720000000000)
assert sl==F(3939275036289,169664000000000)
assert 0<w0<1 and 0<w0+sl<1
M=lambda h:add(add(a,mult(db,w0+sl*h)),mult(dj,h))
lo=M(F(0));hi=M(F(1))
assert lo[0]==lo[1] and hi[0]==hi[1]
assert lo[0]==F(12238132337992249925,35205614928358539264)
assert lo[2]==F(72273275560058390723,5867602488059756544)
assert hi[0]==F(12238552734313788965,35205614928358539264)
assert hi[2]==F(24070360310471940161,1955867496019918848)
assert lo[2]>lo[3] and hi[2]>hi[3]
for x in (lo,hi):
 assert x[2]+L*x[0]+K*x[1]==v[(0,0,0)]
assert hi[0]-lo[0]==F(4379128349365,366725155503734784)
print('PASS_STAGE142_AUTHOR_EXACT: Bellman=680 strict_gaps=1238 ordered_DFS_four_corners=PASS alpha142=',hi[0],'V142=',hi[2])
