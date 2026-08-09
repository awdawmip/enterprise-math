"""Route Bonferroni row defect into squarefree signed-divisor tokens.

For one anchor-surviving signed state with transverse support

    P={p_0<p_1<...<p_{c-1}}

and positive odd Bonferroni order m, the exact point defect is

    E_m(P)=binom(c-1,m).

Fix the least support prime p_0.  For every m-element subset T of
P\{p_0}, form the squarefree product

    D = p_0 * product(T).

There are exactly binom(c-1,m) such products, and every D divides the signed
state M-x.  Thus Bonferroni defect is not merely a row multiplicity: it admits an
exact decomposition into squarefree multi-prime divisor incidences.

This supplies the missing row-to-column interface to the P017 owner-local signed
divisor capacity theorem on PR #191 (commit family beginning at 2b6fa4): an odd
transverse divisor D occupies one residue class modulo 2D and has signed reuse
capacity at most floor((k-1)/D)+1.  In particular, if the minimum possible
(m+1)-prime transverse token product is greater than k-1, every order-m defect
token is globally single-use across both mirror orientations.

The same threshold forces strict quotient descent.  If D>k-1 is an integer
transverse to M=k(k+1), then D cannot equal k or k+1, so D>=k+2.  For a state in
the open square basin,

    n <= (k+1)^2-1 = k(k+2),

and therefore

    q=n/D <= k.

Thus a globally single-use high-product defect token carries its state to an
exact quotient at or below the parent scale.  More generally the minimum token
product gives a finite quotient ceiling

    Q_m(k)=floor(k(k+2)/P_perp(k,m+1)).

The token decomposition and quotient inequalities are exact.  The cross-branch
reuse-capacity theorem remains a PROVED_WIP P017 input until separately
promoted; this bridge does not duplicate its implementation or claim canonical
status.
"""

from __future__ import annotations

from itertools import combinations
from math import comb, gcd, isqrt, prod

from .legendre import is_prime
from .p017_p018_bonferroni_defect import odd_bonferroni_point_defect
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_transverse_primorial import transverse_odd_primorial


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def point_defect_tokens(support: tuple[int, ...], order: int) -> dict[str, object]:
    """Return the canonical least-prime squarefree tokens for one support row."""
    _require_order(order)
    if len(set(support)) != len(support):
        raise ValueError("support primes must be distinct")
    normalized = tuple(sorted(support))
    for prime in normalized:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime < 3
            or not is_prime(prime)
        ):
            raise ValueError("support entries must be distinct odd primes")

    support_size = len(normalized)
    point = odd_bonferroni_point_defect(support_size, order)
    expected = int(point["defect"])
    if not normalized or support_size <= order:
        tokens: tuple[int, ...] = ()
        least: int | None = normalized[0] if normalized else None
    else:
        least = normalized[0]
        tokens = tuple(
            least * prod(subset)
            for subset in combinations(normalized[1:], order)
        )

    if len(tokens) != expected:
        raise AssertionError("defect token count does not equal binom(c-1,m)")
    if len(set(tokens)) != len(tokens):
        raise AssertionError("distinct prime subsets produced duplicate squarefree tokens")
    if expected != (comb(support_size - 1, order) if support_size > order else 0):
        raise AssertionError("point defect lost its binomial coordinate")

    return {
        "support": normalized,
        "support_size": support_size,
        "order": order,
        "least_support_prime": least,
        "defect": expected,
        "tokens": tokens,
    }


