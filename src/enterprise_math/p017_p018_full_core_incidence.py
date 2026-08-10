"""Exact full-core incidence from the P017×P018 anchor-Möbius divisor fibers.

The generic core-adaptive Bonferroni majorant uses the *complete* transverse
small-prime core C(n), not merely one selected token.  This module shows that
its column incidence can be reconstructed without first enumerating signed
rows.

Fix k, M=k(k+1), N_max=k(k+2), and let P_perp be the finite set of odd
transverse primes p<=k with p∤M.  Let

    A = product_{p in R} p^{e_p},  e_p>=1,

where R is a subset of P_perp.  Write F_surv(E) for the exact anchor-surviving
signed incidence of the divisor E, supplied by the centered anchor-Möbius
boundary-carry layer.

A is the complete transverse small-prime core of n exactly when:

1. A|n;
2. for every p in R, pA∤n (exact selected p-adic exponent);
3. no q in P_perp\R divides n/A.

Finite inclusion-exclusion therefore gives

    I_full(A)
      = sum_{Q squarefree, supp(Q) subset P_perp\R} mu(Q)
          sum_{J subset R} (-1)^|J|
              F_surv(A Q product_{p in J} p).

Terms whose divisor exceeds N_max vanish automatically and may be omitted.
This is an exact finite formula.  It is the all-support analogue of the
least-support/exact-valuation CG13/CG14 formulas on P017, but here the outside
Möbius factor excludes *every* unselected transverse small prime.

Consequently, for any positive odd Bonferroni order m, the high full-core
correction has the exact column form

    H_m^core
      = sum_{A>k-1} I_full(A)
          binom(omega(rad A)-1,m).

For A>k-1, P017 CG12 gives I_full(A)<=1 because A itself is an odd transverse
divisor.  Thus the row defect has been turned into a weighted single-use column
sum whose individual divisor fibers are computable from bulk quotients plus the
finite anchor-Möbius boundary-carry spectrum.

This closes the *representation* interface only.  It does not provide the
uniform inequality needed for Legendre's conjecture; the remaining problem is
to control the weighted high-core sum (or equivalently the low-core residual)
without enumerating exponentially many divisor terms.
"""

from __future__ import annotations

from itertools import combinations
from math import comb

from .legendre import primes_up_to
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_core_adaptive_bonferroni import complete_transverse_core
from .p017_p018_signed_boundary_carry import anchor_surviving_divisor_boundary_carry


def _factor_with_exponents(value: int) -> tuple[tuple[int, int], ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    factors: list[tuple[int, int]] = []
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            exponent = 0
            while remaining % candidate == 0:
                remaining //= candidate
                exponent += 1
            factors.append((candidate, exponent))
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def _transverse_odd_primes(k: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    center = k * (k + 1)
    return tuple(
        p for p in primes_up_to(k)
        if p % 2 == 1 and center % p != 0
    )


def _bounded_squarefree_terms(
    primes: tuple[int, ...],
    limit: int,
) -> tuple[tuple[int, int], ...]:
    """Return (Q,mu(Q)) for squarefree Q from primes with Q<=limit."""
    if limit < 1:
        return ()
    rows: list[tuple[int, int]] = [(1, 1)]

    def extend(start: int, current: int, parity: int) -> None:
        for index in range(start, len(primes)):
            prime = primes[index]
            if current > limit // prime:
                continue
            value = current * prime
            rows.append((value, -1 if parity == 0 else 1))
            extend(index + 1, value, parity + 1)

    extend(0, 1, 0)
    rows.sort(key=lambda row: row[0])
    return tuple(rows)


def _validated_full_core(k: int, full_core: int) -> tuple[tuple[int, int], ...]:
    if (
        isinstance(full_core, bool)
        or not isinstance(full_core, int)
        or full_core < 3
        or full_core % 2 == 0
    ):
        raise ValueError("full_core must be an odd integer >=3")
    factors = _factor_with_exponents(full_core)
    center = k * (k + 1)
    if any(prime > k or center % prime == 0 for prime, _exponent in factors):
        raise ValueError("full_core primes must be transverse and <=k")
    if full_core > k * (k + 2):
        raise ValueError("full_core exceeds the open square-basin maximum")
    return factors


def direct_full_core_signed_points(k: int, full_core: int) -> tuple[int, ...]:
    """Reference-only direct rows whose complete transverse core is exactly A."""
    factors = _validated_full_core(k, full_core)
    selected = tuple(prime for prime, _exponent in factors)
    profile = signed_support_profile(k)
    points: list[int] = []
    for row in profile["rows"]:
        support = tuple(int(p) for p in row["support"])
        if support != selected:
            continue
        state = int(row["state"])
        if complete_transverse_core(state, support) != full_core:
            continue
        point = (
            int(row["radius"])
            if str(row["side"]) == "lower"
            else -int(row["radius"])
        )
        points.append(point)
    return tuple(sorted(points))


def full_core_incidence_mobius(
    k: int,
    full_core: int,
    *,
    verify_direct: bool = True,
) -> dict[str, object]:
    """Evaluate the exact all-support + exact-valuation Möbius formula for A."""
    factors = _validated_full_core(k, full_core)
    selected = tuple(prime for prime, _exponent in factors)
    selected_set = set(selected)
    outside = tuple(
        prime for prime in _transverse_odd_primes(k)
        if prime not in selected_set
    )
    limit = k * (k + 2)
    outer_terms = _bounded_squarefree_terms(outside, limit // full_core)

    total = 0
    rows: list[tuple[int, int, int, int, int]] = []
    for outside_product, mu in outer_terms:
        base = full_core * outside_product
        for subset_size in range(len(selected) + 1):
            for subset in combinations(selected, subset_size):
                multiplier = 1
                for prime in subset:
                    multiplier *= prime
                divisor = base * multiplier
                if divisor > limit:
                    continue
                sign = mu * (-1 if subset_size % 2 else 1)
                incidence = int(
                    anchor_surviving_divisor_boundary_carry(k, divisor)[
                        "anchor_surviving_fiber_size"
                    ]
                )
                total += sign * incidence
                rows.append(
                    (
                        outside_product,
                        multiplier,
                        sign,
                        divisor,
                        incidence,
                    )
                )

    if total < 0:
        raise AssertionError("full-core Möbius incidence became negative")

    direct_points: tuple[int, ...] | None = None
    if verify_direct:
        direct_points = direct_full_core_signed_points(k, full_core)
        if total != len(direct_points):
            raise AssertionError("full-core Möbius formula disagrees with direct incidence")

    if full_core > k - 1 and total > 1:
        raise AssertionError("high full core violated CG12 single-use capacity")

    return {
        "k": k,
        "full_core": full_core,
        "prime_exponents": factors,
        "support_primes": selected,
        "support_size": len(selected),
        "outside_transverse_prime_count": len(outside),
        "mobius_term_rows": tuple(rows),
        "full_core_incidence": total,
        "high_core_single_use": full_core > k - 1,
        "direct_signed_points": direct_points,
    }


def high_core_bonferroni_weight(full_core: int, order: int) -> int:
    """Return binom(omega(rad A)-1,m), the row-defect weight encoded by A."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    support_size = len(_factor_with_exponents(full_core))
    if support_size <= order:
        return 0
    return comb(support_size - 1, order)
