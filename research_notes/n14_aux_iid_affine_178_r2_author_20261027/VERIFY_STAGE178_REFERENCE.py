#!/usr/bin/env python3
"""Reference exact rational Stage178 dual + primal verifier; external N14 only.
Full independently executed DFS and stdout reside in the portable research package.
"""
from fractions import Fraction as F
from functools import lru_cache
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(64228036011,290873926);L=F(93785824168,436310889)
T=(8,2,0);S=(9,0,1)
def child(x,i):return(x[0]+1,x[1]+(i==0),x[2]+(i==1))
def ell(x):return F(2)**(x[1]+x[2])/F(3)**x[1]
@lru_cache(None)
def bell(x):
 v=[K*ell(x),L]
 if x[0]<N:v.append(1+sum((P[i]*bell(child(x,i))[0] for i in range(3)),F()))
 m=min(v);return m,tuple(a for a,y in zip('PQC',v) if y==m),v
tie={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   x=(n,a,b);v,acts,opts=bell(x)
   if len(acts)>1:tie[x]=acts
   gaps.extend(y-v for y in opts if y>v)
assert tie=={T:('P','C'),S:('Q','C')} and len(gaps)==1238
H=bell((0,0,0))[0]
assert H==F(977402749984215798412630525,5975334471155518248321024)
assert min(gaps)==F(67271053,31414384008)
def run(t,s):
 @lru_cache(None)
 def rec(x):
  if x==T:act='P' if t else 'C'
  elif x==S:act='Q' if s else 'C'
  else:act=bell(x)[1][0]
  if act=='P':return F(),F(1),F(),F()
  if act=='Q':return F(1),F(),F(),F()
  z=[rec(child(x,i)) for i in range(3)]
  return(sum((P[i]*z[i][0] for i in range(3)),F()),
         sum((Q[i]*z[i][1] for i in range(3)),F()),
         1+sum((P[i]*z[i][2] for i in range(3)),F()),
         1+sum((Q[i]*z[i][3] for i in range(3)),F()))
 return rec((0,0,0))
m=run(0,0);dt=tuple(x-y for x,y in zip(run(1,0),m))
ds=tuple(x-y for x,y in zip(run(0,1),m))
assert run(1,1)==tuple(m[i]+dt[i]+ds[i] for i in range(4))
assert dt==(F(-1210671875,1114512556032),F(2319296875,1253826625536),
F(-16248859375,92876046336),F(-9353640625,104485552128))
assert ds==(F(15611328125,3962711310336),F(-1813671875,557256278016),
F(-63480078125,495338913792),F(-10480859375,46438023168))
t0=F(1870960582929997,3860125696000000)
ts=F(147788325,60314464)
sstar=F(221018345896667,1050939200000000)
assert t0+ts*sstar==1
def mix(s):return tuple(m[i]+(t0+ts*s)*dt[i]+s*ds[i] for i in range(4))
left,right=mix(F()),mix(sstar)
assert left[0]==left[1]==F(5148172029061283786075,14750257906470044565504)
assert left[2]==F(338725183820868439620725,29500515812940089131008)
assert right[0]==right[1]==F(1571019175748196236077,4497734146660704976896)
assert right[2]==F(25558154902620967560277,2248867073330352488448)
assert all(v[2]>=v[3] and v[2]+K*v[1]+L*v[0]==H for v in (left,right))
assert right[0]>left[0] and right[2]<left[2]
assert right[2]-left[2]==-(K+L)*(right[0]-left[0])
print('STAGE178_REFERENCE_RATIONAL_CHECK_PASS')
