"""Exact radical-support diagnostics for the P025 abc pressure test.

This module does not prove the abc conjecture.  It treats ``rad(n)`` as a
multiplicative support collapse: prime multiplicities are forgotten while prime
support is retained.  The helpers below expose exact integer defect coordinates,
residual multiplicity pressure, and the arithmetic skeleton behind the
Mason--Stothers Wronskian proof.

Prime factorization, radicals, and the Mason--Stothers theorem are established
mathematics.  P025 uses them as a pressure test for finite-collapse semantics.
"""

from __future__ import annotations

from math import gcd


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def prime_factorization(n: int) -> tuple[tuple[int, int], ...]:
    """Return the exact prime factorization of a positive integer."""
    _require_positive("n", n)
    remaining = n
    factors: list[tuple[int, int]] = []
    candidate = 2
    while candidate * candidate <= remaining:
        exponent = 0
        while remaining % candidate == 0:
            remaining //= candidate
            exponent += 1
        if exponent:
            factors.append((candidate, exponent))
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def prime_support(n: int) -> tuple[int, ...]:
    """Return the distinct prime support of ``n``."""
    return tuple(p for p, _exponent in prime_factorization(n))


def radical(n: int) -> int:
    """Return ``rad(n)=prod_{p|n} p`` exactly."""
    result = 1
    for p in prime_support(n):
        result *= p
    return result


def multiplicity_residual(n: int) -> int:
    """Return the multiplicity detail forgotten by the radical collapse.

    ``n = rad(n) * multiplicity_residual(n)``.
    """
    _require_positive("n", n)
    return n // radical(n)


def _validate_abc(a: int, b: int, c: int) -> None:
    for name, value in (("a", a), ("b", b), ("c", c)):
        _require_positive(name, value)
    if a + b != c:
        raise ValueError("abc triple must satisfy a+b=c")
    if gcd(a, b) != 1:
        raise ValueError("abc triple must satisfy gcd(a,b)=1")


def abc_support_state(a: int, b: int, c: int) -> dict[str, object]:
    """Return exact support/residual data for a primitive abc triple."""
    _validate_abc(a, b, c)
    support_a = prime_support(a)
    support_b = prime_support(b)
    support_c = prime_support(c)
    supports = (set(support_a), set(support_b), set(support_c))
    if supports[0] & supports[1] or supports[0] & supports[2] or supports[1] & supports[2]:
        raise AssertionError("primitive abc supports must be pairwise disjoint")

    radical_a = radical(a)
    radical_b = radical(b)
    radical_c = radical(c)
    radical_product = radical_a * radical_b * radical_c
    if radical_product != radical(a * b * c):
        raise AssertionError("pairwise support disjointness must make radical multiplicative")

    residual_a = multiplicity_residual(a)
    residual_b = multiplicity_residual(b)
    residual_c = multiplicity_residual(c)
    residual_product = residual_a * residual_b * residual_c
    if radical_product * residual_product != a * b * c:
        raise AssertionError("radical/residual decomposition failed")

    return {
        "supports": (support_a, support_b, support_c),
        "radicals": (radical_a, radical_b, radical_c),
        "residuals": (residual_a, residual_b, residual_c),
        "radical_product": radical_product,
        "residual_product": residual_product,
    }


def ceil_div_positive(numerator: int, denominator: int) -> int:
    """Return ceil(numerator/denominator) for positive integers."""
    _require_positive("numerator", numerator)
    _require_positive("denominator", denominator)
    return (numerator + denominator - 1) // denominator


def _validate_rational_exponent(u: int, v: int) -> None:
    _require_positive("u", u)
    _require_positive("v", v)
    if u <= v:
        raise ValueError("require rational exponent u/v > 1")


def rational_abc_defect(a: int, b: int, c: int, u: int, v: int) -> int:
    """Return the exact integer defect ceil(c^v / rad(abc)^u)."""
    _validate_abc(a, b, c)
    _validate_rational_exponent(u, v)
    rad_abc = radical(a * b * c)
    return ceil_div_positive(c**v, rad_abc**u)


def rational_abc_bound_holds(
    a: int, b: int, c: int, u: int, v: int, bound: int
) -> bool:
    """Check the exact rational-exponent abc inequality with integer arithmetic.

    The returned predicate is equivalent to
    ``rational_abc_defect(a,b,c,u,v) <= bound``.
    """
    _validate_abc(a, b, c)
    _validate_rational_exponent(u, v)
    _require_positive("bound", bound)
    rad_abc = radical(a * b * c)
    direct = c**v <= bound * rad_abc**u
    defect = rational_abc_defect(a, b, c, u, v)
    if direct != (defect <= bound):
        raise AssertionError("integer defect coordinate disagrees with direct bound")
    return direct


