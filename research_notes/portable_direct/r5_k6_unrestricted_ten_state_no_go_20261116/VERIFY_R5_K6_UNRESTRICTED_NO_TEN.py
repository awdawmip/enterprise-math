#!/usr/bin/env python3
"""Exact exhaustive no-10-state certificate, source-labelled k=6,J={0,1},slack=2.
Only Python standard library. Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
from itertools import product

K, N, BUDGET = 6, 64, 10
FULL = (1 << N) - 1
q = [sum(((r >> i) & 1) * ((r >> ((i + 1) % K)) & 1)
         for i in range(K)) for r in range(N)]
def eligible(r, u):
    return (u & ~r) == 0 and 0 <= q[r] - q[u] <= 2
G = [sum(1 << u for u in range(N) if eligible(r, u)) for r in range(N)]
assert len(set(G)) == N, 'Equal feasibility masks require representative deduplication'
CENTERS = tuple(r for r in range(N) if not any(
    r != z and G[r] & ~G[z] == 0 for z in range(N)))
assert len(CENTERS) == 22
NEXT = tuple(tuple((u & ~(1 << i)) | (b << i) for u in range(N))
             for i, b in ((0, 0), (0, 1), (1, 0), (1, 1)))
SERVE = tuple(tuple(j for j, r in enumerate(CENTERS) if (G[r] >> u) & 1)
              for u in range(N))
ALL_COVERS = set()
CALLS = 0
MIN_COVER = N
def search(selected, mask):
    global CALLS, MIN_COVER
    CALLS += 1
    if mask == FULL:
        MIN_COVER = min(MIN_COVER, len(selected))
        ALL_COVERS.add(tuple(sorted(CENTERS[j] for j in selected)))
        return
    if len(selected) >= BUDGET:
        return
    missing = (u for u in range(N) if not ((mask >> u) & 1))
    x = min(missing, key=lambda u: sum(j not in selected for j in SERVE[u]))
    for j in SERVE[x]:
        if j not in selected:
            search(selected + (j,), mask | G[CENTERS[j]])
search((), 0)
assert MIN_COVER == BUDGET and len(ALL_COVERS) == 116
assert all(len(c) == BUDGET for c in ALL_COVERS)

def forced_targets(centers):
    """Necessary propagation of uniquely served initialized raw snapshots."""
    forced = [set() for _ in centers]
    for u in range(N):
        js = [j for j, r in enumerate(centers) if (G[r] >> u) & 1]
        assert js
        if len(js) == 1:
            forced[js[0]].add(u)
    while True:
        choices = [[tuple(j2 for j2, r2 in enumerate(centers)
                        if all((G[r2] >> NEXT[op][u]) & 1 for u in forced[j]))
                    for op in range(4)] for j in range(BUDGET)]
        if any(not ch for row in choices for ch in row):
            return None
        changed = False
        for j in range(BUDGET):
            for op in range(4):
                if len(choices[j][op]) == 1:
                    target = choices[j][op][0]
                    forward = {NEXT[op][u] for u in forced[j]}
                    if not forward.issubset(forced[target]):
                        forced[target].update(forward)
                        changed = True
        if not changed:
            return choices

def viability_count(centers, transitions):
    """Greatest postfixed output-correct raw-state relation under all four operations."""
    beliefs = [G[r] for r in centers]
    for _ in range(N * BUDGET + 1):
        nxt = []
        for j in range(BUDGET):
            can = beliefs[j]
            for op in range(4):
                dest = beliefs[transitions[j][op]]
                pre = sum(1 << u for u in range(N) if (dest >> NEXT[op][u]) & 1)
                can &= pre
            nxt.append(can)
        if nxt == beliefs:
            union = 0
            for m in nxt:
                union |= m
            return union.bit_count()
        beliefs = nxt
    raise AssertionError('Finite decreasing fixpoint did not stabilize')

surviving = []
rejected_local = 0
checked_transition_tables = 0
max_coverable = 0
per_family = []
for centers in sorted(ALL_COVERS):
    choices = forced_targets(centers)
    if choices is None:
        rejected_local += 1
        continue
    unknown = [(j, op, choices[j][op]) for j in range(BUDGET)
               for op in range(4) if len(choices[j][op]) > 1]
    assert all(len(ch) == 2 for _, _, ch in unknown)
    base = [[ch[0] for ch in row] for row in choices]
    family_best = 0
    for opts in product(*(entry[2] for entry in unknown)):
        table = [row[:] for row in base]
        for (j, op, _), dest in zip(unknown, opts):
            table[j][op] = dest
        covered = viability_count(centers, table)
        family_best = max(family_best, covered)
        checked_transition_tables += 1
    assert family_best < N
    max_coverable = max(max_coverable, family_best)
    surviving.append(centers)
    per_family.append({'centers': centers, 'undetermined_edges': len(unknown),
                       'checked_tables': 1 << len(unknown),
                       'maximum_viable_raw_snapshots': family_best})
assert rejected_local == 111 and len(surviving) == 5
assert checked_transition_tables == 328
assert max_coverable == 52

# Independently recheck the prior 11-state coherent witness by output labels.
WITNESS = (
    ((0, 1), (60, 61, 62, 63)),
    ((), (51,)), ((), (43,)), ((1,), (37, 39)),
    ((), (27,)), ((), (23,)), ((), (15,)),
)
assert sum(len(centers) for _, centers in WITNESS) == 11
witness_covered_tails = 0
for t in range(16):
    for S, centers in WITNESS:
        if all(eligible(centers[sum(((a >> i) & 1) << h for h, i in enumerate(S))],
                        (t << 2) | a) for a in range(4)):
            witness_covered_tails |= 1 << t
assert witness_covered_tails == (1 << 16) - 1

out = {
    'status': 'PASS_R5_K6_UNRESTRICTED_TEN_STATE_NO_GO',
    'science_pin': '435e77af0d180eac32bd1f9c4c464bc4010b7551',
    'scope': 'genuine-source canonical ring k=6, slack 2, named Set on bits 0 and 1, arbitrary deterministic Moore internal updates',
    'centres_total': N, 'undominated_centres': list(CENTERS),
    'static_minimum': MIN_COVER, 'static_minimal_ten_centre_covers': len(ALL_COVERS),
    'cover_search_calls': CALLS, 'forced_propagation_rejections': rejected_local,
    'remaining_centre_covers': len(surviving),
    'remaining_transition_tables_tested': checked_transition_tables,
    'maximum_viable_raw_snapshots_over_remaining_tables': max_coverable,
    'remaining_families': per_family,
    'unrestricted_minimum': 11,
    'eleven_state_witness_tail_coverage': witness_covered_tails,
    'eleven_state_witness_check': 'PASS_ALL_16_TAILS_ALL_FOUR_ASSIGNMENTS',
    'upper_bound_source': 'R5_TWO_CONTROL_CUBE_COVER_THEOREM.md (explicit 11-state controller)',
    'review': 'NOT_REVIEWED',
}
print(json.dumps(out, indent=2, sort_keys=True))

