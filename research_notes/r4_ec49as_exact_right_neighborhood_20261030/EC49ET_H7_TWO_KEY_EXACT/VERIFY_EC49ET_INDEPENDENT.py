#!/usr/bin/env python3
"""Independent exact native-X6 witness check and exhaustive fiber/type audit.
Python standard library only; no imports from EC49ET optimization code.
"""
from itertools import permutations
from fractions import Fraction
from collections import Counter
import json
from pathlib import Path

OP={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HISTORY=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
B=('N','A','B','AB','BA')
W={2:['ce','de','ec','ed'],3:['feg','gef'],4:['cecc','dedd','eccc','eddd'],5:['cecfg','dedgf','eccfg','eddgf'],6:['fegfgc','fegfgd','geffgc','geffgd'],7:['fegfggf','geffgfg']}

def primitives(w):return tuple(t for x in w for t in OP[x])
def p_counts(w):
 q=primitives(w);return tuple(sum(x==i for x in q) for i in range(1,7))
def displacement(w):
 q=primitives(w);return tuple(q.count(i)-q.count(-i) for i in range(1,7))
def signature(w):
 out=[]
 for state,last in HISTORY:
  for d in primitives(w):
   if last==1 and d==2:
    if state=='N':state='A'
    elif state=='B':state='BA'
   if last==2 and d==1:
    if state=='N':state='B'
    elif state=='A':state='AB'
   last=d
  out.append(tuple(x==state for x in B))
 return tuple(out)
def rank(matrix):
 rows=[list(map(Fraction,row)) for row in matrix]
 m,n=len(rows),len(rows[0]);r=0
 for j in range(n):
  i=next((i for i in range(r,m) if rows[i][j]),None)
  if i is None:continue
  rows[r],rows[i]=rows[i],rows[r]
  div=rows[r][j];rows[r]=[x/div for x in rows[r]]
  for k in range(r+1,m):
   coef=rows[k][j]
   if coef: rows[k]=[a-coef*b for a,b in zip(rows[k],rows[r])]
  r+=1
  if r==m:break
 return r

def observation_rank(words):
 sig=[signature(w) for w in words]
 matrix=[[col for tr in sig for col in tr[i]] for i in range(9)]
 return rank(matrix)

def all_unique(letters):return {''.join(p) for p in permutations(letters)}

def audit(words):
 E=set();M=set();S=set(); observations={}
 for h,ww in words.items():
  assert all(len(w)==h and displacement(w)==(2,0,0,0,0,0) for w in ww)
  expected=(3,1,1,0,0,0) if h<=3 else (5,3,1,0,0,0)
  assert {p_counts(w) for w in ww}=={expected}
  assert observation_rank(ww)==9
  for w in ww:
   v=primitives(w)
   for j in range(1,len(v)+1):E.add(v[:j])
   M.add(p_counts(w));S.add(signature(w))
  observations[h]=dict(words=ww,rank=9,native_length=sorted({len(primitives(w)) for w in ww}))
 assert (len(E),len(M),len(S))==(116,2,6)
 return observations
def main():
 observations=audit(W)
 winner={2:list(W[2]),**{int(h):ww for h,ww in json.loads(Path('EC49ET_MILP_EXECUTED.json').read_text())['optimizer']['witness'].items()}}
 audit(winner)
 E=set();M=set();S=set()
 # Exhaust full native return equal-positive-count fibers by inverse count formulas.
 counts={}
 for h in range(3,8):
  p=(3,1,1) if h==3 else (5,3,1)
  e=p[2]; r=p[0]+p[1]-h-1
  assert r>=0
  f=p[0]-2*e-r;g=p[1]-r
  allw=set()
  for c in range(r+1):
   allw|=all_unique('a'*(e-1)+'e'*e+'c'*c+'d'*(r-c)+'f'*f+'g'*g)
  need={signature(t) for t in (('feg','gef') if h in (3,7) else ('ce','de','ec','ed'))}
  selected={w for w in allw if signature(w) in need}
  count_expected={3:(6,4),4:(32,8),5:(240,120),6:(360,360),7:(140,120)}[h]
  assert (len(allw),len(selected))==count_expected
  assert all(displacement(w)==(2,0,0,0,0,0) and p_counts(w)==(*p,0,0,0) for w in allw)
  counts[h]=dict(all_words=len(allw),mandatory_signature_candidates=len(selected))
 report={'unit':'EC49ET','status':'PASS','model':'ordered six-axis native steps + 9-history first A/B observer','scope':'all words in unique two-key H7 fiber assignment; exact rational witness ranks','ranks':observations,'resource_count':[116,2,6],'complete_fiber_counts':counts}
 Path('EC49ET_INDEPENDENT_EXECUTED.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','resource_count':report['resource_count'],'fiber_counts':counts},ensure_ascii=False))
if __name__=='__main__':main()
