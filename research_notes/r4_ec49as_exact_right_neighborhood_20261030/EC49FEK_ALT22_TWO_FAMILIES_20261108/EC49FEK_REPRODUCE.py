"""EC49FEK exact finite exclusion of <=93 signed-native-X6 prefix edges.
Requires unchanged pinned EC49FEJ_SIEVE.py, EC49FEJ_CONSTRUCT.py,
and EC49FEJ_DEPTH_FILTER2.py from prior EC49FEJ archive.
Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from collections import Counter, defaultdict
from itertools import product
from EC49FEJ_SIEVE import high_keys, pool
from EC49FEJ_CONSTRUCT import native, prefixes
from EC49FEJ_DEPTH_FILTER2 import early_variants, cover
import json
import sys

EARLY = early_variants()
FREE = frozenset().union(*(prefixes(w) for ev in EARLY for w in ev))
assert len(EARLY) == 4 and len(FREE) == 54
assert {len(set().union(*(prefixes(w) for w in ev))) for ev in EARLY} == {42}

def check_inventory(K, high, cap=94):
    groups = []
    for h in range(4, 10):
        need = (16, 32) if h in high else (1, 2, 4, 8)
        av = defaultdict(set)
        for k in K:
            for w, signature in pool(h, k):
                if signature in need:
                    av[signature].add(native(w))
        if any(not av[signature] for signature in need):
            return {'status': 'infeasible', 'lower_bound': None, 'depth_covers': []}
        groups += [tuple(av[signature]) for signature in need]
    assert len(groups) == 16
    lower = 42
    depth_covers = []
    max_depth = max(map(len, (w for grp in groups for w in grp)))
    for d in range(1, max_depth + 1):
        active = [grp for grp in groups if min(map(len, grp)) >= d]
        if not active:
            continue
        masks = defaultdict(int)
        for i, grp in enumerate(active):
            for w in grp:
                masks[w[:d]] |= 1 << i
        free_at = {p for p in FREE if len(p) == d}
        free = 0
        for p in free_at:
            free |= masks.get(p, 0)
        missing = ((1 << len(active)) - 1) & ~free
        if missing:
            bits = [j for j in range(len(active)) if (missing >> j) & 1]
            opts = {sum(1 << i for i, j in enumerate(bits) if (mask >> j) & 1)
                    for p, mask in masks.items() if p not in free_at}
            m = cover(tuple(sorted(opts - {0})), (1 << len(bits)) - 1)
        else:
            m = 0
        depth_covers.append((d, m))
        lower += m
        if lower >= cap:
            break
    return {'status': 'excluded93' if lower >= 94 else 'unresolved',
            'lower_bound': lower, 'depth_covers': depth_covers}

def run(high, start=0, stop=None):
    choices = sorted(high - {3})
    hkeys = {h: high_keys(h) for h in choices}
    inventories = list(product(*(hkeys[h] for h in choices)))
    stop = min(len(inventories), len(inventories) if stop is None else stop)
    stats = Counter()
    rows = []
    for i in range(start, stop):
        K = ((3, 1, 1),) + inventories[i]
        result = check_inventory(K, high)
        stats[result['status']] += 1
        rows.append({'i': i, 'keys': K, **result})
    return {'high_horizons': sorted(high),
            'low_horizons': sorted(set(range(2, 10)) - high),
            'total_inventories': len(inventories), 'start': start, 'stop': stop,
            'tested': len(rows), 'stats': dict(stats), 'results': rows}

if __name__ == '__main__':
    tag = sys.argv[1] if len(sys.argv) > 1 else 'F8'
    high = {'F8': {3, 4, 6, 8, 9}, 'F5': {3, 4, 5, 6, 9}}[tag]
    st = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    ed = int(sys.argv[3]) if len(sys.argv) > 3 else None
    print(json.dumps(run(high, st, ed), separators=(',', ':')))
