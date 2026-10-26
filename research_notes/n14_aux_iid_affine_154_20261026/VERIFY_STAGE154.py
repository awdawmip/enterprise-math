"""Stage154 N14 auxiliary complete-real author verifier, Python stdlib only."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import json
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K,L=F(68426856,199229),F(68268104,199229)
B,U=(11,0,1),(10,5,4)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680
def child(s):
 n,a,b=s;return((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
H={};A={};ties=[];gaps=[]
for s in reversed(S):
 v={'P':K*lr(s),'Q':L}
 if s[0]<N:v['C']=1+sum((P[i]*H[child(s)[i]] for i in range(3)),F())
 m=min(v.values());opt=tuple(a for a in v if v[a]==m)
 if len(opt)>1:ties.append((s,opt))
 A[s]='Q' if s in (B,U) else opt[0]
 assert A[s] in opt
 H[s]=m;gaps.extend(x-m for x in v.values() if x>m)
assert set(ties)=={(B,('Q','C')),(U,('Q','C'))}
assert len(gaps)==1238 and min(gaps)==F(4439,398458)
assert H[0,0,0]==F(1824690544010408840595299,7275912299338115579904)
def act(s,b,u):
 if s==B:return 'Q' if b else 'C'
 if s==U:return 'Q' if u else 'C'
 return A[s]
def backward(b,u):
 V={}
 for s in reversed(S):
  op=act(s,b,u)
  if op=='Q':v=(F(1),F(),F(),F())
  elif op=='P':v=(F(),F(1),F(),F())
  else:
   assert s[0]<N
   ch=child(s)
   v=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*V[ch[i]][j] for i in range(3)),F()) for j in range(4))
  V[s]=v
 return V[0,0,0]
def literal(b,u):
 out=[0]*4;hits=defaultdict(lambda:[0,F(),F()]);nvisit=0
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,c,p,q=stack.pop();nvisit+=1;s=(n,a,c)
  if s in (B,U):
   hits[s][0]+=1;hits[s][1]+=F(p,24**n);hits[s][2]+=F(q,12**n)
  op=act(s,b,u)
  if op=='C':
   assert n<N
   stack.extend(((n+1,a+1,c,3*p,q),(n+1,a,c+1,p,q),(n+1,a,c,20*p,10*q)))
  else:
   x=p*24**(N-n);y=q*12**(N-n)
   if op=='Q':out[0]+=x
   else:out[1]+=y
   out[2]+=n*x;out[3]+=n*y
 return tuple(F(out[j],(24 if j%2==0 else 12)**N) for j in range(4)),nvisit,hits
corners={};vis=[];hit={}
for b,u in product((0,1),repeat=2):
 v,n,h=literal(b,u)
 assert v==backward(b,u)
 corners[b,u]=v;vis.append([b,u,n])
 hit[f'{b}{u}']={str(s):[str(x) for x in h[s]] for s in (B,U)}
assert all(x==hit['00'] for x in hit.values())
assert hit['00'][str(B)]==['11','107421875/1451188224','107421875/725594112']
assert hit['00'][str(U)]==['300','125/5435817984','125/2579890176']
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
M=corners[0,0];dB=sub(corners[1,0],M);dU=sub(corners[0,1],M)
assert sub(sub(corners[1,1],corners[1,0]),dU)==(F(),)*4
b0=(M[1]-M[0])/(dB[0]-dB[1])
db=-(dU[0]-dU[1])/(dB[0]-dB[1])
assert b0==F(7483738461750611,8143872000000000)
assert db==-F(1149859,2714624000000) and 0<b0+db<b0<1
def obs(u):return add(add(M,tuple((b0+db*u)*x for x in dB)),tuple(u*x for x in dU))
right,left=obs(F()),obs(F(1))
a153=F(18373341781933759925,52808422392537808896)
v153=F(318626572163909741813,26404211196268904448)
a154=F(18373341782531446925,52808422392537808896)
v154=F(318626571958867301813,26404211196268904448)
for v,a,t in ((left,a153,v153),(right,a154,v154)):
 assert v[0]==v[1]==a and v[2]==t and v[2]>v[3]
 assert v[2]+K*v[1]+L*v[0]==H[0,0,0]
assert a154-a153==F(24903625,2200350933022408704)
assert (v153-v154)/(a154-a153)==K+L==F(136694960,199229)
rec={'status':'AUTHOR_EXACT_EXTERNAL_NOT_ADMITTED','dual':{'K':str(K),'L':str(L),'Hroot':str(H[0,0,0])},
 'ties':[[list(s),list(actions)] for s,actions in ties],
 'strict_gaps':len(gaps),'min_gap':str(min(gaps)),'dfs_visits':vis,'first_hit':hit,
 'corners':{f'{b}{u}':[str(x) for x in v] for (b,u),v in corners.items()},
 'b0':str(b0),'db_du':str(db),
 'left':{'alpha':str(a153),'tP':str(v153),'tQ':str(left[3])},
 'right':{'alpha':str(a154),'tP':str(v154),'tQ':str(right[3])},
 'alpha_increment':str(a154-a153),'slope':str(K+L)}
Path(__file__).with_name('certificate154.replayed.json').write_text(json.dumps(rec,indent=2)+'\n')
print('PASS Stage154 exact full real interval; 680 Bellman states and 4 corners dual-checked')
