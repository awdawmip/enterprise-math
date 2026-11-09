#!/usr/bin/env python3
"""R670-D: exact reachable-state and minimality certificate for a no-repeat group observer."""
import json
from collections import deque
from pathlib import Path
E=(0,1,2)
G=((0,2,1),(2,1,0),(1,0,2))
def mul(x,y): return tuple(x[y[i]] for i in range(3))
def check(k):
    assert k in (2,3)
    init=(E,-1); reach={init:''}; q=deque([init])
    while q:
        h,last=q.popleft()
        for x in range(k):
            if x==last: continue
            nxt=(mul(h,G[x]),x)
            if nxt not in reach:
                reach[nxt]=reach[(h,last)]+str(x)
                q.append(nxt)
    obs={st:(st[0],tuple(x for x in range(k) if x!=st[1])) for st in reach}
    assert len(set(obs.values()))==len(reach)
    assert len(reach)==1+6*k
    assert max(map(len,reach.values()))<=(6 if k==2 else 4)
    witnesses={str(x):{''.join(map(str,h)):word for (h,last),word in reach.items() if last==x} for x in range(k)}
    assert all(len(v)==6 for v in witnesses.values())
    return {'alphabet_size':k,'reachable_states':len(reach),'longest_shortest_witness':max(map(len,reach.values())),'witnesses_by_last':witnesses}
if __name__=='__main__':
    records=[check(2),check(3)]
    result={'marker':'R670D_GENERAL_NOREPEAT_GROUP_OBSERVER_13_19_MINIMAL_PASS','scope':'V17 auxiliary reflection-loop no-repeat complete-block scheduler','verified_instances':records,'formal_claim':'not admitted'}
    Path(__file__).with_name('R670_MINIMALITY_ADDENDUM_EVIDENCE.json').write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
