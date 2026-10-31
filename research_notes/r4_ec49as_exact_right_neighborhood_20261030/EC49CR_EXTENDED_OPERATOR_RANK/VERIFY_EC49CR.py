"""Exact rational formal observer rank, modular actual path witnesses for new signed op e.
Declared scope: signed X6 positive BRC channels W0,W1 and literal counts, four A/B labels.
"""
from __future__ import annotations
import json, itertools, sys, time
from collections import defaultdict
from pathlib import Path
from fractions import Fraction
from sympy import Matrix
import VERIFY_EC49CJ as old

S={**old.S,'e':(3,1,1,-3)}
P=old.P

def suffixes(min_h, max_h):
    return {''.join(t):tuple(itertools.chain.from_iterable(S[x] for x in t))
            for j in range(min_h,max_h+1) for t in itertools.product(S,repeat=j)}

def rows_for(suffix):
    gr=defaultdict(list)
    for key,ss in suffix.items():
        target=tuple(-x for x in old.displacement(ss))
        labs=[old.label(old.follow(q,ss)) for q in range(9)]
        for lab in range(4):
            row=tuple(int(x==lab) for x in labs)
            gr[target].append((key,lab,row))
    return dict(sorted(gr.items()))

def row_rank_q(rows):
    return Matrix(rows).rank() if rows else 0

def summary(suf):
    groups=rows_for(suf)
    table=[]
    for target,records in groups.items():
        patterns=[r[2] for r in records]
        pivots=old.rank_select(patterns)
        rq=row_rank_q(patterns)
        assert len(pivots)==rq, (target,len(pivots),rq)
        table.append({'target':list(target),'rational_per_type_rank':rq,
                      'obs_rows':len(records),'basis_readouts':[[records[j][0],records[j][1]] for j in pivots]})
    return {'suffix_count':len(suf),'target_count':len(table),
            'per_channel_rank':sum(x['rational_per_type_rank'] for x in table),
            'three_channel_formal_rank':3*sum(x['rational_per_type_rank'] for x in table),'fibers':table}

def attempt(n,suf):
    rs=old.row_system(suf)
    record=old.certify(n,suf,rs)
    assert old.recheck_certificate(record,suf,rs)
    return record

def main():
    here=Path(__file__).parent
    obs_sets={'S1':suffixes(1,1),'S2':suffixes(2,2),'SLE2':suffixes(1,2),
              'EPS_SLE2':suffixes(0,2),'EPS_SLE1':suffixes(0,1)}
    out={}
    for name,s in obs_sets.items():
        r=summary(s)
        out[name]=r
        print(name,'words',len(s),'fibers',r['target_count'],'1ch',r['per_channel_rank'],'all3',r['three_channel_formal_rank'],flush=True)
        for f in r['fibers']:
            print('  ',f['target'][:2],f['rational_per_type_rank'],flush=True)
    out['ROLLING_EPS_SLE1_FROM_EPS_SLE2']={
        'rank_of_domain':out['EPS_SLE2']['three_channel_formal_rank'],
        'rank_of_joint_five_successors':out['SLE2']['three_channel_formal_rank'],
        'kernel':out['EPS_SLE2']['three_channel_formal_rank']-out['SLE2']['three_channel_formal_rank']}
    # exact real paths for S<=2, subsequent states reuse previously validated modular DP
    if '--no-path' not in sys.argv:
        for n in [4,6,8,10]:
            k=f'REAL_{n}_SLE2'
            a=attempt(n,obs_sets['SLE2'])
            out[k]={z:v for z,v in a.items() if z not in ('blocks','layers')}
            (here/f'CERT_EC49CR_{k}.json').write_text(json.dumps(a,sort_keys=True,separators=(',',':'))+'\n')
            if a['all_fibers_full']:
                print('FULL SATURATION at',n,flush=True)
                break
    (here/'EXACT_REPORT_EC49CR.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
