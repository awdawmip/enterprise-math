"""Exact checks for the square-root rows, rank thresholds and exceptional primes."""
from collections import Counter
from itertools import product
import json
from math import comb, gcd, isqrt, pi, prod, sin, log, sqrt


def factor(n):
    factors = {}
    for p in range(2, isqrt(n) + 1):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    if n > 1:
        factors[n] = 1
    return factors


def rank(rows):
    pivots = {}
    for row in rows:
        while row and row.bit_length() in pivots:
            row ^= pivots[row.bit_length()]
        if row:
            pivots[row.bit_length()] = row
    return len(pivots)


def local(n, p, e):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return e <= a or (a % 2 == 0 and pow(n, (p-1)//2, p) == 1)


def jacobi(a, factors):
    if any(a % p == 0 for p in factors):
        return 0
    return prod(1 if pow(a, (p-1)//2, p) == 1 else -1 for p in factors)


def main():
    gaps = (1, 2, 4, 8, 16)
    rows = [(2*j+1)**2 + 16*k for k in gaps for j in range(k)]
    parts = [factor(n) for n in rows]
    primes = sorted(set().union(*parts))
    vectors = [sum(1 << primes.index(p) for p, e in f.items() if e % 2) for f in parts]
    cores = [prod(p for p,e in f.items() if e % 2) for f in parts]
    special = {17, 33, 41, 697}
    exceptional = [v for v,d in zip(vectors,cores) if d in special]
    ordinary = [v for v,d in zip(vectors,cores) if d not in special]
    assert rank(vectors) == 27 and len(ordinary) == rank(ordinary) == 24
    assert rank(exceptional) == 3
    ranks = Counter()
    for mask in range(1 << len(exceptional)):
        chosen = [v for j,v in enumerate(exceptional) if mask >> j & 1]
        for size in range(25):
            ranks[(rank(chosen)+size, len(chosen)+size)] += comb(24, size)
    assert sum(ranks.values()) == 2**31
    capacities = [max(s for (r,s) in ranks if r == i) for i in range(28)]
    assert capacities == [0,3,5] + [i+4 for i in range(3,28)]
    limit = 250001
    spf = list(range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if spf[p] == p:
            for n in range(p*p, limit+1, p):
                if spf[n] == n:
                    spf[n] = p
    masks = {1:(1 << len(rows))-1}
    local_masks = {}
    samples = {}
    hist = Counter()
    for m in range(3,limit+1,2):
        p = spf[m]
        t, e = m, 0
        while t%p == 0:
            t //= p
            e += 1
        if (p,e) not in local_masks:
            local_masks[p,e] = sum(int(local(n,p,e)) << j for j,n in enumerate(rows))
        hit = masks[m] = masks[t] & local_masks[p,e]
        if m >= 35:
            hist[hit.bit_count()] += 1
        if 35 <= m <= 701:
            squares = {a*a%m for a in range(m)}
            assert hit == sum((n%m in squares) << j for j,n in enumerate(rows))
            offset = 0
            for k in gaps:
                s = m - 2*k
                actual = {(-s*a-pow(2*a,-1,m))%m for a in range(1,m) if gcd(a,m)==1}
                outside = sum(min(y,m-y) > (s-1)//2 for y in actual)
                assert outside == 2*((hit >> offset) & ((1<<k)-1)).bit_count()
                offset += k
        if m in (10001,100001,limit):
            samples[str(m)] = dict(sorted(hist.items()))
    multiplicities = {}
    for p in (3,5):
        multiplicities[str(p)] = [[int(local(n,p,e)) for n in (17,153,425,33,297)] for e in range(1,6)]
    # Finite product with p <= 10000. Doubling the cutoff is a reproducible check.
    approximate = {}
    for cutoff in (5000,10000):
        single = {}
        for d in sorted(set(cores)):
            f = factor(d)
            ell = -sum(jacobi(a,f)*log(2*sin(pi*a/d)) for a in range(1,d))/sqrt(d)
            inert = prod(1-1/(p*p) for p in range(3,cutoff+1,2)
                         if spf[p]==p and jacobi(p,f)==-1)
            ramified = prod((1+1/p)**2*(1-1/p) for p in f)
            single[d] = sqrt(ell*inert*ramified)/(2*sqrt(pi))
        rest = sum(v for d,v in single.items() if d not in (17,33))
        weights = [rest + 154/225*single[17] + single[33]/9, single[33], single[17]]
        approximate[str(cutoff)] = {
            "C17":round(single[17],8), "C33":round(single[33],8),
            "sum_C":round(sum(weights),8),
            "conditional_T_1_2_3":[round(w/sum(weights),8) for w in weights]}
    result = {"rows": rows, "squarefree_cores":cores, "rank_capacities":capacities,
              "all_label_subsets_counted":sum(ranks.values()), "rank":rank(vectors),
              "rank_thresholds":[next(r for r,v in enumerate(capacities) if v >= h) for h in range(1,32)],
              "small_direct_moduli":334, "integer_histograms_M_at_least_35":samples,
              "local_3_5_at_exponents_1_to_5":multiplicities,
              "finite_product_approximations":approximate}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