def exceptional_below_support_power(
    a: int,
    b: int,
    c: int,
    epsilon_num: int,
    epsilon_den: int,
) -> bool:
    """Check ``rad(abc) < c^(1-epsilon)`` without real powers.

    For epsilon = epsilon_num/epsilon_den in (0,1), this is exactly
    ``rad(abc)^epsilon_den < c^(epsilon_den-epsilon_num)``.
    """
    _validate_abc(a, b, c)
    _require_positive("epsilon_num", epsilon_num)
    _require_positive("epsilon_den", epsilon_den)
    if epsilon_num >= epsilon_den:
        raise ValueError("epsilon must lie strictly between 0 and 1")
    rad_abc = radical(a * b * c)
    return rad_abc**epsilon_den < c ** (epsilon_den - epsilon_num)


def residual_pressure(a: int, b: int, c: int, u: int, v: int) -> dict[str, object]:
    """Expose exact multiplicity pressure forced by a high-quality triple.

    If ``c^v > rad(abc)^u`` with ``u>v``, let
    ``M = (a/rad(a)) (b/rad(b)) (c/rad(c))``.
    Since ``abc = rad(abc) M`` and positive ``a+b=c`` gives ``ab>=c-1``,

    ``M^u > c^(u-v) (c-1)^u``.

    Consequently at least one individual residual ``m`` satisfies
    ``m^(3u) > c^(u-v) (c-1)^u``.
    """
    data = abc_support_state(a, b, c)
    _validate_rational_exponent(u, v)
    rad_abc = int(data["radical_product"])
    residual_product = int(data["residual_product"])
    residuals = tuple(int(x) for x in data["residuals"])
    high_quality = c**v > rad_abc**u
    threshold = c ** (u - v) * (c - 1) ** u

    if high_quality:
        if residual_product**u <= threshold:
            raise AssertionError("high-quality triple violated residual-pressure theorem")
        max_residual = max(residuals)
        if max_residual ** (3 * u) <= threshold:
            raise AssertionError("residual pressure failed to localize to one term")

    return {
        **data,
        "u": u,
        "v": v,
        "high_quality": high_quality,
        "threshold": threshold,
        "residual_product_power": residual_product**u,
        "max_residual": max(residuals),
    }


def radical_addition_counterexample() -> dict[str, object]:
    """Return an explicit failure of radical congruence for addition.

    ``rad(4)=rad(8)=2`` and ``rad(1)=1``, but ``rad(4+1)=5`` while
    ``rad(8+1)=3``.  Thus the radical collapse is not an exact P023-safe
    quotient for binary addition.
    """
    left = (4, 1)
    right = (8, 1)
    coarse_left = (radical(left[0]), radical(left[1]))
    coarse_right = (radical(right[0]), radical(right[1]))
    output_left = radical(sum(left))
    output_right = radical(sum(right))
    if coarse_left != coarse_right or output_left == output_right:
        raise AssertionError("addition counterexample construction failed")
    return {
        "fine_inputs": (left, right),
        "coarse_input": coarse_left,
        "coarse_outputs": (output_left, output_right),
    }


def witness_capacity_elimination(
    height_a: int,
    height_b: int,
    height_c: int,
    support_height: int,
    witness_height: int,
    margin: int = 1,
) -> bool:
    """Check the arithmetic elimination skeleton behind Mason--Stothers.

    Write total multiplicity defect as
    ``D = height_a + height_b + height_c - support_height``.
    If an external argument supplies a common witness with
    ``D <= witness_height <= height_a + height_b - margin``,
    then pure integer cancellation forces
    ``height_c + margin <= support_height``.

    P025 does not claim the witness construction: in Mason--Stothers it is the
    classical Wronskian/derivative argument.
    """
    for name, value in (
        ("height_a", height_a),
        ("height_b", height_b),
        ("height_c", height_c),
        ("support_height", support_height),
        ("witness_height", witness_height),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    _require_positive("margin", margin)

    defect = height_a + height_b + height_c - support_height
    assumptions = (
        defect <= witness_height
        and witness_height <= height_a + height_b - margin
    )
    conclusion = height_c + margin <= support_height
    if assumptions and not conclusion:
        raise AssertionError("witness-capacity elimination arithmetic failed")
    return assumptions and conclusion
