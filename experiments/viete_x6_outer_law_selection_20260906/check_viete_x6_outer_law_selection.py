#!/usr/bin/env python3
"""Exact law-selection checker for the triadic Viète root-refining branch.

Starting population: the 2^6 shortest INNER/OUTER branch words over one full
six-edge Q_S frame cycle.  The checker proves:

1. Q_S-equivariant deterministic branch sections are exactly all-INNER and
   all-OUTER;
2. all-INNER repeatedly collapses through the pivot and has only seven
   distinct micro-Cells;
3. all-OUTER has twelve distinct nonzero micro-Cells and is the unique
   equivariant faithful C12 phase lift.

This is a root-refining law-selection theorem, not a uniqueness theorem for
all possible native rotation dynamics.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRIAD_PATH = (
    ROOT
    / "experiments"
    / "x6_triadic_rotation_v1_20260906"
    / "check_triadic_rotation.py"
)
spec = spec_from_file_location("x6_triadic_rotation_v1", TRIAD_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load existing triadic rotation checker")
tri = module_from_spec(spec)
spec.loader.exec_module(tri)

INNER = 0
OUTER = 1
ZERO = (0,) * tri.N


def cyclic_shift(word, amount=1):
    amount %= len(word)
    return word[amount:] + word[:amount]


def q_orbit(S=(0, 1, 2)):
    q = tri.q_triad(S)
    phases = [tri.unit(S[0])]
    for _ in range(5):
        phases.append(tri.act(q, phases[-1]))
    return tuple(phases)


def lift_word(phases, word):
    seq = [phases[0]]
    for r, bit in enumerate(word):
        a = phases[r]
        b = phases[(r + 1) % 6]
        mid = tri.add(a, b) if bit == OUTER else ZERO
        seq.extend((mid, b))
    return tuple(seq)


def check_equivariant_sections():
    words = tuple(product((INNER, OUTER), repeat=6))
    assert len(words) == 64

    # Q_S transports edge r to r+1 and preserves the branch type INNER/OUTER.
    # Therefore a deterministic branch section is Q-equivariant iff its word
    # is fixed by one cyclic shift.
    equivariant = tuple(word for word in words if cyclic_shift(word) == word)
    assert equivariant == (
        (INNER, INNER, INNER, INNER, INNER, INNER),
        (OUTER, OUTER, OUTER, OUTER, OUTER, OUTER),
    )


def check_faithful_c12_selector():
    phases = q_orbit()
    inner_word = (INNER,) * 6
    outer_word = (OUTER,) * 6

    inner = lift_word(phases, inner_word)
    outer = lift_word(phases, outer_word)
    assert len(inner) == 13 and inner[0] == inner[-1]
    assert len(outer) == 13 and outer[0] == outer[-1]

    # Count the 12 phase positions, excluding the repeated terminal start.
    inner_phase_cells = inner[:-1]
    outer_phase_cells = outer[:-1]

    assert len(set(inner_phase_cells)) == 7
    assert sum(cell == ZERO for cell in inner_phase_cells) == 6

    assert len(set(outer_phase_cells)) == 12
    assert all(cell != ZERO for cell in outer_phase_cells)

    # The OUTER law is therefore the unique Q-equivariant deterministic law
    # that supplies an injective, everywhere-nonzero 12-microstate phase lift.
    candidates = []
    for word in (inner_word, outer_word):
        seq = lift_word(phases, word)[:-1]
        if len(set(seq)) == 12 and all(cell != ZERO for cell in seq):
            candidates.append(word)
    assert candidates == [outer_word]


def check_all_20_same_selection():
    # The proof is representation-independent, but verify the exact Cell
    # sequence property on every selected triad.
    from itertools import combinations

    checked = 0
    for S in combinations(range(tri.N), 3):
        phases = q_orbit(S)
        inner = lift_word(phases, (INNER,) * 6)[:-1]
        outer = lift_word(phases, (OUTER,) * 6)[:-1]
        assert len(set(inner)) == 7
        assert sum(cell == ZERO for cell in inner) == 6
        assert len(set(outer)) == 12
        assert all(cell != ZERO for cell in outer)
        checked += 1
    assert checked == 20


def main():
    check_equivariant_sections()
    check_faithful_c12_selector()
    check_all_20_same_selection()

    print("PASS: triadic Viète OUTER law selection")
    print("shortest_branch_words", 64)
    print("Q_equivariant_deterministic_words", 2)
    print("equivariant_words", "IIIIII, OOOOOO")
    print("all_inner_distinct_phase_cells", 7)
    print("all_outer_distinct_phase_cells", 12)
    print("faithful_nonzero_C12_equivariant_laws", 1)
    print("selected_law", "OOOOOO")


if __name__ == "__main__":
    main()
