"""Literal source semantics copied from immutable VERIFY_EC49FBY.py at 5b10f1c...; use frozen signed-native paths."""
from pathlib import Path
from itertools import combinations
import json,time,sys
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ENC={-1:'a',1:'A',-2:'b',2:'B',-3:'c',3:'C'}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
W={2:('fe','ge'),3:('feg','gef'),4:('degf','fegd','cefg','gefc'),5:('feggf','geffg'),6:('aeeddd','dedead','aeeccc','ceceac'),7:('aeeddgf','dedeagf','aeeccfg','ceceafg'),8:('feggfead','geffgaed','geffgaec','feggfeac'),9:('feggfeafg','geffgaegf')}
def observe(w):
 s=0
 for op in w:
  s=T[s][OPS.index(op)]
  if s==8:return None
 return SIG[s]
def primpref(w):
 s=''.join(ENC[i] for op in w for i in STEPS[op]);return tuple(s[:k] for k in range(1,len(s)+1))
def candidates(h):
 x,y,z=(4,2,1) if h<=5 else (7,3,2)
 b=x+y-h-1; a=z-1;f=x-b-2*z;g=y-b
 assert min(a,b,f,g)>=0
 out={sig:[] for sig in REQ[h]}
 for c in range(b+1):
  m={'a':a,'c':c,'d':b-c,'e':z,'f':f,'g':g}
  def visit(word,state):
   if len(word)==h:
    if SIG[state] in out:out[SIG[state]].append(word)
    return
   for k,op in enumerate(OPS):
    if m[op] and T[state][k]!=8:
     m[op]-=1;visit(word+op,T[state][k]);m[op]+=1
  visit('',0)
 return out

def build():
 t=time.perf_counter()
 chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
 early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
 late=[f'{h}:{s}' for h in (7,8,9) for s in REQ[h]]
 pools={}
 for h in range(4,10):
  for sig,words in candidates(h).items():
   pools[f'{h}:{sig}']=words
   assert chosen[f'{h}:{sig}'] in words
 allwords=set(chosen.values())|{w for p in pools.values() for w in p}
 prefs={w:primpref(w) for w in allwords}
 prefix_ids={p:i for i,p in enumerate(sorted({p for ps in prefs.values() for p in ps}))}
 bits={w:sum(1<<prefix_ids[p] for p in prefs[w]) for w in allwords}
 witness=0
 for w in chosen.values():witness|=bits[w]
 assert witness.bit_count()==158
 masks={key:[bits[w] for w in words] for key,words in pools.items()}
 single={key:bits[w] for key,w in chosen.items()}
 print('BUILT',len(allwords),len(prefix_ids),'time',round(time.perf_counter()-t,2),flush=True)
 return chosen,early,late,masks,single
