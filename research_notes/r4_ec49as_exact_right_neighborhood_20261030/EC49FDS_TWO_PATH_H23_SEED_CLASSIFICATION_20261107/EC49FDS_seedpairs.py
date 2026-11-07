#!/usr/bin/env python3
"""Exact H2/H3 two-path rank-nine signed-native seed census.
Frozen EC49 input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json,itertools
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
PRIM={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
LETTERS='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)
def steps(w):return tuple(s for c in w for s in PRIM[c])
def key(w):return tuple(steps(w).count(v) for v in (1,2,3))
def pref(w):
 s=steps(w);return {s[:i] for i in range(1,len(s)+1)}
def language(h):
 out=[]
 for w in itertools.product(LETTERS,repeat=h):
  w=''.join(w);s=steps(w)
  if any(s.count(i)-s.count(-i)!=(2 if i==1 else 0) for i in (1,2,3)):continue
  state=0
  for c in w:state=TRANS[state][LETTERS.index(c)]
  if SIG[state] in (1,2,4,8,16,32):out.append((w,SIG[state]))
 return out
def rank_ok(sigs):return all(any(s&clause for s in sigs) for clause in CLAUSES)
a,b=language(2),language(3)
a2=[v for v in itertools.combinations(a,2) if rank_ok([x[1] for x in v])]
b2=[v for v in itertools.combinations(b,2) if rank_ok([x[1] for x in v])]
res=[]
for aa in a2:
 for bb in b2:
  ws=[x[0] for x in aa+bb];ks=tuple(sorted({key(w) for w in ws}))
  pn=len(set().union(*(pref(w) for w in ws)))
  res.append({'H2':sorted(w for w,s in aa),'H3':sorted(w for w,s in bb),'keys':[list(k) for k in ks], 'num_keys':len(ks),'prefix_edges':pn,'sigs':[x[1] for x in aa+bb]})
minby={}
for r in res:
 k=r['num_keys']
 if k not in minby or r['prefix_edges']<minby[k]['edges']:minby[k]={'edges':r['prefix_edges'],'witness':r,'count':0}
for k,v in minby.items():v['count']=sum(x['num_keys']==k and x['prefix_edges']==v['edges'] for x in res)
thresholds={str(t):{str(k):sum(x['prefix_edges']<=t and x['num_keys']==k for x in res) for k in range(1,6)} for t in (16,20,24,28,31,42)}
keysets={}
for r in res:
 if r['prefix_edges']<=31:
  label=str(r['keys']);d=keysets.setdefault(label,{'keys':r['keys'],'min_edges':r['prefix_edges'],'count':0,'witness':r})
  d['count']+=1
  if r['prefix_edges']<d['min_edges']:d['min_edges']=r['prefix_edges'];d['witness']=r
out={'science_pin':PIN,'scope':'exactly two distinct permitted words each at H2 and H3, rank 9 at both horizons, charged native signed primitive prefix edges','H2_accepted_words':len(a),'H3_accepted_words':len(b),'H2_rank9_pairs':len(a2),'H3_rank9_pairs':len(b2),'joint_rank9_seed_pairs':len(res),'min_by_exact_key_count':{str(k):v for k,v in sorted(minby.items())},'threshold_count':thresholds,'keysets_at_most_31':sorted(keysets.values(),key=lambda d:(d['min_edges'],d['keys'])),'all_rank9_seed_pairs':res}
if __name__=='__main__':print(json.dumps(out,ensure_ascii=False,indent=2))
