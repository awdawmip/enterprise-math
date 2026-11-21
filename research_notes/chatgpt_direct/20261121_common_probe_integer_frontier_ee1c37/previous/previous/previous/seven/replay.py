"""Can a strict 9996 improvement preserve any five message classes?"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent

def regions(previous,weights):
    r3=previous/'previous/previous';r2=r3/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(r2)
    sys.path[:0]=[str(r3/'group'),str(r2/'curve'),str(r2/'bounds')]
    from generate import maps
    from verify import lower,MINIMA
    from cyclic11 import observations,class_cost
    source=[tuple(r)for r in json.loads((previous/'c3/groups.json').read_text())]
    L,T,_=maps()
    actions=[]
    for a in L:
        for b in T:
            g=[b[i]for i in a]
            images=[tuple(sorted(g[p]for p in row))for row in source]
            if set(images)==set(source):actions.append([source.index(r)for r in images])
    assert len(actions)==3
    raw=list(combinations(range(12),7))
    representatives=sorted({min(tuple(sorted(g[j]for j in s))for g in actions)for s in raw})
    assert len(raw)==792 and len(representatives)==270
    _,pair=observations();prices=[class_cost(r,pair)for r in source]
    assert sum(prices)==9996
    jobs=[]
    for i,s in enumerate(representatives):
        if str(i)not in weights:continue
        free={p for j in s for p in source[j]};n=len(free)
        budget=sum(prices[j]for j in s)-1
        caps=[budget-lower(n-v,6)for v in range(14)]
        first=next(v for v in range(1,14)if caps[v]>=MINIMA[v])
        m=sum(1<<p for p in free)
        w=weights[str(i)];assert len(w)==126
        jobs.append([i,m%(1<<64),m>>64,budget,first,*caps,*w])
    return jobs

def verify(previous,workers):
    weights=json.loads((HERE/'weights.json').read_text())
    jobs=regions(previous,weights)
    assert len(jobs)==270
    from prior_bounds import observation_file
    with TemporaryDirectory()as d:
        work=Path(d);observation_file(work/'menu')
        subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',HERE/'check.cpp','-o',work/'check'],check=True)
        (work/'jobs').write_text(''.join(' '.join(map(str,j))+'\n'for j in jobs))
        def check(job):
            out=subprocess.check_output([work/'check',work/'menu',work/'jobs',str(job[0])],text=True)
            objective,total,active,nodes,found,*witness=map(int,out.split())
            assert not found and not witness
            return dict(region=job[0],checked_classes=total,weighted_candidates=active,cover_nodes=nodes)
        with ThreadPoolExecutor(max_workers=workers)as ex:
            cases=list(ex.map(check,jobs))
    return dict(budget=9995,source_price=9996,fixed_labels=5,repartitioned_labels=7,raw_subsets=792,
                symmetry_representatives=270,feasible=False,
                legal_candidates=sum(s['checked_classes']for s in cases),
                weighted_candidates=sum(s['weighted_candidates']for s in cases),
                cover_nodes=sum(s['cover_nodes']for s in cases),cases=cases)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--jobs',type=int,default=2)
    a=p.parse_args();print(json.dumps(verify(a.previous.resolve(),a.jobs),indent=2,sort_keys=True))
