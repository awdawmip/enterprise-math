#!/usr/bin/env python3
"""S23/AV gap classes, exact rational enclosure and O(H) memory streaming audit.

Input model and verification pattern come from Enterprise Math
research_notes/brc_s23_av_gap_class_h5000_20261108_r1/VERIFY_H5000.py
at immutable GitHub commit 83ec2f3dd0dfc5e24aa89578a927612b5a7c270c.
Change: replace materialized O(H^2) threshold sort with H+1-row exact heap merge.
"""
from fractions import Fraction
from collections import defaultdict
from hashlib import sha256
from time import perf_counter
from heapq import heapify, heappop, heappush, heapreplace
import sys

H=int(sys.argv[1]) if len(sys.argv)>1 else 10000
N=2455069; Q=10**26

def enclosure(z, terms=45):
 s=Fraction(0);term=z
 for i in range(terms):
  s += 2*term/(2*i+1);term*=z*z
 return s,s+2*term/((2*terms+1)*(1-z*z))

l2,u2=enclosure(Fraction(1,3));l9,u9=enclosure(Fraction(1,9));l15,u15=enclosure(Fraction(1,15))
a,b=3*l2-u15,3*u2-l15;c,d=l9+l15,u9+u15
lo=a*Q//d;hi=b*Q//c+1
assert lo==545569623581288298975349314 and hi==lo+1
assert Fraction(lo,Q)<a/d and b/c<Fraction(hi,Q)
print('PASS_EXACT_LOG_ENCLOSURE',lo,hi,Q,flush=True)
start=perf_counter()
# Each fixed-v row is sorted ascending by j=H-v,H-v-1,...,0.
# The row's key advances by exactly Q on every pop.
heap=[(lo*v-Q*(H-v),v,H-v) for v in range(H+1)]
heapify(heap)
M=(H+1)*(H+2)//2
classes={};prev=None; count=0
while heap:
 key,v,j=heappop(heap)
 if prev is not None:
  vl,jl=prev;dv,dj=v-vl,j-jl
  # adverse endpoint gives strict actual order
  assert (lo if dv>=0 else hi)*dv>Q*dj,('BAD_ORDER',count,prev,(v,j))
  cls=(dv,dj)
  if cls not in classes: classes[cls]=[vl,jl,vl+jl,1]
  else:
   z=classes[cls]
   if vl>z[0]:z[0]=vl
   if jl>z[1]:z[1]=jl
   if vl+jl<z[2]:z[2]=vl+jl
   z[3]+=1
 prev=v,j;count+=1
 if j:heappush(heap,(key+Q,v,j-1))
assert count==M and sum(c[3] for c in classes.values())==M-1
print('PASS_STREAMED_ORDER',H,M,'classes',len(classes),'seconds',round(perf_counter()-start,3),flush=True)

def valid(K,L,dv,dj,V,J,S):
 return K>=J and L>=V and K+L<=N+S and K*Q>hi*L and (K+dj)*Q<lo*(L+dv)

rows=[];not_found=[]
for (dv,dj),rec in sorted(classes.items(), key=lambda item:(-item[1][3],item[0])):
 V,J,S,num=rec
 if (dv,dj)==(79,431):
  K,L=2074774,380295
  assert valid(K,L,dv,dj,V,J,S)
 else:
  for L in range(V,V+100000):
   fl=lo*L//Q;fh=hi*L//Q
   assert fl==fh
   K=max(fl+1,J)
   if valid(K,L,dv,dj,V,J,S):break
  else:
   not_found.append((dv,dj,rec));continue
 rows.append((dv,dj,V,J,S,num,K,L,K+L-S))
 print('CLASS',dv,dj,'COUNT',num,'MAXV',V,'MAXJ',J,'MINSUM',S,'WITNESS_KL',K,L,'MAX_LENGTH',K+L-S,flush=True)
ell=H*Q//lo+1;k=hi*H//Q+1
assert lo*ell>H*Q and k*Q>hi*H
assert ell<=N and k<=N
print('PASS_OUTER_CELLS',0,ell,k,0,flush=True)
print('UNRESOLVED_CLASSES',not_found,flush=True)
if not not_found:
 assert len(rows)==len(classes)
 assert max(row[-1] for row in rows)<=N
 print('CLASS_DATA_SHA256',sha256('\n'.join(','.join(map(str,row)) for row in rows).encode()).hexdigest(),flush=True)
 print('PASS_S23_AV_STREAM_GAP_CLASS_ENDPOINT',H,N,'seconds',round(perf_counter()-start,3),flush=True)
