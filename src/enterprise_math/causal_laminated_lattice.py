"""Exact integer causal profiles for laminated dimension lifts Lambda_9..Lambda_12.

The Gram matrices are exact catalogue data.  Minimal vectors are enumerated from
the integer Gram forms by `causal_gram_lattice` and then treated only as primitive
integer displacement labels.  A pair u,v is primitive-link adjacent when v-u is
itself minimal.

The purpose is not to reprove packing density.  It is to measure how dimension
extension preserves primitive states, adds new states, refines old local types,
or—when provenance is forgotten—can re-symmetrize intrinsic present geometry.
"""

from __future__ import annotations

from collections import Counter

from .causal_gram_lattice import Gram, minimal_vectors
from .causal_primitive_link_profile import neighborhood_signature, primitive_direction_graph

LAMBDA9_GRAM: Gram = (
    (4,-2,0,0,0,0,0,0,0),
    (-2,4,-2,2,0,0,0,0,0),
    (0,-2,4,0,0,2,0,0,0),
    (0,2,0,4,2,2,0,0,0),
    (0,0,0,2,4,2,0,0,2),
    (0,0,2,2,2,4,2,2,1),
    (0,0,0,0,0,2,4,2,0),
    (0,0,0,0,0,2,2,4,0),
    (0,0,0,0,2,1,0,0,4),
)

LAMBDA10_GRAM: Gram = (
    (4,-2,0,0,0,0,0,0,0,0),
    (-2,4,-2,2,0,0,0,0,0,0),
    (0,-2,4,0,0,2,0,0,0,0),
    (0,2,0,4,2,2,0,0,0,0),
    (0,0,0,2,4,2,0,0,2,1),
    (0,0,2,2,2,4,2,2,1,2),
    (0,0,0,0,0,2,4,2,0,2),
    (0,0,0,0,0,2,2,4,0,2),
    (0,0,0,0,2,1,0,0,4,2),
    (0,0,0,0,1,2,2,2,2,4),
)

LAMBDA11_GRAM: Gram = (
    (4,-2,0,0,0,0,0,0,0,0,0),
    (-2,4,-2,2,0,0,0,0,0,0,0),
    (0,-2,4,0,0,2,0,0,0,0,0),
    (0,2,0,4,2,2,0,0,0,0,0),
    (0,0,0,2,4,2,0,0,2,1,0),
    (0,0,2,2,2,4,2,2,1,2,0),
    (0,0,0,0,0,2,4,2,0,2,0),
    (0,0,0,0,0,2,2,4,0,2,0),
    (0,0,0,0,2,1,0,0,4,2,0),
    (0,0,0,0,1,2,2,2,2,4,2),
    (0,0,0,0,0,0,0,0,0,2,4),
)

LAMBDA12_GRAM: Gram = (
    (4,-2,0,0,0,0,0,0,0,0,0,0),
    (-2,4,-2,2,0,0,0,0,0,0,0,0),
    (0,-2,4,0,0,2,0,0,0,0,0,0),
    (0,2,0,4,2,2,0,0,0,0,0,0),
    (0,0,0,2,4,2,0,0,2,1,0,0),
    (0,0,2,2,2,4,2,2,1,2,0,0),
    (0,0,0,0,0,2,4,2,0,2,0,0),
    (0,0,0,0,0,2,2,4,0,2,0,0),
    (0,0,0,0,2,1,0,0,4,2,0,0),
    (0,0,0,0,1,2,2,2,2,4,2,2),
    (0,0,0,0,0,0,0,0,0,2,4,2),
    (0,0,0,0,0,0,0,0,0,2,2,4),
)


def _minimal(gram: Gram) -> tuple[tuple[int, ...], ...]:
    return minimal_vectors(gram, 4)


def lambda9_minimal_vectors(): return _minimal(LAMBDA9_GRAM)
def lambda10_minimal_vectors(): return _minimal(LAMBDA10_GRAM)
def lambda11_minimal_vectors(): return _minimal(LAMBDA11_GRAM)
def lambda12_minimal_vectors(): return _minimal(LAMBDA12_GRAM)


def primitive_degree_histogram(vectors):
    adjacency = primitive_direction_graph(vectors)
    return dict(sorted(Counter(len(adjacency[v]) for v in vectors).items()))


def rooted_context_histogram(vectors):
    adjacency = primitive_direction_graph(vectors)
    return dict(Counter(neighborhood_signature(adjacency, v) for v in vectors))


def layer_histogram(vectors, coordinate=-1):
    return dict(sorted(Counter(v[coordinate] for v in vectors).items()))


def layer_degree_histogram(vectors, coordinate=-1):
    adjacency = primitive_direction_graph(vectors)
    return dict(sorted(Counter((v[coordinate], len(adjacency[v])) for v in vectors).items()))


def embedded_degree_transition(old_vectors, new_vectors):
    if not old_vectors or not new_vectors or len(new_vectors[0]) != len(old_vectors[0]) + 1:
        raise ValueError("new shell must be a one-coordinate lift of the old shell")
    old_adjacency = primitive_direction_graph(old_vectors)
    new_adjacency = primitive_direction_graph(new_vectors)
    new_set = set(new_vectors)
    transition = Counter()
    for old in old_vectors:
        lifted = old + (0,)
        if lifted not in new_set:
            raise ValueError("new primitive shell does not contain embedded old shell")
        transition[(len(old_adjacency[old]), len(new_adjacency[lifted]))] += 1
    return dict(sorted(transition.items()))


def rooted_context_transition(old_vectors, new_vectors):
    """Incidence between old and new rooted local signatures on retained states."""
    old_adjacency = primitive_direction_graph(old_vectors)
    new_adjacency = primitive_direction_graph(new_vectors)
    new_set = set(new_vectors)
    counter = Counter()
    for old in old_vectors:
        lifted = old + (0,)
        if lifted not in new_set:
            raise ValueError("new primitive shell does not contain embedded old shell")
        counter[(
            neighborhood_signature(old_adjacency, old),
            neighborhood_signature(new_adjacency, lifted),
        )] += 1
    return dict(counter)


def layer_edge_histogram(vectors, coordinate=-1):
    adjacency = primitive_direction_graph(vectors)
    seen = set(); counts = Counter()
    for left in vectors:
        for right in adjacency[left]:
            edge = tuple(sorted((left, right)))
            if edge in seen: continue
            seen.add(edge)
            counts[tuple(sorted((left[coordinate], right[coordinate])))] += 1
    return dict(sorted(counts.items()))


def _profile(vectors, previous=None):
    result = {
        "minimal_vector_count": len(vectors),
        "degree_histogram": primitive_degree_histogram(vectors),
        "rooted_context_histogram": rooted_context_histogram(vectors),
        "layer_histogram": layer_histogram(vectors),
        "layer_degree_histogram": layer_degree_histogram(vectors),
        "layer_edge_histogram": layer_edge_histogram(vectors),
    }
    if previous is not None:
        result["old_degree_transition"] = embedded_degree_transition(previous, vectors)
        result["old_rooted_context_transition"] = rooted_context_transition(previous, vectors)
    return result


def lambda9_profile(): return _profile(lambda9_minimal_vectors())
def lambda10_profile(): return _profile(lambda10_minimal_vectors(), lambda9_minimal_vectors())
def lambda11_profile(): return _profile(lambda11_minimal_vectors(), lambda10_minimal_vectors())
def lambda12_profile(): return _profile(lambda12_minimal_vectors(), lambda11_minimal_vectors())
