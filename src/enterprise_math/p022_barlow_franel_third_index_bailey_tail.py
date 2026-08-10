"""Bailey pole-tail reduction for the Franel one-third index.

Let p=6d+5 be prime and put

    r=(p+1)/3=2d+2,     M=d+1=(p+1)/6.

Modulo p the Franel value F_r is the truncated hypergeometric sum with three
upper parameters -1/3.  A q->1 specialization of the Wang--Xu Bailey
transformation supercongruence rewrites that sum modulo p^2 as p times another
truncated hypergeometric sum.  One must not discard the latter modulo p: its
(5/6)_k denominator contains exactly one factor p once k>=d+1.

Extracting that unique pole gives the exact mod-p reduction

    F_r = - C_d H_d                              (mod p),

where C_d is a p-adic unit and

    H_d = sum_(j=0)^(d+1)
          (-1/6)_j^2 (2/3)_j
          -------------------- .
          (7/6)_j (1/2)_j j!

Consequently

    p | F_((p+1)/3)    iff    p | H_d.

The rational parameters of H_d are congruent modulo p to

    (-M,-M,4M; M+1,3M).

Therefore H_d agrees modulo p with the terminating value

    S_M = 3F2(-M,-M,4M; M+1,3M; 1).

The two rational numbers H_d and S_M are generally not equal over Q; only
their reductions modulo p agree.  A classical terminating 3F2 transformation
further gives

    S_M = (2M+1)_M/(M+1)_M * T_M,
    T_M = 3F2(-M,-M,-M;-3M,3M;1),

whose prefactor is a p-unit when p=6M-1.  Finally

    D_M T_M = U_M,
    D_M = C(3M,M) C(4M-1,M),
    U_M = sum_k C(M,k) C(2M+k,k) C(4M-1,k),

so the one-third zero is equivalent to divisibility of a single integer
binomial sum U_M by p.

Prior-art boundary: the Bailey q-supercongruence used as input is due to
Xiaoxia Wang and Chang Xu, "New q-supercongruences from the Bailey
transformation" (2022).  The pole extraction and its identification with the
P022 third-index obstruction are the contribution recorded here.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _pochhammer(value: Fraction, length: int) -> Fraction:
    result = Fraction(1, 1)
    for step in range(length):
        result *= value + step
    return result


def _fraction_mod_prime(value: Fraction, prime: int) -> int:
    denominator = value.denominator % prime
    if denominator == 0:
        raise ValueError("fraction denominator is not a p-adic unit")
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def _require_positive_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_third_index_prime(prime: int) -> tuple[int, int, int]:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be 5 modulo 6")
    d = (prime - 5) // 6
    rank = (prime + 1) // 3
    truncation = d + 1
    if rank != 2 * truncation:
        raise AssertionError("third-index parameterization changed")
    return rank, d, truncation


def bailey_pole_tail_sum(offset: int) -> Fraction:
    """Return the universal rational H_d before reduction modulo p."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    total = Fraction(0, 1)
    for j in range(offset + 2):
        total += (
            _pochhammer(Fraction(-1, 6), j) ** 2
            * _pochhammer(Fraction(2, 3), j)
            / (
                _pochhammer(Fraction(7, 6), j)
                * _pochhammer(Fraction(1, 2), j)
                * factorial(j)
            )
        )
    return total


