"""Exact affine gap scanner Stage131 candidate only, keeping B Q/C tie, T fixed P."""
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6));N=14
K0=F(522693,802);L0=F(244736,401)
B=(11,0,1);T=(14,7,4)
def children(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def rat(s):
 n,a,b=s;return F(2**(a+b),3**a)
C={}; chosen={};offers={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);o={'P':(F(0),rat(s),F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    ch=children(s)
    o['C']=tuple((F(1) if j==0 else F(0))+sum(P[i]*C[ch[i]][j] for i in range(3)) for j in range(3))
   value=lambda v:v[0]+K0*v[1]+L0*v[2]
   best=min(value(v) for v in o.values())
   opts=[t for t,v in o.items() if value(v)==best]
   act='Q' if s==B else 'P' if s==T else opts[0]
   assert act in opts,(s,act,opts)
   C[s]=o[act];chosen[s]=act;offers[s]=o
m=offers[B]['C'][1]/(1-offers[B]['C'][2]);assert m==F(112,129)
G=[];openings=[];cnt=0
for s,o in offers.items():
 f=lambda v:v[0]+K0*v[1]+L0*v[2]
 d=lambda v:-v[1]-m*v[2]
 for op,v in o.items():
  if op==chosen[s]:continue
  gap=f(v)-f(C[s]);dg=d(v)-d(C[s]);assert gap>=0
  if gap==0:
   assert s in (B,T)
   openings.append((s,op,dg))
  else:
   cnt+=1
   if dg<0:G.append((gap/(-dg),s,chosen[s],op,gap,dg))
assert cnt==1238 and len(openings)==2
print('m',m,'openings',openings,'positive candidates',len(G))
for t in sorted(G)[:5]:print('CANDIDATE',t)
t,s,old,new,*_=min(G)
K1=K0-t;L1=L0-m*t
print('FIRST',t,'at',s,old,new,'K131',K1,'L131',L1)
H={};ties={};positive=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   state=(n,a,b);cc={'P':K1*rat(state),'Q':L1}
   if n<N:cc['C']=1+sum(P[i]*H[ch] for i,ch in enumerate(children(state)))
   best=min(cc.values());H[state]=best;opts=[op for op,v in cc.items() if v==best]
   if len(opts)>1:ties[state]=opts
   positive.extend(v-best for v in cc.values() if v>best)
print('ties',ties,'strict',len(positive),'minimum positive',min(positive),'root',H[(0,0,0)])
print('PASS STAGE131 DUAL CANDIDATE')
