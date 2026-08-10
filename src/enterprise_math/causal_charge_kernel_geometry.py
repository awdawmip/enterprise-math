"""Causal charge-kernel interpretation of integer relation lattices.

Allowed fine displacements may be specified first by conserved integer or finite
charges, rather than by naming a classical lattice.  Free integer charges reduce
relation rank; finite modular charges restrict residue sectors but do not reduce
the integer rank of a finite-index kernel.

This module records exact A/D and scaled-E8 specializations.  Smith normal form
and lattice-kernel theory are mature prior art; the project use here is causal:
identify which conservation law would make a classical lattice appear as a
shadow, and separate free-rank loss from torsion/residue restriction.
"""

from __future__ import annotations

Vector = tuple[int, ...]


def _require_integer_vector(vector: Vector) -> None:
    if not vector or any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError("vector must be a non-empty integer tuple")


def exact_total_charge(vector: Vector) -> int:
    _require_integer_vector(vector)
    return sum(vector)


def parity_total_charge(vector: Vector) -> int:
    return exact_total_charge(vector) % 2


def in_a_kernel(vector: Vector) -> bool:
    return exact_total_charge(vector) == 0


def in_d_kernel(vector: Vector) -> bool:
    return parity_total_charge(vector) == 0


def a_relation_rank(slot_count: int) -> int:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    return max(0, slot_count - 1)


def d_relation_rank(slot_count: int) -> int:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    # Parity is a finite-index restriction, not a rational-rank equation.
    return slot_count


def a_kernel_basis(slot_count: int) -> tuple[Vector, ...]:
    if slot_count < 2:
        return ()
    basis = []
    for index in range(slot_count - 1):
        vector = [0] * slot_count
        vector[index] = 1
        vector[-1] = -1
        basis.append(tuple(vector))
    return tuple(basis)


def d_kernel_basis(slot_count: int) -> tuple[Vector, ...]:
    """Standard root basis spanning D_n={x:sum x even} for n>=2."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be an integer at least two")
    basis = []
    for index in range(slot_count - 1):
        vector = [0] * slot_count
        vector[index] = 1
        vector[index + 1] = -1
        basis.append(tuple(vector))
    last = [0] * slot_count
    last[-2] = 1
    last[-1] = 1
    basis[-1] = tuple(last)  # Replace the final chain difference by e_(n-1)+e_n.
    return tuple(basis)


def d_primitive_pair_moves(slot_count: int) -> tuple[Vector, ...]:
    """Parity-preserving two-slot moves with one unit magnitude per touched slot."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    moves = []
    for left in range(slot_count):
        for right in range(left + 1, slot_count):
            for sign_left in (-1, 1):
                for sign_right in (-1, 1):
                    vector = [0] * slot_count
                    vector[left] = sign_left
                    vector[right] = sign_right
                    moves.append(tuple(vector))
    return tuple(moves)


def scaled_e8_charge_constraints(vector: Vector) -> tuple[bool, bool]:
    """Return the two finite congruence conditions defining the scaled E8 lattice.

    For y=2*x with x in E8, all eight coordinates of y have the same parity and
    sum(y) is divisible by four.
    """
    _require_integer_vector(vector)
    if len(vector) != 8:
        raise ValueError("scaled E8 vectors must have eight coordinates")
    same_parity = len({value % 2 for value in vector}) == 1
    total_mod_four = sum(vector) % 4 == 0
    return same_parity, total_mod_four


def in_scaled_e8_charge_kernel(vector: Vector) -> bool:
    return all(scaled_e8_charge_constraints(vector))


def scaled_e8_relation_rank() -> int:
    """Finite congruence conditions leave full integer rank eight."""
    return 8


def classify_total_conservation(move: Vector) -> tuple[int, int]:
    """Return (exact total change, parity change) for a primitive displacement."""
    change = exact_total_charge(move)
    return change, change % 2
