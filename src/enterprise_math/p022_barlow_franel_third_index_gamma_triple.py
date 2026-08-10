"""Cyclotomic gamma-triple and Dwork-cycle structure for the one-third datum.

The fixed classical obstruction uses the hypergeometric parameters

    alpha = (5/6, 1/3, 1/3),   beta = (1,1,1).

They are defined over Q(zeta_6), not over Q.  Abdelraouf's gamma-triple
formalism applies to such cyclotomic data.  This module records an explicit
N=6 representation satisfying the zero-delta-sum condition needed by the
geometric realization, together with the exact rational Galois closure.

For primes p=5 mod 6, Dwork's dash operation has period two on the datum:

    (5/6,1/3,1/3) <-> (1/6,2/3,2/3).

Thus q=p^2 is the first residue-field size for which 6 divides q-1, matching
the inert-prime geometry over Q(zeta_6).  No claim is made here that the
classical truncated obstruction is already identified with a specific
Frobenius matrix entry; that bridge remains open.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd

from .p022_barlow_low_order_defect_reduction import _is_prime

THIRD_INDEX_ALPHA = (Fraction(5, 6), Fraction(1, 3), Fraction(1, 3))
THIRD_INDEX_BETA = (Fraction(1), Fraction(1), Fraction(1))
THIRD_INDEX_CONJUGATE_ALPHA = (
    Fraction(1, 6),
    Fraction(2, 3),
    Fraction(2, 3),
)

# Proposition-2.15-style representation.  The last three entries form an
# empty gamma block: (T^2-1)/((T-1)(T+1))=1.
THIRD_INDEX_GAMMA = (-1, -1, -1, 1, 1, 1, -2, 1, 1)
THIRD_INDEX_DELTA = (5, 2, 2, -6, -6, -6, 0, 0, 3)
THIRD_INDEX_CYCLOTOMIC_ORDER = 6

# Exact Q-rational Galois closure:
# Phi_6 Phi_3^2 / Phi_1^6 = (T^6-1)(T^3-1)/((T^2-1)(T-1)^7).
THIRD_INDEX_CLOSURE_GAMMA = (-6, -3, 2, 1, 1, 1, 1, 1, 1, 1)
THIRD_INDEX_CLOSURE_DELTA = (0,) * len(THIRD_INDEX_CLOSURE_GAMMA)
THIRD_INDEX_CLOSURE_ALPHA = tuple(
    sorted(THIRD_INDEX_ALPHA + THIRD_INDEX_CONJUGATE_ALPHA)
)
THIRD_INDEX_CLOSURE_BETA = (Fraction(1),) * 6


def _phase_mod_one(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def _factor_root_phases(length: int, phase: Fraction) -> tuple[Fraction, ...]:
    return tuple(
        _phase_mod_one((phase + step) / length)
        for step in range(length)
    )


def represented_parameters(
    gamma: tuple[int, ...],
    delta: tuple[int, ...],
    cyclotomic_order: int,
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Recover reduced alpha/beta multisets from a gamma triple exactly."""
    if len(gamma) != len(delta) or not gamma:
        raise ValueError("gamma and delta must have the same positive length")
    if cyclotomic_order <= 0:
        raise ValueError("cyclotomic_order must be positive")
    if any(value == 0 for value in gamma):
        raise ValueError("gamma entries must be nonzero")

    numerator: Counter[Fraction] = Counter()
    denominator: Counter[Fraction] = Counter()
    for exponent, shift in zip(gamma, delta):
        if exponent < 0:
            phase = _phase_mod_one(Fraction(shift, cyclotomic_order))
            numerator.update(_factor_root_phases(-exponent, phase))
        else:
            phase = _phase_mod_one(Fraction(-shift, cyclotomic_order))
            denominator.update(_factor_root_phases(exponent, phase))

    for phase in tuple(set(numerator) | set(denominator)):
        cancellation = min(numerator[phase], denominator[phase])
        numerator[phase] -= cancellation
        denominator[phase] -= cancellation
        if numerator[phase] == 0:
            del numerator[phase]
        if denominator[phase] == 0:
            del denominator[phase]

    def conventional(counter: Counter[Fraction]) -> tuple[Fraction, ...]:
        values: list[Fraction] = []
        for phase, multiplicity in counter.items():
            parameter = Fraction(1) if phase == 0 else phase
            values.extend([parameter] * multiplicity)
        return tuple(sorted(values))

    return conventional(numerator), conventional(denominator)


