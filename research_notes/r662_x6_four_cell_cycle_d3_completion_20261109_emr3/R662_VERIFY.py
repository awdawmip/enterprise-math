#!/usr/bin/env python3
"""R662: X6 four-cell square completion for the R661 endpoint-local V29/V27/V17 transducer."""
from itertools import combinations, permutations, product
from collections import Counter
import json
from pathlib import Path

PASS_EDGES=((0,1),(2,0),(2,3),(3,0))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
TRIADS=tuple(combinations(range(6),3))
NEI={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
def code(s):
 z=set(s)
 return tuple(0 if any(((a in z)+(b in z))!=1 for a,b in m)
              else (1 if sum(b in z for a,b in m)%2==0 else -1) for m in MATCH)
C={s:code(s) for s in TRIADS}
assert len(set(C.values()))==20
def signed(seed):
 m=[[0]*4 for _ in range(4)]
 for (a,b),v in zip(PASS_EDGES,seed):m[a][b]+=v
 return tuple(tuple(m[i][j]-m[j][i] for j in range(4)) for i in range(4))
OMEGA={seed:signed(seed) for seed in product(range(4),repeat=4)}
def choose(seed,rin,rout,s):
 om=OMEGA[seed];u=[sum(om[i])+rin[i]-rout[i] for i in range(4)]
 def score(t):
  return sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*om[i][j]*C[t][j] for i in range(4) for j in range(4))
 ranked=sorted(((score(t),t) for t in NEI[s]),reverse=True)
 gap=ranked[0][0]-ranked[1][0]
 return (ranked[0][1],gap) if gap>0 else (None,gap)
def transport(old,new,slots):
 out=dict(zip(old,slots))
 leaving=next(iter(set(old)-set(new)))
 entering=next(iter(set(new)-set(old)))
 out[entering]=out[leaving]
 return tuple(out[t] for t in new)
def run(seeds,word,trace=False):
 n=len(seeds);rin=[[0]*4 for _ in range(n)];rout=[[0]*4 for _ in range(n)]
 triads=[(0,1,2)]*n;slots=[(0,1,2)]*n;pairs=Counter();rows=[]
 for x,a,y,b in word:
  assert x!=y and 0<=a<4 and 0<=b<4
  rout[x][a]+=1;rin[y][b]+=1;pairs[(x,a,y,b)]+=1
  assert sum(map(sum,rin))==sum(map(sum,rout))
  row={'event':(x,a,y,b)}
  for i in (x,y):
   nxt,gap=choose(seeds[i],rin[i],rout[i],triads[i])
   if nxt is None:return None
   slots[i]=transport(triads[i],nxt,slots[i]);triads[i]=nxt
   row[str(i)]={'triad':nxt,'slots':slots[i],'gap':gap}
  rows.append(row)
 return {'triads':tuple(triads),'slots':tuple(slots),
  'rin':tuple(map(tuple,rin)),'rout':tuple(map(tuple,rout)),
  'pairs':tuple(sorted((*k,v) for k,v in pairs.items())),
  'trace':rows if trace else None}
def compose(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
def parity(a):return sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))%2

S=((3,3,3,3),(2,0,1,1),(3,3,3,3),(3,3,3,3))
e=(0,0,1,2);f=(1,0,2,0);g=(1,1,2,0)
A=(e,f,g);B=(f,e,g)
IDENT=(0,1,2);RHO=(1,2,0);TARGET=(IDENT,RHO,IDENT,IDENT)
stats={'port_pairs':0,'both_strict':0,'same_triads_parity':0,'same_ledgers_pairs':0,'relative_D3_exact':0}
witness=None
for a,b,c,d in product(range(4),repeat=4):
 h=(2,a,3,b);k=(3,c,0,d)
 x=run(S,A+(h,k),True);y=run(S,B+(h,k),True)
 stats['port_pairs']+=1
 if x is None or y is None:continue
 stats['both_strict']+=1
 if x['triads']==y['triads'] and all(parity(v)==parity(w) for v,w in zip(x['slots'],y['slots'])):
  stats['same_triads_parity']+=1
 if all(x[z]==y[z] for z in ('rin','rout','pairs')):
  stats['same_ledgers_pairs']+=1
 delta=tuple(compose(y['slots'][i],inv(x['slots'][i])) for i in range(4))
 if delta==TARGET:stats['relative_D3_exact']+=1
 if witness is None:witness={'h':h,'k':k,'history_A':x,'history_B':y,'delta':delta}
assert stats==dict.fromkeys(stats,256)
assert witness['h']==(2,0,3,0) and witness['k']==(3,0,0,0)
assert witness['history_A']['triads']==witness['history_B']['triads']==((1,2,4),(0,3,4),(0,1,2),(1,2,4))
assert witness['history_A']['slots']==((0,2,1),(0,2,1),(1,0,2),(0,2,1))
assert witness['history_B']['slots']==((0,2,1),(1,0,2),(1,0,2),(0,2,1))
for gamma in permutations(IDENT):
 assert compose(compose(witness['history_B']['slots'][1],gamma),
      inv(compose(witness['history_A']['slots'][1],gamma)))==RHO
four=tuple(permutations((e,f,witness['h'],witness['k'])))
valid=[(w,run(S,w)) for w in four]
assert all(v is not None for _,v in valid)
control_pairs=0
for (wa,va),(wb,vb) in combinations(valid,2):
 if va['triads']==vb['triads'] and all(parity(a)==parity(b) for a,b in zip(va['slots'],vb['slots'])) and va['slots']!=vb['slots']:
  control_pairs+=1
assert control_pairs==0
marker='R662_X6_FOUR_CELL_CYCLE_D3_COMPLETION_EXACT_PASS'
evidence={'marker':marker,'scope':'conditional H; X6 four-cell square endpoint-local strict V29/V27/V17',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d',
 'cell_raw_X6':[(0,0,0,0,0,0),(1,0,0,0,0,0),(1,1,0,0,0,0),(0,1,0,0,0,0)],
 'seeds':S,'events':{'e':e,'f':f,'g':g,'h':witness['h'],'k':witness['k'],
 'A':A+(witness['h'],witness['k']),'B':B+(witness['h'],witness['k'])},
 'stats':stats,'witness':witness,'control':{'four_distinct_edge_strict_words':len(valid),'collisions':control_pairs},
 'S3_common_right_updates_tested':6,'Q_zero_every_prefix':True,
 'status':'AUTHOR_SIDE_EXACT; DRIVER_UNREVIEWED'}
Path(__file__).with_name('R662_EVIDENCE_RECOMPUTED.json').write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(marker,json.dumps(stats,sort_keys=True),'control',len(valid),control_pairs)
