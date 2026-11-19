"""Reflection completions in the integer kernel of the seven reciprocal moments.

Requires python-flint (fmpz_mat). No floating point or optimization solver.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd, lcm, prod
import json

from flint import fmpz_mat


SCALE = 12_252_240
BUDGET = 2332
DENOMINATORS = [d for d in range(2, BUDGET+2) if SCALE % d == 0]


def centres():
    by_sum = defaultdict(list)
    for d, e in combinations(DENOMINATORS, 2):
        by_sum[SCALE//d + SCALE//e].extend((d, e))
    for d in DENOMINATORS:
        by_sum[2*(SCALE//d)].append(d)
    return {s: sorted(ds) for s, ds in by_sum.items()}


def rows(ds, normalize=True):
    xs = [SCALE//d for d in ds]
    if normalize:
        lo = min(xs)
        step = gcd(*(x-lo for x in xs))
        xs = [(x-lo)//step for x in xs]
    return [[x**k for k in range(7)] for x in xs]


def index(a):
    # For a rank-seven row lattice this is its index in Z^7.
    return abs(int(fmpz_mat(fmpz_mat(a).hnf().tolist()[:7]).det()))


def peel(ds):
    while len(ds) >= 8 and sum(d-1 for d in sorted(ds)[:8]) <= 2*BUDGET:
        a = rows(ds)
        idx = index(a)
        orders = [index(a[:i]+a[i+1:])//idx for i in range(len(ds))]
        keep = [d for d, h in zip(ds, orders) if (d-1)*h <= BUDGET]
        if keep == ds:
            return ds
        ds = keep
    return []


def outside_orders(core, outside):
    hs = fmpz_mat(rows(core,normalize=False)).hnf().tolist()[:7]
    inv = fmpz_mat(hs).inv().tolist()
    den = lcm(*(int(v.denominator) for row in inv for v in row))
    scaled = [[int(v*den) for v in row] for row in inv]
    for d in outside:
        x = SCALE//d
        v = [x**i for i in range(7)]
        nums = [sum(a*b[j] for a,b in zip(v,scaled)) for j in range(7)]
        yield d, den//gcd(den,*nums)


def kernel(ds):
    a = fmpz_mat(rows(ds))
    h, u = a.hnf(transform=True)
    assert u*a == h and abs(int(u.det())) == 1
    assert not any(v for row in h.tolist()[7:] for v in row)
    k = fmpz_mat(u.tolist()[7:])
    rank = k.nrows()
    order = list(range(len(ds)))
    for i in range(rank):
        def forced_cost(j):
            return (ds[order[j]]-1)*gcd(*(int(k[t,j]) for t in range(i,rank)))
        j = max(range(i,len(ds)),key=forced_cost)
        order[i],order[j] = order[j],order[i]
        data = k.tolist()
        for row in data:
            row[i],row[j] = row[j],row[i]
        k = fmpz_mat(data).hnf()
    return [ds[i] for i in order], [[int(v) for v in row] for row in k.tolist()]


def solve(ds, required):
    ds, basis = kernel(ds)
    n,r = len(ds),len(basis)
    value = [0]*n
    periods = [[gcd(*(row[j] for row in basis[i:])) for j in range(n)] for i in range(r+1)]
    cost = [d-1 for d in ds]
    nodes, answers = 0, []
    def visit(i, plus, minus):
        nonlocal nodes
        nodes += 1
        needed = 0
        for j in range(i,n):
            c,g = cost[j],periods[i][j]
            if not g:
                v = value[j]*c
                if v>plus or -v>minus or (not v and ds[j] in required):
                    return
                needed += abs(v)
            else:
                left,right = (value[j]%g)*c,(-value[j]%g)*c
                if not left and ds[j] in required:
                    left = right = g*c
                if left>plus and right>minus:
                    return
                needed += min(left if left<=plus else plus+minus+1,
                              right if right<=minus else plus+minus+1)
        if needed>plus+minus:
            return
        if i == r:
            pos = sum(max(v,0)*c for v,c in zip(value,cost))
            neg = sum(max(-v,0)*c for v,c in zip(value,cost))
            if any(value) and max(pos,neg)<=BUDGET:
                witness = tuple(sorted((d,v) for d,v in zip(ds,value) if v))
                assert all(sum(v*(SCALE//d)**k for d,v in witness)==0 for k in range(7))
                assert required.issubset({d for d,v in witness})
                answers.append(witness)
            return
        g = basis[i][i]
        assert g>0 and all(basis[k][i]==0 for k in range(i+1,r))
        low = -((minus//cost[i]+value[i])//g)
        high = (plus//cost[i]-value[i])//g
        for t in range(low,high+1):
            if value[i]+t*g==0 and ds[i] in required:
                continue
            for j in range(i,n):
                value[j] += t*basis[i][j]
            v = value[i]*cost[i]
            visit(i+1,plus-max(0,v),minus-max(0,-v))
            for j in range(i,n):
                value[j] -= t*basis[i][j]
    visit(0,BUDGET,BUDGET)
    return nodes, answers


def eight_node_circuits():
    # Three complete pairs at one centre use six distinct columns.
    # The other two must cancel on the degree-six annihilator of those columns.
    by_sum = defaultdict(list)
    for a,b in combinations(DENOMINATORS,2):
        by_sum[SCALE//a+SCALE//b].append((a,b))
    count = Counter()
    winners = set()
    points = {d: SCALE//d for d in DENOMINATORS}
    for paired in by_sum.values():
        for match in combinations(paired,3):
            fixed = tuple(d for pair in match for d in pair)
            count['six_node_seeds'] += 1
            fixed_cost = sum(d-1 for d in fixed)
            if fixed_cost >= 2*BUDGET:
                continue
            count['affordable_six_node_seeds'] += 1
            roots = [points[d] for d in fixed]
            seen = {}
            for d in DENOMINATORS:
                if d in fixed or fixed_cost+d-1 >= 2*BUDGET:
                    continue
                delta = abs(prod(points[d]-x for x in roots))
                bound = min(BUDGET,2*BUDGET-fixed_cost-1)//(d-1)
                for j in range(1,bound+1):
                    k = j*delta
                    for e in seen.get(k,()):
                        count['matched_multiples'] += 1
                        # Test once, at the smallest positive pair of coefficients.
                        if gcd(j,k//abs(prod(points[e]-x for x in roots))) != 1:
                            continue
                        ds = sorted(fixed+(e,d))
                        xs = [points[t] for t in ds]
                        deriv = [prod(v-u for u in xs if u!=v) for v in xs]
                        scale = lcm(*map(abs,deriv))
                        coefficients = [scale//w for w in deriv]
                        assert gcd(*coefficients)==1
                        pos = sum(max(0,w)*(t-1) for t,w in zip(ds,coefficients))
                        neg = sum(max(0,-w)*(t-1) for t,w in zip(ds,coefficients))
                        count['primitive_pair_tests'] += 1
                        if max(pos,neg) <= BUDGET:
                            winners.add(tuple(zip(ds,coefficients)))
                for j in range(1,bound+1):
                    k = j*delta
                    if k not in seen:
                        seen[k]=[d]
                    else:
                        seen[k].append(d)
    return dict(counts=count,unoriented_primitive_solutions=sorted(winners))


def main():
    stats = Counter()
    hits, hard = [], []
    for s,core in sorted(centres().items()):
        if len(core)<7:
            continue
        stats['eligible_centres_including_single_exception'] += 1
        if len(core)>=8:
            stats['centres_with_eight_dictionary_points'] += 1
            remain = peel(core)
            if remain:
                nodes, found = solve(remain,set())
                stats['pure_kernel_cases'] += 1
                stats['pure_kernel_nodes'] += nodes
                hard.append((s,len(core),len(remain),nodes))
                hits.extend((s,None,w) for w in found)
        outs = [d for d in DENOMINATORS if d not in core]
        stats['outside_candidates'] += len(outs)
        for d,ord_d in outside_orders(core,outs):
            if (d-1)*ord_d>BUDGET:
                continue
            stats['outside_after_order'] += 1
            remain = peel(sorted(core+[d]))
            if d not in remain:
                continue
            stats['outside_kernel_cases'] += 1
            nodes, found = solve(remain,{d})
            stats['outside_kernel_nodes'] += nodes
            hits.extend((s,d,w) for w in found)
    assert len(hits)==2 and all(s==374374 and d is None for s,d,w in hits)
    print(json.dumps(dict(dictionary=len(DENOMINATORS),budget=BUDGET,scale=SCALE,
                          eight_node_audit=eight_node_circuits(),counts=stats,pure_remaining=hard,oriented_solutions=hits),
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
