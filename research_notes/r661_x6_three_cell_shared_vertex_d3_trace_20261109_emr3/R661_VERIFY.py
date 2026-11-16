#!/usr/bin/env python3
"""R661 exact 3-cell endpoint-local signed V27/V29/V17 verifier (standard library)."""
from itertools import combinations, product
from collections import defaultdict
import json
from pathlib import Path

B=((0,1),(2,0),(2,3),(3,0))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
TRIADS=tuple(combinations(range(6),3))
NEI={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
def code(s):
 z=set(s)
 return tuple(0 if any(((a in z)+(b in z))!=1 for a,b in m) else (1 if sum(b in z for a,b in m)%2==0 else -1) for m in MATCH)
C={s:code(s) for s in TRIADS}
assert len(set(C.values()))==20
def signed(seed):
 M=[[0]*4 for _ in range(4)]
 for (a,b),count in zip(B,seed):M[a][b]+=count
 return tuple(tuple(M[i][j]-M[j][i] for j in range(4)) for i in range(4))
OMEGA_CACHE={seed:signed(seed) for seed in product(range(4),repeat=4)}
def choose(seed,rin,rout,s):
 om=OMEGA_CACHE[seed]
 u=[sum(om[i])+rin[i]-rout[i] for i in range(4)]
 def score(t):
  return sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*om[i][j]*C[t][j] for i in range(4) for j in range(4))
 ranked=sorted(((score(t),t) for t in NEI[s]),reverse=True)
 gap=ranked[0][0]-ranked[1][0]
 return (ranked[0][1],gap) if gap>0 else (None,gap)
def insert_slot(old,new,slots):
 leaving=next(iter(set(old)-set(new)))
 old_slot=dict(zip(old,slots))
 incoming=next(iter(set(new)-set(old)))
 old_slot[incoming]=old_slot[leaving]
 return tuple(old_slot[t] for t in new)
def run(seeds,word,trace=False):
 n=len(seeds)
 rin=[[0]*4 for _ in range(n)]
 rout=[[0]*4 for _ in range(n)]
 triads=[(0,1,2)]*n
 slots=[(0,1,2)]*n
 rows=[]
 pairs=defaultdict(int)
 for (x,a,y,b) in word:
  assert x!=y and 0<=x<n and 0<=y<n and 0<=a<4 and 0<=b<4
  rout[x][a]+=1
  rin[y][b]+=1
  pairs[(x,a,y,b)]+=1
  row={'event':(x,a,y,b)}
  for i in (x,y):
   nxt,gap=choose(seeds[i],rin[i],rout[i],triads[i])
   if nxt is None: return None
   slots[i]=insert_slot(triads[i],nxt,slots[i])
   triads[i]=nxt
   row[str(i)]={'triad':nxt,'slots':slots[i],'gap':gap}
  rows.append(row)
 end={'triads':tuple(triads),'slots':tuple(slots),
      'rin':tuple(tuple(r) for r in rin),
      'rout':tuple(tuple(r) for r in rout),
      'pair_counts':tuple(sorted((*k,v) for k,v in pairs.items()))}
 return (end,rows) if trace else end
def compose(a,b):return tuple(a[b[i]] for i in range(3))
def inverse(a):return tuple(a.index(i) for i in range(3))
def parity(s):return sum(s[i]>s[j] for i in range(3) for j in range(i+1,3))%2

