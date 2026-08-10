"""Global primitive-step geometry generated from a local simply-laced relation graph.

The causal pair matrix C realizes the abstract translation module

    Z^R / ker(C)  ~=  im_Z(C).

Thus a global state can be represented by the integer relation-signature vector
`C n`, and each primitive unit direction acts by adding one column of C.  Because
the graph-theoretic antipode has the negative column, the primitive generator set
already contains both orientations.

Breadth-first search in this image therefore constructs the exact intrinsic word
ball using only the local primitive relation graph.  Original A/D/E coordinates
are unnecessary after the local graph has been supplied.
"""

from __future__ import annotations

from collections import deque

from .causal_graph_gram_rank import causal_simply_laced_gram
from .causal_primitive_link_profile import Adjacency

RelationState = tuple[int, ...]


def causal_relation_generators(adjacency: Adjacency) -> tuple[RelationState, ...]:
    matrix = causal_simply_laced_gram(adjacency)
    return tuple(
        tuple(row[column] for row in matrix)
        for column in range(len(matrix))
    )


def _add(left: RelationState, right: RelationState) -> RelationState:
    return tuple(a + b for a, b in zip(left, right))


def causal_word_ball(adjacency: Adjacency, radius: int) -> frozenset[RelationState]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    generators = causal_relation_generators(adjacency)
    zero = (0,) * len(generators)
    distance = {zero: 0}
    queue = deque([zero])
    while queue:
        state = queue.popleft()
        depth = distance[state]
        if depth == radius:
            continue
        for generator in generators:
            nxt = _add(state, generator)
            if nxt in distance:
                continue
            distance[nxt] = depth + 1
            queue.append(nxt)
    return frozenset(distance)


def causal_word_ball_count(adjacency: Adjacency, radius: int) -> int:
    return len(causal_word_ball(adjacency, radius))


def causal_word_shell_count(adjacency: Adjacency, radius: int) -> int:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if radius == 0:
        return 1
    return causal_word_ball_count(adjacency, radius) - causal_word_ball_count(adjacency, radius - 1)


def causal_ball_growth(adjacency: Adjacency, maximum_radius: int) -> tuple[int, ...]:
    if (
        isinstance(maximum_radius, bool)
        or not isinstance(maximum_radius, int)
        or maximum_radius < 0
    ):
        raise ValueError("maximum_radius must be a non-negative integer")
    # Single BFS is cheaper than recomputing every nested ball.
    generators = causal_relation_generators(adjacency)
    zero = (0,) * len(generators)
    distance = {zero: 0}
    queue = deque([zero])
    shell_sizes = [1] + [0] * maximum_radius
    while queue:
        state = queue.popleft()
        depth = distance[state]
        if depth == maximum_radius:
            continue
        for generator in generators:
            nxt = _add(state, generator)
            if nxt in distance:
                continue
            next_depth = depth + 1
            distance[nxt] = next_depth
            shell_sizes[next_depth] += 1
            queue.append(nxt)
    total = 0
    balls = []
    for shell in shell_sizes:
        total += shell
        balls.append(total)
    return tuple(balls)
