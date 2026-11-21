"""Fix the two indicated size-13 classes. Only the size-9 class must be cyclic."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent
EXISTING=HERE.parent/'fixed_classes'
CAP=9995

def setup(previous):
    last=previous/'previous/previous'
    older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(last/'group'),str(older/'bounds'),str(older/'curve')]
    from generate import maps
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    from verify import MINIMA
    assert MINIMA[10]==744
    bad,menu=observations()
    known=json.loads((previous/'c3/groups.json').read_text())
    fixed=[frozenset(r) for r in known[:2]]
    known_nine=tuple(sorted(known[2]))
    price=sum(class_cost(list(r),menu) for r in fixed)
    assert price==2592 and [len(r) for r in fixed]==[13,13] and fixed[0].isdisjoint(fixed[1])
    free=set(range(125)).difference(*fixed)
    def rot(i):return 25*(i//5%5)+5*(i%5)+i//25
    assert all(frozenset(rot(i) for i in r)==r for r in fixed)
    cycles=sorted({tuple(sorted({i,rot(i),rot(rot(i))})) for i in free})
    assert sum(map(len,cycles))==len(free)==99
    single=[o for o in cycles if len(o)==1];triple=[o for o in cycles if len(o)==3]
    assert len(single)+len(triple)==len(cycles)
    cutoff=CAP-price-9*MINIMA[10]
    valid={}
    for k in range(4):
        for a in combinations(triple,k):
            for b in combinations(single,9-3*k):
                r=tuple(sorted(p for orb in a+b for p in orb))
                if any((bad[i][j]>>t)&1 for i,j,t in combinations(r,3)):continue
                c=class_cost(r,menu)
                if c<=cutoff:valid[r]=c
    linear,translations,_=maps()
    stabilizer=[]
    for g in linear:
        for t in translations:
            a=bytes(t[i] for i in g)
            if {frozenset(a[i] for i in r) for r in fixed}==set(fixed):stabilizer.append(a)
    reps=[];seen=set()
    for r in sorted(valid,key=lambda q:(valid[q],q)):
        if r in seen:continue
        orb={tuple(sorted(g[i] for i in r)) for g in stabilizer}
        assert all(x in valid and valid[x]==valid[r] for x in orb)
        seen|=orb
        reps.append((r,valid[r],len(orb),known_nine in orb))
    assert len(stabilizer)==6 and seen==set(valid) and len(valid)==21 and len(reps)==12
    prior=json.loads((EXISTING/'result.json').read_text())
    assert prior['minimum']==9996 and prior['number']==2
    assert any({tuple(sorted(r)) for r in known}=={tuple(r) for r in part} for part in prior['partitions'])
    assert sum(r[3] for r in reps)==1
    return free,price,reps,observation_file

def check_region(path,free,price_cap,weight,budget):
    assert len(weight)==126
    points=sorted(free);full=sum(1<<i for i in points)
    slack=1000*budget-sum(weight[i] for i in points)
    union=0;seen=set();nkept=0
    degree=Counter()
    for line in path.open():
        lo,hi,n,c=map(int,line.split());m=(hi<<64)|lo
        assert n==10 and m.bit_count()==10 and not (m&~full) and 744<=c<=price_cap and m not in seen
        seen.add(m);union|=m
        pts=[];q=m
        while q:
            b=q&-q;pts.append(b.bit_length()-1);q-=b
        rc=1000*c-sum(weight[i] for i in pts)
        assert rc>=0
        if rc<=slack:
            nkept+=1;degree.update(pts)
    assert union==full
    pivot=min(points,key=lambda i:(degree[i],i))
    return {'candidate_rows':len(seen),'eligible_rows':nkept,'pivot':pivot,'first_choices':degree[pivot],'slack':slack}

def read_receipt(stdout,stderr,region):
    assert not stdout.strip()
    logs=stderr.splitlines()
    assert list(map(int,logs[0].split()))==[region[k] for k in ('pivot','first_choices','eligible_rows','slack')]
    label,n,v=logs[-1].split()
    assert label=='done' and int(n)==region['first_choices']
    counts=[tuple(map(int,l.split())) for l in logs[1:-1]]
    assert [n for n,v in counts]==list(range(100,region['first_choices']+1,100))
    assert all(a[1]<=b[1] for a,b in zip(counts,counts[1:]))
    if counts:assert counts[-1][1]<=int(v)
    return dict(region,cover_nodes=int(v),solutions=0)

def verify(previous,jobs,old_runs=None,rebuilt=None):
    free,price,reps,observation_file=setup(previous)
    weights={tuple(x['nine']):x['weights'] for x in json.loads((HERE/'weights.json').read_text())}
    assert set(weights)=={r for r,c,m,old in reps if not old}
    def cmd(*args,**kwargs):
        return subprocess.run(list(map(str,args)),check=True,text=True,**kwargs)
    with TemporaryDirectory() as tmp:
        tmp=Path(tmp)
        observation_file(tmp/'obs')
        for k in ('rows','cover'):cmd('c++','-std=c++20','-O3','-mpopcnt',EXISTING/(k+'.cpp'),'-o',tmp/k)
        def work(j):
            r,c,m,old=reps[j]
            rec={'nine':list(r),'cost':c,'orbit_size':m,'known_nine_orbit':old}
            if old:return rec
            region=free-set(r);budget=CAP-price-c;mx=budget-8*744
            mask=sum(1<<i for i in region)
            destination=(rebuilt or tmp)/f'region{j+10}'
            wf=tmp/f'weights{j}';wf.write_text(' '.join(map(str,weights[r]))+'\n')
            with destination.open('w') as f:
                cmd(tmp/'rows',tmp/'obs',input=f'{mask%2**64} {mask>>64} 10 10 {mx}\n',stdout=f)
            reg=check_region(destination,region,mx,weights[r],budget)
            if old_runs:
                import filecmp
                assert filecmp.cmp(destination,old_runs/f'region{j+10}',shallow=False)
                out=(old_runs/f'alt{j+10}').read_text()
                err=(old_runs/f'alt{j+10}.log').read_text()
            else:
                run=cmd(tmp/'cover',destination,wf,budget,0,1,capture_output=True)
                out,err=run.stdout,run.stderr
            rec.update(read_receipt(out,err,reg),row_cost_ceiling=mx,residual_budget=budget)
            return rec
        with ThreadPoolExecutor(max_workers=jobs) as ex:
            runs=list(ex.map(work,range(len(reps))))
    return {'minimum':9996,'strict_budget':CAP,'cost_of_fixed_pair':price,
            'nine_cost_ceiling':CAP-price-9*744,'eligible_cyclic_nines':sum(m for r,c,m,o in reps),
            'nine_orbits':len(reps),'stabilizer_of_two_supports':6,'branches':runs,
            'other_orbits_searched':sum(not x['known_nine_orbit'] for x in runs)}

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--previous',type=Path,required=True)
    ap.add_argument('--jobs',type=int,default=4)
    args=ap.parse_args()
    if args.jobs<1:ap.error('--jobs must be positive')
    print(json.dumps(verify(args.previous.resolve(),args.jobs),indent=2,sort_keys=True))
