"""Recover all phase and fixed-class choices on the optimizing quotient supports."""
from itertools import combinations,product
from collections import Counter

def realize(fixed_rows, gen, used, price, groups, pair, bad, class_cost):
    fixed_choices={q:c for q,c in fixed_rows if not q&~used}
    fixed=[]
    for a,b in combinations(sorted(fixed_choices),2):
        if a&b:continue
        c=used^a^b
        if b<c and c in fixed_choices and sum(fixed_choices[q] for q in (a,b,c))==price:fixed.append([a,b,c])
    cycles=[];seen=set()
    for i in range(125):
        if i in seen:continue
        cyc=[i]
        while gen[cyc[-1]]!=i:cyc.append(gen[cyc[-1]])
        cycles.append(cyc);seen.update(cyc)
    def pointset(q):return tuple(sorted(i for k,cyc in enumerate(cycles) if q>>k&1 for i in cyc))
    ways=[];packets=[];prices=[]
    for mask in groups:
        lines=[cyc for k,cyc in enumerate(cycles) if mask>>k&1]
        assert all(len(cyc)==3 for cyc in lines)
        best=10**6;winners=[]
        def dfs(j,row,forbidden):
            nonlocal best,winners
            if j==len(lines):
                cost=class_cost(row,pair)
                if cost<best:best,winners=cost,[]
                if cost==best:
                    t=list(row);orbit=[]
                    for _ in range(3):
                        orbit.append(tuple(sorted(t)));t=[gen[x]for x in t]
                    winners.append(orbit)
                return
            for x in lines[j] if j else lines[0][:1]:
                if forbidden>>x&1:continue
                unavailable=forbidden
                for i in row:unavailable|=bad[i][x]
                dfs(j+1,row+[x],unavailable)
        dfs(0,[],0)
        prices.append(best);packets.append(winners);ways.append(len(winners))
    partitions=set()
    for fixed_set in fixed:
        for combo in product(*packets):
            rows=list(map(pointset,fixed_set))+[r for orb in combo for r in orb]
            partitions.add(tuple(sorted(rows)))
    assert price+3*sum(prices)==9996
    return dict(fixed_ways=len(fixed),phase_ways=ways,seed_prices=prices,distinct=len(partitions)),partitions
