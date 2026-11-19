"""Exact finite tests for the labelled semiprime Hamilton layouts."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import exp, factorial, gcd, log1p, sqrt
import json

PRIMES = (2, 3, 5, 7, 11, 13)


def triangle(r):
    return r * (r + 1) // 2


def one_side_min(r):
    m = r // 2
    saving = ((m - 2) * (m - 1) * (2*m - 3) // 6 if r % 2 == 0
              else m * (m - 1) * (m - 2) // 3)
    return r*(r-1)*(r+1)*(r+2)*(3*r-1)//60 - saving


def graph(r):
    p = PRIMES[:r]
    vertices = [a*b for j, b in enumerate(p) for a in p[:j+1]]
    edges = [(a,b) for a,b in combinations(vertices,2) if gcd(a,b)>1]
    return vertices, edges


def lengths(path, edges):
    rank = {v:i for i,v in enumerate(path)}
    spans = [abs(rank[u]-rank[v]) for u,v in edges]
    return sum(spans), max(spans)


def star_paths(r):
    # The new star is always on the right in the working orientation.
    if r == 1:
        yield (4,), (), ()
        return
    p = PRIMES[r-1]
    star = tuple(a*p for a in PRIMES[:r])
    for old, slots, flips in star_paths(r-1):
        for sign in (1,-1) if r>=3 else (1,):
            core = old if sign==1 else old[::-1]
            for new in permutations(star):
                if gcd(core[-1],new[0])>1:
                    yield core + new, slots+(new.index(p*p),), flips+(sign,)


def one_side_cost(r, slots):
    base = r*(r-1)*(r+1)*(r+2)*(3*r-1)//60
    return base + sum((r+1-2*j)*(t-j+1) for j,t in enumerate(slots,2))


def orientation_loss(slots, flips):
    labels = []
    orientation = 1
    for sign in flips:
        orientation *= sign
        labels.append(orientation)
    return sum((triangle(i+2)-1-2*slots[i]) * (x != y)
               for i,x in enumerate(labels) for y in labels[i+1:])


def threshold_count(r, first, deficit):
    # Fix the head of the last star, coded by a label in 1..r-1.
    bound = r-1-deficit
    if bound < -triangle(first-1):
        return 0
    free = [min(r-1,bound+triangle(i-1)) for i in range(1,r) if i != first]
    free.append(r-1)  # the square
    total = 1
    for used, end in enumerate(free):
        total *= max(0,end-used)
    return total


def exhaustive(r):
    _,edges=graph(r)
    minimum = None
    paths = 0
    perfect = 0
    for path,slots,flips in star_paths(r):
        value, _ = lengths(path,edges)
        baseline=one_side_cost(r,slots)
        assert value-baseline == orientation_loss(slots,flips)
        paths += 1
        if minimum is None or value<minimum:
            minimum, perfect = value, 1
        elif value==minimum:
            perfect += 1
    assert minimum == one_side_min(r)
    return dict(r=r,oriented_constructions=paths,minimum=minimum,
                minimizing_constructions=perfect)


def first_distribution(r):
    result = [Fraction(1)]
    for size in range(3,r+1):
        denominator = 2*size-5
        result = [(1-x)/denominator for x in result]
        result.append(Fraction(size-2,denominator))
    return result


def finite_law(r):
    primes=PRIMES[:r]
    vertices,edges=graph(r)
    end_star=tuple(primes[-1]*p for p in primes)
    # Check the terminal permutation for every formal head, then test the
    # maximum against actual gcd edges on every reachable prefix below.
    total=0
    for head in range(1,r):
        choices=list(range(1,r+1))
        choices.remove(head)
        counts=Counter()
        for suffix in permutations(choices):
            order=(head,)+suffix
            excess=max(order.index(i)-triangle(i-1) for i in range(1,r))
            counts[r-1-excess]+=1
        for d in range(r+1):
            assert sum(v for k,v in counts.items() if k>=d)==threshold_count(r,head,d)
        total+=sum(counts.values())
    # Direct gcd construction for every one-sided path through r=5.
    paths = 0
    heads = Counter()
    observed_tail = Counter()
    for path,slots,flips in star_paths(r):
        if -1 in flips:
            continue
        _,stretch=lengths(path,edges)
        positions={v:i for i,v in enumerate(path[-r:])}
        rhs=triangle(r-1)+max(positions[end_star[i]]-triangle(i)
                               for i in range(r-1))
        assert stretch==rhs and set(path)==set(vertices)
        heads[path[-r]//primes[-1]]+=1
        observed_tail[triangle(r)-1-stretch]+=1
        paths+=1
    mixture = first_distribution(r)
    assert mixture == [Fraction(heads[p],paths) for p in primes[:-1]]
    for d in range(r):
        exact = sum(q*threshold_count(r,i,d)/factorial(r-1)
                    for i,q in enumerate(mixture,1))
        assert exact==Fraction(sum(n for t,n in observed_tail.items() if t>=d),paths)
    return dict(r=r,conditional_last_stars=total,direct_gcd_paths=paths,
                head_probabilities=[str(q) for q in mixture])


def scaled_tail(r, head, u):
    d=int(u*r**(2/3)+0.5)
    total=0.0
    for i in range(1,r):
        deficit=d-triangle(i-1)
        if deficit<=0:
            break
        if i==head:
            continue
        index=i-int(i>head)
        total+=log1p(-deficit/(r-index))
    return exp(total)


def unrestricted_six():
    """Subset cut recurrence. NumPy stores all endpoint costs in 16 bits."""
    import numpy as np
    vertices, edges = graph(6)
    n = len(vertices)
    neighbors = [[j for j,v in enumerate(vertices) if v!=u and gcd(u,v)>1]
                 for u in vertices]
    masks = np.arange(1<<n, dtype=np.int32)
    boundaries = np.zeros(1<<n, dtype=np.int16)
    pop = np.zeros(1<<n, dtype=np.uint8)
    for i, adjacent in enumerate(neighbors):
        bit = 1<<i
        small = masks[:bit]
        pop[bit:2*bit] = pop[:bit]+1
        neighbor_bits = sum(1<<j for j in adjacent)
        count = pop[small & neighbor_bits].astype(np.int16)
        boundaries[bit:2*bit] = boundaries[:bit]+len(adjacent)-2*count
    size = 1<<n
    # Any actual length sum is at most 90*20; the sentinel stays separate.
    inf = 30000
    total = np.full(size,inf,dtype=np.int16)
    total[0] = 0
    end = np.full((size,n),inf,dtype=np.int16)
    for t in range(1,n+1):
        level = masks[pop==t]
        for i,adjacent in enumerate(neighbors):
            bit = 1<<i
            subset = level[(level & bit)!=0]
            prev = subset-bit
            cut = boundaries[subset]
            total[subset] = np.minimum(total[subset],total[prev]+cut)
            if t==1:
                end[subset,i] = cut
            else:
                best = np.full(len(subset),inf,dtype=np.int16)
                for j in adjacent:
                    best = np.minimum(best,end[prev,j])
                end[subset,i] = np.minimum(inf,best+cut)
    cost = int(end[-1].min())
    s = size-1
    target = int(end[-1].argmin())
    path = []
    while s:
        path.append(vertices[target])
        wanted = int(end[s,target]-boundaries[s])
        s -= 1<<target
        if s:
            target = next(j for j in neighbors[target]
                          if s>>j&1 and end[s,j]==wanted)
    assert all(gcd(u,v)>1 for u,v in zip(path,path[1:]))
    assert lengths(path,edges)[0]==cost==one_side_min(6)
    return dict(vertices=n,subsets=size,unrestricted=int(total[-1]),
                hamilton=cost,path=path)


def run():
    conditional = []
    for r in range(3,6):
        conditional.append(finite_law(r))
    r=9
    head=1
    exact=[str(Fraction(threshold_count(r,head,d),factorial(r-1))) for d in range(r)]
    return dict(r6_global=unrestricted_six(),two_ended=[exhaustive(r) for r in range(3,6)],
                conditional_checks=conditional,
                r9_head1_survival_d_0_through_8=exact,
                numerical_survival=[dict(r=r,head=head,u=u,
                    finite=round(scaled_tail(r,head,u),8),
                    limit=round(exp(-2*sqrt(2)*u**1.5/3),8))
                    for r in (100,10000,1000000)
                    for head in (1,r-1) for u in (0.5,1,2)])


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
