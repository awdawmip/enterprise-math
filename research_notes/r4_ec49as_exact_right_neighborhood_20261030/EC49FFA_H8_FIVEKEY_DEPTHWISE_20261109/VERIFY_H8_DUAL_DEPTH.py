#!/usr/bin/env python3
"""Recheck all H8 five-key BRC/signed-X6 prefix-disjoint certificates."""
import sys,json,collections,itertools
from h8_key_depth_sieve import (eligible,words,counts,all_groups,prefixes,signed_steps,
                               build_inventories,LETTERS,NEXT,OBS)
SCI='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def verify(late, certificate_path, expected_total, expected_min):
    mixed=8
    late=tuple(map(int,late))
    group_labels=all_groups(mixed,late)
    assert len(group_labels)==23
    inventories,st,_=build_inventories(mixed,late)
    assert len(inventories)==expected_total,(len(inventories),expected_total)
    inventory_set=set(inventories)
    allkeys=set(itertools.chain.from_iterable(inventories))
    wordtotal=0
    for h,s in group_labels:
        for k in sorted(allkeys):
            for lab,w in words(h,k):
                if lab!=s:continue
                assert len(w)==h and k[2]==w.count('e')
                cnt=counts(h,k)
                assert cnt==(w.count('a'),w.count('c')+w.count('d'),w.count('f'),w.count('g'))
                state=0
                for c in w:state=NEXT[state][LETTERS.index(c)]
                assert OBS[state]==lab
                pos=[0]*6
                for step in signed_steps(w):pos[abs(step)-1]+=1 if step>0 else -1
                assert pos==[2,0,0,0,0,0],(h,s,k,w)
                wordtotal+=1
    seen=set(); dist=collections.Counter(); lines=0
    with open(certificate_path,encoding='utf-8') as f:
        for line in f:
            rec=json.loads(line)
            keys=tuple(sorted(tuple(key) for key in rec['keys']))
            assert len(keys)==5 and len(set(keys))==5 and keys in inventory_set
            assert keys not in seen
            seen.add(keys)
            D=rec['D']
            assert len(D)==20
            lb=0
            for d,sel in enumerate(D,1):
                assert len(sel)==len(set(sel)) and all(0<=j<23 for j in sel)
                seen_pref=set()
                for group_id in sel:
                    h,s=group_labels[group_id]
                    merged=set()
                    for k in keys:
                        X=prefixes(h,k,s)
                        if X:
                            # Every eligible word using a fixed key has the same length.
                            assert max(X)>=d,(keys,h,s,d)
                            merged.update(X[d])
                    assert merged,(keys,h,s,d)
                    assert seen_pref.isdisjoint(merged),(keys,d,group_id)
                    seen_pref.update(merged)
                lb+=len(sel)
            assert lb==rec['lower_bound'] and lb>=expected_min
            dist[lb]+=1
            lines+=1
    assert len(seen)==len(inventory_set)==expected_total
    assert min(dist)==expected_min,(min(dist),expected_min)
    return {'status':'EXACT_INTEGER_PASS','late_high_set':''.join(map(str,late)),
            'total_verified':lines,'signature_feasible_inventories':len(inventory_set),
            'native_prefix_lower_bound_min':min(dist),'maximum_certified_lower_bound':max(dist),
            'endpoint_label_word_checks':wordtotal,'bound_distribution':dict(sorted(dist.items()))}

if __name__=='__main__':
  late=sys.argv[1];pat=sys.argv[2]
  target={'5689':(5472,98),'5789':(9216,96)}[late]
  print(json.dumps(verify(late,pat,*target),sort_keys=True))
