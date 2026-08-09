"""Exact quotient transport of square-collapse basins.

The core results are finite and integer-only.  Division by any integer d>=2
maps one square basin to at most two adjacent quotient-root indices.  Repeated
floor divisions depend only on the total divisor product, so intermediate
factorizations do not create an exponential family of final root scales.  From
k>=3, the actual quotient root index strictly decreases after every nontrivial
division.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_nat(name: str, value: int, *, minimum: int = 0) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def square_basin_quotient_transport(k: int, divisor: int, n: int) -> dict[str, int]:
    """Transport one state from the k-th square basin through floor division.

    Preconditions:
        k >= 1,
        divisor >= 2,
        k^2 <= n < (k+1)^2.

    If j=R_2(floor(k^2/divisor)), then the returned quotient root is exactly
    j or j+1, and j<k.
    """
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
    """Return the quotient window for divisible states strictly inside the square basin.

    This is the P017 specialization when ``divisor`` is the chosen least prime:

        floor(k^2/d)+1 <= q <= floor(((k+1)^2-1)/d).

    Every such q satisfies j^2 < q < (j+2)^2 for
    j=R_2(floor(k^2/d)).
    """
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


def iterated_floor_division(n: int, divisors: list[int]) -> dict[str, object]:
    """Apply floor division successively and compare with one division by the product.

    Each divisor must be at least two.  Exact integer division is path-flat:

        (...((n//d1)//d2)...//dh) == n//(d1*d2*...*dh).
    """
    _require_nat("n", n)
    if not divisors:
        raise ValueError("divisors must be nonempty")

    value = n
    product = 1
    history = [n]
    for index, divisor in enumerate(divisors):
        _require_nat(f"divisors[{index}]", divisor, minimum=2)
        value //= divisor
        product *= divisor
        history.append(value)

    direct = n // product
    if value != direct:
        raise AssertionError("iterated floor division depends on factorization path")

    return {
        "n": n,
        "divisors": tuple(divisors),
        "product": product,
        "history": tuple(history),
        "iterated_quotient": value,
        "direct_quotient": direct,
    }


def square_basin_iterated_quotient_transport(
    k: int, divisors: list[int], n: int
) -> dict[str, object]:
    """Transport a square-basin state through a whole quotient path.

    The final quotient and final root index depend only on the product of the
    divisors.  Consequently the final square-root index still has only the two
    T110 candidates attached to that total divisor, independent of how it was
    factorized into intermediate division steps.
    """
    path = iterated_floor_division(n, divisors)
    direct = square_basin_quotient_transport(k, int(path["product"]), n)
    final_quotient = int(path["iterated_quotient"])
    final_root = integer_nth_root(final_quotient, 2)

    if final_quotient != direct["quotient"]:
        raise AssertionError("path quotient and total-divisor quotient disagree")
    if final_root != direct["quotient_root"]:
        raise AssertionError("path root and total-divisor root disagree")

    return {
        **path,
        "k": k,
        "base_root": direct["base_root"],
        "final_root": final_root,
    }


def square_basin_actual_root_descent(k: int, divisor: int, n: int) -> dict[str, int]:
    """Verify strict descent of the actual quotient-root index for k>=3.

    Since d>=2 and n<(k+1)^2, for k>=3 one has n/d < k^2.  Therefore
    R_2(floor(n/d)) < k.  The finite basin indices k=1,2 are deliberately left
    as base cases rather than hidden in an asymptotic argument.
    """
    _require_nat("k", k, minimum=3)
    data = square_basin_quotient_transport(k, divisor, n)
    if data["quotient_root"] >= k:
        raise AssertionError("actual quotient-root scale did not strictly descend")
    return data
