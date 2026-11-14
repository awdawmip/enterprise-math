"""R762U: exact integer verification of causal-token lift of V29 event ledgers.
No scientific floating point, trigonometric, or phase operations.
Conditional token semantics only; not a native TRIADIC_CLOSURE_E checker.
"""
from collections import Counter, defaultdict
from itertools import product
import json


def edge_components(edges):
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    components = []
    unseen = set(adj)
    while unseen:
        start = next(iter(unseen))
        unseen.remove(start)
        stack = [start]
        vs = {start}
        while stack:
            for w in adj[stack.pop()]:
                if w in unseen:
                    unseen.remove(w)
                    vs.add(w)
                    stack.append(w)
        components.append(vs)
    return components


def minimum_seeds(edges):
    """Minimum initial tokens under consumptive directed-edge firing, all edges once."""
    out = Counter(a for a, b in edges)
    inc = Counter(b for a, b in edges)
    return sum(
        max(1, sum(max(0, out[v] - inc[v]) for v in comp))
        for comp in edge_components(edges)
    )


def decomposition(edges):
    """Construct optimal edge-disjoint directed trail cover via Euler tours."""
    trails = []
    for component in edge_components(edges):
        local = [(a, b, k, False)
                 for k, (a, b) in enumerate(edges) if a in component]
        out = Counter(a for a, b, _, _ in local)
        inc = Counter(b for a, b, _, _ in local)
        plus = [v for v in sorted(component)
                for _ in range(max(0, out[v] - inc[v]))]
        minus = [v for v in sorted(component)
                 for _ in range(max(0, inc[v] - out[v]))]
        assert len(plus) == len(minus)
        aug = local + [(v, u, -1, True) for v, u in zip(minus, plus)]
        adj = defaultdict(list)
        for k, (a, b, _, _) in enumerate(aug):
            adj[a].append(k)
        stack = [(aug[0][0], None)]
        circuit = []
        while stack:
            v, _ = stack[-1]
            if adj[v]:
                e = adj[v].pop()
                stack.append((aug[e][1], e))
            else:
                _, e = stack.pop()
                if e is not None:
                    circuit.append(e)
        circuit.reverse()
        assert len(circuit) == len(aug)
        if not minus:
            trails.append([aug[e][2] for e in circuit])
        else:
            first = next(i for i, e in enumerate(circuit) if aug[e][3])
            rotated = circuit[first + 1:] + circuit[:first + 1]
            current = []
            for e in rotated:
                if aug[e][3]:
                    assert current
                    trails.append(current)
                    current = []
                else:
                    current.append(aug[e][2])
            assert not current
    assert sorted(i for trail in trails for i in trail) == list(range(len(edges)))
    assert len(trails) == minimum_seeds(edges)
    for trail in trails:
        assert all(edges[i][1] == edges[j][0]
                   for i, j in zip(trail, trail[1:]))
    return trails


def replay(edges, trails):
    inventory = Counter(edges[t[0]][0] for t in trails)
    before = inventory.copy()
    for trail in trails:
        for k in trail:
            a, b = edges[k]
            assert inventory[a] >= 1
            inventory[a] -= 1
            inventory[b] += 1
            assert all(v >= 0 for v in inventory.values())
    assert sum(inventory.values()) == sum(before.values()) == len(trails)
    return dict(sorted(before.items())), dict(
        sorted((k, v) for k, v in inventory.items() if v)
    )


def ledgers(edges):
    M = Counter()
    Rin = Counter()
    Rout = Counter()
    for a, b in edges:
        ca, pa = a.split(':')
        cb, pb = b.split(':')
        if ca == cb:
            M[(ca, pa, pb)] += 1
        else:
            Rout[(ca, pa)] += 1
            Rin[(cb, pb)] += 1

    def u(c, p):
        return (sum(m for (cc, a, b), m in M.items() if cc == c and a == p)
                - sum(m for (cc, a, b), m in M.items() if cc == c and b == p)
                + Rin[c, p] - Rout[c, p])

    return {
        'A_u': [u('A', str(k)) for k in range(4)],
        'B_u': [u('B', str(k)) for k in range(2)],
        'M_A': [[M['A', str(i), str(j)] for j in range(4)]
                for i in range(4)],
        'A_Rin': [Rin['A', str(i)] for i in range(4)],
        'A_Rout': [Rout['A', str(i)] for i in range(4)]
    }


def network_case(shared_B):
    edges = [('A:0', 'A:1'), ('A:1', 'A:2'), ('A:2', 'A:0')]
    B = 'B:0'
    for i, n in [(0, 2), (1, 4), (2, 3)]:
        edges.extend([(f'A:{i}', B if shared_B else 'B:1')] * n)
    edges += [(B, 'A:3')] * 10
    trails = decomposition(edges)
    start, end = replay(edges, trails)
    L = ledgers(edges)
    assert L['A_u'] == [-2, -4, -3, 10]
    assert L['A_Rin'] == [0, 0, 0, 10]
    assert L['A_Rout'] == [2, 4, 3, 0]
    assert sum(L['A_u']) + sum(L['B_u']) == 0
    assert sum(len(t) for t in trails) == 22
    return dict(
        edges=22, passes=3, transfers=19,
        min_seeds=minimum_seeds(edges),
        components=len(edge_components(edges)),
        initial=start, final=end, V29=L
    )


def check_all_simple_graphs(n):
    vertices = [str(i) for i in range(n)]
    possible = [(a, b) for a in vertices for b in vertices if a != b]
    tested = 0
    for mask in range(1, 1 << len(possible)):
        es = [e for j, e in enumerate(possible) if mask >> j & 1]
        trails = decomposition(es)
        replay(es, trails)
        tested += 1
    return tested


def check_multigraphs_three_vertices():
    possible = [(str(i), str(j)) for i in range(3) for j in range(3)
                if i != j]
    total = 0
    for counts in product(range(3), repeat=len(possible)):
        edges = [edge for edge, count in zip(possible, counts)
                 for _ in range(count)]
        if not edges:
            continue
        replay(edges, decomposition(edges))
        total += 1
    return total


def run():
    evidence = {
        'schema': 'R762U_EXACT_CAUSAL_SEED_VERIFY_V1',
        'scope': 'conditional V29+single-token firing semantics; NOT native force admission',
        'simple_directed_graphs_checked': {
            str(n): check_all_simple_graphs(n) for n in (2, 3, 4)
        },
        'three_vertex_multigraphs_checked': check_multigraphs_three_vertices(),
        'original_T3_two_B_ports': network_case(False),
        'reconnected_single_B_port': network_case(True),
    }
    assert evidence['original_T3_two_B_ports']['min_seeds'] == 19
    assert evidence['reconnected_single_B_port']['min_seeds'] == 10
    return evidence


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False, sort_keys=True))
