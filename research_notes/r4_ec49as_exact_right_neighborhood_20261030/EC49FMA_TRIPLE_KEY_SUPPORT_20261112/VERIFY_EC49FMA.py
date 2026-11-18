#!/usr/bin/env python3
"""Frozen BRC key-support census for ALL 3-key replacements of EC49FKX seed.
Run in PR checkout; reuses original pinned EC49FGW native-word generator.
"""
import sys, itertools, collections, math, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0,str(ROOT))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key

SEED={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def main():
    words=list(all_words())
    labs=sorted({label for label,w in words})
    bit={label:1<<i for i,label in enumerate(labs)}
    assert len(words)==178850 and len(labs)==24
    support=collections.defaultdict(int)
    for label,w in words:support[raw_key(w)] |= bit[label]
    assert len(support)==94 and SEED<=support.keys()
    outside=sorted(support.keys()-SEED); inside=sorted(SEED)
    assert len(outside)==87
    full=(1<<24)-1
    assert [k for k in support if support[k]&bit[(2,16)]]==[(3,0,1)]
    assert [k for k in support if support[k]&bit[(2,32)]]==[(2,1,1)]
    stats={}; allrows=[]
    for n in (2,3):
        adds=list(itertools.combinations(outside,n))
        addmask=[_union(support,ks) for ks in adds]
        rows=[]
        for removed in itertools.combinations(inside,n):
            missing=full & ~_union(support,SEED-set(removed))
            count=sum((mask&missing)==missing for mask in addmask)
            # Independent mask-frequency counting, without looping over added tuples.
            freq=collections.Counter(support[k]&missing for k in outside)
            alternate=_frequency_cover(freq,missing,n)
            assert count==alternate,(removed,count,alternate)
            rows.append({'removed':removed,'missing_bits':missing.bit_count(),'coverable':count})
        stats[n]={'total':len(rows)*len(adds),'coverable':sum(r['coverable'] for r in rows),
                  'uncoverable':len(rows)*len(adds)-sum(r['coverable'] for r in rows),
                  'zero_removed_classes':sum(r['coverable']==0 for r in rows)}
        if n==3:allrows=rows
    assert stats[2]=={'total':78561,'coverable':6315,'uncoverable':72246,'zero_removed_classes':13}
    assert stats[3]=={'total':3709825,'coverable':38169,'uncoverable':3671656,'zero_removed_classes':26}
    zero_extra=allrows[27]
    assert set(zero_extra['removed'])=={(3,1,1),(4,2,1),(6,4,1)}
    for demand,forced in [((3,16),(4,0,1)),((3,32),(2,2,1))]:
        assert {k for k in outside if support[k]&bit[demand]}=={forced}
    assert not any((support[k]&bit[(5,16)]) and (support[k]&bit[(8,1)]) for k in outside)
    report={'schema':'EC49FMA_TRIPLE_KEY_COVER_V1','science_pin':PIN,
      'model': 'full frozen nine-state BRC, native signed-X6 paths, 24 labels, key support only',
      'catalog_words':len(words),'keys':len(support),'seed':inside,
      'forced_global_keys':[(2,1,1),(3,0,1)],
      'seven_key_all':math.comb(94,7),'seven_key_after_forced':math.comb(92,5),
      'radius2_recheck':stats[2],'radius3':stats[3],
      'triple_removed_rows':allrows,
      'checker':'direct inserted-key enumeration and independent grouped-frequency count agree for each removed-key class',
      'remaining_problem':'Exact ordered signed native-prefix cost on 38169 coverable triple-key replacements'}
    print(json.dumps(report,indent=2))
    print('EC49FMA_FULL_TRIPLE_SUPPORT_EXACT_PASS')

def _union(support,keys):
    m=0
    for k in keys:m |= support[k]
    return m

def _frequency_cover(freq,missing,n):
    masks=sorted(freq)
    if n==2:
        z=sum(freq[a]*freq[b] for a,b in itertools.combinations(masks,2) if (a|b)==missing)
        return z+sum(math.comb(v,2) for k,v in freq.items() if k==missing)
    total=0
    for i,a in enumerate(masks):
        for j in range(i,len(masks)):
            b=masks[j]
            for t in range(j,len(masks)):
                c=masks[t]
                if (a|b|c)!=missing:continue
                if i==j==t: total+=math.comb(freq[a],3)
                elif i==j: total+=math.comb(freq[a],2)*freq[c]
                elif j==t: total+=freq[a]*math.comb(freq[b],2)
                else: total+=freq[a]*freq[b]*freq[c]
    return total
if __name__=='__main__':main()
