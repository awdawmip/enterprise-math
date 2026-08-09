"""Discovery-stage P018 all-power cross-divisor coalescence law.

This module generalizes the square-basin cubic collision mechanism to arbitrary
source power basins and arbitrary quotient-root observations.

Let

    k^p <= n < (k+1)^p

with source-basin exponent ``p>=1``. Observe the quotient through an ``r``-th
integer root, ``r>=1``. If two distinct divisors ``2<=d<e`` give the same
actual quotient-root ``t`` then

    e*t^r <= n < d*(t+1)^r.

The collision itself supplies the sharp scale constant. Since ``e>=d+1``, if
``t+1 >= r(d+1)`` then the standard finite-difference/Bernoulli estimate gives

    d*((t+1)^r - t^r) <= t^r,

and hence

    d*(t+1)^r <= (d+1)*t^r <= e*t^r <= n,

contradicting ``n < d*(t+1)^r``. Therefore

    t+1 < r(d+1),

so in particular ``t < r*e``. Multiplying by ``t^r`` yields the all-power
cross-root coalescence law

    t^(r+1) < r*e*t^r <= r*n < r*(k+1)^p.

Thus every actual cross-divisor collision lies below the exact integer horizon

    H_{p,r}(k) = R_{r+1}(r*(k+1)^p - 1).

The asymptotic collision exponent is

    gamma(p,r) = p/(r+1).

Consequently ``r+1>p`` is the sublinear/coalescence-contraction regime;
``r+1=p`` is the linear boundary; and ``r+1<p`` is not forced to contract by
this mechanism. In the same-exponent family ``r=p`` one obtains the strictly
sublinear law ``O(k^(p/(p+1)))``.

Both the exponent and the leading root-order constant ``r`` are asymptotically
sharp. For every ``r,m>=1`` (using ``m>=2`` in the executable witness), put

    d=m,  e=m+1,  t=r*m-1,
    n=(m+1)*(r*m-1)^r.

Bernoulli's inequality applied to ``rm/(rm-1)=1+1/(rm-1)`` gives

    m*(r*m)^r > (m+1)*(r*m-1)^r,

so division by both ``m`` and ``m+1`` has exact ``r``-root ``t``. Moreover

    t^(r+1)/(r*n) = (r*m-1)/(r*(m+1)) -> 1.

For any fixed source exponent ``p``, assigning this ``n`` to its canonical
``p``-root basin also makes ``t`` scale as ``k^(p/(r+1))``. Hence neither the
exponent nor the leading constant can be improved uniformly for the general
cross-divisor collision mechanism.

All statements use exact integer roots/division. Bernoulli/difference-of-powers
inequalities are classical; the project-specific value is the finite-precision
coalescence packaging, exact integer horizon, and exponent/phase-boundary law.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def coalescence_root_constant(root_exp: int) -> int:
    """Return the sharp general cross-divisor constant C_r=r."""
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
    """Validate the all-power actual cross-divisor collision law.

    If the two quotient roots coincide at ``t``, verify

        t^(r+1) < r*(k+1)^p

    and the stronger local scale fact ``t+1 < r*(d+1)``.
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
    result: dict[str, object] = {
        "k": k,
        "n": n,
        "source_exp": source_exp,
        "root_exp": root_exp,
        "left": left,
        "right": right,
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
    if t**root_exp >= left * delta:
        raise AssertionError("divisor-spacing difference inequality failed")

    # Mathematical proof boundary: if t+1 were at least r(d+1), the standard
    # difference-of-powers/Bernoulli estimate would imply
    # d*(t+1)^r <= (d+1)t^r, contradicting the exact collision interval.
    if t + 1 >= root_exp * (left + 1):
        raise AssertionError("collision violated the sharp t+1<r(d+1) bound")
    if t >= root_exp * right:
        raise AssertionError("collision root exceeded the sharp r*e scale")

    argument_exclusive = root_exp * (k + 1) ** source_exp
    if t ** (root_exp + 1) >= argument_exclusive:
        raise AssertionError("cross-root collision escaped the all-power bound")
    if t > horizon:
        raise AssertionError("cross-root collision exceeded H_{p,r}(k)")

    return {
        **result,
        "common_root": t,
        "root_order_constant": root_exp,
        "root_increment": delta,
        "collision_power": t ** (root_exp + 1),
        "horizon_argument": argument_exclusive - 1,
        "sublinear_regime": root_exp + 1 > source_exp,
        "linear_boundary": root_exp + 1 == source_exp,
    }


def sharp_adjacent_collision_family(
    source_exp: int, root_exp: int, m: int
) -> dict[str, int]:
    """Return an explicit asymptotically sharp adjacent-divisor collision.

    ``d=m``, ``e=m+1``, ``t=r*m-1`` and
    ``n=(m+1)t^r``.  Both quotient roots are exactly ``t``.  The returned
    ``k`` is the canonical source ``p``-root index of ``n``.
    """
    for name, value in (
        ("source_exp", source_exp),
        ("root_exp", root_exp),
        ("m", m),
    ):
        _require_int(name, value)
    if source_exp < 1 or root_exp < 1 or m < 2:
        raise ValueError("source_exp/root_exp must be positive and m>=2")

    d = m
    e = m + 1
    t = root_exp * m - 1
    n = e * t**root_exp
    if n >= d * (t + 1) ** root_exp:
        raise AssertionError("sharp adjacent collision interval is empty")
    if n // e != t**root_exp:
        raise AssertionError("upper-divisor quotient is not the exact lower root power")
    if not t**root_exp <= n // d < (t + 1) ** root_exp:
        raise AssertionError("lower-divisor quotient escaped the common root cell")

    k = integer_nth_root(n, source_exp)
    if not k**source_exp <= n < (k + 1) ** source_exp:
        raise AssertionError("constructed state escaped its canonical source basin")
    horizon = cross_root_coalescence_horizon(k, source_exp, root_exp)
    if t > horizon:
        raise AssertionError("sharp witness escaped the general horizon")

    return {
        "source_exp": source_exp,
        "root_exp": root_exp,
        "m": m,
        "k": k,
        "n": n,
        "left": d,
        "right": e,
        "common_root": t,
        "horizon": horizon,
        "sharp_ratio_numerator": t,
        "sharp_ratio_denominator": root_exp * (m + 1),
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

    Therefore ``k^s >= r*2^p`` is sufficient.  This threshold is deliberately
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
