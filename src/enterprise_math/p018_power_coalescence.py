"""Discovery-stage P018 all-power quotient-root coalescence algebra.

There are two dual finite-precision views of integer quotient transport.

* Canonical T110/APQ fixes a denominator and varies the source state across one
  power basin: only two adjacent target root indices are possible.
* This module also fixes the state and a positive target root and varies the
  *total denominator*: the entire denominator fiber is one exact integer
  interval.

For ``t>0`` and root exponent ``r>=1``,

    R_r(floor(n/d)) = t

is equivalent to

    floor(n/(t+1)^r) < d <= floor(n/t^r).

Thus the full positive-denominator fiber is

    F_{n,r}(t)
      = [ floor(n/(t+1)^r)+1 , floor(n/t^r) ]

with exact cardinality

    M_{n,r}(t)
      = floor(n/t^r) - floor(n/(t+1)^r).

This exact interval is the natural coalescence cell in total-divisor space.  A
factor-extraction path is first flattened by T111 to its total divisor and then
lands in one such cell.

The sharp graded law bounds the diameter/capacity of this exact fiber.  If two
fiber labels ``2<=d<e`` share root ``t`` then

    (e-d) * t^(r+1) < r*n.

For a source basin ``k^p<=n<(k+1)^p`` this gives

    (e-d) * t^(r+1) < r*(k+1)^p.

Hence any set of ``m`` distinct nontrivial total divisors coalescing at a
positive root obeys

    (m-1) * t^(r+1) < r*(k+1)^p,

so

    m <= 1 + floor((r*(k+1)^p - 1) / t^(r+1)).

The exact two-divisor horizon is

    H_{p,r}(k)=R_{r+1}(r*(k+1)^p-1),

and the collision exponent is ``gamma(p,r)=p/(r+1)``.  The phase boundary is
``r+1>p`` (sublinear), ``r+1=p`` (linear), ``r+1<p`` (no forced contraction).

The capacity law is asymptotically sharp at every multiplicity scale.  For gap
``g>=1`` and parameter ``a>=2``, put

    d=g*a, e=g*(a+1), t=r*a-1, n=e*t^r.

The endpoint labels share root t; monotonicity makes every integer label in
[d,e] share it, producing exactly ``g+1`` consecutive coalescing labels, while

    g*t^(r+1)/(r*n)=(r*a-1)/(r*(a+1))->1.

For fixed source exponent p and k=R_p(n), this also realizes the exponent
``p/(r+1)`` asymptotically.  Classical floor-division order and Bernoulli /
difference-of-powers inequalities are prior art; the candidate project result
is their exact finite-precision coalescence packaging and recursion interface.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def coalescence_root_constant(root_exp: int) -> int:
    """Return the sharp gap-one cross-divisor constant C_r=r."""
    _require_int("root_exp", root_exp)
    if root_exp < 1:
        raise ValueError("root_exp must be positive")
    return root_exp


def total_divisor_root_fiber(n: int, root_exp: int, target_root: int) -> dict[str, object]:
    """Return the exact positive-denominator fiber for one positive root.

    For t>0,

        R_r(n//d)=t
        iff
        floor(n/(t+1)^r) < d <= floor(n/t^r).

    The returned tuple contains every positive denominator in the fiber.  For
    factor-extraction paths one normally consumes the subfiber ``d>=2`` and may
    further intersect with actual divisors of ``n``.
    """
    for name, value in (
        ("n", n),
        ("root_exp", root_exp),
        ("target_root", target_root),
    ):
        _require_int(name, value)
    if n < 0 or root_exp < 1 or target_root < 1:
        raise ValueError("n must be nonnegative; root_exp/target_root positive")

    lower_exclusive = n // (target_root + 1) ** root_exp
    upper_inclusive = n // target_root**root_exp
    if upper_inclusive < lower_exclusive:
        raise AssertionError("quotient-root fiber endpoints reversed")
    labels = tuple(range(lower_exclusive + 1, upper_inclusive + 1))
    for divisor in labels:
        if integer_nth_root(n // divisor, root_exp) != target_root:
            raise AssertionError("exact divisor fiber admitted a wrong root")
    if lower_exclusive >= 1:
        if integer_nth_root(n // lower_exclusive, root_exp) == target_root:
            raise AssertionError("exclusive lower neighbor remained in root fiber")
    if integer_nth_root(n // (upper_inclusive + 1), root_exp) == target_root:
        raise AssertionError("upper neighbor remained in root fiber")

    return {
        "n": n,
        "root_exp": root_exp,
        "target_root": target_root,
        "lower_exclusive": lower_exclusive,
        "upper_inclusive": upper_inclusive,
        "positive_divisor_labels": labels,
        "positive_capacity": len(labels),
        "nontrivial_divisor_labels": tuple(d for d in labels if d >= 2),
        "nontrivial_capacity": sum(d >= 2 for d in labels),
    }


def exact_root_fiber_capacity(n: int, root_exp: int, target_root: int) -> int:
    """Return floor(n/t^r)-floor(n/(t+1)^r) for t>0."""
    data = total_divisor_root_fiber(n, root_exp, target_root)
    expected = int(data["upper_inclusive"]) - int(data["lower_exclusive"])
    if expected != data["positive_capacity"]:
        raise AssertionError("exact root-fiber capacity identity failed")
    return expected


def cross_root_coalescence_horizon(
    k: int, source_exp: int, root_exp: int
) -> int:
    """Return H_{p,r}(k)=R_{r+1}(r*(k+1)^p-1)."""
    for name, value in (
        ("k", k),
        ("source_exp", source_exp),
        ("root_exp", root_exp),
    ):
        _require_int(name, value)
    if k < 1 or source_exp < 1 or root_exp < 1:
        raise ValueError("k and both exponents must be positive")
    argument = root_exp * (k + 1) ** source_exp - 1
    return integer_nth_root(argument, root_exp + 1)


def power_basin_cross_root(
    k: int,
    n: int,
    source_exp: int,
    root_exp: int,
    divisor: int,
) -> int:
    """Return R_r(floor(n/d)) for n in the complete p-power basin at k."""
    for name, value in (
        ("k", k),
        ("n", n),
        ("source_exp", source_exp),
        ("root_exp", root_exp),
        ("divisor", divisor),
    ):
        _require_int(name, value)
    if k < 1 or source_exp < 1 or root_exp < 1:
        raise ValueError("k and both exponents must be positive")
    if not k**source_exp <= n < (k + 1) ** source_exp:
        raise ValueError("n must lie in the complete source power basin")
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    return integer_nth_root(n // divisor, root_exp)


def cross_root_divisor_collision(
    k: int,
    n: int,
    source_exp: int,
    root_exp: int,
    left: int,
    right: int,
) -> dict[str, object]:
    """Validate the sharp divisor-span collision law.

    If the quotient roots coincide at t and ``g=right-left``, verify

        g * t^(r+1) < r*(k+1)^p.

    The proof-scale inequality is ``g*(t+1)<r*right``.
    """
    for name, value in (("left", left), ("right", right)):
        _require_int(name, value)
    if not 2 <= left < right:
        raise ValueError("require 2 <= left < right")

    left_root = power_basin_cross_root(k, n, source_exp, root_exp, left)
    right_root = power_basin_cross_root(k, n, source_exp, root_exp, right)
    horizon = cross_root_coalescence_horizon(k, source_exp, root_exp)
    gap = right - left
    result: dict[str, object] = {
        "k": k,
        "n": n,
        "source_exp": source_exp,
        "root_exp": root_exp,
        "left": left,
        "right": right,
        "divisor_gap": gap,
        "left_root": left_root,
        "right_root": right_root,
        "coalesces": left_root == right_root,
        "coalescence_horizon": horizon,
        "asymptotic_exponent_numerator": source_exp,
        "asymptotic_exponent_denominator": root_exp + 1,
    }
    if left_root != right_root:
        return result

    t = left_root
    if right * t**root_exp > n:
        raise AssertionError("common root lower interval failed")
    if n >= left * (t + 1) ** root_exp:
        raise AssertionError("common root upper interval failed")

    delta = (t + 1) ** root_exp - t**root_exp
    if gap * t**root_exp >= left * delta:
        raise AssertionError("divisor-gap difference inequality failed")
    if gap * (t + 1) >= root_exp * right:
        raise AssertionError("collision violated g*(t+1)<r*e")

    argument_exclusive = root_exp * (k + 1) ** source_exp
    if t > 0:
        if gap * t ** (root_exp + 1) >= argument_exclusive:
            raise AssertionError("collision escaped the graded all-power bound")
        if gap == 1 and t > horizon:
            raise AssertionError("gap-one collision exceeded H_{p,r}(k)")

    return {
        **result,
        "common_root": t,
        "root_order_constant": root_exp,
        "root_increment": delta,
        "collision_power": t ** (root_exp + 1),
        "weighted_collision_power": gap * t ** (root_exp + 1),
        "horizon_argument": argument_exclusive - 1,
        "sublinear_regime": root_exp + 1 > source_exp,
        "linear_boundary": root_exp + 1 == source_exp,
    }


def coalescence_multiplicity_cap(
    k: int,
    source_exp: int,
    root_exp: int,
    target_root: int,
) -> int | None:
    """Return the graded cap for a positive target root.

    For t>0, any set of distinct nontrivial total denominators coalescing at t
    has size at most

        1 + floor((r*(k+1)^p - 1) / t^(r+1)).

    Root zero is the terminal degenerate cell and has no finite cap from this
    inequality, so the function returns ``None`` there.
    """
    for name, value in (
        ("k", k),
        ("source_exp", source_exp),
        ("root_exp", root_exp),
        ("target_root", target_root),
    ):
        _require_int(name, value)
    if k < 1 or source_exp < 1 or root_exp < 1 or target_root < 0:
        raise ValueError("k/exponents must be positive and target_root nonnegative")
    if target_root == 0:
        return None
    numerator = root_exp * (k + 1) ** source_exp - 1
    denominator = target_root ** (root_exp + 1)
    return 1 + numerator // denominator


def observed_root_divisor_multiplicity(
    k: int,
    n: int,
    source_exp: int,
    root_exp: int,
    target_root: int,
    max_divisor: int,
) -> dict[str, object]:
    """Audit actual total-denominator multiplicity against the graded cap."""
    for name, value in (("target_root", target_root), ("max_divisor", max_divisor)):
        _require_int(name, value)
    if target_root <= 0:
        raise ValueError("target_root must be positive")
    if max_divisor < 2:
        raise ValueError("max_divisor must be at least 2")
    hits = tuple(
        divisor
        for divisor in range(2, max_divisor + 1)
        if power_basin_cross_root(k, n, source_exp, root_exp, divisor) == target_root
    )
    cap = coalescence_multiplicity_cap(k, source_exp, root_exp, target_root)
    if cap is None:
        raise AssertionError("positive target unexpectedly lost its cap")
    if len(hits) > cap:
        raise AssertionError("observed divisor multiplicity exceeded graded cap")
    if len(hits) >= 2:
        collision = cross_root_divisor_collision(
            k, n, source_exp, root_exp, hits[0], hits[-1]
        )
        if not collision["coalesces"]:
            raise AssertionError("extreme hit divisors failed to coalesce")
    return {
        "k": k,
        "n": n,
        "source_exp": source_exp,
        "root_exp": root_exp,
        "target_root": target_root,
        "divisor_hits": hits,
        "multiplicity": len(hits),
        "multiplicity_cap": cap,
    }


def sharp_consecutive_collision_block(
    source_exp: int, root_exp: int, gap: int, parameter: int
) -> dict[str, object]:
    """Construct a sharp block of gap+1 consecutive coalescing denominators."""
    for name, value in (
        ("source_exp", source_exp),
        ("root_exp", root_exp),
        ("gap", gap),
        ("parameter", parameter),
    ):
        _require_int(name, value)
    if source_exp < 1 or root_exp < 1 or gap < 1 or parameter < 2:
        raise ValueError("exponents/gap must be positive and parameter>=2")

    d = gap * parameter
    e = gap * (parameter + 1)
    t = root_exp * parameter - 1
    n = e * t**root_exp
    if n >= d * (t + 1) ** root_exp:
        raise AssertionError("sharp collision block interval is empty")
    k = integer_nth_root(n, source_exp)
    if not k**source_exp <= n < (k + 1) ** source_exp:
        raise AssertionError("constructed state escaped its canonical source basin")

    hits = tuple(range(d, e + 1))
    exact_fiber = total_divisor_root_fiber(n, root_exp, t)
    exact_labels = set(exact_fiber["positive_divisor_labels"])
    for divisor in hits:
        if divisor not in exact_labels:
            raise AssertionError("sharp block escaped the exact root fiber")
    cap = coalescence_multiplicity_cap(k, source_exp, root_exp, t)
    if cap is None or len(hits) > cap:
        raise AssertionError("sharp block exceeded the proved multiplicity cap")

    return {
        "source_exp": source_exp,
        "root_exp": root_exp,
        "gap": gap,
        "parameter": parameter,
        "k": k,
        "n": n,
        "left": d,
        "right": e,
        "common_root": t,
        "divisor_hits": hits,
        "multiplicity": len(hits),
        "multiplicity_cap": cap,
        "exact_fiber_lower_exclusive": exact_fiber["lower_exclusive"],
        "exact_fiber_upper_inclusive": exact_fiber["upper_inclusive"],
        "weighted_ratio_numerator": gap * t,
        "weighted_ratio_denominator": root_exp * e,
    }


def sharp_adjacent_collision_family(
    source_exp: int, root_exp: int, m: int
) -> dict[str, int]:
    """Backward-compatible gap-one sharp family."""
    data = sharp_consecutive_collision_block(source_exp, root_exp, 1, m)
    return {
        "source_exp": source_exp,
        "root_exp": root_exp,
        "m": m,
        "k": int(data["k"]),
        "n": int(data["n"]),
        "left": int(data["left"]),
        "right": int(data["right"]),
        "common_root": int(data["common_root"]),
        "horizon": cross_root_coalescence_horizon(int(data["k"]), source_exp, root_exp),
        "sharp_ratio_numerator": int(data["weighted_ratio_numerator"]),
        "sharp_ratio_denominator": int(data["weighted_ratio_denominator"]),
    }


def same_exponent_coalescence_horizon(k: int, exponent: int) -> int:
    """Return the p=r specialization H_{p,p}(k)."""
    return cross_root_coalescence_horizon(k, exponent, exponent)


def coalescence_phase(source_exp: int, root_exp: int) -> str:
    """Classify the sharp exponent p/(r+1) relative to one."""
    _require_int("source_exp", source_exp)
    _require_int("root_exp", root_exp)
    if source_exp < 1 or root_exp < 1:
        raise ValueError("both exponents must be positive")
    if root_exp + 1 > source_exp:
        return "sublinear"
    if root_exp + 1 == source_exp:
        return "linear-boundary"
    return "superlinear-bound"


def coarse_sublinear_descent_threshold(source_exp: int, root_exp: int) -> int:
    """Return a simple sufficient k-threshold for H_{p,r}(k)<k."""
    _require_int("source_exp", source_exp)
    _require_int("root_exp", root_exp)
    if source_exp < 1 or root_exp < 1:
        raise ValueError("both exponents must be positive")
    gap = root_exp + 1 - source_exp
    if gap <= 0:
        raise ValueError("no sublinear descent threshold when r+1<=p")
    target = root_exp * (1 << source_exp)
    return integer_nth_root(target - 1, gap) + 1


def verify_coarse_sublinear_descent(
    k: int, source_exp: int, root_exp: int
) -> dict[str, int | str]:
    """Check strict horizon descent beyond the coarse sufficient threshold."""
    threshold = coarse_sublinear_descent_threshold(source_exp, root_exp)
    if k < threshold:
        raise ValueError("k is below the coarse sufficient descent threshold")
    horizon = cross_root_coalescence_horizon(k, source_exp, root_exp)
    if horizon >= k:
        raise AssertionError("sublinear all-power horizon failed strict descent")
    return {
        "k": k,
        "source_exp": source_exp,
        "root_exp": root_exp,
        "phase": coalescence_phase(source_exp, root_exp),
        "threshold": threshold,
        "horizon": horizon,
        "drop": k - horizon,
    }
