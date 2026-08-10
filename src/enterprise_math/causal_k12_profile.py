"""Exact integer primitive-link profile for the Coxeter-Todd lattice K12.

The Gram matrix is exact catalogue data.  Minimal vectors are enumerated from the
integer form; no floating coordinates are needed.  The causal purpose is to
separate several notions often collapsed into one word 'symmetry':

* primitive-direction homogeneity;
* pair/flag continuation-type fragmentation;
* local common-neighbor connectedness.

K12 has one primitive-direction rooted type but nontrivial compatible-pair and
5-flag branching.  Thus direction isotropy does not imply all relation flags are
identical.
"""

from __future__ import annotations

from collections import Counter

from .causal_gram_lattice import Gram, minimal_vectors
from .causal_primitive_link_profile import (
    flag_extension_histograms,
    neighborhood_signature,
    primitive_direction_graph,
)

K12_GRAM: Gram = (
    (4,0,0,-2,0,0,2,-1,-1,-1,2,-1),
    (0,4,0,0,-2,0,2,-1,-1,-1,-1,2),
    (0,0,4,0,0,-2,2,2,2,-1,-1,-1),
    (-2,0,0,4,0,0,-1,-1,2,2,-1,-1),
    (0,-2,0,0,4,0,-1,2,-1,2,-1,-1),
    (0,0,-2,0,0,4,-1,-1,-1,2,2,2),
    (2,2,2,-1,-1,-1,4,0,0,-2,0,0),
    (-1,-1,2,-1,2,-1,0,4,0,0,-2,0),
    (-1,-1,2,2,-1,-1,0,0,4,0,0,-2),
    (-1,-1,-1,2,2,2,-2,0,0,4,0,0),
    (2,-1,-1,-1,-1,2,0,-2,0,0,4,0),
    (-1,2,-1,-1,-1,2,0,0,-2,0,0,4),
)


def k12_minimal_vectors():
    return minimal_vectors(K12_GRAM, 4)


def k12_primitive_profile(maximum_flag_size: int = 6) -> dict[str, object]:
    vectors = k12_minimal_vectors()
    adjacency = primitive_direction_graph(vectors)
    rooted = Counter(neighborhood_signature(adjacency, v) for v in vectors)
    pair_extensions = Counter()
    seen = set()
    for left in vectors:
        for right in adjacency[left]:
            edge = tuple(sorted((left, right)))
            if edge in seen:
                continue
            seen.add(edge)
            pair_extensions[len(adjacency[left].intersection(adjacency[right]))] += 1
    return {
        "primitive_count": len(vectors),
        "degree_histogram": dict(sorted(Counter(len(adjacency[v]) for v in vectors).items())),
        "rooted_context_histogram": dict(rooted),
        "pair_extension_histogram": dict(sorted(pair_extensions.items())),
        "flag_extension_histograms": flag_extension_histograms(adjacency, maximum_flag_size),
    }
