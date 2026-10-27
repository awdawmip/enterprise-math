"""PREFIX-272 exact formal Z2 ordered-path-pair BRC verifier (not native Phi)."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json


def I(a, ids):
    # Keep every labeled ordered pair, positive magnitude and Z2 character.
    branches = [(abs(a[i]), 0 if a[i] >= 0 else 1) for i in ids if a[i]]
    return sum((u * v * (1 if p == q else -1)
                for u, p in branches for v, q in branches), F(0))


def ncomp(k, edges, support):
    nbr = {v: [] for v in support}
    for i, j in edges:
        if i in nbr and j in nbr:
            nbr[i].append(j); nbr[j].append(i)
    seen = set(); count = 0
    for i in support:
        if i in seen: continue
        count += 1; seen.add(i); pending = [i]
        while pending:
            for j in nbr[pending.pop()]:
                if j not in seen: seen.add(j); pending.append(j)
    return count


def check(k, edges, magnitudes):
    support = [i for i in range(k) if magnitudes[i]]
    r = len(support); c = ncomp(k, edges, support)
    groups = Counter(); grams = set()
    for signs in product((-1, 1), repeat=r):
        a = list(magnitudes)
        for j, s in zip(support, signs): a[j] *= s
        signature = tuple(I(a, (i,)) for i in range(k)) + tuple(
            I(a, (i, j)) for i, j in edges)
        groups[signature] += 1
        grams.add(tuple(a[i] * a[j] for i in range(k) for j in range(i, k)))
    assert len(groups) == (2 ** (r-c) if r else 1)
    assert set(groups.values()) == {(2 ** c if r else 1)}
    assert len(grams) == (2 ** (r-1) if r else 1)
    return (len(groups), len(grams), max(c-1, 0))


def cycle_ok(magnitudes, edges, edge_intensities):
    active = {i for i, m in enumerate(magnitudes) if m}
    adjacency = {i: [] for i in active}
    for (i, j), value in zip(edges, edge_intensities):
        if i not in active or j not in active:
            if value != magnitudes[i]**2 + magnitudes[j]**2: return False
            continue
        p = (value-magnitudes[i]**2-magnitudes[j]**2)/(2*magnitudes[i]*magnitudes[j])
        if p not in (-1, 1): return False
        adjacency[i].append((j, p)); adjacency[j].append((i, p))
    signs = {}
    for root in active:
        if root in signs: continue
        signs[root] = 1; todo = [root]
        while todo:
            u = todo.pop()
            for v, p in adjacency[u]:
                s = signs[u]*p
                if v in signs and signs[v] != s: return False
                if v not in signs: signs[v] = s; todo.append(v)
    return True


def run():
    graphs = 0; configurations = 0; by_size = {}
    for k in range(1, 6):
        pairs = list(combinations(range(k), 2)); by_size[k] = 2**len(pairs)
        for mask in product((False, True), repeat=len(pairs)):
            edges = [p for p, include in zip(pairs, mask) if include]
            mags = [F(1)]*k
            check(k, edges, mags)
            assert cycle_ok(mags, edges, [I(mags, e) for e in edges])
            graphs += 1; configurations += 2**k
    q = [F(1,2), F(2,3), F(3,5), F(7,4)]
    rational = {"chain": check(4, [(0,1),(1,2),(2,3)], q),
                "disconnected": check(4, [(0,1),(2,3)], q)}
    z = check(5, [(0,1),(1,2),(2,3),(3,4)], [F(1),F(0),F(2),F(0),F(3)])
    six = [F(1)]*6; pairs = [(0,1),(2,3),(4,5)]
    triple = check(6,pairs,six)
    spanning = check(6,[(i,i+1) for i in range(5)],six)
    a=[F(1)]*6; b=[F(1),F(1),F(-1),F(-1),F(1),F(1)]
    assert all(I(a,e)==I(b,e) for e in pairs)
    assert (I(a,(1,2)),I(b,(1,2))) == (4,0)
    assert not cycle_ok([F(1)]*3,[(0,1),(1,2),(0,2)],[F(4),F(4),F(0)])
    left=[F(1),F(2),F(3),F(5)]; right=[F(1),F(2),F(-3),F(-5)]
    for _ in range(9):
        assert I(left,(0,1))==I(right,(0,1))
        assert I(left,(2,3))==I(right,(2,3))
        left=[left[1],left[0],left[3],left[2]]
        right=[right[1],right[0],right[3],right[2]]
    assert I(left,(1,2)) != I(right,(1,2))
    print(json.dumps({"status":"PASS", "graphs":graphs,"sign_configurations":configurations,
          "graphs_by_k":by_size,"rational":rational,"zero_support":z,
          "six_disjoint_pairs":triple,"six_spanning_tree":spanning,
          "bridge_probe":[4,0],"contradictory_cycle_rejected":True,
          "block_local_steps":9,"source_import_executed":False,
          "native_heartbeat_executed":False},indent=2,sort_keys=True))


if __name__ == "__main__": run()
