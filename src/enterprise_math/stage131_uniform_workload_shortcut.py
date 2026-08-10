"""Closed uniform-workload one-shortcut optimizer for Stage131 chains.

For one shortcut a->b on an n-edge chain under uniform unit weight on every
comparable query pair, define positive segment lengths

    x=a+1,
    y=b-a-1,
    z=n-b+1.

They satisfy x+y+z=n+1 and the total query-depth reduction is exactly xyz.
Among positive integer triples with fixed sum, product is maximized exactly when
the parts differ pairwise by at most one.  Therefore the optimal shortcut set is
constructed in O(1) arithmetic (up to at most six permutations), without
scanning all O(n^2) shortcuts.
"""

from __future__ import annotations

from itertools import permutations

from .stage131_chain_tc_spanner import Edge


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def balanced_positive_three_parts(total: int) -> tuple[tuple[int, int, int], ...]:
    s = _positive_int(total, name="total")
    if s < 3:
        raise ValueError("three positive parts require total at least three")
    quotient, remainder = divmod(s, 3)
    if remainder == 0:
        multiset = (quotient, quotient, quotient)
    elif remainder == 1:
        multiset = (quotient + 1, quotient, quotient)
    else:
        multiset = (quotient + 1, quotient + 1, quotient)
    return tuple(sorted(set(permutations(multiset))))


def optimal_uniform_one_shortcuts_closed(chain_length: int) -> tuple[Edge, ...]:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return ()
    edges = {
        (x - 1, x + y)
        for x, y, _z in balanced_positive_three_parts(n + 1)
    }
    return tuple(sorted(edges))


def optimal_uniform_one_shortcut_gain(chain_length: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return 0
    x, y, z = balanced_positive_three_parts(n + 1)[0]
    return x * y * z


def uniform_query_pair_count(chain_length: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    return n * (n + 1) // 2


def uniform_adjacent_total_depth(chain_length: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    return n * (n + 1) * (n + 2) // 6
