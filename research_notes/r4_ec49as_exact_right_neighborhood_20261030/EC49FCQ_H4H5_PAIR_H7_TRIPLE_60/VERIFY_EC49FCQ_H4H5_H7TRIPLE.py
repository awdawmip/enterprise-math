#!/usr/bin/env python3
"""Five-path early-2 + H7-triple signed native prefix proof search, frozen model.
No floating point and no external graph/embedding index. Strict improvement under 158.
"""
from frozen_model import build, W, primpref, candidates, observe
from itertools import combinations
from time import perf_counter
from pathlib import Path
import json,hashlib,sys

PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def antichain_bit(values):
    vals=sorted(set(values),key=int.bit_count)
    out=[]
    for v in vals:
        if not any(v&a==a for a in out):out.append(v)
    return out

def antichain_literal(values):
    vals=sorted(set(values),key=len)
    out=[]
    for v in vals:
        if not any(a.issubset(v) for a in out):out.append(v)
    return out

def solve_bit(keys,original,pools):
    chosen=set(keys)
    fixed=0
    for k,v in original.items():
        if k not in chosen:fixed |= v
    fcount=fixed.bit_count();cap=158-fcount
    assert cap>0
    opts=[antichain_bit([mask&~fixed for mask in pools[k] if (mask&~fixed).bit_count()<cap]) for k in keys]
    states=[0]; sizes=[];raw=1
    for k in keys: raw*=len(pools[k])
    for q in opts:
        unions={x|y for x in states for y in q if (x|y).bit_count()<cap}
        states=antichain_bit(unions)
        sizes.append(len(states))
    return {'fixed':fcount,'cap':cap,'improved':bool(states),'states':sizes,'raw_cartesian':str(raw)}

def solve_literal(keys,chosen,lpools):
    selected=set(keys)
    fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in selected))
    cap=158-len(fixed)
    opts=[antichain_literal([q-fixed for q in lpools[k] if len(q-fixed)<cap]) for k in keys]
    states=[frozenset()];sizes=[]
    for q in opts:
        unions={x|y for x in states for y in q if len(x|y)<cap}
        states=antichain_literal(unions)
        sizes.append(len(states))
    return {'fixed':len(fixed),'cap':cap,'improved':bool(states),'states':sizes}

def main():
    chosen,early,late,pools,original=build()
    h7=[k for k in late if k.startswith('7:')]
    assert len(early)==10 and len(h7)==4 and len(chosen)==24
    groups=[tuple(e)+tuple(t) for e in combinations(early[:6],2) for t in combinations(h7,3)]
    assert len(groups)==60
    print('GROUPS',len(groups),flush=True)
    raw_words={f'{h}:{s}':candidates(h)[s] for h in (4,5,6,7) for s in (16,32) if f'{h}:{s}' in pools} # only some
    for h in (4,6,7):
        for s in (1,2,4,8):raw_words[f'{h}:{s}']=candidates(h)[s]
    all_lit={w:frozenset(primpref(w)) for w in set(chosen.values())|{w for k in set().union(*[set(g) for g in groups]) for w in raw_words[k]}}
    lpools={k:[all_lit[w] for w in raw_words[k]] for k in set().union(*[set(g) for g in groups])}
    records=[]; start=perf_counter();totalraw=0
    for idx,keys in enumerate(groups):
        bit=solve_bit(keys,original,pools)
        lit=solve_literal(keys,chosen,lpools)
        assert bit['fixed']==lit['fixed'] and bit['cap']==lit['cap']
        assert bit['improved']==lit['improved'] and bit['states']==lit['states'],(idx,keys,bit,lit)
        totalraw+=int(bit['raw_cartesian'])
        records.append({'index':idx,'slots':list(keys),**bit,'literal_crosscheck':'PASS'})
        if idx%30==29: print('COMPLETE',idx+1,'elapsed',round(perf_counter()-start,2), 'improved',sum(r['improved'] for r in records),flush=True)
    result={'schema':'EC49FCQ_H4H5PAIR_H7TRIPLE_EXACT_V1','scientific_pin':PIN,
            'scope':'choose 2 of 6 H4-H5 slots and 3 of 4 H7 slots, fixed remaining 19 original words',
            'groups':len(groups),'raw_cartesian_total':str(totalraw),
            'all_bit_literal_crosscheck':True,
            'improving_groups':sum(r['improved'] for r in records),
            'max_intermediate_antichain':max(max(r['states']) for r in records),
            'records':records}
    path=Path(__file__).with_name('EC49FCQ_60_H4H5_results.json')
    content=(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    path.write_bytes(content)
    print('FINISH','groups',len(groups),'improving',result['improving_groups'], 'raw',totalraw,
          'max_antichain',result['max_intermediate_antichain'], 'sha256',hashlib.sha256(content).hexdigest(),'seconds',round(perf_counter()-start,2),flush=True)
if __name__=='__main__':main()
