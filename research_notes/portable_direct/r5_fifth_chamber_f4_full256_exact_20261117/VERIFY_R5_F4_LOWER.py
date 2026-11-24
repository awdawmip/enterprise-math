#!/usr/bin/env python3
"""Exact five-state, all-101-budget minimax lower certificate for four errors."""
import json,hashlib,sys
from pathlib import Path
from functools import lru_cache
from BUILD_R5_F4_ACTIONS import INPUT_SHA256,maximal_normal_supports
L=25845652773852463277015040000
H=(18,24,82,34,17)

def solve(src,f=4):
    raw=Path(src).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==INPUT_SHA256
    data=json.loads(raw)
    tab={int(k):tuple(map(int,item['counts'])) for k,item in data['counts_and_cohorts'].items()}
    assert set(tab)==set(range(214,315)) and all(len(r)==256 for r in tab.values())
    full=(1<<len(H))-1
    unique={}
    for k in range(214,315):
        row=tuple(tab[k][h] for h in H)
        unique.setdefault(maximal_normal_supports(row,L),k)
    actions=[(k,ans,tuple(full^a for a in ans)) for ans,k in unique.items()]
    actions.sort(key=lambda a:(a[0] not in (216,223,296),a[0]))
    @lru_cache(None)
    def V(*levels):
        union=0
        for x in levels:union|=x
        if union.bit_count()<=1:return 0
        best=1<<35
        for cost,answers,missing in actions:
            worst=0
            for ans,no in zip(answers,missing):
                next_levels=(levels[0]&ans,)+tuple((levels[j]&ans)|(levels[j-1]&no) for j in range(1,len(levels)))
                if next_levels==levels:break
                worst=max(worst,V(*next_levels))
                if cost+worst>=best:break
            else:
                best=min(best,cost+worst)
        assert best<(1<<35)
        return best
    return {'f':f,'exact_lower':V(*([full]+[0]*f)),'memo_states':V.cache_info().currsize,
            'masks':list(H),'budgets':list(range(214,315)),'tau':str(L)}

if __name__=='__main__':
    out=solve(sys.argv[1],4)
    assert out['exact_lower']==4535 and out['memo_states']==4321,out
    print(json.dumps(out,indent=2))
