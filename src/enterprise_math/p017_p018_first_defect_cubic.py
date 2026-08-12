"""Cubic compression of the first residual order-three Bonferroni defect band.

The residual hard-core bridge and Bonferroni primorial localization give a
particularly rigid first scale band for order three:

    P_odd(5)=15015 < k <= P_odd(6)=255255.

If a residual pair has positive order-three Bonferroni defect, the first-band
rigidity theorem forces exactly five distinct odd core primes in total, split
between the two mirror sides as (4,1) or (1,4), and the total pair defect is
exactly one.

Universally the four-prime core is at least 3*5*7*11=1155, whose square already
exceeds the whole first band.  Hence that side is always the numerical larger
core and the smaller core is an odd prime power.

The anchor-sensitive refinement is stronger.  Let

    T_4(k)=P_perp(k,4)

be the product of the first four odd primes transverse to M=k(k+1).  Every
four-prime defect side satisfies e>=T_4(k), so

    d <= floor((k-1)/T_4(k)).

Likewise T_5(k)=P_perp(k,5) is a joint obstruction: if T_5(k)>=k, no residual
order-three defect can exist at all.

Now consume the existing P017/P018 cubic partner-resolution theorem.  With

    D_c(k)=floor(((H_c(k)+1)^2-1)/k),

any residual pair whose smaller core d exceeds D_c(k) has both odd full-core
root channels above the cubic candidate horizon and is fully root-resolved.
Consequently every *unresolved* first-band order-three defect lies on an odd
transverse prime-power label

    d <= min(D_c(k), floor((k-1)/T_4(k))).

This is an exact bridge theorem.  It does not assert that every label in the
budget occurs, nor that every label inside the budget is unresolved.  It only
compresses the possible unresolved defect labels.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_p018_bonferroni_shell_horizon import (
    residual_first_defect_band_rigidity,
)
from .p017_p018_cubic_pair_resolution import (
    cubic_partner_ambiguity_cutoff,
    residual_pair_cubic_resolution,
)
from .p017_p018_transverse_primorial import transverse_odd_primorial


ORDER_THREE_FIRST_BAND_LOWER = 15_015
ORDER_THREE_FIRST_BAND_UPPER = 255_255
UNIVERSAL_MIN_FOUR_ODD_PRIME_PRODUCT = 1_155


def _require_first_band(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int):
        raise ValueError("k must be an integer")
    if not ORDER_THREE_FIRST_BAND_LOWER < k <= ORDER_THREE_FIRST_BAND_UPPER:
        raise ValueError("k must lie in the first residual order-three defect band")


def odd_prime_power_base(value: int) -> int | None:
    """Return the unique odd prime base when value is an odd prime power."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 3 or value % 2 == 0:
        return None
    remaining = value
    base: int | None = None
    candidate = 3
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            if not is_prime(candidate):
                candidate += 2
                continue
            if base is None:
                base = candidate
            elif base != candidate:
                return None
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 2
    if remaining > 1:
        if base is None:
            base = remaining
        elif remaining != base:
            return None
    return base if base is not None and is_prime(base) else None


def first_band_order3_label_cutoff(k: int) -> dict[str, object]:
    """Return the dynamic unresolved small-label cutoff.

    The four-prime side is bounded below by the first four transverse odd primes,
    while the first five transverse odd primes give a complete residual-defect
    impossibility test.
    """
    _require_first_band(k)
    four = transverse_odd_primorial(k, 4)
    five = transverse_odd_primorial(k, 5)
    if not bool(four["complete"]) or not bool(five["complete"]):
        raise AssertionError("first defect band unexpectedly lacks five transverse odd primes")

    four_product = int(four["product"])
    five_product = int(five["product"])
    if four_product < UNIVERSAL_MIN_FOUR_ODD_PRIME_PRODUCT:
        raise AssertionError("transverse four-prime product fell below the universal minimum")

    cubic = cubic_partner_ambiguity_cutoff(k)
    product_cutoff = (k - 1) // four_product
    return {
        "k": k,
        "cubic_partner_ambiguity_cutoff": cubic,
        "four_prime_transverse_primes": tuple(four["transverse_primes"]),
        "minimum_four_prime_core": four_product,
        "five_prime_transverse_primes": tuple(five["transverse_primes"]),
        "minimum_five_prime_core_product": five_product,
        "residual_order3_defect_impossible": five_product >= k,
        "four_prime_product_cutoff": product_cutoff,
        "unresolved_prime_power_label_cutoff": min(cubic, product_cutoff),
    }


