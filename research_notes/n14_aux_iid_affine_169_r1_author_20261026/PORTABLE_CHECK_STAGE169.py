#!/usr/bin/env python3
"""R1 Stage169 author checker: external ternary IID N<=14, exact rational arithmetic.
Checks Bellman dual + four-corner suffix and independent integer-path prefix DFS.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import product
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
PN=(3,1,20);QN=(1,1,10)
K=F(100796326719840,394715670863);L=F(298940013781960,1184147012589)
R=(10,0,1);Y=(6,4,1)
A0=F(882432475025404219615,2530093150022563528704)
V0=F(4191390146637112343957,361441878574651932672)
def c(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
 o=[K*ratio(s),L]
 if s[0]<N:o.append(1+sum(P[i]*bell(c(s,i))[0] for i in range(3)))
 return min(o),o
unique={};ties={};gaps=[]
for n in range(15):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,o=bell(s);w=[i for i,x in enumerate(o) if x==v]
   if len(w)>1:ties[s]=tuple('PQC'[i] for i in w)
   else:unique[s]='PQC'[w[0]]
   gaps.extend(x-v for x in o if x>v)
assert len(unique)+len(ties)==680 and len(gaps)==1238 and min(gaps)>0
assert ties=={R:('Q','C'),Y:('P','C')}
assert bell((0,0,0))[0]==F(24482517961003925257583517135827,129736380945356220519564705792)
def action(s,r,y):return ('Q' if r else 'C') if s==R else ('P' if y else 'C') if s==Y else unique[s]
def suffix(r,y):
 @lru_cache(None)
 def go(s):
  a=action(s,r,y)
  if a=='P':return F(0),F(1),F(0),F(0)
  if a=='Q':return F(1),F(0),F(0),F(0)
  z=[go(c(s,i)) for i in range(3)]
  return (sum(P[i]*z[i][0] for i in range(3)),sum(Q[i]*z[i][1] for i in range(3)),1+sum(P[i]*z[i][2] for i in range(3)),1+sum(Q[i]*z[i][3] for i in range(3)))
 return go((0,0,0))
def ordered(r,y):
 sums=defaultdict(int);hits={R:[0,F(0),F(0)],Y:[0,F(0),F(0)]}
 def walk(n,a,b,p,q):
  s=(n,a,b)
  if s in hits:
   hits[s][0]+=1;hits[s][1]+=F(p,24**n);hits[s][2]+=F(q,12**n)
  t=action(s,r,y)
  if t!='C':
   for k,w in [('Pm',p),('Qm',q),('tP',n*p),('tQ',n*q)]:sums[n,k]+=w
   if t=='P':sums[n,'eQ']+=q
   else:sums[n,'eP']+=p
   return
  for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*PN[i],q*QN[i])
 walk(0,0,0,1,1)
 def total(k,d):return sum((F(sums[n,k],d**n) for n in range(15)),F(0))
 assert total('Pm',24)==total('Qm',12)==1
 return (total('eP',24),total('eQ',12),total('tP',24),total('tQ',12)),hits
corners={};first_hits=None
for r,y in product((0,1),repeat=2):
 a=suffix(r,y);b,h=ordered(r,y)
 assert a==b,(r,y,a,b)
 assert first_hits is None or h==first_hits
 corners[r,y]=a;first_hits=h
assert first_hits[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert first_hits[Y]==[18,F(5,32768),F(5,82944)]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda t,a:tuple(t*x for x in a)
m=corners[0,0];dr=sub(corners[1,0],m);dy=sub(corners[0,1],m)
assert sub(sub(corners[1,1],corners[0,1]),dr)==(F(0),)*4
err=lambda x:x[0]-x[1]
r0=-err(m)/err(dr);rs=-err(dy)/err(dr)
assert (r0,rs)==(F(8969559568954741,11823616000000000),F(874857538089,1477952000000000))
obs=lambda r,y:add(add(m,scale(r,dr)),scale(y,dy))
lo,hi=obs(r0,0),obs(r0+rs,1)
assert 0<r0<r0+rs<1 and lo[0]==lo[1]==A0 and lo[2]==V0 and lo[2]>lo[3]
assert hi[0]==hi[1]==F(882433753904177815735,2530093150022563528704)
assert hi[2]==F(4191297370163761372757,361441878574651932672) and hi[2]>hi[3]
assert lo[2]+K*lo[1]+L*lo[0]==hi[2]+K*hi[1]+L*hi[0]==bell((0,0,0))[0]
assert hi[0]-lo[0]==F(1973578354315,3904464737689141248)
assert Y[1]>R[1] and Y[0]<R[0]
print('PASS: 680 count states; 1238 positive action gaps; two ties R,Y')
print('Hroot:',bell((0,0,0))[0],'K+L:',K+L,'min gap:',min(gaps))
print('first hit R,Y:',first_hits)
print('r(y)=',r0,'+',rs,'*y')
print('left:',lo,'right:',hi,'width:',hi[0]-lo[0])
print('PASS: suffix=ordered integer DFS, four corners, affine, balanced, dual tight and inherited endpoint')
print('STATUS: AUTHOR_VERIFIED; NATIVE_REVIEW_PENDING; NATIVE_X6_TRANSFER_UNPROVED')
