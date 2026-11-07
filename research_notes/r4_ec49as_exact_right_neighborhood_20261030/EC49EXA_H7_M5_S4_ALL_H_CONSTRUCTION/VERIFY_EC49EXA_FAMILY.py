#!/usr/bin/env python3
"""EC49EXA exact rational/integer checker, independently coded finite-X6 witness.

This checks explicit all-H constructive family, with no numerical tolerance.
The symbolic two-channel BRC keys are complete positive-count vectors; no logarithms.
"""
import json,sys
from fractions import Fraction

OPS={
'a':(-1,-1), 'b':(-2,-2), 'c':(1,2,-1,-2),
'd':(2,1,-2,-1), 'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
HISTORY=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')

def expand(w):return tuple(a for op in w for a in OPS[op])

def positive_count(w):
  steps=expand(w)
  return tuple(sum(a==i for a in steps) for i in range(1,7))

def return_displacement(w):
  steps=expand(w)
  return tuple(sum(a==i for a in steps)-sum(a==-i for a in steps) for i in range(1,7))

def signature(w):
  out=[]
  for stage,previous in HISTORY:
    for step in expand(w):
      if previous==1 and step==2:
        stage={'N':'A','B':'BA'}.get(stage,stage)
      elif previous==2 and step==1:
        stage={'N':'B','A':'AB'}.get(stage,stage)
      previous=step
    out.append(BUCKETS.index(stage))
  return tuple(out)

def family(h):
  if h==2:return ('ce','de','ec','ed')
  if h==3:return ('cec','ded','ecc','edd')
  if h>=4:
    return tuple(x+'f'*(h-4) for x in ('cefg','degf','ecfg','edgf'))
  raise ValueError(h)

def rational_rank(rows):
  a=[[Fraction(x) for x in row] for row in rows]
  rank=0
  for c in range(9):
    pivot=next((r for r in range(rank,len(a)) if a[r][c]),None)
    if pivot is None:continue
    a[rank],a[pivot]=a[pivot],a[rank]
    lead=a[rank][c]
    a[rank]=[x/lead for x in a[rank]]
    for r in range(len(a)):
      if r!=rank and a[r][c]:
        fac=a[r][c]
        a[r]=[x-fac*y for x,y in zip(a[r],a[rank])]
    rank+=1
  return rank

def obs_rows(words):
  return [tuple(int(x==bucket) for x in signature(w)) for w in words for bucket in range(5)]

def det_bareiss(mat):
  a=[list(map(int,row)) for row in mat];n=len(a);sign=1;prev=1
  for k in range(n-1):
    if a[k][k]==0:
      r=next((i for i in range(k+1,n) if a[i][k]),None)
      if r is None:return 0
      a[k],a[r]=a[r],a[k];sign=-sign
    pivot=a[k][k]
    for i in range(k+1,n):
      for j in range(k+1,n):
        numerator=a[i][j]*pivot-a[i][k]*a[k][j]
        assert numerator%prev==0
        a[i][j]=numerator//prev
    for i in range(k+1,n):a[i][k]=0
    prev=pivot
  return sign*a[-1][-1]

def edge_union(groups):
  return {expand(w)[:k] for words in groups for w in words for k in range(1,len(expand(w))+1)}

def run(H=24):
  assert H>=4
  reference=tuple(signature(w) for w in family(2))
  assert len(set(reference))==4
  indices=(1,3,4,7,8,11,13,17,18)
  minor=[obs_rows(family(2))[i] for i in indices]
  assert det_bareiss(minor)==-1
  verified=[]
  for h in range(2,H+1):
    words=family(h)
    assert all(len(w)==h for w in words)
    assert all(return_displacement(w)==(2,0,0,0,0,0) for w in words)
    assert tuple(signature(w) for w in words)==reference
    assert rational_rank(obs_rows(words))==9
    positive={positive_count(w) for w in words}
    assert len(positive)==1
    ph=next(iter(positive))
    expect=(3,1,1,0,0,0) if h==2 else ((4,2,1,0,0,0) if h<=4 else (h,2,1,0,0,0))
    assert ph==expect,(h,ph,expect)
    E=len(edge_union(family(i) for i in range(2,h+1)))
    assert E==({2:28,3:44,4:56}.get(h,8*h+24)),(h,E)
    M=len({positive_count(family(i)[0]) for i in range(2,h+1)})
    assert M==({2:1,3:2}.get(h,h-2)),(h,M)
    verified.append({'h':h,'E':E,'M':M,'S':len(reference),'shared_positive_count':ph})
  return {'status':'PASS','integer_arithmetic':True,'exact_rational_rank':True,'full_X6_six_coordinates':True,'rank9_9x9_minor_det':-1,'H_tested':H,'terminal':verified[-1],'checks':verified,'theorem':'Analytic all integer H >=4: E=8H+24,M=H-2,S=4; checker validates h<=H'}

if __name__=='__main__':
  H=int(sys.argv[1]) if len(sys.argv)>1 else 24
  print(json.dumps(run(H),ensure_ascii=False,indent=2))
