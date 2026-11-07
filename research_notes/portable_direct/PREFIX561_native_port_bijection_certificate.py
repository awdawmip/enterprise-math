#!/usr/bin/env python3
"""PREFIX-561: exact native 96-port exchange lift from frozen four-STAR X6.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires published PREFIX550_shared_gauge_compact_certificate.py.
"""
from collections import Counter
import json
import PREFIX550_shared_gauge_compact_certificate as native

def sigma_signed(x):
    if x == 0:
        return 0
    return (1 if x > 0 else -1) * ({5: 6, 6: 5}.get(abs(x), abs(x)))

def sigma_weight(w):
    return w[:4] + (w[5], w[4]) + w[6:]

def sigma_root(r):
    return r[:4] + (r[5], r[4])

def construct_lift():
    phase_by_pair = {(p, c): i for i, (_, p, c) in enumerate(native.P)}
    assert len(phase_by_pair) == 48
    phase_lift = [phase_by_pair[(sigma_signed(p), sigma_signed(c))]
                  for _, p, c in native.P]
    f = tuple(2 * phase_lift[i // 2] + i % 2 for i in range(96))
    assert all(f[f[i]] == i for i in range(96))
    return f

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def step(rows, vec):
    out = []
    for row in rows:
        c = Counter()
        for (j, w), mult in row.items():
            for mon, coeff in vec[j].items():
                c[add(w, mon)] += mult * coeff
        out.append(c)
    return out

def specialize(w):
    return w[:4] + (w[4] + w[5], 0) + w[6:]

def validate():
    assert len(native.P) == 48 and len(native.V) == 96 and len(native.A) == 6
    f = construct_lift()
    roots = (native.ZERO_ROOT,) + native.ROOTS
    action_lift = {}
    changes = 0
    for i in range(96):
        mapped = []
        for a in native.A:
            j, w = native.edge(i, a, native.ZERO_ROOT)
            found = [aa for aa in native.A
                     if native.edge(f[i], aa, native.ZERO_ROOT)
                     == (f[j], sigma_weight(w))]
            assert len(found) == 1, (i, a)
            action_lift[(i, a)] = found[0]
            mapped.append(found[0])
            changes += found[0] != a
        assert set(mapped) == set(native.A)
    assert all(action_lift[(f[i], action_lift[(i, a)])] == a
               for i in range(96) for a in native.A)
    edges = 0
    for r in roots:
        sr = sigma_root(r)
        for i in range(96):
            for a in native.A:
                j, w = native.edge(i, a, r)
                ja, wa = native.edge(f[i], action_lift[(i, a)], sr)
                assert ja == f[j] and wa == sigma_weight(w), (r, i, a)
                edges += 1
    assert edges == 7488
    ids, growth = native.classes(native.ROOTS[0])
    assert growth == [1, 12, 51]
    pairs = ((1, 14), (3, 17), (4, 18), (6, 32), (8, 34),
             (9, 23), (10, 36), (11, 25), (12, 38), (20, 44),
             (22, 46), (24, 48), (26, 50), (28, 40), (30, 42),
             (35, 47), (37, 49))
    phi = list(range(51))
    for a, b in pairs:
        phi[a], phi[b] = b, a
    assert all(ids[f[i]] == phi[ids[i]] for i in range(96))
    assert f[9] == 9
    assert sorted(f[i] for i in (7, 29, 31)) == [7, 29, 31]
    fixed = sum(f[i] == i for i in range(96))
    assert fixed == 32
    orbits = sorted({tuple(sorted({i, f[i]})) for i in range(96)})
    assert len(orbits) == 64
    orbit_of = {i: k for k, orb in enumerate(orbits) for i in orb}
    special_roots = (native.ZERO_ROOT, (1, 0, 0, 0, 0, 0),
                     (0, 0, -1, 0, 0, 0))
    comparisons = 0
    for r in special_roots:
        assert sigma_root(r) == r
        rows96 = []
        for i in range(96):
            row = Counter()
            for a in native.A:
                j, w = native.edge(i, a, r)
                row[(j, specialize(w))] += 1
            rows96.append(row)
        rows64 = []
        for orb in orbits:
            candidates = []
            for i in orb:
                projected = Counter()
                for (j, w), mult in rows96[i].items():
                    projected[(orbit_of[j], w)] += mult
                candidates.append(projected)
            assert all(x == candidates[0] for x in candidates)
            rows64.append(candidates[0])
        v96 = [Counter({(0,) * 7: 1}) for _ in range(96)]
        v64 = [Counter({(0,) * 7: 1}) for _ in range(64)]
        for d in range(7):
            for i in range(96):
                assert v96[i] == v64[orbit_of[i]], (r, d, i)
                comparisons += 1
            if d < 6:
                v96 = step(rows96, v96)
                v64 = step(rows64, v64)
    assert comparisons == 2016
    return {
        "status": "ALL_CHECKS_PASS",
        "science_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "root_count_including_zero": len(roots),
        "native_edge_equivariance_checks": edges,
        "native_fixed_ports": fixed,
        "native_swapped_port_pairs": (96 - fixed) // 2,
        "action_label_changes": changes,
        "gated_target_port": 9,
        "gated_source_ports": [7, 29, 31],
        "induced_51_class_involution_verified": True,
        "q5_equals_q6_orbit_states": len(orbits),
        "exact_7var_histogram_comparisons_depth0_to6": comparisons,
        "proof_scope": "all nonnegative lengths via exact edge equivalence and path induction",
        "native_path_scope": "ordered actions, branch and gate positions preserved"
    }

if __name__ == "__main__":
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
