"""Exact finite corroboration of the P000-compatible conditional X6 star-buffer model.

A state lists the current location of each individually labelled force quantum.
Ports 0..n-1 have capacity 1; n is a central Cell with capacity B.
Moves traverse just one signed primitive X6 spoke. No probabilistic arithmetic.
"""
from collections import deque
from itertools import combinations, product
import json


def shortest(n, capacity, permutation):
    start = tuple(range(n))
    goal = tuple(permutation)
    distance = {start: 0}
    ways = {start: 1}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        depth = distance[state]
        occupied = {p for p in state if p != n}
        hub_count = sum(p == n for p in state)
        for token, old in enumerate(state):
            if old == n:
                destinations = (p for p in range(n) if p not in occupied)
            else:
                destinations = (n,) if hub_count < capacity else ()
            for new in destinations:
                next_state = list(state)
                next_state[token] = new
                next_state = tuple(next_state)
                if next_state not in distance:
                    distance[next_state] = depth + 1
                    ways[next_state] = 0
                    queue.append(next_state)
                if distance[next_state] == depth + 1:
                    ways[next_state] += ways[state]
    return distance.get(goal), ways.get(goal, 0)


def simulate_constructive(n):
    """Two-slot optimal schedule for the labelled cycle i -> i+1 (mod n)."""
    where = list(range(n))
    trace = []

    def move(label, destination):
        current = where[label]
        assert current != destination
        assert current == n or destination == n
        assert destination == n or destination not in where
        candidate = where[:]
        candidate[label] = destination
        assert candidate.count(n) <= 2
        assert len({x for x in candidate if x != n}) == len([x for x in candidate if x != n])
        where[:] = candidate
        trace.append((label, current, destination))

    move(0, n)
    move(1, n)
    move(0, 1)
    for i in range(2, n):
        move(i, n)
        move(i-1, i)
    move(n-1, 0)
    assert len(trace) == 2*n
    assert tuple(where) == tuple((i+1)%n for i in range(n))
    assert sorted((source, dest) for _,source,dest in trace) == sorted(
        [(i, n) for i in range(n)] + [(n, i) for i in range(n)]
    )
    return trace


def unit_step(v):
    return sum(abs(x) for x in v) == 1


def signed_x6_cases():
    count = 0
    for axes in combinations(range(6), 3):
        for signs in product((-1, 1), repeat=3):
            vertices = []
            for axis, sign in zip(axes, signs):
                v = [0]*6
                v[axis] = sign
                vertices.append(tuple(v))
            assert len(set(vertices)) == 3
            assert all(unit_step(v) for v in vertices)
            for direction in (1, -1):
                for i in range(3):
                    j = (i + direction) % 3
                    incoming = tuple(-v for v in vertices[i])
                    outgoing = vertices[j]
                    assert unit_step(incoming) and unit_step(outgoing)
                    assert tuple(vertices[i][t] + incoming[t] + outgoing[t] for t in range(6)) == vertices[j]
            count += 1
    return count


def source_residual():
    # Both orientations record the same six boundary TRANSFER types.
    distinct = []
    for k in range(1, 7):
        values = {sum(w) % 3 for w in product((-1, 1), repeat=k)}
        assert len(values) == (2 if k == 1 else 3)
        distinct.append((k, len(values)))
    return distinct


def main():
    census = []
    for n in range(2, 7):
        goal = tuple((i+1) % n for i in range(n))
        illegal, illegal_ways = shortest(n, 1, goal)
        assert illegal is None and illegal_ways == 0
        moves, schedules = shortest(n, 2, goal)
        assert moves == 2*n, (n, moves)
        assert schedules == n * 2**(n-1), (n, schedules)
        simulate_constructive(n)
        census.append({"cycle_size": n, "minimum_moves": moves, "shortest_schedules_capacity_2": schedules})
    signed_cases = signed_x6_cases()
    assert signed_cases == 160
    residual = source_residual()
    result = {
        "schema":"R762AC_X6_STAR_BUFFER_EXACT_V1",
        "status":"PASS",
        "model":"conditional source-labelled full-occupancy star with unbounded source identity",
        "finite_check":"BFS on all reachable labelled placements, n=2..6, B=1 and B=2",
        "census":census,
        "signed_three_port_incidence_cases":signed_cases,
        "cyclic_source_residual_by_macro_count":residual,
        "arithmetic":"exact integer and finite tuples",
        "universal_proof":"in companion research note; finite testing is corroboration"
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


if __name__ == "__main__":
    main()
