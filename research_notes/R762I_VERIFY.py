#!/usr/bin/env python3
"""R762I: exact six-step signed X6 three-port loop enumeration.
Pure exact path combinatorics; no physical force, BRC propagation, V29/V39."""
import itertools
import json
from collections import Counter
AXES = range(3)

def path_from_word(word):
    state = [0, 0, 0]
    cells = [tuple(state)]
    for letter in word:
        axis = letter % 3
        state[axis] += 1 if letter < 3 else -1
        cells.append(tuple(state))
    return tuple(cells)

def signature(cells):
    if cells[-1] != (0,0,0):
        return None
    ports = [tuple(int(i == a) for i in AXES) for a in AXES]
    if any(cells.count(p) != 1 for p in ports):
        return None
    visits = [cells.index(p) for p in ports]
    order = tuple(sorted(AXES, key=lambda a: visits[a]))
    returns = (int(cells[2] == (0,0,0)), int(cells[4] == (0,0,0)))
    return tuple(visits), order, returns

def construct(order, returns):
    a,b,c = order
    s2 = (0,0,0) if returns[0] else tuple(int(i in (a,b)) for i in AXES)
    s4 = (0,0,0) if returns[1] else tuple(int(i in (b,c)) for i in AXES)
    u = lambda x: tuple(int(i == x) for i in AXES)
    return ((0,0,0),u(a),s2,u(b),s4,u(c),(0,0,0))

def edge_current(cells):
    result = Counter()
    for u,v in zip(cells,cells[1:]):
        diffs = [v[i]-u[i] for i in AXES]
        a = next(i for i,t in enumerate(diffs) if t)
        edge_start = u if diffs[a] == 1 else v
        result[(edge_start,a)] += diffs[a]
    return tuple(sorted((pos,axis,amp) for (pos,axis),amp in result.items() if amp))

valid = []
for w in itertools.permutations(range(6)):
    cells = path_from_word(w)
    sig = signature(cells)
    if sig is None:
        continue
    visits, order, returns = sig
    assert sorted(visits) == [1,3,5]
    assert construct(order, returns) == cells
    valid.append((w, cells, visits, order, returns, edge_current(cells)))

assert len(valid) == 24
counts = Counter((r[3], r[4]) for r in valid)
assert len(counts) == 24 and set(counts.values()) == {1}
counts_order = Counter(r[3] for r in valid)
counts_return = Counter(r[4] for r in valid)
assert set(counts_order.values()) == {4}
assert set(counts_return.values()) == {6}
assert set(counts_order) == set(itertools.permutations(AXES))
assert set(counts_return) == set(itertools.product((0,1),repeat=2))

def parity(order):
    return sum(order[i]>order[j] for i in AXES for j in AXES if i<j) % 2
chi_return = Counter((parity(r[3]),r[4]) for r in valid)
assert len(chi_return) == 8 and set(chi_return.values()) == {3}
assert len(set((r[5],r[3]) for r in valid)) == 24

for choice in itertools.combinations(range(6),3):
    for signs in itertools.product((-1,1),repeat=3):
        def embed(cell):
            z=[0]*6
            for local, global_axis in enumerate(choice):
                z[global_axis]=signs[local]*cell[local]
            return tuple(z)
        seen=set()
        for _,cells,visits,order,returns,_ in valid:
            trace=tuple(embed(x) for x in cells)
            assert trace[0]==trace[-1]==(0,)*6
            assert len(set(trace))>=4
            seen.add(trace)
        assert len(seen)==24

result = {
    "schema":"R762I_X6_TIMED_PORT_RETURN_CODE_V1",
    "status":"AUTHOR_SIDE_EXACT_COMBINATORICS_NOT_NATIVE_FORCE_LAW",
    "domain":"Each of 160 selected signed 3-port configurations, rooted six-step shortest X6 Cell paths",
    "all_balanced_words_per_configuration":720,
    "port_covering_shortest_paths_per_configuration":len(valid),
    "distinct_first_visit_orders":len(counts_order),
    "first_visit_step_indices":[1,3,5],
    "return_flag_pairs":4,
    "order_return_pair_fibers":dict(Counter(counts.values())),
    "first_visit_order_fibers":dict(Counter(counts_order.values())),
    "return_flag_fibers":dict(Counter(counts_return.values())),
    "chirality_return_fibers":dict(Counter(chi_return.values())),
    "joint_edge_current_and_order_injective":True,
    "full_trace_finite_minimal_fixed_width_bits":5,
    "conditional_given_order_return_repair_bits":2,
    "conditional_given_chirality_and_returns_order_repair_bits":2,
    "signed_port_configurations_verified":160,
    "native_triadic_force_event_admission":"UNTESTED",
    "V29_V39_and_BRC_physical_propagation":"NOT_EXECUTED"
}
print(json.dumps(result,indent=2,sort_keys=True))
