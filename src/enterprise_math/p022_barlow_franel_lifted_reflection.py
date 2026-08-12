"""Lift the Franel reflection congruence to its first q-adic jet.

For an odd prime q and 0<=r<=q-1 put s=q-1-r.  The usual Jarvis--Verrill
reflection is

    F_r = (-8)^r F_s                                      (mod q).

The Franel recurrence has the exact coefficient symmetry n -> -n-1.  Applying
it to G_r=(-8)^r F_(q-1-r), expanding the shifted polynomial coefficients to
first order in q, and comparing with the differentiated Franel recurrence
shows that

    E_r = (F_r-G_r)/q                                     (mod q)

satisfies the same inhomogeneous recurrence as Straub's formal derivative
F'_r.  Their difference is a homogeneous Franel solution.  The endpoint
congruence

    F_(q-1) = 8^(q-1)                                     (mod q^2)

fixes that homogeneous solution and gives

    E_r = F'_r - Q_q(8) F_r                               (mod q),

where Q_q(8)=(8^(q-1)-1)/q is the Fermat quotient.

At a Franel zero digit the Fermat-quotient term vanishes, so

    (F_r-(-8)^r F_(q-1-r))/q = F'_r                       (mod q).

Applying the same identity at the reflected zero and using
(-8)^(q-1)=1+q Q_q(8) mod q^2 gives the formal-jet reflection law

    F'_(q-1-r) = -(-8)^(-r) F'_r                          (mod q).

Thus formal-stationary zeros occur in reflected pairs.  Moreover, if q^2
divides F_r, then q divides F'_r exactly when the reflected zero also has depth
at least two.  The sole mod-q^2 copy-depth obstruction left by the Gessel--Lucas
first jet is therefore a reflected double-deep stationary pair.

Jarvis--Verrill reflection and Straub's formal derivative are prior art.  The
P022 contribution is the lifted first-jet identity and its use to reinterpret
the double-stationary copy obstruction geometrically.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_franel_gessel_lucas_copy import franel_formal_derivative
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def _fraction_mod(value, modulus: int) -> int:
    denominator = value.denominator % modulus
    if gcd(denominator, modulus) != 1:
        raise ValueError("fraction denominator is not a unit modulo the modulus")
    return value.numerator % modulus * pow(denominator, -1, modulus) % modulus


def fermat_quotient(base: int, prime: int) -> int:
    """Return Q_p(base)=(base^(p-1)-1)/p modulo p using mod-p^2 powering."""
    _require_odd_prime(prime)
    if base % prime == 0:
        raise ValueError("base must be a p-adic unit")
    residue = pow(base, prime - 1, prime * prime)
    if (residue - 1) % prime:
        raise AssertionError("Fermat's theorem must make the quotient integral modulo p")
    return ((residue - 1) // prime) % prime


def franel_digit_table_mod_square(prime: int) -> tuple[int, ...]:
    """Return F_0,...,F_(p-1) modulo p^2 from the Franel recurrence."""
    _require_odd_prime(prime)
    modulus = prime * prime
    values = [1, 2]
    for n in range(1, prime - 1):
        denominator = (n + 1) ** 2 % modulus
        if gcd(denominator, modulus) != 1:
            raise AssertionError("digit recurrence denominators must be p-units")
        following = (
            ((7 * n * n + 7 * n + 2) * values[n] + 8 * n * n * values[n - 1])
            * pow(denominator, -1, modulus)
        ) % modulus
        values.append(following)
    if len(values) != prime:
        raise AssertionError("digit table must stop at p-1")
    return tuple(values)


def endpoint_franel_lift(prime: int) -> tuple[int, int]:
    """Certify F_(p-1)=8^(p-1) modulo p^2.

    The congruence also follows directly by cubing
    C(p-1,k)=(-1)^k(1-p H_k) mod p^2 and using
    sum_k (-1)^k H_k = -Q_p(2) mod p.
    """
    table = franel_digit_table_mod_square(prime)
    actual = table[prime - 1]
    predicted = pow(8, prime - 1, prime * prime)
    if actual != predicted:
        raise AssertionError("Franel endpoint lift failed")
    return actual, predicted


def lifted_reflection_first_jet(rank: int, prime: int) -> tuple[int, int]:
    """Return actual/predicted first-jet reflection residues modulo p."""
    _require_odd_prime(prime)
    if isinstance(rank, bool) or not isinstance(rank, int) or not 0 <= rank < prime:
        raise ValueError("rank must lie in 0..p-1")
    table = franel_digit_table_mod_square(prime)
    reflected = prime - 1 - rank
    modulus = prime * prime
    difference = (
        table[rank] - pow(-8, rank, modulus) * table[reflected]
    ) % modulus
    if difference % prime:
        raise AssertionError("ordinary reflection must make the difference divisible by p")
    actual = (difference // prime) % prime
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    predicted = (
        derivative - fermat_quotient(8, prime) * (table[rank] % prime)
    ) % prime
    if actual != predicted:
        raise AssertionError("lifted Franel reflection first jet failed")
    return actual, predicted


def zero_digit_lifted_reflection(rank: int, prime: int) -> tuple[int, int]:
    """At p|F_r, certify the lifted reflection quotient equals F'_r mod p."""
    table = franel_digit_table_mod_square(prime)
    if table[rank] % prime:
        raise ValueError("rank must be a Franel zero digit modulo p")
    actual, predicted = lifted_reflection_first_jet(rank, prime)
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    if actual != derivative or predicted != derivative:
        raise AssertionError("zero-digit lift must remove the Fermat-quotient term")
    return actual, derivative


