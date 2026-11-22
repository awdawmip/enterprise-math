"""Route Bonferroni row defect into squarefree and full-block divisor tokens.

For one anchor-surviving signed state with transverse support

    P={p_0<p_1<...<p_{c-1}}

and positive odd Bonferroni order m, the exact point defect is

    E_m(P)=binom(c-1,m).

Fix the least support prime p_0.  For every m-element subset T of
P\{p_0}, form two parallel tokens:

    D_rad  = p_0 * product(T),
    D_full = product_{p in {p_0} union T} p^{v_p(n)}.

There are exactly binom(c-1,m) token pairs.  Both divide the signed state M-x;
D_rad records support only, while D_full removes the complete selected
prime-power blocks.

The squarefree token supplies the row-to-column interface to the P017
owner-local signed divisor capacity theorem on PR #191: any odd transverse D
has signed reuse capacity at most floor((k-1)/D)+1.  Since D_full>=D_rad, the
same capacity mechanism is at least as strong on the full-block token.

If D_rad>k-1, transversality excludes D_rad=k,k+1, so D_rad>=k+2.  Every
corresponding full-block quotient satisfies

    q=n/D_full <= n/D_rad <= k.

Canonical L020 then forces the original square-basin state to have no large
prime tail >k, because that tail would survive the selected small-prime block
removal and divide q.  Thus every high-product single-use defect row is fully
k-smooth.  Its full k-smooth core is therefore the state itself, which is >k^2;
hence any mirror full-core product containing this side is already >k and the
canonical L053 full-core progression is singleton.  Consequently every defect
token that can participate in a repeated residual S<k hard-core cell must lie
in the complementary reusable regime

    D_rad <= k-1.

Moreover the small-prime support of q is exactly the complement of the selected
support primes.  Full-block descent deletes precisely m+1 support directions.
If c=m+1, then q=1 and D_full=n.

The token decomposition and quotient inequalities are exact.  The cross-branch
reuse-capacity theorem remains a PROVED_WIP P017 input until separately
promoted; this bridge does not duplicate its implementation or claim canonical
status.
"""

from __future__ import annotations

from itertools import combinations
from math import comb, gcd, isqrt, prod

from .cutoff_pairing import distinct_prime_factors, transverse_prime_support
from .legendre import anchor_product, is_prime
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_p018_bonferroni_defect import odd_bonferroni_point_defect
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_transverse_primorial import transverse_odd_primorial


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def _prime_power_block(state: int, prime: int) -> int:
    block = 1
    remaining = state
    while remaining % prime == 0:
        block *= prime
        remaining //= prime
    return block


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


def high_product_token_singleton_state(k: int, state: int, radical_token: int) -> dict[str, int | bool]:
    """Certify that D_rad>k-1 forces a fully-smooth L053-singleton side."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int) or not (k * k < state < (k + 1) ** 2):
        raise ValueError("state must lie in the open k-th square basin")
    center = k * (k + 1)
    if (
        isinstance(radical_token, bool)
        or not isinstance(radical_token, int)
        or radical_token <= k - 1
        or radical_token % 2 == 0
        or gcd(radical_token, center) != 1
        or state % radical_token
    ):
        raise ValueError("radical_token must be an odd transverse divisor >k-1 of state")

    # Remove complete blocks for every selected prime represented in the squarefree token.
    selected = tuple(distinct_prime_factors(radical_token))
    if prod(selected) != radical_token:
        raise ValueError("radical_token must be squarefree")
    full_token = prod(_prime_power_block(state, prime) for prime in selected)
    descent = defect_token_quotient_descent(k, state, full_token)
    smooth = square_basin_smooth_tail(k, state)
    if int(smooth["tail"]) != 1:
        raise AssertionError("high-product token side retained an L020 large tail")
    if int(smooth["smooth_core"]) != state:
        raise AssertionError("fully smooth state did not equal its L020 full core")
    if state <= k:
        raise AssertionError("square-basin full core did not exceed k")

    return {
        "k": k,
        "state": state,
        "squarefree_token": radical_token,
        "full_block_token": full_token,
        "quotient": int(descent["quotient"]),
        "fully_k_smooth": True,
        "full_core": state,
        "full_core_exceeds_k": True,
        "l053_singleton_for_any_mirror_partner": True,
        "cannot_belong_to_repeated_residual_S_lt_k_cell": True,
    }


def point_full_block_defect_tokens(
    k: int,
    state: int,
    support: tuple[int, ...],
    order: int,
) -> dict[str, object]:
    """Lift each squarefree defect token to complete selected prime-power blocks."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int) or not (k * k < state < (k + 1) ** 2):
        raise ValueError("state must lie in the open k-th square basin")
    _require_order(order)
    center = k * (k + 1)
    if gcd(state, center) != 1:
        raise ValueError("state must be anchor-surviving")

    canonical_support = tuple(transverse_prime_support(state, k, anchor_product(k)))
    normalized = tuple(sorted(support))
    if normalized != canonical_support:
        raise ValueError("support must equal the complete transverse small-prime support of state")

    squarefree = point_defect_tokens(normalized, order)
    if not normalized or len(normalized) <= order:
        rows: tuple[dict[str, object], ...] = ()
    else:
        least = normalized[0]
        token_rows: list[dict[str, object]] = []
        for subset in combinations(normalized[1:], order):
            selected = (least, *subset)
            radical_token = prod(selected)
            full_token = prod(_prime_power_block(state, prime) for prime in selected)
            quotient = state // full_token
            omitted = tuple(prime for prime in normalized if prime not in selected)

            if state % full_token:
                raise AssertionError("full-block token does not divide state")
            if full_token < radical_token:
                raise AssertionError("full-block token shrank below its squarefree radical")
            if any(quotient % prime == 0 for prime in selected):
                raise AssertionError("selected full prime-power block survived in quotient")
            if any(quotient % prime != 0 for prime in omitted):
                raise AssertionError("omitted support prime disappeared from quotient")

            single_use_product_regime = radical_token > k - 1
            fully_k_smooth = False
            quotient_support: tuple[int, ...] | None = None
            l053_singleton = False
            if single_use_product_regime:
                singleton = high_product_token_singleton_state(k, state, radical_token)
                if int(singleton["full_block_token"]) != full_token:
                    raise AssertionError("singleton full-block token disagrees with selected block product")
                if int(singleton["quotient"]) != quotient:
                    raise AssertionError("singleton quotient disagrees with selected block quotient")
                fully_k_smooth = True
                l053_singleton = True
                quotient_support = tuple(distinct_prime_factors(quotient)) if quotient > 1 else ()
                if quotient_support != omitted:
                    raise AssertionError("full-block quotient support is not the exact support complement")
                if not omitted and quotient != 1:
                    raise AssertionError("full-support token did not collapse to quotient one")

            token_rows.append(
                {
                    "selected_primes": selected,
                    "omitted_support_primes": omitted,
                    "squarefree_token": radical_token,
                    "full_block_token": full_token,
                    "quotient": quotient,
                    "single_use_product_regime": single_use_product_regime,
                    "reusable_product_regime": radical_token <= k - 1,
                    "fully_k_smooth": fully_k_smooth,
                    "l053_singleton_side": l053_singleton,
                    "quotient_support": quotient_support,
                }
            )
        rows = tuple(token_rows)

    if len(rows) != int(squarefree["defect"]):
        raise AssertionError("full-block token count lost the exact Bonferroni defect")
    return {
        "k": k,
        "state": state,
        "support": normalized,
        "support_size": len(normalized),
        "order": order,
        "defect": int(squarefree["defect"]),
        "token_rows": rows,
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
