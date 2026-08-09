"""Primitive root-count shadows derived from binary code weight spectra.

For binary Construction-A preimages, minimum grade four is a tie between
residue-preserving +/-2 axis events and +/-1 lifts of weight-four codewords.
If a length-N code has A4 weight-four codewords and no lower nonzero weight,
then the minimum-grade primitive event count is

    2N + 16*A4.

The [7,3,4] simplex code has seven nonzero codewords, all weight four, giving
14+112=126 primitive events (the E7 root count).  The extended [8,4,4] Hamming
code has fourteen weight-four codewords, giving 16+224=240 (the E8 root count).
These code-lattice correspondences are classical; the project uses them as a
causal conservation/minimum-grade interpretation.
"""

from __future__ import annotations

from .causal_code_lattice import (
    binary_span,
    construction_a_primitive_events,
    extended_hamming_8_code,
    minimum_hamming_weight,
    weight_histogram,
)


def simplex_7_code():
    rows = (
        (0, 0, 0, 1, 1, 1, 1),
        (0, 1, 1, 0, 0, 1, 1),
        (1, 0, 1, 0, 1, 0, 1),
    )
    return binary_span(rows)


def grade_four_primitive_count_from_weight_spectrum(codewords) -> int:
    if minimum_hamming_weight(codewords) != 4:
        raise ValueError("formula requires minimum nonzero Hamming weight four")
    length = len(codewords[0])
    a4 = weight_histogram(codewords).get(4, 0)
    return 2 * length + 16 * a4


def e7_causal_root_count() -> int:
    code = simplex_7_code()
    closed = grade_four_primitive_count_from_weight_spectrum(code)
    direct = len(construction_a_primitive_events(code))
    if closed != direct:
        raise AssertionError("code spectrum formula must match direct primitive events")
    return closed


def e8_causal_root_count() -> int:
    code = extended_hamming_8_code()
    closed = grade_four_primitive_count_from_weight_spectrum(code)
    direct = len(construction_a_primitive_events(code))
    if closed != direct:
        raise AssertionError("code spectrum formula must match direct primitive events")
    return closed


def coxeter_shadow_from_root_count(rank: int, root_count: int) -> int:
    if rank <= 0 or root_count <= 0 or root_count % rank != 0:
        raise ValueError("rank must divide positive root count")
    return root_count // rank
