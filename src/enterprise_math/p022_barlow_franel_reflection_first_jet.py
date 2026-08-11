"""First-jet lift of the Jarvis--Verrill Franel reflection congruence.

Jarvis--Verrill gives, for an odd prime p and 0<=n<p,

    F_n = (-8)^n F_(p-1-n)                              (mod p).

Write

    R_n = (-8)^n F_(p-1-n).

Reflecting the classical Franel recurrence around p-1 and expanding its
coefficients modulo p^2 shows that the first-order error R_n-F_n satisfies the
negative of the differentiated Franel recurrence.  If F'_n denotes Straub's
formal derivative for the Franel Apéry-like sequence, recurrence uniqueness and
the n=0,1 initial values give the exact congruence

    R_n = (1+p*c_p) F_n - p F'_n                        (mod p^2),

where

    c_p = (F_(p-1)-1)/p                                 (mod p).

The n=1 initial value is not an empirical fit: the Franel recurrence at n=p-1
gives

    -8 F_(p-2) = (2-3p) F_(p-1)                        (mod p^2),

which is exactly the required second initial condition.

At a p-zero the nuisance scalar c_p disappears.  If m=p-1-n and
F_n=p*u, then

    (-8)^n F_m/p = u - F'_n                             (mod p).

Applying the formula again at m yields the derivative reflection law

    F'_m = -(-8)^(-n) F'_n                              (mod p).

Hence, when n and m are both simple p-zeros, the unique Gessel--Lucas copy
multiplier that can raise the p-adic depth transforms by

    a*_m = -1-a*_n                                      (mod p).

For a self-reflected forced midpoint n=(p-1)/2 with (-2/p)=-1, a simple zero
satisfies F'_n=2(F_n/p) mod p, so its exceptional copy multiplier is exactly n.

The Jarvis--Verrill mod-p reflection and Straub formal derivative/Gessel--Lucas
framework are prior art.  The p^2 reflection lift and the zero-depth/copy
consequences are P022-local deductions from those ingredients and the Franel
recurrence.
"""

from __future__ import annotations

