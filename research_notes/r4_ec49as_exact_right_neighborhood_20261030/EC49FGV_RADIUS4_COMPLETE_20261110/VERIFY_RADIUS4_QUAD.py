#!/usr/bin/env python3
"""Exact four-label feasibility search for the radius-four BRC problem.

After the complete singleton and pair stages, check all remaining four-label
positions with the same seven-key domain (excluding the special H8 case,
previously proved even without a key limit by EC49FGM). All arithmetic exact.
Usage: python VERIFY_RADIUS4_QUAD.py 0   # A
       python VERIFY_RADIUS4_QUAD.py 1   # B
"""
import json,collections,itertools,time,sys
from pathlib import Path
from model_ec49fgv import words,REQ,STEPS,check
from VERIFY_RADIUS4_SINGLETON import native_prefix
ROOT=Path(__file__).parent
W=json.loads((ROOT/'EC49FGJ_SEVEN_KEY_94_WITNESSES.json').read_text())
R=json.loads((ROOT/'EXACT_EC49FGU_PAIR.json').read_text())
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert W['frozen_scientific_pin']==PIN

def indexed_trie(keys):
 nodes=[[b'',{},[]]]
 for h in REQ:
  for key in sorted(keys):
   for sig,w in words(h,key):
    at=0
    for p in native_prefix(w):
     if p not in nodes[at][1]:
      nodes[at][1][p]=len(nodes)
      nodes.append([p,{},[]])
     at=nodes[at][1][p]
    nodes[at][2].append(((h,sig),w))
 return nodes

def prune_dominated(dic):
 # Same label, exact delta sets: a subset dominates any strict superset.
 ar=sorted(dic,key=lambda s:(len(s),tuple(sorted(s))))
 kept={}
 for s in ar:
  if not any(k<=s for k in kept):kept[s]=dic[s]
 return kept

def four_way(choices,B):
 ordered=sorted(choices,key=lambda label:len(choices[label]))
 memo=set();stats=collections.Counter()
 def dfs(i,cover,words0):
  stats['visited']+=1
  if i==4:return words0
  key=(i,cover)
  if key in memo:return None
  lab=ordered[i]
  for diff,w in sorted(choices[lab].items(),key=lambda x:len(x[0]-cover)):
   new=cover|diff
   if len(new)>B:continue
   if any(not any(len(new|cand)<=B for cand in choices[nextlabel])
          for nextlabel in ordered[i+1:]):continue
   sol=dfs(i+1,new,{**words0,lab:w})
   if sol is not None:return sol
  memo.add(key)
  return None
 return dfs(0,frozenset(),{}),dict(stats)

def work(pr,res):
 start=time.time()
 rows=sorted(pr['demands'],key=lambda r:(r['window'],r['signature']))
 path=[set(native_prefix(x['word'])) for x in rows]
 labels=[(x['window'],x['signature']) for x in rows]
 keyset=set()
 for r in rows:
  p=[a for c in r['word'] for a in STEPS[c]]
  keyset.add(tuple(p.count(k) for k in (1,2,3)))
 trie=indexed_trie(keyset)
 counts=collections.Counter();cases=[];full_witnesses=[]
 for i,item in enumerate(res['remaining']):
  Q=tuple(item['quad']);sel=set(labels[j] for j in Q)
  F=set.union(*(path[j] for j in range(24) if j not in Q))
  B=93-len(F)
  assert item['B']==B
  choices=collections.defaultdict(dict)
  stack=[(0,frozenset())]
  while stack:
   ix,missing=stack.pop()
   _,children,term=trie[ix]
   if term:
    for lab,w in term:
     if lab in sel:choices[lab].setdefault(missing,w)
   for prefix,nid in children.items():
    if prefix in F:stack.append((nid,missing))
    elif len(missing)<B:stack.append((nid,missing|{nid}))
  assert sel==set(choices)
  choices={l:prune_dominated(choices[l]) for l in sel}
  answer,stats=four_way(choices,B)
  if answer is None:
   counts['no_93']+=1;counts['no_93_B_'+str(B)]+=1
  else:
   counts['has_93']+=1;counts['has_93_B_'+str(B)]+=1
   nw=[(lab[0],lab[1],answer[lab]) if lab in answer
       else (lab[0],lab[1],rows[j]['word'])
       for j,lab in enumerate(labels)]
   total,keys=check(nw)
   assert total<=93 and len(keys)<=7
   full_witnesses.append({'quad':list(Q),'cost':total,'keys':keys,
    'words':[{'window':h,'signature':s,'word':w} for h,s,w in nw]})
  cases.append({'quad':list(Q),'B':B,
    'status':'FEASIBLE' if answer else 'INFEASIBLE',
    'visited':stats['visited'],
    'choices':[len(choices[lab]) for lab in sorted(sel)]})
  if (i+1)%50==0:
   print(pr['profile_id'],i+1,'/',len(res['remaining']),
         dict(counts),'elapsed',round(time.time()-start,1),flush=True)
 return {'profile':pr['profile_id'],'cases_checked':len(cases),
         'summary':dict(counts),'cases':cases,'witnesses':full_witnesses}

if __name__=='__main__':
 idx=int(sys.argv[1]) if len(sys.argv)>1 else 0
 out=work(W['profiles'][idx],R['profiles'][idx])
 assert out['summary'].get('has_93',0)==0
 assert out['cases_checked']==(460 if idx==0 else 458)
 (ROOT/f'EXACT_EC49FGV_QUAD_{out["profile"]}.json').write_text(
   json.dumps(out,indent=2)+'\n')
 print('EC49FGV_QUAD_PASS',out['profile'],out['cases_checked'])
