"""First-link homogeneity criterion from binary weight-four code support data.

In the grade-four Construction-A resonance regime, primitive events are axis
+/-2e_i and sign lifts of weight-four codeword supports.

Let r_i be the number of weight-four supports containing coordinate i.  An axis
primitive event at i has 8*r_i primitive neighbors.

For a glue event on support S, neighbors split into:
* four axis events;
* four same-support one-sign flips (whose difference is an axis event);
* four sign lifts for every other weight-four support T with |S intersect T|=2.
Thus glue link degree is 8+4*N2(S).

If coordinate incidence r is uniform and intersection-two count N2 is uniform,
axis and glue provenance sectors have equal first-link degree exactly when

    N2 = 2*r - 2.

The [7,3,4] simplex and extended [8,4,4] Hamming support systems satisfy this,
giving degrees 32 and 56.  This recovers part of exceptional root homogeneity
from code support combinatorics instead of taking Weyl symmetry as primitive.
"""

from __future__ import annotations

from collections import Counter

from .causal_code_lattice import hamming_weight

Support = frozenset[int]


def weight_four_supports(codewords) -> tuple[Support, ...]:
    return tuple(
        frozenset(index for index, bit in enumerate(word) if bit)
        for word in codewords
        if hamming_weight(word) == 4
    )


def coordinate_incidence(codewords) -> tuple[int, ...]:
    supports = weight_four_supports(codewords)
    if not codewords:
        raise ValueError("codeword family must be non-empty")
    length = len(codewords[0])
    return tuple(sum(index in support for support in supports) for index in range(length))


def intersection_two_counts(codewords) -> tuple[int, ...]:
    supports = weight_four_supports(codewords)
    return tuple(
        sum(other != support and len(other & support) == 2 for other in supports)
        for support in supports
    )


def axis_link_degrees(codewords) -> tuple[int, ...]:
    return tuple(8 * incidence for incidence in coordinate_incidence(codewords))


def glue_link_degrees(codewords) -> tuple[int, ...]:
    return tuple(8 + 4 * count for count in intersection_two_counts(codewords))


def provenance_degree_is_uniform(codewords) -> bool:
    return len(set(axis_link_degrees(codewords)) | set(glue_link_degrees(codewords))) == 1


def homogeneity_balance_identity(codewords) -> bool:
    incidences = coordinate_incidence(codewords)
    intersections = intersection_two_counts(codewords)
    if not incidences or not intersections:
        return False
    if len(set(incidences)) != 1 or len(set(intersections)) != 1:
        return False
    r = incidences[0]
    n2 = intersections[0]
    return n2 == 2 * r - 2


def support_intersection_histogram(codewords) -> dict[int, int]:
    supports = weight_four_supports(codewords)
    histogram = Counter()
    for index, left in enumerate(supports):
        for right in supports[index + 1 :]:
            histogram[len(left & right)] += 1
    return dict(sorted(histogram.items()))
