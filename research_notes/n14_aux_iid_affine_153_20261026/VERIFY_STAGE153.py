"""Stage153 author-level exact finite N14 ordered-history verifier."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K,L=F(5994,17),F(5960,17);B,Z=(11,0,1),(12,2,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680
def child(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
H={};A={};ties=[];gaps=[]
for s in reversed(S):
 costs={'P':K*lr(s),'Q':L}
 if s[0]<N:costs['C']=1+sum((P[i]*H[child(s)[i]] for i in range(3)),F())
 m=min(costs.values());opt=tuple(a for a in costs if costs[a]==m)
 if len(opt)>1:ties.append((s,opt))
 A[s]='Q' if s in (B,Z) else opt[0]
 assert A[s] in opt
 H[s]=m;gaps.extend(v-m for v in costs.values() if v>m)
assert set(ties)=={(B,('Q','C')),(Z,('Q','C'))}
assert len(gaps)==1238 and min(gaps)==F(71917,33841152)
assert H[0,0,0]==F(79691642847444362851,310422953206480896)
def act(s,b,z):
 if s==B:return 'Q' if b else 'C'
 if s==Z:return 'Q' if z else 'C'
 return A[s]
def backward(b,z):
 T={}
 for s in reversed(S):
  op=act(s,b,z)
  if op=='Q':v=(F(1),F(),F(),F())
  elif op=='P':v=(F(),F(1),F(),F())
  else:
   assert s[0]<N
   ch=child(s)
   v=tuple((F(1) if j>=2 else F())+sum(((P if j%2==0 else Q)[i]*T[ch[i]][j] for i in range(3)),F()) for j in range(4))
  T[s]=v
 return T[0,0,0]
def dfs(b,z):
 sums=[0]*4;hits=defaultdict(lambda:[0,F(),F()]);count=0
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,c,p,q=stack.pop();count+=1;s=(n,a,c)
  if s in (B,Z):
   hits[s][0]+=1;hits[s][1]+=F(p,24**n);hits[s][2]+=F(q,12**n)
  op=act(s,b,z)
  if op=='C':
   assert n<N
   stack.extend(((n+1,a+1,c,3*p,q),(n+1,a,c+1,p,q),(n+1,a,c,20*p,10*q)))
  else:
   x=p*24**(N-n);y=q*12**(N-n)
   if op=='Q':sums[0]+=x
   else:sums[1]+=y
   sums[2]+=n*x;sums[3]+=n*y
 return tuple(F(sums[j],(24 if j%2==0 else 12)**N) for j in range(4)),count,hits
corners={};vis=[];first_hit={}
for b,z in product((0,1),repeat=2):
 v,n,h=dfs(b,z);assert v==backward(b,z)
 corners[b,z]=v;vis.append([b,z,n])
 first_hit[f'{b}{z}']={str(s):[str(x) for x in h[s]] for s in (B,Z)}
assert all(q==first_hit['00'] for q in first_hit.values())
assert first_hit['00'][str(B)]==['11','107421875/1451188224','107421875/725594112']
assert first_hit['00'][str(Z)]==['1555','607421875/61917364224','607421875/34828517376']
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
M=corners[0,0];dB=sub(corners[1,0],M);dZ=sub(corners[0,1],M)
assert sub(sub(corners[1,1],corners[1,0]),dZ)==(F(),)*4
b0=(M[1]-M[0])/(dB[0]-dB[1])
db=-(dZ[0]-dZ[1])/(dB[0]-dB[1])
assert b0==F(2686983670724537,2714624000000000) and db==-F(9019,127248)
assert 0<b0<1 and 0<b0+db<1
def obs(z):return add(add(M,tuple((b0+db*z)*x for x in dB)),tuple(z*x for x in dZ))
v0,v1=obs(F()),obs(F(1))
a0=F(18373003413933759925,52808422392537808896)
a1=F(18373341781933759925,52808422392537808896)
t0=F(318745538371909741813,26404211196268904448)
t1=F(318626572163909741813,26404211196268904448)
for v,a,t in ((v0,a0,t0),(v1,a1,t1)):
 assert v[0]==v[1]==a and v[2]==t and v[2]>v[3]
 assert v[2]+K*v[1]+L*v[0]==H[0,0,0]
assert (a1-a0)==F(10326171875,1611585156022272)
assert (t0-t1)/(a1-a0)==K+L==F(11954,17)
rec={'status':'AUTHOR_EXACT_NOT_ADMITTED','dual':{'K':str(K),'L':str(L),'Hroot':str(H[0,0,0])},
 'ties':[[list(s),list(v)] for s,v in ties],'strict_gaps':len(gaps),
 'min_gap':str(min(gaps)),'dfs_visits':vis,'first_hit':first_hit,
 'corners':{f'{b}{z}':[str(x) for x in v] for (b,z),v in corners.items()},
 'M00':[str(x) for x in M],'dB':[str(x) for x in dB],'dZ':[str(x) for x in dZ],
 'b0':str(b0),'db_dz':str(db),
 'left':{'alpha':str(a0),'tP':str(t0),'tQ':str(v0[3])},
 'right':{'alpha':str(a1),'tP':str(t1),'tQ':str(v1[3])},
 'delta':str(a1-a0),'slope':str(K+L)}
Path(__file__).with_name('certificate153.replayed.json').write_text(json.dumps(rec,indent=2)+'\n')
print('PASS Stage153 full real interval; all exact checks passed; first-hits',first_hit['00'])
