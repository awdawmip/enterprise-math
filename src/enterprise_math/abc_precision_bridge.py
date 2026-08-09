"""P025 bridge from abc multiplicity pressure to the canonical integer-root core."""

from __future__ import annotations

from .abc_support import residual_pressure
from .core import integer_nth_root


def residual_root_horizon(a: int, b: int, c: int, u: int, v: int) -> dict[str, object]:
    """Return the exact root horizon forced by a high-quality abc triple.

    P025's elementary residual-pressure inequality gives, for ``u>v``,

    ``max_residual^(3u) > c^(u-v) (c-1)^u``

    whenever ``c^v > rad(abc)^u``.  Therefore the largest multiplicity residual
    lies strictly above the canonical integer root

    ``R_(3u)(c^(u-v) (c-1)^u)``.

    This is a bridge only: it reuses the existing integer-root primitive and
    does not claim a new root theory.
    """
    data = residual_pressure(a, b, c, u, v)
    threshold = int(data["threshold"])
    horizon = integer_nth_root(threshold, 3 * u)
    if bool(data["high_quality"]) and int(data["max_residual"]) <= horizon:
        raise AssertionError("high-quality residual failed to cross integer-root horizon")
    return {
        **data,
        "root_exponent": 3 * u,
        "residual_root_horizon": horizon,
        "crosses_root_horizon": int(data["max_residual"]) > horizon,
    }
