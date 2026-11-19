"""Exact finite checks for the trace of a uniformly counted idempotent."""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from math import prod
import json


def trim(coeffs):
    a = list(coeffs)
    while a and not a[-1]:
        a.pop()
    return tuple(a)


def divide(f, g, m):
    """Monic divisor, all coefficients in increasing degree."""
    assert g[-1] == 1
    rem = list(trim(x % m for x in f))
    quo = [0] * max(0, len(rem) - len(g) + 1)
    while len(rem) >= len(g):
        shift = len(rem) - len(g)
        top = rem[-1]
        quo[shift] = top
        for i, val in enumerate(g):
            rem[shift+i] = (rem[shift+i] - top*val) % m
        while rem and not rem[-1]:
            rem.pop()
    return trim(quo), tuple(rem)


def gcd_poly(f, g, p):
    f = trim(x % p for x in f)
    g = trim(x % p for x in g)
    while g:
        scale = pow(g[-1], -1, p)
        g = tuple(x*scale % p for x in g)
        f, g = g, divide(f, g, p)[1]
    return tuple(x*pow(f[-1], -1, p) % p for x in f) if f else ()


def factors(f, r, m):
    for low in product(range(m), repeat=r):
        g = low + (1,)
        h, rem = divide(f, g, m)
        if not rem:
            yield g, h


def grass(p, r, d):
    return prod(p**(d-i)-1 for i in range(r)) // prod(p**(r-i)-1 for i in range(r))


def interval_hist(f, r, p, e, checks):
    d, q = len(f)-1, p**e
    cross = r*(d-r)
    grass1 = grass(p, r, d)
    orbit = q**cross * p**((e-1)*cross) * grass1
    values = [orbit] * q
    for k in range(1, e+1):
        v = p**k
        scale = orbit // (grass1 * p**((k-1)*cross))
        by_fibre = {}
        for g, h in factors(f, r, v):
            t = -g[-2] % v if r else 0
            if k > 1 and len(gcd_poly(g, h, p)) > 1:
                reduced_pair = tuple(x % (v//p) for x in g+h)
                by_fibre.setdefault(reduced_pair, Counter())[t] += 1
                continue
            for z in range(q):
                if (t-z) % v == 0:
                    values[z] += scale * (v-v//p)
                elif (t-z) % (v//p) == 0:
                    values[z] -= scale * (v//p)
        for counts in by_fibre.values():
            a = next(iter(counts)) % (v//p)
            assert len(counts) == p and all(
                counts[a+i*(v//p)] == counts[a] > 0 for i in range(p))
            checks["singular_lift_fibres"] += 1
    assert all(t % q == 0 for t in values)
    hist = [t//q for t in values]
    assert sum(hist) == orbit
    return hist


def rank_mod(a, d, p):
    rows = [list(a[i*d:(i+1)*d]) for i in range(d)]
    k = 0
    for j in range(d):
        pivot = next((u for u in range(k, d) if rows[u][j] % p), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        inv = pow(rows[k][j] % p, -1, p)
        for u in range(k+1, d):
            c = rows[u][j] * inv % p
            rows[u] = [(x-c*y) % p for x, y in zip(rows[u],rows[k])]
        k += 1
    return k


def scan_matrices(d, p, e):
    q = p**e
    data = [[] for _ in range(d+1)]
    for a in product(range(q), repeat=d*d):
        if all((sum(a[i*d+h]*a[h*d+j] for h in range(d))-a[i*d+j]) % q == 0
               for i in range(d) for j in range(d)):
            data[rank_mod(a,d,p)].append(a)
    return data


def trace_companion(f, a, q):
    d = len(f)-1
    return (sum(a[i*d+i+1] for i in range(d-1))
            - sum(c*v for c,v in zip(f[:-1],a[-d:]))) % q


def multiply_mod(f, g, divisor, p):
    if not f or not g:
        return ()
    coeff = [0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            coeff[i+j] += a*b
    return divide(coeff, divisor, p)[1]


def x_power(n, f, p):
    ans, base = (1,), (0,1)
    while n:
        if n % 2:
            ans = multiply_mod(ans, base, f, p)
        base = multiply_mod(base, base, f, p)
        n //= 2
    return ans


def cycle_type(f, p):
    counts = {}
    for j in range(1, len(f)):
        a = list(x_power(p**j, f, p))
        a += [0]*max(0, 2-len(a))
        a[1] -= 1
        deg = len(gcd_poly(f, a, p))-1
        total = deg - sum(k*m for k,m in counts.items() if j % k == 0)
        assert total % j == 0
        counts[j] = total//j
    answer = tuple(k for k,m in counts.items() for _ in range(m))
    assert sum(answer) == len(f)-1
    return answer


def quartic():
    f = (-1,-1,0,0,1)
    census = Counter()
    for p in range(2,1001):
        if p == 283 or any(p % i == 0 for i in range(2, int(p**0.5)+1)):
            continue
        census[cycle_type(f,p)] += 1
    def decomposition(s):
        todo, lengths = set(range(4)), []
        while todo:
            i = min(todo)
            start = i
            while i in todo:
                todo.remove(i)
                i = s[i]
            assert i == start
            j = s[i]
            length = 1
            while j != i:
                length += 1
                j = s[j]
            lengths.append(length)
        return tuple(sorted(lengths))
    group = Counter(decomposition(s) for s in permutations(range(4)))
    good = {(1,3),(4,)}
    assert cycle_type(f,2) == (4,) and cycle_type(f,7) == (1,3)
    assert sum(group[s] for s in good) == 14
    return {"Frobenius_at_2_and_7":[[4],[1,3]], "group_counts":{str(k):v for k,v in sorted(group.items())},
            "unramified_primes_through_1000":sum(census.values()),
            "factor_patterns":{str(k):v for k,v in sorted(census.items())},
            "rank_two_uniform_count_in_census":sum(census[s] for s in good)}


def main():
    tally = Counter()
    settings, examples = [], {}
    digest = sha256()
    for d,p,e in [(2,2,1),(2,2,2),(2,2,3),(2,2,4),(2,3,2),
                   (2,5,1),(3,2,1),(3,2,2),(3,3,1),(4,2,1)]:
        q = p**e
        data = scan_matrices(d,p,e)
        settings.append([d,p,e,q**(d*d),[len(a) for a in data]])
        for low in product(range(q), repeat=d):
            f = low+(1,)
            for r,matrices in enumerate(data):
                direct = [0]*q
                for a in matrices:
                    direct[trace_companion(f,a,q)] += 1
                result = interval_hist(f,r,p,e,tally)
                assert direct == result, (f,r,p,e,direct,result)
                key = [d,p,e,low,r,result]
                digest.update(json.dumps(key,separators=(",",":")).encode()+b"\n")
                tally["direct_histograms"] += 1
                if (d,p,e,r) == (2,2,3,1) and low in [(0,0),(0,7),(1,1)]:
                    examples[str(low)] = result
    print(json.dumps({"polynomial_order":"constant coefficient first; leading 1 omitted in examples",
                      "settings_d_p_e_raw_matrices_and_idempotent_counts_by_rank":settings,
                      "tests":dict(tally),"ordered_histograms_sha256":digest.hexdigest(),
                      "rank_one_examples_mod8":examples,"quartic_x4_minus_x_minus_one":quartic()},
                     indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
