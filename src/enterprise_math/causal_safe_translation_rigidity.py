"""Safe additive translations force eventual periodic P008 basin geometry.

Infinite theorem (proved in the accompanying note/orientation): let V:N0->N0 be
strictly increasing and unbounded, with q its P008 level quotient.  If a fixed
t>0 is future-safe on a tail,

    q(x)=q(y) => q(x+t)=q(y+t),

then every sufficiently large complete boundary has a predecessor exactly t
units earlier.  Because there are only t residue classes, the tail boundary set
is eventually a union of complete arithmetic rays modulo t.  Hence there exist
K,p such that

    V(k+p)=V(k)+t,
    w_(k+p)=w_k

for all k>=K.  On that tail the translation is detail-preserving:

    q(n+t)=q(n)+p,
    delta(n+t)=delta(n).

Conversely, such eventual complete-level periodicity makes +t tail-safe.

This module supplies finite exact certificates on represented growth prefixes;
it does not mistake a finite sample for an all-depth proof.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_completion_collapse import completion_root_index


@dataclass(frozen=True)
class TailPeriodCertificate:
    start_level: int
    level_period: int
    value_translation: int
    verified_level_count: int


def _validate_growth(growth: tuple[int, ...]) -> None:
    if not isinstance(growth, tuple) or len(growth) < 2:
        raise ValueError("growth must contain at least two levels")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in growth
    ):
        raise ValueError("growth values must be non-negative integers")
    if any(left >= right for left, right in zip(growth, growth[1:])):
        raise ValueError("growth must be strictly increasing")


def tail_period_certificate(
    growth: tuple[int, ...],
    start_level: int,
    level_period: int,
) -> TailPeriodCertificate | None:
    """Exact represented-tail certificate of V(k+p)=V(k)+T with constant T."""
    _validate_growth(growth)
    if (
        isinstance(start_level, bool)
        or not isinstance(start_level, int)
        or start_level < 0
    ):
        raise ValueError("start_level must be non-negative")
    if (
        isinstance(level_period, bool)
        or not isinstance(level_period, int)
        or level_period <= 0
    ):
        raise ValueError("level_period must be positive")
    if start_level + level_period >= len(growth):
        return None
    translations = tuple(
        growth[index + level_period] - growth[index]
        for index in range(start_level, len(growth) - level_period)
    )
    if not translations or len(set(translations)) != 1:
        return None
    total = translations[0]
    widths = tuple(right - left for left, right in zip(growth, growth[1:]))
    if not all(
        widths[index + level_period] == widths[index]
        for index in range(start_level, len(widths) - level_period)
    ):
        return None
    return TailPeriodCertificate(
        start_level=start_level,
        level_period=level_period,
        value_translation=total,
        verified_level_count=len(translations),
    )


def translation_is_safe_from_level(
    growth: tuple[int, ...],
    translation: int,
    start_level: int,
) -> bool:
    """Finite represented-tail check that each translated basin stays in one q-fiber."""
    _validate_growth(growth)
    if isinstance(translation, bool) or not isinstance(translation, int) or translation < 0:
        raise ValueError("translation must be non-negative")
    if (
        isinstance(start_level, bool)
        or not isinstance(start_level, int)
        or not (0 <= start_level < len(growth) - 1)
    ):
        raise ValueError("start_level must have a represented next level")
    for level in range(start_level, len(growth) - 1):
        left = growth[level] + translation
        right = growth[level + 1] - 1 + translation
        if right >= growth[-1]:
            break
        if completion_root_index(growth, left) != completion_root_index(growth, right):
            return False
    return True


def certificate_preserves_detail(
    growth: tuple[int, ...],
    certificate: TailPeriodCertificate,
) -> bool:
    _validate_growth(growth)
    start = certificate.start_level
    period = certificate.level_period
    total = certificate.value_translation
    widths = tuple(right - left for left, right in zip(growth, growth[1:]))
    for level in range(start, len(growth) - period):
        if growth[level + period] != growth[level] + total:
            return False
        if level + period < len(widths) and widths[level + period] != widths[level]:
            return False
        width = widths[level]
        for detail in range(width):
            if growth[level] + detail + total != growth[level + period] + detail:
                return False
    return True


def first_tail_period_certificate(
    growth: tuple[int, ...],
    maximum_start_level: int,
    maximum_level_period: int,
) -> TailPeriodCertificate | None:
    """Smallest represented value-translation certificate among searched tails.

    This is a finite discovery helper, not proof of infinite eventual periodicity.
    """
    _validate_growth(growth)
    candidates = []
    for start in range(min(maximum_start_level, len(growth) - 2) + 1):
        for period in range(1, maximum_level_period + 1):
            certificate = tail_period_certificate(growth, start, period)
            if certificate is not None:
                candidates.append(certificate)
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda item: (
            item.value_translation,
            item.level_period,
            item.start_level,
        ),
    )
