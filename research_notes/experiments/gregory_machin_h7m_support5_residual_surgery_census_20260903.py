#!/usr/bin/env python3
"""Blind support-five -> residual-surgery census for Enterprise Math issue #1160.

Declared native search box:
- 2 <= D <= 7,000,000;
- D^2+1 is smooth over odd split primes <= 1300;
- five distinct reciprocal denominators;
- union of free Gaussian split-prime supports has size exactly five;
- free valuation rank is four (minimal five-column circuit);
- round pre-completion Lehmer cutoff mu < 1.70.

Two finite palette classes are exhaustive within their declarations:
A) at least one denominator carries the full five-prime palette;
B) no full-support column is used and the five-prime palette is generated as the
   union of two denominator support sets.

After exact endpoint circuits are found, every ordered denominator pair and every
1 <= k <= 4 is tested for the residual R = U_a U_b^{-k}.  Every positive
2-reciprocal factorization of R is enumerated from divisors of its exact norm;
no relation is seeded.  Only exact endpoint-preserving surgeries are then ranked.

This checker imports the H=7M smooth-norm/signature machinery from the sibling
support-six blind census.  Floating logs are used only after exact native
feasibility, for the declared Lehmer cutoff/ranking.
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_h7m_smooth_support6_census_20260903.py"
spec = importlib.util.spec_from_file_location("gm6", BASE)
gm6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gm6)

HEIGHT = 7_000_000
PRIME_CAP = 1300
MU_BOUND = 1.70


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


def rank4_endpoint_circuit(Ds, signatures):
    """Exact rank-4 minimal circuit in any >=4 free valuation rows."""
    assert len(Ds) == 5
    primes = tuple(
        sorted(set().union(*(set(p for p, _ in signatures[D][1]) for D in Ds)))
    )
    columns = [dict(signatures[D][1]) for D in Ds]
    rows = [[col.get(p, 0) for col in columns] for p in primes]

    primitive = None
    for row_indices in itertools.combinations(range(len(rows)), 4):
        selected = [rows[i] for i in row_indices]
        cofactors = []
        for j in range(5):
            minor = [[row[k] for k in range(5) if k != j] for row in selected]
            value = det_bareiss(minor)
            if j % 2:
                value = -value
            cofactors.append(value)
        if not any(cofactors):
            continue
        if any(value == 0 for value in cofactors):
            return None
        g = 0
        for value in cofactors:
            g = math.gcd(g, abs(value))
        primitive = [value // g for value in cofactors]
        if primitive[0] < 0:
            primitive = [-value for value in primitive]
        if all(sum(row[j] * primitive[j] for j in range(5)) == 0 for row in rows):
            break
        primitive = None

    if primitive is None:
        return None

    torsion = sum(primitive[j] * signatures[D][0] for j, D in enumerate(Ds)) % 8
    if torsion % 2 == 0:
        return None
    scale = min((torsion, torsion - 8), key=abs)
    coeffs = tuple(scale * value for value in primitive)
    assert sum(coeffs[j] * signatures[D][0] for j, D in enumerate(Ds)) % 8 == 1
    return primes, coeffs


def ds_inside_palette(P, groups, max_support):
    out = []
    for r in range(1, max_support + 1):
        for subset in itertools.combinations(P, r):
            out.extend(groups.get(tuple(subset), ()))
    return sorted(set(out))


def combinations_under_cost(ds, k: int, bound: float):
    items = sorted((1.0 / math.log10(D), D) for D in ds)
    n = len(items)
    if n < k:
        return []
    costs = [x[0] for x in items]
    denominators = [x[1] for x in items]
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


def pair_mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def pair_pow(z, k: int):
    out = (1, 0)
    for _ in range(k):
        out = pair_mul(out, z)
    return out


def primitive_pair(z):
    g = math.gcd(abs(z[0]), abs(z[1]))
    z = (z[0] // g, z[1] // g)
    if z[0] < 0 or (z[0] == 0 and z[1] < 0):
        z = (-z[0], -z[1])
    return z, g


def factor_integer_over_allowed(n: int, allowed):
    out = {}
    for p in (2, *allowed):
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        if n == 1:
            break
    assert n == 1
    return out


def residual_norm_factorization(a, b, k, allowed):
    """Factor norm of prim((a+i)(b-i)^k) from smooth input norms exactly."""
    raw = pair_mul((a, 1), pair_pow((b, -1), k))
    (A, B), g = primitive_pair(raw)
    fa = gm6.factor_over_allowed(a, allowed)
    fb = gm6.factor_over_allowed(b, allowed)
    fg = factor_integer_over_allowed(g, allowed)
    exponents = defaultdict(int)
    for p, e in fa.items():
        exponents[p] += e
    for p, e in fb.items():
        exponents[p] += k * e
    for p, e in fg.items():
        exponents[p] -= 2 * e
    assert all(e >= 0 for e in exponents.values())
    N = A * A + B * B
    check = 1
    for p, e in exponents.items():
        check *= p**e
    assert check == N
    return A, B, {p: e for p, e in exponents.items() if e}


def divisors_from_factorization(factors):
    divs = [1]
    for p, e in factors.items():
        old = divs
        powers = [p**j for j in range(e + 1)]
        divs = [d * q for d in old for q in powers]
    return sorted(divs)


def all_positive_two_reciprocal_splits(a, b, k, allowed):
    """Complete positive splits of R=U_a U_b^{-k} into U_m^s U_n^{-s}.

    If prim(R)=(A,sB), B>0, write N=A^2+B^2.  Every positive split is
    determined by a divisor d of N with 0<d<A<N/d and d == A (mod B):
      m=(A-d)/B, n=(N/d-A)/B.
    This is equivalent to (Bm-A)(Bn+A)=-N.
    """
    A, signed_B, factors = residual_norm_factorization(a, b, k, allowed)
    sign = 1 if signed_B > 0 else -1
    B = abs(signed_B)
    if B == 0:
        return []
    N = A * A + B * B
    out = []
    for d in divisors_from_factorization(factors):
        if not (0 < d < A < N // d):
            continue
        if (A - d) % B:
            continue
        m = (A - d) // B
        n = (N // d - A) // B
        if m < 2 or n <= m:
            continue
        # Exact product certificate up to positive scale.
        left = pair_mul((m, sign), (n, -sign))
        assert left[0] * signed_B == left[1] * A
        assert left[0] > 0
        out.append((m, n, d, sign, A, signed_B))
    return out


def apply_surgery(Ds, coeffs, a, b, k, m, n, sign):
    coeff = defaultdict(int, dict(zip(Ds, coeffs)))
    ca = coeff.pop(a)
    coeff[b] += k * ca
    coeff[m] += sign * ca
    coeff[n] -= sign * ca
    result_Ds = tuple(sorted(D for D, c in coeff.items() if c))
    result_coeffs = tuple(coeff[D] for D in result_Ds)
    return result_Ds, result_coeffs


def lehmer(Ds):
    return sum(1.0 / math.log10(D) for D in Ds)


def census():
    smooth, allowed = gm6.smooth_denominators(HEIGHT, PRIME_CAP)
    signatures = {
        D: gm6.signature_from_factorization(D, gm6.factor_over_allowed(D, allowed))
        for D in smooth
    }
    groups = defaultdict(list)
    for D in smooth:
        support = tuple(p for p, _ in signatures[D][1])
        if len(support) <= 5:
            groups[support].append(D)

    # Class A: a full five-prime-support denominator is present.
    full_palettes = [support for support in groups if len(support) == 5]
    full_promising = set()
    for P in full_palettes:
        ds = ds_inside_palette(P, groups, 5)
        if len(ds) < 5:
            continue
        full = set(groups[P])
        for quintuple in combinations_under_cost(ds, 5, MU_BOUND):
            if not any(D in full for D in quintuple):
                continue
            actual = set().union(*(set(p for p, _ in signatures[D][1]) for D in quintuple))
            if actual == set(P):
                full_promising.add(quintuple)

    full_endpoints = []
    for quintuple in full_promising:
        result = rank4_endpoint_circuit(quintuple, signatures)
        if result is not None and len(result[0]) == 5:
            full_endpoints.append((lehmer(quintuple), quintuple, result[1], result[0]))
    full_endpoints.sort()

    # Class B: palette generated by two <=4-support denominator support sets.
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
        if len(ds) < 5:
            continue
        set_p = set(P)
        for quintuple in combinations_under_cost(ds, 5, MU_BOUND):
            actual = set().union(*(set(p for p, _ in signatures[D][1]) for D in quintuple))
            if actual == set_p:
                pair_promising.add(quintuple)

    pair_endpoints = []
    for quintuple in pair_promising:
        result = rank4_endpoint_circuit(quintuple, signatures)
        if result is not None and len(result[0]) == 5:
            pair_endpoints.append((lehmer(quintuple), quintuple, result[1], result[0]))
    pair_endpoints.sort()

    endpoints = sorted(full_endpoints + pair_endpoints)

    improvements = []
    for base_mu, Ds, coeffs, primes in endpoints:
        for a, b in itertools.permutations(Ds, 2):
            for k in range(1, 5):
                for m, n, d, sign, A, signed_B in all_positive_two_reciprocal_splits(
                    a, b, k, allowed
                ):
                    if {m, n} == {a, b}:
                        continue
                    new_Ds, new_coeffs = apply_surgery(Ds, coeffs, a, b, k, m, n, sign)
                    new_mu = lehmer(new_Ds)
                    if new_mu < base_mu:
                        endpoint, sheet, crossings = gm6.tangent_sheet_certificate(new_Ds, new_coeffs)
                        assert endpoint == (1, 1) and sheet == 0
                        improvements.append(
                            (
                                new_mu,
                                base_mu - new_mu,
                                Ds,
                                coeffs,
                                a,
                                b,
                                k,
                                d,
                                (A, signed_B),
                                new_Ds,
                                new_coeffs,
                                crossings,
                            )
                        )
    improvements.sort()

    return {
        "smooth": len(smooth),
        "full_palettes": len(full_palettes),
        "full_promising": len(full_promising),
        "full_endpoints": full_endpoints,
        "pair_palettes": len(pair_palettes),
        "pair_promising": len(pair_promising),
        "pair_endpoints": pair_endpoints,
        "endpoints": endpoints,
        "improvements": improvements,
    }


def main():
    result = census()
    print(f"smooth_denominators={result['smooth']}")
    print(f"full_palettes={result['full_palettes']}")
    print(f"full_promising={result['full_promising']}")
    print(f"full_endpoint_count={len(result['full_endpoints'])}")
    print(f"pair_palettes={result['pair_palettes']}")
    print(f"pair_promising={result['pair_promising']}")
    print(f"pair_endpoint_count={len(result['pair_endpoints'])}")
    print("five-term endpoints below mu=1.70:")
    for row in result["endpoints"]:
        print(f"  mu={row[0]:.15f} D={row[1]} c={row[2]} primes={row[3]}")
    print("strictly improving complete residual surgeries (1<=k<=4):")
    for row in result["improvements"]:
        print(
            f"  mu={row[0]:.15f} gain={row[1]:.15f} base={row[2]} "
            f"pair=({row[4]},{row[5]}) k={row[6]} d={row[7]} residual={row[8]} "
            f"D={row[9]} c={row[10]} crossings={row[11]}"
        )

    # Frozen blind-search regression certificate.
    assert result["smooth"] == 17741
    assert result["full_palettes"] == 6364
    assert result["full_promising"] == 5773
    assert len(result["full_endpoints"]) == 2
    assert result["pair_palettes"] == 311403
    assert result["pair_promising"] == 62743
    assert len(result["pair_endpoints"]) == 3
    assert len(result["endpoints"]) == 5

    expected_endpoints = [
        ((114, 239, 682, 12943, 740943), (88, 7, -12, 24, -44)),
        ((114, 239, 268, 247057, 740943), (76, 7, 24, -12, -32)),
        ((57, 239, 757, 110443, 5055058), (44, 7, -12, 12, 12)),
        ((53, 107, 4443, 110443, 4841182), (34, 15, 17, -5, 5)),
        ((68, 117, 1252, 110443, 4841182), (34, 32, 15, -5, 5)),
    ]
    assert [(row[1], row[2]) for row in result["endpoints"]] == expected_endpoints

    assert len(result["improvements"]) == 3
    best = result["improvements"][0]
    assert best[2] == (53, 107, 4443, 110443, 4841182)
    assert best[4:8] == (53, 107, 2, 1)
    assert best[8] == (303479, 53)
    assert best[9] == (107, 4443, 5726, 110443, 4841182, 1737720807)
    assert best[10] == (83, 17, 34, -5, 5, -34)
    assert abs(best[0] - 1.4891213592834787) < 1e-14

    # The complete residual norm split has exactly these three improving divisors.
    assert [row[7] for row in result["improvements"]] == [1, 2810, 5725]
    print("H=7M support-five -> complete residual-surgery regression certificate: PASS")


if __name__ == "__main__":
    main()
