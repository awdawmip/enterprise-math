#!/usr/bin/env python3
"""Separate author checker: top-down Bellman + exact ordered-word traversal, iid N14 Stage106."""
from fractions import Fraction as R
from functools import lru_cache
p=(R(1,8),R(1,24),R(5,6));q=(R(1,12),R(1,12),R(5,6))
K=R(107892,101);L=72+R(8,9)*K
A=(11,5,4);B=(12,0,1)
a0=R(38038153259411651,109561042308169728);a1=R(646648605512624167,1862537719238885376)
v0=R(353483207227801957,27390260577042432);v1=R(6009214469256084569,465634429809721344)
s0=R(241563037007287,307200000000000)
s1=R(4106591957559179,5222400000000000)
def kid(n,a,b,j): return n+1,a+(j==0),b+(j==1)
@lru_cache(None)
def value(n,a,b):
 opts=[('P',K*R(2**(a+b),3**a)),('Q',L)]
 if n<14:opts.append(('C',1+sum((p[j]*value(*kid(n,a,b,j))[0] for j in range(3)),R(0))))
 m=min(v for _,v in opts)
 return m,tuple(x for x,v in opts if v==m)
assert { (n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(value(n,a,b)[1])>1 }=={A,B}
assert set(value(*A)[1])=={'Q','C'} and set(value(*B)[1])=={'Q','C'}
def act(n,a,b):
 if (n,a,b) in (A,B):return 'Q'
 return value(n,a,b)[1][0]
# Full ordered first-hit traversal, retaining prefix multiplicity and each P/Q probability.
hits={A:[0,R(),R()],B:[0,R(),R()]}
def first(n,a,b,pp,qq):
 state=n,a,b
 if state in hits:
  hits[state][0]+=1;hits[state][1]+=pp;hits[state][2]+=qq;return
 if act(n,a,b)!='C':return
 for j in range(3):first(*kid(n,a,b,j),pp*p[j],qq*q[j])
first(0,0,0,R(1),R(1))
assert hits[A]==[2258,R(28225,195689447424),R(28225,92876046336)],hits
assert hits[B]==[12,R(48828125,725594112),R(48828125,362797056)]

def forced(z):
 n0,a0,b0=z
 totals=[R()]*4;num=[0]
 def recurse(n,a,b,pp,qq):
  a0=act(n,a,b)
  if a0=='C':
   for j in range(3):recurse(*kid(n,a,b,j),pp*p[j],qq*q[j])
  else:
   if a0=='P':totals[1]+=qq
   else:totals[0]+=pp
   totals[2]+=pp*(n-n0);totals[3]+=qq*(n-n0);num[0]+=1
 for j in range(3):recurse(*kid(*z,j),p[j],q[j])
 return tuple(totals)+(num[0],)
assert forced(A)==(R(1493,1536),R(7,576),R(239,192),R(167,144),9)
assert forced(B)==(R(63,64),R(1,144),R(9,8),R(13,12),5)

def evaluate(u,s):
 total=[R()]*4;visited=[0];terminal=[0]
 def rec(n,a,b,pp,qq):
  visited[0]+=1
  z=n,a,b
  if z==A:
   w=1-u
   total[0]+=pp*w;total[2]+=pp*w*n;total[3]+=qq*w*n
   pp*=u;qq*=u;zact='C'
  elif z==B:
   total[0]+=pp*s;total[2]+=pp*s*n;total[3]+=qq*s*n
   pp*=1-s;qq*=1-s;zact='C'
  else:zact=act(n,a,b)
  if pp==0 and qq==0:return
  if zact=='C':
   for j in range(3):rec(*kid(n,a,b,j),pp*p[j],qq*q[j])
  else:
   if zact=='P':total[1]+=qq
   else:total[0]+=pp
   total[2]+=pp*n;total[3]+=qq*n;terminal[0]+=1
 rec(0,0,0,R(1),R(1))
 return tuple(total),visited[0],terminal[0]
for u,s,alpha,v in [(R(),s0,a0,v0),(R(1),s1,a1,v1),(R(1,2),(s0+s1)/2,(a0+a1)/2,(v0+v1)/2)]:
 out,nodes,terms=evaluate(u,s)
 assert out[0]==out[1]==alpha and out[2]==v and out[2]>out[3],(u,out,alpha,v)
 print('PASS u=',u,'ordered_nodes=',nodes,'terminal_words=',terms,'alpha=',alpha,'tP=',out[2],'tQ=',out[3])
print('PASS_INDEPENDENT_ORDERED_STAGE106')