def defect_token_single_use_threshold(k: int, order: int) -> dict[str, object]:
    """Return the minimum transverse token product and #191 single-use regime."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)
    minimum = transverse_odd_primorial(k, order + 1)
    complete = bool(minimum["complete"])
    product_value = int(minimum["product"])
    return {
        "k": k,
        "order": order,
        "required_token_prime_count": order + 1,
        "minimum_transverse_token_primes": tuple(minimum["transverse_primes"]),
        "minimum_transverse_token_product": product_value,
        "enough_transverse_primes": complete,
        "all_defect_tokens_globally_single_use_by_p017_capacity": (
            (not complete) or product_value > k - 1
        ),
        "capacity_dependency": "P017_PROVED_WIP_SIGNED_COMPOSITE_DIVISOR_CAPACITY",
    }


def defect_token_quotient_horizon(k: int, order: int) -> dict[str, object]:
    """Return Q_m(k)=floor(k(k+2)/minimum token product) exactly."""
    threshold = defect_token_single_use_threshold(k, order)
    if not bool(threshold["enough_transverse_primes"]):
        return {
            **threshold,
            "defect_tokens_possible": False,
            "quotient_ceiling": 0,
            "quotient_root_ceiling": 0,
            "strict_parent_scale_descent": True,
        }
    minimum = int(threshold["minimum_transverse_token_product"])
    ceiling = (k * (k + 2)) // minimum
    root_ceiling = isqrt(ceiling)
    strict = minimum > k - 1
    if strict and ceiling > k:
        raise AssertionError("single-use token threshold failed to force q<=k")
    return {
        **threshold,
        "defect_tokens_possible": True,
        "quotient_ceiling": ceiling,
        "quotient_root_ceiling": root_ceiling,
        "strict_parent_scale_descent": strict,
    }


def defect_token_quotient_descent(k: int, state: int, divisor: int) -> dict[str, int | bool]:
    """Certify q=state/D<=k for one transverse token with D>k-1."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int) or not (k * k < state < (k + 1) ** 2):
        raise ValueError("state must lie in the open k-th square basin")
    center = k * (k + 1)
    if (
        isinstance(divisor, bool)
        or not isinstance(divisor, int)
        or divisor <= k - 1
        or divisor % 2 == 0
        or gcd(divisor, center) != 1
    ):
        raise ValueError("divisor must be an odd transverse token with D>k-1")
    if state % divisor:
        raise ValueError("divisor must divide the square-basin state")
    if divisor in (k, k + 1):
        raise AssertionError("transverse token cannot equal an anchor factor")
    if divisor < k + 2:
        raise AssertionError("D>k-1 and transversality failed to imply D>=k+2")

    quotient = state // divisor
    if quotient > k:
        raise AssertionError("single-use token quotient did not descend to q<=k")
    return {
        "k": k,
        "state": state,
        "divisor": divisor,
        "quotient": quotient,
        "quotient_root": isqrt(quotient),
        "strict_parent_scale_descent": True,
    }


def signed_defect_token_profile(k: int, order: int) -> dict[str, object]:
    """Decompose the entire signed-state Bonferroni defect into divisor tokens."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)
    center = k * (k + 1)
    profile = signed_support_profile(k)

    token_rows: list[dict[str, object]] = []
    multiplicities: dict[int, list[int]] = {}
    total_defect = 0
    for row in profile["rows"]:
        support = tuple(int(prime) for prime in row["support"])
        token_data = point_defect_tokens(support, order)
        defect = int(token_data["defect"])
        total_defect += defect
        if defect == 0:
            continue

        radius = int(row["radius"])
        side = str(row["side"])
        signed_point = radius if side == "lower" else -radius
        state = int(row["state"])
        if state != center - signed_point:
            raise AssertionError("signed-state convention M-x failed")

        tokens = tuple(int(value) for value in token_data["tokens"])
        for divisor in tokens:
            if divisor % 2 == 0 or gcd(divisor, center) != 1:
                raise AssertionError("defect token is not odd and transverse")
            if state % divisor:
                raise AssertionError("defect token does not divide its signed state")
            multiplicities.setdefault(divisor, []).append(signed_point)

        token_rows.append(
            {
                "radius": radius,
                "side": side,
                "signed_point": signed_point,
                "state": state,
                "support": support,
                "support_size": len(support),
                "defect": defect,
                "tokens": tokens,
            }
        )

    token_count = sum(len(row["tokens"]) for row in token_rows)
    if token_count != total_defect:
        raise AssertionError("global defect did not equal squarefree token incidence mass")

    grouped = {
        divisor: tuple(points)
        for divisor, points in sorted(multiplicities.items())
    }
    return {
        "k": k,
        "order": order,
        "signed_state_count": int(profile["signed_state_count"]),
        "prime_state_count": int(profile["prime_state_count"]),
        "composite_state_count": int(profile["composite_state_count"]),
        "high_support_defect": total_defect,
        "defect_token_count": token_count,
        "defect_rows": tuple(token_rows),
        "token_signed_point_multiplicities": grouped,
        "single_use_threshold": defect_token_single_use_threshold(k, order),
        "quotient_horizon": defect_token_quotient_horizon(k, order),
    }
