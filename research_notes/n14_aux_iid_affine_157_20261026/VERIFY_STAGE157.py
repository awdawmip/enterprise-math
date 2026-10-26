"""Stage157: finite external N14 iid exact-rational author reproduction."""
from fractions import Fraction as F
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(3342600,10529);OLD=F(109612440,326191)
J=(10,2,0);T=(14,0,0);Z=F(0)
def states():
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):yield n,a,b
def kids(s):
 n,a,b=s;return (n+1,a+1,b),(n+1,a,b+1),(n+1,a,b)
def bell(k):
 h={};pol={};ties={};gaps=[]
 for s in states():
  d={'P':k*F(2,3)**s[1]*2**s[2],'Q':k}
  if s[0]<N:d['C']=1+sum(p*h[c] for p,c in zip(P,kids(s)))
  m=min(d.values());w=[key for key,v in d.items() if v==m]
  h[s]=m;pol[s]=w[0]
  if len(w)>1:ties[s]=w
  gaps.extend(v-m for v in d.values() if v>m)
 return h,pol,ties,gaps
H,pol,ties,gaps=bell(K)
assert len(list(states()))==680 and len(gaps)==1238
assert set(ties)=={J,T} and set(ties[J])=={'P','C'} and set(ties[T])=={'P','Q'}
assert min(gaps)==F(232231247,11789784576)
assert H[(0,0,0)]==F(16797051003483763023587,72098013403919941632)
H0,p0,t0,g0=bell(OLD);hm,pm,tm,gm=bell((OLD+K)/2)
assert set(tm)=={T}
assert all((pm[s]==p0[s] or pm[s] in t0.get(s,[]))
           and (pm[s]==pol[s] or pm[s] in ties.get(s,[])) for s in pm)
def choice(s,j,x):
 if s==J:return 'P' if j else 'C'
 if s==T:return 'P' if x else 'Q'
 return pol[s]
def dag(j,x):
 D={}
 for s in states():
  a=choice(s,j,x)
  if a=='P':v=(Z,F(1),Z,Z)
  elif a=='Q':v=(F(1),Z,Z,Z)
  else:
   c=[D[y] for y in kids(s)]
   v=(sum(p*z[0] for p,z in zip(P,c)),sum(q*z[1] for q,z in zip(Q,c)),
      1+sum(p*z[2] for p,z in zip(P,c)),1+sum(q*z[3] for q,z in zip(Q,c)))
  D[s]=v
 return D[(0,0,0)]
def ordered(j,x):
 sums=[0]*4;meta=[0,0]
 def rec(n,a,b,wp,wq):
  meta[0]+=1;d=choice((n,a,b),j,x)
  if d=='C':
   assert n<N
   rec(n+1,a+1,b,wp*3,wq)
   rec(n+1,a,b+1,wp,wq)
   rec(n+1,a,b,wp*20,wq*10)
  else:
   meta[1]+=1;ip=wp*24**(N-n);iq=wq*12**(N-n)
   if d=='Q':sums[0]+=ip
   if d=='P':sums[1]+=iq
   sums[2]+=n*ip;sums[3]+=n*iq
 rec(0,0,0,1,1)
 return (F(sums[0],24**N),F(sums[1],12**N),F(sums[2],24**N),F(sums[3],12**N)),meta
def hit_counts():
 hits={J:[0,0,0],T:[0,0,0]}
 def rec(n,a,b,wp,wq):
  s=(n,a,b)
  if s in hits:
   hits[s][0]+=1;hits[s][1]+=wp*24**(N-n);hits[s][2]+=wq*12**(N-n);return
  if pol[s]!='C':return
  rec(n+1,a+1,b,wp*3,wq)
  rec(n+1,a,b+1,wp,wq)
  rec(n+1,a,b,wp*20,wq*10)
 rec(0,0,0,1,1)
 return {s:(n,F(p,24**N),F(q,12**N)) for s,(n,p,q) in hits.items()}
assert hit_counts()[J]==(45,F(1953125,11943936),F(1953125,26873856))
assert hit_counts()[T]==(1,F(6103515625,78364164096),F(6103515625,78364164096))
V={}
for j in (0,1):
 for x in (0,1):
  z=dag(j,x);o,meta=ordered(j,x);assert z==o
  V[j,x]=z
sub=lambda a,b:tuple(i-k for i,k in zip(a,b))
add=lambda a,b:tuple(i+k for i,k in zip(a,b))
scale=lambda a,k:tuple(i*k for i in a)
base=V[0,0];dJ=sub(V[1,0],base);dT=sub(V[0,1],base)
assert add(sub(V[1,1],V[1,0]),sub(V[0,0],V[0,1]))==(Z,Z,Z,Z)
x0=(base[0]-base[1])/(dT[1]-dT[0])
grad=(dJ[0]-dJ[1])/(dT[1]-dT[0]);jstar=-x0/grad
assert x0==F(660136987826389,327680000000000000)
assert grad==-F(360279,25600000)
assert jstar==F(660136987826389,4611571200000000)
assert 0<x0<1 and 0<jstar<1
def at(j):return add(add(base,scale(dJ,j)),scale(dT,x0+grad*j))
v0=at(Z);v1=at(jstar)
alpha0=F(7319074368089652265,21035720123168587776)
alpha1=F(763084945158127578305,2192919042319171190784)
value0=F(5285134543382516317,438244169232678912)
value1=F(3298586218925748578843,274114880289896398848)
assert v0[0]==v0[1]==alpha0 and v0[2]==value0
assert v1[0]==v1[1]==alpha1 and v1[2]==value1
assert v0[2]>v0[3] and v1[2]>v1[3]
assert v0[2]+K*(v0[0]+v0[1])==H[(0,0,0)]
assert v1[2]+K*(v1[0]+v1[1])==H[(0,0,0)]
assert alpha1-alpha0==F(34752911724120248905,842080912250561737261056)
print('PASS',len(list(states())),'states',len(gaps),'positive gaps',hit_counts())
print('Stage157 alpha',alpha1,'value',value1,'width',alpha1-alpha0,'slope',2*K)
