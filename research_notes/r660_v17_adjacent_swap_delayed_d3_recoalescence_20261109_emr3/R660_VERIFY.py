#!/usr/bin/env python3
"""R660 exact frozen V23/V27/V29/V17 adjacent-swap memory verifier."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path
B=((0,1),(2,0),(2,3),(3,0))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
TRIADS=tuple(combinations(range(6),3))
NEI={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
EVENTS=tuple((i,i) for i in range(4))
Y_SEED=(3,3,3,3)
def code(s):
 z=set(s)
 return tuple(0 if any(((a in z)+(b in z))!=1 for a,b in m) else (1 if sum(b in z for a,b in m)%2==0 else -1) for m in MATCH)
C={s:code(s) for s in TRIADS}
assert len(set(C.values()))==20
def signed(seed):
 M=[[0]*4 for _ in range(4)]
 for (a,b),count in zip(B,seed):M[a][b]+=count
 return [[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
@lru_cache(None)
def choose(seed,history,side,s):
 omega=signed(seed)
 u=[sum(omega[i]) for i in range(4)]
 for a,b in history:
  u[a if side=='x' else b]+=-1 if side=='x' else 1
 def score(t):
  return sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*omega[i][j]*C[t][j] for i in range(4) for j in range(4))
 ranked=sorted(((score(t),t) for t in NEI[s]),reverse=True)
 gap=ranked[0][0]-ranked[1][0]
 return (ranked[0][1],gap) if gap>0 else (None,gap)
def insert_slot(old,new,slots):
 leaving=next(iter(set(old)-set(new)))
 old_slot=dict(zip(old,slots))
 incoming=next(iter(set(new)-set(old)))
 old_slot[incoming]=old_slot[leaving]
 return tuple(old_slot[t] for t in new)
def run(xseed,yseed,word,trace=False):
 triads={'x':(0,1,2),'y':(0,1,2)}
 slots={'x':(0,1,2),'y':(0,1,2)}
 rows=[]
 for k in range(len(word)):
  event_history=word[:k+1];row={'event':list(word[k])}
  for side,seed in [('x',xseed),('y',yseed)]:
   nxt,gap=choose(seed,event_history,side,triads[side])
   if nxt is None:return None
   slots[side]=insert_slot(triads[side],nxt,slots[side]);triads[side]=nxt
   row[side]={'triad':list(nxt),'slots':list(slots[side]),'gap':gap}
  rows.append(row)
 end=(triads['x'],slots['x'],triads['y'],slots['y'])
 return (end,rows) if trace else end
def parity(s):
 return sum(s[i]>s[j] for i in range(3) for j in range(i+1,3))%2
def compose(a,b):
 return tuple(a[b[i]] for i in range(3))
def inverse(a):
 return tuple(a.index(i) for i in range(3))
stats=[]
for n in range(4):
 total=strict=collisions=0;max_fiber=0
 for xseed in product(range(4),repeat=4):
  groups=defaultdict(dict)
  for word in product(EVENTS,repeat=n):
   total+=1;out=run(xseed,Y_SEED,word)
   if out is None:continue
   strict+=1;tx,sx,ty,sy=out
   key=(tuple(sorted(word)),tx,parity(sx),ty,parity(sy))
   groups[key][word]=(sx,sy)
  for group in groups.values():
   items=list(group.items())
   for i in range(len(items)):
    for j in range(i+1,len(items)):
     if items[i][1]!=items[j][1]:collisions+=1
   max_fiber=max(max_fiber,len(set(group.values())))
 stats.append({'length':n,'total_words':total,'strict_words':strict,'same_summary_different_slot_pairs':collisions,'maximum_full_slot_fiber':max_fiber})
assert [s['total_words'] for s in stats]==[256,1024,4096,16384]
assert [s['strict_words'] for s in stats]==[256,560,1634,5501]
assert [s['same_summary_different_slot_pairs'] for s in stats]==[0,0,0,21]
assert [s['maximum_full_slot_fiber'] for s in stats]==[1,1,1,2]
X_SEED=(2,0,0,0)
A=(EVENTS[2],EVENTS[3],EVENTS[0])
BW=(EVENTS[3],EVENTS[2],EVENTS[0])
ra=run(X_SEED,Y_SEED,A,trace=True);rb=run(X_SEED,Y_SEED,BW,trace=True)
assert ra and rb
assert ra[0]==((3,4,5),(0,2,1),(0,1,2),(1,0,2))
assert rb[0]==((3,4,5),(1,0,2),(0,1,2),(1,0,2))
assert [[r[c]['gap'] for r in ra[1]] for c in ('x','y')]==[[1,1,1],[3,1,9]]
assert [[r[c]['gap'] for r in rb[1]] for c in ('x','y')]==[[1,1,1],[3,1,9]]
assert ra[1][1]['x']['triad']!=rb[1][1]['x']['triad']
assert ra[1][2]['x']['triad']==rb[1][2]['x']['triad']
assert ra[0][2:]==rb[0][2:]
assert parity(ra[0][1])==parity(rb[0][1])==1
delta=compose(rb[0][1],inverse(ra[0][1]))
assert delta==(1,2,0) and compose(delta,ra[0][1])==rb[0][1]
assert sorted(A)==sorted(BW)
evidence={'marker':'R660_THREE_STEP_ADJACENT_SWAP_DELAYED_D3_RECOALESCENCE_PASS','frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f','operators':'V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d','model':'two X6 Cells, four typed PF10 ports; auxiliary event-first strict signed V27 then V17','finite_domain':{'x_seed_counts':[0,1,2,3],'y_seed':list(Y_SEED),'alphabet':[list(e) for e in EVENTS],'lengths':[0,1,2,3]},'coverage':stats,'witness':{'x_seed':list(X_SEED),'y_seed':list(Y_SEED),'word_A':A,'word_B':BW,'end_A':ra[0],'end_B':rb[0],'trace_A':ra[1],'trace_B':rb[1],'relative_D3_delta':delta,'same_full_ledger_and_pair_histogram':True,'first_triad_recoalescence_after_event':3},'scope':'auxiliary model exact; minimum only for declared finite domain; not yet native V28/V30 verified','review':'AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('R660_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(evidence['marker'],stats,delta)
