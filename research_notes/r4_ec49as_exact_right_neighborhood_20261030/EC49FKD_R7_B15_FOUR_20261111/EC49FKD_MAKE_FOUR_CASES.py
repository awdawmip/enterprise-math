#!/usr/bin/env python3
"""Regenerate EC49FKD exact four-label candidate cases from frozen FJD inputs."""
import sys,itertools,collections,json,os
from pathlib import Path
R=Path(__file__).resolve().parent
D=Path(os.environ.get('EC49FKB_INPUT_DIR',R.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(D))
import EC49FGW_RADIUS5_SCREEN as g
cert=json.loads((R.parent/'EC49FKC_R7_B15_TRIPLE_20261111'/'EXACT_TRIPLE_CERTS_EC49FKC.json').read_text())
assert cert['frozen_pin']==g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
triple_groups=collections.defaultdict(set)
for c in cert['triples']:triple_groups[c['profile']].add(c['group_index'])
out=[];info=[]
for profile in g.W['profiles']:
 rows,ps=g.validate_profile(profile)
 labels=[(d['window'],d['signature']) for d in rows]
 keys={g.raw_key(d['word']) for d in rows}
 pre=collections.defaultdict(int);key_support=collections.defaultdict(int)
 for i,(d,P) in enumerate(zip(rows,ps)):
  key_support[g.raw_key(d['word'])]|=1<<i
  for v in P:pre[v]|=1<<i
 groups=collections.defaultdict(list)
 for Q in itertools.combinations(range(24),7):
  b=sum(1<<i for i in Q)
  if any(v&b==v for v in key_support.values()):continue
  rem=tuple(sorted(v for v,m in pre.items() if m&b==m))
  if len(rem)==16:groups[rem].append(Q)
 assert len(groups)==67 and sum(map(len,groups.values()))==4336
 for j,(removed,Qs) in enumerate(sorted(groups.items()),1):
  if len(Qs)==1762 or j in triple_groups[profile['profile_id']]:continue
  F=set(pre)-set(removed)
  common=set.intersection(*({labels[i] for i in Q} for Q in Qs))
  for S in itertools.combinations(sorted(common),4):
   out.append('\t'.join([profile['profile_id'],str(j),str(len(Qs)),';'.join(f'{h},{s}' for h,s in S),';'.join(','.join(map(str,x)) for x in sorted(keys)),';'.join(v.hex() for v in sorted(F))]))
  info.append((profile['profile_id'],j,len(Qs),len(common)))
(R/'EC49FKD_FOUR_CASES.tsv').write_text('\n'.join(out)+'\n')
assert len(out)==1075,len(out)
print('cases',len(out),'unresolved groups',len(info),'by profile',collections.Counter(t[0] for t in info))
