"""Discovery-stage P018 all-power cross-divisor coalescence law.

Let a source state lie in the complete power basin

    k^p <= n < (k+1)^p

and observe floor quotients through an ``r``-th integer root.  The basic actual
cross-divisor collision law is

    R_r(n//d) = R_r(n//e) = t,   2<=d<e
        =>
    (e-d) * t^(r+1) < r*n < r*(k+1)^p.

Thus the *divisor-span* of a root collision is itself controlled by the target
root scale.  The pair theorem ``t^(r+1)<r(k+1)^p`` is only the gap-one case.

For any finite set of distinct total divisors coalescing at the same positive
root t, if the multiplicity is ``m`` then its span is at least ``m-1``. Hence

    (m-1) * t^(r+1) < r*(k+1)^p

and therefore

    m <= 1 + floor((r*(k+1)^p - 1) / t^(r+1)).

This is a graded path-coalescence capacity law.  With canonical quotient-path
flatness, the same bound applies to distinct factor-extraction paths after they
are identified by their total divisors.

The law is asymptotically sharp at every multiplicity scale.  Fix an integer
gap ``g>=1`` and parameter ``a>=2``.  Put

    d = g*a,
    e = g*(a+1),
    t = r*a - 1,
    n = e*t^r.

The endpoint divisors d,e have the same actual r-root t; monotonicity then puts
every integer divisor in the consecutive block [d,e] into the same root cell,
so the multiplicity is exactly ``g+1``.  Moreover

    g*t^(r+1)/(r*n)
      = (r*a-1)/(r*(a+1)) -> 1.

For any fixed source exponent p, assigning n to its canonical p-root basin gives
``t asymp k^(p/(r+1))``.  Consequently the leading constant r, exponent
``p/(r+1)``, and the graded multiplicity profile all have the correct asymptotic
shape for this mechanism.

The exact two-divisor horizon is

    H_{p,r}(k) = R_{r+1}(r*(k+1)^p - 1).

The phase boundary is governed by ``p/(r+1)``: ``r+1>p`` is sublinear,
``r+1=p`` is linear, and ``r+1<p`` is not forced to contract.  In particular,
the same-exponent family r=p always contracts as ``O(k^(p/(p+1)))``.

All reference functions use exact integer roots and floor division. Classical
Bernoulli/difference-of-powers inequalities are prior art; the project-specific
candidate contribution is the finite-precision coalescence packaging, sharp
integer horizons/capacities, and their use as a well-founded recursion skeleton.
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

    If the quotient roots coincide at ``t`` and ``g=right-left``, verify

        g * t^(r+1) < r*(k+1)^p.

    The proof-scale inequality is

        g*(t+1) < r*right.

    For g=1 this gives the earlier ``t+1<r(d+1)`` theorem.
    """
    for name, value in (("left", left), ("right", right)):
        _require_int(name, value)
    if not 2 <= left < right:
        raise ValueError("require 2 <= left < right")

    left_root = power_basin_cross_root(
        k, n, source_exp, root_exp, left
    )
    right_root = power_basin_cross_root(
        k, n, source_exp, root_exp, right
    )
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

    # Generalized Bernoulli contradiction: if
    # r*right <= gap*(t+1), then the tangent bound at x=t+1 gives
    # left*(t+1)^r <= right*t^r, contradicting the exact collision cell.
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
    """Return the sharp graded cap for a positive target root.

    For t>0, any set of distinct total divisors coalescing at t has size at most

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
    """Audit actual divisor multiplicity against the graded cap on a finite range."""
    for name, value in (("target_root", target_root), ("max_divisor", max_divisor)):
        _require_int(name, value)
    if target_root <= 0:
        raise ValueError("target_root must be positive")
    if max_divisor < 2:
        raise ValueError("max_divisor must be at least 2")
    hits = tuple(
        divisor
        for divisor in range(2, max_divisor + 1)
        if power_basin_cross_root(
            k, n, source_exp, root_exp, divisor
        ) == target_root
    )
    cap = coalescence_multiplicity_cap(
        k, source_exp, root_exp, target_root
    )
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
    """Construct a sharp block of gap+1 consecutive coalescing divisors.

    Put ``d=gap*parameter``, ``e=gap*(parameter+1)``, ``t=r*parameter-1``
    and ``n=e*t^r``. The endpoint collision implies every integer divisor in
    ``[d,e]`` has the same actual root t by monotonicity.
    """
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
    for divisor in hits:
        quotient = n // divisor
        if not t**root_exp <= quotient < (t + 1) ** root_exp:
            raise AssertionError("intermediate divisor escaped the common root cell")
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
        "horizon": cross_root_coalescence_horizon(
            int(data["k"]), source_exp, root_exp
        ),
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
    """Return a simple sufficient k-threshold for H_{p,r}(k)<k.

    If ``s=r+1-p>=1``, then ``k+1<=2k`` gives

        r*(k+1)^p <= r*2^p*k^p.

    Therefore ``k^s >= r*2^p`` is sufficient. This threshold is deliberately
    simple rather than optimal.
    """
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
