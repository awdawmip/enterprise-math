#!/usr/bin/env python3
"""Author cross-check: top-down exact Bellman and literal ordered-path DFS for Stage107."""
from fractions import Fraction as R
from functools import lru_cache
p=(R(1,8),R(1,24),R(5,6));q=(R(1,12),R(1,12),R(5,6))
K=R(778896,767);L=72+R(8,9)*K;A=(10,3,0);B=(12,0,1)
alpha0=R(646648605512624167,1862537719238885376)
V0=R(6009214469256084569,465634429809721344)
s0=R(4106591957559179,5222400000000000)
c=R(38521,136000)
u1=R(1115808042440821,1479206400000000)
eta=R(299609375,6315571150848)
def nxt(n,a,b,j):return n+1,a+(j==0),b+(j==1)
@lru_cache(None)
def dual(n,a,b):
 z=(n,a,b); opts=[('P',K*R(2**(a+b),3**a)),('Q',L)]
 if n<14:opts.append(('C',1+sum((p[j]*dual(*nxt(n,a,b,j))[0] for j in range(3)),R())))
 best=min(v for _,v in opts)
 return best,tuple(act for act,val in opts if val==best)
def policy(z):
 if z==A:return 'C'
 if z==B:return 'Q'
 return dual(*z)[1][0]
assert {(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(dual(n,a,b)[1])>1}=={A,B}
# Real first-hit paths, with P and Q likelihoods *and* their multiplicity.
hits={A:[0,R(),R()],B:[0,R(),R()]}
def first(n,a,b,pp,qq):
 z=(n,a,b)
 if z in hits:
  hits[z][0]+=1; hits[z][1]+=pp;hits[z][2]+=qq;return
 if policy(z)!='C':return
 for j in range(3):first(*nxt(n,a,b,j),pp*p[j],qq*q[j])
first(0,0,0,R(1),R(1))
assert hits[A]==[120,R(390625,5971968),R(390625,20155392)]
assert hits[B]==[12,R(48828125,725594112),R(48828125,362797056)]

def forced(z):
 n0=z[0]; total=[R() for _ in range(4)]; paths=[0]
 def visit(n,a,b,pp,qq):
  act=policy((n,a,b))
  if act=='C':
   for j in range(3):visit(*nxt(n,a,b,j),pp*p[j],qq*q[j])
  else:
   if act=='P':total[1]+=qq
   if act=='Q':total[0]+=pp
   total[2]+=pp*(n-n0);total[3]+=qq*(n-n0);paths[0]+=1
 for j in range(3):visit(*nxt(*z,j),p[j],q[j])
 return tuple(total)+(paths[0],)
assert forced(A)==(R(635,165888),R(10201,10368),R(7711,6912),R(1069,864),21)
assert forced(B)==(R(63,64),R(1,144),R(9,8),R(13,12),5)

def evaluate(u,s):
 result=[R() for _ in range(4)]; counts=[0,0]
 def visit(n,a,b,pp,qq):
  counts[0]+=1;z=(n,a,b)
  if z==A:
   result[1]+=qq*u;result[2]+=pp*u*n;result[3]+=qq*u*n
   pp*=1-u;qq*=1-u;act='C'
  elif z==B:
   result[0]+=pp*s;result[2]+=pp*s*n;result[3]+=qq*s*n
   pp*=1-s;qq*=1-s;act='C'
  else:act=policy(z)
  if pp==0 and qq==0:return
  if act=='C':
   for j in range(3):visit(*nxt(n,a,b,j),pp*p[j],qq*q[j])
  else:
   if act=='P':result[1]+=qq
   if act=='Q':result[0]+=pp
   result[2]+=pp*n;result[3]+=qq*n;counts[1]+=1
 visit(0,0,0,R(1),R(1))
 return tuple(result),tuple(counts)
for u in (R(0),u1/2,u1):
 s=s0+c*u
 out,counts=evaluate(u,s)
 alpha=alpha0+eta*u
 assert out[0]==out[1]==alpha,(u,out,alpha)
 assert out[2]==V0-(K+L)*eta*u,(u,out)
 assert out[2]>out[3]
 print('PASS_DFS u=',u,'s=',s,'visited=',counts[0],'terminal=',counts[1],'alpha=',alpha,'tP=',out[2])
print('PASS_INDEPENDENT_ORDERED_STAGE107')
