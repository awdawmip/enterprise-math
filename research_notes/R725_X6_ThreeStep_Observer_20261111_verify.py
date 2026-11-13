#!/usr/bin/env python3
"""R725: exact X6 three-step signed Cell path/observer combinatorics.
Pure integer source/coordinate combinatorics; not native force propagation.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
import json

N = 6
TRIPLES = tuple(combinations(range(N), 3))
STEPS = tuple((a, s) for a in range(N) for s in (-1, 1))
ZERO = (0,) * N

def inc(v, x):
    a, s = x
    w = list(v)
    w[a] += s
    return tuple(w)

def add(v, w):
    return tuple(x + y for x, y in zip(v, w))

def path_net(path):
    v = ZERO
    for x in path:
        v = inc(v, x)
    return v

def observer(v):
    return sum(1 << i for i, t in enumerate(TRIPLES)
               if len({v[a] for a in t}) > 1)

def can3(z, t):
    x = [z[a] for a in t]
    m = min(x)
    return tuple(v-m for v in x)

def groups(items, fn):
    out = defaultdict(list)
    for v in items:
        out[fn(v)].append(v)
    return out

def hist(g):
    return dict(sorted(Counter(map(len, g.values())).items()))

paths = tuple(product(STEPS, repeat=3))
assert len(paths) == 1728
states = []
for p in paths:
    v = ZERO
    trace = []
    for x in p:
        v = inc(v, x)
        trace.append(observer(v))
    states.append((p, v, tuple(trace)))

terminal = groups(states, lambda x: x[2][-1])
traces = groups(states, lambda x: x[2])
nets = tuple(sorted({x[1] for x in states}))
by_net = groups(states, lambda x: x[1])
net_terminal = groups(nets, observer)
assert len(terminal) == 51 and hist(terminal) == {24:25, 36:20, 68:6}
assert len(traces) == 402 and hist(traces) == {2:120, 4:132, 6:120, 8:30}
assert len(nets) == 304 and hist(net_terminal) == {4:16, 6:20, 8:15}
assert hist(by_net) == {1:12, 3:120, 6:160, 33:12}
assert dict(sorted(Counter(x.bit_count() for x in terminal).items())) == {
    10:6, 16:15, 18:10, 19:20
}

# Independently verify min-normalized can3 on every path prefix.
for z in (ZERO, (-3,2,1,-4,0,5), (7,-6,3,8,-9,4)):
    for p, _, trace in states:
        v = ZERO
        for step, mask in zip(p, trace):
            v = inc(v, step)
            direct = sum(1 << j for j, t in enumerate(TRIPLES)
                         if can3(z,t) != can3(add(z,v),t))
            assert mask == direct

# S6-equivariance of the triple-observer identity, all 304 nets.
TINDEX = {t:i for i,t in enumerate(TRIPLES)}
for perm in permutations(range(N)):
    moved = [TINDEX[tuple(sorted(perm[a] for a in t))] for t in TRIPLES]
    for v in nets:
        w = [0]*N
        for a,x in enumerate(v):
            w[perm[a]] = x
        o = observer(v)
        transported = sum(1 << moved[i] for i in range(len(TRIPLES))
                          if o & (1<<i))
        assert observer(w) == transported

# All appended signed step displacements at horizons 0,1,2,3.
Q = {ZERO}
delta = {ZERO}
future = {}
for h in range(4):
    if h:
        delta = {inc(q, x) for q in delta for x in STEPS}
        Q |= delta
    qlist = tuple(sorted(Q))
    f = groups(nets, lambda v: tuple(observer(add(v,q)) for q in qlist))
    future[h] = {
        "continuation_displacements":len(Q),
        "signature_classes":len(f),
        "fiber_multiplicities":hist(f)
    }
    if h == 3:
        h3_fibers = f
assert [future[h]["signature_classes"] for h in range(4)] == [51,218,278,284]
assert [future[h]["continuation_displacements"] for h in range(4)] == [1,13,85,377]
assert future[0]["fiber_multiplicities"] == {4:16, 6:20, 8:15}
assert future[1]["fiber_multiplicities"] == {1:132, 2:86}
assert future[2]["fiber_multiplicities"] == {1:252, 2:26}
assert future[3]["fiber_multiplicities"] == {1:264, 2:20}

# Complete future-safe quotient is the diagonal-translation quotient.
diagonal = groups(nets, lambda v: tuple(v[i]-v[0] for i in range(1,N)))
assert len(diagonal) == 284 and hist(diagonal) == {1:264, 2:20}
assert sorted(sorted(g) for g in diagonal.values()) == (
    sorted(sorted(g) for g in h3_fibers.values()))

# Horizon 2 cannot distinguish +3e0 from -3e0, but horizon 3 can.
vp = (3,0,0,0,0,0)
vm = (-3,0,0,0,0,0)
for q in {ZERO} | {path_net(p) for k in (1,2) for p in product(STEPS,repeat=k)}:
    assert observer(add(vp,q)) == observer(add(vm,q))
q = (-3,0,0,0,0,0)
assert observer(add(vp,q)) != observer(add(vm,q))

result = {
    "schema":"ENTERPRISE_MATH_R725_X6_THREE_STEP_OBSERVER_V1",
    "task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
    "frozen_science_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "model":"ordered_signed_native_cell_coordinate_paths_not_force_closure",
    "axes":N, "primitive_step_choices":len(STEPS),
    "ordered_paths":len(paths),
    "terminal_masks":len(terminal),
    "terminal_path_fibers":hist(terminal),
    "terminal_mask_weights":dict(sorted(Counter(x.bit_count() for x in terminal).items())),
    "prefix_trace_classes":len(traces),
    "prefix_trace_path_fibers":hist(traces),
    "distinct_net_vectors":len(nets),
    "path_fibers_by_net":hist(by_net),
    "net_fibers_by_terminal":hist(net_terminal),
    "permanent_diagonal_quotient_classes":len(diagonal),
    "permanent_diagonal_pairs":20,
    "future_horizons":future,
    "full_path_bits_from_terminal":7,
    "full_path_bits_from_prefix_trace":3,
    "future_safe_net_bits_from_terminal":3,
    "sharp_future_horizon_for_diagonal_quotient":3,
    "initial_cells_tested":3, "axis_permutations_tested":720,
    "result":"R725_X6_THREE_STEP_OBSERVER_EXACT_PASS"
}
out = Path(__file__).with_name("R725_X6_ThreeStep_Observer_20261111_evidence.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+"\n",
               encoding="utf-8")
print(result["result"])
