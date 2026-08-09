"""Adaptive Bonferroni truncation order for the P017 mirror basin.

This bridge turns a classical finite inclusion--exclusion fact into a task-relative
proof-order observable.

For every anchor-surviving mirror radius r, consider the two signed basin states
M-r and M+r and their transverse prime supports among primes <= k.  Let c(x) be
the number of distinct transverse primes dividing one signed state x, and define

    S_j(k) = sum_x binom(c(x), j).

Equivalently S_j counts incidences of j-element transverse-prime subsets with
signed mirror states.  The union of all transverse-prime divisibility events is
exactly the set of composite signed states: an open square-basin composite has a
prime divisor <=k, while anchor survival excludes every prime dividing M.

Classical Bonferroni gives, for every h>=0,

    U(k) <= B_{2h+1}(k)

where

    B_m(k) = S_1-S_2+...+S_m     (m odd)

and U is the number of composite signed states.  Therefore

    B_{2h+1}(k) < N_signed(k)

is an exact certificate that at least one signed state is prime.  The least odd
order that certifies this is the declared **adaptive Bonferroni certifying
order** for this observable family.

Important: odd Bonferroni upper truncations are not a monotone refinement chain.
For a point of support size c their exact excess is binom(c-1,m), which can grow
when m increases toward the middle of c-1.  Thus a certificate at one odd order
need not be interpreted as part of a nested precision lattice, and moving from
m to m+2 is not automatically an improvement.  What *is* monotone/stable is the
terminal exact regime: once m reaches every relevant support size, all higher
odd truncations remain exact.  The transverse-primorial bridge supplies such a
uniform exact-order ceiling on the residual S<k hard core.

This is not a new inclusion--exclusion theorem and not a proof of Legendre's
conjecture.  In bounded pressure tests the first order-5 certifying case is
k=862; known anchor-critical scales 8191, 65536, 131071 and 524287 also certify
at order five in independent discovery probes, but those large computations are
not promoted as theorem proof here.
"""

from __future__ import annotations

from math import comb

from .legendre import is_prime
from .p017_mirror import (
    anchor_surviving_radius,
    mirror_pair,
    mirror_transverse_supports,
)


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def signed_support_profile(k: int) -> dict[str, object]:
    """Return exact transverse-support sizes for all anchor-surviving signed states."""
    _require_k(k)
    rows: list[dict[str, int | str | tuple[int, ...] | bool]] = []
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        lower, upper = mirror_pair(k, radius)
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        for side, state, support in (
            ("lower", lower, lower_support),
            ("upper", upper, upper_support),
        ):
            support_tuple = tuple(support)
            prime_state = is_prime(state)
            if (not support_tuple) != prime_state:
                raise AssertionError(
                    "empty transverse support is not equivalent to primality on an anchor-surviving basin state"
                )
            rows.append(
                {
                    "radius": radius,
                    "side": side,
                    "state": state,
                    "support": support_tuple,
                    "support_size": len(support_tuple),
                    "is_prime": prime_state,
                }
            )
    return {
        "k": k,
        "signed_state_count": len(rows),
        "prime_state_count": sum(bool(row["is_prime"]) for row in rows),
        "composite_state_count": sum(not bool(row["is_prime"]) for row in rows),
        "rows": tuple(rows),
    }


def support_moments(k: int, max_order: int) -> dict[str, object]:
    """Return S_j=sum_x binom(c(x),j) through the requested finite order."""
    _require_k(k)
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 1:
        raise ValueError("max_order must be a positive integer")
    profile = signed_support_profile(k)
    moments: list[int] = []
    for order in range(1, max_order + 1):
        moments.append(
            sum(
                comb(int(row["support_size"]), order)
                for row in profile["rows"]
                if int(row["support_size"]) >= order
            )
        )
    return {
        **profile,
        "max_order": max_order,
        "moments": tuple(moments),
    }


def odd_bonferroni_upper_from_moments(moments: tuple[int, ...], order: int) -> int:
    """Return S1-S2+...+S_order for one positive odd truncation."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    if order > len(moments):
        raise ValueError("moments do not reach the requested order")
    return sum(
        moments[index] if index % 2 == 0 else -moments[index]
        for index in range(order)
    )


def bonferroni_precision_certificate(k: int, max_order: int) -> dict[str, object]:
    """Find the least odd Bonferroni order <=max_order that forces a basin prime."""
    _require_k(k)
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 1:
        raise ValueError("max_order must be a positive integer")
    data = support_moments(k, max_order)
    moments = tuple(int(value) for value in data["moments"])
    total = int(data["signed_state_count"])
    composite = int(data["composite_state_count"])

    rows: list[dict[str, int | bool]] = []
    first_certificate: int | None = None
    for order in range(1, max_order + 1, 2):
        upper = odd_bonferroni_upper_from_moments(moments, order)
        if upper < composite:
            raise AssertionError("Bonferroni upper bound fell below the actual union")
        certificate = upper < total
        if certificate and first_certificate is None:
            first_certificate = order
        rows.append(
            {
                "order": order,
                "upper_bound": upper,
                "slack_to_all_states": total - upper,
                "certificate": certificate,
            }
        )

    if (first_certificate is not None) != (int(data["prime_state_count"]) > 0):
        # A finite truncation may fail even when primes exist, but if a
        # certificate exists then a prime must exist.  Only enforce that
        # implication, not the converse.
        if first_certificate is not None and int(data["prime_state_count"]) == 0:
            raise AssertionError("Bonferroni certificate claimed a prime where none exists")

    return {
        **data,
        "odd_order_rows": tuple(rows),
        "first_certifying_order": first_certificate,
        "certified_within_horizon": first_certificate is not None,
    }
