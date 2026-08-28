"""Three-section normalization of the P022 sign-free boundary kernel.

At the Driver-routed boundary write M=3m and q=18m-1.  The sign-free
kernel is

    W_M = sum_{0<=j<2M} C(2M,j) C(M+j,j) C(2M-1,j).

Splitting j=3k+a (a=0,1,2) produces three sums of exactly 2m terms.
After triplication, all three are contiguous realizations of the same
rank-nine cyclotomic hypergeometric datum modulo q.  The common fractional
upper/lower signatures are

    alpha = {1/18,7/18,13/18, 2/9,2/9,5/9,5/9,8/9,8/9},
    beta  = {0,0,0, 1/3,1/3,1/3, 2/3,2/3,2/3}.

Because q == -1 (mod 18), Dwork dash on these fractional parameters is
complementation a -> 1-a and therefore has period two.  This is a structural
reduction only; it does not prove W_(3m) nonzero.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb

from .p022_barlow_low_order_defect_reduction import _is_prime


COMMON_ALPHA_MOD_ONE = tuple(
    sorted(
        (
            Fraction(1, 18),
            Fraction(7, 18),
            Fraction(13, 18),
            Fraction(2, 9),
            Fraction(2, 9),
            Fraction(5, 9),
            Fraction(5, 9),
            Fraction(8, 9),
            Fraction(8, 9),
        )
    )
)
COMMON_BETA_MOD_ONE = tuple(
    sorted(
        (
            Fraction(0, 1),
            Fraction(0, 1),
            Fraction(0, 1),
            Fraction(1, 3),
            Fraction(1, 3),
            Fraction(1, 3),
            Fraction(2, 3),
            Fraction(2, 3),
            Fraction(2, 3),
        )
    )
)


def _require_positive_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def boundary_term(scale: int, index: int) -> int:
    """Return w_j for M=3m."""
    _require_positive_integer("scale", scale)
    m = scale
    M = 3 * m
    if isinstance(index, bool) or not isinstance(index, int) or not (0 <= index < 2 * M):
        raise ValueError("index must satisfy 0 <= index < 6*scale")
    j = index
    return comb(2 * M, j) * comb(M + j, j) * comb(2 * M - 1, j)


def boundary_three_sections(scale: int) -> tuple[int, int, int]:
    """Return the three exact integer sums indexed by j modulo 3."""
    _require_positive_integer("scale", scale)
    sections = [0, 0, 0]
    for j in range(6 * scale):
        sections[j % 3] += boundary_term(scale, j)
    return tuple(sections)


def section_term_counts(scale: int) -> tuple[int, int, int]:
    """Each residue section has the same exact horizon 2m."""
    _require_positive_integer("scale", scale)
    return tuple(
        sum(1 for j in range(6 * scale) if j % 3 == residue)
        for residue in range(3)
    )


def section_hypergeometric_parameters(
    scale: int, residue: int
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Return exact 9F8 upper/lower parameters before reducing modulo q.

    One lower parameter equal to 1 is omitted because it is the standard k!
    factor of the hypergeometric series.
    """
    _require_positive_integer("scale", scale)
    if residue not in (0, 1, 2):
        raise ValueError("residue must be 0, 1, or 2")
    m = scale
    a = residue
    sources = (-6 * m, 1 - 6 * m, 3 * m + 1)
    upper = tuple(
        Fraction(source + a + shift, 3)
        for source in sources
        for shift in range(3)
    )
    lower_full = [
        Fraction(a + shift, 3)
        for _ in range(3)
        for shift in (1, 2, 3)
    ]
    lower_full.remove(Fraction(1, 1))
    return upper, tuple(lower_full)


def fractional_signature(values: tuple[Fraction, ...], include_hypergeom_one: bool = False) -> tuple[Fraction, ...]:
    """Reduce rational parameters modulo Z into [0,1)."""
    reduced = [value % 1 for value in values]
    if include_hypergeom_one:
        reduced.append(Fraction(0, 1))
    return tuple(sorted(reduced))


def common_cyclotomic_signature(scale: int) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Certify that all three sections share the same conductor-18 signature."""
    _require_positive_integer("scale", scale)
    prime = 18 * scale - 1
    # The signature is an identity after substituting m == 1/18 (mod q), so
    # prime need not be used arithmetically here.  Requiring q prime pins the
    # exact live P022 boundary where the modular interpretation is valid.
    if not _is_prime(prime):
        raise ValueError("18*scale-1 must be prime")

    signatures = []
    for residue in range(3):
        upper, lower = section_hypergeometric_parameters(scale, residue)
        # Substitute m -> 1/18 modulo q at the parameter level.  Equivalently,
        # replace the scale-dependent parameters by their q-congruent rational
        # representatives and then reduce modulo integers.
        # We compute this directly from the closed representatives.
        a = residue
        m0 = Fraction(1, 18)
        sources = (-6 * m0, 1 - 6 * m0, 3 * m0 + 1)
        upper_q = tuple(
            (source + a + shift) / 3
            for source in sources
            for shift in range(3)
        )
        upper_sig = fractional_signature(upper_q)
        lower_sig = fractional_signature(lower, include_hypergeom_one=True)
        signatures.append((upper_sig, lower_sig))

    if len(set(signatures)) != 1:
        raise AssertionError("three sections do not share one cyclotomic signature")
    alpha, beta = signatures[0]
    if alpha != COMMON_ALPHA_MOD_ONE or beta != COMMON_BETA_MOD_ONE:
        raise AssertionError("conductor-18 signature changed")
    return alpha, beta


def dwork_complement_signature() -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Return the q == -1 (mod 18) dash-conjugate signature."""
    alpha = tuple(sorted((1 - value) % 1 for value in COMMON_ALPHA_MOD_ONE))
    beta = tuple(sorted((1 - value) % 1 for value in COMMON_BETA_MOD_ONE))
    return alpha, beta


def dwork_period_two_certificate() -> bool:
    """Complementation twice returns the original conductor-18 datum."""
    alpha1, beta1 = dwork_complement_signature()
    alpha2 = tuple(sorted((1 - value) % 1 for value in alpha1))
    beta2 = tuple(sorted((1 - value) % 1 for value in beta1))
    return alpha2 == COMMON_ALPHA_MOD_ONE and beta2 == COMMON_BETA_MOD_ONE


def boundary_three_section_mod_prime(scale: int) -> tuple[int, int, int, int]:
    """Return (q,W0,W1,W2) modulo q for q=18m-1 prime."""
    _require_positive_integer("scale", scale)
    prime = 18 * scale - 1
    if not _is_prime(prime):
        raise ValueError("18*scale-1 must be prime")
    sections = boundary_three_sections(scale)
    return (prime, *(value % prime for value in sections))
