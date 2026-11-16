"""Self-contained exhaustive audit. Python 3.10+, GNU/Clang C++17 (unsigned __int128)."""
from __future__ import annotations
import json
import subprocess
import tempfile
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
POINTS = list(product(range(5),repeat=3))
def build_inputs(code):
    masks=[[0]*125 for _ in POINTS]
    forbidden=set()
    histogram=Counter()
    idx=0
    for d in (1,3):
        for start in POINTS:
            by_active={}
            for i,p in enumerate(POINTS):
                active=tuple(j for j in range(3) if (p[j]-start[j])%5 in (0,d))
                output=tuple(p[j] for j in active)
                by_active.setdefault(active,[]).append((i,output))
            for group in by_active.values():
                by_message={}
                for i,out in group:
                    by_message.setdefault(code[i],[]).append(out)
                for outputs in by_message.values():
                    k=len(set(outputs))
                    assert k<=2
                    histogram[k-1]+=len(outputs)
                for (i,yi),(j,yj) in combinations(group,2):
                    if yi!=yj:
                        masks[i][j]|=1<<idx
                        masks[j][i]|=1<<idx
                for (i,yi),(j,yj),(k,yk) in combinations(group,3):
                    if len({yi,yj,yk})==3:
                        forbidden.add((i,j,k))
            idx+=1
    return masks,forbidden,histogram

def members(s):
    while s:
        b=s&-s
        yield b.bit_length()-1
        s^=b

def class_cost(points,masks):
    total=0
    for i in points:
        x=0
        for j in points:
            x|=masks[i][j]
        total+=x.bit_count()
    return total

def extend_packing(seed,opt_orbits):
    shifts = [[1<<(25*((x+a)%5)+5*((y+b)%5)+(z+c)%5) for x,y,z in POINTS] for a,b,c in POINTS]
    sets=sorted({sum(sh[i] for i in p) for p in seed for sh in shifts})
    if opt_orbits is not None:
        assert len(sets)==opt_orbits
    graph=[sum(1<<j for j,t in enumerate(sets) if not s&t) for s in sets]
    best=[]
    nodes=0
    def dfs(chosen,can):
        nonlocal best,nodes
        nodes+=1
        if len(chosen)>len(best):best=chosen
        while can.bit_count()+len(chosen)>len(best):
            bit=can&-can
            can^=bit
            j=bit.bit_length()-1
            dfs(chosen+[j],can&graph[j])
    dfs([],2**len(graph)-1)
    return {'sets':len(sets),'nodes':nodes,'maximum_packing':len(best),
            'packing':[list(members(sets[i])) for i in best]}

def lower(cost,nlabels,opt12_limit,runner12,cap13):
    @lru_cache(None)
    def search(n,k,last,free12,thirteens):
        if k==0:return (0,()) if n==0 else (10**9,())
        if n<0:return (10**9,())
        choices=[]
        for size in range(1,min(n,last,13)+1):
            if size*k<n or (size==13 and not thirteens):continue
            val=runner12 if size==12 and free12==0 else cost[size]
            val2,rest=search(n-size,k-1,size,free12-int(size==12 and free12>0),thirteens-int(size==13))
            choices.append((val+val2,(size,)+rest))
        return min(choices,default=(10**9,()))
    # A partition with fewer than nlabels classes can be split without increasing cost.
    return search(125,nlabels,13,opt12_limit,cap13)

def main():
    code=list(map(int,(HERE/'common_12_certificate.txt').read_text().split()))
    assert len(code)==125 and set(code)==set(range(12))
    masks,edges,hist=build_inputs(code)
    assert len(edges)==47000 and sum(hist.values())==31250
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        obsfile=td/'observations.bin'
        with obsfile.open('wb') as f:
            for row in masks:
                for word in row:f.write(word.to_bytes(32,'little'))
            for tri in sorted(edges):f.write(bytes(tri))
        exe=td/'enumerate';seeds=td/'seeds.txt'
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',str(HERE/'common_class_enumeration.cpp'),'-o',str(exe)],check=True)
        raw=subprocess.check_output([str(exe),str(obsfile),str(seeds)],text=True)
        seedrows=[tuple(map(int,line.split())) for line in seeds.read_text().splitlines()]
    costs={0:0,1:0};witnesses={};visits=0
    for l in raw.splitlines():
        k,count,v,*points=map(int,l.split())
        visits+=count;costs[k]=v;witnesses[k]=points
        assert k==len(points) and class_cost(points,masks)==v and not any(t in edges for t in combinations(sorted(points),3))
    assert max(costs)==13
    # Canonical seeds have coordinates transformed; reconstruct whole families using the
    # stabilizer as well as translations, since the search only keeps five second-point choices.
    def all_orientations(points):
        from itertools import permutations
        for perm in permutations(range(3)):
            for signs in product((1,-1),repeat=3):
                for scale in (1,2):
                    ids=[]
                    for i in points:
                        p=POINTS[i]
                        x,y,z=[p[j]*signs[k]*scale%5 for k,j in enumerate(perm)]
                        ids.append(25*x+5*y+z)
                    yield tuple(sorted(ids))
    orient12=set();orient13=set()
    next12=min(r[1] for r in seedrows if r[0]==12 and r[1]>costs[12])
    for k,v,*pts in seedrows:
        if k==12 and v==costs[12]:orient12.update(all_orientations(pts))
        if k==13:orient13.update(all_orientations(pts))
    pack12=extend_packing(orient12,250)
    pack13=extend_packing(orient13,250)
    assert sum(class_cost([i for i,c in enumerate(code) if c==a],masks) for a in range(12))==hist[1]
    bounds={k:lower(costs,k,pack12['maximum_packing'],next12,pack13['maximum_packing']) for k in (11,12)}
    assert hist[1]<bounds[11][0]
    print(json.dumps(dict(cost_by_size=costs,admissible_set_visits=visits,witness=witnesses,
          next_cost_at_size12=next12,packing_minimum_cost12=pack12,packing_size13=pack13,
          lower_bounds=bounds,certificate_histogram=hist,strict_separation_at_least=bounds[11][0]-hist[1]),indent=2))

if __name__=='__main__':main()
