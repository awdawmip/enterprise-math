"""Compute all minima with the given three old fixed classes and nine arbitrary ten-point classes."""
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent
CAP=6804

def solve(previous,jobs):
    second=previous/'previous/previous/previous'
    sys.path.insert(0,str(second/'bounds'))
    from cyclic11 import class_cost,observations
    from prior_bounds import observation_file
    bad,menus=observations()
    known=json.loads((previous/'c3/groups.json').read_text())
    fixed=known[:3]
    assert [class_cost(r,menus)for r in fixed]==[1296,1296,600]
    free=set(range(125)).difference(*fixed)
    assert len(free)==90
    mask=sum(1<<i for i in free)
    weights=json.loads((HERE/'weights.json').read_text())
    with TemporaryDirectory()as tmp:
        w=Path(tmp)
        (w/'weights').write_text(' '.join(map(str,weights)))
        observation_file(w/'obs')
        for name in ('rows','cover'):
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/(name+'.cpp'),'-o',w/name],check=True)
        with (w/'rows.txt').open('w')as f:
            subprocess.run([w/'rows',w/'obs'],input=f'{mask%2**64} {mask>>64} 10 10 {CAP-8*744}\n',text=True,stdout=f,check=True)
        lines=(w/'rows.txt').read_text().splitlines()
        census={};united=0
        for line in lines:
            lo,hi,size,price=map(int,line.split());m=(hi<<64)|lo
            assert size==10 and not m&~mask and m.bit_count()==10 and m not in census
            assert sum(weights[i] for i in free if m>>i&1)<=1000*price
            census[m]=price;united|=m
        assert united==mask
        def run(i):
            cmd=[w/'cover',w/'rows.txt',w/'weights',str(CAP),str(i),'8']
            run=subprocess.run(cmd,text=True,capture_output=True,check=True)
            last=run.stderr.splitlines()[-1].split();assert last[0]=='done'
            tables=[]
            for line in run.stdout.splitlines():
                parts=list(map(int,line.split()))
                assert len(parts)==18
                masks=[(hi<<64)|lo for lo,hi in zip(parts[::2],parts[1::2])]
                rows=[[i for i in free if m>>i&1]for m in masks]
                assert sorted(sum(rows,[]))==sorted(free)
                assert all(not any(bad[x][y]>>z&1 for x,y,z in combinations(r,3))for r in rows)
                assert sum(class_cost(row,menus)for row in rows)==sum(census[m]for m in masks)==CAP
                allrows=tuple(sorted(tuple(sorted(r))for r in fixed+rows))
                g=lambda i:25*(i//5%5)+5*(i%5)+i//25
                assert tuple(sorted(tuple(sorted(g(i)for i in r))for r in allrows))==allrows
                tables.append(allrows)
            return int(last[1]),int(last[2]),tables
        with ThreadPoolExecutor(jobs)as pool:
            runs=list(pool.map(run,range(8)))
    tables=[r for n,v,rs in runs for r in rs]
    assert len(set(tables))==len(tables)==2
    return dict(candidate_rows=len(census),first_choices=sum(n for n,v,rs in runs),visits=sum(v for n,v,rs in runs),
                minimum=3192+CAP, number=len(tables), partitions=sorted(tables))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',required=True,type=Path);p.add_argument('--jobs',type=int,default=4)
    a=p.parse_args();print(json.dumps(solve(a.previous.resolve(),a.jobs),indent=2,sort_keys=True))
