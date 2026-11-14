#!/usr/bin/env python3
"""EC49FOZ: exact depth-2 obstruction and depth-3 adaptive policy.
Run in the EC49FOZ evidence folder with SOURCE/ from EC49FOY.
"""
from pathlib import Path
from collections import defaultdict
from itertools import product
import csv, hashlib
S=Path('SOURCE'); R=(3,5,6,7)
H='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
CSV={14304:'03c030adfd11fd833a4d7234dd3b963511eb6ae14cb4c6010e8e667a03f3d52f',
     14309:'cc734f77d2d142651fdfcb41d38b20ae93b0d85f7b49fa90f2e868f92c0de7f6'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load():
 p=S/'EC49FOW_EVIDENCE/frozen_original_master.txt';assert digest(p)==H
 with p.open() as h:
  assert tuple(map(int,h.readline().split()))==(94,178850,38169)
  keys=[]
  for _ in range(94):
   m=[0]*24
   for j in range(int(h.readline())):
    l,w=h.readline().split();m[int(l)]|=1<<R.index(int(w[:2],16))
   keys.append(m)
  cases=[tuple(map(int,h.readline().split())) for _ in range(38169)]
 return keys,cases
def costs(rep,keys,cases):
 def dom(case):
  d=[0]*24
  for k in case:
   for i,m in enumerate(keys[k]):d[i]|=m
  return tuple(d)
 d=dom(cases[rep]);ids=[i for i,c in enumerate(cases) if dom(c)==d]
 assert len(ids)==75 and ids==list(map(int,(S/f'CLASS_{rep}_IDS.txt').read_text().split()))
 optional=[i for i,m in enumerate(d) if m.bit_count()>1]
 actions=list(product(*(tuple(r for j,r in enumerate(R) if m>>j&1) for i,m in enumerate(d) if m.bit_count()>1)))
 assert len(optional)==7 and len(actions)==432
 p=S/f'CLASS_{rep}_PROFILES.csv';assert digest(p)==CSV[rep]
 g=defaultdict(dict)
 with p.open(newline='') as h:
  for row in csv.DictReader(h):
   c,r,s,v=(int(row[x]) for x in ('config','root','subset','cost'))
   assert (r,s) not in g[c];g[c][r,s]=v
 assert set(g)==set(ids)
 unique={}
 for c in ids:unique.setdefault(tuple(sorted(g[c].items())),c)
 assert len(unique)==40
 out=[]
 for c in unique.values():
  row=[]
  for a in actions:
   subsets={r:0 for r in R}
   for label,r in zip(optional,a):subsets[r]|=1<<label
   row.append(sum(g[c][r,subsets[r]] for r in R))
  out.append(tuple(row))
 assert len(set(out))==40
 return out
def fibers(cost,mask,j):
 d=defaultdict(int)
 for i,row in enumerate(cost):
  if mask>>i&1:d[row[j]]|=1<<i
 return list(d.values())
def one(cost,mask):
 if mask.bit_count()<=1:return 0
 for j in range(432):
  if all(b.bit_count()==1 for b in fibers(cost,mask,j)):return j
 return None
def verify(rep,cost,first):
 whole=(1<<40)-1
 for j in range(432):
  assert any(one(cost,b) is None for b in fibers(cost,whole,j)),('depth2',rep,j)
 branches=second=third=0
 for b in fibers(cost,whole,first):
  branches+=1
  if b.bit_count()==1:continue
  for j in range(432):
   sub=fibers(cost,b,j)
   if all(one(cost,c) is not None for c in sub):break
  else:raise AssertionError(('depth3',rep,b))
  second+=1
  third+=sum(c.bit_count()>1 for c in sub)
 assert (branches,second,third)==(22,7,7)
 print('PASS',rep,'depth2 excluded for all 432 first actions; depth3 attained',
       'first',first,'nodes',branches,second,third)
if __name__=='__main__':
 keys,cases=load()
 for rep,first in ((14304,78),(14309,119)):
  verify(rep,costs(rep,keys,cases),first)
 print('EXACT_ADAPTIVE_MINIMUM_3_BOTH')
