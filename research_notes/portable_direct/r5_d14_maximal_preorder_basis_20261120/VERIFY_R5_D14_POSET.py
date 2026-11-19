#!/usr/bin/env python3
"""Recheck the 278 maximal-cost-aware-dominance components.
Place the following unchanged predecessor bundle files beside this program:
  EXACT_R5_ALL_101_BUDGETS.json, classes_1906.tsv,
  dominance_edges_1906.bin, CERTIFIED_52_CLASSES.csv,
  NEW_R5_D14_SEEDS.json.
These originate in EnterpriseMath_R5_D14_SixRoots_26388_20261120.zip.
The helper verifies finite order arithmetic; it does not resolve new f8 DP roots.
"""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

p = Path(__file__).resolve().parent
expected = json.loads((p / 'RESULT.json').read_text())
def sha(name):
    return hashlib.sha256((p / name).read_bytes()).hexdigest()

assert sha('EXACT_R5_ALL_101_BUDGETS.json') == expected['input_sha256']
assert sha('dominance_edges_1906.bin') == expected['predecessor_matrix_sha256']
assert sha('classes_1906.tsv') == expected['predecessor_classes_sha256']
classes = list(csv.DictReader((p / 'classes_1906.tsv').open(), delimiter='\t'))
before = list(csv.DictReader((p / 'CERTIFIED_52_CLASSES.csv').open()))
n = len(classes)
assert n == 1906 and len(before) == n
weight = [int(x['members']) for x in classes]
assert sum(weight) == 29646
matrix = (p / 'dominance_edges_1906.bin').read_bytes()
assert len(matrix) == n * n and sum(matrix) == 38127
assert all(x < 2 for x in matrix)
def e(i, j):
    return matrix[i*n+j]

covered = [int(x['certified']) == 1 for x in before]
assert sum(covered) == 1220
assert sum(weight[i] for i in range(n) if covered[i]) == 25896
refs = json.loads((p / 'NEW_R5_D14_SEEDS.json').read_text())['new_exact_references']
assert len(refs) == 6
for ref in refs:
    j = int(ref['class'])
    assert ref['v8'] == 8335
    assert (int(classes[j]['u']), int(classes[j]['v'])) == (ref['u'], ref['v'])
    fresh = [i for i in range(n) if not covered[i] and e(i,j)]
    assert len(fresh) == ref['classes_at_selection']
    assert sum(weight[i] for i in fresh) == ref['gain_at_selection']
    for i in fresh:
        covered[i] = True

U = [i for i in range(n) if not covered[i]]
q = len(U)
assert q == 641 and sum(weight[i] for i in U) == 3258
rows = [sum(1<<j for j,v in enumerate(U) if e(i,v)) for i in U]
assert sum(r.bit_count() for r in rows) == 2384
assert all((rows[i]>>i)&1 for i in range(q))
# Exact induced transitivity (using arbitrary-precision bitsets).
for i, row in enumerate(rows):
    todo = row
    while todo:
        bit = todo & -todo
        j = bit.bit_length() - 1
        assert rows[j] & ~row == 0
        todo -= bit
parent = list(range(q))
def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i
for i in range(q):
    for j in range(i+1,q):
        if ((rows[i]>>j)&1) and ((rows[j]>>i)&1):
            parent[find(j)] = find(i)
groups = defaultdict(list)
for i in range(q):
    groups[find(i)].append(i)
groups = list(groups.values())
maxima, minima = [], []
for group in groups:
    i = group[0]
    mask = sum(1<<j for j in group)
    if rows[i] & ~mask == 0:
        maxima.append(group)
    if not any((rows[j]>>i)&1 for j in range(q) if j not in group):
        minima.append(group)
reps = [U[g[0]] for g in maxima]
assert len(groups) == 468
assert Counter(map(len, groups)) == Counter({1:307, 2:154, 3:6, 8:1})
assert len(reps) == 278 and len(minima) == 133
assert all(any(e(i,j) for j in reps) for i in U)
assert all(sum(e(j,k) for k in reps) == 1 for j in reps)
assert Counter(int(classes[r]['actions']) for r in reps) == Counter({7:166,8:3,9:109})
assert reps == expected['maximal_representative_class_ids']
print('PASS', 'unresolved',q,'SCC',len(groups),
      'maximal',len(reps),'minimal',len(minima),
      'maximal_action_counts',dict(Counter(int(classes[r]['actions']) for r in reps)))
