#!/usr/bin/env python3
"""Exact frozen-BRC signed-prefix five-slot replacement search.
Scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Uses the preexisting witness and independent typed candidate enumerator.
"""
import argparse,hashlib,json,time
from itertools import combinations
from frozen_model import build, primpref, candidates
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def prune_bit(vals):
    kept=[]
    for x in sorted(set(vals),key=int.bit_count):
        if not any((x&y)==y for y in kept):
            kept.append(x)
    return kept

def prune_lit(vals):
    kept=[]
    for x in sorted(set(vals),key=len):
        if not any(y.issubset(x) for y in kept):
            kept.append(x)
    return kept

def run_bit(keys, originals,pools):
    picked=set(keys);fixed=0
    for k,m in originals.items():
        if k not in picked:fixed|=m
    fcount=fixed.bit_count();cap=158-fcount
    states=[0];sizes=[];options=[]
    for key in keys:
        opt=prune_bit(m&~fixed for m in pools[key] if ((m&~fixed).bit_count()<cap))
        options.append(len(opt))
        states=prune_bit(x|y for x in states for y in opt if (x|y).bit_count()<cap)
        sizes.append(len(states))
    return {'fixed':fcount,'cap':cap,'states':sizes,'option_antichain_counts':options,'strict_improvement_exists':bool(states), 'optimal_if_no_improvement':158 if not states else None}

def run_lit(keys,chosen,lpools):
    selected=set(keys)
    fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in selected))
    cap=158-len(fixed);states=[frozenset()];sizes=[]
    for key in keys:
        opt=prune_lit(q-fixed for q in lpools[key] if len(q-fixed)<cap)
        states=prune_lit(x|y for x in states for y in opt if len(x|y)<cap)
        sizes.append(len(states))
    return {'fixed':len(fixed),'cap':cap,'states':sizes,'strict_improvement_exists':bool(states)}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int,default=4)
    p.add_argument('--literal',type=int,default=4)
    p.add_argument('--output',default='EC49FCR_BATCH.json');a=p.parse_args()
    start=time.monotonic()
    chosen,early,late,pools,original=build()
    h7=[k for k in late if k.startswith('7:')]
    groups=[tuple(e)+tuple(t) for e in combinations(early,2) if any(k.startswith('6:') for k in e) for t in combinations(h7,3)]
    assert len(groups)==120
    assert 0 <= a.start < a.stop <= len(groups)
    lpools={};selected_keys=set().union(*(set(groups[i]) for i in range(a.start,a.stop)))
    if a.literal:
        for k in selected_keys:
            h,s=map(int,k.split(':'))
            lpools[k]=[frozenset(primpref(w)) for w in candidates(h)[s]]
    records=[];raw_total=0
    for i in range(a.start,a.stop):
        keys=groups[i]
        raw=1
        for k in keys:raw*=len(pools[k])
        b=run_bit(keys,original,pools)
        if a.literal and i < a.start+a.literal:
            l=run_lit(keys,chosen,lpools)
            assert (b['fixed'],b['cap'],b['states'],b['strict_improvement_exists'])==(l['fixed'],l['cap'],l['states'],l['strict_improvement_exists']),(i,b,l)
            cross='PASS'
        else:cross='NOT_RUN'
        records.append({'group_index':i,'slots':keys,'raw_cartesian':str(raw),'bit':b,'literal_crosscheck':cross})
        raw_total+=raw
        print('GROUP',i,'seconds',round(time.monotonic()-start,2),'cap',b['cap'],'states',b['states'],'improved',b['strict_improvement_exists'],'crosscheck',cross,flush=True)
        if b['strict_improvement_exists']:
            raise RuntimeError('Improvement candidate requires five-word witness reconstruction; not a 158-rigidity certificate')
    res={'schema':'EC49FCR_H6PAIR_H7TRIPLE_BATCH_V1','pin':PIN,'model_semantics':'frozen model 24 slots, signed X6 step expansion; fixed witness 158','group_family':'two early incl H6 and three H7','total_family_groups':120,'index_range':[a.start,a.stop],'groups_checked':len(records),'improving':sum(x['bit']['strict_improvement_exists'] for x in records),'raw_cartesian_total':str(raw_total),'crosschecked':sum(x['literal_crosscheck']=='PASS' for x in records),'max_antichain':max(max(x['bit']['states']) for x in records),'records':records}
    bs=(json.dumps(res,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    open(a.output,'wb').write(bs)
    print('SUMMARY',json.dumps({k:v for k,v in res.items() if k!='records'}|{'seconds':round(time.monotonic()-start,2),'sha256':hashlib.sha256(bs).hexdigest()}),flush=True)
if __name__=='__main__':main()
