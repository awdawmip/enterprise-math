#!/usr/bin/env python3
"""Blind bounded smooth-norm support-six census for Enterprise Math issue #1160.

Search box (declared before endpoint recognition):
- 2 <= D <= 7,000,000;
- every odd split prime dividing D^2+1 is <= 1300;
- six distinct reciprocal denominators;
- union of free Gaussian split-prime coordinates has size exactly five;
- Lehmer measure is below the already-established support-four Størmer benchmark;
- palette is either represented by a full-support column, or is the union of two
  denominator supports.  These two palette classes are searched exhaustively.

No Hwang denominator, coefficient, five-prime palette, numerical value of pi, or
floating arctangent recognition is used in candidate generation or endpoint tests.
Floating logarithms are used only for the post-native Lehmer threshold/ranking.

The exact endpoint certificate is the C8 + oriented Gaussian-prime valuation
criterion from the #1160 predecessor theorem.  A final tangent-sheet check gives
an exact finite winding/lift certificate without introducing real arctangent.
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from array import array
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_gaussian_triple_census_20260903.py"
spec = importlib.util.spec_from_file_location("gm3", BASE)
gm3 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gm3)

HEIGHT = 7_000_000
PRIME_CAP = 1300
STORMER_DENOMINATORS = (57, 239, 682, 12943)
STORMER_BOUND = sum(1.0 / math.log10(D) for D in STORMER_DENOMINATORS)


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def sqrt_minus_one_mod_prime(p: int) -> int:
    assert p % 4 == 1
    a = 2
    while pow(a, (p - 1) // 2, p) != p - 1:
        a += 1
    r = pow(a, (p - 1) // 4, p)
    assert (r * r + 1) % p == 0
    return r


def smooth_denominators(height: int, prime_cap: int):
    """Return all D whose D^2+1 has no odd prime factor above prime_cap.

    For p == 1 mod 4 the roots of X^2+1 mod p are +/-r.  Dividing along those
    two arithmetic progressions is a deterministic exact norm-support sieve;
    no integer factorization oracle is used on the 7M raw denominator universe.
    """
    vals = array("Q", (D * D + 1 for D in range(height + 1)))

    # v_2(D^2+1) is exactly one for odd D and zero for even D.
    for D in range(1, height + 1, 2):
        vals[D] //= 2

    allowed = [p for p in primes_upto(prime_cap) if p % 4 == 1]
    for p in allowed:
        r = sqrt_minus_one_mod_prime(p)
        for rr in (r, (-r) % p):
            start = rr
            if start < 2:
                start += ((2 - start + p - 1) // p) * p
            for D in range(start, height + 1, p):
                value = vals[D]
                while value % p == 0:
                    value //= p
                vals[D] = value

    candidates = [D for D in range(2, height + 1) if vals[D] == 1]
    return candidates, allowed


def factor_over_allowed(D: int, allowed: list[int]) -> dict[int, int]:
    n = D * D + 1
    out: dict[int, int] = {}
    if n % 2 == 0:
        e = 0
        while n % 2 == 0:
            n //= 2
            e += 1
        out[2] = e
    for p in allowed:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        if n == 1:
            break
    assert n == 1, (D, n)
    return out


def signature_from_factorization(D: int, factorization: dict[int, int]):
    """Exact (epsilon mod 8, oriented split-prime valuation vector)."""
    z = (D, 1)
    coords: dict[int, int] = {}

    for p, e in factorization.items():
        if p == 2:
            continue
        assert p % 4 == 1
        pi = gm3.sum_two_squares_prime(p)
        pib = (pi[0], -pi[1])
        vp = vb = 0
        while True:
            q = gm3.gaussian_div_exact(z, pi)
            if q is None:
                break
            z = q
            vp += 1
        while True:
            q = gm3.gaussian_div_exact(z, pib)
            if q is None:
                break
            z = q
            vb += 1
        assert vp + vb == e, (D, p, e, pi, vp, vb, z)
        coords[p] = vp - vb

    ramified = 0
    while True:
        q = gm3.gaussian_div_exact(z, (1, 1))
        if q is None:
            break
        z = q
        ramified += 1

    unit_exp = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3,
    }.get(z)
    assert unit_exp is not None, (D, z)
    epsilon = (ramified + 2 * unit_exp) % 8
    return epsilon, tuple(sorted((p, v) for p, v in coords.items() if v))


def det_bareiss(A: list[list[int]]) -> int:
    n = len(A)
    if n == 0:
        return 1
    M = [row[:] for row in A]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if M[r][k] != 0), None)
            if swap is None:
                return 0
            M[k], M[swap] = M[swap], M[k]
            sign = -sign
        pivot = M[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * pivot - M[i][k] * M[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            M[i][k] = 0
    return sign * M[n - 1][n - 1]


def primitive_endpoint_circuit(Ds, primes, signatures):
    """Return least-absolute C8-target scaling of a rank-(s-1) circuit."""
    s = len(Ds)
    assert len(primes) + 1 == s
    columns = [dict(signatures[D][1]) for D in Ds]
    rows = [[col.get(p, 0) for col in columns] for p in primes]

    cofactors = []
    for j in range(s):
        minor = [[row[k] for k in range(s) if k != j] for row in rows]
        value = det_bareiss(minor)
        if j % 2:
            value = -value
        if value == 0:
            return None
        cofactors.append(value)

    g = 0
    for value in cofactors:
        g = math.gcd(g, abs(value))
    c0 = [value // g for value in cofactors]
    if c0[0] < 0:
        c0 = [-value for value in c0]

    for row in rows:
        assert sum(a * b for a, b in zip(row, c0)) == 0

    torsion = sum(c0[j] * signatures[D][0] for j, D in enumerate(Ds)) % 8
    if torsion % 2 == 0:
        return None

    # Every odd residue is its own inverse modulo 8.
    scale = min((torsion, torsion - 8), key=abs)
    coeffs = tuple(scale * value for value in c0)
    assert sum(coeffs[j] * signatures[D][0] for j, D in enumerate(Ds)) % 8 == 1
    return coeffs


def ds_inside_palette(P, groups, max_support):
    out = []
    for r in range(1, max_support + 1):
        for subset in itertools.combinations(P, r):
            out.extend(groups.get(tuple(subset), ()))
    return sorted(set(out))


def combinations_under_cost(ds, k: int, bound: float):
    """Enumerate exactly the k-subsets with Lehmer denominator cost < bound."""
    items = sorted((1.0 / math.log10(D), D) for D in ds)
    costs = [item[0] for item in items]
    denominators = [item[1] for item in items]
    n = len(items)

    prefix = [0.0]
    for cost in costs:
        prefix.append(prefix[-1] + cost)

    out = []

    def rec(start: int, need: int, total: float, chosen: list[int]):
        if need == 0:
            out.append(tuple(sorted(chosen)))
            return
        if n - start < need:
            return
        if total + (prefix[start + need] - prefix[start]) >= bound:
            return

        for i in range(start, n - need + 1):
            next_total = total + costs[i]
            if need == 1:
                if next_total >= bound:
                    break
            else:
                min_tail = prefix[i + need] - prefix[i + 1]
                if next_total + min_tail >= bound:
                    break
            rec(i + 1, need - 1, next_total, chosen + [denominators[i]])

    rec(0, k, 0.0, [])
    return out


def tangent_sheet_certificate(Ds, coeffs):
    """Finite unwrapped tangent-chart lift, with no arctangent input.

    Each U_D^{+/-} changes direction by less than a quarter-turn because D>=2.
    A signed crossing of the vertical axis therefore changes the tangent sheet by
    exactly +/-1.  The state itself is kept as a primitive integer direction pair.
    """
    z = (1, 0)
    sheet = 0
    crossings = 0

    for D, coefficient in zip(Ds, coeffs):
        sign = 1 if coefficient > 0 else -1
        factor = (D, sign)
        for _ in range(abs(coefficient)):
            old = z
            a, b = old
            c, d = factor
            new = (a * c - b * d, a * d + b * c)
            g = math.gcd(abs(new[0]), abs(new[1]))
            new = (new[0] // g, new[1] // g)

            assert old[0] != 0 and new[0] != 0, (D, old, new)
            if (old[0] > 0) != (new[0] > 0):
                sheet += sign
                crossings += 1
            z = new

    return z, sheet, crossings


def census(height: int = HEIGHT, prime_cap: int = PRIME_CAP):
    smooth, allowed = smooth_denominators(height, prime_cap)
    signatures = {
        D: signature_from_factorization(D, factor_over_allowed(D, allowed)) for D in smooth
    }

    support_distribution = Counter(len(signatures[D][1]) for D in smooth)
    groups = defaultdict(list)
    for D in smooth:
        support = tuple(p for p, _ in signatures[D][1])
        if len(support) <= 5:
            groups[support].append(D)

    # Class A: one denominator already carries the full five-prime palette.
    full_palettes = [support for support in groups if len(support) == 5]
    full_promising = set()
    for P in full_palettes:
        ds = ds_inside_palette(P, groups, 5)
        if len(ds) < 6:
            continue
        full = set(groups[P])
        for sextuple in combinations_under_cost(ds, 6, STORMER_BOUND):
            if any(D in full for D in sextuple):
                full_promising.add(sextuple)

    full_endpoints = []
    for sextuple in full_promising:
        P = tuple(
            sorted(set().union(*(set(p for p, _ in signatures[D][1]) for D in sextuple)))
        )
        if len(P) != 5:
            continue
        coeffs = primitive_endpoint_circuit(sextuple, P, signatures)
        if coeffs is not None:
            full_endpoints.append((sextuple, coeffs, P))

    # Class B: no full-support column, but two denominator supports generate the
    # entire five-prime palette.  This includes the Hwang circuit without seeding it.
    support_keys = [support for support in groups if len(support) <= 4]
    pair_palettes = set()
    for i, A in enumerate(support_keys):
        set_a = set(A)
        for B in support_keys[i + 1 :]:
            if len(A) + len(B) < 5:
                continue
            union = set_a | set(B)
            if len(union) == 5:
                pair_palettes.add(tuple(sorted(union)))

    pair_promising = set()
    for P in pair_palettes:
        ds = ds_inside_palette(P, groups, 4)
        if len(ds) < 6:
            continue
        set_p = set(P)
        for sextuple in combinations_under_cost(ds, 6, STORMER_BOUND):
            actual = set().union(*(set(p for p, _ in signatures[D][1]) for D in sextuple))
            if actual == set_p:
                pair_promising.add(sextuple)

    pair_endpoints = []
    for sextuple in pair_promising:
        P = tuple(
            sorted(set().union(*(set(p for p, _ in signatures[D][1]) for D in sextuple)))
        )
        coeffs = primitive_endpoint_circuit(sextuple, P, signatures)
        if coeffs is None:
            continue
        mu = sum(1.0 / math.log10(D) for D in sextuple)
        pair_endpoints.append((mu, sextuple, coeffs, P))
    pair_endpoints.sort()

    return {
        "allowed_split_primes": len(allowed),
        "smooth_denominators": len(smooth),
        "support_distribution": dict(sorted(support_distribution.items())),
        "full_palettes": len(full_palettes),
        "full_promising": len(full_promising),
        "full_endpoints": full_endpoints,
        "pair_palettes": len(pair_palettes),
        "pair_promising": len(pair_promising),
        "pair_endpoints": pair_endpoints,
    }


def main() -> None:
    result = census()
    for key in (
        "allowed_split_primes",
        "smooth_denominators",
        "support_distribution",
        "full_palettes",
        "full_promising",
        "pair_palettes",
        "pair_promising",
    ):
        print(f"{key}={result[key]}")
    print(f"full_endpoint_count={len(result['full_endpoints'])}")
    print(f"pair_endpoint_count={len(result['pair_endpoints'])}")
    for mu, Ds, coeffs, primes in result["pair_endpoints"]:
        print(
            f"endpoint mu={mu:.15f} D={Ds} c={coeffs} primes={primes} L1={sum(abs(c) for c in coeffs)}"
        )

    # Frozen blind-search regression certificate.
    assert result["allowed_split_primes"] == 104
    assert result["smooth_denominators"] == 17741
    assert result["support_distribution"] == {
        1: 25,
        2: 187,
        3: 855,
        4: 2817,
        5: 6368,
        6: 6120,
        7: 1331,
        8: 38,
    }
    assert result["full_promising"] == 18
    assert len(result["full_endpoints"]) == 0
    assert result["pair_palettes"] == 311403
    assert result["pair_promising"] == 21
    assert len(result["pair_endpoints"]) == 1

    mu, Ds, coeffs, primes = result["pair_endpoints"][0]
    assert Ds == (239, 1023, 5832, 110443, 4841182, 6826318)
    assert coeffs == (183, 32, -68, 12, -12, -100)
    assert primes == (5, 13, 229, 457, 1201)
    assert abs(mu - 1.512439470049298) < 1e-14

    endpoint, sheet, crossings = tangent_sheet_certificate(Ds, coeffs)
    assert endpoint == (1, 1)
    assert sheet == 0
    assert crossings == 0
    print("H=7,000,000 / split-prime<=1300 blind support-six certificate: PASS")


if __name__ == "__main__":
    main()
