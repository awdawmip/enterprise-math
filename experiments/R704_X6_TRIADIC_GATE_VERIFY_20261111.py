#!/usr/bin/env python3
"""R704 exhaustive signed-X6 three-distinct-axis candidate Port audit; stdlib only."""
from itertools import combinations, permutations, product
from collections import defaultdict, Counter
import json

D = 6
paths = []
for axes in combinations(range(D), 3):
    for signs in product((-1, 1), repeat=3):
        sign = dict(zip(axes, signs))
        for order in permutations(axes):
            z = (0,) * D
            word, ports = [], []
            for i in order:
                s = sign[i]
                word.append((i, s))
                ports.append((z, i, s))
                q = list(z)
                q[i] += s
                z = tuple(q)
            paths.append((tuple(word), tuple(ports), z))
assert len(paths) == 960

by_port = defaultdict(set)
by_end = defaultdict(set)
by_step = [set(), set(), set()]
for k, (word, gates, endpoint) in enumerate(paths):
    by_end[endpoint].add(k)
    assert sum(abs(v) for v in endpoint) == 3
    assert sum(v*v for v in endpoint) == 3
    assert endpoint != (0,) * D
    for step, gate in enumerate(gates):
        by_port[gate].add(k)
        by_step[step].add(gate)
assert len(by_end) == 160 and {len(v) for v in by_end.values()} == {6}
assert list(map(len, by_step)) == [12, 120, 480]
assert len(by_port) == 612
for gates, usage in zip(by_step, (80, 8, 2)):
    assert {len(by_port[p]) for p in gates} == {usage}
assert len({frozenset(v) for v in by_port.values()}) == 612

terminal_blocks = [by_port[p] for p in by_step[2]]
assert sum(map(len, terminal_blocks)) == 960
assert len(set().union(*terminal_blocks)) == 960
endpoint_fault_signatures = defaultdict(list)
for port in by_step[2]:
    lost = by_port[port]
    hist = Counter(paths[k][2] for k in lost)
    assert len(hist) == 1 and list(hist.values()) == [2]
    endpoint_fault_signatures[tuple(sorted(hist.items()))].append(port)
assert len(endpoint_fault_signatures) == 160
assert {len(v) for v in endpoint_fault_signatures.values()} == {3}
for end, sources in by_end.items():
    blocks = [by_port[p] for p in by_step[2] if by_port[p] <= sources]
    assert len(blocks) == 3
    assert sum(map(len, blocks)) == 6
    assert len(set().union(*blocks)) == 6

evidence = {
  "marker": "R704_X6_SIGNED_TRIADIC_PORT_INCIDENCE_EXACT_PASS",
  "frozen_science_pin": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
  "paths": 960, "endpoints": 160, "paths_per_endpoint": 6,
  "ports_by_step": [12,120,480], "uses_by_step": [80,8,2],
  "total_ports":612, "single_fault_labeled_signatures":612,
  "terminal_fault_endpoint_signatures":160, "terminal_endpoint_ambiguity":3,
  "terminal_pair_states": "2^480", "terminal_pair_state_bits":480,
  "endpoint_hist_states": "4^160=2^320", "endpoint_hist_state_bits":320,
  "valid_endpoint_source_counts":[0,2,4,6], "native_three_step_returns":0,
  "scope":"candidate static Boolean directed Port gates on signed X6 3-axis paths"
}
with open("R704_X6_TRIADIC_GATE_EVIDENCE_20261111.json", "w", encoding="utf-8") as f:
    json.dump(evidence, f, indent=2, sort_keys=True)
print(evidence["marker"], len(paths), len(by_end), len(by_port), len(endpoint_fault_signatures))
