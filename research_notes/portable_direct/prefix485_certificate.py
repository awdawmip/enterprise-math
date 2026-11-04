#!/usr/bin/env python3
"""PREFIX-485: exact integer BRC-KMP-source finite-horizon certificate."""
from collections import defaultdict,Counter
A='aAbBcCdDeE'; V=(0,1,0,2,1); W=(0,0,1,0,1)
def kmp(q,c,w):
 s=w[:q]+c;return max(j for j in range(len(w)+1) if s.endswith(w[:j]))
def sr(t,c):
 return t if t or c not in 'bBcC' else (1 if c in 'bB' else 2)
def mv(o,i):
 r=list(o)
 if i==10:r[0]+=1
 else:
  a=i//2;positive=i%2==0;y=o[a+1]
  d=int(y<0) if positive else int(y>0)
  r[a+1]+=1 if positive else -1;r[6]+=d*V[a];r[7]+=d*W[a]
 return tuple(r)
def word(s,w):
 o=(0,)*8;q=t=0
 for c in s:
  if c=='x':assert q==len(w) or o==(0,)*8;o=mv(o,10);q=0
  else:o=mv(o,A.index(c));q=kmp(q,c,w);t=sr(t,c)
 return o,q,t
def check(w):
 z=[word(s,w) for s in ('aAeE','bBcC','cCbB')]
 assert len({(o,q) for o,q,t in z})==1
 assert z[0]==((0,0,0,0,0,0,1,1),0,0)
 assert [t for o,q,t in z]==[0,1,2]
 assert [word(s+'b',w)[2]==1 for s in ('aAeE','bBcC','cCbB')]==[True,True,False]
 d={((0,)*8,0,0):1};e={(0,0):1}
 for n in range(9):
  fibers=defaultdict(set)
  for (o,q,t),count in d.items():fibers[(o,q)].add(t)
  hist=Counter(map(len,fibers.values()))
  h0=sum(1+int(1 in a and (0 in a or 2 in a)) for a in fibers.values())
  total=sum(d.values())
  assert total==sum(e.values())
  assert all(sum(v for (o,q,t),v in d.items() if t==s)==sum(v for (q,t),v in e.items() if t==s) for s in range(3))
  print(w,n,'base',len(fibers),'H0',h0,'H1',len(d),'types',hist[1],hist[2],hist[3],'paths',total)
  if n==8:
   expected={'aab':(58496,87405,87691,29587,28623,286), 'aba':(58498,87381,87640,29615,28624,259)}[w]
   assert (len(fibers),h0,len(d),hist[1],hist[2],hist[3])==expected
   assert total==110054001
   break
  dn=defaultdict(int);en=defaultdict(int)
  for (o,q,t),count in d.items():
   for i,c in enumerate(A):dn[(mv(o,i),kmp(q,c,w),sr(t,c))]+=count
   if n==0 or q==len(w):dn[(mv(o,10),0,t)]+=count
  for (q,t),count in e.items():
   for c in A:en[(kmp(q,c,w),sr(t,c))]+=count
   if n==0 or q==len(w):en[(0,t)]+=count
  d,e=dn,en
for gate in ('aab','aba'):check(gate)
print('ALL_CHECKS_PASS')
