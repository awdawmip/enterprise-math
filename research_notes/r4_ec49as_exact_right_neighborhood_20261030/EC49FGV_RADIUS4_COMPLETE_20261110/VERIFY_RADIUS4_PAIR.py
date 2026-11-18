#!/usr/bin/env python3
"""Exact two-label necessary screen for four-path changes, frozen seven keys.
Input is the singleton screen output and the immutable EC49FGJ A/B witness.
"""
import json,collections,itertools,time
from pathlib import Path
from model_ec49fgv import words,REQ,STEPS
from VERIFY_RADIUS4_SINGLETON import native_prefix
P=Path(__file__).parent
D=json.loads((P/'EC49FGJ_SEVEN_KEY_94_WITNESSES.json').read_text())
S=json.loads((P/'EXACT_EC49FGT_SINGLETON.json').read_text())
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert D['frozen_scientific_pin']==PIN

def make_trie(keys):
 nodes=[[b'',{},set()]]
 for h in REQ:
  for key in sorted(keys):
   for sig,w in words(h,key):
    at=0
    for p in native_prefix(w):
     if p not in nodes[at][1]:
      nodes[at][1][p]=len(nodes);nodes.append([p,{},set()])
     at=nodes[at][1][p]
    nodes[at][2].add((h,sig))
 return nodes

def joint_possible(A,B,budget):
 for a in A:
  if len(a)>budget:continue
  for b in B:
   if max(len(a),len(b))>budget:continue
   if len(a|b)<=budget:return True
 return False

def screen(pr,single):
 rows=sorted(pr['demands'],key=lambda d:(d['window'],d['signature']))
 labels=[(d['window'],d['signature']) for d in rows]
 path=[set(native_prefix(d['word'])) for d in rows]
 keys=set()
 for d in rows:
  pp=[a for c in d['word'] for a in STEPS[c]]
  keys.add(tuple(pp.count(x) for x in (1,2,3)))
 assert len(keys)==7
 nodes=make_trie(keys)
 ctr=collections.Counter();remaining=[]
 for entry in single['retained']:
  Q=tuple(entry['quad']);select=set(labels[i] for i in Q)
  if select=={(8,s) for s in (1,2,4,8)}:
   ctr['exception_non_fixed_key']+=1;continue
  fixed=set().union(*(path[i] for i in range(24) if i not in Q))
  budget=93-len(fixed);assert budget==entry['B']
  choices=collections.defaultdict(set)
  stack=[(0,frozenset())]
  while stack:
   k,missing=stack.pop()
   pref,children,term=nodes[k]
   if term:
    for lab in term & select:choices[lab].add(missing)
   for pref2,nid in children.items():
    if pref2 in fixed:stack.append((nid,missing))
    elif len(missing)<budget:stack.append((nid,missing|{nid}))
  if any(lab not in choices for lab in select):
   ctr['singleton_fail']+=1;continue
  bad=False
  for a,b in itertools.combinations(sorted(select),2):
   if not joint_possible(choices[a],choices[b],budget):
    bad=True;break
  if bad:
   ctr['pair_fail']+=1;ctr['rejected_B_'+str(budget)]+=1
  else:
   ctr['survive']+=1;ctr['survive_B_'+str(budget)]+=1
   remaining.append({'quad':Q,'B':budget,'labels':sorted(select)})
 assert ctr['singleton_fail']==0
 assert ctr['exception_non_fixed_key']==1
 return {'profile':pr['profile_id'],'trie_nodes':len(nodes),
         'singleton_survivors':len(single['retained']),
         'count':dict(ctr),'remaining':remaining}

if __name__=='__main__':
 out={'schema':'EC49FGV_PAIR_RADIUS4_V1','frozen_pin':PIN,
      'profiles':[screen(p,s) for p,s in zip(D['profiles'],S['profiles'])]}
 assert [x['count']['pair_fail'] for x in out['profiles']]==[2273,2275]
 assert [x['count']['survive'] for x in out['profiles']]==[460,458]
 (P/'EXACT_EC49FGU_PAIR.json').write_text(json.dumps(out,indent=2)+'\n')
 print('EC49FGV_PAIR_PASS',[(x['profile'],x['trie_nodes'])
                          for x in out['profiles']])
