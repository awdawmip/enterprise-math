"""Exact paired-Pell shell certificates extracted from the precision-pi paper.

The tool is integer/rational only.  It verifies a shared square coordinate ``P``
against one positive Pell shell and one negative Pell shell and exposes the
forced fourth-order factorization.  It does not derive any modular or Ramanujan
identity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from numbers import Integral


def _int(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be an integer")
    return int(value)


@dataclass(frozen=True)
class PairedPellCertificate:
    P: int
    d_positive: int
    y_positive: int
    d_negative: int
    y_negative: int
    positive_shell: int
    negative_shell: int
    fourth_residual: int
    fused_shell: int

    @property
    def fugacity(self) -> Fraction:
        if self.P == 0:
            raise ZeroDivisionError("P=0 has no P^-4 fugacity")
        return Fraction(1, self.P**4)


def paired_pell_certificate(
    P: int,
    d_positive: int,
    y_positive: int,
    d_negative: int,
    y_negative: int,
) -> PairedPellCertificate:
    """Verify a common-``P`` positive/negative Pell pair exactly.

    Required equations are

    ``P^2 - d_positive*y_positive^2 = +1`` and
    ``P^2 - d_negative*y_negative^2 = -1``.

    The returned certificate checks
    ``P^4-1=(P^2-1)(P^2+1)=d_positive*d_negative*(y_positive*y_negative)^2``.
    """
    P = _int(P, "P")
    d_positive = _int(d_positive, "d_positive")
    y_positive = _int(y_positive, "y_positive")
    d_negative = _int(d_negative, "d_negative")
    y_negative = _int(y_negative, "y_negative")
    if min(d_positive, d_negative) <= 0:
        raise ValueError("Pell discriminants must be positive")
    positive_shell = P**2 - 1
    negative_shell = P**2 + 1
    if P**2 - d_positive * y_positive**2 != 1:
        raise ValueError("positive Pell certificate failed")
    if P**2 - d_negative * y_negative**2 != -1:
        raise ValueError("negative Pell certificate failed")
    fourth_residual = P**4 - 1
    fused_shell = d_positive * d_negative * (y_positive * y_negative) ** 2
    if positive_shell * negative_shell != fourth_residual:
        raise AssertionError("fourth-residual factorization failed")
    if fused_shell != fourth_residual:
        raise AssertionError("paired Pell fusion failed")
    return PairedPellCertificate(
        P=P,
        d_positive=d_positive,
        y_positive=y_positive,
        d_negative=d_negative,
        y_negative=y_negative,
        positive_shell=positive_shell,
        negative_shell=negative_shell,
        fourth_residual=fourth_residual,
        fused_shell=fused_shell,
    )


def n58_certificate() -> PairedPellCertificate:
    """Return the exact ``P=99`` pair used in the N=58 case."""
    return paired_pell_certificate(99, 2, 70, 58, 13)


def n58_integer_constants() -> dict[str, int | bool]:
    """Verify and expose the integer identities behind the N=58 paper example."""
    certificate = n58_certificate()
    values: dict[str, int | bool] = {
        "P": certificate.P,
        "four_times_P": 4 * certificate.P,
        "P_squared": certificate.P**2,
        "ramanujan_linear_n": 29 * 70 * 13,
        "ramanujan_constant": 1103,
        "pell_positive": certificate.P**2 - 2 * 70**2 == 1,
        "pell_negative": certificate.P**2 - 58 * 13**2 == -1,
    }
    values["ramanujan_constant_certificate"] = (
        4 * int(values["ramanujan_constant"])
        == int(values["ramanujan_linear_n"])
        - 2 * certificate.P * (certificate.P + 13 - 1)
    )
    if values["four_times_P"] != 396:
        raise AssertionError("396 certificate failed")
    if values["P_squared"] != 9801:
        raise AssertionError("9801 certificate failed")
    if values["ramanujan_linear_n"] != 26390:
        raise AssertionError("26390 certificate failed")
    if not values["ramanujan_constant_certificate"]:
        raise AssertionError("1103 certificate failed")
    return values


def n58_ratio_certificate() -> Fraction:
    """Return the exact geometric ratio certificate ``25/99^4``."""
    return Fraction(25, 99**4)


def geometric_tail_bound(first_omitted: Fraction | int, q: Fraction) -> Fraction:
    """Return ``first_omitted/(1-q)`` for a nonnegative geometric majorant."""
    first = Fraction(first_omitted)
    q = Fraction(q)
    if first < 0:
        raise ValueError("first omitted term must be nonnegative")
    if q < 0 or q >= 1:
        raise ValueError("q must satisfy 0 <= q < 1")
    return first / (1 - q)
