"""Classify all strict eleven-message codes containing five full thirteen-history classes.

Python 3.10+, little-endian 64-bit host, C++17. Recreates all inputs from the
observation semantics and writes no intermediate state outside a TemporaryDirectory.
"""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations, permutations, product
import json
from pathlib import Path
import subprocess
import tempfile

D = Path(__file__).resolve().parent
POINTS = list(product(range(5), repeat=3))
INDEX = {v:i for i,v in enumerate(POINTS)}
ORDER = 125

def members(bits):
    while bits:
        low=bits & -bits
        yield low.bit_length()-1
        bits-=low

def observations():
    ambiguity=[[0]*ORDER for _ in POINTS]
    forbidden=set()
    for action,step in enumerate((1,3)):
        for mi,menu in enumerate(POINTS):
            receipt={}
            for i,point in enumerate(POINTS):
                active=tuple(k for k in range(3) if (point[k]-menu[k])%5 in (0,step))
                future=tuple(point[k] for k in active)
                receipt.setdefault(active,[]).append((i,future))
            for histories in receipt.values():
                for (i,a),(j,b) in combinations(histories,2):
                    if a!=b:
                        ambiguity[i][j]|=1<<(action*125+mi)
                        ambiguity[j][i]=ambiguity[i][j]
                for (i,a),(j,b),(k,c) in combinations(histories,3):
                    if a!=b and b!=c and a!=c: forbidden.add((i,j,k))
    assert len(forbidden)==47000
    return forbidden,ambiguity

def saturated(forbidden):
    # All sets of at least 13 through the origin. A candidate clique of pairs
    # forbidden by previously chosen vertices contributes at most one new point.
    excluded=[[0]*ORDER for _ in POINTS]
    for triple in forbidden:
        for a,b,c in permutations(triple):excluded[a][b]|=1<<c
    through=set()
    def visit(chosen,can,blocked):
        size=chosen.bit_count()
        groups=0;order=[];left=can
        while left:
            groups+=1;clique=left
            while clique:
                low=clique&-clique;v=low.bit_length()-1
                order.append((v,groups));left^=low;clique&=left&blocked[v]
        for v,level in reversed(order):
            if size+level<13:return
            bit=1<<v;can^=bit;rest=can&~blocked[v];s=chosen|bit
            if size+1>=13:through.add(s)
            if size+1+rest.bit_count()>=13:
                visit(s,rest,{j:blocked[j]|excluded[v][j] for j in members(rest)})
    visit(1,(1<<ORDER)-2,excluded[0]);assert all(s.bit_count()==13 for s in through)
    translates=[[1<<INDEX[tuple((x+y)%5 for x,y in zip(p,t))] for p in POINTS] for t in POINTS]
    all_classes={sum(row[j] for j in members(s)) for s in through for row in translates}
    assert len(all_classes)==250
    return sorted(all_classes),translates

def packing_orbits(classes,translates):
    graph=[sum(1<<j for j,t in enumerate(classes) if not (s&t)) for s in classes]
    frequency=Counter()
    def visit(union,depth,candidates):
        if depth==5:frequency[union]+=1;return
        while candidates.bit_count()+depth>=5:
            low=candidates&-candidates;candidates-=low;i=low.bit_length()-1
            visit(union|classes[i],depth+1,candidates&graph[i])
    visit(0,0,(1<<len(classes))-1)
    maps=[]
    for per in permutations(range(3)):
        for signs in product((1,-1),repeat=3):
            for scale in (1,2):
                maps.append([INDEX[tuple(w[k]*sgn*scale%5 for k,sgn in zip(per,signs))] for w in POINTS])
    reps=[];remaining=set(frequency)
    while remaining:
        s=min(remaining);indices=list(members(s));before=len(remaining)
        for m in maps:
            oriented=[m[i] for i in indices]
            for v in translates:remaining.discard(sum(v[i] for i in oriented))
        orbit=before-len(remaining)
        reps.append({'union_mask':str(s),'union_orbit_size':orbit,'packings_per_union':frequency[s]})
    assert sum(r['union_orbit_size']*r['packings_per_union'] for r in reps)==sum(frequency.values())
    return reps,sum(frequency.values()),len(frequency)

