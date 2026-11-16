"""Classify every completion of five maximum-sized labels under the affine model group."""
import argparse,json,os,sys,subprocess
from collections import Counter
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
HERE=Path(__file__).resolve().parent

def solve(previous):
    last=previous/'previous';older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(last/'group'),str(older/'bounds')]
    from generate import maps
    from cyclic11 import observations,class_cost,setbits
    from six13 import enumerate_classes
    bad,pair=observations()
    labels=list(map(int,(older/'native/eleven.txt').read_text().split()))
    parents=[tuple(i for i,k in enumerate(labels)if k==j)for j in range(5)]
    assert all(len(r)==13 for r in parents)
    free=sorted(set(range(125)).difference(*parents));assert len(free)==60
    def compress(mask):
        return sum(1<<j for j,x in enumerate(free)if mask>>x&1)
    def write_probe_files(w):
        mask=sum(1<<x for x in free)
        rows=enumerate_classes(mask,9,bad)
        assert all(s.bit_count()<=12 for s in rows)
        (w/'p5sets0.dat').write_text(''.join(f'{compress(s)} 0\n' for s in rows))
        with (w/'p5bad0.dat').open('w') as f:
            for i,j in combinations(range(60),2):
                m=compress(bad[free[i]][free[j]])
                if m:print(i,j,m,file=f)
        with (w/'p5cost0.dat').open('w') as f:
            for i,x in enumerate(free):
                for j,y in enumerate(free):
                    v=pair[x][y];print(i,j,*[(v>>(64*h))%2**64 for h in range(4)],file=f)
    with TemporaryDirectory()as d:
        w=Path(d);write_probe_files(w)
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',HERE/'completions.cpp','-o',w/'cover'],check=True)
        lines=subprocess.check_output([w/'cover','0'],cwd=w,text=True).splitlines()
    canon=lambda rows:tuple(sorted(tuple(sorted(r))for r in rows))
    transform=lambda t,rs:canon([t[p] for p in r]for r in rs)
    tables={}
    for line in lines[:-1]:
        tag,cost,*masks=line.split();assert tag=='table'
        rows=canon(parents+[[free[i] for i in setbits(int(m))] for m in masks])
        assert sum(class_cost(r,pair)for r in rows)==6480+int(cost)
        assert len(set().union(*rows))==125 and len(rows)==11 and rows not in tables
        tables[rows]=6480+int(cost)
    assert len(tables)==40 and int(lines[-1].split()[1])==40
    lin,tr,_=maps();all_maps=[bytes(t[p]for p in a)for a in lin for t in tr]
    parents=canon(parents);h=[g for g in all_maps if transform(g,parents)==parents]
    count=12000//len(h);assert count==200
    left=set(tables);orbits=[]
    while left:
        r=min(left);images={transform(g,r)for g in h}
        assert images<=left and all(tables[t]==tables[r]for t in images)
        left-=images
        orbits.append([tables[r],len(images)*count,len(h)//len(images)])
    census=Counter()
    for cost,number,stab in orbits:census[cost]+=number
    return {'positions':count,'completions_per_position':len(tables),'parent_stabilizer':len(h),
            'cost_histogram':dict(sorted(census.items())),'affine_orbits_by_cost_count_and_stabilizer':sorted(orbits)}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True)
    print(json.dumps(solve(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
