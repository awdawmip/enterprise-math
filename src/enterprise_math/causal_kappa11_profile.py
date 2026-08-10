"""Exact integer primitive-link profile for KAPPA11.

The Gram matrix is catalogue data for the 11-dimensional KAPPA11 lattice
(det=972, minimum=4, kissing number=432).  Minimal vectors are enumerated from
the exact integer Gram form; no floating embedding is used in the causal profile.

This gives a same-dimensional comparison with laminated Lambda11.  The purpose is
not to infer packing density from causal invariants, but to keep packing density,
primitive relation capacity, and rooted causal-type fragmentation as separate
coordinates.
"""

from __future__ import annotations

from collections import Counter

from .causal_gram_lattice import Gram, minimal_vectors
from .causal_primitive_link_profile import neighborhood_signature, primitive_direction_graph

KAPPA11_GRAM: Gram = (
    (4,-2,0,0,0,0,0,0,0,0,0),
    (-2,4,-2,2,0,0,0,0,0,0,-1),
    (0,-2,4,0,0,2,0,2,2,1,2),
    (0,2,0,4,2,2,0,2,1,1,1),
    (0,0,0,2,4,2,2,1,1,1,2),
    (0,0,2,2,2,4,1,2,2,2,2),
    (0,0,0,0,2,1,4,1,2,-1,2),
    (0,0,2,2,1,2,1,4,2,1,2),
    (0,0,2,1,1,2,2,2,4,1,2),
    (0,0,1,1,1,2,-1,1,1,4,1),
    (0,-1,2,1,2,2,2,2,2,1,4),
)


def kappa11_minimal_vectors():
    return minimal_vectors(KAPPA11_GRAM, 4)


def kappa11_profile() -> dict[str, object]:
    vectors = kappa11_minimal_vectors()
    adjacency = primitive_direction_graph(vectors)
    rooted = Counter(neighborhood_signature(adjacency, vector) for vector in vectors)
    return {
        "primitive_count": len(vectors),
        "degree_histogram": dict(sorted(Counter(len(adjacency[v]) for v in vectors).items())),
        "rooted_context_histogram": dict(rooted),
        "rooted_type_sizes": tuple(sorted(rooted.values(), reverse=True)),
    }