def bailey_pole_tail_unit(offset: int) -> Fraction:
    """Return the p-adic unit C_d multiplying H_d after pole extraction."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    k = offset + 1
    return (
        6
        * _pochhammer(Fraction(-1, 3), k) ** 2
        * _pochhammer(Fraction(1, 2), k)
        / (
            factorial(k)
            * _pochhammer(Fraction(1, 3), k)
            * _pochhammer(Fraction(5, 6), offset)
        )
    )


def bailey_tail_integer_parameters(prime: int) -> tuple[int, int, int, int, int]:
    """Return (-M,-M,4M;M+1,3M) for the naturally terminating tail."""
    _, _, truncation = _require_third_index_prime(prime)
    M = truncation
    residues = (-M, -M, 4 * M, M + 1, 3 * M)
    rational_parameters = (
        Fraction(-1, 6),
        Fraction(-1, 6),
        Fraction(2, 3),
        Fraction(7, 6),
        Fraction(1, 2),
    )
    for integer_parameter, rational_parameter in zip(
        residues,
        rational_parameters,
    ):
        if (
            integer_parameter % prime
            != _fraction_mod_prime(rational_parameter, prime)
        ):
            raise AssertionError(
                "terminating integer parameters do not match modulo p"
            )
    return residues


def bailey_terminating_tail_sum(prime: int) -> Fraction:
    """Return S_M=3F2(-M,-M,4M;M+1,3M;1) as an exact rational."""
    _, _, M = _require_third_index_prime(prime)
    total = Fraction(0, 1)
    for j in range(M + 1):
        total += (
            _pochhammer(Fraction(-M, 1), j) ** 2
            * _pochhammer(Fraction(4 * M, 1), j)
            / (
                _pochhammer(Fraction(M + 1, 1), j)
                * _pochhammer(Fraction(3 * M, 1), j)
                * factorial(j)
            )
        )
    return total


def bailey_symmetric_tail_factor(prime: int) -> Fraction:
    """Return the exact prefactor (2M+1)_M/(M+1)_M."""
    _, _, M = _require_third_index_prime(prime)
    return (
        _pochhammer(Fraction(2 * M + 1, 1), M)
        / _pochhammer(Fraction(M + 1, 1), M)
    )


def bailey_symmetric_tail_sum(prime: int) -> Fraction:
    """Return T_M=3F2(-M,-M,-M;-3M,3M;1) exactly."""
    _, _, M = _require_third_index_prime(prime)
    total = Fraction(0, 1)
    for j in range(M + 1):
        total += (
            _pochhammer(Fraction(-M, 1), j) ** 3
            / (
                _pochhammer(Fraction(-3 * M, 1), j)
                * _pochhammer(Fraction(3 * M, 1), j)
                * factorial(j)
            )
        )
    return total


def bailey_symmetric_binomial_denominator(truncation: int) -> int:
    """Return D_M=C(3M,M)C(4M-1,M), the natural integer denominator."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    return comb(3 * M, M) * comb(4 * M - 1, M)


