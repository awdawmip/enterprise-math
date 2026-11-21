"""Reconstruct every claimed optimal partition and match an integer lower bound."""
from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
POINTS = list(product(range(5),repeat=3))
# Exact single-class minima from the preceding exhaustive enumerator.
MINIMA = (0,0,12,36,72,120,201,292,419,557,744,936,1104,1296)


@cache
def lower(n, labels):
    if not labels:
        return 0 if not n else 10**9
    return min((MINIMA[k]+lower(n-k,labels-1) for k in range(1,min(13,n-labels+1)+1)),default=10**9)


def index(p):
    x,y,z = p
    return 25*x + 5*y + z


def shift(row,d,t):
    return sorted(index(tuple((a+t*b)%5 for a,b in zip(POINTS[i],d))) for i in row)


def cheap_line_partitions(m):
    data = json.loads((ROOT/'witnesses.json').read_text())
    if str(m) in data['explicit']:
        return data['explicit'][str(m)]
    if m == 20:
        return [shift(row,(0,0,1),t) for row in data['twenty'] for t in range(5)]
    if 21 <= m <= 25:
        d=(1,1,2)
        chosen=data['twenty_one_blocks'][:25-m]
        groups=[shift(row,d,t) for row in chosen for t in range(5)]
        used={i for g in groups for i in g}
        for i in range(125):
            if i not in used:
                row=shift([i],d,0)
                line=[shift(row,d,t)[0] for t in range(5)]
                assert used.isdisjoint(line)
                used.update(line)
                groups.append(line)
        return groups
    return box_partition(m)


@cache
def possible(shape,small):
    plans={}
    if max(shape) in (small,small+1) and sum(a>1 for a in shape)<=1:
        plans[1]=None
    for axis,dimension in enumerate(shape):
        for width in range(1,dimension):
            a,b=list(shape),list(shape)
            a[axis]=width
            b[axis]-=width
            for x in possible(tuple(a),small):
                for y in possible(tuple(b),small):
                    plans.setdefault(x+y,(axis,width,x,y))
    return plans


def box_partition(m):
    small=125//m
    def cut(origin,shape,labels):
        split=possible(shape,small)[labels]
        if split is None:
            coords=product(*(range(x,x+d) for x,d in zip(origin,shape)))
            return [[index(((a+b+2*c)%5,(a+2*b+c)%5,(2*a+b+c)%5)) for a,b,c in coords]]
        j,w,x,y=split
        a,b=list(shape),list(shape)
        a[j]=w
        b[j]-=w
        start=list(origin)
        start[j]+=w
        return cut(origin,tuple(a),x)+cut(start,tuple(b),y)
    return cut((0,0,0),(5,5,5),m)


def evidence():
    witnesses=json.loads((ROOT/'witnesses.json').read_text())
    masks=[[0]*125 for _ in POINTS]
    bad=set()
    for t,(d,start) in enumerate(product((1,3),POINTS)):
        observations=defaultdict(list)
        for i,p in enumerate(POINTS):
            axes=tuple(j for j in range(3) if (p[j]-start[j])%5 in (0,d))
            observations[axes].append((i,tuple(p[j]for j in axes)))
        for group in observations.values():
            for (i,u),(j,v) in combinations(group,2):
                if u!=v:
                    masks[i][j] |= 1<<t
                    masks[j][i] |= 1<<t
            for (i,u),(j,v),(k,w) in combinations(group,3):
                if len({u,v,w})==3:bad.add((i,j,k))
    assert len(bad)==47000
    rows={}
    for m in sorted(set(range(witnesses['first'],126)) | {int(i) for i in witnesses['explicit']}):
        groups=cheap_line_partitions(m)
        assert len(groups)==m and sorted(i for g in groups for i in g)==list(range(125))
        total=0
        for g in groups:
            assert not any(t in bad for t in combinations(sorted(g),3))
            for i in g:
                words=0
                for j in g:words|=masks[i][j]
                total+=words.bit_count()
        assert total==lower(125,m),(m,total,lower(125,m))
        if m >= 25:
            a,b = divmod(125,m)
            assert total == 6*((m-b)*a*(a-1) + b*a*(a+1))
        rows[m]=total
    return rows


if __name__=='__main__':
    print(json.dumps(evidence(),sort_keys=True,indent=2))