def class_cost(s,ambiguity):
    total=0
    for i in members(s):
        bits=0
        for j in members(s):bits|=ambiguity[i][j]
        total+=bits.bit_count()
    return total

def classify(union,solutions,classes):
    remainder=[i for i in range(125) if not (union>>i&1)]
    occupied=set(members(union))
    candidates=[g for g in classes if g & ~union==0]
    core_partitions=[groups for groups in combinations(candidates,5)
                     if all(not g&h for g,h in combinations(groups,2))]
    codes=set()
    for solution in solutions:
        residual=[sum(1<<remainder[i] for i in members(g)) for g in solution]
        for core in core_partitions:codes.add(tuple(sorted([*core,*residual])))
    assert len(codes)==len(solutions)*len(core_partitions)
    stabilizer=[]
    for perm in permutations(range(3)):
        for signs in product((1,-1),repeat=3):
            for k in (1,2):
                p=[tuple(x[j]*a*k%5 for j,a in zip(perm,signs)) for x in POINTS]
                for t in POINTS:
                    def image(i):return INDEX[tuple((a+b)%5 for a,b in zip(p[i],t))]
                    if any(image(i) not in occupied for i in occupied):continue
                    stabilizer.append([1<<image(i) for i in range(125)])
    unseen=set(codes);orbits=[]
    while unseen:
        rep=min(unseen);items=[list(members(v)) for v in rep]
        transforms={tuple(sorted(sum(m[i] for i in c) for c in items)) for m in stabilizer}
        assert transforms<=unseen;unseen-=transforms;orbits.append(len(transforms))
    return len(stabilizer),sorted(orbits),len(core_partitions)

def run():
    forbidden,ambiguity=observations()
    all_classes,translations=saturated(forbidden)
    costs=Counter(class_cost(s,ambiguity) for s in all_classes)
    reps,npack,nunion=packing_orbits(all_classes,translations)
    with tempfile.TemporaryDirectory() as tmp:
        tmp=Path(tmp); binary=tmp/'sets'; observations_file=tmp/'conditions'
        with observations_file.open('wb') as f:
            for row in ambiguity:
                for value in row:f.write(value.to_bytes(32,'little'))
            for t in sorted(forbidden):f.write(bytes(t))
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(D/'saturated_fill.cpp'),'-o',str(binary)],check=True)
        def fill(entry):
            s=int(entry['union_mask']);pts=[i for i in range(125) if not (s>>i&1)];assert len(pts)==60
            p=tmp/entry['union_mask'];p.write_text(' '.join(map(str,pts)))
            solution_file=tmp/(entry['union_mask']+'.out')
            output=subprocess.check_output([str(binary),str(observations_file),str(p),str(solution_file)],text=True).splitlines()
            solutions=[tuple(map(int,line.split())) for line in solution_file.read_text().splitlines()]
            entry=dict(entry)
            if solutions:
                stabilizer,orbits,decompositions=classify(s,solutions,all_classes)
                assert decompositions==entry['packings_per_union']
                entry.update(stabilizer_order=stabilizer,full_code_orbits_in_fixed_union=orbits,
                             residual_size_profiles=[list(x) for x in sorted({tuple(sorted(v.bit_count() for v in code)) for code in solutions})])
            return dict(entry,cover_search_nodes=int(output[0]),residual_cost_histogram={int(t.split()[0]):int(t.split()[1]) for t in output[1:]})
        with ThreadPoolExecutor(max_workers=2) as pool:out=list(pool.map(fill,reps))
    used=[r for r in out if r['residual_cost_histogram']]
    assert len(used)==1 and used[0]['residual_cost_histogram']=={4812:40}
    assert used[0]['packings_per_union']==2 and used[0]['union_orbit_size']==100 and costs=={1296:250}
    return dict(forbidden_triples=len(forbidden),large_class_costs=dict(costs),
                disjoint_five_packings=npack,distinct_unions=nunion,orbits=out,
                successful_unions=100,strict_unlabeled_partitions_with_five_size13=8000,
                strict_read_count_in_all_such_codes=5*1296+4812)

if __name__=='__main__':print(json.dumps(run(),indent=2))
