#!/usr/bin/env python3
"""Independent literal native signed-prefix word enumeration, no support-profile/antichain pruning.
Verifies 48 pair and 48 triple saved obstructions across A and B.
"""
import json,itertools,hashlib,sys,random,collections
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'EC49FJR'))
import EC49FGW_RADIUS5_SCREEN as src
M={'a':[-1,-1], 'c':[1,2,-1,-2], 'd':[2,1,-2,-1], 'e':[3,1,1,-3], 'f':[1,-1], 'g':[2,-2]}

def concrete_prefixes(w):
    a=[];p=[]
    for ch in w:
        for v in M[ch]:
            p.append(v); a.append(tuple(p))
    return a

def key_of(w):
    p=[v for ch in w for v in M[ch]]
    return (p.count(1),p.count(2),p.count(3))

catalog=list(src.all_words());assert len(catalog)==178850
words=collections.defaultdict(list)
for lab,w in catalog:
    words[lab].append((key_of(w),concrete_prefixes(w)))

pair=json.loads(Path(__file__).with_name('EC49FJW_B9_PAIR_REPORT.json').read_text())
tri=json.loads(Path(__file__).with_name('EC49FJW_B9_TRIPLE_REPORT.json').read_text())
records=[]
for p,pr,tr in zip(src.W['profiles'],pair['profiles'],tri['profiles']):
    obs=[(d['window'],d['signature']) for d in sorted(p['demands'],key=lambda d:(d['window'],d['signature']))]
    original=[d['word'] for d in sorted(p['demands'],key=lambda d:(d['window'],d['signature']))]
    keys={key_of(w) for w in original}
    assert len(keys)==7
    pp=[set(concrete_prefixes(w)) for w in original]
    assert len(set().union(*pp))==94
    pair_w=[e for group in pr['groups'] for e in group['examples']]
    # deterministic uneven sample across 24 prefix backgrounds
    pair_samples=pair_w[:24] + pair_w[-24:]
    tri_samples=tr['certificates'][:24]+tr['certificates'][-24:]
    for typ,samples in [('pair',pair_samples),('triple',tri_samples)]:
        for z in samples:
            Q=z['positions'] if typ=='pair' else z['Q']
            pick=z['pair_positions'] if typ=='pair' else z['triple']
            F=set().union(*(pp[i] for i in range(24) if i not in Q))
            assert len(F)==84 and len(Q)==7
            opts=[]
            for i in pick:
                lab=obs[i]
                unique={frozenset(x for x in prefixes if x not in F) for k,prefixes in words[lab] if k in keys}
                b9=[s for s in unique if len(s)<=9]
                assert b9
                opts.append(b9)
            count=0;good=False;minimum=1000
            for prod in itertools.product(*opts):
                count+=1
                cost=len(set().union(*prod))
                if cost<minimum:minimum=cost
                if cost<=9:good=True;break
            assert not good, (p['profile_id'],typ,Q,pick)
            records.append({'profile':p['profile_id'],'type':typ,'Q':Q,'labels':[list(obs[i]) for i in pick],'filtered_tuple_count':count,'least_filtered_union':minimum,'certified_no_9_union':True})
print('INDEPENDENT_DIRECT_CHECK_PASS',len(records),collections.Counter((x['profile'],x['type']) for x in records))
path=Path(__file__).with_name('EC49FJW_DIRECT_CHECK_REPORT.json')
path.write_text(json.dumps({'schema':'EC49FJW_DIRECT_LITERAL_WORDS_AUDIT_V1','samples':records,'source_pin':src.PIN,'method':'direct literal signed X6 word prefixes and full-key tuples without antichain or original-prefix support data'},indent=2)+'\n')
print('DIRECT_REPORT_SHA256',hashlib.sha256(path.read_bytes()).hexdigest())
