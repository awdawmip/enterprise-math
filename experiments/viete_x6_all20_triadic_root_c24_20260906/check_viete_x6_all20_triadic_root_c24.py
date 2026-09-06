#!/usr/bin/env python3
"""Exact bridge from universal X6 triadic C6/C12 rotation to Viète +/-3 and C24.

Reuses the already-published triadic rotation checker/module.  The new checks
identify the oriented half-turn midpoint on the all-OUTER microtrace as a
balanced two-component native Cell and attach the principal C12/C24 readouts.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from math import gcd
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


def neg(z):
    return tuple(-x for x in z)


def norm2(z):
    return sum(x * x for x in z)


def support(z):
    return sum(x != 0 for x in z)


def orbit(q, start):
    out = [start]
    for _ in range(5):
        out.append(tri.act(q, out[-1]))
    return tuple(out)


def outer_cycle(phases):
    out = []
    for r in range(6):
        a = phases[r]
        b = phases[(r + 1) % 6]
        out.extend((a, tri.add(a, b)))
    return tuple(out)


def mul_pair(x, y):
    """Multiply a+bJ and c+dJ with J^2=-1."""
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c


def modulus(m):
    return 6 * (2**m)


def order_mod(x, n):
    return n // gcd(x % n, n)


def check_all_20_oriented_half_turn_roots():
    checked = 0
    for S in combinations(range(6), 3):
        q = tri.q_triad(S)
        q_inv = tri.power(q, 5)
        a0 = tri.unit(S[0])

        forward = orbit(q, a0)
        reverse = orbit(q_inv, a0)
        assert forward[3] == neg(a0)
        assert reverse[3] == neg(a0)

        forward_cycle = outer_cycle(forward)
        reverse_cycle = outer_cycle(reverse)
        assert len(set(forward_cycle)) == 12
        assert len(set(reverse_cycle)) == 12

        # A half-turn is six microsteps; its half-way microstate is microstep 3.
        root_f = forward_cycle[3]
        root_r = reverse_cycle[3]
        assert root_f == tri.add(forward[1], forward[2])
        assert root_r == tri.add(reverse[1], reverse[2])
        assert root_r == neg(root_f)

        # The C12 root Cell is a balanced two-component native displacement.
        assert support(root_f) == 2
        assert norm2(root_f) == 2
        assert tri.brc.shortest_event_count(root_f) == 2
        assert tri.brc.shortest_path_multiplicity(root_f) == 2

        # Its two local signed component basis vectors are exactly the adjacent
        # unit phases with coordinates (1,1).
        assert tri.add(forward[1], forward[2]) == root_f
        assert norm2(forward[1]) == 1
        assert norm2(forward[2]) == 1
        assert support(forward[1]) == 1
        assert support(forward[2]) == 1

        checked += 2

    assert checked == 40


def check_principal_phase_and_spinor_readouts():
    # Use one fixed reference character marker J.  The orientation sheet eps
    # changes J -> eps*J.  Numerators omit the common sqrt(2) denominator.
    for eps in (-1, 1):
        # C12 root coordinate is +/-3 and has order four.
        assert order_mod(3 * eps, 12) == 4

        # Balanced spinor U2=(1+eps J)/sqrt(2).
        u_num = (1, eps)
        square_num = mul_pair(u_num, u_num)
        assert square_num == (0, 2 * eps)  # U2^2 = eps*J after /2

        # Sweep reversal produces the inverse spinor.
        inv_num = (1, -eps)
        assert mul_pair(u_num, inv_num) == (2, 0)

        # Same orientation sheet selects the entire principal +/-3 tower.
        for m in range(12):
            n = modulus(m)
            value = (3 * eps) % n
            assert order_mod(value, n) == 2 ** (m + 1)
            if m == 0:
                assert 3 % n == (-3) % n
            else:
                assert 3 % n != (-3) % n


def check_brc_branch_horizons():
    words = tuple(product((0, 1), repeat=6))  # 0=INNER, 1=OUTER
    assert len(words) == 64

    # Full C12 phase-refinement horizon asks for a nonzero midpoint on every
    # macro edge.  That uniquely selects the all-OUTER branch word.
    full_phase_words = tuple(word for word in words if all(word))
    assert full_phase_words == ((1, 1, 1, 1, 1, 1),)

    # One specified half-turn quarter-root readout only inspects the midpoint
    # of macro edge r=1 for the chosen start convention; exactly half the path
    # population remains admissible.
    one_root_words = tuple(word for word in words if word[1] == 1)
    assert len(one_root_words) == 32

    # Endpoint/frame-only observation discards all six branch bits.
    assert len(words) == 2**6


def main():
    check_all_20_oriented_half_turn_roots()
    check_principal_phase_and_spinor_readouts()
    check_brc_branch_horizons()

    print("PASS: all-20 X6 triadic Viète root/C24 bridge")
    print("oriented_triad_root_arcs_checked", 40)
    print("C12_root_cell", "balanced support-2 native Cell, norm^2=2, B_min=2")
    print("C24_anchor", "normalized same balanced component state")
    print("principal_precision_sheet", "+/-3 at all finite levels")
    print("full_C12_nonzero_midpoint_branch_words", 1)
    print("single_specified_root_branch_words", 32)
    print("endpoint_only_branch_words", 64)


if __name__ == "__main__":
    main()
