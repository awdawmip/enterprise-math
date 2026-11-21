#!/usr/bin/env python3
"""Unit253: independent exact reverse-winding FIFO for the Unit245 directed-Port graph.
Original Unit245 immutable certificate:
f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json
This verifies CONDITIONAL graph minima, not actual native physical Port or C24 sensor execution.
"""
from collections import deque, Counter
import json

SITES = (0, 2, 4, 6, 8, 10)
ORIGINAL = (
    (30,38,36,38,38,46),
    (38,30,46,38,38,36),
    (32,36,32,48,38,32),
    (28,30,40,36,44,34),
    (30,28,34,44,36,40),
    (36,32,32,38,48,32),
)

def minimum_reverse(ingress, egress):
    adj = [[] for _ in range(13)]
    for u in range(12):
        adj[u].extend((((u + 1) % 12, 1), ((u - 1) % 12, -1)))
    adj[ingress].append((12, 0))
    adj[12].append((egress, 0))
    initial = (0, 2, 0, 0)
    target = (0, 2, 12, -12)
    queue = deque([(initial, 0)])
    seen = {initial}
    while queue:
        (a, b, wa, wb), depth = queue.popleft()
        if (a, b, wa, wb) == target:
            return depth, len(seen)
        if depth == 48:
            continue
        for nxt, dw in adj[a]:
            nw = wa + dw
            if nxt == b or abs(nw) > 48:
                continue
            state = (nxt, b, nw, wb)
            if state not in seen:
                seen.add(state)
                queue.append((state, depth + 1))
        for nxt, dw in adj[b]:
            nw = wb + dw
            if nxt == a or abs(nw) > 48:
                continue
            state = (a, nxt, wa, nw)
            if state not in seen:
                seen.add(state)
                queue.append((state, depth + 1))
    raise AssertionError(("unreachable reverse goal", ingress, egress))

def main():
    matrix, total = [], 0
    comparisons = 0
    for i, ingress in enumerate(SITES):
        row = []
        for j, egress in enumerate(SITES):
            cost, discoveries = minimum_reverse(ingress, egress)
            total += discoveries
            assert cost == ORIGINAL[j][i], (ingress, egress, cost, ORIGINAL[j][i])
            comparisons += 1
            row.append(cost)
        matrix.append(row)
    histogram = Counter(matrix[i][j] - ORIGINAL[i][j] for i in range(6) for j in range(6))
    assert sum(v for k, v in histogram.items() if k) == 24
    assert max(abs(k) for k in histogram) == 10
    assert histogram == Counter({-10:4, -8:4, -4:4, 0:12, 4:4, 8:4, 10:4})
    result = {
        "schema":"X6_TIME_UNIT253_REVERSE_WINDING_RECIPROCITY_EXACT_V1",
        "date":"2026-11-22",
        "task_id":"RS-X6-NATIVE-TIME-DYNAMICS",
        "frozen_p000":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "original_unit245_commit":"f56840285cafeb9f5767ea91e903e1f53808186f",
        "sites":list(SITES),
        "original_target_windings":[-12,12],
        "reverse_target_windings":[12,-12],
        "original_cost_matrix":[list(r) for r in ORIGINAL],
        "reverse_cost_matrix":matrix,
        "matrix_comparisons":comparisons,
        "visited_state_discoveries_total":total,
        "asymmetric_ordered_port_pairs":24,
        "max_absolute_gap":10,
        "cost_gap_histogram":{str(k):histogram[k] for k in sorted(histogram)},
        "failures":0,
        "status":"AUTHOR_PROVED / EXACT_INDEPENDENT_BFS_EXECUTED / NO_PHYSICAL_NATIVE_EXECUTION / UNREVIEWED / NOT_ADMITTED"
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__ == "__main__":
    main()
