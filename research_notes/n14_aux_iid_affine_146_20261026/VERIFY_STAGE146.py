from fractions import Fraction as F
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(580442338958517,1418470016864);L=F(52669253445512,132981564081)
T=(7,1,2);U=(8,6,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def nexts(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
H={};act={};ties=[];positive=[]
for s in reversed(S):
 d={'P':K*ratio(s),'Q':L}
 if s[0]<14:d['C']=1+sum((P[i]*H[t] for i,t in enumerate(nexts(s))),F())
 h=min(d.values());o=tuple(k for k,v in d.items() if v==h)
 H[s]=h;act[s]=o[0]
 if len(o)>1:ties.append((s,o))
 positive += [v-h for v in d.values() if v>h]
assert len(S)==680 and set(ties)=={(T,('Q','C')),(U,('P','C'))}
assert len(positive)==1238 and min(positive)==F(6129035788073,1378752856391808)
assert H[(0,0,0)]==F(1064448260606076968085635550307,3642399692121256208464084992)
def mode(s,v,u):
 return ('Q' if v else 'C') if s==T else ('P' if u else 'C') if s==U else act[s]
def backward(v,u):
 memo={}
 for s in reversed(S):
  m=mode(s,v,u)
  if m=='P':z=(F(),F(1),F(),F())
  elif m=='Q':z=(F(1),F(),F(),F())
  else:
   c=[memo[t] for t in nexts(s)]
   z=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*c[i][j] for i in range(3)),F()) for j in range(4))
  memo[s]=z
 return memo[0,0,0]
def direct(v,u):
 total=[0]*4;hit=defaultdict(lambda:[0,F(),F()]);seen=0;stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,x,y=stack.pop();seen+=1;s=(n,a,b)
  if s in (T,U):
   hit[s][0]+=1;hit[s][1]+=F(x,24**n);hit[s][2]+=F(y,12**n)
  m=mode(s,v,u)
  if m=='C':
   assert n<14
   stack.extend(((n+1,a+1,b,3*x,y),(n+1,a,b+1,x,y),(n+1,a,b,x*20,y*10)))
  else:
   X=x*24**(14-n);Y=y*12**(14-n)
   if m=='Q':total[0]+=X
   if m=='P':total[1]+=Y
   total[2]+=n*X;total[3]+=n*Y
 return tuple(F(total[j],(24 if j%2==0 else 12)**14) for j in range(4)),seen,hit
M={};visits=[]
for v,u in ((0,0),(1,0),(0,1),(1,1)):
 z,n,h=direct(v,u)
 assert z==backward(v,u)
 assert h[T]==[70,F(21875,2985984),F(21875,1119744)]
 assert h[U]==[11,F(11,150994944),F(11,429981696)]
 M[v,u]=z;visits.append(n)
assert visits==[607816,592066,606232,590482],visits
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=M[0,0];dT=sub(M[1,0],base);dU=sub(M[0,1],base)
assert sub(sub(M[1,1],M[1,0]),dU)==(F(),)*4
v0=(base[1]-base[0])/(dT[0]-dT[1])
vs=(dU[1]-dU[0])/(dT[0]-dT[1])
assert v0==F(245752551670737,579687950800000)
assert vs==F(9485087007,2318751803200000)>0
assert 0<v0<v0+vs<1
def mix(u):return tuple(base[j]+(v0+vs*u)*dT[j]+u*dU[j] for j in range(4))
lo,hi=mix(F()),mix(F(1))
assert lo[0]==lo[1]==F(61650988568176660266901,177207634216336528244736)
assert lo[2]==F(34260854261470059183743591,2835322147461384451915776)
assert hi[0]==hi[1]==F(246603954391193214663775,708830536865346112978944)
assert hi[2]==F(274086831038532347195394643,22682577179691075615326208)
assert hi[0]-lo[0]==F(487599068297,2916998094096074539008)>0
assert lo[2]>lo[3] and hi[2]>hi[3]
for z in (lo,hi):assert z[2]+L*z[0]+K*z[1]==H[0,0,0]
assert lo[2]-hi[2]==(K+L)*(hi[0]-lo[0])
print('PASS_STAGE146_FRACTION_AND_LITERAL_INTEGER_DFS',len(S),len(positive),visits)
