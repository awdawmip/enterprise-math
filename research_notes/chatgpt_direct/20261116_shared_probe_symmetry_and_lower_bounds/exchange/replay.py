"""Certify a lower bound on the replacement distance from the 8723-read table."""
from argparse import ArgumentParser
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent

def check(older,groupdir,table,radius,workers):
    sys.path[:0]=[str(older/'curve'),str(older/'bounds'),str(groupdir)]
    import generate
    generate.BASE=older
    lin,trans,_=generate.maps()
    groups=json.loads(table.read_text())
    assert len(groups)==13 and sorted(p for g in groups for p in g)==list(range(125))
    masks=[sum(1<<p for p in g) for g in groups]
    with TemporaryDirectory() as tmp:
        work=Path(tmp)
        rows=generate.bank(work,lin,trans,8728)
        keys=list(rows)
        reverse={m:i for i,k in enumerate(keys) for m in rows[k]}
        kind=[reverse[m] for m in masks]
        assert sum(keys[i][1] for i in kind)==8723
        profiles=[(p,v) for p,v in generate.profiles(keys,8728) if p<8723]
        assert len(profiles)==18
        with (work/'rows').open('w')as stream:
            print(len(keys),file=stream)
            for s,c in keys:
                print(s,c,len(rows[s,c]),file=stream)
                for m in rows[s,c]:print(m%(1<<64),m>>64,file=stream)
        with (work/'profiles').open('w')as stream:
            for p,v in profiles:print(p,*v,file=stream)
        with (work/'incumbent').open('w')as stream:
            for m in masks:print(m%(1<<64),m>>64,file=stream)
        def expected(k):
            valid=set()
            for selection in combinations(range(13), k):
                removed=sum(1<<i for i in selection)
                fixed=Counter(t for i,t in enumerate(kind) if i not in selection)
                for n,(p,v) in enumerate(profiles):
                    if all(v[t]>=j for t,j in fixed.items()):valid.add((removed,n,p))
            return valid
        exe=work/'trade'
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/'trade.cpp'),'-o',str(exe)],check=True)
        def task(j):
            out=subprocess.check_output([str(exe),str(work/'rows'),str(work/'profiles'),str(work/'incumbent'),'1',str(radius),str(j),str(workers)],text=True,cwd=work)
            return [tuple(map(int,l.split())) for l in out.splitlines()]
        with ThreadPoolExecutor(max_workers=workers)as pool:
            results=[r for batch in pool.map(task,range(workers)) for r in batch]
    summary=[]
    for k in range(1,radius+1):
        r=[z for z in results if z[0]==k]
        assert set((mask,n,c) for _,mask,n,c,_,_ in r)==expected(k)
        assert len(r)==len({(mask,n,c) for _,mask,n,c,_,_ in r})
        assert not any(ok for *_,ok in r)
        summary.append({'replacements':k,'possible_subsets':comb(13,k),'compatible_subset_profiles':len(r),'nodes':sum(z[4]for z in r)})
    return {'certified_radius':radius,'lower_cost_profiles':len(profiles),'details':summary}

if __name__=='__main__':
    p=ArgumentParser()
    p.add_argument('--older',required=True,type=Path);p.add_argument('--group',required=True,type=Path)
    p.add_argument('--table',required=True,type=Path);p.add_argument('--jobs',type=int,default=3)
    p.add_argument('--radius',type=int,default=None)
    a=p.parse_args()
    d=a.radius or json.loads((HERE/'result.json').read_text())['certified_radius']
    print(json.dumps(check(a.older.resolve(),a.group.resolve(),a.table.resolve(),d,a.jobs),indent=2))
