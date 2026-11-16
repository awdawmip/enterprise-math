"""Finite lower bound for common-map, three five-cycles, eleven old messages, one query.

Uses only Python standard library and the two included C++17 finite checkers.
The price is the total number of endpoint queries over 31,250 equal-weight cases.
"""
from collections import Counter
from functools import cache, reduce
from itertools import combinations, permutations, product
import json
from operator import or_
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
P = list(product(range(5),repeat=3))
INDEX = {p:i for i,p in enumerate(P)}
ALL = (1<<125)-1


def members(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask-=bit


def observations(path):
    ambiguity=[[0]*125 for _ in P]
    forbidden=set()
    for t,step in enumerate((1,3)):
        for j,menu in enumerate(P):
            condition=1<<(t*125+j)
            bins={}
            for i,p in enumerate(P):
                active=tuple(k for k in range(3) if (p[k]-menu[k])%5 in (0,step))
                bins.setdefault(active,[]).append((i,tuple(p[k] for k in active)))
            for rows in bins.values():
                for (i,a),(j,b) in combinations(rows,2):
                    if a!=b:
                        ambiguity[i][j]|=condition
                        ambiguity[j][i]|=condition
                for (i,a),(j,b),(k,c) in combinations(rows,3):
                    if len({a,b,c})==3:forbidden.add((i,j,k))
    assert len(forbidden)==47000
    with path.open('wb') as f:
        for row in ambiguity:
            for mask in row:f.write(mask.to_bytes(32,'little'))
        for t in sorted(forbidden):f.write(bytes(t))


def compile_check(src,target):
    subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/src),'-o',str(target)],check=True)


def point_symmetries():
    transforms=[]
    for perm in permutations(range(3)):
        for scale in (1,2):
            for signs in product((scale,-scale),repeat=3):
                transforms.append([INDEX[tuple(p[j]*a%5 for j,a in zip(perm,signs))] for p in P])
    translates=[[INDEX[tuple((x+y)%5 for x,y in zip(p,t))] for p in P] for t in P]
    return transforms,translates


def image(group,perm):
    return sum(1<<perm[i] for i in members(group))


def cheap_families(work,obs,transforms,translates):
    prog=work/'enumerate';seeds=work/'seeds';compile_check('class_enumerator.cpp',prog)
    output=subprocess.check_output([str(prog),str(obs),str(seeds)],text=True)
    costs={1:0}
    for line in output.splitlines():
        k,_,cost,*w=map(int,line.split());costs[k]=cost
    assert max(costs)==13
    classes={12:{},13:{}}
    for line in seeds.read_text().splitlines():
        n,price,*points=map(int,line.split());classes[n].setdefault(price,[]).append(sum(1<<i for i in points))
    prices=sorted(classes[12]);assert prices[:3]==[1104,1116,1244] and list(classes[13])==[1296]
    def whole(seeds):
        group=set()
        for c in seeds:
            if c in group:continue
            # The full physical symmetry group factors into linear origin stabilizer and translations.
            orbit={image(c,f) for f in transforms}
            group.update(image(a,t) for a in orbit for t in translates)
        return sorted(group)
    cheap=whole(classes[12][1104]);runners=whole(classes[12][1116]);large=whole(classes[13][1296]);assert len(cheap)==len(large)==250 and len(runners)==3000
    parents={}
    for group in large:
        (core,)=[g for g in cheap if not(g&~group)]
        assert core not in parents;parents[core]=group
    assert len(parents)==len(cheap)
    return costs,cheap,runners,parents


