"""Integer-only total-factor scale algebra for Enterprise Math."""

from __future__ import annotations

from math import gcd

from .core import integer_nth_root


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def scale_factor(base: int, level: int) -> int:
    """Encode a `(base, level)` representation as one positive total scale factor."""
    _positive("base", base)
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    return base**level


def scaled_root_factor(n: int, exponent: int, factor: int) -> int:
    """Return R_p(n d^p) for total scale factor d."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    _positive("exponent", exponent)
    _positive("factor", factor)
    return integer_nth_root(n * factor**exponent, exponent)


def project_scale_factor(value: int, source_factor: int, target_factor: int) -> int:
    """Project a coordinate from scale `source_factor` to a coarser divisor scale."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a non-negative integer")
    _positive("source_factor", source_factor)
    _positive("target_factor", target_factor)
    if source_factor % target_factor != 0:
        raise ValueError("target_factor must divide source_factor")
    return value // (source_factor // target_factor)


def greatest_common_coarsening(left: int, right: int) -> int:
    """Greatest common coarsening in the divisibility scale order."""
    _positive("left", left)
    _positive("right", right)
    return gcd(left, right)


def least_common_refinement(left: int, right: int) -> int:
    """Least common refinement in the divisibility scale order."""
    _positive("left", left)
    _positive("right", right)
    return left // gcd(left, right) * right
