#!/usr/bin/env python3
"""EC49FCU independent literal signed-prefix checker; original scientific source pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Execute with PYTHONPATH pointing to predecessor frozen_model.py directory.
Uses literal frozenset[str] and no integer bitset or suffix pruning.
"""
import json,hashlib,time
from itertools import combinations,product
from frozen_model import build,primpref,candidates

def minimal(sets):
    out=[]
    for value in sorted(set(sets), key=lambda s:(len(s),sorted(s))):
        if not any(kept.issubset(value) for kept in out): out.append(value)
    return out

def run(keys,chosen,pools):
    selected=set(keys)
    fixed=frozenset().union(*(primpref(word) for key,word in chosen.items() if key not in selected))
    cap=158-len(fixed)
    opts={k:minimal(frozenset(primpref(w))-fixed for w in pools[k] if len(frozenset(primpref(w))-fixed)<cap) for k in keys}
    states=[frozenset()]; sizes=[]; trials=0
    for k in keys:
        cands=[]
        for s in states:
            for p in opts[k]:
                trials+=1
                u=s|p
                if len(u)<cap: cands.append(u)
        states=minimal(cands)
        sizes.append(len(states))
        if not states:
            sizes += [0]*(len(keys)-len(sizes));break
    return {'fixed':len(fixed),'cap':cap,'option_counts':[len(opts[k]) for k in keys],'states':sizes,'improvement':bool(states),'trials':trials}

def main():
    t=time.monotonic()
    chosen,early,late,_,_=build()
    s7=[k for k in late if k.startswith('7:')];s8=[k for k in late if k.startswith('8:')];s9=[k for k in late if k.startswith('9:')]
    groups=[tuple(p)+(a,b,c) for p in combinations(early,2) for a,b,c in product(s7,s8,s9)]
    indices=tuple(range(161,168))
    keys=set().union(*(set(groups[idx]) for idx in indices))
    pools={k:candidates(int(k.split(':')[0]))[int(k.split(':')[1])] for k in keys}
    rows=[]
    for idx in indices:
        row=run(groups[idx],chosen,pools)
        rows.append({'index':idx,'keys':groups[idx],**row})
        print(idx,row,flush=True)
    obj={'schema':'EC49FCU_LITERAL_CROSSCHECK_V1','frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','indices':list(indices),'rows':rows,'independent_encoding':'literal frozenset[str] ordered signed prefixes; no integer bitset and no suffix pruning','completed':len(rows),'all_no_strict_improvement':all(not r['improvement'] for r in rows)}
    content=(json.dumps(obj,sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    with open('EC49FCU_LITERAL_7.json','wb') as f:f.write(content)
    print('SUMMARY',obj['all_no_strict_improvement'],hashlib.sha256(content).hexdigest(),'seconds',round(time.monotonic()-t,3),flush=True)
if __name__=='__main__':main()
