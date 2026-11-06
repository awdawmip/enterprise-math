#!/usr/bin/env python3
"""Exact frozen signed-native 5-slot prefix exchange, early2 plus H7+H8+H9.
Source input pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json,hashlib,time,argparse
from itertools import combinations,product
from frozen_model import build,primpref,candidates

def antichain(values):
    kept=[]
    for x in sorted(set(values),key=int.bit_count):
        if not any((x&y)==y for y in kept): kept.append(x)
    return kept

def run(keys,original,pools,literal=None):
    sel=set(keys); fixed=0
    for key,m in original.items():
        if key not in sel: fixed |= m
    fixed_count=fixed.bit_count(); limit=158-fixed_count
    opts=[antichain(m & ~fixed for m in pools[k] if (m & ~fixed).bit_count()<limit) for k in keys]
    mandatory=0
    suffix=[0]*(len(keys)+1)
    for i in range(len(keys)-1,-1,-1):
        intersection=opts[i][0] if opts[i] else 0
        for o in opts[i][1:]: intersection &= o
        mandatory |= intersection
        suffix[i]=mandatory
    states=[0]; sizes=[];tested=0
    for i,op in enumerate(opts):
        next_states=[]
        for state in states:
            for mask in op:
                merged=state|mask
                tested+=1
                if (merged|suffix[i+1]).bit_count()<limit:
                    next_states.append(merged)
        states=antichain(next_states)
        sizes.append(len(states))
        if not states:
            sizes += [0]*(len(keys)-i-1)
            break
    return {'fixed':fixed_count,'strict_cap':limit,'option_antichain_counts':[len(o) for o in opts],'states':sizes,'improvement':bool(states),'combination_tests':tested}

def literal_run(keys,chosen,lit_pools):
    sel=set(keys);fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in sel)); cap=158-len(fixed)
    def alit(v):
        k=[]
        for x in sorted(set(v),key=len):
            if not any(y.issubset(x) for y in k):k.append(x)
        return k
    states=[frozenset()]; sz=[]
    for key in keys:
        opt=alit(p-fixed for p in lit_pools[key] if len(p-fixed)<cap)
        states=alit(s|p for s in states for p in opt if len(s|p)<cap)
        sz.append(len(states))
    return {'fixed':len(fixed),'cap':cap,'states':sz,'improvement':bool(states)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=45)
    ap.add_argument('--literal',type=int,default=5)
    ap.add_argument('--h7',default=None,help='Restrict to one H7 slot, e.g. 7:1')
    ap.add_argument('--early4h5',action='store_true',help='Restrict early pair to one H4 and one H5')
    ap.add_argument('--output',default='EC49FCS_PART.json')
    a=ap.parse_args(); t=time.monotonic()
    chosen, early, late, pools, original=build()
    s7=[k for k in late if k.startswith('7:')]
    s8=[k for k in late if k.startswith('8:')]
    s9=[k for k in late if k.startswith('9:')]
    groups=[tuple(pair)+(h7,h8,h9) for pair in combinations(early,2) for h7,h8,h9 in product(s7,s8,s9)]
    assert len(groups)==45*4*4*2==1440
    if a.h7: groups=[group for group in groups if group[2]==a.h7]
    if a.early4h5: groups=[group for group in groups if group[0].startswith('4:') and group[1].startswith('5:')]
    assert 0<=a.start<a.stop<=len(groups)
    lit_keys=set().union(*(set(groups[i]) for i in range(a.start,min(a.start+a.literal,a.stop))))
    lpools={key:[frozenset(primpref(w)) for w in candidates(int(key.split(':')[0]))[int(key.split(':')[1])]] for key in lit_keys}
    records=[]; rawtotal=0; ops=0
    for idx in range(a.start,a.stop):
        keys=groups[idx]; b=run(keys,original,pools)
        if b['improvement']:
            raise RuntimeError('Improvement candidate: inspect witness before claiming rigidity index='+str(idx))
        raw=1
        for k in keys:raw*=len(pools[k])
        rawtotal+=raw;ops+=b['combination_tests']
        if idx<a.start+a.literal:
            q=literal_run(keys,chosen,lpools)
            assert (b['fixed'],b['strict_cap'],b['states'],b['improvement'])==(q['fixed'],q['cap'],q['states'],q['improvement']),(idx,b,q)
            cross='PASS'
        else:cross='NOT_RUN'
        records.append({'index':idx,'slots':keys,'raw_cartesian':str(raw),'result':b,'literal':cross})
        if (idx-a.start)%10==0 or idx==a.stop-1:
            print('PROGRESS',idx,'secs',round(time.monotonic()-t,2),'cap',b['strict_cap'],'st',b['states'],'tested',b['combination_tests'],flush=True)
    obj={'schema':'EC49FCS_H7_H8_H9_EARLY2_EXACT_V1','source_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','witness_cost':158,'family_count':len(groups),'h7_restriction':a.h7,'early4h5':a.early4h5,'subset':[a.start,a.stop],'checked':len(records),'all_have_exact_minimum':158,'literal_crosschecks':sum(r['literal']=='PASS' for r in records),'raw_cartesian_total':str(rawtotal),'actual_stage_unions':ops,'max_stage_antichain':max(max(r['result']['states']) for r in records),'records':records}
    content=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    with open(a.output,'wb') as f:f.write(content)
    print('SUMMARY',json.dumps({k:v for k,v in obj.items() if k!='records'}|{'sha256':hashlib.sha256(content).hexdigest(),'wall_seconds':round(time.monotonic()-t,2)}),flush=True)
if __name__=='__main__':main()
