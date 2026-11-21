"""Independently certify every typed Bellman inequality and cost-window minimum."""
from pathlib import Path
from collections import defaultdict, deque
import argparse, hashlib, json, time

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--catalog', type=Path, required=True)
p.add_argument('--table', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
start = time.time()
typed = defaultdict(dict)
lines = a.catalog.read_text().splitlines()
assert int(lines[0]) == len(lines) - 1
for line in lines[1:]:
    s, e, c, d = map(int, line.split())
    assert c not in typed[s, e]
    typed[s, e][c] = d

lines = a.table.read_text().splitlines()
n, cap, min_e, budget, lower, q = map(int, lines[0].split())
counts, radix, floors = [list(map(int, line.split())) for line in lines[1:4]]
embedded = list(map(int, lines[4].split()))
assert len(counts) == len(radix) == len(floors) == 14
assert q > 0 and 0 <= lower <= budget
multiplier = 1
for s in range(1, 14):
    assert radix[s] == multiplier
    multiplier *= counts[s] + 1
    if counts[s]:
        assert floors[s] == min(typed[s, 0])
assert multiplier == n
assert cap == budget - min_e - sum(c * f for c, f in zip(counts, floors))
table = [[None] * (cap + 1) for _ in range(n)]
window = [[None] * (cap + 1) for _ in range(n)]
for line in lines[5:]:
    state, extra, d, w = map(int, line.split())
    assert 0 <= state < n and 0 <= extra <= cap
    assert table[state][extra] is None and d >= -1
    table[state][extra] = d
    window[state][extra] = w
assert all(all(x is not None for x in row) for row in table)

# Embedded base: the six-large-class theorem forces one outer deletion.
force = sum(s >= 12 for s in embedded) == 6
base = [0] + [-1] * cap
embedded_min = 0
embedded_types = []
for s in embedded:
    e = 2 if s == 12 and force else 1
    if e == 2:
        force = False
    embedded_types.append([s, e])
    cmin = min(typed[s, e])
    embedded_min += cmin
    nxt = [-1] * (cap + 1)
    for c, d in typed[s, e].items():
        spent = c - cmin
        for x in range(cap - spent + 1):
            if base[x] >= 0:
                nxt[x + spent] = max(nxt[x + spent], base[x] + d)
    base = nxt
assert not force and embedded_min == min_e and table[0] == base

# Every possible final proper type is checked, not merely the predecessor
# chosen by the generating program. These inequalities inductively certify
# all reachable states, including the claim that negative cells are unreachable.
inequalities = 0
for state in range(1, n):
    for s in range(1, 14):
        count = (state // radix[s]) % (counts[s] + 1)
        if not count:
            continue
        previous = table[state - radix[s]]
        for c, d in typed[s, 0].items():
            spent = c - floors[s]
            for x in range(cap - spent + 1):
                if previous[x] >= 0:
                    assert table[state][x + spent] >= previous[x] + d
                    inequalities += 1

# Check the sliding minimum at every query coordinate, including coordinates
# where the exact-cost spectrum is empty but the permitted window is not.
queries = 0
width = budget - lower
inf = 1_000_000_000
for state in range(n):
    queue = deque()
    score = lambda x: q * x - table[state][x]
    for x in range(cap + 1):
        while queue and queue[0] < x - width:
            queue.popleft()
        if table[state][x] >= 0:
            while queue and score(queue[-1]) >= score(x):
                queue.pop()
            queue.append(x)
        expected = score(queue[0]) if queue else inf
        assert window[state][x] == expected
        queries += 1

out = {
    'verified': True,
    'remaining_count_states': n,
    'extra_cost_cap': cap,
    'embedded_types': embedded_types,
    'total_cost_window': [lower, budget],
    'q': q,
    'bellman_inequalities': inequalities,
    'cost_window_queries_checked': queries,
    'table_sha256': hashlib.sha256(a.table.read_bytes()).hexdigest(),
    'catalog_sha256': hashlib.sha256(a.catalog.read_bytes()).hexdigest(),
    'elapsed_seconds': time.time() - start,
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, indent=2), flush=True)
