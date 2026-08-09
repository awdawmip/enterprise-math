"""Arithmetic fiber spectrum of the Barlow shell-cardinality quotient.

At radius n, a two-sided microscopic stacking window consists of two independent
length-n ±1 words.  Whole-shell cardinality sees them only through

    Q = delta_plus^2 + delta_minus^2.

Hence shell-cardinality fibers are binomial-weighted representations of Q as a
sum of two parity-compatible squares.
"""

from __future__ import annotations

from math import comb


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def admissible_absolute_imbalances(radius: int) -> tuple[int, ...]:
    """Non-negative absolute imbalances of a length-radius ±1 word."""
    _require_natural("radius", radius)
    start = radius % 2
    return tuple(range(start, radius + 1, 2))


def absolute_imbalance_fiber_size(radius: int, absolute_imbalance: int) -> int:
    """Number of one-sided words whose absolute imbalance is d."""
    _require_natural("radius", radius)
    _require_natural("absolute_imbalance", absolute_imbalance)
    if absolute_imbalance > radius or (radius - absolute_imbalance) % 2:
        return 0
    plus_count = (radius + absolute_imbalance) // 2
    one_sign = comb(radius, plus_count)
    return one_sign if absolute_imbalance == 0 else 2 * one_sign


def possible_shell_drift_energies(radius: int) -> tuple[int, ...]:
    """All Q=d_plus^2+d_minus^2 represented by finite two-sided windows."""
    values = admissible_absolute_imbalances(radius)
    return tuple(sorted({left * left + right * right for left in values for right in values}))


def shell_energy_fiber_size(radius: int, drift_energy: int) -> int:
    """Microscopic two-sided word count in one Q-energy fiber."""
    _require_natural("radius", radius)
    _require_natural("drift_energy", drift_energy)
    values = admissible_absolute_imbalances(radius)
    return sum(
        absolute_imbalance_fiber_size(radius, left)
        * absolute_imbalance_fiber_size(radius, right)
        for left in values
        for right in values
        if left * left + right * right == drift_energy
    )


def shell_energy_fiber_spectrum(radius: int) -> tuple[tuple[int, int], ...]:
    """Return ``(Q, microscopic_window_count)`` for all represented energies."""
    return tuple(
        (energy, shell_energy_fiber_size(radius, energy))
        for energy in possible_shell_drift_energies(radius)
    )


def shell_cardinality_from_energy(radius: int, drift_energy: int) -> int:
    """Whole-shell cardinality corresponding to one represented energy."""
    _require_natural("radius", radius)
    _require_natural("drift_energy", drift_energy)
    if radius == 0:
        if drift_energy != 0:
            raise ValueError("radius zero has only zero drift energy")
        return 1
    numerator = 42 * radius * radius + 8 - drift_energy
    if numerator < 0 or numerator % 4:
        raise ValueError("energy is incompatible with an integer Barlow shell")
    return numerator // 4


def shell_cardinality_fiber_spectrum(radius: int) -> tuple[tuple[int, int], ...]:
    """Return ``(shell_vertex_count, microscopic_window_count)``.

    The map Q -> S is injective at fixed radius, so this is simply the energy
    fiber spectrum relabelled by shell cardinality.
    """
    return tuple(
        sorted(
            (
                (shell_cardinality_from_energy(radius, energy), fiber_size)
                for energy, fiber_size in shell_energy_fiber_spectrum(radius)
            )
        )
    )


def minimum_shell_cardinality(radius: int) -> int:
    """FCC-type maximal-drift lower endpoint ``10 n^2 + 2`` for n>0."""
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return 10 * radius * radius + 2


def maximum_shell_cardinality(radius: int) -> int:
    """Balanced-prefix upper endpoint ``floor(21 n^2 / 2)+2``."""
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return (21 * radius * radius) // 2 + 2


def minimum_drift_energy(radius: int) -> int:
    """Parity-forced smallest Q: 0 for even n, 2 for odd n."""
    _require_natural("radius", radius)
    return 0 if radius % 2 == 0 else 2


def maximum_drift_energy(radius: int) -> int:
    _require_natural("radius", radius)
    return 2 * radius * radius


def energy_congruence_class(radius: int) -> tuple[int, int]:
    """Return ``(residue, modulus)`` forced by parity.

    For even n, both imbalances are even and Q is divisible by 4.
    For odd n, both are odd, each square is 1 mod 8, and Q is 2 mod 8.
    """
    _require_natural("radius", radius)
    return (0, 4) if radius % 2 == 0 else (2, 8)
