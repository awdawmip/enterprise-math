"""Author-side exact verification of the lawful finite BRC P/Q noisy-S2 observer theorem."""
from fractions import Fraction as F
from itertools import product

q={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
   'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
YS=('B3','B4P0','B4Q0','B4P1','B4Q1')
def add(d,key,x):d[key]=d.get(key,F(0))+x
def tv(a,b):return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in a.keys()|b.keys()),F(0))/2
def leaves(law):
 d={(s,j,k):q[s]*(r[s][j] if law=='P' else 1)/4 for s in q for j,k in product((0,1),repeat=2)}
 assert len(d)==16 and all(x>0 for x in d.values()) and sum(d.values())==1
 return d
def kernel(u,v,ds):
 ans=[]
 for j,rate in enumerate((u,v)):
  d={'B3':1-rate}
  for k in (0,1):
   d[f'B4P{k}']=rate*ds[2*j+k]/2
   d[f'B4Q{k}']=rate*(1-ds[2*j+k])/2
  assert sum(d.values())==1 and all(x>=0 for x in d.values())
  ans.append(d)
 return ans
def actual(law,eps,u,v,ds):
 out={}
 for (s,j,k),m in leaves(law).items():
  if s in ('AV','BV'):add(out,('E',None,'E'),m)
  elif s=='AU':add(out,('A',None,'A'),m)
  else:
   rate=(u,v)[j];d=ds[2*j+k]
   for z,n in ((j,1-eps),(1-j,eps)):
    add(out,('B',z,'B3'),m*n*(1-rate))
    add(out,('B',z,f'B4P{k}'),m*n*rate*d)
    add(out,('B',z,f'B4Q{k}'),m*n*rate*(1-d))
 assert sum(out.values())==1
 return out
def observed(law):
 out={}
 for (c,z,y),m in law.items():add(out,(c,z),m)
 return out
def marginal(law):
 out={}
 for (c,z,y),m in law.items():add(out,(c,y),m)
 return out
def decoded(law,f0,f1,a,b):
 out={}
 for (c,z),m in observed(law).items():
  if c!='B':add(out,(c,z,c),m)
  else:
   t=a if z==0 else b
   for y in YS:add(out,(c,z,y),m*(t*f0[y]+(1-t)*f1[y]))
 assert sum(out.values())==1
 return out
def scalars(eps):
 p=F(1,10);a=p+(1-2*p)*eps;b=1-a
 ej=(1-2*p)*eps*(1-eps)/(b*(1+2*a))
 beta=p*eps/b;alpha=1-beta-2*ej
 assert 0<=alpha<=1 and 0<=beta<=1
 return ej,alpha,beta
def delta(u,v,ds):
 return (2*abs(u-v)+sum((abs(v*ds[2+k]-u*ds[k])+abs(v*(1-ds[2+k])-u*(1-ds[k])) for k in (0,1)),F(0)))/4
def signed(eps,f0,f1):
 return sum((abs(eps*f1[y]-(1-eps)*f0[y])+abs((1-eps)*f1[y]-eps*f0[y]) for y in YS),F(0))/20
assert sum(m for (s,j,k),m in leaves('P').items() if s=='BU' and j==0)==F(1,40)
assert sum(m for (s,j,k),m in leaves('Q').items() if s=='BU' and j==0)==F(1,8)
rates=(F(0),F(1,4),F(1,2),F(3,4),F(1))
decisions=((F(0),)*4,(F(1),)*4,(F(1),F(0),F(0),F(1)),
           (F(0),F(1),F(1),F(0)),(F(1,2),)*4,(F(0),F(0),F(1),F(1)))
levels=(F(0),F(1,10),F(1,4),F(2,5),F(1,2))
n=0
for u,v in product(rates,repeat=2):
 for ds in decisions:
  f0,f1=kernel(u,v,ds);D=tv(f0,f1)
  assert D==delta(u,v,ds)
  for eps in levels:
   P=actual('P',eps,u,v,ds);Q=actual('Q',eps,u,v,ds)
   ej,a,b=scalars(eps)
   assert tv(P,decoded(P,f0,f1,a,b))==D*ej/4
   assert tv(Q,decoded(Q,f0,f1,a,b))==D*ej/4
   assert tv(marginal(P),marginal(Q))==D/10
   assert tv(P,Q)==signed(eps,f0,f1)
   n+=1
assert n==750
print('PASS: both normalized strictly-positive 16-leaf laws; 750 exact policy/sensor cases')
eps=F(1,4);ds=(F(0),)*4
u=F(1,4);v=F(3,4);f0,f1=kernel(u,v,ds);D=tv(f0,f1)
P=actual('P',eps,u,v,ds);Q=actual('Q',eps,u,v,ds)
assert D==F(1,2)
K0={y:((1-eps)*f0[y]-eps*f1[y])/(1-2*eps) for y in YS}
K1={y:((1-eps)*f1[y]-eps*f0[y])/(1-2*eps) for y in YS}
assert min(list(K0.values())+list(K1.values()))>=0 and sum(K0.values())==sum(K1.values())==1
assert K0['B3']==1 and K1['B3']==0 and K1['B4Q0']==K1['B4Q1']==F(1,2)
# Extrapolation theta0=3/2,theta1=-1/2 gives valid K0,K1, not valid latent-J probabilities.
PM=decoded(P,f0,f1,F(3,2),-F(1,2));QM=decoded(Q,f0,f1,F(3,2),-F(1,2))
assert tv(marginal(P),marginal(PM))==tv(marginal(Q),marginal(QM))==0
ej,a,b=scalars(eps)
assert D*ej/4==F(15,896)
assert tv(P,decoded(P,f0,f1,a,b))==tv(Q,decoded(Q,f0,f1,a,b))==F(15,896)
assert tv(P,Q)==tv(observed(P),observed(Q))==F(1,20)
print('EXACT S23: eps=1/4, u=1/4, v=3/4, all decisions Q; D=1/2')
print('Marginal radius=0; sharp joint radius=15/896; pairwise full TV=sensor TV=1/20')
f0b,f1b=kernel(F(0),F(1,2),ds)
P2=actual('P',eps,F(0),F(1,2),ds);Q2=actual('Q',eps,F(0),F(1,2),ds)
assert tv(f0b,f1b)==D and tv(P2,Q2)==F(1,16)
print('Same D=1/2 but different P/Q full-joint TV=1/16')
print('Universal claims: analytic Hahn projection, dual bound and coordinate inversion in PROOF.md')
