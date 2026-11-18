"""Exact finite tests for the norm cuts in cubic.md. Standard library only."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import isqrt
import json


ONE = (1, 0)
ZERO = (0, 0)
ROOTS = (ONE, (0, 1), (-1, -1))


def mul(z, w):
    a, b = z
    c, d = w
    return a*c - b*d, a*d + b*c - b*d


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def norm(z):
    return z[0]**2 - z[0]*z[1] + z[1]**2


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def first_split_prime(n):
    while n % 3 != 1 or not is_prime(n):
        n += 1
    return n


def ideal_primes(ns):
    out = []
    for p in ns:
        assert is_prime(p) and p % 3 == 1
        m = 2*isqrt(p) + 2
        gs = [(a, b) for a in range(-m, m+1) if a % 3 == 1
              for b in range(-m, m+1, 1) if b % 3 == 0 and norm((a, b)) == p]
        assert len(gs) == 2
        out.extend(gs)
    return out


def cubic(z, pi):
    """Return chi_pi(z) from the specified primary generator and residue field."""
    p = norm(pi)
    r = (-pi[0] * pow(pi[1], -1, p)) % p
    assert (r*r + r + 1) % p == 0
    v = pow((z[0] + r*z[1]) % p, (p-1)//3, p)
    if not v:
        return ZERO
    return ROOTS[[1, r, r*r % p].index(v)]


def staircase():
    # Increasing row norms with a separate, disjoint dyad of column norms.
    f, step, size = 30000, 120, 30
    level = 5*f*f//2
    endpoints = [first_split_prime(f + step*i) for i in range(size+1)]
    cols = [first_split_prime(level//endpoints[j+1] + 1) for j in range(size)]
    rows = endpoints[:-1]
    assert all(rows[i]*cols[j] <= level if i <= j
               else rows[i]*cols[j] > level for i in range(size) for j in range(size))
    assert len(set(rows+cols)) == 2*size
    return {"rows": rows, "columns": cols, "partial_product_limit": level,
            "rank_by_triangularity": size}


def tuples_and_rows():
    x = ideal_primes((7, 13, 19, 31))
    y = ideal_primes((13, 19, 31, 37))
    z = ideal_primes((37, 43, 61))
    assert set(x).isdisjoint(z)
    row_ps = ideal_primes((7, 13, 19, 31, 37, 43, 61, 67))
    row_qs = [ONE] + ideal_primes((13, 19, 37, 43, 67))
    full = list(product(x, y, z))
    cut = [(a,b,c) for a,b,c in full if norm(a)*norm(b) <= 500 and 2*norm(b) <= norm(c)]
    counts = Counter(mul(mul(a,b),c) for a,b,c in cut if len({a,b,c}) == 3)
    histogram = Counter(counts.values())
    moments = {"q_unit": 0, "q_prime": 0}
    row_count = Counter()
    vanishing = 0
    nonreal = 0
    for p, q in product(row_ps, row_qs):
        if p == q:
            continue
        h = mul(p, mul(q, q))
        # Compute coefficient sum by evaluating chi_p(b) chi_q(b)^2 instead.
        direct = ZERO
        for v, mult in counts.items():
            t = cubic(v, q) if q != ONE else ONE
            w = mul(cubic(v, p), mul(t, t))
            direct = add(direct, (mult*w[0], mult*w[1]))
        # Independent sum in the opposite orientation using the middle role as pivot.
        sliced = ZERO
        for b in y:
            left = ZERO
            right = ZERO
            for a in x:
                if a != b and norm(a)*norm(b) <= 500:
                    left = add(left, cubic(h, a))
            for c in z:
                if b != c and 2*norm(b) <= norm(c):
                    right = add(right, cubic(h, c))
            sliced = add(sliced, mul(mul(left, cubic(h,b)), right))
        assert direct == sliced
        name = "q_unit" if q == ONE else "q_prime"
        row_count[name] += 1
        moments[name] += norm(direct)
        vanishing += direct == ZERO
        nonreal += direct[1] != 0
    # Check one actual transition band and the bound from fixing the two other roles.
    lower, upper = Fraction(15*500, 16), Fraction(17*500, 16)
    actual = sum(lower <= norm(a)*norm(b) <= upper for a,b,c in full)
    cap = 0
    for b, c in product(y, z):
        lo, hi = lower/norm(b), upper/norm(b)
        cap += 2*max(0, hi.__floor__() - lo.__ceil__() + 1)
    assert 0 < actual <= cap
    return {"raw_tuples":len(full), "gated_tuples":len(cut),
            "gated_squarefree_tuples": sum(counts.values()),
            "distinct_squarefree_products": len(counts),
            "multiplicities": dict(sorted(histogram.items())),
            "rows":dict(row_count), "sum_squared_norm":moments,
            "zero_rows":vanishing, "nonreal_rows": nonreal,
            "band_15_16_to_17_16_before_sieving":{"tuples":actual,"integer_slice_bound":cap}}


def exponents():
    data = []
    for i in range(51):
        t = Fraction(i, 100)
        a = 1+max(1, 2*t, (2+4*t)/3)
        b = Fraction(4,3)+2*t
        nu = Fraction(1,2)-t
        assert a == max(2, Fraction(7,3)-4*nu/3) and b == Fraction(7,3)-2*nu
        assert (max(a,b) < Fraction(7,3)) == (t < Fraction(1,2))
        if i in (36, 49, 50):
            data.append([str(t), str(a), str(b)])
    return data


if __name__ == "__main__":
    print(json.dumps({"rank_witness":staircase(), "arithmetic":tuples_and_rows(),
                      "height_exponents_theta_first_second":exponents()}, indent=2))
