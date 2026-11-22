"""Fixed combined-product geometry for P017 high-product mirror tokens.

Let ``M=k(k+1)`` and let ``S`` be an odd squarefree product of transverse
primes.  A terminal mirror token with combined product ``S`` chooses one prime
``p|S`` for the partner side and puts the complementary product ``A=S/p`` on
the residual side:

    A | M-x,
    p | M+x.

For every choice of p, CRT plus mandatory odd parity gives one exact signed
residue class modulo ``2S``.  In the high-product regime ``S>=k`` the signed
window ``0<|x|<k`` has diameter smaller than ``2S``, so each split has at most
one bounded signed realization.

If two different split primes p,q are both realized at signed points x_p,x_q,
then all primes in S/(pq) divide both residual-side labels.  Hence

    2*S/(p*q) | x_p-x_q.

The two points cannot coincide, and ``|x_p-x_q|<2k``.  Therefore

    k*p*q > S.

So the realized split-prime set is a clique in the threshold graph
``p~q iff k*p*q>S``.  Because the condition is monotone in p and q, the largest
possible clique is obtained from the largest prime factors of S; its size is an
explicit finite upper bound on same-S split reuse.  The bound is sharp:
``k=61,S=105`` realizes all three splits p=3,5,7.

This is a P017 owner-local capacity theorem.  It does not claim Legendre and it
uses no primality randomness or analytic sieve input.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import is_prime


def _factor_squarefree(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 3 or value % 2 == 0:
        raise ValueError("S must be an odd integer >=3")
    remaining = value
    factors: list[int] = []
    candidate = 3
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            factors.append(candidate)
            remaining //= candidate
            if remaining % candidate == 0:
                raise ValueError("S must be squarefree")
        candidate += 2
    if remaining > 1:
        factors.append(remaining)
    if not factors or any(not is_prime(p) for p in factors) or prod(factors) != value:
        raise ValueError("S must be a squarefree product of odd primes")
    return tuple(factors)


def _validated_high_product(k: int, product_value: int) -> tuple[int, tuple[int, ...]]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    factors = _factor_squarefree(product_value)
    center = k * (k + 1)
    if gcd(product_value, center) != 1:
        raise ValueError("S must be transverse to M=k(k+1)")
    if product_value < k:
        raise ValueError("high-product split geometry requires S>=k")
    return center, factors


def split_signed_residue(k: int, product_value: int, partner_prime: int) -> dict[str, int]:
    """Return the unique signed split residue modulo 2S for one p|S.

    The canonical class satisfies A|M-x, p|M+x, and x odd, where A=S/p.
    ``centered_residue`` is the unique representative in ``(-S,S)``.
    """
    center, factors = _validated_high_product(k, product_value)
    if partner_prime not in factors:
        raise ValueError("partner_prime must divide S")
    p = partner_prime
    residual_product = product_value // p

    # x=M+A*t and A*t=-2M (mod p).
    step = ((-2 * center) * pow(residual_product, -1, p)) % p
    residue_mod_s = (center + residual_product * step) % product_value
    odd_residue = (
        residue_mod_s
        if residue_mod_s % 2 == 1
        else residue_mod_s + product_value
    )
    modulus = 2 * product_value
    if not (0 <= odd_residue < modulus and odd_residue % 2 == 1):
        raise AssertionError("split residue failed parity normalization")
    centered = odd_residue if odd_residue < product_value else odd_residue - modulus
    if centered == 0 or not (-product_value < centered < product_value):
        raise AssertionError("split residue failed centered normalization")
    if (center - centered) % residual_product or (center + centered) % p:
        raise AssertionError("centered split residue lost one side divisibility")

    return {
        "k": k,
        "center": center,
        "combined_product": product_value,
        "partner_prime": p,
        "residual_product": residual_product,
        "residue_mod_2S": odd_residue,
        "centered_residue": centered,
        "modulus": modulus,
    }


def split_spacing_clique_capacity(k: int, product_value: int) -> dict[str, object]:
    """Return the exact threshold-clique upper bound on realized split count."""
    _center, factors = _validated_high_product(k, product_value)
    n = len(factors)
    capacity = 1
    for size in range(2, n + 1):
        chosen = factors[n - size :]
        if k * chosen[0] * chosen[1] > product_value:
            capacity = size
    return {
        "k": k,
        "combined_product": product_value,
        "prime_factors": factors,
        "factor_count": n,
        "split_spacing_clique_capacity": capacity,
    }


def fixed_product_split_capacity(k: int, product_value: int) -> dict[str, object]:
    """Evaluate exact bounded split residues and the pair-spacing capacity.

    ``aligned_split_points`` includes only splits whose unique mod-2S residue
    lies in ``0<|x|<k``.  ``anchor_split_points`` additionally imposes
    ``gcd(|x|,M)=1``.  Every actual terminal high-product token with combined
    product S must lie in the latter set.
    """
    center, factors = _validated_high_product(k, product_value)
    aligned: list[tuple[int, int]] = []
    anchor: list[tuple[int, int]] = []
    residues: dict[int, int] = {}

    for p in factors:
        data = split_signed_residue(k, product_value, p)
        point = int(data["centered_residue"])
        residues[p] = point
        if abs(point) < k:
            aligned.append((p, point))
            if gcd(abs(point), center) == 1:
                anchor.append((p, point))

    for index, (p, x) in enumerate(anchor):
        for q, y in anchor[index + 1 :]:
            if x == y:
                raise AssertionError("two distinct split primes realized the same signed point")
            shared = product_value // (p * q)
            if (x - y) % (2 * shared):
                raise AssertionError("same-S split spacing lost the shared complementary core")
            if not k * p * q > product_value:
                raise AssertionError("two realized splits violated the high-product pair threshold")

    clique = split_spacing_clique_capacity(k, product_value)
    if len(anchor) > int(clique["split_spacing_clique_capacity"]):
        raise AssertionError("exact anchor split count exceeded the spacing clique capacity")

    return {
        **clique,
        "split_residues": tuple(sorted(residues.items())),
        "aligned_split_points": tuple(aligned),
        "aligned_split_count": len(aligned),
        "anchor_split_points": tuple(anchor),
        "anchor_split_count": len(anchor),
        "same_product_terminal_capacity": min(
            len(factors),
            int(clique["split_spacing_clique_capacity"]),
            len(anchor),
        ),
    }
