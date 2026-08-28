"""N-only valuation-wall GCD extractor domain operator.

This module packages the accepted PCF4R theorem as a reusable executable
operator under the existing T1 scale/enumeration/valuation family.  It is not a
new global tool family and it is not a factoring-speedup claim.

Promised theorem domain:
    N = p*q with distinct odd primes 3 < p < q.

Constructor-side inputs are only N and public constants. Hidden factors are not
used to choose seeds, recurrence indices, or branches.

Hard boundaries:
- correctness as a universal theorem is only claimed on the promised semiprime
  domain above;
- the current implementation streams Theta(p) recurrence steps in the worst
  case, hence remains exponential in input bit length for balanced semiprimes;
- this operator is research-level tooling and does not imply Foundation or
  Working Truth promotion.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import gcd, isqrt
from typing import Any, Literal

from .legendre import is_prime


THEOREM_NODE = "EXACT_N_ONLY_GCD_EXTRACTOR_THEOREM"
THEOREM_PACKAGE = (
    "research_notes/"
    "PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_THEOREM_PACKAGE_20260828.md"
)
METHOD_ID = "t1.nonly_valuation_wall_gcd_extractor"

FactorMode = Literal["DENOMINATOR", "DYADIC", "FALLBACK_T", "FALLBACK_T1"]


@dataclass(frozen=True)
class NOnlyValuationWallFactorCertificate:
    """Public certificate emitted by :func:`factor_nonly_valuation_wall`.

    ``first_nonunit_seed`` is the first dyadic seed whose gcd with the streamed
    observable is nonunit.  ``factor_seed`` is the seed that actually exposes
    the proper factor; they differ only in a synchronized fallback branch.
    """

    N: int
    factor: int
    cofactor: int
    mode: FactorMode
    first_nonunit_seed: int
    factor_seed: int
    fallback_t: int | None
    dyadic_trace: tuple[tuple[int, int], ...]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _require_promised_input_shape(N: int) -> None:
    """Reject inputs that visibly violate the promised-domain public shape.

    This deliberately does not try to prove that N is a product of two distinct
    primes; doing so would itself be a factoring/recognition problem.  The
    theorem promise remains a caller-side precondition.
    """

    if N <= 1:
        raise ValueError("N must be greater than 1")
    if N % 2 == 0 or gcd(N, 6) != 1:
        raise ValueError("promised inputs are odd and coprime to 6")


def valuation_wall_threshold(r: int) -> int:
    """Return the exact first activation index ceil(r/3) for prime r>3."""

    if r <= 3 or not is_prime(r):
        raise ValueError("r must be a prime greater than 3")
    return (r + 2) // 3


def local_valuation_wall_certificate(s: int, r: int) -> dict[str, Any]:
    """Return the exact PCF4R local valuation-wall certificate.

    Preconditions are checked literally: ``r`` must be prime, ``r>3``, and
    ``0<=s<r``.  The theorem then gives

        v_r(A_s) = floor(2s/r) + floor(3s/r),

    for A_s=(2s)!(3s)!/(s!)^5.
    """

    if r <= 3 or not is_prime(r):
        raise ValueError("r must be a prime greater than 3")
    if s < 0 or s >= r:
        raise ValueError("local valuation wall requires 0 <= s < r")

    exponent = (2 * s) // r + (3 * s) // r
    threshold = valuation_wall_threshold(r)
    divides = exponent > 0
    if divides != (s >= threshold):
        raise AssertionError("valuation-wall threshold mismatch")
    return {
        "operator": "local_valuation_wall_certificate",
        "s": s,
        "prime": r,
        "valuation_exponent": exponent,
        "threshold": threshold,
        "divides": divides,
        "core_law": "v_r(A_s)=floor(2s/r)+floor(3s/r)",
        "hard_boundary": "valid only for prime r>3 and 0<=s<r",
    }


def activation_wall_synchronization_certificate(
    previous_seed: int,
    current_seed: int,
    *,
    coefficient: int = 3,
) -> dict[str, Any]:
    """Expose the generic activation-wall synchronization inequalities.

    If a hidden-factor activation law has the form ``r | X_s iff c*s >= r``, a
    previous unit probe at ``u`` and a current total-gcd probe at ``s`` imply

        c*u < p < q <= c*s.

    The ratio consequence is ``q/p < s/u``.  For dyadic PCF4R probes this is
    the accepted ``q<2p`` certificate.
    """

    if previous_seed <= 0:
        raise ValueError("previous_seed must be positive")
    if current_seed <= previous_seed:
        raise ValueError("current_seed must exceed previous_seed")
    if coefficient <= 0:
        raise ValueError("coefficient must be positive")

    return {
        "operator": "activation_wall_synchronization_certificate",
        "previous_seed": previous_seed,
        "current_seed": current_seed,
        "coefficient": coefficient,
        "p_lower_exclusive": coefficient * previous_seed,
        "q_upper_inclusive": coefficient * current_seed,
        "schedule_ratio_numerator": current_seed,
        "schedule_ratio_denominator": previous_seed,
        "strict_ratio_law": "q/p < current_seed/previous_seed",
        "pcf4r_q_lt_2p": current_seed == 2 * previous_seed and coefficient == 3,
        "hard_boundary": (
            "This is a consequence operator for an already-proved exact activation law; "
            "it does not establish that law for an arbitrary sequence."
        ),
    }


def valuation_wall_step_mod(a_previous: int, s: int, N: int) -> tuple[int | None, int]:
    """Advance A_s modulo N, or expose a denominator gcd before inversion.

    The exact recurrence is

        A_s/A_(s-1) = 6(2s-1)(3s-2)(3s-1)/s^3.

    The returned pair is ``(new_residue, 1)`` when ``s`` is a unit modulo N.
    If ``gcd(s,N)>1``, the function returns ``(None, gcd(s,N))`` and performs no
    modular inversion.
    """

    if s <= 0:
        raise ValueError("s must be positive")
    if N <= 1:
        raise ValueError("N must be greater than 1")

    denominator_gcd = gcd(s, N)
    if denominator_gcd != 1:
        return None, denominator_gcd

    numerator = 6 * (2 * s - 1) * (3 * s - 2) * (3 * s - 1) % N
    denominator = pow(s, 3, N)
    residue = a_previous % N
    residue = residue * numerator * pow(denominator, -1, N) % N
    return residue, 1


def _certificate(
    N: int,
    factor: int,
    mode: FactorMode,
    first_nonunit_seed: int,
    factor_seed: int,
    fallback_t: int | None,
    dyadic_trace: list[tuple[int, int]],
) -> NOnlyValuationWallFactorCertificate:
    if not (1 < factor < N) or N % factor != 0:
        raise AssertionError("attempted to freeze a non-factor certificate")
    return NOnlyValuationWallFactorCertificate(
        N=N,
        factor=factor,
        cofactor=N // factor,
        mode=mode,
        first_nonunit_seed=first_nonunit_seed,
        factor_seed=factor_seed,
        fallback_t=fallback_t,
        dyadic_trace=tuple(dyadic_trace),
    )


def factor_nonly_valuation_wall(N: int) -> NOnlyValuationWallFactorCertificate:
    """Return a nontrivial factor on the promised PCF4R semiprime domain.

    The constructor sees only ``N``.  It streams the public factorial observable
    modulo N, probes only public dyadic indices, and uses the public
    ``floor(sqrt(N)/3), +1`` fallback if the first nonunit dyadic gcd equals N.

    A ``RuntimeError`` means the supplied input did not follow the promised-domain
    theorem path or the implementation invariant was violated; it must not be
    interpreted as a counterexample without separately checking the domain promise.
    """

    _require_promised_input_shape(N)

    root = isqrt(N)
    fallback_t = root // 3
    residue = 1
    saved: dict[int, int] = {}
    dyadic_trace: list[tuple[int, int]] = []

    for s in range(1, root + 1):
        next_residue, denominator_gcd = valuation_wall_step_mod(residue, s, N)
        if denominator_gcd != 1:
            if 1 < denominator_gcd < N:
                return _certificate(
                    N,
                    denominator_gcd,
                    "DENOMINATOR",
                    s,
                    s,
                    None,
                    dyadic_trace,
                )
            raise RuntimeError("unexpected total denominator gcd")

        if next_residue is None:
            raise AssertionError("unit denominator path did not return a residue")
        residue = next_residue

        if s == fallback_t or s == fallback_t + 1:
            saved[s] = residue

        if s & (s - 1):
            continue

        g = gcd(residue, N)
        dyadic_trace.append((s, g))
        if 1 < g < N:
            return _certificate(N, g, "DYADIC", s, s, None, dyadic_trace)
        if g != N:
            continue

        sync = activation_wall_synchronization_certificate(s // 2, s)
        if not sync["pcf4r_q_lt_2p"]:
            raise AssertionError("dyadic synchronization certificate failed")
        if fallback_t not in saved or fallback_t + 1 not in saved:
            raise RuntimeError(
                "synchronized branch violated the promised-domain fallback ordering"
            )

        at_t = gcd(saved[fallback_t], N)
        if 1 < at_t < N:
            return _certificate(
                N,
                at_t,
                "FALLBACK_T",
                s,
                fallback_t,
                fallback_t,
                dyadic_trace,
            )

        at_t1 = gcd(saved[fallback_t + 1], N)
        if 1 < at_t1 < N:
            return _certificate(
                N,
                at_t1,
                "FALLBACK_T1",
                s,
                fallback_t + 1,
                fallback_t,
                dyadic_trace,
            )

        raise RuntimeError(
            "synchronized fallback failed; verify the distinct-prime promised domain"
        )

    raise RuntimeError(
        "no valuation-wall stop before isqrt(N); verify the promised semiprime domain"
    )


def verify_nonly_valuation_wall_certificate(
    certificate: NOnlyValuationWallFactorCertificate,
    *,
    replay: bool = False,
) -> bool:
    """Check the public arithmetic certificate, optionally replaying the operator.

    This function validates the emitted factor relation and structural fields. It
    does not independently prove the caller's semiprime promise.  ``replay=True``
    reruns the N-only constructor and requires the same factor/mode/seed outcome.
    """

    if certificate.N <= 1:
        return False
    if not (1 < certificate.factor < certificate.N):
        return False
    if certificate.N % certificate.factor != 0:
        return False
    if certificate.cofactor != certificate.N // certificate.factor:
        return False
    if certificate.first_nonunit_seed <= 0 or certificate.factor_seed <= 0:
        return False
    if certificate.mode in {"FALLBACK_T", "FALLBACK_T1"}:
        if certificate.fallback_t is None:
            return False
        if certificate.factor_seed not in {
            certificate.fallback_t,
            certificate.fallback_t + 1,
        }:
            return False
    elif certificate.fallback_t is not None:
        return False

    if replay:
        fresh = factor_nonly_valuation_wall(certificate.N)
        return (
            fresh.factor == certificate.factor
            and fresh.mode == certificate.mode
            and fresh.first_nonunit_seed == certificate.first_nonunit_seed
            and fresh.factor_seed == certificate.factor_seed
        )
    return True


__all__ = [
    "THEOREM_NODE",
    "THEOREM_PACKAGE",
    "METHOD_ID",
    "NOnlyValuationWallFactorCertificate",
    "valuation_wall_threshold",
    "local_valuation_wall_certificate",
    "activation_wall_synchronization_certificate",
    "valuation_wall_step_mod",
    "factor_nonly_valuation_wall",
    "verify_nonly_valuation_wall_certificate",
]
