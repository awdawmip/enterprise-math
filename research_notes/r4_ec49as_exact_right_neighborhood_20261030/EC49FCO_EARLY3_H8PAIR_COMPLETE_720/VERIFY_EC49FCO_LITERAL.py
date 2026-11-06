#!/usr/bin/env python3
"""Second implementation: literal ordered signed step prefixes as frozenset[str], no integer bitsets.
Checks independently selected FCO groups with exact exhaustive improvements search.
"""
from frozen_model import REQ,W,observe,primpref,candidates
from itertools import combinations
import sys,time,json,hashlib
CHOSEN={f'{h}:{observe(w)}':w for h,vs in W.items() for w in vs}
EARLY=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
H8=[f'8:{s}' for s in REQ[8]]
GROUPS=[(*e,*b) for e in combinations(EARLY,3) for b in combinations(H8,2)]
WORDS={key:candidates(int(key.partition(':')[0]))[int(key.partition(':')[2])] for key in set(k for g in GROUPS for k in g)}
PREF={w:frozenset(primpref(w)) for w in set(CHOSEN.values())|set(w for vs in WORDS.values() for w in vs)}

def exact(idx):
    keys=GROUPS[idx];selected=set(keys)
    fixed=frozenset().union(*(PREF[w] for k,w in CHOSEN.items() if k not in selected))
    cap=158-len(fixed)
    pools=[{PREF[w]-fixed for w in WORDS[k] if len(PREF[w]-fixed)<cap} for k in keys]
    triples={a|b|c for a in pools[0] for b in pools[1] for c in pools[2] if len(a|b|c)<cap}
    checks=0
    for e in triples:
        for a in pools[3]:
            ea=e|a
            if len(ea)>=cap:continue
            for b in pools[4]:
                checks+=1
                if len(ea|b)<cap:return {'index':idx,'slots':keys,'min':len(fixed)+len(ea|b),'fixed_edges':len(fixed),'checked':checks}
    return {'index':idx,'slots':keys,'min':158,'fixed_edges':len(fixed),'checked':checks}

if __name__=='__main__':
  t=time.monotonic(); rows=[]
  for idx in (map(int,sys.argv[1:]) if len(sys.argv)>1 else range(720)):
    r=exact(idx);rows.append(r)
    if idx % 120 == 0: print('VERIFIED',idx,r['min'],'s',round(time.monotonic()-t,2),flush=True)
  s=json.dumps({'algorithm':'independent literal signed prefix frozenset enumeration','science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','rows':rows},sort_keys=True,separators=(',',':'))+'\n'
  open('EC49FCO_LITERAL_CHECKS.json','w').write(s)
  print('SUMMARY',len(rows),'sha256',hashlib.sha256(s.encode()).hexdigest(),flush=True)