SEEDS=((3,3,3,3),(2,0,1,1),(3,3,3,3))
e=(0,0,1,2);f=(1,0,2,0);g=(1,1,2,0)
A=(e,f,g);D=(f,e,g)
a,trace_a=run(SEEDS,A,True)
d,trace_d=run(SEEDS,D,True)
assert a['triads']==d['triads']==((0,2,4),(0,3,4),(1,2,4))
assert a['slots']==((0,2,1),(0,2,1),(0,2,1))
assert d['slots']==((0,2,1),(1,0,2),(0,2,1))
assert a['rin']==d['rin'] and a['rout']==d['rout'] and a['pair_counts']==d['pair_counts']
assert all(parity(x)==parity(y) for x,y in zip(a['slots'],d['slots']))
delta=compose(d['slots'][1],inverse(a['slots'][1]))
assert delta==(1,2,0) and compose(delta,compose(delta,delta))==(0,1,2)
assert all(v['gap']>0 for rows in (trace_a,trace_d) for row in rows for k,v in row.items() if k!='event')
assert trace_a[1]['1']['triad']!=trace_d[1]['1']['triad']
# Disjoint supports: swap exact equality on all full state fields.
seeds4=((3,3,3,3),)*4
h=(0,0,1,0);k=(2,1,3,1)
full_a=run(seeds4,(h,k),True)
full_b=run(seeds4,(k,h),True)
assert full_a and full_b and full_a[0]==full_b[0]

stats={'tested':0,'both_strict':0,'same_triads':0,'same_triads_same_parity':0,
       'same_triads_same_parity_different_slots':0,'nontrivial_even_D3_center':0}
for seed in product(range(4),repeat=4):
 seeds=((3,3,3,3),seed,(3,3,3,3))
 for b,c in product(range(4),repeat=2):
  e0=(0,0,1,b);f0=(1,c,2,0)
  for j in range(4):
   for side in (0,1):
    g0=(0,0,1,j) if side==0 else (1,j,2,0)
    if g0 in (e0,f0):continue
    r=run(seeds,(e0,f0,g0))
    s=run(seeds,(f0,e0,g0))
    stats['tested']+=1
    if r is None or s is None:continue
    stats['both_strict']+=1
    if r['triads']!=s['triads']:continue
    stats['same_triads']+=1
    if any(parity(x)!=parity(y) for x,y in zip(r['slots'],s['slots'])):continue
    stats['same_triads_same_parity']+=1
    if r['slots']!=s['slots']:
     stats['same_triads_same_parity_different_slots']+=1
     dt=compose(s['slots'][1],inverse(r['slots'][1]))
     if dt in ((1,2,0),(2,0,1)):stats['nontrivial_even_D3_center']+=1
assert stats=={'tested':24576,'both_strict':4366,'same_triads':4026,
 'same_triads_same_parity':3986,'same_triads_same_parity_different_slots':6,
 'nontrivial_even_D3_center':6}
short={'tested':0,'both_strict':0,'same_triads_same_parity_different_slots':0}
for seed in product(range(4),repeat=4):
 seeds=((3,3,3,3),seed,(3,3,3,3))
 for b,c in product(range(4),repeat=2):
  e0=(0,0,1,b);f0=(1,c,2,0)
  r=run(seeds,(e0,f0));s=run(seeds,(f0,e0))
  short['tested']+=1
  if r is None or s is None:continue
  short['both_strict']+=1
  if r['triads']==s['triads'] and all(parity(x)==parity(y) for x,y in zip(r['slots'],s['slots'])) and r['slots']!=s['slots']:
   short['same_triads_same_parity_different_slots']+=1
assert short=={'tested':4096,'both_strict':855,'same_triads_same_parity_different_slots':0}
for W in (A,D):
 rr=[[0]*4 for _ in range(3)]
 oo=[[0]*4 for _ in range(3)]
 for x,aa,y,bb in W:
  oo[x][aa]+=1;rr[y][bb]+=1
  assert sum(map(sum,rr))==sum(map(sum,oo))
marker='R661_THREE_CELL_SHARED_VERTEX_D3_TRACE_EXACT_PASS'
evidence={'marker':marker,'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
          'scope':'3-cell endpoint-local auxiliary transducer with H explicitly conditional',
          'seeds':SEEDS,'events':{'e':e,'f':f,'g':g,'A':A,'B':D},
          'A':{'end':a,'trace':trace_a},'B':{'end':d,'trace':trace_d},
          'relative_center_D3':delta,'finite_three_event_scan':stats,
          'finite_two_event_scan':short,'disjoint_support_commutes':True,
          'Q_conserved_all_prefixes':True,'review':'AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('R661_EVIDENCE_RECOMPUTED.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(marker,stats,short)
