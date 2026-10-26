#!/usr/bin/env python3
"""Exact Stage171 *dual-only* scan following Stage170, without primal claim."""
from fractions import Fraction as F
from functools import lru_cache
N=14
P=(F(1,8),F(1,24),F(5,6));K=F(4773735,18929);L=F(14183320,56787)
dK=-F(1);dL=-F(10592,12501)
R=(10,0,1);T=(12,5,2);Z=(12,4,3)
def c(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def val(s):
 o=[K*lr(s),L]
 if s[0]<N:o.append(1+sum(P[i]*val(c(s,i))[0] for i in range(3)))
 return min(o),o
@lru_cache(None)
def der(s):
 v,o=val(s);w=[i for i,x in enumerate(o) if x==v]
 ix=1 if s==R else 0 if s==T else w[0]
 assert len(w)==1 or s in (R,T)
 do=[dK*lr(s),dL]
 if s[0]<N:do.append(sum(P[i]*der(c(s,i))[0] for i in range(3)))
 return do[ix],do
cross=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,o=val(s);dv,do=der(s)
   for i in range(len(o)):
    gap=o[i]-v;dg=do[i]-dv
    if gap==0:assert dg>=0,(s,i,dg)
    elif dg<0:cross.append((gap/-dg,s,i))
ct,s,ix=min(cross)
assert (s,ix)==(Z,1)
assert ct==F(128035242,28942441)
kn=K+dK*ct;ln=L+dL*ct
assert kn==F(378837,1529) and ln==F(1128472,4587)
@lru_cache(None)
def chk(s):
 o=[kn*lr(s),ln]
 if s[0]<N:o.append(1+sum(P[i]*chk(c(s,i))[0] for i in range(3)))
 return min(o),o
ties={};pos=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,o=chk(s);w=[i for i,x in enumerate(o) if x==v]
   if len(w)>1:ties[s]=tuple('PQC'[i] for i in w)
   pos.extend(x-v for x in o if x>v)
assert ties=={R:('Q','C'),Z:('Q','C')}
assert len(pos)==1238 and min(pos)==F(3442966771823,94671649898496)
assert chk((0,0,0))[0]==F(332293501648867121767,1807757198084800512)
print('PASS Stage171 DUAL ONLY; closure',ct,'K',kn,'L',ln,'slope',kn+ln)
print('PASS 680 states, 1238 positive gaps, two ties',ties)
print('PASS min gap',min(pos),'root',chk((0,0,0))[0])
print('UNPROVED: Stage171 primal real interval / right endpoint')
