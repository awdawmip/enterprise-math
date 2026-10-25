#!/usr/bin/env python3
"""Exact global action-gap ray sweep from Stage107 B saturation to Stage108."""
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6))
Z=[(n,a,b) for n in range(14,-1,-1) for a in range(n+1) for b in range(n-a+1)]
A=(10,3,0);B=(12,0,1);C=(11,5,4)
K0,L0=F(778896,767),F(747576,767)
Dk,Dl=F(-635,165888),F(-167,34992)
def ch(z):
 n,a,b=z
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def rho(z):return F(2**(z[1]+z[2]),3**z[1])
def bell(k,l):
 d={};o={};c={}
 for z in Z:
  vv={'P':k*rho(z),'Q':l}
  if z[0]<14:vv['C']=1+sum((P[i]*d[v] for i,v in enumerate(ch(z))),F())
  d[z]=min(vv.values());o[z]=[a for a,v in vv.items() if v==d[z]];c[z]=vv
 return d,o,c
_,opt,_=bell(K0,L0)
assert {z for z in Z if len(opt[z])>1}=={A,B}
policy={z:('C' if z==A else 'Q' if z==B else opt[z][0]) for z in Z}
add=lambda a,b:tuple(a[i]+b[i] for i in range(3))
scale=lambda s,a:tuple(s*v for v in a)
sub=lambda a,b:tuple(a[i]-b[i] for i in range(3))
val=lambda a,k,l:a[0]+a[1]*k+a[2]*l
d={}; gaps={}
for z in Z:
 costs={'P':(F(),rho(z),F()),'Q':(F(),F(),F(1))}
 if z[0]<14:
  t=(F(1),F(),F())
  for i,y in enumerate(ch(z)):t=add(t,scale(P[i],d[y]))
  costs['C']=t
 d[z]=costs[policy[z]]
 gaps[z]={a:sub(v,d[z]) for a,v in costs.items()}
assert gaps[A]['P']==(F(-7711,6912),F(167,34992),F(-635,165888))
assert gaps[A]['P'][1]*Dk+gaps[A]['P'][2]*Dl==0
assert gaps[B]['C'][1]*Dk+gaps[B]['C'][2]*Dl==F(767,35831808)
candidate=[]
for z in Z:
 for act,g in gaps[z].items():
  old=val(g,K0,L0);der=g[1]*Dk+g[2]*Dl
  assert old>=0 and not (old==0 and der<0)
  if old>0 and der<0:candidate.append((old/(-der),z,act))
assert len(candidate)==853
h,z,action=min(candidate)
assert (h,z,action)==(F(42349837824,39613249),C,'Q')
k,l=K0+h*Dk,L0+h*Dl
assert (k,l)==(F(208946709,206588),F(50075544,51647))
d,opt,c=bell(k,l)
assert {z for z in Z if len(opt[z])>1}=={A,C}
assert sum(v>d[z] for z in Z for v in c[z].values())==1238
assert min(v-d[z] for z in Z for v in c[z].values() if v>d[z])==F(37821,1652704)
assert d[0,0,0]==F(495598934898928452760465,707312394011255242752)
print('PASS_STAGE108 FACE_SWEEP 853 crossings; first tie at C, all 680 states')
