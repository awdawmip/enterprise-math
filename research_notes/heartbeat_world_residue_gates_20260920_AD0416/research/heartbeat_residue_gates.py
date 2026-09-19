"""Geometry-derived local switches for Heartbeat World (research model only).

A selected dyadic partition, cyclic axis order and external tick schedule are
additional structure, not definitions of the world's geometry or force balance.
Each width1 gate exchanges neighboring integer Cells and costs one primitive step.
At width m it costs m primitive steps, NOT a free coarse jump.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import permutations
from typing import Callable, Sequence
from enterprise_math.brc_transport import Affine, eye
from brc_residue_transport import DIM, ZERO, Key, ResidueControl, GuardedKernel, native

FORWARD = tuple(range(DIM))
REVERSE = FORWARD[::-1]


def axis_index(i: int) -> int:
    if type(i) is not int or not 0 <= i < DIM:
        raise ValueError('native axis index must lie in 0..5')
    return i


def gate(x: Sequence[int], axis: int, width: int = 1) -> Key:
    """Exchange the two adjacent coarse cells paired by a neighbor's parity.

    q=floor(x/width), s=q_(axis+1) mod2. Pair q_axis=2h+s+epsilon
    with 2h+s+1-epsilon. Retain all sub-cell remainders.
    """
    x = native(x); i = axis_index(axis)
    if type(width) is not int or width < 1:
        raise ValueError('positive integer width required')
    q = [a // width for a in x]
    offset = q[(i+1) % DIM] % 2
    pair, bit = divmod(q[i]-offset, 2)
    new_coarse = 2*pair + offset + 1-bit
    out = list(x)
    out[i] = width*new_coarse + x[i] % width
    return tuple(out)


def walk(x: Sequence[int], axes: Sequence[int], width: int = 1) -> Key:
    x = native(x)
    for i in axes:
        x = gate(x, i, width)
    return x


def velocity(x: Sequence[int], width: int = 1) -> Key:
    c = ResidueControl('neighbor_xor', width).observe(x)
    return tuple(width*(1-2*c[i])*(-1 if i == DIM-1 else 1) for i in range(DIM))


def gate_kernel(axis: int, *, tick: int = 0, control: ResidueControl | None = None,
                fire: Q | Callable[[Key], Q] = Q(1)) -> GuardedKernel:
    """State-dependent firing weights are allowed only through the control key."""
    i = axis_index(axis)
    control = control or ResidueControl()
    rows = {}
    for c in control.states:
        p = fire(c) if callable(fire) else fire
        if type(p) is int:
            p = Q(p)
        if not isinstance(p, Q) or not 0 <= p <= 1:
            raise ValueError('firing probability must be an exact rational in [0,1]')
        x = control.representative(c); y = gate(x, i, control.width)
        delta = tuple(b-a for a,b in zip(x,y))
        terms = []
        if p:
            terms.append((p, Affine(eye(DIM), delta), 1))
        if p < 1:
            terms.append((1-p, Affine.identity(DIM), 1))
        rows[c] = terms
    return GuardedKernel.from_rows(tick, 1, control, rows)


def word_kernel(axes: Sequence[int], *, tick: int = 0,
                control: ResidueControl | None = None) -> GuardedKernel:
    axes = tuple(axis_index(i) for i in axes)
    control = control or ResidueControl()
    rows = {}
    for c in control.states:
        x = control.representative(c); y = walk(x, axes, control.width)
        rows[c] = [(1, Affine(eye(DIM), tuple(b-a for a,b in zip(x,y))), 1)]
    return GuardedKernel.from_rows(tick, len(axes), control, rows)


def shuffled_sweep(*, tick: int = 0, control: ResidueControl | None = None) -> GuardedKernel:
    """Choose ONE of720 permutations per six ticks, independently each sweep.

    Internal partial-sweep queries require retaining the chosen word or unused
    axis mask. This boundary packet preserves complete-sweep observations only.
    Its720 paths may coalesce into fewer effect atoms; multiplicities stay intact.
    """
    control = control or ResidueControl()
    orders = tuple(permutations(range(DIM)))
    rows = {}
    for c in control.states:
        x = control.representative(c)
        rows[c] = [(Q(1,720), Affine(eye(DIM), tuple(b-a for a,b in zip(x,walk(x,order,control.width)))), 1)
                   for order in orders]
    return GuardedKernel.from_rows(tick, DIM, control, rows)


def active_heartbeat_gate(axis: int, *, tick: int = 0) -> GuardedKernel:
    """One tick of actual material expansion A_2 followed by the local gate.

    Expansion's physical implementation cost is not counted as a free unit move.
    The full64 parity control is necessary for the declared mixed action family.
    """
    from heartbeat_algebra import beat, multiplication_matrix, LAM
    i = axis_index(axis); control = ResidueControl('parity')
    linear = multiplication_matrix(LAM, 2)
    rows = {}
    for c in control.states:
        x = control.representative(c); ax = beat(x); y = gate(ax, i)
        delta = tuple(b-a for a,b in zip(ax,y))
        rows[c] = [(1, Affine(linear, delta), 1)]
    return GuardedKernel.from_rows(tick, 1, control, rows)
