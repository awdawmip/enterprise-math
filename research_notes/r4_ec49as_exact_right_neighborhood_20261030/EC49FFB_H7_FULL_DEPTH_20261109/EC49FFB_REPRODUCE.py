#!/usr/bin/env python3
"""Reproduce EC49FFB H7 mixed-B original signed-X6 depth certificates.
Uses sibling EC49FFA_H8_FIVEKEY_DEPTHWISE_20261109/h8_key_depth_sieve.py.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import argparse, collections, json, sys
from pathlib import Path
parent=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(parent/'EC49FFA_H8_FIVEKEY_DEPTHWISE_20261109'))
import h8_key_depth_sieve as core

def choose_disjoint(adj):
    n=len(adj); deg=[v.bit_count() for v in adj];best=()
    orders=[sorted(range(n),key=lambda j:(deg[j],j)),
            sorted(range(n),key=lambda j:(deg[j],-j)),
            list(range(n)),list(range(n-1,-1,-1))]
    for offset in range(n):
        orders.append(sorted(range(n),key=lambda j:((deg[j]+j+offset)%n,deg[j],j)))
    for order in orders:
        taken=[];mask=0
        for j in order:
            if not adj[j]&mask:
                taken.append(j);mask|=1<<j
        if len(taken)>len(best):best=tuple(sorted(taken))
    assert all((adj[i]&(1<<j))==0 for i in best for j in best if i!=j)
    return best

def disjoint_certificate(keys,groups,depths=24):
    supports=[];minlen=[]
    for h,s in groups:
        layers=collections.defaultdict(set);lens=[]
        for k in keys:
            ps=core.prefixes(h,k,s)
            if ps:
                lens.append(max(ps))
                for d,p in ps.items():
                    if d<=depths:layers[d].update(p)
        assert lens,(h,s,keys)
        supports.append(layers);minlen.append(min(lens))
    chosen=[]
    for d in range(1,depths+1):
        active=[i for i in range(len(groups)) if minlen[i]>=d]
        adj=[0]*len(active)
        for j,g in enumerate(active):
            for k in range(j+1,len(active)):
                if not supports[g][d].isdisjoint(supports[active[k]][d]):
                    adj[j]|=1<<k;adj[k]|=1<<j
        chosen.append([active[i] for i in choose_disjoint(adj)])
    return chosen

def reproduce(late,start=0,limit=0,outdir=Path('.')):
    late=tuple(int(x) for x in late)
    assert late in ((5,7,8,9),(6,7,8,9))
    name=''.join(map(str,late))
    inventory,status,_=core.build_inventories(7,late)
    expected={'5789':8352,'6789':5376}[name]
    assert len(inventory)==expected,(name,len(inventory))
    groups=core.all_groups(7,late)
    assert len(groups)==23
    counts=collections.Counter()
    dest=outdir/f'EC49FFB_WITNESSES_{name}_{start}_{limit}.jsonl'
    stop=len(inventory) if not limit else min(len(inventory),start+limit)
    with dest.open('w') as f:
        for idx in range(start,stop):
            K=inventory[idx];D=disjoint_certificate(K,groups)
            bound=sum(map(len,D));counts[bound]+=1
            f.write(json.dumps({'index':idx,'keys':K,'D':D,'lower_bound':bound},separators=(',',':'))+'\n')
    summary={'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        'late':name,'candidate_inventories':sum(status.values()),'feasible_inventories':len(inventory),
        'checked_inventories':sum(counts.values()),'min_depthwise_lower_bound':min(counts),
        'count_at_or_below_93':sum(v for k,v in counts.items() if k<=93),
        'depths':24,'start':start,'limit':limit,'histogram':dict(sorted(counts.items()))}
    (outdir/f'EC49FFB_SUMMARY_{name}_{start}_{limit}.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='histogram'},sort_keys=True),flush=True)
    return summary

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('late',choices=('5789','6789'))
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--limit',type=int,default=0)
    args=ap.parse_args()
    reproduce(args.late,args.start,args.limit)
