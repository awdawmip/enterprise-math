#!/usr/bin/env python3
"""R284FW: exact q=2 barrier certificates using the existing R284FV flow oracle.

The separate mathematical note proves that these certificates lift to every q>=2.
"""
from itertools import product
import R284FV_prefix_count_lattice as prior


def families(q):
    a, b = 2*q+5, 2*q+3
    return [
        (0,0,0,0,a,b,0),
        (0,0,0,0,a,b,1),
        (0,0,0,0,a,b+1,0),
        (0,0,0,0,a+1,b,0),
        (0,0,0,1,a-1,b,1),
        (0,0,0,1,a,b,0),
        (0,0,1,0,a-1,b,1),
        (0,0,1,0,a,b,0),
        (0,1,0,0,a-1,b,1),
        (0,1,0,0,a,b,0),
        (1,0,0,0,a,b,0),
    ]


def barrier_states(idx, x):
    # Counts of attempted updates on edge 1->2, keyed by changed column type.
    types = tuple(p for p in range(1,8)
                  if x[p-1] and prior.PHASE[p][1] != prior.PHASE[p][2])
    if idx in (1,3):
        base = [(4,0)] + [(a,1) for a in range(4)]
    elif idx == 2:
        base = [(3,0),(3,1)] + [(a,2) for a in range(3)]
    else:
        base = [(3,0)] + [(a,1) for a in range(3)]
    extra = next((p for p in types if p not in (5,6)), None)
    if extra is None:
        return types, [dict(zip((5,6), t)) for t in base]
    return types, [dict(zip((extra,5,6), (c,a,b)))
                   for c in range(2) for a,b in base]


def third_phase_witness(x, attempted, q):
    prior.Q = q
    types = tuple(attempted)
    prefix = tuple(attempted[p] for p in types)
    for miss in product(*(range(min(q, v)+1) for v in prefix)):
        if sum(miss) > q:
            continue
        succ = {p:v-m for p,v,m in zip(types,prefix,miss)}
        for third in (0,3):
            d = prior.prefix_distance(x,1,third,2,succ)
            if d <= 2:     # two one-flip read balls intersect
                return third, tuple(miss), d
    return None


def verify_barrier_cut(types, barriers, x):
    # From zero, every possible count-lattice path to its full-update endpoint
    # must intersect a forbidden prefix before crossing the finite test box.
    bad = {tuple(t.get(p,0) for p in types) for t in barriers}
    seen = {tuple(0 for _ in types)}
    todo = list(seen)
    while todo:
        t = todo.pop()
        for i,p in enumerate(types):
            nxt = t[:i] + (t[i]+1,) + t[i+1:]
            if nxt[i] > x[p-1]:
                continue
            if nxt in bad:
                continue
            assert nxt[types.index(5)] < 5 and nxt[types.index(6)] < 3
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return len(seen)


def main():
    for q in (2,3,7,13):
        counts = []
        for idx,x in enumerate(families(q)):
            types,barriers = barrier_states(idx,x)
            assert all(third_phase_witness(x,t,q) is not None for t in barriers), (q,idx)
            assert max(t.get(5,0) for t in barriers) < x[4]
            assert max(t.get(6,0) for t in barriers) < x[5]
            reachable = verify_barrier_cut(types,barriers,x)
            counts.append((len(barriers),reachable))
        print("q=",q,"families=",len(counts),
              "barriers=",sum(a for a,_ in counts),
              "reachable_without_barrier=",sum(b for _,b in counts),"PASS")
    assert sum(len(barrier_states(i,x)[1]) for i,x in enumerate(families(2))) == 59


if __name__ == "__main__":
    main()