def packing_reps(cheap,point_linear,point_trans):
    index={v:i for i,v in enumerate(cheap)}
    def permute(p):return [index[image(v,p)] for v in cheap]
    linear=list(map(permute,point_linear));trans=list(map(permute,point_trans))
    edges=[sum(1<<j for j in range(i+1,len(cheap)) if not (s&cheap[j])) for i,s in enumerate(cheap)]
    ranks={k:set() for k in (4,5,6)}
    def visit(chosen,candidates):
        if len(chosen)>6:raise ValueError('a seventh disjoint cheap class was found')
        if len(chosen)>=4:ranks[len(chosen)].add(chosen)
        while len(chosen)+candidates.bit_count()>=4 and candidates:
            b=candidates&-candidates;candidates-=b;i=b.bit_length()-1
            visit(chosen+(i,),candidates&edges[i])
    visit((),(1<<len(cheap))-1)
    reps={}
    for n,packings in ranks.items():
        seen=set();rep=[]
        for q in sorted(packings):
            if q in seen:continue
            rotated={tuple(sorted(r[i] for i in q)) for r in linear}
            seen.update(tuple(sorted(t[i] for i in v)) for t in trans for v in rotated)
            rep.append(tuple(cheap[i] for i in q))
        assert seen==packings
        reps[n]=rep
    return reps,{n:len(g) for n,g in ranks.items()}


def packing_number(points):
    edges=[sum(1<<j for j in range(i+1,len(points)) if not (points[i]&points[j])) for i in range(len(points))]
    best=0
    def visit(depth,candidates):
        nonlocal best
        best=max(best,depth)
        while depth+candidates.bit_count()>best:
            bit=candidates&-candidates;candidates-=bit;index=bit.bit_length()-1
            visit(depth+1,candidates&edges[index])
    visit(0,(1<<len(points))-1)
    return best


def six_core_completion(reps,parents,work,obs):
    prog=work/'complete';compile_check('five_group_completion.cpp',prog)
    cases=0;nodes=0;partitions=0
    for groups in reps:
        union=reduce(or_,groups)
        for flags in product((0,1),repeat=6):
            selected=[parents[g] if p else g for g,p in zip(groups,flags)]
            used=reduce(or_,selected)
            if used.bit_count()!=sum(s.bit_count() for s in selected):continue
            pts=work/'points.txt';pts.write_text(' '.join(map(str,members(ALL^used))))
            result=subprocess.check_output([str(prog),str(obs),str(pts)],text=True).splitlines()
            cases+=1;nodes+=int(result[0]);partitions+=sum(int(l.split()[1]) for l in result[1:])
    assert partitions==0
    return {'tested_residuals':cases,'search_nodes':nodes,'eleven_class_completions':partitions}


def lower_bound(costs,runner):
    # Each 12-point group has three permissible relaxed price levels.
    # Every 13 costs 1296 and contributes its minimum-price 12-point subset.
    @cache
    def best(total,slots,cap):
        if slots==0:return (0,()) if total==0 else (10**9,())
        if not slots<=total<=cap*slots:return (10**9,())
        return min((costs[k]+v,(k,)+s) for k in range(1,min(total,cap)+1) for v,s in [best(total-k,slots-1,k)])
    candidates=[]
    for a in range(6):
        for c in range(6-a):
            for r in range(12-a-c):
                if c+a in runner and r>runner[c+a]:continue
                for higher in range(12-a-c-r):
                    small=11-a-c-r-higher
                    value,shape=best(125-13*a-12*(c+r+higher),small,11)
                    candidates.append((a*1296+c*1104+r*1116+higher*1244+value,a,c,r,higher,shape))
    return min(candidates)


def main():
    lin,trans=point_symmetries()
    with TemporaryDirectory() as temp:
        work=Path(temp);data=work/'public';observations(data)
        costs,cheap,runners,parents=cheap_families(work,data,lin,trans)
        reps,num=packing_reps(cheap,lin,trans)
        runner={n:max(packing_number([s for s in runners if not(s&reduce(or_,g))]) for g in groups) for n,groups in reps.items()}
        assert runner=={4:2,5:1,6:0}
        complete=six_core_completion(reps[6],parents,work,data)
        optimum=lower_bound(costs,runner)
        print(json.dumps({'minimum_costs':costs,'cheap_core_pack_counts':num,'cheap_core_orbits':{k:len(g) for k,g in reps.items()},'maximum_runners_after_cores':runner,'six_core_residuals':complete,'global_cost_lower_bound':optimum[0],'relaxed_attaining_profile':{'size13':optimum[1],'cheap12':optimum[2],'runner12':optimum[3],'higher12':optimum[4],'smaller':optimum[5]}},indent=2))

if __name__=='__main__':main()
