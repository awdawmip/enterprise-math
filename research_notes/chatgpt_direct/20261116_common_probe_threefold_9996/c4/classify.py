"""Reconstruct every minimizing row and normalizer orbit for the winning quotient supports."""
from itertools import combinations, product

def classify(previous, generator, bank, hits):
    import sys
    old=previous/'previous';older=old/'previous'
    sys.path[:0]=[str(old/'group'),str(older/'bounds')]
    from cyclic11 import observations,class_cost
    from generate import maps
    from functools import cache
    bad,pair=observations()
    cells=[];assigned=set()
    for p in range(125):
        if p in assigned:continue
        row=[];x=p
        while x not in row:
            row.append(x);assigned.add(x);x=generator[x]
        cells.append(row)
    assert len(cells)==32
    short=[];prices={};target={a for s,a,c in hits}|{s^a for s,a,c in hits}
    with bank.open()as f:
        for line in f:
            r,s,c,n,lo,hi=map(int,line.split())
            if r<4:short.append((r,s,c));prices[r,s]=c
            elif s in target:prices[r,s]=c
    def shape(rows):return tuple(sorted(tuple(sorted(row)) for row in rows))
    @cache
    def lift(r,s):
        terms=[v for i,v in enumerate(cells)if s>>i&1]
        assert all(len(v)%r==0 for v in terms)
        result=[]
        def go(i,points):
            if i==len(terms):
                if r*class_cost(points,pair)==prices[r,s]:
                    rows=[];u=points
                    for j in range(r):
                        rows.append(u);u=[generator[x]for x in u]
                    result.append(shape(rows))
                return
            options=[terms[i][j::r] for j in range(r)]
            for opt in options if i else options[:1]:
                if any(bad[x][y]>>z&1 for x,y in combinations(points,2) for z in opt):continue
                if any(bad[x][y]>>z&1 for x in points for y,z in combinations(opt,2)):continue
                if any(bad[x][y]>>z&1 for x,y,z in combinations(opt,3)):continue
                go(i+1,points+opt)
        go(0,[])
        assert result and len(set(result))==len(result)
        return result
    def short_sets(free, left, cost):
        if not free:return [[]] if left==0 and cost==0 else []
        pivot=free&-free;result=[]
        for r,s,c in short:
            if r>left or c>cost or s&~free or not s&pivot:continue
            for tail in short_sets(free^s,left-r,cost-c):result.append([(r,s)]+tail)
        return result
    tally=[];tables=set()
    for s,a,c in sorted(hits):
        combos=short_sets((2**32-1)^s,4,c)
        ns=0
        for choice in combos:
            for small in product(*(lift(r,v) for r,v in choice)):
                ns+=1
                for x,y in product(lift(4,a),lift(4,s^a)):
                    table=shape(row for part in (*small,x,y) for row in part)
                    assert table not in tables;tables.add(table)
        tally.append([ns,len(lift(4,a)),len(lift(4,s^a))])
    linear,translations,_=maps();eye=bytes(range(125))
    def mul(x,y):return bytes(x[i]for i in y)
    h={eye};g=generator
    while g not in h:h.add(g);g=mul(generator,g)
    group={mul(t,a) for a in linear for t in translations}
    normal=[k for k in group if mul(k,mul(generator,bytes(k.index(i)for i in range(125)))) in h]
    def act(g,table):return shape(tuple(g[p]for p in r)for r in table)
    left=set(tables);samples=[];orbits=[];sizes=[]
    while left:
        rep=min(left);samples.append(rep)
        images={act(g,rep)for g in normal};assert images<=left;left-=images
        assert {k for k in group if act(k,rep)==rep}==h
        sizes.append(len(images));orbits.append(len(group)//len(h))
    return dict(lifts=tally,fixed_group_optima=len(tables),normalizer=len(normal),conjugates=len(group)//len(normal),
                normalizer_orbit_sizes=sizes,affine_orbit_sizes=orbits,total=sum(orbits)),samples
