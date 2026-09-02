"""Exact research checker for projective/gauge-compensated Weighted-BRC quotienting.

All checks use non-negative rational cross multiplication. No logarithm, float,
Decimal, or Fraction is required for projective equivalence or compensation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Ratio:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.numerator < 0 or self.denominator <= 0:
            raise ValueError("invalid ratio")


def add_ratio(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)


def mul_ratio(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.numerator, a.denominator * b.denominator)


def div_positive(a: Ratio, b: Ratio) -> Ratio:
    if a.numerator <= 0 or b.numerator <= 0:
        raise ValueError("positive ratios required")
    return Ratio(a.numerator * b.denominator, a.denominator * b.numerator)


def eq_ratio(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator == b.numerator * a.denominator


def le_ratio(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator <= b.numerator * a.denominator


def lt_ratio(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator < b.numerator * a.denominator


def max_ratio(a: Ratio, b: Ratio) -> Ratio:
    return b if le_ratio(a, b) else a


def scale_ratio(a: Ratio, lam: Ratio) -> Ratio:
    return mul_ratio(a, lam)


def int_scale(a: Ratio, count: int) -> Ratio:
    return Ratio(a.numerator * count, a.denominator)


RZERO = Ratio(0, 1)
RONE = Ratio(1, 1)


@dataclass(frozen=True)
class CWM:
    count: int
    total: Ratio
    maximum: Ratio

    def __post_init__(self) -> None:
        if isinstance(self.count, bool) or not isinstance(self.count, int) or self.count < 0:
            raise ValueError("count must be a non-negative integer")


ZERO = CWM(0, RZERO, RZERO)
ONE = CWM(1, RONE, RONE)


def plus(a: CWM, b: CWM) -> CWM:
    return CWM(a.count + b.count, add_ratio(a.total, b.total), max_ratio(a.maximum, b.maximum))


def times(a: CWM, b: CWM) -> CWM:
    return CWM(a.count * b.count, mul_ratio(a.total, b.total), mul_ratio(a.maximum, b.maximum))


def gauge(lam: Ratio, value: CWM) -> CWM:
    if lam.numerator <= 0:
        raise ValueError("gauge scale must be positive")
    return CWM(value.count, scale_ratio(value.total, lam), scale_ratio(value.maximum, lam))


def equal(a: CWM, b: CWM) -> bool:
    return a.count == b.count and eq_ratio(a.total, b.total) and eq_ratio(a.maximum, b.maximum)


def exact_realizable(value: CWM) -> bool:
    if value.count == 0:
        return value.total.numerator == 0 and value.maximum.numerator == 0
    if value.total.numerator <= 0 or value.maximum.numerator <= 0:
        return False
    if value.count == 1:
        return eq_ratio(value.total, value.maximum)
    return lt_ratio(value.maximum, value.total) and le_ratio(value.total, int_scale(value.maximum, value.count))


def check_scaling_laws() -> int:
    samples = (
        ZERO,
        ONE,
        CWM(1, Ratio(2), Ratio(2)),
        CWM(2, Ratio(3), Ratio(2)),
        CWM(3, Ratio(9, 2), Ratio(2)),
    )
    lambdas = (Ratio(1, 2), Ratio(1), Ratio(2), Ratio(3, 2))
    checks = 0
    for lam, a, b in product(lambdas, samples, samples):
        if not equal(gauge(lam, plus(a, b)), plus(gauge(lam, a), gauge(lam, b))):
            raise AssertionError("gauge scaling must commute with CWM addition")
        if not equal(gauge(lam, times(a, b)), times(gauge(lam, a), b)):
            raise AssertionError("left gauge slide through multiplication failed")
        if not equal(gauge(lam, times(a, b)), times(a, gauge(lam, b))):
            raise AssertionError("right gauge slide through multiplication failed")
        checks += 1
    for lam, mu, value in product(lambdas, lambdas, samples):
        if not equal(gauge(lam, gauge(mu, value)), gauge(mul_ratio(lam, mu), value)):
            raise AssertionError("gauge action composition failed")
    return checks


Signature = tuple[CWM, ...]
NormalizedEntry = tuple[int, Ratio, Ratio]
NormalizedSignature = tuple[NormalizedEntry, ...]


def signature_equal(left: Signature, right: Signature) -> bool:
    return len(left) == len(right) and all(equal(a, b) for a, b in zip(left, right))


def signature_gauge(lam: Ratio, signature: Signature) -> Signature:
    return tuple(gauge(lam, value) for value in signature)


def boolean_signature(signature: Signature) -> tuple[bool, ...]:
    return tuple(value.count > 0 for value in signature)


def projective_scale(left: Signature, right: Signature) -> Ratio | None:
    """Return lambda with right=G_lambda(left), or None when not projectively equal."""
    if len(left) != len(right):
        return None
    if tuple(value.count for value in left) != tuple(value.count for value in right):
        return None
    support = [index for index, value in enumerate(left) if value.count > 0]
    if not support:
        # Dead signatures are handled as one exact class. Use unit scale by convention.
        return RONE if signature_equal(left, right) else None
    anchor = support[0]
    if left[anchor].maximum.numerator <= 0 or right[anchor].maximum.numerator <= 0:
        return None
    lam = div_positive(right[anchor].maximum, left[anchor].maximum)
    for lvalue, rvalue in zip(left, right):
        if lvalue.count == 0:
            if rvalue.count != 0 or rvalue.total.numerator != 0 or rvalue.maximum.numerator != 0:
                return None
            continue
        if not eq_ratio(rvalue.total, scale_ratio(lvalue.total, lam)):
            return None
        if not eq_ratio(rvalue.maximum, scale_ratio(lvalue.maximum, lam)):
            return None
    return lam


def normalized_signature(signature: Signature) -> NormalizedSignature:
    support = [index for index, value in enumerate(signature) if value.count > 0]
    if not support:
        return tuple((value.count, RZERO, RZERO) for value in signature)
    anchor_mass = signature[support[0]].maximum
    if anchor_mass.numerator <= 0:
        raise AssertionError("live signature anchor must have positive max mass")
    result: list[NormalizedEntry] = []
    for value in signature:
        if value.count == 0:
            result.append((0, RZERO, RZERO))
        else:
            result.append(
                (
                    value.count,
                    div_positive(value.total, anchor_mass),
                    div_positive(value.maximum, anchor_mass),
                )
            )
    return tuple(result)


def normalized_equal(left: NormalizedSignature, right: NormalizedSignature) -> bool:
    if len(left) != len(right):
        return False
    for (lc, lw, lm), (rc, rw, rm) in zip(left, right):
        if lc != rc or not eq_ratio(lw, rw) or not eq_ratio(lm, rm):
            return False
    return True


def check_projective_equivalence_and_normalization() -> None:
    base: Signature = (
        CWM(1, Ratio(1), Ratio(1)),
        CWM(2, Ratio(3), Ratio(2)),
        ZERO,
    )
    twice = signature_gauge(Ratio(2), base)
    sixfold = signature_gauge(Ratio(6), base)

    lam_1 = projective_scale(base, base)
    lam_2 = projective_scale(base, twice)
    lam_3 = projective_scale(twice, sixfold)
    if lam_1 is None or not eq_ratio(lam_1, Ratio(1)):
        raise AssertionError("projective reflexivity failed")
    if lam_2 is None or not eq_ratio(lam_2, Ratio(2)):
        raise AssertionError("projective factor 2 not recovered")
    reverse = projective_scale(twice, base)
    if reverse is None or not eq_ratio(reverse, Ratio(1, 2)):
        raise AssertionError("projective symmetry failed")
    if lam_3 is None or not eq_ratio(lam_3, Ratio(3)):
        raise AssertionError("projective transitive factor not recovered")
    direct = projective_scale(base, sixfold)
    if direct is None or not eq_ratio(direct, mul_ratio(lam_2, lam_3)):
        raise AssertionError("projective transitivity factor multiplication failed")

    if not normalized_equal(normalized_signature(base), normalized_signature(twice)):
        raise AssertionError("canonical projective normalization failed")
    if not normalized_equal(normalized_signature(base), normalized_signature(sixfold)):
        raise AssertionError("canonical normalization not scale-invariant")

    inconsistent: Signature = (
        CWM(1, Ratio(2), Ratio(2)),
        CWM(2, Ratio(9), Ratio(6)),  # factor 3 on second target, not factor 2
        ZERO,
    )
    if projective_scale(base, inconsistent) is not None:
        raise AssertionError("one common lambda must serve every target")


def check_incoming_compensation() -> None:
    representative: Signature = (
        CWM(1, Ratio(1), Ratio(1)),
        CWM(2, Ratio(3), Ratio(2)),
    )
    lam = Ratio(2)
    eliminated = signature_gauge(lam, representative)

    incoming = CWM(2, Ratio(3), Ratio(2))
    compensated = gauge(lam, incoming)

    for rep_future, old_future in zip(representative, eliminated):
        original_output = times(incoming, old_future)
        rewritten_output = times(compensated, rep_future)
        if not equal(original_output, rewritten_output):
            raise AssertionError("incoming gauge compensation failed")

    # Multiple incoming branches may be compensated independently and then recoalesced.
    incoming_2 = CWM(1, Ratio(1, 2), Ratio(1, 2))
    combined_original = plus(times(incoming, eliminated[0]), times(incoming_2, eliminated[0]))
    combined_rewrite = times(plus(gauge(lam, incoming), gauge(lam, incoming_2)), representative[0])
    if not equal(combined_original, combined_rewrite):
        raise AssertionError("multi-incoming gauge compensation failed")


def check_equivalence_levels() -> None:
    exact_a: Signature = (CWM(1, Ratio(1), Ratio(1)),)
    projective_b: Signature = (CWM(1, Ratio(2), Ratio(2)),)
    boolean_only_c: Signature = (CWM(2, Ratio(2), Ratio(1)),)

    if boolean_signature(exact_a) != boolean_signature(projective_b):
        raise AssertionError("projective pair must be Boolean-equivalent")
    if signature_equal(exact_a, projective_b):
        raise AssertionError("lambda!=1 pair must not be exact-CWM equivalent")
    lam = projective_scale(exact_a, projective_b)
    if lam is None or not eq_ratio(lam, Ratio(2)):
        raise AssertionError("projective pair not recognized")

    if boolean_signature(exact_a) != boolean_signature(boolean_only_c):
        raise AssertionError("strict hierarchy witness must be Boolean-equivalent")
    if projective_scale(exact_a, boolean_only_c) is not None:
        raise AssertionError("different count vector must block projective equivalence")


def check_scalar_edge_factor_relocation() -> None:
    future_a = CWM(1, Ratio(1), Ratio(1))
    future_b = CWM(1, Ratio(2), Ratio(2))
    if not equal(future_b, gauge(Ratio(2), future_a)):
        raise AssertionError("atomic projective pair failed")
    edge_to_b = CWM(1, Ratio(3, 2), Ratio(3, 2))
    redirected_edge = gauge(Ratio(2), edge_to_b)
    if not equal(times(edge_to_b, future_b), times(redirected_edge, future_a)):
        raise AssertionError("scalar edge factor relocation failed")


def check_realizability_preservation() -> int:
    states = (
        CWM(1, Ratio(1), Ratio(1)),
        CWM(2, Ratio(3), Ratio(2)),
        CWM(3, Ratio(9, 2), Ratio(2)),
    )
    scales = (Ratio(1, 2), Ratio(2), Ratio(3, 2), Ratio(5))
    checks = 0
    for state, lam in product(states, scales):
        if not exact_realizable(state):
            raise AssertionError("source gauge sample must be positive-path realizable")
        scaled = gauge(lam, state)
        if not exact_realizable(scaled):
            raise AssertionError("positive scaling left exact realizability locus")
        checks += 1
    return checks


def main() -> None:
    scaling_checks = check_scaling_laws()
    check_projective_equivalence_and_normalization()
    check_incoming_compensation()
    check_equivalence_levels()
    check_scalar_edge_factor_relocation()
    realizability_checks = check_realizability_preservation()
    print(
        "BRC projective gauge quotient research check PASS: "
        f"{scaling_checks} central-scaling triples; "
        f"{realizability_checks} realizability-scale checks; "
        "normalization, compensation, and equivalence hierarchy confirmed"
    )


if __name__ == "__main__":
    main()
