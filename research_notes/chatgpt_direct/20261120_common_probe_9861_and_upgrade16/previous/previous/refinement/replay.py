"""Rebuild all single-split bounds and the optimal adjacent-budget classification."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from functools import cache
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def analyze(previous, jobs, eleven_floor, twelve_floor):
    fourth = previous / 'previous'
    third = fourth / 'previous'
    second = third / 'previous'
    sys.path[:0] = [str(second/'bounds'), str(second/'curve')]
    from prior_bounds import observation_file
    from verify import lower, MINIMA, cheap_line_partitions
    from cyclic11 import class_cost, observations

    bad, menus = observations()

    @cache
    def split(row):
        parent_cost = class_cost(row, menus)
        best = -1
        winner = ()
        for size in range(1, len(row)//2 + 1):
            if parent_cost - MINIMA[size] - MINIMA[len(row)-size] <= best:
                continue
            for first in combinations(row, size):
                other = set(row).difference(first)
                gain = parent_cost - class_cost(first, menus) - class_cost(other, menus)
                if gain > best:
                    best, winner = gain, first
        return best, winner

    def check_table(groups):
        assert sorted(x for r in groups for x in r) == list(range(125))
        assert all(not any(bad[x][y] >> z & 1 for x,y,z in combinations(r,3)) for r in groups)
        rows = [tuple(sorted(r)) for r in groups]
        options = [split(row) for row in rows]
        gain = max(t for t, _ in options)
        j = next(i for i in range(len(rows)) if options[i][0] == gain)
        parent_cost = sum(class_cost(r, menus) for r in rows)
        return dict(cost=parent_cost, saving=gain, refined=parent_cost-gain, parent=rows[j], child=options[j][1])

    budgets = {'11': (11, eleven_floor, 11292), '12': (12, twelve_floor, 9996)}
    def decode(raw, spec, mode):
        out = {}
        for line in raw.splitlines():
            w = list(map(int, line.split()))
            size, visited, examined, tested = w[:4]
            data = dict(normalized_visits=visited, classes_priced=examined, splits_priced=tested)
            for n,key in enumerate(('maximum_gain','minimum_fine_cost')):
                start = 4+n*(size+2)
                val, left = w[start:start+2]
                if left == 0:
                    assert examined == 0
                    data[key] = None
                    continue
                p = w[start+2:start+2+size]
                one = [x for j,x in enumerate(p) if left >> j & 1]
                two = set(p).difference(one)
                assert len(p)==size and one and two and not any(bad[x][y] >> z & 1 for x,y,z in combinations(p,3))
                parent = class_cost(p, menus)
                children = class_cost(one, menus)+class_cost(two, menus)
                if mode=='minimum': assert parent==MINIMA[size]
                tail = 0
                if spec is not None:
                    k, floor, ceiling = spec
                    necessary = lower(125-size,k-1)
                    assert parent+necessary<=ceiling
                    tail = max(necessary,floor-parent)
                assert val==(parent-children if n==0 else children+tail)
                data[key]=dict(value=val, parent=p, first_child=one, parent_cost=parent, children_cost=children)
            out[size]=data
        assert set(out)==set(range(2,14))
        return out

    with TemporaryDirectory() as folder:
        w = Path(folder)
        observation_file(w/'observation')
        subprocess.run([os.environ.get('CXX','c++'),'-std=c++17','-O3','-mpopcnt',HERE/'split.cpp','-o',w/'check'],check=True)
        modes = [('all','all',None),('minimum','minimum',None)]
        for name,(k,lb,ub) in budgets.items():
            modes.extend([(name+'_any','joint',(k,lb,31250)),(name+'_competitive','joint',(k,lb,ub))])
        def run(args):
            name,mode,spec=args
            stdin = ''
            if spec:
                k,lb,ub=spec
                stdin=' '.join(map(str,[ub,lb,*[lower(125-s,k-1) for s in range(14)]]))
            raw=subprocess.check_output([w/'check',w/'observation',mode],text=True,input=stdin)
            return name, decode(raw,spec,mode)
        with ThreadPoolExecutor(jobs)as pool:
            census=dict(pool.map(run,modes))

    optimal = {}
    values = json.loads((second/'curve/values.json').read_text())
    for k in range(13,125):
        if k==13:
            # The previous exact classification gives a single affine orbit.
            groups=json.loads((third/'asymmetric8721/groups.json').read_text())
        elif k==17:
            groups=json.loads((HERE/'optimal17.json').read_text())
        else:
            groups=cheap_line_partitions(k)
        row=check_table(groups)
        if k>=14:
            assert row['cost']==lower(125,k)==values[str(k)]
            sizes=[s for s in range(2,14) if MINIMA[s]+lower(125-s,k-1)==row['cost']]
            best=max(census['minimum'][s]['maximum_gain']['value'] for s in sizes)
            assert best==row['saving'], (k,best,row)
        row['gap_to_next']=row['refined']-values[str(k+1)]
        optimal[k]=row
    special_eleven=json.loads((fourth/'eleven_six_counts/groups.json').read_text())
    special_eleven.append(json.loads((previous/'eleven_equal/groups.json').read_text()))
    special={'symmetric_eleven_optima':[check_table(g)for g in special_eleven],
             'threefold_twelve_optimum':check_table(json.loads((previous/'c3/groups.json').read_text()))}
    summary={}
    for name,spec in budgets.items():
        summary[name]={}
        for scope in ('any','competitive'):
            rng=census[name+'_'+scope]
            summary[name][scope]=dict(saving_at_most=max(v['maximum_gain']['value']for v in rng.values()if v['maximum_gain']),
                    fine_cost_at_least=min(v['minimum_fine_cost']['value']for v in rng.values()if v['minimum_fine_cost']))
    compatible=[k for k,row in optimal.items() if row['gap_to_next']==0]
    assert compatible==list(range(62,125))
    assert summary['11']['any']['fine_cost_at_least']>9996 and summary['12']['any']['fine_cost_at_least']>8721
    return dict(coarse_floors=[eleven_floor,twelve_floor],small_budgets=summary,
                optimal_coarse=optimal,compatible_first_budgets=compatible,special_tables=special,census=census)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',required=True,type=Path)
    p.add_argument('--jobs',type=int,default=3)
    p.add_argument('--eleven-floor',type=int,default=11119)
    p.add_argument('--twelve-floor',type=int,default=9847)
    a=p.parse_args()
    print(json.dumps(analyze(a.previous.resolve(),a.jobs,a.eleven_floor,a.twelve_floor),indent=2,sort_keys=True))
