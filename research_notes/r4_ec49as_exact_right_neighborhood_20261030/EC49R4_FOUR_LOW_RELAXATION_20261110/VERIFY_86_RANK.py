#!/usr/bin/env python3
"""Native signed-X6 literal prefix and nine-history rank audit for the 86-edge witness."""
from ec49fgd_mixed_seed_dp import expand,signature,key,pref
from collections import defaultdict
import json
A={'N':0,'A':1,'B':2,'AB':3,'BA':4}
START=[('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0)]
W={2:['fe','ge'],3:['feg','gef'],4:['gefd','fegd','fegc','gefc'],
   5:['feggg','gefgg'],6:['gefdff','fegdff','fegcgg','gefcgg'],
   7:['gefdfff','fegdfff','fegcggg','gefcggg'],
   8:['gefdffff','fegdffff','fegcgggg','gefcgggg'],
   9:['feggggggg','gefgggggg']}
def obs(word):
 st=expand(word);out=[]
 for name,v in START:
  z=name;p=v
  for a in st:
   if p==1 and a==2:
    if z=='N':z='A'
    elif z=='B':z='BA'
   elif p==2 and a==1:
    if z=='N':z='B'
    elif z=='A':z='AB'
   p=a
  out.append(A[z])
 return out
def rank(ws):
 P=1000003
 obsall=[obs(w) for w in ws]
 M=[[int(o[i]==j) for o in obsall for j in range(5)] for i in range(9)]
 p=0
 for j in range(len(M[0])):
  piv=next((i for i in range(p,9) if M[i][j]%P),None)
  if piv is None:continue
  M[p],M[piv]=M[piv],M[p]
  inv=pow(M[p][j],-1,P)
  M[p]=[(x*inv)%P for x in M[p]]
  for i in range(p+1,9):
   f=M[i][j]
   if f:M[i]=[(u-f*v)%P for u,v in zip(M[i],M[p])]
  p+=1
  if p==9:break
 return p
sigs={h:[signature(w) for w in ws] for h,ws in W.items()}
ranks={h:rank(ws) for h,ws in W.items()}
assert all(x==9 for x in ranks.values())
P=set().union(*(pref(w) for ws in W.values() for w in ws))
assert len(P)==86
KEYS={h:sorted(set(key(w) for w in ws)) for h,ws in W.items() if h>=4}
print(json.dumps({'rank_mod1000003':ranks,'signatures':sigs,'key_sets':KEYS,
 'distinct_positive_keys':len({k for ks in KEYS.values() for k in ks}),
 'prefix_edges':len(P)},indent=2))