def bailey_symmetric_integer_sum(truncation: int) -> int:
    """Return U_M=sum C(M,k)C(2M+k,k)C(4M-1,k)."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    return sum(
        comb(M, k) * comb(2 * M + k, k) * comb(4 * M - 1, k)
        for k in range(M + 1)
    )


def bailey_symmetric_integer_identity(prime: int) -> tuple[int, int, int]:
    """Return (D_M,U_M,D_M*T_M numerator) and certify exact integerization."""
    _, _, M = _require_third_index_prime(prime)
    denominator = bailey_symmetric_binomial_denominator(M)
    integer_sum = bailey_symmetric_integer_sum(M)
    scaled = bailey_symmetric_tail_sum(prime) * denominator
    if scaled.denominator != 1 or scaled.numerator != integer_sum:
        raise AssertionError("symmetric tail binomial integerization failed")
    if denominator % prime == 0:
        raise AssertionError("natural symmetric denominator must be a p-unit")
    return denominator, integer_sum, scaled.numerator


def bailey_dual_hahn_parameters(prime: int) -> tuple[int, int, int, int, int, int]:
    """Return (degree,y,gamma,delta,N,lambda(y)) for the dual-Hahn diagonal."""
    _, _, M = _require_third_index_prime(prime)
    degree = M
    y = M
    gamma = 3 * M - 1
    delta = -5 * M
    N = 3 * M
    argument = -M * M
    if y * (y + gamma + delta + 1) != argument:
        raise AssertionError("dual-Hahn spectral argument changed")
    return degree, y, gamma, delta, N, argument


def bailey_symmetric_transform(prime: int) -> tuple[Fraction, Fraction]:
    """Certify the exact terminating Weber--Erdelyi 3F2 transform."""
    terminating = bailey_terminating_tail_sum(prime)
    transformed = (
        bailey_symmetric_tail_factor(prime)
        * bailey_symmetric_tail_sum(prime)
    )
    if terminating != transformed:
        raise AssertionError("terminating 3F2 symmetrization failed")
    return terminating, transformed


def bailey_symmetric_tail_residue(prime: int) -> tuple[int, int, int]:
    """Return (S_M, prefactor, T_M) modulo p with a unit prefactor."""
    terminating, _ = bailey_symmetric_transform(prime)
    factor = bailey_symmetric_tail_factor(prime)
    symmetric = bailey_symmetric_tail_sum(prime)
    terminating_residue = _fraction_mod_prime(terminating, prime)
    factor_residue = _fraction_mod_prime(factor, prime)
    symmetric_residue = _fraction_mod_prime(symmetric, prime)
    if factor_residue == 0:
        raise AssertionError("symmetric terminating prefactor must be a p-unit")
    if terminating_residue != factor_residue * symmetric_residue % prime:
        raise AssertionError("symmetric terminating residues disagree")
    return terminating_residue, factor_residue, symmetric_residue


def third_index_zero_via_integer_sum(prime: int) -> bool:
    """Certify one-third Franel divisibility by the integer sum U_M."""
    _, integer_sum, _ = bailey_symmetric_integer_identity(prime)
    predicted = integer_sum % prime == 0
    actual = third_index_zero_via_symmetric_tail(prime)
    if actual != predicted:
        raise AssertionError("integerized tail and Franel zero disagree")
    return actual


def third_index_zero_via_symmetric_tail(prime: int) -> bool:
    """Certify one-third Franel divisibility via the symmetric tail T_M."""
    terminating, _, symmetric = bailey_symmetric_tail_residue(prime)
    predicted = symmetric == 0
    if (terminating == 0) != predicted:
        raise AssertionError("unit prefactor must preserve tail vanishing")
    actual = third_index_zero_via_bailey_tail(prime)
    if actual != predicted:
        raise AssertionError("symmetric tail and Franel zero disagree")
    return actual


def bailey_tail_modular_bridge(prime: int) -> tuple[int, int]:
    """Return the equal mod-p residues of H_d and the terminating S_M."""
    _, offset, _ = _require_third_index_prime(prime)
    rational_tail = _fraction_mod_prime(
        bailey_pole_tail_sum(offset),
        prime,
    )
    terminating_tail = _fraction_mod_prime(
        bailey_terminating_tail_sum(prime),
        prime,
    )
    if rational_tail != terminating_tail:
        raise AssertionError("Bailey rational and terminating tails must agree mod p")
    return rational_tail, terminating_tail


def bailey_pole_tail_residue(prime: int) -> tuple[int, int, int, int]:
    """Return (rank,d,C_d mod p,H_d mod p) and certify F_r=-C_d H_d."""
    rank, offset, _ = _require_third_index_prime(prime)
    unit = _fraction_mod_prime(bailey_pole_tail_unit(offset), prime)
    tail, terminating_tail = bailey_tail_modular_bridge(prime)
    if tail != terminating_tail:
        raise AssertionError("Bailey tail bridge failed")
    actual = triple_moment_factor(rank) % prime
    predicted = (-unit * tail) % prime
    if unit == 0:
        raise AssertionError("the extracted Bailey prefactor must be a p-adic unit")
    if actual != predicted:
        raise AssertionError(
            "Bailey pole-tail reduction disagrees with the Franel value"
        )
    return rank, offset, unit, tail


def third_index_zero_via_bailey_tail(prime: int) -> bool:
    """Certify p|F_((p+1)/3) iff the universal Bailey tail vanishes mod p."""
    rank, _, _, tail = bailey_pole_tail_residue(prime)
    actual = triple_moment_factor(rank) % prime == 0
    predicted = tail == 0
    if actual != predicted:
        raise AssertionError("Bailey tail zero equivalence failed")
    return actual