def transverse_odd_prime_power_labels(k: int, cutoff: int) -> tuple[int, ...]:
    """List odd prime powers <=cutoff that are transverse to M=k(k+1)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    center = k * (k + 1)
    return tuple(
        value
        for value in range(3, cutoff + 1, 2)
        if gcd(value, center) == 1 and odd_prime_power_base(value) is not None
    )


def first_band_order3_ambiguity_budget(k: int) -> dict[str, object]:
    """Return the finite prime-power label superset for unresolved defect pairs."""
    cutoffs = first_band_order3_label_cutoff(k)
    cutoff = int(cutoffs["unresolved_prime_power_label_cutoff"])
    labels = transverse_odd_prime_power_labels(k, cutoff)
    if bool(cutoffs["residual_order3_defect_impossible"]) and labels:
        # Labels can exist arithmetically, but the five-prime joint barrier has
        # already killed the residual defect.  The effective ambiguity budget is
        # therefore empty.
        labels = ()
    return {
        **cutoffs,
        "candidate_prime_power_labels": labels,
        "candidate_label_count": len(labels),
    }


def residual_order3_defect_cubic_compression(k: int, radius: int) -> dict[str, object]:
    """Classify one actual first-band residual order-three defect pair.

    Positive defect is required.  The theorem proves the smaller core is an odd
    prime power and either the pair is already cubic-resolved or that prime
    power lies in the finite transverse-prime ambiguity-label budget.
    """
    _require_first_band(k)
    data = residual_first_defect_band_rigidity(k, radius, 3)
    if int(data["total_pair_defect"]) != 1:
        raise ValueError("radius must carry positive residual order-three defect")

    cutoffs = first_band_order3_label_cutoff(k)
    if bool(cutoffs["residual_order3_defect_impossible"]):
        raise AssertionError("actual first-band residual defect violates the transverse five-prime barrier")

    a = int(data["lower_core"])
    b = int(data["upper_core"])
    a_support = int(data["lower_support_size"])
    b_support = int(data["upper_support_size"])

    if sorted((a_support, b_support)) != [1, 4]:
        raise AssertionError("first-band order-three defect lost its rigid 4+1 support split")

    four_prime_core = a if a_support == 4 else b
    one_prime_core = b if a_support == 4 else a
    dynamic_four_minimum = int(cutoffs["minimum_four_prime_core"])
    if four_prime_core < dynamic_four_minimum:
        raise AssertionError("four-prime core fell below its transverse minimum product")
    if UNIVERSAL_MIN_FOUR_ODD_PRIME_PRODUCT**2 <= ORDER_THREE_FIRST_BAND_UPPER:
        raise AssertionError("static four-prime square comparison was miscomputed")
    if four_prime_core * four_prime_core <= k:
        raise AssertionError("four-prime core failed to lie above sqrt(k) in the first band")

    small_core = min(a, b)
    large_core = max(a, b)
    if small_core != one_prime_core or large_core != four_prime_core:
        raise AssertionError("support rigidity did not identify the numerical small/large cores")

    prime_base = odd_prime_power_base(small_core)
    if prime_base is None:
        raise AssertionError("one-prime small core is not an odd prime power")
    product_cutoff = int(cutoffs["four_prime_product_cutoff"])
    if small_core > product_cutoff:
        raise AssertionError("small prime-power core exceeded the transverse four-prime product cutoff")

    resolution = residual_pair_cubic_resolution(k, small_core, large_core)
    cubic_cutoff = int(cutoffs["cubic_partner_ambiguity_cutoff"])
    fully_resolved = bool(resolution["fully_core_pair_root_resolved"])
    if not fully_resolved and small_core > cubic_cutoff:
        raise AssertionError("unresolved defect escaped the cubic ambiguity cutoff")

    budget = first_band_order3_ambiguity_budget(k)
    inside_budget = small_core in set(budget["candidate_prime_power_labels"])
    if not fully_resolved and not inside_budget:
        raise AssertionError("unresolved defect escaped the transverse prime-power label budget")

    return {
        **data,
        "small_core": small_core,
        "large_core": large_core,
        "small_core_prime_base": prime_base,
        "four_prime_core": four_prime_core,
        "four_prime_transverse_primes": tuple(cutoffs["four_prime_transverse_primes"]),
        "minimum_four_prime_core": dynamic_four_minimum,
        "five_prime_transverse_primes": tuple(cutoffs["five_prime_transverse_primes"]),
        "minimum_five_prime_core_product": int(cutoffs["minimum_five_prime_core_product"]),
        "four_prime_product_cutoff": product_cutoff,
        "cubic_partner_ambiguity_cutoff": cubic_cutoff,
        "fully_cubic_resolved": fully_resolved,
        "inside_unresolved_prime_power_budget": inside_budget,
        "unresolved_prime_power_small_label": (not fully_resolved) and inside_budget,
        "larger_base_root": int(resolution["larger_base_root"]),
        "cubic_horizon": int(resolution["cubic_horizon"]),
    }
