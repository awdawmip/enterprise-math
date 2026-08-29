#!/usr/bin/env python3
"""
Exact regression for RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING.

Standard-library only.  It verifies:
1. local pairing/rectangle degeneration counts on 1 <= r,s <= 200;
2. the exact 3:2 resonance intersection law;
3. support-faithful carrier CW homology for mixed finite column sets;
4. disconnected links at resonance pinch points;
5. the canonical carrier-height cocycle and its nonzero period on every
   resonance generator;
6. support-erasure H2 and atom-lift ambiguity as negative controls.

No numerical distance and no factor-recovery objective is used.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd

TASK = "RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING"


class UF:
    def __init__(self, xs):
        self.parent = {x: x for x in xs}

    def find(self, x):
        p = self.parent[x]
        if p != x:
            self.parent[x] = self.find(p)
        return self.parent[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[b] = a


def rank_q(rows):
    """Exact matrix rank over Q from a list of row lists."""
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][c]
        a[r] = [x / pivot for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def local_signature(r, s):
    p0 = tuple(sorted((6, r * s)))
    p1 = tuple(sorted((2 * r, 3 * s)))
    p2 = tuple(sorted((2 * s, 3 * r)))
    positions = (2 * r, 2 * s, 3 * r, 3 * s)
    return {
        "n_pairing_states": len({p0, p1, p2}),
        "n_rectangle_positions": len(set(positions)),
        "equality": r == s,
        "resonance": r != s and (2 * r == 3 * s or 2 * s == 3 * r),
        "overlap": gcd(r, s) > 1,
        "seed_collision": (r in (2, 3) or s in (2, 3)),
    }


def resonance_pairs(columns):
    """Sorted unordered resonance pairs. For r<s, necessarily 3r=2s."""
    cols = tuple(sorted(set(columns)))
    out = []
    for r, s in combinations(cols, 2):
        if 3 * r == 2 * s:
            out.append((r, s))
        elif 2 * r == 3 * s:
            raise AssertionError("impossible for sorted r<s")
    return out


def build_carrier_complex(columns):
    """
    Build the normalized support-faithful carrier complex.

    Start with K_R x I on distinct exact bundle objects R.
    For each 3r=2s, identify only the exact equal rectangle positions
    (3,r) ~ (2,s).  Edge identities and face identities are retained:
    support is not erased.
    """
    cols = tuple(sorted(set(columns)))
    k = len(cols)
    vertices = [(row, r) for row in (2, 3) for r in cols]
    uf = UF(vertices)
    resonances = resonance_pairs(cols)
    for r, s in resonances:
        uf.union((3, r), (2, s))

    roots = {}
    for v in vertices:
        root = uf.find(v)
        if root not in roots:
            roots[root] = len(roots)
    qv = {v: roots[uf.find(v)] for v in vertices}
    V = len(roots)

    edges = []  # (name, tail, head, type)
    for r in cols:
        edges.append((f"v:{r}", (2, r), (3, r), "vertical"))
    for r, s in combinations(cols, 2):
        edges.append((f"h2:{r}:{s}", (2, r), (2, s), "horizontal"))
        edges.append((f"h3:{r}:{s}", (3, r), (3, s), "horizontal"))
    eid = {e[0]: i for i, e in enumerate(edges)}
    E = len(edges)

    faces = []
    for r, s in combinations(cols, 2):
        bd = {
            eid[f"h2:{r}:{s}"]: +1,
            eid[f"v:{s}"]: +1,
            eid[f"h3:{r}:{s}"]: -1,
            eid[f"v:{r}"]: -1,
        }
        corners = [
            ((2, r), eid[f"v:{r}"], eid[f"h2:{r}:{s}"]),
            ((2, s), eid[f"h2:{r}:{s}"], eid[f"v:{s}"]),
            ((3, s), eid[f"v:{s}"], eid[f"h3:{r}:{s}"]),
            ((3, r), eid[f"h3:{r}:{s}"], eid[f"v:{r}"]),
        ]
        faces.append(((r, s), bd, corners))
    F = len(faces)

    d1 = [[0] * E for _ in range(V)]
    for e, (_, a, b, _) in enumerate(edges):
        qa, qb = qv[a], qv[b]
        if qa != qb:
            d1[qa][e] -= 1
            d1[qb][e] += 1

    d2 = [[0] * F for _ in range(E)]
    for f, (_, bd, _) in enumerate(faces):
        for e, c in bd.items():
            d2[e][f] = c

    for i in range(V):
        for f in range(F):
            assert sum(d1[i][e] * d2[e][f] for e in range(E)) == 0

    r1 = rank_q(d1)
    r2 = rank_q(d2)
    betti = (V - r1, E - r1 - r2, F - r2)

    alpha = [1 if typ == "vertical" else 0 for _, _, _, typ in edges]
    for f in range(F):
        assert sum(alpha[e] * d2[e][f] for e in range(E)) == 0

    incident = defaultdict(set)
    for e, (_, a, b, _) in enumerate(edges):
        incident[qv[a]].add(e)
        incident[qv[b]].add(e)
    link_edges = defaultdict(list)
    for _, _, corners in faces:
        for v, e1, e2 in corners:
            link_edges[qv[v]].append((e1, e2))

    link_stats = {}
    for q in range(V):
        nodes = set(incident[q])
        adj = {x: set() for x in nodes}
        for a, b in link_edges[q]:
            adj.setdefault(a, set()).add(b)
            adj.setdefault(b, set()).add(a)
        seen = set()
        comps = []
        for x in sorted(nodes):
            if x in seen:
                continue
            stack = [x]
            seen.add(x)
            comp = []
            while stack:
                y = stack.pop()
                comp.append(y)
                for z in adj.get(y, ()):
                    if z not in seen:
                        seen.add(z)
                        stack.append(z)
            comps.append(comp)
        link_stats[q] = {
            "vertices": len(nodes),
            "edges": len(link_edges[q]),
            "components": len(comps),
            "component_sizes": sorted(map(len, comps)),
        }

    resonance_witnesses = []
    for r, s in resonances:
        gamma = [0] * E
        gamma[eid[f"h2:{r}:{s}"]] = -1
        gamma[eid[f"v:{r}"]] = +1
        boundary = [
            sum(d1[i][e] * gamma[e] for e in range(E))
            for i in range(V)
        ]
        assert all(x == 0 for x in boundary)
        period = sum(alpha[e] * gamma[e] for e in range(E))
        assert period == 1
        q = qv[(3, r)]
        assert q == qv[(2, s)]
        resonance_witnesses.append((r, s, period, link_stats[q]))

    return {
        "columns": cols,
        "k": k,
        "m": len(resonances),
        "resonances": resonances,
        "V": V,
        "E": E,
        "F": F,
        "betti": betti,
        "rank_d1": r1,
        "rank_d2": r2,
        "alpha": alpha,
        "resonance_witnesses": resonance_witnesses,
        "link_stats": link_stats,
    }


def support_erasure_negative_control(k):
    n = k * (k - 1) // 2
    d2 = [[1] * n, [1] * n, [1] * n]
    rank_d2 = rank_q(d2)
    assert rank_d2 == (1 if n else 0)
    return n - rank_d2


def matching(atom_pairs):
    return frozenset(frozenset(p) for p in atom_pairs)


def perm_apply(perm, M):
    return matching((perm[a], perm[b]) for pair in M for a, b in [tuple(pair)])


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def inverse(p):
    inv = [0] * 4
    for i, x in enumerate(p):
        inv[x] = i
    return tuple(inv)


def atom_lift_negative_control():
    atoms = range(4)
    M0 = matching(((0, 1), (2, 3)))
    M1 = matching(((0, 2), (1, 3)))
    M2 = matching(((0, 3), (1, 2)))
    states = (M0, M1, M2)

    transpositions = []
    for a, b in combinations(atoms, 2):
        p = list(atoms)
        p[a], p[b] = p[b], p[a]
        p = tuple(p)
        image = tuple(states.index(perm_apply(p, M)) for M in states)
        transpositions.append(((a, b), p, image))

    by_image = defaultdict(list)
    for item in transpositions:
        by_image[item[2]].append(item)
    two_lift_classes = [v for v in by_image.values() if len(v) == 2]
    assert len(two_lift_classes) == 3

    a = two_lift_classes[0][0][1]
    b = two_lift_classes[0][1][1]
    ratio = compose(inverse(a), b)
    state_image = tuple(states.index(perm_apply(ratio, M)) for M in states)
    assert state_image == (0, 1, 2)
    assert ratio != (0, 1, 2, 3)
    assert sum(ratio[i] != i for i in atoms) == 4
    return {
        "two_lift_state_transpositions": len(two_lift_classes),
        "kernel_ratio": ratio,
    }


def main():
    joint = Counter()
    for r in range(1, 201):
        for s in range(1, 201):
            sig = local_signature(r, s)
            joint[(sig["n_pairing_states"], sig["n_rectangle_positions"])] += 1
    expected_joint = {
        (3, 4): 38876,
        (3, 3): 130,
        (2, 4): 792,
        (2, 3): 2,
        (2, 2): 198,
        (1, 2): 2,
    }
    assert dict(joint) == expected_joint

    resonance_count = 0
    for r in range(1, 201):
        for s in range(r + 1, 201):
            sig = local_signature(r, s)
            if not sig["resonance"]:
                continue
            resonance_count += 1
            assert r % 2 == 0 and s % 3 == 0
            t = r // 2
            assert (r, s) == (2 * t, 3 * t)
            if t == 1:
                assert (r, s) == (2, 3)
                assert not sig["overlap"]
                assert (sig["n_pairing_states"], sig["n_rectangle_positions"]) == (2, 3)
            else:
                assert sig["overlap"]
                assert not sig["seed_collision"]
                assert (sig["n_pairing_states"], sig["n_rectangle_positions"]) == (3, 3)
    assert resonance_count == 66

    cases = [
        (5, 7, 11),
        (4, 6, 11),
        (4, 6, 9),
        (2, 3, 5),
        (35, 55, 77),
        (4, 6, 25),
        (12, 18, 25),
        (16, 24, 36, 54, 81),
        (25, 125, 7, 11),
    ]

    rows = []
    for cols in cases:
        x = build_carrier_complex(cols)
        k, m = x["k"], x["m"]
        expected_b1 = (k - 1) * (k - 2) // 2 + m
        assert x["betti"] == (1, expected_b1, 0)
        assert x["V"] == 2 * k - m
        assert x["E"] == k * k
        assert x["F"] == k * (k - 1) // 2
        assert x["rank_d2"] == x["F"]
        for r, s, period, link in x["resonance_witnesses"]:
            assert 3 * r == 2 * s
            assert period == 1
            assert link["components"] == 2
            assert link["component_sizes"] == [k, k]
            assert link["vertices"] == 2 * k
            assert link["edges"] == 2 * (k - 1)
        rows.append((cols, m, x["betti"]))

    assert support_erasure_negative_control(4) == 5
    assert support_erasure_negative_control(10) == 44
    lift = atom_lift_negative_control()

    print(f"PASS {TASK}")
    print("joint_signature_census", dict(sorted(joint.items())))
    print("unordered_resonances_r<s<=200", resonance_count)
    for cols, m, betti in rows:
        print("mixed", cols, "m=", m, "betti=", betti)
    print("support_erasure_beta2_k4", support_erasure_negative_control(4))
    print("atom_lift_control", lift)


if __name__ == "__main__":
    main()
