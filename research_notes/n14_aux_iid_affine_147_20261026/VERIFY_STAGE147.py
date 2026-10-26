from fractions import Fraction as F
from collections import defaultdict
import json
N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(488636304489,1197470344); L=F(59157759848,149683793)
T=(7,1,2); W=(10,4,1); U=(8,6,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def nexts(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
H={};act={};ties=[];pos=[]
for s in reversed(S):
 d={'P':K*ratio(s),'Q':L}
 if s[0]<N:d['C']=1+sum((P[i]*H[t] for i,t in enumerate(nexts(s))),F())
 h=min(d.values());o=tuple(k for k,v in d.items() if v==h)
 H[s]=h;act[s]=o[0]
 if len(o)>1:ties.append((s,o))
 pos.extend(v-h for v in d.values() if v>h)
assert len(S)==680 and set(ties)=={(T,('Q','C')),(W,('P','C'))},ties
assert len(pos)==1238 and min(pos)==F(6129035788073,1340860232871936)
assert H[0,0,0]==F(59027133919370211202074389,202463115774324935491584)
assert act[U]=='P'
def mode(s,v,w):
 if s==T:return 'Q' if v else 'C'
 if s==W:return 'P' if w else 'C'
 return act[s]
def backward(v,w):
 memo={}
 for s in reversed(S):
  m=mode(s,v,w)
  if m=='P':z=(F(0),F(1),F(0),F(0))
  elif m=='Q':z=(F(1),F(0),F(0),F(0))
  else:
   c=[memo[t] for t in nexts(s)]
   z=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*c[i][j] for i in range(3)),F()) for j in range(4))
  memo[s]=z
 return memo[0,0,0]
def direct(v,w):
 total=[0]*4;hit=defaultdict(lambda:[0,F(),F()]);seen=0;stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,x,y=stack.pop();seen+=1;s=(n,a,b)
  if s in (T,W):
   hit[s][0]+=1;hit[s][1]+=F(x,24**n);hit[s][2]+=F(y,12**n)
  m=mode(s,v,w)
  if m=='C':
   assert n<N
   stack.extend(((n+1,a+1,b,3*x,y),(n+1,a,b+1,x,y),(n+1,a,b,x*20,y*10)))
  else:
   X=x*24**(N-n);Y=y*12**(N-n)
   if m=='Q':total[0]+=X
   if m=='P':total[1]+=Y
   total[2]+=n*X;total[3]+=n*Y
 return tuple(F(total[j],(24 if j%2==0 else 12)**N) for j in range(4)),seen,hit
M={};visits=[];hits={}
for v,w in ((0,0),(1,0),(0,1),(1,1)):
 z,n,h=direct(v,w)
 assert z==backward(v,w)
 M[v,w]=z;visits.append(n);hits[v,w]=h
assert visits==[606232,590482,583552,567802]
for state,expected in [(T,(70,F(21875,2985984),F(21875,1119744))),(W,(756,F(21875,7077888),F(21875,17915904)))]:
 for h in hits.values():assert tuple(h[state])==expected
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=M[0,0];dT=sub(M[1,0],base);dW=sub(M[0,1],base)
assert sub(sub(M[1,1],M[1,0]),dW)==(F(),)*4
v0=(base[1]-base[0])/(dT[0]-dT[1])
vs=(dW[1]-dW[0])/(dT[0]-dT[1])
assert (v0,vs)==(F(28086276907713,66250051520000),F(36045864,207031411))
assert 0<v0<v0+vs<1
def mix(w):return tuple(base[j]+(v0+vs*w)*dT[j]+w*dW[j] for j in range(4))
lo,hi=mix(F()),mix(F(1))
alpha146=F(246603954391193214663775,708830536865346112978944)
V146=F(274086831038532347195394643,22682577179691075615326208)
alpha147=F(246608842944125560263775,708830536865346112978944)
V147=F(273961171711816388948994643,22682577179691075615326208)
assert lo[0]==lo[1]==alpha146 and lo[2]==V146
assert hi[0]==hi[1]==alpha147 and hi[2]==V147
assert hi[0]-lo[0]==F(3274332971875,474771825210949632)>0
assert lo[2]>lo[3] and hi[2]>hi[3]
assert lo[2]-lo[3]==F(386046490754488341010345,840095451099669467234304)
assert hi[2]-hi[3]==F(386586105152287841810345,840095451099669467234304)
for z in (lo,hi):assert z[2]+L*z[0]+K*z[1]==H[0,0,0]
assert lo[2]-hi[2]==(K+L)*(hi[0]-lo[0])
print('PASS_STAGE147_EXACT_FRACTION_AND_LITERAL_INTEGER_DFS',len(S),len(pos),visits)
