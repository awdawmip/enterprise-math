"""Exact Stage150 finite proof certificate, Python 3 stdlib only.
Full ordered policy space is covered by Bellman lower bound; DFS validates
four concrete deterministic history policies with integer branch weights.
"""
from fractions import Fraction as F
from collections import defaultdict

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
B=(11,0,1)
R=(13,5,2)
K0=F(100164600,266527)
L0=F(98815768,266527)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def nxt(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s): return F(2**(s[1]+s[2]),3**s[1])
def solve(K,L,make_coeff=False):
 H={};A={};C={};ties=[];positive=[]
 for s in reversed(S):
  d={'P':K*ratio(s),'Q':L}
  coeff={'P':(F(),ratio(s),F()),'Q':(F(),F(),F(1))}
  if s[0]<N:
   child=nxt(s)
   d['C']=F(1)+sum((P[i]*H[child[i]] for i in range(3)),F())
   if make_coeff:
    coeff['C']=tuple((F(1) if j==0 else F())+sum((P[i]*C[child[i]][j] for i in range(3)),F()) for j in range(3))
  h=min(d.values());actions=tuple(k for k in d if d[k]==h)
  choice='Q' if s==B and 'Q' in actions else 'P' if s==R and 'P' in actions else actions[0]
  H[s]=h;A[s]=choice
  if make_coeff:C[s]=coeff[choice]
  if len(actions)>1:ties.append((s,actions))
  positive.extend(y-h for y in d.values() if y>h)
 return H,A,C,ties,positive

# Stage149 -> Stage150 along the B tie ray.
H0,A0,C0,T0,_=solve(K0,L0,True)
assert len(S)==680
assert set(T0)=={(B,('Q','C')),((11,7,3),('P','C'))}
coefB=tuple((F(1) if j==0 else F())+sum((P[i]*C0[nxt(B)[i]][j] for i in range(3)),F()) for j in range(3))
dK=F(-1);dL=-coefB[1]/(F(1)-coefB[2]);assert dL==F(-112,129)
# The full ray gap scan, including strict competitors at every state.
changes={};C={};H={};A={}
for s in reversed(S):
 d={'P':K0*ratio(s),'Q':L0}
 c={'P':(F(),ratio(s),F()),'Q':(F(),F(),F(1))}
 if s[0]<N:
  z=nxt(s);d['C']=F(1)+sum((P[i]*H[z[i]] for i in range(3)),F())
  c['C']=tuple((F(1) if j==0 else F())+sum((P[i]*C[z[i]][j] for i in range(3)),F()) for j in range(3))
 h=min(d.values());options=[k for k in d if d[k]==h]
 a='Q' if s==B else 'P' if s==(11,7,3) else options[0]
 assert a in options
 H[s]=d[a];A[s]=a;C[s]=c[a]
 for other in d:
  if other==a:continue
  gap=d[other]-H[s]
  slope=(c[other][1]-C[s][1])*dK+(c[other][2]-C[s][2])*dL
  changes[s,other]=(gap,slope)
assert changes[B,'C']==(0,0)
assert changes[(11,7,3),'C'][0]==0 and changes[(11,7,3),'C'][1]>0
hits=[(gap/(-sl),s,act) for (s,act),(gap,sl) in changes.items() if gap>0 and sl<0]
t0,s0,act0=min(hits)
assert (t0,s0,act0)==(F(202961376,32249767),R,'P')
K=K0+dK*t0;L=L0+dL*t0
assert K==F(44712,121) and L==F(44200,121)
HD,AD,_,ties,pos=solve(K,L)
assert HD[0,0,0]==F(1183067867036626543351,4418962039762845696)
assert set(ties)=={(B,('Q','C')),(R,('P','C'))}
assert len(pos)==1238 and min(pos)==F(607,29403)

def action(s,b,r):
 if s==B:return 'Q' if b else 'C'
 if s==R:return 'P' if r else 'C'
 return AD[s]
def backward(b,r):
 z={}
 for s in reversed(S):
  a=action(s,b,r)
  if a=='P':v=(F(),F(1),F(),F())
  elif a=='Q':v=(F(1),F(),F(),F())
  else:
   ch=nxt(s)
   v=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*z[ch[i]][j] for i in range(3)),F()) for j in range(4))
  z[s]=v
 return z[0,0,0]
def ordered_dfs(b,r):
 totals=[0]*4;seen=0;first=defaultdict(lambda:[0,F(),F()])
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,c,x,y=stack.pop();seen+=1;s=(n,a,c)
  if s in (B,R):
   first[s][0]+=1;first[s][1]+=F(x,24**n);first[s][2]+=F(y,12**n)
  ac=action(s,b,r)
  if ac=='C':
   assert n<14
   stack.extend(((n+1,a+1,c,3*x,y),(n+1,a,c+1,x,y),(n+1,a,c,20*x,10*y)))
  else:
   xx=x*24**(14-n);yy=y*12**(14-n)
   if ac=='Q':totals[0]+=xx
   else:totals[1]+=yy
   totals[2]+=n*xx;totals[3]+=n*yy
 return tuple(F(totals[j],(24 if j%2==0 else 12)**14) for j in range(4)),seen,first
corners={};vis=[]
for b,r in ((0,0),(1,0),(0,1),(1,1)):
 v,count,first=ordered_dfs(b,r)
 assert v==backward(b,r)
 corners[b,r]=v;vis.append(count)
 assert tuple(first[B])==(11,F(107421875,1451188224),F(107421875,725594112))
 assert tuple(first[R])==(14662,F(114546875,440301256704),F(114546875,835884417024))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];dB=sub(corners[1,0],base);dR=sub(corners[0,1],base)
assert sub(sub(corners[1,1],corners[1,0]),dR)==(F(),)*4
b0=(base[1]-base[0])/(dB[0]-dB[1]);dbdr=(dR[1]-dR[0])/(dB[0]-dB[1])
assert (b0,dbdr)==(F(7957468505269291,8143872000000000),F(3658169,636240000))
assert 0<b0<b0+dbdr<1
vec=lambda r:tuple(base[i]+(b0+dbdr*r)*dB[i]+r*dR[i] for i in range(4))
lo=vec(F());hi=vec(F(1))
assert (lo[0],lo[2])==(F(6124245464096172775,17602807464179269632),F(106280162016260661671,8801403732089634816))
assert (hi[0],hi[2])==(F(18372793163552518325,52808422392537808896),F(318819628004877985013,26404211196268904448))
assert lo[0]==lo[1] and hi[0]==hi[1] and lo[2]>lo[3] and hi[2]>hi[3]
assert lo[2]+L*lo[0]+K*lo[1]==HD[0,0,0]
assert hi[2]+L*hi[0]+K*hi[1]==HD[0,0,0]
assert hi[0]-lo[0]==F(13860171875,12892681248178176)
assert (lo[2]-hi[2])/(hi[0]-lo[0])==F(88912,121)
print('PASS_STAGE150: 680 exact states; 1238 positive gaps; two cross-checked exact corner algorithms')
print('Ray',dK,dL,'first closure',t0,'new tie',R)
print('First-hit B,R',11,14662,'DFS visits',vis)
print('alpha150',hi[0],'V150',hi[2],'eta',hi[0]-lo[0],'slope',K+L)
