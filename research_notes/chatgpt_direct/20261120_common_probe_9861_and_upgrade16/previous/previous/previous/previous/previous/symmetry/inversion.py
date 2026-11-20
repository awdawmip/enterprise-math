"""Enumerate the allowed class costs and partition the 63 central-inversion point orbits."""
from collections import Counter, defaultdict
from functools import cache
from itertools import product, permutations
from pathlib import Path
import argparse
import json
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
BUDGET = 8728

def indexes(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit

def mask(indices):
    return sum(1 << i for i in indices)

def load_classes(older, work, database):
    sys.path.insert(0,str(older/'bounds'))
    sys.path.insert(0,str(older/'curve'))
    from prior_bounds import observation_file, symmetries, expand
    from verify import MINIMA, lower
    assert all(MINIMA[s] + lower(125-s,12) > BUDGET for s in range(1,9))
    ceilings={9:587,10:780,11:965,12:1140,13:1350}
    assert all(ceilings[s]+1+lower(125-s,12)>BUDGET for s in ceilings)
    def wanted(size,cost):
        return size in ceilings and cost+lower(125-size,12)<=BUDGET
    if database:
        classes={}
        with database.open() as source:
            for _ in range(int(next(source))):
                size,cost,n = map(int,next(source).split())
                rows = [next(source) for _ in range(n)]
                if wanted(size,cost):
                    classes[size,cost]=[int(z[0]) | int(z[1])<<64 for z in (r.split() for r in rows)]
        return classes,lower
    observation_file(work/'menus')
    binary=work/'enumerate'
    subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(older/'curve/class_minima.cpp'),'-o',str(binary)],check=True)
    subprocess.run([str(binary),str(work/'menus'),str(work/'seeds')], check=True,stdout=subprocess.DEVNULL)
    seeds=defaultdict(set)
    with (work/'seeds').open() as source:
        for line in source:
            s,c,*row=map(int,line.split())
            if wanted(s,c):
                seeds[s,c].add(tuple(row))
    linear,shifts=symmetries()
    return {key:expand(rows,linear,shifts) for key,rows in seeds.items()},lower

def aggregate(classes):
    neg = [25*((-x)%5)+5*((-y)%5)+(-z)%5 for x,y,z in product(range(5),repeat=3)]
    representatives=sorted({min(i,neg[i]) for i in range(125)})
    qidx={i:representatives.index(min(i,neg[i])) for i in range(125)}
    assert len(representatives)==63
    sets = defaultdict(Counter)
    for (s,c),inventory in classes.items():
        for points in inventory:
            images = mask(neg[i] for i in indexes(points))
            if images==points:mult=1
            elif points<images and not points&images:mult=2
            else:continue
            compressed=mask({qidx[i] for i in indexes(points)})
            sets[s,c,mult][compressed]+=1
    return sets

def anchor_orbits(anchors):
    points=list(product(range(5),repeat=3))
    def index(t):
        return 25*(t[0]%5) + 5*(t[1]%5) + t[2]%5
    neg = [index([-x for x in p]) for p in points]
    reps=sorted({min(i,neg[i]) for i in range(125)})
    qidx={i:reps.index(min(i,neg[i])) for i in range(125)}
    group=[]
    for perm,signs,d in product(permutations(range(3)),product((-1,1),repeat=3),(1,2)):
        group.append([qidx[index([d*signs[j]*points[i][perm[j]] for j in range(3)])] for i in reps])
    def normalize(rows):
        remaining=set(rows)
        result=[]
        while remaining:
            seed=min(remaining)
            orbit={mask(g[i] for i in indexes(seed)) for g in group}
            assert orbit<=remaining
            result.append((seed,len(orbit)))
            remaining-=orbit
        return result
    return {t:normalize(anchors[t]) for t in anchors if t[2]==1 and t[0]%2}

def generate_profiles(types,lower):
    grouped = sorted(set((s,c) for s,c,_ in types))
    @cache
    def candidates(n,t,start,cap):
        if t==0:return [()] if n==0 else []
        out=[]
        for j in range(start,len(grouped)):
            s,c=grouped[j]
            if n<s or c+lower(n-s,t-1)>cap:continue
            out.extend(((s,c),)+tail for tail in candidates(n-s,t-1,j,cap-c))
        return out
    return sorted(((sum(c for s,c in row),Counter(row)) for row in candidates(125,13,0,BUDGET)),key=lambda x:x[0])

def solve(older, database):
    with tempfile.TemporaryDirectory() as tmp:
        work=Path(tmp)
        classes,lower=load_classes(older,work,database)
        sets=aggregate(classes)
        types=sorted(sets)
        profiles=generate_profiles([(s,c,1) for s,c in classes],lower)
        jobs=[]
        anchors=anchor_orbits(sets)
        count_splits=0
        for cost,p in profiles:
            bins=[]
            for (s,c),n in sorted(p.items()):
                options=[]
                for pairs in range(n//2+1):
                    fixed=n-2*pairs
                    if fixed and not sets[s,c,1]:continue
                    if pairs and not sets[s,c,2]:continue
                    if s%2 and fixed>1:continue
                    options.append({(s,c,1):fixed,(s,c,2):pairs})
                bins.append(options)
            for choices in product(*bins):
                counts={k:v for group in choices for k,v in group.items() if v}
                if sum(v for (s,c,m),v in counts.items() if m==1 and s%2)==1:
                    odd=next(t for t,v in counts.items() if t[0]%2 and t[2]==1)
                    counts[odd]-=1
                    for a,multiplicity in anchors[odd]:
                        free=((1<<63)-1)^a
                        jobs.append((cost,free,multiplicity,[counts.get(t,0) for t in types]))
                    count_splits+=1
        data=[str(len(types))]
        for t in types:
            rows=sets[t]
            data.append(str(len(rows)))
            data.extend(f'{r} {m}' for r,m in sorted(rows.items()))
        data.append(str(len(jobs)))
        for c,free,weight,quotas in jobs:data.append(' '.join(map(str,[c,free,weight,*quotas])))
        exe=work/'cover'
        subprocess.run(['c++','-std=c++17','-O3',str(HERE/'inversion.cpp'),'-o',str(exe)],check=True)
        output=subprocess.check_output([str(exe)],input='\n'.join(data)+'\n',text=True)
        result=Counter()
        nodes=0
        for l,(c,free,w,q) in zip(output.splitlines(),jobs,strict=True):
            claimed,count,visited = map(int,l.split())
            assert claimed==c
            result[c]+=count
            nodes+=visited
        return {'budget':BUDGET,'profiles':len(profiles),'fixed_pair_profiles':count_splits,'anchored_cases':len(jobs),'visited':nodes,'partitions_by_cost':dict(sorted((k,v) for k,v in result.items() if v))}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--older',type=Path,default=HERE.parents[1]/'round2/delivery')
    p.add_argument('--database',type=Path)
    a=p.parse_args()
    print(json.dumps(solve(a.older.resolve(),a.database),indent=2))
