"""Root-level Kloosterman-fraction parametrization of orientation-Walsh Fourier sums.

This is distinct from the state-factorization inverse-residue interface in
p017_p018_walsh_bilinear_inverse.  Here the inverse residue appears inside one
squarefree conductor q.

For q supported on transverse odd primes, scale a Walsh root r by M^{-1} mod q:

    u = r M^{-1} (mod q),       u^2 = 1 (mod q).

Choose the negative-orientation prime product b and the positive product a,
so q=ab and (a,b)=1.  The corresponding root satisfies

    u=+1 (mod a),  u=-1 (mod b),

hence

    u = 1 - 2 a inv(a,b) (mod q).

The Walsh sign of this root is mu(b).  Therefore the unnormalized root Fourier
sum has the exact divisor/Kloosterman form

    S_q(h)
      = e(hM/q) * sum_(ab=q) mu(b) e(-2hM inv(a,b)/b).

For even omega(q), mu(a)=mu(b).  Additive reciprocity

    inv(a,b)/b + inv(b,a)/a = 1/(ab)  (mod 1)

pairs the ordered splits (a,b),(b,a) into a real cosine:

    S_q(h)
      = 2 sum_{unordered {a,b},ab=q} mu(b)
          cos(2*pi*(2hM inv(a,b)/b - hM/q)).

Thus every reusable even-conductor Fourier quantum is a reciprocity-paired real
Kloosterman-fraction sum on the product hyperbola ab=q<=C_k.  This gives a much
smaller-scale analytic interface than the physical-state thin strip |mn-M|<k:
the modulus product here is only q=O(k).

The identity is exact.  No Kloosterman-fraction estimate or Legendre theorem is
claimed.
"""

from __future__ import annotations

from cmath import exp, pi
from itertools import combinations
from math import cos, prod

from .p017_p018_orientation_walsh_fourier import signed_root_fourier


def _mu_squarefree(value: int) -> int:
    if value < 1 or value % 2 == 0:
        raise ValueError("value must be a positive odd squarefree integer")
    remaining = value
    omega = 0
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            omega += 1
            if remaining % p == 0:
                raise ValueError("value must be squarefree")
        p += 2
    if remaining > 1:
        omega += 1
    return -1 if omega % 2 else 1


def signed_unity_root_from_split(a: int, b: int) -> dict[str, int]:
    """Return u mod q with u=1 mod a and u=-1 mod b."""
    if a < 1 or b < 1 or a % 2 == 0 or b % 2 == 0:
        raise ValueError("a,b must be positive odd integers")
    from math import gcd

    if gcd(a, b) != 1:
        raise ValueError("a,b must be coprime")
    q = a * b
    inverse = 0 if b == 1 else pow(a, -1, b)
    raw = 1 if b == 1 else 1 - 2 * a * inverse
    u = raw % q
    if u % a != 1 % a or u % b != (-1) % b:
        raise AssertionError("CRT signed-unity root reconstruction failed")
    return {"a": a, "b": b, "q": q, "inverse_a_mod_b": inverse, "root_u": u}


def root_fourier_kloosterman_split(k: int, selected_primes: tuple[int, ...], frequency: int) -> dict[str, object]:
    """Verify the divisor/Kloosterman formula against the existing root Fourier oracle."""
    normalized = tuple(sorted(int(p) for p in selected_primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("selected_primes must be nonempty and distinct")
    M = k * (k + 1)
    q = prod(normalized)

    rows: list[dict[str, object]] = []
    split_sum = 0j
    n = len(normalized)
    for size in range(n + 1):
        for negative_subset in combinations(normalized, size):
            negative = set(negative_subset)
            b = prod(negative_subset, start=1)
            a = q // b
            root = signed_unity_root_from_split(a, b)
            mu_b = -1 if size % 2 else 1
            inverse = int(root["inverse_a_mod_b"])
            if b == 1:
                fraction_phase = 1 + 0j
            else:
                fraction_phase = exp(-4j * pi * frequency * M * inverse / b)
            term = mu_b * exp(2j * pi * frequency * M / q) * fraction_phase
            direct_root_term = mu_b * exp(
                2j * pi * frequency * M * int(root["root_u"]) / q
            )
            if abs(term - direct_root_term) > 1e-8:
                raise AssertionError("split Kloosterman phase disagreed with CRT root phase")
            split_sum += term
            rows.append(
                {
                    "positive_product_a": a,
                    "negative_product_b": b,
                    "mu_b": mu_b,
                    "root_u": int(root["root_u"]),
                    "inverse_a_mod_b": inverse,
                    "term": term,
                }
            )

    existing = signed_root_fourier(k, normalized, frequency)
    oracle = complex(existing["direct_fourier_sum"])
    if abs(split_sum - oracle) > 1e-7 * max(1.0, abs(oracle)):
        raise AssertionError("root-level Kloosterman divisor sum disagreed with Walsh Fourier oracle")
    return {
        "k": k,
        "selected_primes": normalized,
        "conductor": q,
        "frequency": frequency,
        "kloosterman_split_sum": split_sum,
        "existing_root_fourier_sum": oracle,
        "root_kloosterman_identity": True,
        "split_rows": tuple(rows),
    }


def even_conductor_reciprocity_cosine(k: int, selected_primes: tuple[int, ...], frequency: int) -> dict[str, object]:
    """Pair a<->b by additive reciprocity when omega(q) is positive even."""
    normalized = tuple(sorted(int(p) for p in selected_primes))
    if len(normalized) < 2 or len(normalized) % 2:
        raise ValueError("selected_primes must have positive even cardinality")
    M = k * (k + 1)
    q = prod(normalized)
    seen: set[tuple[int, int]] = set()
    cosine_sum = 0.0
    rows: list[dict[str, object]] = []

    n = len(normalized)
    for size in range(n + 1):
        for negative_subset in combinations(normalized, size):
            b = prod(negative_subset, start=1)
            a = q // b
            key = tuple(sorted((a, b)))
            if key in seen:
                continue
            seen.add(key)
            if a == b:
                raise AssertionError("nontrivial squarefree conductor produced a=b")

            # Choose the displayed orientation with b>1 when possible; the cosine is symmetric.
            if b == 1:
                a, b = b, a
            inverse = 0 if b == 1 else pow(a, -1, b)
            mu_b = _mu_squarefree(b)
            angle_cycles = (
                (2 * frequency * M * inverse / b if b > 1 else 0.0)
                - frequency * M / q
            )
            pair_value = 2.0 * mu_b * cos(2 * pi * angle_cycles)
            cosine_sum += pair_value
            rows.append(
                {
                    "a": a,
                    "b": b,
                    "mu_b": mu_b,
                    "inverse_a_mod_b": inverse,
                    "pair_cosine_value": pair_value,
                }
            )

    direct = root_fourier_kloosterman_split(k, normalized, frequency)
    oracle = complex(direct["kloosterman_split_sum"])
    if abs(oracle.imag) > 1e-7 * max(1.0, abs(oracle)):
        raise AssertionError("even-conductor Walsh Fourier sum is not real")
    if abs(cosine_sum - oracle.real) > 1e-7 * max(1.0, abs(oracle.real)):
        raise AssertionError("reciprocity cosine pairing disagreed with exact root Fourier sum")

    return {
        "k": k,
        "selected_primes": normalized,
        "conductor": q,
        "frequency": frequency,
        "reciprocity_cosine_sum": cosine_sum,
        "exact_root_fourier_sum": oracle,
        "even_conductor_real_fourier": True,
        "additive_reciprocity_pairing": True,
        "rows": tuple(rows),
    }
