"""Finite rotation-refinement certificates for the Enterprise Euler/Viète line.

The module is deliberately target-free: it never imports or uses ``pi`` or a
trigonometric function. It models the cyclic phase tower

    C_6 -> C_12 -> C_24 -> ...

by the injective map k |-> 2k, and the distinguished element u_m = 3.
The relation 2*u_(m+1) = iota_m(u_m) is the finite square-root law. Decimal
square roots are used only for the symmetric/antisymmetric trace recurrence
that produces the finite Viète approximants.

This is a project research checker, not a native-geometry promotion. Level 0
has a six-orientation Cell-shell interpretation and level 1 has the actual
Cell/gate incidence interpretation. Higher levels are typed as transition-
history refinements unless a separate physical realization theorem is supplied.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from math import gcd, lcm
from typing import Literal

PhaseKind = Literal["cell", "gate", "higher-transition"]


def _nonnegative_int(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return value


def _integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def phase_order(depth: int) -> int:
    """Minimal cyclic order preserving C6 and a 2^depth-th root of reversal."""
    depth = _nonnegative_int(depth, "depth")
    return 6 << depth


def minimal_cyclic_order(depth: int) -> int:
    """Return lcm(6, 2^(depth+1)); this equals ``phase_order(depth)``."""
    depth = _nonnegative_int(depth, "depth")
    return lcm(6, 1 << (depth + 1))


def normalize_phase(index: int, depth: int) -> int:
    """Canonical residue of a phase index at one refinement depth."""
    index = _integer(index, "index")
    return index % phase_order(depth)


def successor(index: int, depth: int, steps: int = 1) -> int:
    """Advance by an integer number of directed phase transitions."""
    steps = _integer(steps, "steps")
    return (normalize_phase(index, depth) + steps) % phase_order(depth)


def coarse_embed(index: int, depth: int) -> int:
    """Embed C_(6*2^depth) into the next level by sending k to 2k."""
    depth = _nonnegative_int(depth, "depth")
    return (2 * normalize_phase(index, depth)) % phase_order(depth + 1)


def element_order(index: int, depth: int) -> int:
    """Exact additive order of ``index`` in the finite cyclic phase group."""
    order = phase_order(depth)
    residue = normalize_phase(index, depth)
    return 1 if residue == 0 else order // gcd(order, residue)


def distinguished_root_index(depth: int) -> int:
    """The three-step state isolating the 2-primary rotation factor."""
    _nonnegative_int(depth, "depth")
    return 3


def distinguished_root_order(depth: int) -> int:
    """Order of the distinguished state: exactly 2^(depth+1)."""
    return element_order(distinguished_root_index(depth), depth)


def root_square_certificate(depth: int) -> tuple[int, int]:
    """Return both sides of 2*u_(m+1) = iota_m(u_m)."""
    depth = _nonnegative_int(depth, "depth")
    fine_square = (2 * distinguished_root_index(depth + 1)) % phase_order(depth + 1)
    embedded_coarse = coarse_embed(distinguished_root_index(depth), depth)
    return fine_square, embedded_coarse


def half_turn_index(depth: int) -> int:
    """Index of exact orientation reversal at the selected phase level."""
    return phase_order(depth) // 2


def reflection(index: int, depth: int) -> int:
    """Reverse the chosen cyclic orientation."""
    return (-normalize_phase(index, depth)) % phase_order(depth)


def quarter_turn_roots(depth: int = 1) -> tuple[int, int]:
    """The two roots q and q^-1 of the half-turn, swapped by reflection."""
    depth = _nonnegative_int(depth, "depth")
    order = phase_order(depth)
    if order % 4:
        raise ValueError("this phase level has no exact quarter-turn")
    root = order // 4
    return root, (-root) % order


def phase_birth_level(index: int, depth: int) -> int:
    """First subdivision level at which a final-level phase state appears.

    At final depth ``d``, indices divisible by 2^d descend from Cell states,
    indices divisible by 2^(d-1) but not 2^d descend from the physical gate
    layer, and odd indices are newly introduced at depth ``d``.
    """
    depth = _nonnegative_int(depth, "depth")
    residue = normalize_phase(index, depth)
    if residue == 0:
        return 0
    valuation = 0
    while residue % 2 == 0:
        residue //= 2
        valuation += 1
    return max(0, depth - valuation)


def phase_kind(index: int, depth: int) -> PhaseKind:
    """Classify a phase state by its geometric/history origin."""
    birth = phase_birth_level(index, depth)
    if birth == 0:
        return "cell"
    if birth == 1:
        return "gate"
    return "higher-transition"


def cell_gate_cycle() -> tuple[str, ...]:
    """Actual first incidence subdivision around one pivot Cell."""
    labels: list[str] = []
    for index in range(6):
        labels.extend((f"C{index}", f"G{index}"))
    return tuple(labels)


@dataclass(frozen=True)
class RotationLevelCertificate:
    depth: int
    order: int
    minimal_order: int
    root_index: int
    root_order: int
    half_turn: int
    root_square: int
    embedded_previous_root: int
    root_birth_level: int
    root_kind: PhaseKind

    @property
    def valid(self) -> bool:
        return (
            self.order == self.minimal_order
            and self.root_order == 1 << (self.depth + 1)
            and self.root_square == self.embedded_previous_root
            and self.root_birth_level == self.depth
        )


def rotation_level_certificate(depth: int) -> RotationLevelCertificate:
    """Produce the exact finite certificate at one tower level."""
    depth = _nonnegative_int(depth, "depth")
    square, embedded = root_square_certificate(depth)
    return RotationLevelCertificate(
        depth=depth,
        order=phase_order(depth),
        minimal_order=minimal_cyclic_order(depth),
        root_index=distinguished_root_index(depth),
        root_order=distinguished_root_order(depth),
        half_turn=half_turn_index(depth),
        root_square=square,
        embedded_previous_root=embedded,
        root_birth_level=phase_birth_level(3, depth),
        root_kind=phase_kind(3, depth),
    )


def rotation_tower_certificates(max_depth: int) -> tuple[RotationLevelCertificate, ...]:
    """Certificates from the coarse C6 shell through ``max_depth``."""
    max_depth = _nonnegative_int(max_depth, "max_depth")
    return tuple(rotation_level_certificate(depth) for depth in range(max_depth + 1))


def local_cell_gate_capacity() -> int:
    """Six neighboring Cell states plus six actual transition gates."""
    return 12


def required_nonlocal_phase_states(depth: int) -> int:
    """States beyond the one-step local Cell+gate geometry."""
    return max(0, phase_order(depth) - local_cell_gate_capacity())


def _precision(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 20:
        raise ValueError("precision must be an integer at least 20")
    return value


def symmetric_trace(depth: int, *, precision: int = 80) -> Decimal:
    """Target-free nested-radical trace c_d.

    c_0=-1 and c_(d+1)=sqrt((1+c_d)/2), choosing the forward positive branch.
    """
    depth = _nonnegative_int(depth, "depth")
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 12
        value = Decimal(-1)
        for _ in range(depth):
            value = ((Decimal(1) + value) / Decimal(2)).sqrt()
        context.prec = precision
        return +value


def antisymmetric_trace(depth: int, *, precision: int = 80) -> Decimal:
    """Positive antisymmetric coordinate s_d satisfying c_d^2+s_d^2=1."""
    depth = _nonnegative_int(depth, "depth")
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 12
        cosine = symmetric_trace(depth, precision=precision + 12)
        value = (Decimal(1) - cosine * cosine).sqrt()
        context.prec = precision
        return +value


def viete_factors(depth: int, *, precision: int = 80) -> tuple[Decimal, ...]:
    """Return c_2,...,c_depth; no classical pi or trigonometry is used."""
    depth = _nonnegative_int(depth, "depth")
    precision = _precision(precision)
    if depth < 2:
        return ()
    return tuple(symmetric_trace(index, precision=precision) for index in range(2, depth + 1))


def viete_product(depth: int, *, precision: int = 80) -> Decimal:
    """Finite product of the target-free symmetric traces."""
    precision = _precision(precision)
    with localcontext() as context:
        context.prec = precision + 12
        value = Decimal(1)
        for factor in viete_factors(depth, precision=precision + 12):
            value *= factor
        context.prec = precision
        return +value


def rotation_pi_approximant(depth: int, *, precision: int = 80) -> Decimal:
    """Finite rotation-completion readout Pi_d=2^d*s_d=2/prod(c_2..c_d)."""
    depth = _nonnegative_int(depth, "depth")
    precision = _precision(precision)
    if depth < 1:
        raise ValueError("depth must be at least 1")
    with localcontext() as context:
        context.prec = precision + 12
        value = (Decimal(2) ** depth) * antisymmetric_trace(depth, precision=precision + 12)
        context.prec = precision
        return +value


def rotation_pi_viete_form(depth: int, *, precision: int = 80) -> Decimal:
    """Equivalent finite Viète product readout 2/prod(c_2..c_d)."""
    depth = _nonnegative_int(depth, "depth")
    precision = _precision(precision)
    if depth < 1:
        raise ValueError("depth must be at least 1")
    if depth == 1:
        return Decimal(2)
    with localcontext() as context:
        context.prec = precision + 12
        value = Decimal(2) / viete_product(depth, precision=precision + 12)
        context.prec = precision
        return +value


def completion_tail_bound(depth: int, *, precision: int = 80) -> Decimal:
    """Target-free upper bound for the gap to the monotone completion limit."""
    depth = _nonnegative_int(depth, "depth")
    precision = _precision(precision)
    if depth < 2:
        raise ValueError("depth must be at least 2")
    with localcontext() as context:
        context.prec = precision + 12
        two = Decimal(2)
        bound_scale = two * (Decimal(1) + two.sqrt())
        defect_tail = bound_scale * bound_scale / (Decimal(3) * (Decimal(4) ** depth))
        if defect_tail >= 1:
            raise ArithmeticError("derived tail estimate is not contractive")
        value = (
            rotation_pi_approximant(depth, precision=precision + 12)
            * defect_tail
            / (Decimal(1) - defect_tail)
        )
        context.prec = precision
        return +value
