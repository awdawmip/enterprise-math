#!/usr/bin/env python3
"""Exact finite BRC Bellman solver for two independent original named prices.
Frozen class 16943, 141 named states, 228 physical observations.  Inputs p32/t=1-a, p34/t=1-b.
Run from extracted self-contained archive's code directory with both parser modules present.
"""
import sys, json, time, math
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parent))
from EC49FQI_NATIVE_DATA import V,PIN,keys
from EC49FRQ_INDEPENDENT_ALL228 import OBS,subset_keys
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(V)==228 and len(OBS)==228
assert all(tuple(OBS[i])==tuple(V[i if i<144 else 144+keys.index(subset_keys[i-144])]) for i in range(228))
ALL=(1<<141)-1
parts=[]
for vec in V:
 d={}
 for i,resp in enumerate(vec):
  d[resp]=d.get(resp,0)|(1<<i)
 parts.append(tuple(d.values()))

def solve(a,b,full=False):
 a,b=Fraction(a),Fraction(b)
 assert 0<=a<=1 and 0<=b<=1
 den=math.lcm(a.denominator,b.denominator)
 ca=den-a*den
 cb=den-b*den
 prices=[den]*228
 prices[32]=int(ca)
 prices[34]=int(cb)
 t0=time.perf_counter()
 @lru_cache(maxsize=None)
 def D(mask):
  n=mask.bit_count()
  if n==1:
   return (0,-1)
  best=10**30
  bi=-1
  for q,partition in enumerate(parts):
   children=[mask & c for c in partition if mask & c]
   if len(children)<2:
    continue
   val=n*prices[q]
   for child in children:
    if child.bit_count()>1:
     val+=D(child)[0]
     if val>best:
      break
   if val<best:
    best,bi=val,q
  assert bi>=0
  return (best,bi)
 value,root=D(ALL)
 def tree(mask):
  if mask.bit_count()==1:
   return {'leaf':mask.bit_length()-1}
  q=D(mask)[1]
  children={}
  for partition in parts[q]:
   child=mask&partition
   if child:
    i=(child&-child).bit_length()-1
    children[str(V[q][i])]=tree(child)
  return {'named_observer':q,'children':children}
 obj=tree(ALL)
 cnt=Counter()
 depthmax=0
 for i in range(141):
  n=obj
  d=0
  used=set()
  while 'named_observer' in n:
   q=n['named_observer']
   assert q not in used
   used.add(q)
   cnt[q]+=1
   d+=1
   n=n['children'][str(V[q][i])]
  assert n['leaf']==i
  depthmax=max(d,depthmax)
 u=sum(cnt.values())
 k32=cnt[32]
 k34=cnt[34]
 assert value==u*den-a.numerator*(den//a.denominator)*k32-b.numerator*(den//b.denominator)*k34
 info={'a':str(a),'b':str(b),'Bellman_integer_value':value,'denominator':den,'U':u,'N32':k32,'N34':k34,'root_observer':root,'states':D.cache_info().currsize,'worst_depth':depthmax,'seconds':round(time.perf_counter()-t0,3)}
 return info,obj if full else None

if __name__=='__main__':
 a,b=sys.argv[1:3]
 info,tree=solve(a,b,True)
 print(json.dumps(info,ensure_ascii=False),flush=True)
 if len(sys.argv)>=4:
  Path(sys.argv[3]).write_text(json.dumps({'info':info,'tree':tree},ensure_ascii=False,separators=(',',':'))+'\n')
