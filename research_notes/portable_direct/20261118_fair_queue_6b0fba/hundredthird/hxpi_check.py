"""Count the four named ports of the original strict hexagon. Python 3.9+."""
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
import json
from math import gcd, lcm, prod
from pathlib import Path
import runpy


SOURCE_BLOB = "026b13094e8cf8d5656d45cd7b69e0d1ff9cf895"


def factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        result.append(n)
    return result


def prime_support(t):
    return sorted(set(factors(2**t - 1) + factors(2**t + 1)))


def residue_count(a, modulus, residue):
    return (2*a-residue)//modulus - (a-residue)//modulus


def crt_events(a, primes, shifts):
    # Inclusion-exclusion. The nonempty local alternatives are disjoint.
    terms = [(1, 0, 1)]
    for p in primes:
        next_terms = terms.copy()
        for modulus, residue, sign in terms:
            inv = pow(modulus, -1, p)
            for shift in shifts:
                correction = (shift - residue) * inv % p
                next_terms.append((modulus*p, residue + modulus*correction, -sign))
        terms = next_terms
    total = odd = 0
    for modulus, residue, sign in terms:
        total += sign * residue_count(a, modulus, residue)
        odd_residue = residue if residue % 2 else residue + modulus
        odd += sign * residue_count(a, 2*modulus, odd_residue)
    return total - odd, odd


def arithmetic_table(t):
    m = 4**t
    a = (m-1)//3
    primes = prime_support(t)
    count = {}
    for left, right in product(range(2), repeat=2):
        shifts = ([0] if left else []) + ([1] if right else [])
        count[left, right] = crt_events(a, primes, shifts)
    hist = {}
    for outer, left, right in product(range(2), repeat=3):
        value = sum((-1)**(i-left+j-right) * count[i, j][outer]
                    for i in range(left, 2) for j in range(right, 2))
        hist[f"{outer}{left}{right}"] = 3*value
    assert sum(hist.values()) == m-1 and min(hist.values()) >= 0
    assert all(hist[f"{o}10"] == hist[f"{o}01"] for o in range(2))
    if t % 3 == 0:
        for idx, size in ((1, sum(count[1, 0])), (2, sum(count[1, 1]))):
            assert Fraction(size, a) == prod(Fraction(p-idx, p) for p in primes)
    return {"t": t, "m": m, "primes": primes, "histogram": hist,
            "two_inner_model": str(prod(Fraction(p-2, p) for p in primes)),
            "correlation_model": str(prod(Fraction(p*(p-2), (p-1)**2) for p in primes))}


def shell(s):
    for q in range(-s, s+1):
        low = max(-s-2*q, -((s+q)//2), q-s)
        high = min(s-2*q, (s-q)//2, q+s)
        if low <= high:
            for r in sorted({low, high}):
                if max(abs(2*q+r), abs(q+2*r), abs(q-r)) == s:
                    yield q, r


def old_id(point, t):
    q, r = point
    value = 0
    for i in range(2*t):
        u, v = q & 1, r & 1
        value |= (u+2*v) << (2*i)
        q, r = (q-u)//2, (r-v)//2
        q, r = q+r, -q
    return value


def turn(point):
    q, r = point
    return -r, q+r


def direct(t, source):
    m = 4**t
    a = (m-1)//3
    K = m*m-m+1

    def ell(point):
        return (point[0] + m*point[1]) % K

    outer = defaultdict(list)
    for point in shell(m):
        outer[old_id(point, t)].append(point)
    assert len(outer) == m-1 and all(len(ports) == 2 for ports in outer.values())
    inner = {ell(point): point for point in shell(m-1)}
    assert len(inner) == 2*(m-1)
    if source is not None:
        source_ports = source["excluded"](2*t)
        assert {i: sorted(map(tuple, p)) for i, p in source_ports.items()} == {
            i: sorted(p) for i, p in outer.items()}
    hist = {f"{i}{j}{k}": 0 for i, j, k in product(range(2), repeat=3)}
    seen = {}
    for q in range(a+1, 2*a+1):
        r = m-2*q
        points = [(q-m, r), (q, r), (q, r-1), (q-m, r+1)]
        for _ in range(3):
            out_l, out_r, in_l, in_r = points
            tag = old_id(out_l, t)
            assert tag not in seen and set(outer[tag]) == {out_l, out_r}
            assert inner[ell(out_l)] == in_l and inner[ell(out_r)] == in_r
            entries = [gcd(*point) for point in points]
            assert entries == [gcd(q, m), gcd(q, m), gcd(q, m-1), gcd(q-1, m-1)]
            seen[tag] = entries
            key = ''.join(str(int(entries[i] == 1)) for i in (0, 2, 3))
            hist[key] += 1
            points = [turn(p) for p in points]
    assert seen.keys() == outer.keys()
    digest = sha256(json.dumps(sorted(seen.items()), separators=(',', ':')).encode()).hexdigest()
    return {"t": t, "old_ids": len(seen), "named_gcd_rows_sha256": digest, "histogram": hist}


def order_4(p):
    d, value = 1, 4 % p
    while value != 1:
        d += 1
        value = 4*value % p
    return d


def distribution_example(Y):
    ps = [p for p in range(3, Y+1, 2) if factors(p) == [p]]
    orders = [(p, order_4(p)) for p in ps]
    period = lcm(*(d for _, d in orders))
    values = defaultdict(int)
    for t in range(1, period+1):
        values[prod(Fraction(p-2, p) for p, d in orders if t % d == 0)] += 1
    return {"Y": Y, "prime_orders": orders, "period": period,
            "two_inner_model_by_period": {str(v): n for v, n in sorted(values.items())}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="optional frozen strict expansion verify.py")
    arg = parser.parse_args()
    original = None
    if arg.source:
        data = arg.source.read_bytes()
        assert sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest() == SOURCE_BLOB
        original = runpy.run_path(str(arg.source))
    tables = [arithmetic_table(t) for t in range(1, 37)]
    replay = [direct(t, original) for t in range(1, 9)]
    assert all(row["histogram"] == tables[row["t"]-1]["histogram"] for row in replay)
    print(json.dumps({"source_verify_git_blob": SOURCE_BLOB,
                      "histogram_bits": ["outer_pair", "inner_gcd_q", "inner_gcd_q_minus_1"],
                      "asymptotic_invariant": "liminf-four=0, limsup-four=1/6; inner ratio from C2 to 3/4",
                      "direct_geometry": replay, "exact_CRT": tables,
                      "truncated_scale_law": [distribution_example(y) for y in (7, 13, 23)]},
                     indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
