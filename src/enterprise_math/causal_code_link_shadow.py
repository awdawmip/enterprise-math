"""First-link relation density from minimum codeword incidence in grade-four code lattices.

Assume a binary length-N code has minimum nonzero Hamming weight four, so
Construction-A minimum square grade four contains both +/-2 axis events and
weight-four +/-1 sign lifts.  For a positive axis event +2e_i, an adjacent
weight-four event must contain coordinate i with positive sign.  Each containing
support yields 2^3=8 such sign lifts.

If every coordinate lies in exactly r weight-four codeword supports, the axis
primitive-link degree is 8r.  With A4 total weight-four codewords, incidence
counting gives 4A4=Nr, hence degree=32A4/N.  For event-transitive examples such as
the [7,3,4] simplex/E7 and extended [8,4,4] Hamming/E8 constructions this is the
full primitive-link degree.  Combined with |Phi|=2N+16A4, one gets

    |Phi|/N = 2 + degree/2,

recovering the simply-laced Coxeter shadow from code incidence.
"""

from __future__ import annotations

from collections import Counter

from .causal_code_lattice import hamming_weight


def weight_four_words(codewords):
    return tuple(word for word in codewords if hamming_weight(word) == 4)


def coordinate_weight_four_incidence(codewords) -> tuple[int, ...]:
    words = weight_four_words(codewords)
    if not codewords:
        raise ValueError("codeword set must be non-empty")
    length = len(codewords[0])
    return tuple(
        sum(word[index] for word in words)
        for index in range(length)
    )


def weight_four_incidence_is_uniform(codewords) -> bool:
    incidence = coordinate_weight_four_incidence(codewords)
    return len(set(incidence)) <= 1


def uniform_weight_four_incidence(codewords) -> int:
    incidence = coordinate_weight_four_incidence(codewords)
    if len(set(incidence)) != 1:
        raise ValueError("weight-four support incidence is not coordinate-uniform")
    return incidence[0]


def axis_primitive_link_degree_from_code(codewords) -> int:
    return 8 * uniform_weight_four_incidence(codewords)


def incidence_formula_link_degree(codewords) -> int:
    if not weight_four_incidence_is_uniform(codewords):
        raise ValueError("formula requires coordinate-uniform weight-four incidence")
    length = len(codewords[0])
    a4 = len(weight_four_words(codewords))
    numerator = 32 * a4
    if numerator % length != 0:
        raise AssertionError("uniform incidence must make 32*A4 divisible by N")
    return numerator // length


def grade_four_root_count(codewords) -> int:
    length = len(codewords[0])
    a4 = len(weight_four_words(codewords))
    return 2 * length + 16 * a4


def coxeter_shadow_from_code_incidence(codewords) -> int:
    length = len(codewords[0])
    roots = grade_four_root_count(codewords)
    if roots % length != 0:
        raise ValueError("root count is not rank-divisible")
    h_from_roots = roots // length
    h_from_link = 2 + axis_primitive_link_degree_from_code(codewords) // 2
    if h_from_roots != h_from_link:
        raise AssertionError("root-count and link-incidence shadows must agree")
    return h_from_roots
