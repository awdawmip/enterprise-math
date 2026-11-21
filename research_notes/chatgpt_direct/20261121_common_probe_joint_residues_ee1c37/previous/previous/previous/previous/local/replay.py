"""Check the edit distance and class replacements needed to improve the threefold witness."""
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def verify(previous, groups, jobs):
    last=previous/'previous'
    ancient=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(ancient)
    sys.path[:0]=[str(last/'group'),str(ancient/'curve'),str(ancient/'bounds')]
    from generate import maps,observation_file
    from cyclic11 import observations,class_cost
    rows=list(map(tuple,json.loads(groups.read_text())))
    source=set(rows);bad,obs=observations()
    costs=[class_cost(x,obs) for x in rows]
    assert sum(costs)==9996
    masks=[sum(1<<p for p in x) for x in rows]
    linear,translations,_=maps()
    stabilizer=[]
    for a in linear:
        for b in translations:
            g=[b[i]for i in a];images=[tuple(sorted(g[x]for x in row))for row in rows]
            if set(images)==source:stabilizer.append([rows.index(i)for i in images])
    assert len(stabilizer)==3
    options=sorted({min(tuple(sorted(g[i]for i in subset))for g in stabilizer)for subset in combinations(range(12),6)})
    with TemporaryDirectory()as tmp:
        w=Path(tmp)
        observation_file(w/'obs')
        for name,path in [('near',HERE/'nearby.cpp'),('free',last/'twelve/neighborhood.cpp')]:
            subprocess.run(['c++','-O3','-mpopcnt','-std=c++20',path,'-o',w/name],check=True)
        def parts(m):return f'{m%(1<<64)} {m>>64}'
        (w/'rows').write_text(''.join(parts(m)+'\n'for m in masks))
        proc=subprocess.run([w/'near',w/'obs',w/'rows','2','2','9995'],check=True,capture_output=True,text=True)
        sentinel,nodes=map(int,proc.stdout.split());assert sentinel==9996
        counts=[int(line.split()[1])for line in proc.stderr.splitlines()]
        with (w/'regions').open('w')as f:
            for subset in options:print(parts(sum(masks[i]for i in subset)),6,9996-sum(costs[i]for i in subset),file=f)
        def run(start):
            res=subprocess.check_output([w/'free',w/'obs',w/'regions',str(start),str(min(start+4,len(options))),'9995'],text=True)
            data=[list(map(int,l.split())) for l in res.splitlines()]
            assert all(len(r)==3 and r[-1]==0 for r in data)
            return sum(n for j,n,z in data)
        with ThreadPoolExecutor(max_workers=jobs)as pool:visits=sum(pool.map(run,range(0,len(options),4)))
        return dict(budget=9995,nearby_row_candidates=counts,nearby_nodes=nodes,nearby_feasible=False,
                    six_representatives=len(options),six_nodes=visits,six_feasible=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--groups',type=Path,default=HERE.parent/'c3/groups.json');p.add_argument('--jobs',type=int,default=3)
    a=p.parse_args();print(json.dumps(verify(a.previous.resolve(),a.groups.resolve(),a.jobs),sort_keys=True,indent=2))
