#!/usr/bin/env python3
"""Solver-free exact integer BRC prefix charging certificate.
Frozen input: nine-state signed-X6 native paths, 178850 words, 94 raw keys,
24 labelled demands; certificate applies to six-key sets FKQ indices 4..8.
"""
import collections, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE/'EC49FGW_RADIUS5_SCREEN.py'
if not SRC.exists():
    SRC = HERE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'/'EC49FGW_RADIUS5_SCREEN.py'
assert SRC.exists(), f'Frozen BRC generator not found: {SRC}'
sys.path.insert(0, str(SRC.parent))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key
assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
K4 = {(2,1,1), (3,0,1), (3,1,1), (4,2,1)}
EXTRAS = {
    4: ((6,4,1),(6,6,1)),
    5: ((6,4,1),(7,5,1)),
    6: ((6,4,1),(7,6,1)),
    7: ((6,4,1),(8,4,1)),
    8: ((6,4,1),(8,5,1)),
}
# Weights in ascending (path window h, terminal signature) demand order.
LABEL_WEIGHTS = (6,6,2,2,4,4,4,4,3,3,7,7,7,7,3,4,3,4,3,3,3,3,4,4)
assert sum(LABEL_WEIGHTS) == 100

def main():
    relevant = K4 | set().union(*(set(x) for x in EXTRAS.values()))
    bykey = collections.defaultdict(list)
    allkeys, labels, nwords = set(), set(), 0
    for label, word in all_words():
        nwords += 1
        key = raw_key(word)
        allkeys.add(key)
        labels.add(label)
        if key in relevant:
            bykey[key].append((label, pref(word)))
    labels = sorted(labels)
    assert nwords == 178850 and len(allkeys) == 94 and len(labels) == 24
    weights = dict(zip(labels, LABEL_WEIGHTS))
    for idx, extras in sorted(EXTRAS.items()):
        words = [(lab, ps) for k in K4 | set(extras) for lab, ps in bykey[k]]
        assert {lab for lab, _ in words} == set(labels)
        nodes = sorted({p for lab, ps in words for p in ps}, key=lambda p: (len(p),p))
        index = {p:j for j,p in enumerate(nodes)}
        parent = [index.get(p[:-1], -1) for p in nodes]
        terminals = collections.defaultdict(set)
        for lab, ps in words:
            terminals[lab].add(index[ps[-1]])
        charge = [0] * len(nodes)
        for lab, js in terminals.items():
            for j in js:
                charge[j] += weights[lab]
        child_flow = [0] * len(nodes)
        flow = [0] * len(nodes)
        root_margin = []
        for j in range(len(nodes)-1, -1, -1):
            excess = charge[j] + child_flow[j] - 1
            if parent[j] >= 0:
                flow[j] = max(0, excess)
                child_flow[parent[j]] += flow[j]
            else:
                root_margin.append(-excess)
                assert excess <= 0, (idx, 'root violated', j, excess)
        print('CERTIFIED', idx, 'words', len(words), 'nodes', len(nodes),
              'labels', len(labels), 'weighted_lower_bound', sum(weights.values()),
              'nonzero_flows', sum(z > 0 for z in flow),
              'min_root_margin', min(root_margin), flush=True)
    print('EC49FKR_ALL_FIVE_100_PREFIX_LOWER_BOUND_PASS', flush=True)

if __name__ == '__main__':
    main()
