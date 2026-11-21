"""An eleven-label one-read partition cannot be invariant under an elementary abelian group of order eight."""
import argparse,json,sys
from collections import Counter
from functools import cache
from itertools import combinations,product
from pathlib import Path


def cube_groups():
    points=list(product(range(5),repeat=3));lookup={p:i for i,p in enumerate(points)}
    representatives=[]
    for swapped in (False,True):
        group=[]
        for a,b,c in product((0,1),repeat=3):
            def act(x,y,z):
                if swapped:
                    if a:x,y=y,x
                    if b:x,y=-x,-y
                else:
                    if a:x=-x
                    if b:y=-y
                if c:z=-z
                return lookup[x%5,y%5,z%5]
            group.append(bytes(act(*p) for p in points))
        representatives.append(group)
    return representatives


def subgroups():
    return [{0}]+[{0,x} for x in range(1,8)]+[set(h) for h in sorted({tuple(sorted((0,x,y,x^y))) for x,y in combinations(range(1,8),2)})]+[set(range(8))]


def verify_one(group,bad,pair,class_cost):
    orbits=[];unused=set(range(125))
    while unused:
        point=min(unused);orbit={g[point] for g in group};orbits.append(orbit);unused-=orbit
    masks=[sum(1<<i for i,o in enumerate(orbits)if len(o)==s) for s in (1,2,4,8)]
    target=tuple(m.bit_count()for m in masks);assert target==(1,6,12,8)
    # An eight-label orbit must take its points from the eight free point orbits.
    assert 8*target[3]+3*13<125
    lowest={};counts=Counter()
    for subgroup in subgroups():
        r=8//len(subgroup)
        if r==8:continue
        family=[]
        for j,orbit in enumerate(orbits):
            cosets={tuple(sorted({group[h][point] for h in subgroup})) for point in orbit}
            if len(cosets)==r:family.append((j,sorted(cosets)))
        def visit(start,support,points,forbidden):
            if points:
                key=(support,r);value=class_cost(points,pair)
                lowest[key]=min(value*r,lowest.get(key,10**6))
            for k in range(start,len(family)):
                bit,cosets=family[k]
                for coset in (cosets if points else cosets[:1]):
                    if len(points)+len(coset)>13:continue
                    selected=points.copy();blocked=forbidden
                    for point in coset:
                        if blocked>>point&1:break
                        for earlier in selected:blocked|=bad[earlier][point]
                        selected.append(point)
                    else:visit(k+1,support|1<<bit,selected,blocked)
        visit(0,0,[],0)
    signatures={}
    for (support,r),cost in lowest.items():
        profile=tuple((m&support).bit_count()for m in masks)
        key=(r,profile);signatures[key]=min(cost,signatures.get(key,10**6))
    @cache
    def capacity(labels,points):
        if labels==0:return 0 if not any(points) else 10**6
        possible=[]
        for (r,profile),cost in signatures.items():
            if r<=labels and all(z<=t for z,t in zip(profile,points)):
                possible.append(cost+capacity(labels-r,tuple(t-z for z,t in zip(profile,points))))
        return min(possible,default=10**6)
    initial=capacity(11,target)
    result=dict(history_orbits=list(target),distinct_signatures=len(signatures),
                supported_label_orbits=len(lowest),relaxed_minimum=None if initial>=10**6 else initial)
    if initial<10**6:
        for j,orbit in enumerate(orbits):
            touching=[(q,r) for q,r in lowest if q>>j&1]
            if all(capacity(11-r,tuple(v-(q&m).bit_count()for v,m in zip(target,masks)))>=10**6 for q,r in touching):
                result.update(blocked_history_orbit=sorted(orbit),candidates_touching=len(touching));break
        else:raise AssertionError('the obstruction was not sufficient')
    return result


def verify(older,groupdir):
    sys.path[:0]=[str(older/'bounds'),str(groupdir)]
    from cyclic11 import observations,class_cost
    from generate import maps
    linear,_,_=maps();truth=bytes(range(125));comp=lambda a,b:bytes(a[x]for x in b)
    invol=[a for a in linear if a!=truth and comp(a,a)==truth]
    all_groups=set()
    for a,b,c in combinations(invol,3):
        if any(comp(u,v)!=comp(v,u)for u,v in ((a,b),(a,c),(b,c))):continue
        group=frozenset([truth,a,b,c,comp(a,b),comp(a,c),comp(b,c),comp(a,comp(b,c))]);
        if len(group)==8:all_groups.add(group)
    bad,pair=observations();results=[];covered=set()
    for group in cube_groups():
        assert all(comp(group[a],group[b])==group[a^b]for a,b in product(range(8),repeat=2))
        conjugates={frozenset(comp(t,comp(g,bytes(t.index(i) for i in range(125))))for g in group)for t in linear}
        assert not covered&conjugates;covered|=conjugates
        result=verify_one(group,bad,pair,class_cost);result['linear_conjugates']=len(conjugates);results.append(result)
    assert covered==all_groups and len(all_groups)==4
    return {'labels':11,'cost_bound_used':False,'linear_groups':len(all_groups),'cases':results}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);p.add_argument('--group',type=Path,required=True);a=p.parse_args()
    print(json.dumps(verify(a.older.resolve(),a.group.resolve()),indent=2,sort_keys=True))
