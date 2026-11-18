"""Run with standard-library Python 3.10+. All reported counts are exact."""
import json
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations, combinations_with_replacement
from math import comb, gcd, prod


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)


def size(r, k):
    return comb(r+k-1, k) if r else int(k == 0)


def indices(r, k):
    return combinations_with_replacement(range(1, r+1), k)


def integer(v):
    return prod(PRIMES[i-1] for i in v)


def rotate(i, m):
    return m if i == m else (i-2) % (m-1)+1


def inverse(i, m):
    return m if i == m else i % (m-1)+1


@cache
def gray(r, k):
    if not k:
        return ((),)
    if r == 1:
        return ((1,)*k,)
    block = tuple(tuple(sorted(rotate(i, r) for i in v))+(r,)
                  for v in gray(r, k-1))
    return gray(r-1, k)+block


def rank(v):
    if not v or max(v) == 1:
        return 0
    m = max(v)
    rest = list(v)
    rest.remove(m)
    return size(m-1, len(v))+rank([inverse(i, m) for i in rest])


def unrank(r, k, a):
    if not k:
        return ()
    lo, hi = 1, r
    while lo < hi:
        mid = (lo+hi)//2
        if a < size(mid, k):
            hi = mid
        else:
            lo = mid+1
    m = lo
    if m == 1:
        return (1,)*k
    rest = unrank(m, k-1, a-size(m-1, k))
    return tuple(sorted(rotate(i, m) for i in rest))+(m,)


def check_shell(r, k, direct):
    v = gray(r, k)
    assert len(v) == size(r, k) and set(v) == set(indices(r, k))
    assert all(rank(t) == a and unrank(r, k, a) == t for a,t in enumerate(v))
    assert v[:size(r-1, k)] == gray(r-1, k)
    assert v[0] == (1,)*k and v[-1] == (r,)*k
    labels = list(map(integer, v))
    positions = {n:i for i,n in enumerate(labels)}
    layers = {integer(t):t[-1] for t in v}
    edges = set()
    for h in map(integer, indices(r, k-1)):
        for p,q in combinations(PRIMES[:r], 2):
            x,y = h*p,h*q
            assert gcd(x,y) == h
            edges.add((x,y))
    if direct:
        independent = set()
        for x,y in combinations(sorted(labels), 2):
            g = gcd(x,y)
            if x//g in PRIMES[:r] and y//g in PRIMES[:r]:
                independent.add((x,y))
        assert independent == edges
    assert all(tuple(sorted((x,y))) in edges for x,y in zip(labels, labels[1:]))
    assert len(edges) == comb(r, 2)*size(r, k-1)
    cut = Counter()
    stretches = []
    snapped = 0
    for x,y in edges:
        a,b = sorted((layers[x],layers[y]))
        for t in range(a,b):
            cut[t] += 1
        delta = abs(positions[y]-positions[x])
        coarse = size(b,k)-size(a,k)
        assert abs(delta-coarse) <= size(r,k)-size(r-1,k)-1
        stretches.append(delta)
        snapped += coarse
    assert all(cut[t] == t*(r-t)*size(t,k-1) for t in range(1,r))
    assert snapped == sum((size(t+1,k)-size(t,k))*t*(r-t)*size(t,k-1)
                          for t in range(1,r))
    assert max(stretches) >= size(r-1,k)
    return dict(r=r,k=k,vertices=len(v),edges=len(edges),direct_gcd_graph=direct,
                retained=[len(v)-1,len(edges)],endpoints=[labels[0],labels[-1]],
                mean_normalized=str(Fraction(sum(stretches),len(edges)*len(v))),
                snapped_distance_sum=snapped,max_rank_gap=max(stretches),
                distinct_label_assignments=comb(r,k+1)*comb(k+1,2) if r>=k+1 else 0,
                gaps_over_one_quarter=sum(4*d>len(v) for d in stretches))


def check_numeric(limit=10**6, cutoff=14):
    omega = bytearray(limit+1)
    for p in range(2,limit+1):
        if omega[p]:
            continue
        q = p
        while q<=limit:
            for m in range(q,limit+1,q):
                omega[m]+=1
            q *= p
    layers = [[] for _ in range(7)]
    for n in range(2,limit+1):
        if omega[n]<=6:
            layers[omega[n]].append(n)
    rows = []
    for k in range(2,7):
        points = layers[k]
        histogram = Counter()
        small = Counter()
        large = Counter()
        for a,b in zip(points,points[1:]):
            g = gcd(a,b)
            j = omega[g]
            histogram[j] += 1
            if j:
                (small if g <= cutoff else large)[j] += 1
                assert (b-a)%g == 0
        assert sum(histogram.values())==len(points)-1
        bounds = []
        for j in range(1,k):
            short = sum(bisect_right(layers[k-j],limit//d)
                        for d in range(2,cutoff+1) if omega[d]==j)
            long = (points[-1]-points[0])//(cutoff+1)
            assert sum(c for h,c in small.items() if h>=j) <= short
            assert sum(c for h,c in large.items() if h>=j) <= long
            bounds.append(dict(j=j,small_gcd_upper=short,large_gcd_upper=long))
        rows.append(dict(k=k,vertices=len(points),gcd_omega=dict(sorted(histogram.items())),
                         exact_split_bounds=bounds))
    assert rows[0]['vertices']==210035
    return dict(limit=limit,gcd_cutoff=cutoff,layers=rows)


def check_order_statistics(r, k):
    """Independent count on the subfamily with k+1 distinct labels."""
    total = comb(r,k+1)*comb(k+1,2)
    macro = k*comb(r,k+1)
    assert Fraction(macro,total)==Fraction(2,k+1)
    powers = [i**k for i in range(r+1)]
    rows = []
    for u in (Fraction(1,2),Fraction(2,3)):
        threshold = u**k
        count = 0
        for top in range(k+1,r+1):
            cutoff = powers[top]-threshold*r**k
            second = bisect_left(powers,cutoff,hi=top)-1
            if second >= k:
                count += k*comb(second,k)
        finite = Fraction(count,total)
        predicted = Fraction(2,k+1)-2*threshold+Fraction(2*k,k+1)*u**(k+1)
        # Round independent continuous labels upwards and condition on distinctness.
        # Rounding perturbs their power gap by at most 2k/r, density <= 2
        # on the positive axis. The cutoffs tested stay away from its atom at 0.
        assert threshold>Fraction(2*k,r)
        assert abs(finite-predicted)<=Fraction(comb(k+1,2)+8*k,r)
        rows.append(dict(s=str(threshold),exact_distinct_tail=str(finite),
                         predicted_tail=str(predicted)))
    return dict(r=r,k=k,distinct_edges=total,
                zero_snapped=total-macro,thresholds=rows)


def main():
    for r in range(2,9):
        frozen = [(1,1)]
        for j in range(2,r+1):
            frozen.extend((i,j) for i in [j-1,*range(1,j-1),j])
        assert tuple(frozen) == gray(r,2)
    cases = [(r,k,True) for r in range(2,7) for k in range(1,6)]
    cases += [(8,6,False),(12,4,False),(16,3,False)]
    return dict(k3_r3=list(map(integer,gray(3,3))),
                gray_shells=[check_shell(*c) for c in cases],
                distinct_labels_limit_checks=[check_order_statistics(1024,k) for k in (2,3,6)],
                additive_order=check_numeric())


if __name__ == '__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
