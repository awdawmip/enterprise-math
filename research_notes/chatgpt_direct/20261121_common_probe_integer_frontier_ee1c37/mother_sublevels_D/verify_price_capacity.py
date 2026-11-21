"""Independently rebuild exact price/defect options from hash-bound native rows."""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import struct

HERE = Path(__file__).resolve().parent


def verify(seeds, mother, mixed):
    certified=json.loads((mixed/'mixed_bound_verification.json').read_text())
    expected=json.loads((HERE/'cost_defect_catalog.json').read_text())
    assert sha256((mixed/'mixed_bound_verification.json').read_bytes()).hexdigest()==expected['source_mixed_bound_sha256']
    raw=seeds.read_bytes();assert sha256(raw).hexdigest()==certified['complete_seed_sha256']
    offsets={int(k):v for k,v in certified['offsets'].items()}
    caps={int(k):v for k,v in certified['finite_cutoffs'].items()}
    coordinates=[(p//25,p//5%5,p%5) for p in range(125)]
    observed=Counter();maximum={}
    def collect(n,c,ids):
        h=[[0]*5 for _ in range(3)]
        for p in ids:
            for axis,value in enumerate(coordinates[p]):h[axis][value]+=1
        delta=sum(max(count-2,0) for axis in h for count in axis)
        assert c>=offsets[n]+3*delta
        maximum[n,c]=max(maximum.get((n,c),-1),delta);observed[n]+=1
    lines=raw.splitlines();assert len(lines)==certified['complete_seed_rows']
    for line in lines:
        n,c,tail=line.split(None,2);n=int(n);c=int(c)
        if n in (8,9,10) and c<=caps[n]:collect(n,c,map(int,tail.split()))
    for n in (11,12):
        raw=(mixed/f'inputs/B{n}').read_bytes()
        record=next(r for r in certified['proper_anchored_banks'] if r['size']==n)
        assert sha256(raw).hexdigest()==record['sha256']
        for lo,hi,c in struct.iter_unpack('<QQQ',raw):
            if c<=caps[n]:
                mask=lo+(hi<<64);collect(n,c,(p for p in range(125) if mask>>p&1))
    assert {str(k):v for k,v in observed.items()}==certified['finite_native_rows_checked']
    catalog={}
    for line in (mother/'catalog.txt').read_text().splitlines():
        n,e,c,weighted=map(int,line.split());catalog.setdefault((n,e),set()).add(c)
    minima={n:min(catalog[n,0]) for n in range(8,13)}
    assert minima=={8:419,9:557,10:744,11:1008,12:1244}
    options={};output=[];rows=[]
    for n in range(8,13):
        options[n]=[]
        for c in sorted(catalog[n,0]):
            upper=maximum[n,c] if c<=caps[n] else min(3*(n-2),(c-offsets[n])//3)
            basis='complete_finite_native_rows' if c<=caps[n] else 'proved_linear_and_cardinality_bounds'
            rows.append({'size':n,'cost':c,'maximum_defect_upper_bound':upper,'basis':basis})
            output.append(f'{n} {c} {upper}\n');options[n].append((c-minima[n],upper))
    assert rows==expected['rows']
    assert ''.join(output).encode()==(HERE/'cost_defect_options.txt').read_bytes()
    @lru_cache(None)
    def capacity(counts):
        if not any(counts):return (0,)*156
        axis=next(i for i,n in enumerate(counts) if n)
        before=list(counts);before[axis]-=1;previous=capacity(tuple(before))
        ans=[-100000]*156
        for extra,delta in options[axis+8]:
            for budget in range(extra,156):ans[budget]=max(ans[budget],previous[budget-extra]+delta)
        return tuple(ans)
    profiles=[r for r in json.loads((mother/'plan_9995.json').read_text())['profiles'] if r['embedded_count']==2]
    assert len(profiles)==14
    queries=set()
    for row in profiles:
        counts=tuple(row['proper_sizes'].count(n) for n in range(8,13))
        for current in product(*(range(n+1) for n in counts)):
            for budget in range(9995-row['minimum_total_cost']+1):queries.add((current,budget))
    query=''.join(' '.join(map(str,(*counts,budget,capacity(counts)[budget])))+'\n' for counts,budget in sorted(queries))
    assert query.encode()==(HERE/'capacity_queries.txt').read_bytes()
    assert len(queries)==expected['all_E2_remaining_count_budget_queries']==7773
    proper=[]
    for line in (mixed/'positive_construct.txt').read_text().splitlines():
        n,c,*pts=map(int,line.split())
        if n!=13:proper.append((n,c,sum(1<<p for p in pts)))
    assert len(proper)==10
    fibers=[sum(1<<p for p,x in enumerate(coordinates) if x[j]==a) for j in range(3) for a in range(5)]
    for mask in range(1024):
        left=[r for i,r in enumerate(proper) if not mask>>i&1];free=0
        for n,c,m in left:free|=m
        counts=tuple(sum(n==s for n,c,m in left) for s in range(8,13))
        budget=sum(c-minima[n] for n,c,m in left)
        delta=sum(max((free&f).bit_count()-2*len(left),0) for f in fibers)
        assert delta<=capacity(counts)[budget]
    return {'finite_hash_bound_rows_recomputed':sum(observed.values()),'proper_price_options':len(rows),
            'count_budget_queries':len(queries),'positive_subsets':1024}
