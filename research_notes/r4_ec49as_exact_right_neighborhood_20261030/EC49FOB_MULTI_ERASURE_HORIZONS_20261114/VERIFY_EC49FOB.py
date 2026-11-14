#!/usr/bin/env python3
"""EC49FOB full k=2,3 and selected k=4..7 BRC root-lookahead census.

Requires unaltered prior pinned files:
  master_and_radius3_cases.txt
  EC49FNY_CERT_ALL.txt
  VERIFY_EC49FNY_INDEPENDENT.py
All calculations exact integer native signed ordered-prefix root-cover costs.
"""
import collections
import hashlib
import itertools
import json
import sys
from functools import lru_cache
from pathlib import Path

import VERIFY_EC49FNY_INDEPENDENT as native

ROOTS = native.ROOTS
MASTER_SHA = 'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
CERT_SHA = '708da9a677ecf1d7842daf732ea51c796262a2974ef3476c9ef34f2f4107b271'
B = 155
SELECTION = {
    2: (None, frozenset()),
    3: (None, frozenset()),
    4: ('159571690231449', frozenset({15})),
    5: ('159571690231449', frozenset({4,5,6,15})),
    6: ('159571690231449', frozenset({4,5,6,8,15})),
    7: ('159571690231449', frozenset({4,5,6,8,9,15})),
}
EXPECTED = {
    2: (2081, {1:211,2:722,3:705,4:357,5:18,None:68}),
    3: (13902,{1:360,2:2318,3:4427,4:3937,5:1977,6:146,None:737}),
    4: (1140, {4:4,5:87,6:406,7:455,None:188}),
    5: (17, {7:4,8:11,None:2}),
    6: (16, {8:4,9:10,None:2}),
    7: (15, {9:4,10:9,None:2}),
}

def verify(master, cert, out):
    assert hashlib.sha256(master.read_bytes()).hexdigest() == MASTER_SHA
    assert hashlib.sha256(cert.read_bytes()).hexdigest() == CERT_SHA
    words, keys = native.frozen(master)
    profiles = {r: native.table(words,keys,r) for r in ROOTS}
    options = {l:tuple(j for j,r in enumerate(ROOTS) if l in profiles[r][1]) for l in range(24)}
    assert all(options.values())
    mask_to_root = []
    for r in ROOTS:
        _names,index,cost_table,_nodes=profiles[r]
        bit={l:1<<b for l,b in index.items()}
        @lru_cache(None)
        def rooted(m, bit=bit, cost_table=cost_table):
            b=0
            while m:
                q=m&-m
                b|=bit[q.bit_length()-1]
                m^=q
            return cost_table[b]
        mask_to_root.append(rooted)
    @lru_cache(None)
    def total(masks):
        return sum(f(m) for f,m in zip(mask_to_root,masks))
    @lru_cache(None)
    def partial_optimum(masks, labels):
        opt=10**9; arg=None
        for roots in itertools.product(*(options[l] for l in labels)):
            tmp=list(masks)
            for l,j in zip(labels,roots):tmp[j]|=1<<l
            value=total(tuple(tmp))
            if value<opt:
                opt=value;arg=tuple(ROOTS[j] for j in roots)
        return opt,arg
    cuts={}
    for line in cert.read_text().splitlines():
        if line.startswith('WITNESS '):
            cols=line.split()
            masks=tuple(map(int,cols[-4:]))
            cuts[(cols[3],masks)]=int(cols[5])
    assert len(cuts)==9
    archive={}
    for k in range(2,8):
        target, required=SELECTION[k]
        results=[]
        for (pattern,masks),prior_lb in sorted(cuts.items()):
            if target is not None and pattern != target:continue
            assert total(masks)==prior_lb
            assigned={l:j for j,m in enumerate(masks) for l in range(24) if m>>l&1}
            for erase in itertools.combinations(sorted(assigned),k):
                if not required.issubset(erase):continue
                mm=list(masks)
                for l in erase:mm[assigned[l]]^=1<<l
                mm=tuple(mm)
                u=tuple(l for l in range(24) if all(not (m>>l)&1 for m in mm))
                horizon=[]
                for h in range(1,len(u)+1):
                    vals=[(partial_optimum(mm,t)[0],t) for t in itertools.combinations(u,h)]
                    maximum=max(v for v,_ in vals)
                    subset=next(t for v,t in vals if v==maximum)
                    horizon.append((maximum,subset))
                values=tuple(v for v,_ in horizon)
                assert values==tuple(sorted(values))
                full,full_roots=partial_optimum(mm,u)
                assert values[-1]==full
                first=next((i+1 for i,v in enumerate(values) if v>B),None)
                assert (first is None)==(full<=B)
                results.append({'pattern':pattern,'erased':erase,'masks':mm,'unassigned':u,
                                'horizons':values,'horizon_maximizers':[x[1] for x in horizon],
                                'first_strict_horizon':first,'full_minimum':full,
                                'full_minimizer_roots':full_roots})
        counts=dict(collections.Counter(c['first_strict_horizon'] for c in results))
        assert (len(results),counts)==EXPECTED[k],(k,len(results),counts)
        archive[str(k)]={'count':len(results),'histogram':{str(z):n for z,n in counts.items()},'cases':results}
        print('EXACT_PASS k=',k,'cases=',len(results),'histogram=',counts,flush=True)
        partial_optimum.cache_clear(); total.cache_clear()
        for cache in mask_to_root:cache.cache_clear()
    out.write_text(json.dumps(archive,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print('OUTPUT_SHA256',hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
    return archive

if __name__=='__main__':
    assert len(sys.argv)==4
    verify(*(Path(x) for x in sys.argv[1:]))
