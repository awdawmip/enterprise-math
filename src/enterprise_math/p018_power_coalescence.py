"""Discovery-stage P018 all-power cross-divisor coalescence law.

This module generalizes the square-basin cubic collision mechanism to arbitrary
source power basins and arbitrary quotient-root observations.

Let

    k^p <= n < (k+1)^p

with source-basin exponent ``p>=1``.  Observe the quotient through an ``r``-th
integer root, ``r>=1``.  If two distinct divisors ``2<=d<e`` give the same
actual quotient-root ``t`` then

    e*t^r <= n < d*(t+1)^r.

Because ``e>=d+1``, subtraction gives

    t^r < d * ((t+1)^r - t^r).

For ``t>0`` the binomial theorem gives the elementary uniform estimate

    (t+1)^r - t^r <= (2^r-1) * t^(r-1).

Writing ``C_r=2^r-1`` therefore yields

    t < C_r*d < C_r*e

and hence

    t^(r+1) < C_r * e*t^r <= C_r*n < C_r*(k+1)^p.

Thus every actual cross-divisor collision lies below the exact integer horizon

    H_{p,r}(k) = R_{r+1}(C_r*(k+1)^p - 1).

The asymptotic collision exponent is

    gamma(p,r) = p/(r+1).

Consequently ``r+1>p`` is the sublinear/coalescence-contraction regime;
``r+1=p`` is the linear boundary; and ``r+1<p`` is not forced to contract by
this argument.  In the same-exponent family ``r=p`` one obtains
``O(k^(p/(p+1)))``.  The square specialization ``p=r=2`` gives the same 2/3
exponent as the sharper square theorem, but its generic binomial constant is 3;
the square-specific argument improves that constant to the asymptotically sharp
value 2.

All statements here use only exact integer roots/division.  The binomial and
order inequalities are classical; the research value is the finite-precision
coalescence packaging and the exponent/phase-boundary interpretation.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def coalescence_binomial_constant(root_exp: int) -> int:
    """Return C_r=2^r-1 for r>=1."""
    _require_int("root_exp", root_exp)
    if root_exp < 1:
        raise ValueError("root_exp must be positive")
    return (1 << root_exp) - 1


def cross_root_coalescence_horizon(
    k: int, source_exp: int, root_exp: int
) -> int:
    """Return H_{p,r}(k)=R_{r+1}(C_r*(k+1)^p-1)."""
    for name, value in (
        ("k", k),
        ("source_exp", source_exp),
        ("root_exp", root_exp),
    ):
        _require_int(name, value)
    if k < 1 or source_exp < 1 or root_exp < 1:
        raise ValueError("k and both exponents must be positive")
    constant = coalescence_binomial_constant(root_exp)
    argument = constant * (k + 1) ** source_exp - 1
    return integer_nth_root(argument, root_exp + 1)


def power_basin_cross_root(k: int, n: int, source_exp: int, root_exp: int, divisor: int) -> int:
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
    """Validate the all-power actual cross-divisor collision bound.

    When the two actual quotient roots differ, the function simply reports the
    two values.  When they coincide at ``t``, it verifies the exact root-cell
    inequalities and the bound

        t^(r+1) < (2^r-1)*(k+1)^p.
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
    constant = coalescence_binomial_constant(root_exp)
    if right * t**root_exp > n:
        raise AssertionError("common root lower interval failed")
    if n >= left * (t + 1) ** root_exp:
        raise AssertionError("common root upper interval failed")

    delta = (t + 1) ** root_exp - t**root_exp
    if t**root_exp >= left * delta:
        raise AssertionError("divisor-spacing difference inequality failed")

    if t > 0:
        binomial_ceiling = constant * t ** (root_exp - 1)
        if delta > binomial_ceiling:
            raise AssertionError("uniform binomial increment bound failed")
        if t >= constant * left:
            raise AssertionError("collision root exceeded C_r*d")
        if t >= constant * right:
            raise AssertionError("collision root exceeded C_r*e")

    argument_exclusive = constant * (k + 1) ** source_exp
    if t ** (root_exp + 1) >= argument_exclusive:
        raise AssertionError("cross-root collision escaped the all-power bound")
    if t > horizon:
        raise AssertionError("cross-root collision exceeded H_{p,r}(k)")

    return {
        **result,
        "common_root": t,
        "binomial_constant": constant,
        "root_increment": delta,
        "collision_power": t ** (root_exp + 1),
        "horizon_argument": argument_exclusive - 1,
        "sublinear_regime": root_exp + 1 > source_exp,
        "linear_boundary": root_exp + 1 == source_exp,
    }


def same_exponent_coalescence_horizon(k: int, exponent: int) -> int:
    """Return the p=r specialization H_{p,p}(k)."""
    return cross_root_coalescence_horizon(k, exponent, exponent)


def coalescence_phase(source_exp: int, root_exp: int) -> str:
    """Classify the exponent p/(r+1) relative to one."""
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

    This is intentionally coarse.  If ``r+1>p``, put ``s=r+1-p>=1`` and
    ``C=2^r-1``.  For ``k>=1`` one has ``k+1<=2k``, hence

        C*(k+1)^p <= C*2^p*k^p.

    Therefore ``k^s >= C*2^p`` suffices for the horizon argument to be below
    ``k^(r+1)``.  We return the least integer k satisfying this simple bound.
    """
    _require_int("source_exp", source_exp)
    _require_int("root_exp", root_exp)
    if source_exp < 1 or root_exp < 1:
        raise ValueError("both exponents must be positive")
    gap = root_exp + 1 - source_exp
    if gap <= 0:
        raise ValueError("no sublinear descent threshold when r+1<=p")
    target = coalescence_binomial_constant(root_exp) * (1 << source_exp)
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
