"""Cubic compression of the first residual order-three Bonferroni defect band.

The residual hard-core bridge and Bonferroni primorial localization give a
particularly rigid first scale band for order three:

    P_odd(5)=15015 < k <= P_odd(6)=255255.

If a residual pair has positive order-three Bonferroni defect, the first-band
rigidity theorem forces exactly five distinct odd core primes in total, split
between the two mirror sides as (4,1) or (1,4), and the total pair defect is
exactly one.

The four-prime core is at least

    3*5*7*11 = 1155.

Since 1155^2 > 255255, throughout the whole first band that four-prime core is
strictly larger than sqrt(k).  Hence it is the numerical larger core.  The
other, smaller core has exactly one distinct prime factor and is therefore an
odd prime power.  From d*e<k and e>=1155,

    d <= floor((k-1)/1155).

Now consume the existing P017/P018 cubic partner-resolution theorem.  With

    D_c(k)=floor(((H_c(k)+1)^2-1)/k),

any residual pair whose smaller core d exceeds D_c(k) has both odd full-core
root channels above the cubic candidate horizon and is fully root-resolved.
Consequently every *unresolved* first-band order-three defect lies on an odd
transverse prime-power label

    d <= min(D_c(k), floor((k-1)/1155)).

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


ORDER_THREE_FIRST_BAND_LOWER = 15_015
ORDER_THREE_FIRST_BAND_UPPER = 255_255
MIN_FOUR_ODD_PRIME_PRODUCT = 1_155


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


def first_band_order3_label_cutoff(k: int) -> dict[str, int]:
    """Return the exact unresolved small-label cutoff min(D_c,(k-1)/1155)."""
    _require_first_band(k)
    cubic = cubic_partner_ambiguity_cutoff(k)
    product = (k - 1) // MIN_FOUR_ODD_PRIME_PRODUCT
    return {
        "k": k,
        "cubic_partner_ambiguity_cutoff": cubic,
        "four_prime_product_cutoff": product,
        "unresolved_prime_power_label_cutoff": min(cubic, product),
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
    return {
        **cutoffs,
        "candidate_prime_power_labels": labels,
        "candidate_label_count": len(labels),
    }


def residual_order3_defect_cubic_compression(k: int, radius: int) -> dict[str, object]:
    """Classify one actual first-band residual order-three defect pair.

    Positive defect is required.  The theorem then proves the smaller core is an
    odd prime power and either the pair is already cubic-resolved or that prime
    power lies in the finite ambiguity-label budget.
    """
    _require_first_band(k)
    data = residual_first_defect_band_rigidity(k, radius, 3)
    if int(data["total_pair_defect"]) != 1:
        raise ValueError("radius must carry positive residual order-three defect")

    a = int(data["lower_core"])
    b = int(data["upper_core"])
    a_support = int(data["lower_support_size"])
    b_support = int(data["upper_support_size"])

    if sorted((a_support, b_support)) != [1, 4]:
        raise AssertionError("first-band order-three defect lost its rigid 4+1 support split")

    four_prime_core = a if a_support == 4 else b
    one_prime_core = b if a_support == 4 else a
    if four_prime_core < MIN_FOUR_ODD_PRIME_PRODUCT:
        raise AssertionError("four-prime core fell below 3*5*7*11")
    if MIN_FOUR_ODD_PRIME_PRODUCT**2 <= ORDER_THREE_FIRST_BAND_UPPER:
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
    product_cutoff = (k - 1) // MIN_FOUR_ODD_PRIME_PRODUCT
    if small_core > product_cutoff:
        raise AssertionError("small prime-power core exceeded the four-prime product cutoff")

    resolution = residual_pair_cubic_resolution(k, small_core, large_core)
    cubic_cutoff = cubic_partner_ambiguity_cutoff(k)
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
        "minimum_four_prime_core": MIN_FOUR_ODD_PRIME_PRODUCT,
        "four_prime_product_cutoff": product_cutoff,
        "cubic_partner_ambiguity_cutoff": cubic_cutoff,
        "fully_cubic_resolved": fully_resolved,
        "inside_unresolved_prime_power_budget": inside_budget,
        "unresolved_prime_power_small_label": (not fully_resolved) and inside_budget,
        "larger_base_root": int(resolution["larger_base_root"]),
        "cubic_horizon": int(resolution["cubic_horizon"]),
    }
