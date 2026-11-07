"""EC49FDF independent-key census. Run from this folder: python VERIFY_EC49FDF.py.
Frozen scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Requires unmodified sibling EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py,
Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.
"""
import sys,json,hashlib
from pathlib import Path
from functools import lru_cache
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128'))
import frozen_model as fm
REQ={h:fm.REQ[h] for h in range(4,10)}
LABELS=[(h,s) for h in REQ for s in REQ[h]]
FIXED=('fe','ge','feg','gef')
F=set().union(*(set(fm.primpref(w)) for w in FIXED))
assert len(F)==16

def key_list(lo,hi):
 return [(x,y,z) for z in range(1,(lo+1)//2+1)
         for y in range(lo+2) for x in range(lo+2)
         if x+y>=hi+1 and x<=lo+1 and y+2*z<=lo+1]
L_KEYS=key_list(4,5); M_KEYS=key_list(6,9)
assert len(L_KEYS)==len(M_KEYS)==7

@lru_cache(None)
def cand(h,key):
 x,y,z=key; b=x+y-h-1;a=z-1;f=x-b-2*z;g=y-b
 if min(a,b,f,g)<0:return {s:() for s in REQ[h]}
 pools={s:[] for s in REQ[h]}
 for c in range(b+1):
  remain={'a':a,'c':c,'d':b-c,'e':z,'f':f,'g':g}
  def dfs(word,state):
   if len(word)==h:
    if fm.SIG[state] in pools:pools[fm.SIG[state]].append(word)
    return
   for j,op in enumerate(fm.OPS):
    if remain[op] and fm.T[state][j]!=8:
     remain[op]-=1;dfs(word+op,fm.T[state][j]);remain[op]+=1
  dfs('',0)
 return {s:tuple(v) for s,v in pools.items()}

def solve(L,M,fix_early=True):
 children=[{}];ends=[0];edge=[0];nw=0
 for i,(h,s) in enumerate(LABELS):
  for w in cand(h,L if h<=5 else M)[s]:
   nw+=1;v=0
   for prefix in fm.primpref(w):
    a=prefix[-1];nxt=children[v].get(a)
    if nxt is None:
     nxt=len(children);children[v][a]=nxt
     children.append({});ends.append(0);edge.append(int(prefix not in F) if fix_early else 1)
    v=nxt
   ends[v]|=1<<i
 dp=[None]*len(children);checks=good=0
 for v in range(len(children)-1,-1,-1):
  mask=ends[v];states={};sub=mask
  while True:
   states[sub]=0
   if not sub:break
   sub=(sub-1)&mask
  for child in children[v].values():
   update={};ec=edge[child]
   for a,ca in states.items():
    for b,cb in dp[child].items():
     checks+=1
     if a&b:continue
     good+=1;key=a|b;cost=ca+cb+(ec if b else 0)
     if cost<update.get(key,10**9):update[key]=cost
   states=update;dp[child]=None
  dp[v]=states
 return {'optimum':dp[0][(1<<len(LABELS))-1]+(len(F) if fix_early else 0),
         'candidate_words':nw,'trie_nodes':len(children),
         'inspected_pairs':checks,'compatible_pairs':good,'root_masks':len(dp[0])}

def main():
 report=[]
 for L in L_KEYS:
  lm=[f'{h}:{s}' for h in (4,5) for s in REQ[h] if not cand(h,L)[s]]
  for M in M_KEYS:
   mm=[f'{h}:{s}' for h in (6,7,8,9) for s in REQ[h] if not cand(h,M)[s]]
   result={'L':L,'M':M,'missing':lm+mm}
   if not result['missing']:result.update(solve(L,M))
   report.append(result)
 completed=[r for r in report if not r['missing']]
 late_only=solve((4,2,1),(6,4,1),False)
 data={'pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
       'source_blob':'7e97065ac9a0ff70435b92ee2f4bd718c9bf1859',
       'fixed_H2_H3':dict(zip(('2:16','2:32','3:16','3:32'),FIXED)),
       'integer_early_keys':L_KEYS,'integer_late_keys':M_KEYS,
       'pairs':report,'feasible_pairs':len(completed),
       'best':min(r['optimum'] for r in completed),
       'total_inspected_pairs':sum(r['inspected_pairs'] for r in completed),
       'late_only_h4_h9':late_only}
 assert len(report)==49 and len(completed)==16 and data['best']==112
 assert data['total_inspected_pairs']==382128898
 assert late_only['optimum']==112 and late_only['inspected_pairs']==21972032
 s=json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
 (HERE/'EXACT_RESULTS_EC49FDF.json').write_text(s,encoding='utf-8')
 print('EC49FDF',data['best'],len(completed),'of',len(report),
       'late_only',late_only['optimum'],'checks',data['total_inspected_pairs'],
       'report_sha256',hashlib.sha256(s.encode()).hexdigest())
if __name__=='__main__':main()
