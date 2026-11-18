#!/usr/bin/env python3
"""Exact pairwise no-ten certificate for two monotone named Set operations.
Auxiliary genuine-source six-cycle, slack 2, frozen pin
435e77af0d180eac32bd1f9c4c464bc4010b7551. Python standard library.
"""
from collections import Counter
from itertools import combinations
import json

K, N = 6, 1 << 6
FULL = (1 << N) - 1
q = [sum((r >> i & 1) * (r >> ((i + 1) % K) & 1) for i in range(K)) for r in range(N)]
G = [sum(1 << u for u in range(N) if u & ~r == 0 and q[r] - q[u] <= 2)
     for r in range(N)]
centres = tuple(r for r in range(N) if not any(r != z and G[r] & ~G[z] == 0
                                                for z in range(N)))
assert len(centres) == 22
ACTIONS = ((0, 1), (1, 1))
U = {i: [(u | (1 << i)) for u in range(N)] for i, _ in ACTIONS}
serves = [tuple(j for j, r in enumerate(centres) if G[r] >> u & 1)
          for u in range(N)]

# Every size-10 source cover; exclude any size-9 cover in the same recursion.
covers, fewer, calls = set(), set(), 0

def cover_search(chosen, mask):
    global calls
    calls += 1
    if mask == FULL:
        if len(chosen) == 10:
            covers.add(tuple(sorted(centres[j] for j in chosen)))
        else:
            fewer.add(tuple(sorted(centres[j] for j in chosen)))
        return
    if len(chosen) == 10:
        return
    u = min((x for x in range(N) if not (mask >> x & 1)),
            key=lambda x: sum(j not in chosen for j in serves[x]))
    for j in serves[u]:
        if j not in chosen:
            cover_search(chosen + (j,), mask | G[centres[j]])

cover_search((), 0)
assert len(covers) == 116 and not fewer

certificates = []
counts = Counter()
for C in sorted(covers):
    unique = {r: tuple(u for u in range(N) if (G[r] >> u & 1) and
                    sum(G[z] >> u & 1 for z in C) == 1) for r in C}
    # A state outputting centre r must initialize all its unique raw inputs.
    forced_pair = None
    for r in C:
        for i, _ in ACTIONS:
            for x, y in combinations(unique[r], 2):
                if not any((G[z] >> U[i][x] & 1) and
                           (G[z] >> U[i][y] & 1) for z in C):
                    forced_pair = {'centre': r, 'set_bit': i, 'unique_pair': [x, y]}
                    break
            if forced_pair:
                break
        if forced_pair:
            break
    if forced_pair:
        certificates.append({'centres': list(C), 'type': 'forced_pair',
                             'witness': forced_pair})
        counts['forced_pair'] += 1
        continue
    # State 36 = 0b100100. Any centre covering it has a conflicting
    # unique raw anchor under one of the two positive Set commands.
    rows = []
    for r in C:
        if not (G[r] >> 36 & 1):
            continue
        witness = next(({'centre': r, 'set_bit': i, 'unique_anchor': v}
                        for i, _ in ACTIONS for v in unique[r]
                        if not any((G[z] >> U[i][36] & 1) and
                                   (G[z] >> U[i][v] & 1) for z in C)), None)
        assert witness is not None, (C, r)
        rows.append(witness)
    assert rows
    certificates.append({'centres': list(C), 'type': 'raw36_obstruction',
                         'witnesses': rows})
    counts['raw36_obstruction'] += 1
assert counts == {'forced_pair': 101, 'raw36_obstruction': 15}
assert sum(len(row['witnesses']) for row in certificates
           if row['type'] == 'raw36_obstruction') == 40

# Independent ten-state controller for either single positive Set action.
R = (23, 29, 43, 46, 47, 53, 58, 59, 62, 63)
down = (0, 1, 2, 3, 3, 5, 6, 6, 8, 8)
up = (0, 1, 2, 4, 4, 5, 7, 7, 9, 9)
B = [G[r] for r in R]
while True:
    new = [sum(1 << u for u in range(N) if (B[j] >> u & 1) and
               (B[down[j]] >> (u & ~1) & 1) and
               (B[up[j]] >> (u | 1) & 1)) for j in range(10)]
    if new == B:
        break
    B = new
assert __import__('functools').reduce(int.__or__, B, 0) == FULL

# Eleven-state construction for both raising commands, using inherited
# source-labelled coherent cubes. All 16 tails x all four assignments checked.
witness = (((0, 1), (60, 61, 62, 63)), ((), (51,)), ((), (43,)),
           ((1,), (37, 39)), ((), (27,)), ((), (23,)), ((), (15,)))
assert sum(len(c) for _, c in witness) == 11
for tail in range(16):
    assert any(all((G[C[sum(((a >> i) & 1) << j for j, i in enumerate(S))]]
                    >> ((tail << 2) | a)) & 1 for a in range(4))
               for S, C in witness)

out = {'status': 'PASS_R5_TWO_RAISES_PAIRWISE_HORIZON_ONE',
       'science_pin': '435e77af0d180eac32bd1f9c4c464bc4010b7551',
       'model': 'genuine-source cyclic six-bit q, slack=2',
       'operations': ['Set_0(1)', 'Set_1(1)'],
       'number_of_raw_states': N,
       'nondominated_source_centres': len(centres),
       'minimum_static_centres': 10,
       'all_ten_centre_covers': len(covers),
       'size_nine_or_smaller_covers_found': len(fewer),
       'source_cover_search_nodes': calls,
       'forced_pair_certificates': counts['forced_pair'],
       'raw36_certificates': counts['raw36_obstruction'],
       'raw36_single_anchor_rows': 40,
       'single_positive_command_optimum': 10,
       'two_positive_commands_horizon_one_and_all_words_optimum': 11,
       'certificates': certificates,
       'review': 'NOT_REVIEWED'}
with open('EXACT_R5_TWO_RAISES_PAIRWISE_EVIDENCE.json', 'w', encoding='utf8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps({k: v for k, v in out.items() if k != 'certificates'}, sort_keys=True))
