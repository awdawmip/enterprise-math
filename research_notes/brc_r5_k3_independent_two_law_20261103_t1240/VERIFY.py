#!/usr/bin/env python3
"""R5 K3 independent-law threshold gaps; exact 4-observer enumeration."""
from fractions import Fraction as F
from itertools import product
Z=F(0); O=F(1); c=F(2,3)
a=(F(1,2),F(2,3),F(1,2),F(3,4))
wstar=(F(1,8),F(1,6),F(1,16),F(3,32))
FUP=[tuple(map(F,t)) for t in ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))]
LUP=[(F(x),F(y),F((1-x)*y)) for x,y in product(range(2),repeat=2)]
S=((Z,Z,Z),(O,Z,Z),(O,O,Z),(O,O,O))
count=0
def ck(b,tag):
 global count
 count+=1
 if not b: raise AssertionError(tag)
def obs(u,ss,r,v):
 x,y,i=u; d=y/16+3*i/32
 w=(F(1,4),(1-x)/4,y/8,i/8)
 m=[w[k]*a[k]*ss[k][0] for k in range(4)]
 s=[c*m[k]*ss[k][1] for k in range(4)]
 h=[s[k]*ss[k][2] for k in range(4)]
 return (F(107,128)-21*x/128+d/4-sum(s,Z)/2,
         F(13,64)+3*x/64-d/2+sum(s,Z)/8,
         3+sum(m,Z)+F(3,2)*sum(s,Z)+sum((r[k]*h[k] for k in range(4)),Z),
         3+sum(m,Z)/2+F(3,8)*sum(s,Z)+sum((v[k]*h[k]/4 for k in range(4)),Z))
def dot(n,z): return sum((n[k]*z[k] for k in range(4)),Z)
def verify(name,r,v,kind,t):
 values=r if kind=='r' else v
 n=(-F(16),-F(76)-8*t,O,Z) if kind=='r' else (-F(16),-F(70)-4*t,Z,F(2))
 k=O if kind=='r' else F(1,2)
 P=sum((wstar[s]*max(Z,values[s]-t) for s in range(4)),Z)
 N=sum((wstar[s]*max(Z,t-values[s]) for s in range(4)),Z)
 expected=2*k*min(P,N)/3
 hf=max(dot(n,obs(u,ss,r,v)) for u in FUP for ss in product(S,repeat=4))
 hl=max(dot(n,obs(u,(ss,)*4,r,v)) for u in LUP for ss in S)
 ck(hf-hl==expected,name+' gap')
 if expected:
  gates=tuple((O,O,O) if values[s]>t else (O,Z,Z) for s in range(4))
  W=obs((Z,O,O),gates,r,v)
  ck(dot(n,W)==hf,name+' witness')
  sep=expected/sum(map(abs,n),Z)
  ck(sep>0,name+' distance')
  print(name,'gap',expected,'W',','.join(map(str,W)),'dist_inf_at_least',sep)
 else: print(name,'zero')
def main():
 uniform=(F(1,2),)*4
 spread=(F(1,4),F(1,2),F(3,4),F(1,2))
 alt=(F(1,6),F(2,3),F(3,5),F(1,3))
 verify('r-only',spread,uniform,'r',F(1,2))
 verify('v-only',uniform,spread,'v',F(1,2))
 verify('both-r',alt,spread,'r',F(1,3))
 verify('both-v',alt,spread,'v',F(1,2))
 verify('uniform-r',uniform,uniform,'r',F(1,3))
 verify('uniform-v',uniform,uniform,'v',F(2,3))
 for kind in ('r','v'):
  for t in (F(1,5),F(2,5),F(3,5),F(4,5)):
   verify(kind+'-'+str(t),spread if kind=='r' else uniform,
          uniform if kind=='r' else spread,kind,t)
 print('PASS_EXACT_R5_K3_INDEPENDENT_TWO_LAW_RIGIDITY',count,'cases',14,
       'FULL deterministic 1536','LR deterministic 16')
if __name__=='__main__':main()
