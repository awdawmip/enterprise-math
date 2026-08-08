"""Integer-only finite-precision calculus for Enterprise Math P018.

Precision is represented by positive integer scale factors ordered by divisibility.
For coarse | fine, projection is exact integer division by fine/coarse and the
lost fiber coordinate is an explicit bounded detail, not a hidden fraction.

This module contains finite identities only.  It introduces no real-number
completion and no limiting process.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def precision_ratio(coarse: int, fine: int) -> int:
    """Return fine/coarse for comparable precision factors."""
    _require_positive("coarse", coarse)
    _require_positive("fine", fine)
    if fine % coarse != 0:
        raise ValueError("coarse precision must divide fine precision")
    return fine // coarse


def project_precision(value: int, coarse: int, fine: int) -> int:
    """Project a fine integer state to a comparable coarser precision."""
    _require_natural("value", value)
    return value // precision_ratio(coarse, fine)


def precision_detail(value: int, coarse: int, fine: int) -> int:
    """Return the exact bounded fiber coordinate discarded by projection."""
    _require_natural("value", value)
    return value % precision_ratio(coarse, fine)


def recompose_precision(
    coarse_value: int, detail: int, coarse: int, fine: int
) -> int:
    """Recompose a fine state from one coarse state and one valid detail."""
    _require_natural("coarse_value", coarse_value)
    _require_natural("detail", detail)
    ratio = precision_ratio(coarse, fine)
    if detail >= ratio:
        raise ValueError("detail must lie in the projection fiber range")
    return ratio * coarse_value + detail


def nested_detail_identity(value: int, low: int, middle: int, high: int) -> tuple[int, int, int]:
    """Return the two local details and their exact low-to-high composition.

    If low | middle | high, write r=middle/low and s=high/middle.  For a high
    state x, if u is the detail of x//s from middle to low and v is the detail
    from high to middle, then the direct low-to-high detail is s*u+v.
    """
    _require_natural("value", value)
    r = precision_ratio(low, middle)
    s = precision_ratio(middle, high)
    _ = r
    middle_value = project_precision(value, middle, high)
    low_middle_detail = precision_detail(middle_value, low, middle)
    middle_high_detail = precision_detail(value, middle, high)
    direct_detail = precision_detail(value, low, high)
    composed = s * low_middle_detail + middle_high_detail
    if direct_detail != composed:
        raise AssertionError("nested precision detail identity failed")
    return low_middle_detail, middle_high_detail, direct_detail


def coarse_order_status(left: int, right: int, coarse: int, fine: int) -> int:
    """Return -1, 0, +1 according to the coarse fibers of two fine states.

    A nonzero result is already a proof of the same strict order at every finer
    refinement of these concrete states.  Zero means that the coarse scale has
    not yet separated the two states.
    """
    _require_natural("left", left)
    _require_natural("right", right)
    left_coarse = project_precision(left, coarse, fine)
    right_coarse = project_precision(right, coarse, fine)
    if left_coarse < right_coarse:
        return -1
    if left_coarse > right_coarse:
        return 1
    return 0


def addition_carry(left: int, right: int, coarse: int, fine: int) -> tuple[int, int, int]:
    """Return (coarse_sum, carry, fine_detail) for exact addition.

    With x=r*a+u and y=r*b+v,
        x+y = r*(a+b+carry) + detail,
    where carry=(u+v)//r is binary.
    """
    _require_natural("left", left)
    _require_natural("right", right)
    ratio = precision_ratio(coarse, fine)
    a, u = divmod(left, ratio)
    b, v = divmod(right, ratio)
    carry, detail = divmod(u + v, ratio)
    coarse_sum = a + b + carry
    if carry not in (0, 1):
        raise AssertionError("two-input precision carry must be binary")
    if left + right != ratio * coarse_sum + detail:
        raise AssertionError("addition carry decomposition failed")
    return coarse_sum, carry, detail


def subtraction_borrow(left: int, right: int, coarse: int, fine: int) -> tuple[int, int, int]:
    """Return (coarse_difference, borrow, detail) for left>=right."""
    _require_natural("left", left)
    _require_natural("right", right)
    if left < right:
        raise ValueError("subtraction_borrow requires left >= right")
    ratio = precision_ratio(coarse, fine)
    a, u = divmod(left, ratio)
    b, v = divmod(right, ratio)
    borrow = int(u < v)
    coarse_difference = a - b - borrow
    detail = u - v + borrow * ratio
    if coarse_difference < 0 or not 0 <= detail < ratio:
        raise AssertionError("invalid borrow decomposition")
    if left - right != ratio * coarse_difference + detail:
        raise AssertionError("subtraction borrow decomposition failed")
    return coarse_difference, borrow, detail


def precision_chain_decomposition(value: int, scales: list[int]) -> tuple[int, list[int]]:
    """Return the base state and mixed-radix details along a divisibility chain.

    scales must satisfy d_0 | d_1 | ... | d_n.  The returned details delta_i
    obey x_i=(d_i/d_{i-1})*x_{i-1}+delta_i for the successive projections x_i
    of the final state.
    """
    _require_natural("value", value)
    if not scales:
        raise ValueError("at least one precision scale is required")
    for scale in scales:
        _require_positive("scale", scale)
    for low, high in zip(scales, scales[1:]):
        precision_ratio(low, high)

    finest = scales[-1]
    states = [project_precision(value, scale, finest) for scale in scales]
    details: list[int] = []
    for i in range(1, len(scales)):
        ratio = scales[i] // scales[i - 1]
        detail = states[i] - ratio * states[i - 1]
        if not 0 <= detail < ratio:
            raise AssertionError("chain detail escaped its mixed-radix range")
        details.append(detail)

    reconstructed = states[0] * (finest // scales[0])
    for i, detail in enumerate(details, start=1):
        reconstructed += (finest // scales[i]) * detail
    if reconstructed != value:
        raise AssertionError("precision-chain telescoping failed")
    return states[0], details


def _divisors(n: int) -> list[int]:
    _require_positive("n", n)
    return [d for d in range(1, n + 1) if n % d == 0]


def _mobius(n: int) -> int:
    """Elementary integer Möbius function for positive n."""
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
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def transported_precision_shell(values: dict[int, int], scale: int) -> int:
    """Return the scale-aware Möbius shell at one precision factor.

    All coarse values are first transported to ``scale`` by multiplication by
    scale/coarse, then ordinary divisor-poset Möbius inversion is applied.
    """
    _require_positive("scale", scale)
    total = 0
    for coarse in _divisors(scale):
        if coarse not in values:
            raise ValueError("values must contain every divisor of scale")
        _require_natural("values[coarse]", values[coarse])
        total += _mobius(scale // coarse) * (scale // coarse) * values[coarse]
    return total


def reconstruct_from_precision_shells(shells: dict[int, int], scale: int) -> int:
    """Invert transported_precision_shell on the divisor lattice."""
    _require_positive("scale", scale)
    total = 0
    for coarse in _divisors(scale):
        if coarse not in shells:
            raise ValueError("shells must contain every divisor of scale")
        if isinstance(shells[coarse], bool) or not isinstance(shells[coarse], int):
            raise ValueError("shell values must be integers")
        total += (scale // coarse) * shells[coarse]
    return total


def scale_root_state(n: int, power: int, scale: int) -> int:
    """P005-compatible root state S_(p,d)(n)=R_p(n*d^p)."""
    _require_natural("n", n)
    _require_positive("power", power)
    _require_positive("scale", scale)
    return integer_nth_root(n * scale**power, power)


def root_precision_detail(n: int, power: int, coarse: int, fine: int) -> int:
    """Return eta where S_(p,fine)=ratio*S_(p,coarse)+eta."""
    ratio = precision_ratio(coarse, fine)
    coarse_root = scale_root_state(n, power, coarse)
    fine_root = scale_root_state(n, power, fine)
    detail = fine_root - ratio * coarse_root
    if not 0 <= detail < ratio:
        raise AssertionError("root precision detail escaped the projection fiber")
    return detail


def scale_collapse_state(n: int, power: int, scale: int) -> int:
    """Return the p-th-power collapse state at one scale."""
    root = scale_root_state(n, power, scale)
    return root**power


def projected_refined_collapse(n: int, power: int, coarse: int, fine: int) -> int:
    """Collapse at fine precision, then project the degree-p state to coarse."""
    ratio = precision_ratio(coarse, fine)
    fine_collapse = scale_collapse_state(n, power, fine)
    return fine_collapse // ratio**power


def collapse_refinement_defect(n: int, power: int, coarse: int, fine: int) -> int:
    """Return the exact nonnegative defect between fine-then-project and coarse collapse.

    If k=S_(p,coarse)(n), the defect always lies in
        0 .. ((k+1)^p-k^p)-1,
    i.e. it is an exact coordinate inside the coarse collapse basin.
    """
    coarse_collapse = scale_collapse_state(n, power, coarse)
    refined = projected_refined_collapse(n, power, coarse, fine)
    defect = refined - coarse_collapse
    k = scale_root_state(n, power, coarse)
    basin_gap = (k + 1) ** power - k**power
    if not 0 <= defect <= basin_gap - 1:
        raise AssertionError("collapse refinement defect escaped the coarse basin")
    return defect


def collapse_recovery_profile(
    n: int, power: int, base_scale: int, refinement_scales: list[int]
) -> list[int]:
    """Return coarse-projected collapse states along an increasing precision chain.

    Each listed scale must be a multiple of base_scale and divide the next one.
    The returned profile is exact and nondecreasing.
    """
    _require_positive("base_scale", base_scale)
    if not refinement_scales:
        raise ValueError("at least one refinement scale is required")
    previous = base_scale
    profile: list[int] = []
    last: int | None = None
    for scale in refinement_scales:
        precision_ratio(base_scale, scale)
        precision_ratio(previous, scale)
        value = projected_refined_collapse(n, power, base_scale, scale)
        if last is not None and value < last:
            raise AssertionError("collapse recovery must be monotone under refinement")
        profile.append(value)
        last = value
        previous = scale
    return profile
