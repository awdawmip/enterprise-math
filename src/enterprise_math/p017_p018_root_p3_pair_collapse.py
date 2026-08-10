"""Square-diagonal Generation 3: every root-certified P3 triple has two free variables.

Let

    U_k = k^2+2k,
    z3 = floor(U_k^(1/4)).

A z3-rough triple-prime survivor has

    n = a*b*c,  z3 < a <= b <= c,

with prime factors counted with multiplicity.  Since

    a*b >= (z3+1)^2 > sqrt(U_k) > k,

the third-factor interval

    k^2/(ab) < c <= U_k/(ab)

has length strictly below 2.  For k>=4 one has z3>=2, hence all three factors
are odd.  The at-most-two consecutive integer candidates therefore contain at
most one possible prime candidate.

Write d=ab, U=q*d+s with 0<=s<d.  The unique possible odd prime candidate is

    c_star = q              if q is odd,
             q-1            if q is even.

Let eps=0 in the first case and eps=1 in the second.  Then c_star lies in the
square shell exactly when

    s + eps*d < 2k.

The ordering condition c_star>=b is equivalent to ab^2<=U.  Thus every
root-certified P3 contaminant is encoded by the prime pair (a,b), one endpoint
remainder gate and the primality of a deterministic odd floor candidate.

This is a structural specialization of short-interval P2/bilinear geometry. It
is not a new asymptotic P2 theorem and does not by itself remove the triple
contaminants.
"""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    rough_survivor_offsets,
    square_interval_upper,
)


def root_p3_odd_candidate(k: int, a: int, b: int) -> dict[str, object]:
    """Project a root-certified factor pair to its unique possible odd c."""
    for name, value in (("k", k), ("a", a), ("b", b)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if k < 4:
        raise ValueError("require k>=4 so the P3 root cutoff is at least 2")

    upper = square_interval_upper(k)
    width = 2 * k
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    if not (z3 < a <= b):
        raise ValueError("require root-certified factors z3<a<=b")

    divisor = a * b
    if not divisor * divisor > upper:
        raise AssertionError("two root-certified factors failed ab>sqrt(U)")
    if not divisor > k:
        raise AssertionError("ab>sqrt(U)>k failed")
    if not 2 * divisor > width:
        raise AssertionError("third-factor interval did not have length <2")

    q, s = divmod(upper, divisor)
    even_top = q % 2 == 0
    epsilon = int(even_top)
    candidate = q - epsilon
    if candidate % 2 != 1:
        raise AssertionError("odd-candidate projection failed")

    gate_left = s + epsilon * divisor
    in_shell = gate_left < width
    value = divisor * candidate
    if in_shell != (k * k < value <= upper):
        raise AssertionError("odd endpoint gate lost exact shell membership")

    ordered = candidate >= b
    ordered_product_gate = a * b * b <= upper
    if ordered != ordered_product_gate:
        # If q is even and q>=b, odd b prevents q=b, hence q-1>=b.
        raise AssertionError("c_star>=b and ab^2<=U lost equivalence")

    raw_candidates = tuple(
        c for c in (q - 1, q) if k * k < divisor * c <= upper
    )
    if len(raw_candidates) > 2:
        raise AssertionError("root-certified pair produced more than two integer candidates")
    odd_candidates = tuple(c for c in raw_candidates if c % 2 == 1)
    if len(odd_candidates) > 1:
        raise AssertionError("two consecutive integers produced two odd candidates")
    if in_shell and odd_candidates != (candidate,):
        raise AssertionError("odd shell candidate disagreed with raw interval reconstruction")
    if not in_shell and candidate in raw_candidates:
        raise AssertionError("closed odd gate left candidate in the raw interval")

    return {
        "k": k,
        "upper": upper,
        "width": width,
        "p3_cutoff": z3,
        "a": a,
        "b": b,
        "pair_product": divisor,
        "top_quotient": q,
        "top_remainder": s,
        "parity_correction": epsilon,
        "odd_candidate": candidate,
        "odd_gate_left": gate_left,
        "candidate_in_shell": in_shell,
        "ordered_candidate": ordered,
        "ordered_product_gate": ordered_product_gate,
        "candidate_is_prime": is_prime(candidate),
        "prime_triple_gate": in_shell and ordered and is_prime(candidate),
        "raw_integer_candidates": raw_candidates,
        "status": "ROOT_P3_TWO_FREE_VARIABLES",
    }


def root_p3_prime_triples_via_pairs(k: int) -> dict[str, object]:
    """Enumerate all z3-rough triple-prime survivors through prime pairs."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    upper = square_interval_upper(k)
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    factor_primes = tuple(p for p in primes_up_to(z2) if p > z3)

    rows: list[tuple[int, int, int, int, int]] = []
    for i, a in enumerate(factor_primes):
        for b in factor_primes[i:]:
            if a * b * b > upper:
                break
            projection = root_p3_odd_candidate(k, a, b)
            if not bool(projection["prime_triple_gate"]):
                continue
            c = int(projection["odd_candidate"])
            value = a * b * c
            rows.append((a, b, c, value, value - k * k))

    # Independent bounded reconstruction from every z3-rough state.
    direct: list[tuple[int, int, int, int, int]] = []
    for r in rough_survivor_offsets(k, z3):
        value = k * k + r
        if is_prime(value):
            continue
        remaining = value
        factors: list[int] = []
        for p in primes_up_to(z2):
            if p <= z3:
                continue
            while remaining % p == 0:
                factors.append(p)
                remaining //= p
            if remaining == 1:
                break
            if p * p > remaining:
                break
        if remaining > 1:
            factors.append(remaining)
        factors.sort()
        if len(factors) == 3 and all(is_prime(p) for p in factors):
            a, b, c = factors
            direct.append((a, b, c, value, r))

    if set(rows) != set(direct):
        raise AssertionError("pair projection failed to reconstruct every root-certified P3 triple")

    return {
        "k": k,
        "p3_cutoff": z3,
        "p2_cutoff": z2,
        "triple_rows": tuple(sorted(rows)),
        "triple_count": len(rows),
        "free_discrete_variables": 2,
        "status": "ROOT_P3_TWO_FREE_VARIABLES",
    }
