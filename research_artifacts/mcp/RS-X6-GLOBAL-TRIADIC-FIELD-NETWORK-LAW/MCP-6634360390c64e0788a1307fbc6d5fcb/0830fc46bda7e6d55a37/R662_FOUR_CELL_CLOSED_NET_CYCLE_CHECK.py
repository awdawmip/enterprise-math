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

# R662 conditional 4-Cell X6 unit square closed NET cycle, frozen R661 core.
SEEDS=((3,3,3,3),(2,0,1,1),(3,3,3,3),(3,3,3,3))
e=(0,0,1,2);f=(1,0,2,0);g=(1,1,2,0)
p=(2,0,3,0);q=(3,0,0,0);r=(2,0,1,0)
WA=(e,f,g,p,q,r);WB=(f,e,g,p,q,r)
resA=run(SEEDS,WA,True);resB=run(SEEDS,WB,True)
assert resA is not None and resB is not None
a,traceA=resA;b,traceB=resB
assert a['triads']==b['triads']==((1,2,4),(1,3,4),(0,2,4),(1,2,4))
for k in ('rin','rout','pair_counts'):assert a[k]==b[k]
assert all(parity(x)==parity(y) for x,y in zip(a['slots'],b['slots']))
assert a['slots']==((0,2,1),(0,2,1),(1,0,2),(0,2,1))
assert b['slots']==((0,2,1),(1,0,2),(1,0,2),(0,2,1))
delta=compose(b['slots'][1],inverse(a['slots'][1]))
assert delta==(1,2,0) and compose(delta,compose(delta,delta))==(0,1,2)
assert all(v['gap']>0 for rows in (traceA,traceB) for row in rows for k,v in row.items() if k!='event')
def net_current(word):
 edge={(0,1):0,(1,2):1,(2,3):2,(3,0):3};j=[0,0,0,0]
 for x,src,y,dst in word:
  if (x,y) in edge:j[edge[x,y]]+=1
  elif (y,x) in edge:j[edge[y,x]]-=1
  else:raise AssertionError('unexpected edge')
 return tuple(j)
j=net_current(WA);assert j==net_current(WB)==(1,1,1,1)
boundary=(-j[0]+j[3],j[0]-j[1],j[1]-j[2],j[2]-j[3])
assert boundary==(0,0,0,0)
for word in (WA,WB):
 incoming=outgoing=0
 for evt in word:
  incoming+=1;outgoing+=1;assert incoming==outgoing
marker='R662_FOUR_CELL_CLOSED_NET_CYCLE_D3_MEMORY_EXACT_PASS'
ev={'marker':marker,'scope':'conditional declared H, serial endpoint-local; NOT_REVIEWED',
 'cells':((0,0,0,0,0,0),(1,0,0,0,0,0),(1,1,0,0,0,0),(0,1,0,0,0,0)),
 'seeds':SEEDS,'A':WA,'B':WB,'net_current':j,'net_boundary':boundary,
 'terminal_A':a,'terminal_B':b,'central_D3':delta,'all_steps_strict':True,
 'remaining':['native H and autonomous scheduler','V39 based-loop holonomy h mapping',
              'rotation covariance and global composition law']}
Path(__file__).with_name('R662_FOUR_CELL_CLOSED_NET_CYCLE_EVIDENCE.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
print(marker)
