"""Finite incidence-graph and named transport checks for k=1,2,3 (Python 3.10+)."""
from collections import defaultdict, deque
from itertools import combinations, permutations
from math import factorial


def subsets(universe, k):
    return tuple(frozenset(s) for s in combinations(universe, k))


def connect(graph, first, second):
    graph[first].add(second)
    graph[second].add(first)


def graph_rank(graph):
    start = next(iter(graph))
    queue = deque([start])
    seen = {start}
    while queue:
        for nxt in graph[queue.popleft()] - seen:
            seen.add(nxt)
            queue.append(nxt)
    assert len(seen) == len(graph)
    edges = sum(map(len, graph.values())) // 2
    return len(graph), edges, edges - len(graph) + 1


def transport(frame, new):
    old = set(frame)
    if len(old - new) != 1 or len(new - old) != 1:
        raise ValueError("Support exchange needs adjacent endpoints.")
    added, = new - old
    return tuple(x if x in new else added for x in frame)


def incidence_word(route):
    word = [route[0]]
    for left, right in zip(route, route[1:]):
        word.extend((left & right, right))
    reduced = []
    for vertex in word:
        if len(reduced) >= 2 and reduced[-2] == vertex:
            reduced.pop()
        else:
            reduced.append(vertex)
    return reduced


def end_frame(route):
    frame = tuple(sorted(route[0]))
    for right in route[1:]:
        frame = transport(frame, right)
    return frame


def twice_subdivided_witness(k):
    # 0 denotes a, 1 denotes c, 2 denotes u, 3 denotes d.
    common = frozenset(range(4, 4 + k - 2))
    def support(x, y):
        return common | {x, y}
    start, middle, end = support(0, 1), support(0, 2), support(0, 3)
    route = [start, support(1, 2), middle, support(2, 3), end]
    assert start & middle & end == common | {0}
    assert len(start & route[1] & middle) == len(middle & route[3] & end) == k - 2
    baseline = [start, support(0, 3), middle, support(0, 1), end]
    assert end_frame(route) == end_frame(baseline) == end_frame([start, end])
    assert incidence_word(baseline) == incidence_word([start, end])
    reduced_loop = incidence_word(route + [start])
    assert len(reduced_loop) == 9 and reduced_loop[0] == reduced_loop[-1]
    assert len(set(reduced_loop[:-1])) == 8


def check():
    for k, expected in enumerate(((0, 0), (6, 11), (26, 151)), 1):
        universe = tuple(range(k + 3))
        base, lift = defaultdict(set), defaultdict(set)
        for support in subsets(universe, k):
            for x in support:
                common = support - {x}
                connect(base, support, common)
                for frame in permutations(sorted(support)):
                    partial = tuple(None if axis == x else axis for axis in frame)
                    connect(lift, frame, partial)
        nv, ne, rk = graph_rank(base)
        lv, le, kernel_rank = graph_rank(lift)
        assert (rk, kernel_rank) == expected
        assert (lv, le) == (nv * factorial(k), ne * factorial(k))
        if k >= 2:
            twice_subdivided_witness(k)
        print(f"k={k}: incidence V={nv}, E={ne}, rank={rk}; named cover V={lv}, E={le}, rank={kernel_rank}")


if __name__ == "__main__":
    check()
