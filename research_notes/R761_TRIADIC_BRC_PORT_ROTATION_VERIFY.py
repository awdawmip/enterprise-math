#!/usr/bin/env python3
"""R761 exact typed branch/port/rotation candidate verifier (no physical-time solver).

Input: one chosen X6 Cell, unit equal force quantum, 6 signed native axes.
An event retains three distinct signed ports, one cyclic orientation and three
source branches. All arithmetic is exact finite BRC incidence/count algebra.
"""
from collections import defaultdict, deque
from itertools import combinations, permutations, product
import json

AX = tuple(range(1, 7))
IDENTITY = AX
PORTS = tuple((a, s) for a in AX for s in (-1, 1))

def normalize_cycle(cycle):
    """Normalize by cyclic rotation only; never quotient by reflection."""
    index = min(range(3), key=lambda j: cycle[j][0])
    return cycle[index:] + cycle[:index]

def events():
    for abc in combinations(AX, 3):
        for signs in product((-1, 1), repeat=3):
            p = tuple(zip(abc, signs))
            yield normalize_cycle(p)
            yield normalize_cycle((p[0], p[2], p[1]))

def rotation(event):
    p = list(IDENTITY)
    for a, b in zip(event, event[1:] + event[:1]):
        p[a[0]-1] = b[0]
    return tuple(p)

def compose(p, q):
    """p o q, each permutation maps axis i to p[i-1]."""
    return tuple(p[q[i]-1] for i in range(6))

def invert(p):
    r = [None]*6
    for i, to in enumerate(p, 1):
        r[to-1] = i
    return tuple(r)

def sign(p):
    inv = sum(p[i] > p[j] for i in range(6) for j in range(i+1, 6))
    return -1 if inv % 2 else 1

def pass_ledger(event):
    """V29 PASS batch: nonnegative M[(source_signed_port,target_signed_port)] occurrences."""
    return {edge: 1 for edge in zip(event, event[1:] + event[:1])}

def contrast(event):
    M = pass_ledger(event)
    u = {p: 0 for p in PORTS}
    omega = defaultdict(int)
    for (a, b), count in M.items():
        u[a] += count
        u[b] -= count
        omega[(a, b)] += count
        omega[(b, a)] -= count
    return (u, {k: v for k, v in omega.items() if v})

def reverse(event):
    return normalize_cycle((event[0], event[2], event[1]))

def relabel(event, perm):
    return normalize_cycle(tuple((perm[i-1], s) for i, s in event))

def image_by_permutation(edge, perm):
    return tuple((perm[i-1], s) for i, s in edge)

def closure_depth(gens):
    seen = {IDENTITY: 0}
    q = deque([IDENTITY])
    while q:
        g = q.popleft()
        for h in gens:
            n = compose(g, h)
            if n not in seen:
                seen[n] = seen[g] + 1
                q.append(n)
    return seen

def closure(gens):
    return set(closure_depth(gens))

def cycle_type(p):
    remaining = set(AX)
    sizes = []
    while remaining:
        i = min(remaining)
        j = i
        count = 0
        while j in remaining:
            remaining.remove(j)
            count += 1
            j = p[j-1]
        sizes.append(count)
    return tuple(sorted(sizes, reverse=True))

def verify():
    ev = tuple(events())
    assert len(ev) == 320 and len(set(ev)) == 320
    assert all(len({p[0] for p in e}) == 3 for e in ev)
    assert all(len(pass_ledger(e)) == 3 for e in ev)
    assert all(all(x == 0 for x in contrast(e)[0].values()) for e in ev)
    assert all(rotation(e) == invert(rotation(reverse(e))) for e in ev)
    assert all(rotation(e) != rotation(reverse(e)) for e in ev)
    assert all(contrast(reverse(e))[1] == {k: -v for k, v in contrast(e)[1].items()} for e in ev)
    assert all(sign(rotation(e)) == 1 for e in ev)
    frame_set = set(map(rotation, ev))
    assert len(frame_set) == 40
    depth = closure_depth(frame_set)
    generated = set(depth)
    assert len(generated) == 360
    depth_distribution = {d: list(depth.values()).count(d) for d in sorted(set(depth.values()))}
    assert depth_distribution == {0: 1, 1: 40, 2: 229, 3: 90}
    assert all(cycle_type(p)==(4,2) for p,d in depth.items() if d==3)
    assert generated == {p for p in permutations(AX) if sign(p) == 1}

    lifted = defaultdict(list)
    for e in ev:
        for visible in combinations(e, 2):
            lifted[frozenset(visible)].append(e)
    assert len(lifted) == 60
    assert all(len(x) == 16 for x in lifted.values())
    counts = {}
    for pair, es in lifted.items():
        fibers = defaultdict(int)
        for e in es:
            fibers[rotation(e)] += 1
        assert len(fibers) == 8
        assert set(fibers.values()) == {2}
        assert all(set(pair).issubset(set(e)) for e in es)
        counts[str(tuple(sorted(pair)))] = sorted(fibers.values())

    covariance = 0
    for perm in permutations(AX):
        pinv = invert(perm)
        for e in ev:
            e2 = relabel(e, perm)
            lhs = rotation(e2)
            rhs = compose(compose(perm, rotation(e)), pinv)
            assert lhs == rhs
            m2 = pass_ledger(e2)
            assert m2 == {image_by_permutation(k, perm): v for k,v in pass_ledger(e).items()}
            covariance += 1
    assert covariance == 720*320

    for support in combinations(AX, 3):
        gs = {rotation(e) for e in ev if {p[0] for p in e} == set(support)}
        assert len(gs) == 2 and len(closure(gs)) == 3

    return {
        "schema": "R761_TRIADIC_SIGNED_PORT_BRC_ROTATION_EXACT_V1",
        "candidate": "LOCAL_UNIT_EQUAL_QUANTUM_TRIADIC_EVENT_WITH_V29_PASS_BATCH_AND_S6_ROTATION_SKELETON",
        "population": "one chosen Cell anchor, six native signed axes, q=1, no arbitrary extra branch label choices",
        "typed_source": "three distinct nonzero signed force ports; cyclic branch identity and signed port labels retained",
        "verified": {
            "events": len(ev), "support_sets": 20, "signed_port_sets": 160,
            "orientations_per_signed_set": 2, "distinct_rotation_increments": len(frame_set),
            "reachable_frame_group": "A6", "reachable_frames": len(generated),
            "minimum_event_count_distribution": depth_distribution,
            "exact_max_minimum_event_count": max(depth.values()),
            "depth_three_cycle_type": "(4,2)",
            "odd_reachable_frames": sum(sign(g) < 0 for g in generated),
            "visible_signed_two_port_pairs": len(lifted),
            "full_triads_per_visible_pair": 16,
            "distinct_frame_values_per_pair": 8,
            "full_events_per_frame_per_pair": 2,
            "covariance_pairs_checked": covariance,
            "V29_PASS_occurrences_per_event": 3,
            "V29_scalar_and_portwise_contrast_after_atomic_batch": 0,
            "fixed_support_reachable_frame_group": "C3",
        },
        "observer_and_horizon": "full signed event vs two-visible-port source/support; frame-only futures are exact permutation composition at this anchor",
        "boundary": "candidate scheduler/bridge; V39 based-loop admissibility and native force event authorisation not established",
        "result": "PASS"
    }

if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
