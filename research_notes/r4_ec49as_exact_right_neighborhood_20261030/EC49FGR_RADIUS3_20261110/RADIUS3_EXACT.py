#!/usr/bin/env python3
"""Frozen BRC exact radius-three obstruction for original EC49FGJ A/B seven-key 94-edge witnesses.
All 3-replacement candidates within <=7 keys use original 7 raw keys, by H2/H3 key-forcing lemma.
"""
import sys,json,itertools,collections,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).parent))
import EC49FGQ_TWO_SWAP_EXACT as M
P=pathlib.Path(__file__).parent
ROOT=json.loads((P/'EC49FGJ_SEVEN_KEY_94_WITNESSES.json').read_text())

def solve(profile):
    oldkeys=set(map(tuple,profile['allowed_keys']))
    base={(d['window'],d['signature']):d['word'] for d in profile['demands']}
    all_labels=M.LABELS
    assert set(base)==set(all_labels)
    ids={}
    def mask(w):
        val=0
        for prefix in M.micro_prefixes(w):
            idx=ids.setdefault(prefix,len(ids))
            val|=1<<idx
        return val
    options=collections.defaultdict(set)
    for h in M.REQ:
        for k in oldkeys:
            for s,w in M.words(h,k):
                assert M.key_of(w)==k
                options[h,s].add(mask(w))
    baseline={label:mask(word) for label,word in base.items()}
    original_union=0
    for x in baseline.values():original_union|=x
    assert original_union.bit_count()==94
    assert len({M.key_of(x) for x in base.values()})==7
    # Complete h=2/h=3 low-window support computed without a 7-key restriction:
    # H2 s16 -> {(3,0,1)}, s32 -> {(2,1,1)};
    # H3 s16 -> {(3,1,1),(4,0,1)}, s32 -> {(3,1,1),(2,2,1)}.
    H2={(2,16):(3,0,1),(2,32):(2,1,1)}
    H3={(3,16):{(3,1,1),(4,0,1)},(3,32):{(3,1,1),(2,2,1)}}
    assert all(M.key_of(base[label])==k for label,k in H2.items())
    stats=collections.Counter();buckets=collections.Counter();cases=[];min_left=None;pair_test=0;triple_test=0;first_example=None
    for triple in itertools.combinations(all_labels,3):
        fixed=0;used=set()
        for label,w in base.items():
            if label not in triple:
                fixed|=baseline[label]
                used.add(M.key_of(w))
        B=93-fixed.bit_count();buckets[B]+=1
        if B<0:stats['fixed_reject']+=1;continue
        stats['screened']+=1
        missing=oldkeys-used
        if missing:
            h2={H2[label] for label in triple if label in H2}
            other=missing-h2
            if other:
                assert other=={(3,1,1)},(triple,missing)
                assert {(3,16),(3,32)}.issubset(triple)
                assert H3[(3,16)] & H3[(3,32)] == {(3,1,1)}
                # Six fixed cache keys remain. Both H3 signatures must use the common
                # (3,1,1) key or distinct new keys; two new keys exceed budget 7.
                stats['forced_h3_class']+=1
            else:stats['forced_h2_class']+=1
        else:stats['no_released_key_class']+=1
        sets=[]
        for label in triple:
            choices={delta for mask0 in options[label] if (delta:=mask0 &~fixed).bit_count()<=B}
            sets.append(choices)
        if any(not x for x in sets):stats['empty_label_filter']+=1;continue
        sets.sort(key=len)
        unionpair=set()
        for a in sets[0]:
            for b in sets[1]:
                pair_test+=1
                z=a|b
                if z.bit_count()<=B:unionpair.add(z)
        if not unionpair:stats['empty_pair_filter']+=1;continue
        hits=0
        for u in unionpair:
            for v in sets[2]:
                triple_test+=1
                if (u|v).bit_count()<=B:
                    hits+=1
                    if first_example is None:first_example=(triple,B,u,v)
                    break
            if hits:break
        if hits:stats['at_least_one_93_completion']+=1
        else:stats['exhaustive_three_set_reject']+=1
        cases.append({'triple':[list(k) for k in triple],'budget':B,'sizes':[len(x) for x in sets],'pair_unions':len(unionpair),'success':bool(hits)})
    assert stats['fixed_reject']+stats['screened']==2024
    print(profile['profile_id'],'stats',dict(stats),'pair_tests',pair_test,'triple_tests',triple_test,'first_example',first_example,flush=True)
    return {'profile':profile['profile_id'],'stats':dict(stats),'budget_distribution':dict(sorted(buckets.items())),'pair_mask_tests':pair_test,'triple_mask_tests':triple_test,'total_label_triples':2024,'completed':stats['at_least_one_93_completion']==0,'first_found':str(first_example),'full_screened_triple_details':cases}

if __name__=='__main__':
    assert ROOT['frozen_scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
    reports={'schema':'EC49FGR_EXACT_RADIUS3_AUDIT_V1','frozen_scientific_pin':ROOT['frozen_scientific_pin'],'profiles':[solve(profile) for profile in ROOT['profiles']]}
    out=P/'EXACT_RADIUS3_AUDIT.json';out.write_text(json.dumps(reports,indent=2)+'\n')
    print('OUTPUT',out,flush=True)
