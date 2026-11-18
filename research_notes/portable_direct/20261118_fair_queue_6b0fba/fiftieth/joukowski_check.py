"""Exact arithmetic for the s=3 comparator on the projective line. Python 3.8+."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def heights(k):
    a, b = 1, 1
    result = []
    for j in range(1, k + 1):
        num, den = 3 * (a * a + b * b), a * b
        common = gcd(num, den)
        assert common == (3 if j % 2 == 0 else 1)
        a, b = num // common, den // common
        assert a > b and a < 3 ** (2 ** j)
        result.append((a, b))
    return result


def first_bad(p, k):
    a, b = 1, 1
    seen = set()
    for j in range(1, k + 1):
        a, b = (-3 * (a * a + b * b)) % p, (a * b) % p
        if a == 0 or b == 0:
            return j
        x = a * pow(b, -1, p) % p
        key = min(x, p - x)
        if key in seen:
            return j
        seen.add(key)
    return None


def certify_bad():
    pool = [2, 3, 5, 7, 37, 11, 13, 1373, 19, 31, 599, 809, 823, 6197,
            16971637, 17, 53, 73, 113, 643, 677, 727, 4027, 252341, 295037,
            462401, 7274341, 10181887, 17073239]
    assert len(set(pool)) == len(pool) and all(prime(p) for p in pool)
    points = heights(5)
    accumulated = {2, 3}
    rows = []
    for j, (a, b) in enumerate(points, 1):
        factors = [a, b]
        for c, d in points[:j - 1]:
            factors.extend((abs(a * d - b * c), a * d + b * c))
        new = set()
        for value in factors:
            assert value > 0
            for p in pool:
                while value % p == 0:
                    new.add(p)
                    value //= p
            assert value == 1
        extra = sorted(new - accumulated)
        assert all(first_bad(p, j) == j for p in extra)
        rows.append(dict(depth=j, absolute_fraction=[a, b], new_bad_primes=extra))
        accumulated.update(new)
    assert accumulated == set(pool)
    return rows


def graph(p, normalized=False):
    """The extra index p denotes infinity."""
    a, b = (-3, -3) if normalized else (-3, -pow(2, -1, p))
    return [p] + [(a * x + b * pow(x, -1, p)) % p for x in range(1, p)] + [p]


def iterated_histograms(edges, depth):
    size = len(edges)
    mass = [1] * size
    answer = []
    for _ in range(depth):
        following = [0] * size
        for x, y in enumerate(edges):
            following[y] += mass[x]
        mass = following
        row = dict(sorted(Counter(mass).items()))
        assert sum(row.values()) == sum(x * n for x, n in row.items()) == size
        answer.append(row)
    return answer


def periodic_count(edges):
    """Iteratively peel off points absent from the current image."""
    indeg = Counter(edges)
    remove = [x for x in range(len(edges)) if indeg[x] == 0]
    for x in remove:
        y = edges[x]
        indeg[y] -= 1
        if indeg[y] == 0:
            remove.append(y)
    return len(edges) - len(remove)


def tree_checks():
    elements = [(0,)]
    law = {1: Fraction(1)}
    rows = []
    for k in range(1, 5):
        width = 2 ** (k - 1)
        previous = elements
        elements = []
        for left, right in product(previous, repeat=2):
            elements.append(left + tuple(z + width for z in right))
            elements.append(tuple(z + width for z in left) + right)
        counts = Counter(sum(a == i for i, a in enumerate(perm)) for perm in elements)
        new = {0: Fraction(1, 2)}
        for a, u in law.items():
            for b, v in law.items():
                new[a + b] = new.get(a + b, Fraction()) + u * v / 2
        law = new
        assert len(set(elements)) == len(elements) == 2 ** (2 ** k - 1)
        assert all(counts[z] == v * len(elements) for z, v in law.items())
        assert sum(z * v for z, v in law.items()) == 1
        assert sum((z - 1) ** 2 * v for z, v in law.items()) == k
        rows.append(dict(depth=k, group_size=len(elements), fixed_leaf_counts=dict(sorted(counts.items())),
                         fraction_with_fixed_leaf=str(1 - law[0])))
    return rows


def exceptional_power():
    rows = {}
    for p in (5, 7):
        f = graph(p)
        if p == 5:
            c = 1
            m = [0 if x == c else p if x == -c % p else
                 (x-c)*pow((x+c) % p, -1, p) % p for x in range(p)] + [1]
            power = lambda z: p if z == 0 else 0 if z == p else pow(z, -2, p)
        else:
            # Field coordinate pair (a,b) for a+b*c, c^2=1/6.
            c2 = pow(6, -1, p)
            def power(z):
                a, b = z
                return ((a*a+c2*b*b) % p, 2*a*b % p)
            m = [(((x*x+c2)*pow((x*x-c2) % p, -1, p)) % p,
                  (-2*x*pow((x*x-c2) % p, -1, p)) % p) for x in range(p)] + [(1, 0)]
            assert all((a*a-c2*b*b) % p == 1 for a,b in m)
        assert len(set(m)) == p+1 and all(m[f[x]] == power(m[x]) for x in range(p+1))
        hist = iterated_histograms(f, 7)
        sizes = [p + 1 - row.get(0, 0) for row in hist]
        expected = ([2 + 4 // gcd(4, 2**k) for k in range(1, 8)] if p == 5
                    else [8 // gcd(8, 2**k) for k in range(1, 8)])
        assert sizes == expected
        rows[p] = dict(image_sizes=sizes, periodic=periodic_count(f))
    return rows


def lattes_37():
    p = 37
    # Both rational Frobenius-sign groups in twist coordinates: y^2=(x^3-6x)/d.
    signs = []
    images = []
    for d in (1, 2):
        assert (pow(d, 18, p) == 1) == (d == 1)
        points = {None} | {(x, y) for x in range(p) for y in range(p)
                           if (d*y*y - x**3 + 6*x) % p == 0}
        def phi(pt):
            if pt is None or pt[0] == 0:
                return None
            x, y = pt
            return (graph(p)[x], 8*(6*x*x-1)*y*pow(x*x, -1, p) % p)
        image = {phi(pt) for pt in points}
        assert image <= points and {phi(pt) for pt in image} == image
        assert {pt for pt in points if phi(pt) is None} == {None, (0, 0)}
        ximage = {p if pt is None else pt[0] for pt in image}
        images.append(ximage)
        signs.append(dict(twist=d, group_order=len(points), image_order=len(image),
                          x_image_size=len(ximage)))
    assert images[0] & images[1] == {p}
    assert images[0] | images[1] == set(graph(p))
    return signs


def main():
    bad = certify_bad()
    tree = tree_checks()
    special = exceptional_power()
    tested = [p for p in range(5, 1000) if prime(p)] + [1009, 10007, 10009, 65537, 100003]
    examples = {}
    for p in tested:
        f = graph(p)
        hist = iterated_histograms(f, 8)
        assert sum(row['depth'] for row in bad if p in row['new_bad_primes']) == (first_bad(p, 5) or 0)
        # Classical one-step Legendre discriminant, with the two preimages 0,infinity above infinity.
        chi6 = 1 if pow(6, (p - 1)//2, p) == 1 else -1
        assert hist[0].get(1, 0) == 1 + chi6
        if p in (5, 7, 13, 37, 1009, 10007, 10009, 65537, 100003):
            examples[p] = dict(legendre6=chi6, first_bad_through_depth8=first_bad(p, 8),
                               image_sizes=[p+1-r.get(0, 0) for r in hist],
                               histogram_depth3=hist[2], periodic_points=periodic_count(f))
    assert iterated_histograms(graph(7, normalized=True), 1)[0] == {0: 3, 1: 2, 2: 3}
    assert iterated_histograms(graph(7), 1)[0] == {0: 4, 2: 4}
    print(json.dumps(dict(projective_prime_count=len(tested), projective_depth=8,
                          primes_tested="all 5<=p<1000 plus 1009,10007,10009,65537,100003",
                          certified_first_failures=bad, tree_permutation_enumeration=tree,
                          exceptional_conjugacies=special, lattes_37=lattes_37(), examples=examples),
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
