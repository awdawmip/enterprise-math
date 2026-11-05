#!/usr/bin/env python3
"""Exact all-triples for H4-H6 signed X6 BRC fixed-cache neighborhood."""
from itertools import combinations
import json
from pathlib import Path
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
OPS='acdefg'
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ENC={-1:'a',1:'A',-2:'b',2:'B',-3:'c',3:'C'}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
W={2:('fe','ge'),3:('feg','gef'),4:('degf','fegd','cefg','gefc'),5:('feggf','geffg'),6:('aeeddd','dedead','aeeccc','ceceac'),7:('aeeddgf','dedeagf','ceceafg','aeeccfg'),8:('feggfead','geffgaed','geffgaec','feggfeac'),9:('feggfeafg','geffgaegf')}

def observe(w):
 s=0
 for c in w:
  s=T[s][OPS.index(c)]
  if s==8: return None
 return SIG[s]
def primitive(w):
 return ''.join(ENC[i] for c in w for i in STEPS[c])
def pref(w):
 s=primitive(w)
 return tuple(s[:i] for i in range(1,len(s)+1))

def legal(h):
 x,y,z=(4,2,1) if h<=5 else (7,3,2)
 b=x+y-h-1;a=z-1;f=x-b-2*z;g=y-b
 assert min(b,a,f,g)>=0
 out={sig:[] for sig in REQ[h]}
 for c in range(b+1):
  counter={'a':a,'c':c,'d':b-c,'e':z,'f':f,'g':g}
  def rec(w,s):
   if len(w)==h:
    if SIG[s] in out: out[SIG[s]].append(w)
    return
   for i,op in enumerate(OPS):
    if counter[op]>0 and T[s][i]!=8:
     counter[op]-=1;rec(w+op,T[s][i]);counter[op]+=1
  rec('',0)
 return out

def main():
 chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
 assert len(chosen)==24
 E={w:pref(w) for words in W.values() for w in words}
 root=set().union(*(set(E[w]) for w in chosen.values()))
 assert len(root)==158
 slots=[];pools={};counts={}
 for h in range(4,7):
  g=legal(h);counts[str(h)]=sum(map(len,g.values()))
  for sig in REQ[h]:
   slot=f'{h}:{sig}';slots.append(slot);pools[slot]=g[sig]
   assert chosen[slot] in g[sig]
   for w in g[sig]:E[w]=pref(w)
 assert counts=={'4':48,'5':24,'6':120}
 # Assign bit id only to prefixes of candidate words, but all 24 selected words included.
 ids={s:i for i,s in enumerate(set(p for paths in E.values() for p in paths))}
 bits={w:sum(1<<ids[p] for p in E[w]) for w in E}
 original={s:bits[w] for s,w in chosen.items()}
 assert _union(original.values()).bit_count()==158
 results=[];bests=[];total_evals=0
 for trio in combinations(slots,3):
  rest=_union(b for s,b in original.items() if s not in trio)
  A=[(w,bits[w]&~rest) for w in pools[trio[0]]]
  B=[(w,bits[w]&~rest) for w in pools[trio[1]]]
  C=[(w,bits[w]&~rest) for w in pools[trio[2]]]
  mincost=10**9;arg=None
  for wa,ba in A:
   for wb,bb in B:
    u=ba|bb
    for wc,bc in C:
     v=rest.bit_count()+(u|bc).bit_count()
     total_evals+=1
     if v<mincost: mincost=v;arg=(wa,wb,wc)
  assert mincost<=158,(trio,mincost)
  # Independently recompute winning witness directly from signed words, no bits.
  witness=chosen.copy();witness.update(zip(trio,arg))
  actual=len(set().union(*(set(pref(w)) for w in witness.values())))
  assert actual==mincost,(trio,mincost,actual)
  item={'slots':list(trio),'minimum':mincost,'minimizer':list(arg),'eval_count':len(A)*len(B)*len(C)}
  results.append(item)
  if mincost<158: bests.append(item)
 out={'schema':'EC49FBW_H4_H6_ALL_TRIPLES_EXACT_V1','frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','candidate_count':counts,'fixed_reference':W,'baseline_edges':158,'slot_count':len(slots),'tested_triplets':len(results),'complete_evaluations':total_evals,'min_achieved':min(x['minimum'] for x in results),'improvements':bests,'triple_results':results}
 with Path(__file__).with_name('EXACT_REPORT_EC49FBW.json').open('w') as fh:json.dump(out,fh,ensure_ascii=False,indent=2)
 print(json.dumps({k:v for k,v in out.items() if k not in ('triple_results','fixed_reference')},indent=2))

def _union(xs):
 r=0
 for v in xs:r|=v
 return r
if __name__=='__main__': main()
