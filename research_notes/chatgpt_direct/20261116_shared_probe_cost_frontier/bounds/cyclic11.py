"""Exact optimization in the cyclic family with five specified 13-point classes."""
from itertools import product,combinations
from collections import Counter
import json
from pathlib import Path
P=list(product(range(5),repeat=3))
def index(point):
    x,y,z=point
    return 25*x+5*y+z
def rot(i):
    x,y,z=P[i]
    return index((z,x,-y%5))
def setbits(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask ^=bit

def observations():
    bad=[[0]*125 for _ in P]
    pair=[[0]*125 for _ in P]
    menus=list(product((1,3),P))
    for k,(d,start) in enumerate(menus):
        active={}
        for i,p in enumerate(P):
            a=tuple(j for j in range(3) if (p[j]-start[j])%5 in (0,d))
            y=tuple(p[j] for j in a)
            active.setdefault(a,[]).append((i,y))
        for g in active.values():
            for (i,x),(j,y) in combinations(g,2):
                if x!=y:
                    pair[i][j]|=1<<k
                    pair[j][i]|=1<<k
            for (i,x),(j,y),(h,z) in combinations(g,3):
                if x==y or y==z or x==z:
                    continue
                bad[i][j]|=1<<h
                bad[j][i]|=1<<h
                bad[i][h]|=1<<j
                bad[h][i]|=1<<j
                bad[j][h]|=1<<i
                bad[h][j]|=1<<i
    return bad,pair

def class_cost(points,pair):
    v=0
    for i in points:
        m=0
        for j in points:
            m |=pair[i][j]
        v+=m.bit_count()
    return v

def run():
    bad,pair=observations()
    a={0}
    for h,k in product((1,-1),repeat=2):
        a.update([index((0,2*h%5,k%5)),index((h%5,0,2*k%5)),index((2*h%5,k%5,0))])
    large=[[index(((x+t)%5,(y-t)%5,(z-t)%5)) for x,y,z in (P[i] for i in sorted(a))] for t in range(5)]
    available=set(range(125)).difference(*large)
    assert len(available)==60
    cycles=[]
    while available:
        i=min(available)
        cycle=[i]
        j=rot(i)
        while j!=i:
            cycle.append(j)
            j=rot(j)
        assert len(cycle)==6 and available.issuperset(cycle)
        cycles.append(cycle)
        available.difference_update(cycle)
    counts=Counter()
    winner={}
    tests=0
    def dfs(points,rem,block):
        nonlocal tests
        if not rem:
            cost=class_cost(points,pair)
            counts[cost]+=1
            winner.setdefault(cost,list(points))
            return
        can=[]
        for j in rem:
            options=[i for i in cycles[j] if not block>>i&1]
            if not options:
                return
            can.append((len(options),j,options))
        _,j,options=min(can)
        if not points: options=options[:1]
        for i in options:
            tests+=1
            b=block
            for w in points:
                b |=bad[w][i]
            dfs(points+[i],rem-{j},b)
    dfs([],set(range(10)),0)
    base=winner[min(counts)]
    small=[base]
    for _ in range(5):
        small.append([rot(i)for i in small[-1]])
    code=[-1]*125
    for lab,cl in enumerate(large+small):
        for v in cl:
            assert code[v]<0
            code[v]=lab
        assert all(not (bad[i][j]>>k&1) for i,j,k in combinations(sorted(cl),3))
    assert -1 not in code
    costs=[class_cost(cl,pair) for cl in large+small]
    return dict(family='five fixed large translates and six small images under r(z,x,-y) written r(x,y,z)=(z,x,-y)',r_orbits=cycles,
                explored_extensions=tests,feasible_unlabelled_partitions=sum(counts.values()),
                small_seed_cost_frequencies=sorted(counts.items()),large_cost=costs[0],
                best_seed=sorted(base),total_paid=sum(costs),zero_read=31250-sum(costs),
                classes=large+small,one_based=False,code=code)
if __name__=='__main__':
    ans=run()
    here=Path(__file__).parent
    (here/'cyclic11.json').write_text(json.dumps(ans,indent=2)+'\n')
    (here/'best11.txt').write_text(' '.join(map(str,ans['code']))+'\n')
    print({k:v for k,v in ans.items() if k not in ('code','classes','r_orbits')})