from .p022_barlow_franel_gessel_lucas_copy import (
    _fraction_mod,
    franel_formal_derivative,
)
from .p022_barlow_franel_half_index import (
    half_index,
    half_index_is_forced_zero,
)
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def reflection_scalar(prime: int) -> int:
    """Return c_p=(F_(p-1)-1)/p mod p."""
    _require_odd_prime(prime)
    value = triple_moment_factor(prime - 1)
    if (value - 1) % prime:
        raise AssertionError("F_(p-1) must be one modulo p")
    return ((value - 1) // prime) % prime


def reflected_first_jet_residues(prime: int, index: int) -> tuple[int, int]:
    """Return actual/predicted reflected residues modulo p^2."""
    _require_odd_prime(prime)
    if (
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 0 <= index < prime
    ):
        raise ValueError("index must lie in 0..p-1")
    modulus = prime * prime
    reflected = prime - 1 - index
    actual = (
        pow(-8, index, modulus)
        * (triple_moment_factor(reflected) % modulus)
    ) % modulus
    derivative = _fraction_mod(franel_formal_derivative(index), modulus)
    predicted = (
        (1 + prime * reflection_scalar(prime))
        * (triple_moment_factor(index) % modulus)
        - prime * derivative
    ) % modulus
    if actual != predicted:
        raise AssertionError("Franel p-square reflection first jet failed")
    return actual, predicted


def zero_reflection_quotient_residue(
    prime: int,
    index: int,
) -> tuple[int, int, int, int]:
    """At p|F_n return (u,v,d,s) with s*v=u-d mod p.

    Here m=p-1-n, u=F_n/p mod p, v=F_m/p mod p, d=F'_n mod p,
    and s=(-8)^n mod p.  The function allows depth at least two; in that case
    the corresponding quotient residue is zero.
    """
    _require_odd_prime(prime)
    if not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    reflected = prime - 1 - index
    current = triple_moment_factor(index)
    mirror = triple_moment_factor(reflected)
    if current % prime or mirror % prime:
        raise ValueError("index and its reflection must be Franel p-zeros")
    reflected_first_jet_residues(prime, index)
    u = (current // prime) % prime
    v = (mirror // prime) % prime
    derivative = _fraction_mod(franel_formal_derivative(index), prime)
    scale = pow(-8, index, prime)
    if scale * v % prime != (u - derivative) % prime:
        raise AssertionError("zero reflection quotient first-jet law failed")
    return u, v, derivative, scale


def zero_derivative_reflection(prime: int, index: int) -> tuple[int, int]:
    """At a reflected zero pair certify d_m=-(-8)^(-n)d_n mod p."""
    u, v, derivative, scale = zero_reflection_quotient_residue(prime, index)
    _ = (u, v)
    reflected = prime - 1 - index
    mirror_derivative = _fraction_mod(franel_formal_derivative(reflected), prime)
    predicted = (-pow(scale, -1, prime) * derivative) % prime
    if mirror_derivative != predicted:
        raise AssertionError("formal derivatives must reflect anti-equivariantly")
    return mirror_derivative, predicted


def simple_zero_exceptional_multiplier(prime: int, index: int) -> int | None:
    """Unique multiplier a with a*p+n raising a simple zero above depth one.

    Returns None when the formal derivative vanishes; then no multiplier can
    raise the depth because the source quotient unit is nonzero.
    """
    _require_odd_prime(prime)
    if p_adic_valuation(triple_moment_factor(index), prime) != 1:
        raise ValueError("index must be a simple Franel p-zero")
    source_unit = (triple_moment_factor(index) // prime) % prime
    derivative = _fraction_mod(franel_formal_derivative(index), prime)
    if derivative == 0:
        return None
    return (-source_unit * pow(derivative, -1, prime)) % prime


def reflected_exceptional_multipliers(
    prime: int,
    index: int,
) -> tuple[int | None, int | None]:
    """For a simple reflected zero pair certify a*_m=-1-a*_n."""
    _require_odd_prime(prime)
    reflected = prime - 1 - index
    if p_adic_valuation(triple_moment_factor(index), prime) != 1:
        raise ValueError("index must be a simple Franel p-zero")
    if p_adic_valuation(triple_moment_factor(reflected), prime) != 1:
        raise ValueError("reflected index must also be a simple Franel p-zero")
    left = simple_zero_exceptional_multiplier(prime, index)
    right = simple_zero_exceptional_multiplier(prime, reflected)
    zero_derivative_reflection(prime, index)
    if left is None or right is None:
        if left is not None or right is not None:
            raise AssertionError("derivative-zero exceptional status must reflect")
        return None, None
    if right != (-1 - left) % prime:
        raise AssertionError("reflected exceptional multipliers must sum to -1")
    return left, right


def forced_midpoint_first_jet(prime: int) -> tuple[int, int, int]:
    """At a simple forced midpoint return (m,u,d) and certify d=2u mod p."""
    _require_odd_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("prime must lie in the forced-midpoint mod-8 sector")
    midpoint = half_index(prime)
    if p_adic_valuation(triple_moment_factor(midpoint), prime) != 1:
        raise ValueError("forced midpoint must have exact p-adic depth one")
    u, v, derivative, scale = zero_reflection_quotient_residue(prime, midpoint)
    if midpoint != prime - 1 - midpoint or u != v:
        raise AssertionError("declared midpoint must be self-reflected")
    if scale != prime - 1:
        raise AssertionError("forced midpoint reflection multiplier must be -1")
    if derivative != 2 * u % prime:
        raise AssertionError("self-reflected simple zero must satisfy d=2u")
    exceptional = simple_zero_exceptional_multiplier(prime, midpoint)
    if exceptional != midpoint:
        raise AssertionError("forced midpoint exceptional multiplier must equal m")
    return midpoint, u, derivative
