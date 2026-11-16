"""Self-similar one-probe covers. Run with --full to enumerate all 9-component inputs."""
from itertools import product
from collections import Counter
from pathlib import Path
from math import ceil
import json
import sys
from verify_paired import coset_cover, laminar, syndrome

D = Path(__file__).parent
Q = range(5)


def verify(full):
    rec = json.loads((D/'family_pair.json').read_text())
    rows, outer, seven = coset_cover(rec['base'])
    further_rows, extra, _ = coset_cover(rec['additional'])
    assert rows == further_rows == [[1,0,0,1]*2,[0,1,0,1]*2,[0,0,1,1]*2]
    for s, (_, w) in extra.items():
        outer.setdefault(s, (7,w))
    missing = sorted(set(product(Q,repeat=3))-set(outer))
    assert seven == [16]*7 and len(missing) <= 1
    # The 4D fill is stored as base-5 indices in the exact 64 classes.
    four = json.loads((D/'four_filler.json').read_text())['groups']
    assert sorted(i for g in four for i in g) == list(range(625))
    for g in four:
        assert laminar([tuple((i // 5**k) % 5 for k in (3,2,1,0)) for i in g])
    assert len(four)==64
    rows5, inner, sizes5 = coset_cover(json.loads((D/'paired_certificate.json').read_text())['five'])
    assert len(inner)==25 and sum(sizes5)==25
    U8 = len(rec['base']['classes']+rec['additional']['classes'])*5**5 + len(missing)*5*len(four)
    U9 = 8*5**6 + len(missing)*5*len(sizes5)*5**3
    U12 = 7*5**9 + (125-sum(seven))*5*U8
    results = dict(seven_sizes=seven,syndromes=len(outer),missing=missing,
                   eight=U8,nine=U9,twelve=U12,
                   asymptotic="16 M(n)/5^n <= 1+15*(13/125)^floor(n/8)")
    if full:
        bins = Counter()
        for pair_sums in product(Q,repeat=4):
            t = pair_sums[3]
            s = tuple((v+t)%5 for v in pair_sums[:3])
            for free in product(Q, repeat=4):
                w8 = free+tuple((z-v)%5 for z,v in zip(pair_sums,free))
                if s in outer:
                    k,w = outer[s]
                    shift = tuple((x-y)%5 for x,y in zip(w8,w))
                    for v in Q:
                        bins[(0,k,shift,v)]+=1
                else:
                    for v in Q:
                        z=free+(v,)
                        k,w=inner[syndrome(z,rows5)]
                        bins[(1,s,t,k,tuple((a-b)%5 for a,b in zip(z,w)))]+=1
        assert len(bins)==U9 and sum(bins.values())==5**9
        assert max(bins.values())<=16
        results.update(enumerated=sum(bins.values()),size_histogram=dict(sorted(Counter(bins.values()).items())))
    return results


if __name__ == '__main__':
    print(json.dumps(verify('--full' in sys.argv),indent=2))
