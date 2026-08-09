"""Exact quotient transport of square-collapse basins.

The core result is finite and integer-only: dividing every state in one square
basin by an integer d>=2 can move the square-root index to only two adjacent
values, and the new root index is strictly below the original basin index.

The follow-up path results use only exact Euclidean division: iterated floor
quotients equal one quotient by the product divisor, so repeated factor
extraction does not multiply the number of possible final square-root indices.

The threshold layer makes the remaining binary choice exact: for each divisor,
the upper root index turns on at one integer threshold inside (or beyond) the
original basin.  A family of quotient-root bits is therefore driven by one
shared basin offset rather than by independent binary choices.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_nat(name: str, value: int, *, minimum: int = 0) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def square_basin_quotient_transport(k: int, divisor: int, n: int) -> dict[str, int]:
    """Transport one state from the k-th square basin through floor division."""
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)
    _require_nat("n", n)
    lower = k * k
    upper_exclusive = (k + 1) * (k + 1)
    if not lower <= n < upper_exclusive:
        raise ValueError("n must lie in the canonical square basin [k^2,(k+1)^2)")

    base_quotient = lower // divisor
    base_root = integer_nth_root(base_quotient, 2)
    quotient = n // divisor
    quotient_root = integer_nth_root(quotient, 2)

    if base_root >= k:
        raise AssertionError("quotient root scale did not strictly descend")
    if quotient_root not in (base_root, base_root + 1):
        raise AssertionError("square basin divided into more than two root-index basins")

    return {
        "k": k,
        "divisor": divisor,
        "n": n,
        "base_quotient": base_quotient,
        "base_root": base_root,
        "quotient": quotient,
        "quotient_root": quotient_root,
    }


def square_basin_quotient_window(k: int, divisor: int) -> dict[str, int]:
    """Return the complete quotient image of [k^2,(k+1)^2) under floor division."""
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)

    q_min = (k * k) // divisor
    q_max = (((k + 1) * (k + 1)) - 1) // divisor
    base_root = integer_nth_root(q_min, 2)
    max_root = integer_nth_root(q_max, 2)

    if base_root >= k:
        raise AssertionError("quotient window did not strictly descend in root scale")
    if max_root not in (base_root, base_root + 1):
        raise AssertionError("quotient window meets more than two square-root indices")

    return {
        "k": k,
        "divisor": divisor,
        "q_min": q_min,
        "q_max": q_max,
        "base_root": base_root,
        "max_root": max_root,
    }


def open_divisible_cofactor_window(k: int, divisor: int) -> dict[str, int]:
    """Return the quotient window for divisible states strictly inside the square basin."""
    data = square_basin_quotient_window(k, divisor)
    q_min_open = (k * k) // divisor + 1
    q_max = data["q_max"]
    base_root = data["base_root"]

    if q_min_open <= q_max:
        if not base_root * base_root < q_min_open:
            raise AssertionError("open cofactor window did not leave the lower square boundary")
        if not q_max < (base_root + 2) * (base_root + 2):
            raise AssertionError("open cofactor window crossed a third square basin")

    return {
        **data,
        "q_min_open": q_min_open,
        "nonempty": int(q_min_open <= q_max),
    }


def iterated_quotient_flatness(n: int, divisors: list[int]) -> dict[str, object]:
    """Verify that a quotient path depends only on the product divisor."""
    _require_nat("n", n)
    if not divisors:
        raise ValueError("divisors must be a nonempty list")

    value = n
    product = 1
    states = [n]
    for index, divisor in enumerate(divisors):
        _require_nat(f"divisors[{index}]", divisor, minimum=2)
        product *= divisor
        value //= divisor
        states.append(value)

    direct = n // product
    if value != direct:
        raise AssertionError("iterated floor quotient differs from quotient by product divisor")

    return {
        "n": n,
        "divisors": tuple(divisors),
        "divisor_product": product,
        "path_states": tuple(states),
        "iterated_quotient": value,
        "direct_quotient": direct,
    }


def square_basin_iterated_quotient_transport(
    k: int, divisors: list[int], n: int
) -> dict[str, object]:
    """Collapse an iterated quotient path to one two-basin transport."""
    flat = iterated_quotient_flatness(n, divisors)
    product = int(flat["divisor_product"])
    transported = square_basin_quotient_transport(k, product, n)
    if int(flat["iterated_quotient"]) != transported["quotient"]:
        raise AssertionError("flat quotient path disagrees with direct basin transport")
    return {
        **flat,
        "k": k,
        "base_root": transported["base_root"],
        "quotient_root": transported["quotient_root"],
    }


def strict_square_root_descent(k: int, divisor: int, n: int) -> dict[str, int]:
    """Verify strict descent of the actual quotient root for k>=3."""
    _require_nat("k", k, minimum=3)
    data = square_basin_quotient_transport(k, divisor, n)
    if data["quotient"] >= k * k:
        raise AssertionError("quotient did not fall below the original square boundary")
    if data["quotient_root"] >= k:
        raise AssertionError("actual quotient square-root index did not strictly descend")
    return data


def quotient_root_threshold(k: int, divisor: int) -> dict[str, int]:
    """Return the unique state/offset threshold for the upper T110 root branch.

    Let j=R_2(floor(k^2/d)).  The upper root j+1 occurs exactly when

        n >= d*(j+1)^2.

    Relative to the lower square boundary k^2, the same condition is

        s=n-k^2 >= tau,
        tau=d*(j+1)^2-k^2.

    The threshold is positive.  It may exceed 2k, in which case the upper branch
    is never reached inside the k-th square basin.
    """
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)
    lower = k * k
    base_quotient = lower // divisor
    base_root = integer_nth_root(base_quotient, 2)
    state_threshold = divisor * (base_root + 1) * (base_root + 1)
    if state_threshold <= lower:
        raise AssertionError("upper root threshold did not lie above the lower square boundary")
    offset_threshold = state_threshold - lower
    return {
        "k": k,
        "divisor": divisor,
        "base_root": base_root,
        "state_threshold": state_threshold,
        "offset_threshold": offset_threshold,
    }


def square_basin_offset_root_response(
    k: int, divisor: int, offset: int
) -> dict[str, int]:
    """Evaluate the exact one-threshold root response at basin offset ``offset``.

    For 0<=offset<=2k, n=k^2+offset lies in the complete half-open square basin.
    The quotient root is base_root plus the single threshold bit

        1[offset >= offset_threshold].
    """
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)
    _require_nat("offset", offset)
    if offset > 2 * k:
        raise ValueError("offset must satisfy 0 <= offset <= 2k")

    threshold = quotient_root_threshold(k, divisor)
    n = k * k + offset
    transported = square_basin_quotient_transport(k, divisor, n)
    upper_bit = int(offset >= threshold["offset_threshold"])
    predicted_root = threshold["base_root"] + upper_bit
    if transported["quotient_root"] != predicted_root:
        raise AssertionError("quotient root disagrees with the one-threshold response")

    return {
        **transported,
        "offset": offset,
        "state_threshold": threshold["state_threshold"],
        "offset_threshold": threshold["offset_threshold"],
        "upper_bit": upper_bit,
        "predicted_root": predicted_root,
    }


def quotient_root_threshold_pattern(
    k: int, divisors: list[int], offset: int
) -> dict[str, object]:
    """Return the shared-offset threshold bits for several quotient divisors.

    Every bit is a comparison of the *same* basin offset against one divisor's
    threshold.  Thus for a fixed divisor family the vector cannot realize 2^h
    unrelated choices as the basin state moves; coordinates flip only when the
    common offset crosses their thresholds.
    """
    _require_nat("k", k, minimum=1)
    _require_nat("offset", offset)
    if offset > 2 * k:
        raise ValueError("offset must satisfy 0 <= offset <= 2k")
    if not divisors:
        raise ValueError("divisors must be a nonempty list")

    responses = [square_basin_offset_root_response(k, d, offset) for d in divisors]
    return {
        "k": k,
        "offset": offset,
        "divisors": tuple(divisors),
        "thresholds": tuple(r["offset_threshold"] for r in responses),
        "upper_bits": tuple(r["upper_bit"] for r in responses),
        "quotient_roots": tuple(r["quotient_root"] for r in responses),
    }
