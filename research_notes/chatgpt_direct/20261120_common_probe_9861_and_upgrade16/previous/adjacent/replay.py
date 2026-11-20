"""Bound label changes between consecutive globally optimal budgets 14 to 21."""
import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from functools import cache
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent

def verify(previous):
    third = previous/'previous/previous/previous'
    second = third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS'] = str(second)
    sys.path[:0] = [str(third/'group'),str(second/'curve'),str(second/'bounds')]
    from generate import maps
    from verify import lower, MINIMA
    from cyclic11 import observations, class_cost
    from prior_bounds import observation_file
    lin, tr, _ = maps()
    bad, menus = observations()
    seeds = defaultdict(set)
    with TemporaryDirectory() as tmp:
        w = Path(tmp)
        observation_file(w/'observations')
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++17', HERE.parent/'nesting/bank.cpp','-o',w/'enumerate'], check=True)
        subprocess.run([w/'enumerate',w/'observations',w/'seeds'], stdout=subprocess.DEVNULL, check=True)
        for line in (w/'seeds').read_text().splitlines():
            s,c,*pts = map(int,line.split())
            if 5<=s<=9:
                assert c==MINIMA[s]
                seeds[s].add(tuple(pts))

    def mask(xs):
        return sum(1<<x for x in xs)

    banks = {}
    for size, reps in seeds.items():
        images = {tuple(sorted(g[x] for x in r)) for r in reps for g in lin}
        banks[size] = {mask(t[x] for x in r) for r in images for t in tr}

    @cache
    def intersection(a,b):
        if a==b:
            return a
        if a>b:
            return intersection(b,a)
        # Some affine image of the larger member appears among these seeds.
        return max((base&other).bit_count() for base in map(mask,seeds[b]) for other in banks[a])

    available = json.loads((HERE/'witness.json').read_text())
    output = {}
    for k in range(14,21):
        proof = available[str(k)]
        for n,key in ((k,'old'),(k+1,'new')):
            rows = proof[key]
            assert len(rows)==n and sorted(sum(rows,[]))==list(range(125))
            assert all(mask(r) in banks[len(r)] for r in rows)
            assert not any(bad[x][y]>>z&1 for r in rows for x,y,z in combinations(sorted(r),3))
            assert sum(class_cost(r,menus) for r in rows)==lower(125,n)
            s, rem = divmod(125,n)
            assert all(t in {s,s+bool(rem)} for t in range(1,14) if MINIMA[t]+lower(125-t,n-1)==lower(125,n))
        a, rem_a = divmod(125,k)
        b, rem_b = divmod(125,k+1)
        sizes = [a]*(k-rem_a)+[a+1]*rem_a
        @cache
        def matching(i,small,large):
            if i==k:
                return 0
            values = []
            if small:
                values.append(intersection(sizes[i],b)+matching(i+1,small-1,large))
            if large:
                values.append(intersection(sizes[i],b+1)+matching(i+1,small,large-1))
            return max(values)
        bound = 125-matching(0,k+1-rem_b,rem_b)
        changed = 125-sum(len(set(r)&set(t)) for r,t in zip(proof['old'],proof['new']))
        assert bound<=changed==proof['changed']
        output[str(k)] = [bound,changed]
    return {'adjacent_moved_histories_bounds':output,
            'maximal_single_intersections':{f'{a},{b}':intersection(a,b) for a in range(5,10) for b in range(a,10)}}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',required=True,type=Path)
    print(json.dumps(verify(parser.parse_args().previous.resolve()),indent=2,sort_keys=True))
