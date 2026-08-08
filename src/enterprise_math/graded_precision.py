"""Graded finite-precision calculus for Enterprise Math P018 stage 2.

Scale degree records how an exact quantity transports when precision is refined.
Degree-q transport multiplies by the q-th power of the precision ratio.  This
module studies exact projection fibers, Möbius shells, and the finite defects
created when nonlinear homogeneous operations are projected back to a coarser
precision.

Graded algebra itself is established mathematics.  The project-specific object
here is the interaction between degree-aware transport, many-to-one integer
projection, and bounded finite precision defects.
"""

from __future__ import annotations

from .precision import (
    precision_ratio,
    project_precision,
    scale_root_state,
    collapse_refinement_defect,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _divisors(n: int) -> list[int]:
    _require_positive("n", n)
    return [d for d in range(1, n + 1) if n % d == 0]


def _mobius(n: int) -> int:
    _require_positive("n", n)
    remaining = n
    prime_count = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            prime_count += 1
            if remaining % p == 0:
                return 0
        p += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def degree_transport(value: int, coarse: int, fine: int, degree: int) -> int:
    """Transport a degree-q coarse quantity exactly to a finer precision."""
    _require_natural("value", value)
    _require_natural("degree", degree)
    ratio = precision_ratio(coarse, fine)
    return ratio**degree * value


def degree_project(value: int, coarse: int, fine: int, degree: int) -> int:
    """Project a degree-q fine quantity by floor division by ratio**q."""
    _require_natural("value", value)
    _require_natural("degree", degree)
    ratio = precision_ratio(coarse, fine)
    return value // ratio**degree


def degree_detail(value: int, coarse: int, fine: int, degree: int) -> int:
    """Return the bounded degree-q projection fiber coordinate."""
    _require_natural("value", value)
    _require_natural("degree", degree)
    ratio = precision_ratio(coarse, fine)
    return value % ratio**degree


def degree_recompose(
    coarse_value: int,
    detail: int,
    coarse: int,
    fine: int,
    degree: int,
) -> int:
    """Recompose a degree-q fine quantity from its coarse state and detail."""
    _require_natural("coarse_value", coarse_value)
    _require_natural("detail", detail)
    _require_natural("degree", degree)
    ratio = precision_ratio(coarse, fine)
    modulus = ratio**degree
    if detail >= modulus:
        raise ValueError("detail must lie in the degree-q projection fiber")
    return modulus * coarse_value + detail


def graded_product_transport(
    left: int,
    right: int,
    coarse: int,
    fine: int,
    left_degree: int,
    right_degree: int,
) -> int:
    """Verify exact degree addition under multiplication and return the product."""
    _require_natural("left", left)
    _require_natural("right", right)
    _require_natural("left_degree", left_degree)
    _require_natural("right_degree", right_degree)
    transported_product = degree_transport(
        left * right, coarse, fine, left_degree + right_degree
    )
    separate_product = degree_transport(
        left, coarse, fine, left_degree
    ) * degree_transport(right, coarse, fine, right_degree)
    if transported_product != separate_product:
        raise AssertionError("graded multiplication transport failed")
    return transported_product


def graded_sum_transport(
    left: int, right: int, coarse: int, fine: int, degree: int
) -> int:
    """Verify exact transport of sums of equal scale degree."""
    _require_natural("left", left)
    _require_natural("right", right)
    _require_natural("degree", degree)
    transported_sum = degree_transport(left + right, coarse, fine, degree)
    separate_sum = degree_transport(left, coarse, fine, degree) + degree_transport(
        right, coarse, fine, degree
    )
    if transported_sum != separate_sum:
        raise AssertionError("graded addition transport failed")
    return transported_sum


def transported_precision_shell_degree(
    values: dict[int, int], scale: int, degree: int
) -> int:
    """Return the degree-q transported Möbius shell at one scale."""
    _require_positive("scale", scale)
    _require_natural("degree", degree)
    total = 0
    for coarse in _divisors(scale):
        if coarse not in values:
            raise ValueError("values must contain every divisor of scale")
        _require_natural("values[coarse]", values[coarse])
        ratio = scale // coarse
        total += _mobius(ratio) * ratio**degree * values[coarse]
    return total


def reconstruct_from_precision_shells_degree(
    shells: dict[int, int], scale: int, degree: int
) -> int:
    """Invert the degree-q transported Möbius precision shell."""
    _require_positive("scale", scale)
    _require_natural("degree", degree)
    total = 0
    for coarse in _divisors(scale):
        if coarse not in shells:
            raise ValueError("shells must contain every divisor of scale")
        value = shells[coarse]
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("shell values must be integers")
        ratio = scale // coarse
        total += ratio**degree * value
    return total


def monomial_value(values: list[int], exponents: list[int]) -> int:
    """Evaluate a nonnegative integer monomial."""
    if len(values) != len(exponents):
        raise ValueError("values and exponents must have the same length")
    if not values:
        raise ValueError("at least one monomial variable is required")
    result = 1
    for value, exponent in zip(values, exponents):
        _require_natural("monomial value", value)
        _require_natural("monomial exponent", exponent)
        result *= value**exponent
    return result


def monomial_precision_defect(
    fine_values: list[int],
    exponents: list[int],
    coarse: int,
    fine: int,
) -> dict[str, int | list[int]]:
    """Return the exact naturality defect of a homogeneous monomial.

    Inputs are degree-one fine states.  If q=sum(exponents), the monomial has
    scale degree q.  Projecting its fine value by ratio**q can exceed the
    monomial of the projected coarse inputs.  The excess is a finite precision
    carry/defect.
    """
    if len(fine_values) != len(exponents) or not fine_values:
        raise ValueError("fine_values and exponents must be nonempty and aligned")
    ratio = precision_ratio(coarse, fine)
    degree = sum(exponents)
    if degree <= 0:
        raise ValueError("monomial degree must be positive")

    coarse_values = [
        project_precision(value, coarse, fine) for value in fine_values
    ]
    coarse_monomial = monomial_value(coarse_values, exponents)
    fine_monomial = monomial_value(fine_values, exponents)
    recovered = fine_monomial // ratio**degree
    defect = recovered - coarse_monomial
    detail = fine_monomial % ratio**degree

    upper_corner = monomial_value(
        [value + 1 for value in coarse_values], exponents
    )
    defect_bound = upper_corner - coarse_monomial - 1
    if defect < 0 or defect > defect_bound:
        raise AssertionError("monomial precision defect escaped its coarse cell")
    if fine_monomial != ratio**degree * recovered + detail:
        raise AssertionError("degree-q monomial decomposition failed")

    return {
        "degree": degree,
        "ratio": ratio,
        "coarse_values": coarse_values,
        "coarse_monomial": coarse_monomial,
        "recovered": recovered,
        "defect": defect,
        "defect_bound": defect_bound,
        "detail": detail,
    }


def multiplication_precision_carry(
    left: int, right: int, coarse: int, fine: int
) -> dict[str, int]:
    """Return the exact degree-two carry created by multiplication."""
    data = monomial_precision_defect([left, right], [1, 1], coarse, fine)
    ratio = int(data["ratio"])
    left_coarse, left_detail = divmod(left, ratio)
    right_coarse, right_detail = divmod(right, ratio)
    explicit = (
        ratio * left_coarse * right_detail
        + ratio * right_coarse * left_detail
        + left_detail * right_detail
    ) // ratio**2
    if explicit != data["defect"]:
        raise AssertionError("explicit multiplication carry formula failed")
    expected_bound = left_coarse + right_coarse
    if data["defect_bound"] != expected_bound:
        raise AssertionError("multiplication carry bound failed")
    return {
        "left_coarse": left_coarse,
        "right_coarse": right_coarse,
        "left_detail": left_detail,
        "right_detail": right_detail,
        "carry": int(data["defect"]),
        "carry_bound": expected_bound,
        "product_detail": int(data["detail"]),
    }


def power_precision_carry(
    value: int, power: int, coarse: int, fine: int
) -> dict[str, int]:
    """Return the degree-p precision carry of the map x -> x**p."""
    _require_positive("power", power)
    data = monomial_precision_defect([value], [power], coarse, fine)
    ratio = int(data["ratio"])
    coarse_value, local_detail = divmod(value, ratio)
    expected_bound = (coarse_value + 1) ** power - coarse_value**power - 1
    if data["defect_bound"] != expected_bound:
        raise AssertionError("power precision carry bound failed")
    return {
        "coarse_value": coarse_value,
        "local_detail": local_detail,
        "carry": int(data["defect"]),
        "carry_bound": expected_bound,
        "power_detail": int(data["detail"]),
    }


def monomial_recovery_profile(
    finest_values: list[int],
    exponents: list[int],
    base_scale: int,
    refinement_scales: list[int],
) -> list[int]:
    """Return a monotone coarse recovery profile for a monomial.

    ``finest_values`` live at the last scale in ``refinement_scales``.  They are
    projected to every intermediate scale, the monomial is evaluated there,
    and the degree-q result is projected to ``base_scale``.
    """
    _require_positive("base_scale", base_scale)
    if not refinement_scales or refinement_scales[0] != base_scale:
        raise ValueError("refinement_scales must start at base_scale")
    if len(finest_values) != len(exponents) or not finest_values:
        raise ValueError("finest_values and exponents must be nonempty and aligned")
    degree = sum(exponents)
    if degree <= 0:
        raise ValueError("monomial degree must be positive")

    finest_scale = refinement_scales[-1]
    previous_scale = base_scale
    profile: list[int] = []
    last: int | None = None
    for scale in refinement_scales:
        precision_ratio(previous_scale, scale)
        precision_ratio(scale, finest_scale)
        current_values = [
            project_precision(value, scale, finest_scale) for value in finest_values
        ]
        current_monomial = monomial_value(current_values, exponents)
        recovered = degree_project(
            current_monomial, base_scale, scale, degree
        )
        if last is not None and recovered < last:
            raise AssertionError("monomial recovery must be monotone under refinement")
        profile.append(recovered)
        last = recovered
        previous_scale = scale
    return profile


def root_collapse_is_power_carry(
    n: int, power: int, coarse: int, fine: int
) -> dict[str, int]:
    """Identify Stage-1 collapse/refinement defect with a power precision carry."""
    _require_natural("n", n)
    _require_positive("power", power)
    coarse_root = scale_root_state(n, power, coarse)
    fine_root = scale_root_state(n, power, fine)
    power_data = power_precision_carry(fine_root, power, coarse, fine)
    if power_data["coarse_value"] != coarse_root:
        raise AssertionError("root precision compatibility failed")
    collapse_defect = collapse_refinement_defect(n, power, coarse, fine)
    if power_data["carry"] != collapse_defect:
        raise AssertionError("collapse defect is not the root power carry")
    return {
        "coarse_root": coarse_root,
        "fine_root": fine_root,
        "root_detail": int(power_data["local_detail"]),
        "collapse_defect": collapse_defect,
        "power_carry_bound": int(power_data["carry_bound"]),
    }
