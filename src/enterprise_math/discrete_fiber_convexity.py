"""Integer exchange calculus for P019 collision-power contraction fibers.

The balanced block cost Psi_(m,s)(c) has a monotone one-step slope. Therefore
fixed-total separable fibers can be minimized by one-unit exchanges only; no
continuous derivative or real optimization is required.
"""

from __future__ import annotations

from .dimension_contraction import balanced_power_energy, partition_power_energy


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def balanced_power_increment(block_size: int, power: int, total: int) -> int:
    """Exact forward difference Psi(c+1)-Psi(c).

    Write c=m*q+r with floor quotient q and 0<=r<m. One balanced coordinate
    changes from q to q+1, so the increment is |q+1|^s-|q|^s.
    """
    _require_positive("block_size", block_size)
    _require_positive("power", power)
    _require_integer("total", total)
    quotient = total // block_size
    return abs(quotient + 1) ** power - abs(quotient) ** power


def exchange_energy_increment(
    block_sizes: tuple[int, ...],
    power: int,
    totals: tuple[int, ...],
    receiver: int,
    donor: int,
) -> int:
    """Cost change for totals -> totals+e_receiver-e_donor."""
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be non-empty")
    if any(isinstance(size, bool) or not isinstance(size, int) or size <= 0 for size in block_sizes):
        raise ValueError("block sizes must be positive integers")
    _require_positive("power", power)
    if not isinstance(totals, tuple) or len(totals) != len(block_sizes):
        raise ValueError("totals must match block_sizes")
    if any(isinstance(total, bool) or not isinstance(total, int) for total in totals):
        raise ValueError("totals must be integers")
    if receiver == donor:
        return 0
    if not (0 <= receiver < len(block_sizes) and 0 <= donor < len(block_sizes)):
        raise ValueError("receiver and donor must index the blocks")
    return (
        balanced_power_increment(
            block_sizes[receiver], power, totals[receiver]
        )
        - balanced_power_increment(
            block_sizes[donor], power, totals[donor] - 1
        )
    )


def has_decreasing_exchange(
    block_sizes: tuple[int, ...], power: int, totals: tuple[int, ...]
) -> bool:
    """Whether any one-unit transfer strictly decreases the separable cost."""
    for receiver in range(len(block_sizes)):
        for donor in range(len(block_sizes)):
            if receiver == donor:
                continue
            if exchange_energy_increment(
                block_sizes, power, totals, receiver, donor
            ) < 0:
                return True
    return False


def exchange_minimize(
    block_sizes: tuple[int, ...], power: int, totals: tuple[int, ...]
) -> tuple[int, ...]:
    """Reach a fixed-total global minimum by strictly decreasing unit exchanges.

    The algorithm is deterministic only through scan order; minimizers need not
    be unique. Energy is a non-negative integer and every accepted move lowers
    it strictly, so termination is finite.
    """
    # Validate and establish the initial exact energy.
    current = tuple(totals)
    current_energy = partition_power_energy(block_sizes, power, current)
    while True:
        selected = None
        selected_increment = 0
        for receiver in range(len(block_sizes)):
            for donor in range(len(block_sizes)):
                if receiver == donor:
                    continue
                increment = exchange_energy_increment(
                    block_sizes, power, current, receiver, donor
                )
                if increment < selected_increment:
                    selected_increment = increment
                    selected = (receiver, donor)
        if selected is None:
            return current
        receiver, donor = selected
        next_state = list(current)
        next_state[receiver] += 1
        next_state[donor] -= 1
        current = tuple(next_state)
        next_energy = partition_power_energy(block_sizes, power, current)
        if next_energy != current_energy + selected_increment:
            raise AssertionError("exchange slope must equal exact energy change")
        if next_energy >= current_energy:
            raise AssertionError("selected exchange must strictly decrease energy")
        current_energy = next_energy


def exchange_minimum_identity(
    block_sizes: tuple[int, ...], power: int, totals: tuple[int, ...]
) -> tuple[int, int]:
    """Return exchange-minimized energy and the merged-block closed minimum."""
    minimizer = exchange_minimize(block_sizes, power, totals)
    actual = partition_power_energy(block_sizes, power, minimizer)
    expected = balanced_power_energy(sum(block_sizes), power, sum(totals))
    return actual, expected
