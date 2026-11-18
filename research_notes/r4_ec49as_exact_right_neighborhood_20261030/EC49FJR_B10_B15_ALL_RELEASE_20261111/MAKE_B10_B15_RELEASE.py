"""EC49FJR author finite census: six-path cache-key release, budgets 10/12/13/14/15, one, two, or three released keys.
Enumerate ALL possible seventh-key completions, even keys not needed for uncovered labels.
"""
from ec49fjd_shared import *
from itertools import combinations
from collections import defaultdict,Counter
from pathlib import Path
import json,hashlib,time
P=Path(__file__).parent
stats=[];cases=[];alt_hist=Counter();counts=Counter()
with (P/'FJR_CATALOG.tsv').open('w') as fh:
 for lab,w in cat:
  k=raw_key(w);fh.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
def enc(K):return ';'.join(','.join(map(str,k)) for k in sorted(K))
with (P/'FJR_CASES.tsv').open('w') as fh:
 for profile in W['profiles']:
  rows,paths=validate_profile(profile);ksu=defaultdict(int);psu=defaultdict(int)
  for i,(row,ps) in enumerate(zip(rows,paths)):
   ksu[raw_key(row['word'])]|=1<<i
   for p in ps:psu[p]|=1<<i
  orig=frozenset(ksu); assert len(orig)==7
  stat=Counter(); keys_all=tuple(sorted(cover))
  for Q in combinations(range(24),6):
   mask=sum(1<<i for i in Q)
   B=sum((s&mask)==s for s in psu.values())-1
   if B not in (10,12,13,14,15):continue
   released=frozenset(k for k,s in ksu.items() if (s&mask)==s)
   r=len(released)
   if r not in (1,2,3):continue
   fixed=orig-released
   labels=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
   missing=set(labels)-set().union(*(cover[k] for k in fixed))
   outsiders=[k for k in keys_all if k not in fixed]
   if r==1:admissible=[(k,) for k in outsiders if missing.issubset(cover[k])]
   else:admissible=[K for K in combinations(outsiders,r) if missing.issubset(set().union(*(cover[k] for k in K)))]
   assert admissible and tuple(sorted(released)) in admissible,(profile['profile_id'],Q,admissible)
   F=frozenset(p for p,s in psu.items() if s&mask!=s)
   assert len(F)==93-B
   options='|'.join(enc(fixed|frozenset(K)) for K in admissible)
   fh.write(f'{profile["profile_id"]}\t{",".join(map(str,Q))}\t{";".join(f"{h},{s}" for h,s in labels)}\t{options}\t{";".join(p.hex() for p in sorted(F))}\n')
   n=len(admissible); stat[f'B{B}_r{r}']+=1;counts[(B,r)]+=1;alt_hist[(B,r,n)]+=1
   cases.append({'profile':profile['profile_id'],'Q':list(Q),'B':B,'released_n':r,'admissible_keysets':n})
  stats.append({'profile':profile['profile_id'],**dict(stat)})
summary={'schema':'EC49FJR_ALL_RELEASE_B10_B15_FINITE_V1','science_pin':PIN,'profiles':stats,'counts_by_budget_release':{f'B{b}_r{r}':n for (b,r),n in sorted(counts.items())},'alternative_keysets_histogram':{f'B{b}_r{r}_sets{n}':c for (b,r,n),c in sorted(alt_hist.items())},'cases':cases}
(P/'FJR_CASE_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
for x in ['FJR_CATALOG.tsv','FJR_CASES.tsv','FJR_CASE_SUMMARY.json']:
 b=(P/x).read_bytes();print(x,len(b),hashlib.sha256(b).hexdigest())
print('FJR_INPUT_PASS',len(cases),stats,'KEYSET_TRIES',sum(n*c for (b,r,n),c in alt_hist.items()))
