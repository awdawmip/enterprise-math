"""Bound the possible number of common intact labels for global 13 and 14 optima."""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent

def solve(previous, jobs):
    third = previous/'previous/previous'
    second = third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS'] = str(second)
    sys.path[:0] = [str(third/'group'), str(second/'bounds')]
    from generate import maps
    from prior_bounds import observation_file
    from cyclic11 import class_cost, observations
    linear, translations, _ = maps()
    bad, menus = observations()
    mask = lambda row: sum(1 << x for x in row)
    coarse = json.loads((third/'asymmetric8721/groups.json').read_text())
    fine = json.loads((HERE/'witness14.json').read_text())
    for table, size, cost in ((coarse,13,8721), (fine,14,7660)):
        assert sorted(sum(table,[])) == list(range(125)) and len(table)==size
        assert not any(bad[x][y]>>z&1 for row in table for x,y,z in combinations(row,3))
        assert sum(class_cost(row,menus)for row in table)==cost
    shared = sorted(set(map(mask,coarse)) & set(map(mask,fine)))
    assert len(shared)==2
    with TemporaryDirectory() as temp:
        work = Path(temp)
        observation_file(work/'obs')
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',second/'curve/class_minima.cpp','-o',work/'seeds_exe'],check=True)
        subprocess.run([work/'seeds_exe',work/'obs',work/'seeds'],stdout=subprocess.DEVNULL,check=True)
        subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',HERE/'cover.cpp','-o',work/'cover'],check=True)
        def write_masks(name, masks):
            (work/name).write_text(''.join(f'{m % 2**64} {m >> 64}\n'for m in masks))
        write_masks('keep9', [mask(r) for r in coarse if len(r)==9])
        seeds={8:set(),9:set()}
        for line in (work/'seeds').read_text().splitlines():
            s,c,*r=map(int,line.split())
            if (s,c) in ((8,419),(9,557)):
                seeds[s].add(tuple(r))
        totals={}
        for s, sets in seeds.items():
            normalized={tuple(sorted(g[x]for x in r)) for g in linear for r in sets}
            rows={mask(t[x]for x in r)for t in translations for r in normalized}
            totals[str(s)] = len(rows)
            write_masks('full'+str(s), sorted(rows))
        assert totals=={'8':28000,'9':24000}
        def shard(i):
            out=subprocess.check_output([work/'cover',work,'4',str(i),'8'],text=True)
            return [list(map(int,l.split()))for l in out.splitlines()]
        with ThreadPoolExecutor(jobs) as pool:
            cases=sorted(q for l in pool.map(shard,range(8))for q in l)
    assert [c[0] for c in cases]==[j for j in range(512)if j.bit_count()==4]
    assert all(len(c)==3 and not c[2]for c in cases)
    assert sum(c[1]for c in cases)==95668112
    return dict(candidates=totals, cases=cases, nodes=sum(c[1]for c in cases), shared_minimum_attained=2,
                maximum_common_upper_bound=3, minimum_changed_interval=[10,11])

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True)
    parser.add_argument('--jobs',type=int,default=4)
    a=parser.parse_args()
    print(json.dumps(solve(a.previous.resolve(),a.jobs),indent=2,sort_keys=True))
