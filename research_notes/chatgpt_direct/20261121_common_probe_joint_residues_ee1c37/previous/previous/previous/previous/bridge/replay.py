"""Repartition the union of released classes of the 9,996-read twelve-label witness."""
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse, json, subprocess, sys

HERE = Path(__file__).resolve().parent
BUDGET = 11292

def make_jobs(groups, released, observations, class_cost):
    labels = {frozenset(row): i for i,row in enumerate(groups)}
    rotate = lambda p:25*(p//5%5)+5*(p%5)+p//25
    label_map = [labels[frozenset(rotate(p) for p in row)] for row in groups]
    values = [class_cost(row,observations) for row in groups]
    assert sum(values)==9996
    rows=[]
    covered=0
    for selected in combinations(range(12),released):
        orbit=[selected]
        for _ in range(2):
            orbit.append(tuple(sorted(label_map[i] for i in orbit[-1])))
        if selected!=min(orbit):
            continue
        mask=sum(1<<p for i in selected for p in groups[i])
        new_classes=released-1
        if mask.bit_count()>13*new_classes:
            continue
        base=sum(v for i,v in enumerate(values) if i not in selected)
        rows.append((mask%2**64,mask>>64,new_classes,base,*selected))
        covered+=len(set(orbit))
    return rows,covered

def run(older,groups_path,jobs,release_sizes):
    sys.path.insert(0,str(older/'bounds'))
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    _,obs=observations()
    groups=json.loads(groups_path.read_text())
    assert len(groups)==12 and sorted(sum(groups,[]))==list(range(125))
    data={}
    with TemporaryDirectory()as tmp:
        work=Path(tmp)
        observation_file(work/'obs')
        for name in ['cover','tails']:
            subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',HERE/(name+'.cpp'),'-o',work/name],check=True)
        for h in release_sizes:
            tasks,all_choices=make_jobs(groups,h,obs,class_cost)
            f=work/f'jobs{h}'
            f.write_text(''.join(' '.join(map(str,row))+'\n' for row in tasks))
            def one(start):
                path=work/f'tail{h}-{start}'
                end=min(start+2,len(tasks))
                out=subprocess.check_output([work/'cover',work/'obs',f,str(start),str(end),str(BUDGET),path],text=True)
                rows=[list(map(int,line.split())) for line in out.splitlines()]
                assert [r[0] for r in rows]==list(range(start,end))
                tails=path.read_text().splitlines()
                assert len(tails)==sum(v[2] for v in rows)
                return sum(v[1] for v in rows),tails
            with ThreadPoolExecutor(max_workers=jobs)as pool:
                parts=list(pool.map(one,range(0,len(tasks),2)))
            nodes=sum(n for n,_ in parts)
            residuals=[line for _,lines in parts for line in lines]
            distinct=sorted(set(residuals))
            tail_jobs=work/'remainder'
            tail_jobs.write_text(''.join(l+'\n' for l in distinct))
            out=subprocess.check_output([work/'tails',work/'obs',tail_jobs,'0',str(len(distinct)),str(BUDGET)],text=True)
            checks=[list(map(int,l.split())) for l in out.splitlines()]
            assert len(checks)==len(distinct) and all(j==i and found==0 for i,(j,n,found) in enumerate(checks))
            data[str(h)]={'retained_classes':12-h,'new_classes_for_union':h-1,'admitted_selections':all_choices,
                          'cyclic_representatives':len(tasks),'visited':nodes,'residuals':len(residuals),'distinct_residuals':len(distinct),
                          'tail_nodes':sum(n for _,n,_ in checks),'feasible_at_11292':False}
    return {'source_cost':9996,'budget':BUDGET,'cases':data}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--older',required=True,type=Path)
    p.add_argument('--groups',type=Path,default=HERE.parent/'c3/groups.json')
    p.add_argument('--jobs',type=int,default=4)
    p.add_argument('--release',type=int,nargs='+',default=[5,6,7,8,9])
    a=p.parse_args()
    print(json.dumps(run(a.older.resolve(),a.groups.resolve(),a.jobs,a.release),sort_keys=True,indent=2))
