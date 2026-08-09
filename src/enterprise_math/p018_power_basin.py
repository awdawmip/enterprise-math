"""All-power quotient transport for Enterprise Math P018.

For a positive power p, the integer-root basin

    k**p <= n < (k+1)**p

is transported by every nontrivial floor quotient n -> n//d into at most two
adjacent p-th-root basins. The proof is integer-only and extends the square case
already used by P018.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_nat(name: str, value: int, *, minimum: int = 0) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def power_basin_quotient_window(power: int, k: int, divisor: int) -> dict[str, int]:
    """Return the exact quotient/root window of one p-th-power basin.

    With j = R_p(k**p // divisor), every quotient state from the k-th
    p-power basin has p-root index j or j+1. The returned ``split`` flag is one
    exactly when both root indices occur.
    """
    _require_nat("power", power, minimum=1)
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)

    lower = k**power
    upper_exclusive = (k + 1) ** power
    q_min = lower // divisor
    q_max = (upper_exclusive - 1) // divisor
    base_root = integer_nth_root(q_min, power)
    max_root = integer_nth_root(q_max, power)

    if base_root >= k:
        raise AssertionError("nontrivial quotient did not lower the base root index")
    if max_root not in (base_root, base_root + 1):
        raise AssertionError("one power basin reached more than two target root indices")

    split_criterion = divisor * (base_root + 1) ** power <= upper_exclusive - 1
    if split_criterion != (max_root == base_root + 1):
        raise AssertionError("exact split criterion disagrees with quotient window")

    strict_descent = upper_exclusive <= divisor * lower
    if strict_descent != (max_root < k):
        raise AssertionError("strict root-descent criterion disagrees with quotient window")

    return {
        "power": power,
        "k": k,
        "divisor": divisor,
        "q_min": q_min,
        "q_max": q_max,
        "base_root": base_root,
        "max_root": max_root,
        "split": int(split_criterion),
        "strict_root_descent": int(strict_descent),
    }


def whole_basin_strict_root_descent(power: int, k: int, divisor: int) -> bool:
    """Exact criterion that every quotient state has p-root strictly below k.

    The criterion is (k+1)**p <= divisor*k**p.
    """
    return bool(power_basin_quotient_window(power, k, divisor)["strict_root_descent"])


def power_basin_quotient_transport(power: int, k: int, divisor: int, n: int) -> dict[str, int]:
    """Transport one state and expose its binary root-basin branch."""
    _require_nat("power", power, minimum=1)
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)
    _require_nat("n", n)
    lower = k**power
    upper_exclusive = (k + 1) ** power
    if not lower <= n < upper_exclusive:
        raise ValueError("n must lie in [k**power,(k+1)**power)")

    window = power_basin_quotient_window(power, k, divisor)
    quotient = n // divisor
    quotient_root = integer_nth_root(quotient, power)
    base_root = window["base_root"]
    if quotient_root not in (base_root, base_root + 1):
        raise AssertionError("quotient root escaped the two-basin window")

    return {
        **window,
        "n": n,
        "quotient": quotient,
        "quotient_root": quotient_root,
        "upper_bit": quotient_root - base_root,
    }


def iterated_power_basin_quotient_transport(
    power: int, k: int, divisors: list[int], n: int
) -> dict[str, object]:
    """Flatten a finite quotient path and apply the all-power two-basin theorem."""
    if not divisors:
        raise ValueError("divisors must be nonempty")
    product = 1
    value = n
    path = [n]
    for index, divisor in enumerate(divisors):
        _require_nat(f"divisors[{index}]", divisor, minimum=2)
        product *= divisor
        value //= divisor
        path.append(value)
    direct = n // product
    if value != direct:
        raise AssertionError("iterated quotient did not flatten to the product divisor")

    transported = power_basin_quotient_transport(power, k, product, n)
    if transported["quotient"] != direct:
        raise AssertionError("direct all-power transport disagrees with quotient path")
    return {
        **transported,
        "divisors": tuple(divisors),
        "divisor_product": product,
        "path_states": tuple(path),
    }
