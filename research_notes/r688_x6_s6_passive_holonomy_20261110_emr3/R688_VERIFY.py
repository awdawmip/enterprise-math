#!/usr/bin/env python3
"""R688 exact X6/S6 triadic-axis rotation and BRC positive rational branch checker."""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from fractions import Fraction

I = tuple(range(6))
A = (0, 1, 2)
B = (3, 4, 5)
V = tuple(combinations(I, 3))
N = {s: tuple(t for t in V if len(set(s) & set(t)) == 2) for s in V}

def compose(q, p):
    return tuple(q[j] for j in p)

def transposition(a, b):
    p = list(I)
    p[a], p[b] = p[b], p[a]
    return tuple(p)

def active(p):
    return tuple(sorted(p[i] for i in A))

def fullframe(p):
    return tuple(p[i] for i in A), tuple(p[i] for i in B)

def step(s, p, t):
    assert t in N[s] and active(p) == s
    a = next(iter(set(s) - set(t)))
    b = next(iter(set(t) - set(s)))
    q = compose(transposition(a, b), p)
    assert active(q) == t
    return q

def parity(p):
    return sum(p[i] > p[j] for i in I for j in range(i + 1, 6)) % 2

def exact_walk_counts(k):
    states = {(A, I): 1}
    for _ in range(k):
        after = defaultdict(int)
        for (s, p), count in states.items():
            for t in N[s]:
                after[(t, step(s, p, t))] += count
        states = dict(after)
    assert sum(states.values()) == 9 ** k
    return states

def main():
    assert len(V) == 20 and all(len(N[s]) == 9 for s in V)
    # Enumerate and check all 720 permutations, 6480 directed moves and all (S,F) fibres.
    fibres = defaultdict(set)
    directed = 0
    for p in permutations(I):
        s = active(p)
        f, g = fullframe(p)
        fibres[(s, f)].add(g)
        for t in N[s]:
            q = step(s, p, t)
            assert step(t, q, s) == p
            assert parity(q) != parity(p)
            assert fullframe(q)[0] == tuple(
                next(iter(set(t) - set(s))) if x in (set(s) - set(t)) else x
                for x in f
            )
            directed += 1
    assert directed == 6480
    assert len(fibres) == 120 and all(len(v) == 6 for v in fibres.values())

    # Independent BFS reachability from the initial full axis frame.
    reached = {I}
    q = deque([I])
    while q:
        p = q.popleft()
        for t in N[active(p)]:
            z = step(active(p), p, t)
            if z not in reached:
                reached.add(z)
                q.append(z)
    assert len(reached) == 720

    expected = {
        1: (0, 0, 0, 0, 0),
        2: (9, 9, 0, 0, 0),
        3: (36, 0, 18, 18, 0),
        4: (369, 189, 18, 18, 144),
        5: (2952, 0, 1080, 1080, 792),
    }
    # Tuple entries: total, full identity, active-only, passive-only, both.
    summary = {}
    for k in range(1, 6):
        c = Counter()
        for (s, p), mass in exact_walk_counts(k).items():
            if s != A:
                continue
            f, g = fullframe(p)
            name = ("identity" if f == A and g == B else
                    "passive_only" if f == A else
                    "active_only" if g == B else "both")
            c[name] += mass
        found = (sum(c.values()), c["identity"], c["active_only"],
                 c["passive_only"], c["both"])
        assert found == expected[k], (k, found)
        summary[k] = found

    fibre = Counter()
    for (s, p), mass in exact_walk_counts(3).items():
        if s == A and fullframe(p)[0] == A:
            fibre[fullframe(p)[1]] += mass
    assert set(fibre) == {(3, 5, 4), (4, 3, 5), (5, 4, 3)}
    assert all(m == 6 for m in fibre.values())
    assert sum(fibre.values()) == 18
    assert Fraction(18, 9**3) == Fraction(2, 81)
    assert all(Fraction(m, sum(fibre.values())) == Fraction(1, 3)
               for m in fibre.values())

    # Explicit witnesses with identical t=3 and full active V17 frame.
    witnesses = (
        (A, (0,1,3), (0,1,4), A),
        (A, (0,1,3), (0,1,5), A),
        (A, (0,1,4), (0,1,5), A),
    )
    observed = set()
    for path in witnesses:
        p = I
        for s, t in zip(path, path[1:]):
            p = step(s, p, t)
        assert fullframe(p)[0] == A
        observed.add(fullframe(p)[1])
    assert observed == set(fibre)
    print("R688_X6_S6_ROTATION_BRC_EXACT_PASS")
    print("orientations=720 directed_edges=6480 active_classes=120")
    print("base_closed_walks_1_to_5=", summary)
    print("t3_conditional_passive=", {
        ''.join(map(str,k)): str(Fraction(v,18)) for k,v in sorted(fibre.items())
    })

if __name__ == "__main__":
    main()
