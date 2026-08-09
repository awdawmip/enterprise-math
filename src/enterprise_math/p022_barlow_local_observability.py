"""Two-shell observability of the hidden Barlow absolute-drift pair.

A single coordination shell S_n determines only

    Q_n = a_n^2 + b_n^2,

where {a_n,b_n}={|delta_n|,|delta_-n|}.  Static sum-of-two-squares ambiguity
appears at radius seven.  Nevertheless two consecutive energies determine the
current unordered pair exactly.  Thus the uniform observation depth for the
current hidden two-channel drift state is exactly two.
"""

from __future__ import annotations

from math import isqrt

from .p022_barlow_coordination_history import shell_drift_energy_from_vertex_count

DriftPair = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def recover_current_drift_pair_from_consecutive_energies(
    previous_energy: int, current_energy: int
) -> DriftPair:
    """Recover the unordered current absolute pair from ``(Q_(n-1),Q_n)``.

    If the current pair is {a,b}, a legal predecessor changes each absolute
    coordinate by one (with reflection at zero). Therefore

        L=(Q_prev-Q_now-2)/2 = ±a ± b.

    If L^2>Q, |L| must be a+b; if L^2<Q, |L| must be |a-b|; equality means
    ab=0.  Sum and product then recover the unordered pair as integer roots.
    """
    _require_natural("previous_energy", previous_energy)
    _require_natural("current_energy", current_energy)
    difference = previous_energy - current_energy - 2
    if difference % 2:
        raise ValueError("consecutive Barlow energies require an even step residue")
    linear = abs(difference // 2)
    linear_square = linear * linear

    if linear_square > current_energy:
        # linear=a+b
        total = linear
        product_twice = linear_square - current_energy
    elif linear_square < current_energy:
        # linear=|a-b| and (a+b)^2=2Q-linear^2
        total_square = 2 * current_energy - linear_square
        total = isqrt(total_square)
        if total * total != total_square:
            raise ValueError("energy pair does not encode an integral current sum")
        product_twice = current_energy - linear_square
    else:
        # One current coordinate is zero.
        total = isqrt(current_energy)
        if total * total != current_energy:
            raise ValueError("degenerate energy must be a square")
        product_twice = 0

    if product_twice < 0 or product_twice % 2:
        raise ValueError("energy pair does not encode an integral coordinate product")
    product = product_twice // 2
    discriminant = total * total - 4 * product
    if discriminant < 0:
        raise ValueError("energy pair gives a negative quadratic discriminant")
    gap = isqrt(discriminant)
    if gap * gap != discriminant or (total + gap) % 2:
        raise ValueError("energy pair does not encode integer drift coordinates")
    high = (total + gap) // 2
    low = (total - gap) // 2
    if high * high + low * low != current_energy:
        raise AssertionError("recovered pair must reproduce the current energy")
    return (low, high)


def recover_current_drift_pair_from_consecutive_shells(
    radius: int, previous_shell: int, current_shell: int
) -> DriftPair:
    """Exact local decoder ``(S_(n-1),S_n) -> {|delta_n|,|delta_-n|}``."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius <= 0:
        raise ValueError("radius must be a positive integer")
    previous_energy = shell_drift_energy_from_vertex_count(
        radius - 1, previous_shell
    )
    current_energy = shell_drift_energy_from_vertex_count(radius, current_shell)
    return recover_current_drift_pair_from_consecutive_energies(
        previous_energy, current_energy
    )


def recover_drift_history_by_sliding_shell_pairs(
    shell_cardinalities: tuple[int, ...]
) -> tuple[DriftPair, ...]:
    """Recover the entire unordered drift trajectory with a two-shell window."""
    if not isinstance(shell_cardinalities, tuple) or not shell_cardinalities:
        raise ValueError("shell_cardinalities must be a nonempty tuple")
    if shell_cardinalities[0] != 1:
        raise ValueError("history must start with S_0=1")
    output: list[DriftPair] = [(0, 0)]
    for radius in range(1, len(shell_cardinalities)):
        output.append(
            recover_current_drift_pair_from_consecutive_shells(
                radius,
                shell_cardinalities[radius - 1],
                shell_cardinalities[radius],
            )
        )
    return tuple(output)


def uniform_hidden_state_observation_depth() -> int:
    """Sharp depth: one shell fails at n=7, two consecutive shells always suffice."""
    return 2