def zero_digit_formal_derivative_reflection(rank: int, prime: int) -> tuple[int, int]:
    """At a zero digit, reflect the formal derivative modulo p.

    Returns (actual derivative at the mirror, reflected prediction).
    """
    table = franel_digit_table_mod_square(prime)
    if table[rank] % prime:
        raise ValueError("rank must be a Franel zero digit modulo p")
    reflected = prime - 1 - rank
    if table[reflected] % prime:
        raise AssertionError("ordinary reflection must preserve zero status")
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    actual = _fraction_mod(franel_formal_derivative(reflected), prime)
    predicted = (-pow(pow(-8, rank, prime), -1, prime) * derivative) % prime
    if actual != predicted:
        raise AssertionError("formal derivative reflection law failed")
    return actual, predicted


def double_stationary_iff_reflected_deep(rank: int, prime: int) -> bool:
    """For p^2|F_r, p|F'_r iff p^2|F_(p-1-r)."""
    table = franel_digit_table_mod_square(prime)
    if table[rank] != 0:
        raise ValueError("source digit must have depth at least two")
    reflected = prime - 1 - rank
    zero_digit_lifted_reflection(rank, prime)
    zero_digit_formal_derivative_reflection(rank, prime)
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    derivative_stationary = derivative == 0
    reflected_deep = table[reflected] == 0
    if derivative_stationary != reflected_deep:
        raise AssertionError("lifted reflection must identify the double-deep obstruction")
    return derivative_stationary


def simple_copy_degeneracy_reflected_ratio(
    rank: int, prime: int, multiplier: int
) -> tuple[int, int, int]:
    """Expose the reflected-unit ratio when a simple copy first jet vanishes.

    Returns (source unit, reflected unit, copy linear factor).  At a simple
    source zero the factor u+aF'_r is zero exactly when

        (a+1)u = a*(-8)^r*v   (mod p),

    where v=F_(p-1-r)/p mod p.
    """
    table = franel_digit_table_mod_square(prime)
    source = table[rank]
    if source % prime or source == 0:
        raise ValueError("source digit must have exact depth one")
    if isinstance(multiplier, bool) or not isinstance(multiplier, int) or multiplier <= 0:
        raise ValueError("multiplier must be positive")
    reflected = prime - 1 - rank
    reflected_value = table[reflected]
    if reflected_value % prime:
        raise AssertionError("reflection partner must also be a zero digit")
    source_unit = (source // prime) % prime
    reflected_unit = (reflected_value // prime) % prime
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    factor = (source_unit + multiplier * derivative) % prime
    equivalent = (
        (multiplier + 1) * source_unit
        - multiplier * pow(-8, rank, prime) * reflected_unit
    ) % prime
    if factor != equivalent:
        raise AssertionError("lifted reflection ratio form disagrees with the copy first jet")
    return source_unit, reflected_unit, factor