def third_index_gamma_triple_certificate() -> bool:
    """Certify representation, balancing, and primitive 2x2-minor lattice."""
    alpha, beta = represented_parameters(
        THIRD_INDEX_GAMMA,
        THIRD_INDEX_DELTA,
        THIRD_INDEX_CYCLOTOMIC_ORDER,
    )
    if alpha != tuple(sorted(THIRD_INDEX_ALPHA)) or beta != THIRD_INDEX_BETA:
        raise AssertionError("gamma triple does not represent the one-third datum")
    if sum(THIRD_INDEX_GAMMA) != 0:
        raise AssertionError("gamma vector must sum to zero")
    if sum(THIRD_INDEX_DELTA) % THIRD_INDEX_CYCLOTOMIC_ORDER != 0:
        raise AssertionError("delta sum must vanish modulo the cyclotomic order")

    minor_gcd = 0
    for left in range(len(THIRD_INDEX_GAMMA)):
        for right in range(left + 1, len(THIRD_INDEX_GAMMA)):
            minor = (
                THIRD_INDEX_GAMMA[left] * THIRD_INDEX_DELTA[right]
                - THIRD_INDEX_GAMMA[right] * THIRD_INDEX_DELTA[left]
            )
            minor_gcd = gcd(minor_gcd, abs(minor))
    if minor_gcd != 1:
        raise AssertionError("gamma/delta maximal-minor gcd must be one")
    return True


def gamma_power() -> Fraction:
    """Return gamma^gamma for the explicit rank-three representation."""
    result = Fraction(1)
    for value in THIRD_INDEX_GAMMA:
        result *= Fraction(value) ** value
    if result != Fraction(-1, 4):
        raise AssertionError("gamma^gamma changed")
    return result


def dwork_dash(value: Fraction, prime: int) -> Fraction:
    """Dwork dash x*=(x+<-x>_p)/p for rational p-adic units."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if value.denominator % prime == 0:
        raise ValueError("value denominator must be a p-adic unit")
    residue = (
        -value.numerator * pow(value.denominator % prime, -1, prime)
    ) % prime
    return (value + residue) / prime


def third_index_dash_cycle(prime: int) -> tuple[tuple[Fraction, ...], ...]:
    """Certify the period-two Dwork cycle for p=5 mod 6."""
    if not _is_prime(prime) or prime % 6 != 5:
        raise ValueError("prime must be 5 modulo 6")
    first = tuple(sorted(dwork_dash(value, prime) for value in THIRD_INDEX_ALPHA))
    second = tuple(sorted(dwork_dash(value, prime) for value in first))
    if first != tuple(sorted(THIRD_INDEX_CONJUGATE_ALPHA)):
        raise AssertionError("first dash must give the Galois conjugate datum")
    if second != tuple(sorted(THIRD_INDEX_ALPHA)):
        raise AssertionError("second dash must return the original datum")
    return tuple(sorted(THIRD_INDEX_ALPHA)), first, second


def inert_residue_field_size(prime: int) -> int:
    """Return p^2, the first size with 6|(q-1) for p=5 mod 6."""
    third_index_dash_cycle(prime)
    if (prime - 1) % 6 == 0:
        raise AssertionError("p=5 mod 6 cannot already contain sixth roots")
    residue_size = prime * prime
    if (residue_size - 1) % 6 != 0:
        raise AssertionError("p^2-1 must be divisible by six")
    return residue_size


def rational_galois_closure_certificate() -> bool:
    """Certify the exact rank-six cyclotomic closure over Q."""
    alpha, beta = represented_parameters(
        THIRD_INDEX_CLOSURE_GAMMA,
        THIRD_INDEX_CLOSURE_DELTA,
        1,
    )
    if alpha != THIRD_INDEX_CLOSURE_ALPHA or beta != THIRD_INDEX_CLOSURE_BETA:
        raise AssertionError("rational closure gamma vector changed")
    if sum(THIRD_INDEX_CLOSURE_GAMMA) != 0:
        raise AssertionError("rational closure gamma vector must balance")
    return True


def ehmm_direct_gamma_barrier() -> Fraction:
    """Return n-2+q_n-sum(alpha)=1/2 for the direct length-three datum.

    The EHMM theorem currently audited requires this quantity to be at least
    one, so its published sufficient criterion does not directly apply.
    """
    value = Fraction(3 - 2) + Fraction(1) - sum(THIRD_INDEX_ALPHA)
    if value != Fraction(1, 2):
        raise AssertionError("EHMM gamma barrier changed")
    return value
