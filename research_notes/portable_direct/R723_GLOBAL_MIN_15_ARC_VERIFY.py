"""R723 exact global minimum arc count for five-axis rooted V17 CNB S3 carriers.

Independent finite certificate for global lower bound 15, plus explicit 15-arc
all-length positive carrier. Python standard library, exact integers/sets only.
Execute: python R723_GLOBAL_MIN_15_ARC_VERIFY.py > R723_GLOBAL_MIN_15_ARC_RESULTS.json
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
import json

ROOT = '012'
VERTICES = tuple(''.join(x) for x in combinations('01234', 3))
ARCS = tuple((a, b) for a in VERTICES for b in VERTICES
             if len(set(a) & set(b)) == 2)
ARC_IDS = {e: i for i, e in enumerate(ARCS)}
FRAMES = tuple(sorted(''.join(p) for p in permutations(ROOT)))
NEIGHBORS = {a: tuple(b for u, b in ARCS if u == a) for a in VERTICES}
BASE_TEXT = '''012>024 012>123 012>124 013>012 013>023
023>012 023>013 024>023 024>124 123>013
123>023 123>134 124>123 124>134 134>013'''
BASE = frozenset(tuple(x.split('>')) for x in BASE_TEXT.split())
assert len(VERTICES) == 10 and len(ARCS) == 60 and len(FRAMES) == 6
assert len(BASE) == 15 and BASE <= set(ARCS)

def advance(frame, destination):
    outgoing = [x for x in frame if x not in destination]
    incoming = [x for x in destination if x not in frame]
    assert len(outgoing) == len(incoming) == 1
    return frame.replace(outgoing[0], incoming[0])

def path_catalog(length):
    """Exhaustively enumerate V17 frames of all rooted length-m CNB positive paths."""
    catalog = defaultdict(set)
    counts = Counter()
    def visit(previous, current, first, frame, depth, used):
        if depth == length:
            if current == ROOT and previous != first:
                catalog[frame].add(used)
                counts[frame] += 1
            return
        for nxt in NEIGHBORS[current]:
            if nxt != previous:
                visit(current, nxt, nxt if first is None else first,
                      advance(frame, nxt), depth+1,
                      used | (1 << ARC_IDS[(current, nxt)]))
    visit(None, ROOT, None, ROOT, 0, 0)
    assert set(catalog) == set(FRAMES)
    return {f: tuple(sorted(catalog[f])) for f in FRAMES}, dict(counts)

CATALOGS = {m: path_catalog(m) for m in (4, 5)}
GROUPS = tuple((m, f, CATALOGS[m][0][f]) for m in (4, 5) for f in FRAMES)


def independent_global_exclusion(budget=14, pair_prune=False):
    """Exact exhaustive search over path witnesses, not all 60-choose-14 networks.

    Every feasible E has one witness path mask for each of the 12 groups.
    At an unsatisfied group we must add (at least) some complete witness path.
    Every possible witness is branched on; the 14-arc budget prunes. All
    visited sets have the same remaining budget, allowing memoization on M.
    """
    visited = set()
    stats = Counter()
    def search(mask):
        stats['calls'] += 1
        if mask in visited:
            stats['memo_hits'] += 1
            return None
        visited.add(mask)
        budget_left = budget - mask.bit_count()
        if budget_left < 0:
            stats['budget_prunes'] += 1
            return None
        missing = []
        best = None
        for gi, (length, frame, paths) in enumerate(GROUPS):
            if any((p & mask) == p for p in paths):
                continue
            missing.append(gi)
            available = [(p & ~mask).bit_count() for p in paths]
            feasible = sum(c <= budget_left for c in available)
            if feasible == 0:
                stats['single_group_prunes'] += 1
                return None
            key = (feasible, -min(available), gi)
            if best is None or key < best[0]:
                best = (key, gi)
        if best is None:
            stats['solutions'] += 1
            return mask
        if pair_prune and budget_left <= 5:
            for j, gi in enumerate(missing):
                for gj in missing[:j]:
                    if all(((p | q) & ~mask).bit_count() > budget_left
                           for p in GROUPS[gi][2] for q in GROUPS[gj][2]):
                        stats['pair_prunes'] += 1
                        return None
        gi = best[1]
        additions = set()
        for path in GROUPS[gi][2]:
            extended = mask | path
            if extended.bit_count() <= budget:
                additions.add(extended)
        for extended in sorted(additions, key=lambda x: (x.bit_count(), x)):
            ans = search(extended)
            if ans is not None:
                return ans
        stats['exhausted_nodes'] += 1
        return None
    winner = search(0)
    return winner, {'calls': stats['calls'], 'unique_visited': len(visited),
                    'single_group_prunes': stats['single_group_prunes'],
                    'pair_prunes': stats['pair_prunes'],
                    'memo_hits': stats['memo_hits'],
                    'exhausted_nodes': stats['exhausted_nodes']}


def typed_support_and_fixed_point(edges, max_length=11):
    outgoing = {a: tuple(b for u, b in edges if u == a) for a in VERTICES}
    states = {(ROOT, nxt, advance(ROOT, nxt), nxt) for nxt in outgoing[ROOT]}
    data = {'D_1': len(states)}
    exact_sets = {1: states}
    all_support = {}
    for m in range(2, max_length + 1):
        next_states = set()
        for prev, cur, frame, first in states:
            for nxt in outgoing[cur]:
                if nxt != prev:
                    next_states.add((cur, nxt, advance(frame, nxt), first))
        states = next_states
        exact_sets[m] = states
        data[f'D_{m}'] = len(states)
        if m >= 4:
            support = {frame for prev, cur, frame, first in states
                       if cur == ROOT and prev != first}
            all_support[m] = sorted(support)
            assert support == set(FRAMES), (m, support)
    assert exact_sets[10] == exact_sets[11]
    assert len(exact_sets[10]) == 270
    return data, all_support


def enumerate_positive_histogram(edges, m):
    neighbors = {a: tuple(b for u, b in edges if u == a) for a in VERTICES}
    hist = Counter()
    def dfs(prev, cur, first, frame, depth):
        if depth == m:
            if cur == ROOT and prev != first: hist[frame] += 1
            return
        for nxt in neighbors[cur]:
            if nxt != prev:
                dfs(cur, nxt, first if first is not None else nxt,
                    advance(frame, nxt), depth + 1)
    dfs(None, ROOT, None, ROOT, 0)
    return {frame: hist[frame] for frame in FRAMES}


def verify():
    # Two exact searches: independent pruning logic, identical complete target.
    no_pair, stats_plain = independent_global_exclusion(14, pair_prune=False)
    with_pair, stats_pair = independent_global_exclusion(14, pair_prune=True)
    assert no_pair is None and with_pair is None
    # A direct named 15-arc witness reaches all six states at each length.
    profile, support = typed_support_and_fixed_point(BASE)
    hist = {m: enumerate_positive_histogram(BASE, m) for m in range(4, 8)}
    assert hist[4] == dict(zip(FRAMES, (1,1,1,1,1,2)))
    assert hist[5] == dict(zip(FRAMES, (1,1,1,3,1,1)))
    assert hist[6] == dict(zip(FRAMES, (3,1,2,3,2,3)))
    assert hist[7] == dict(zip(FRAMES, (8,6,6,7,7,9)))
    return {
        'schema': 'R723_GLOBAL_MIN_15_ARC_EXACT_CERT_V1',
        'status': 'R723_GLOBAL_15_ARC_SHARP_PASS',
        'model': 'rooted 012, 5 of original 6 X6 axes, ordered V17 CNB directed J(5,3) arc permissions',
        'frozen_P000_commit': 'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'possible_arcs': len(ARCS),
        'edge_catalog': ['>'.join(edge) for edge in ARCS],
        'path_catalog': {str(m): {f: len(CATALOGS[m][0][f]) for f in FRAMES} for m in (4,5)},
        'path_catalog_positive_counts': {str(m): CATALOGS[m][1] for m in (4,5)},
        'budget_14_search_plain': stats_plain,
        'budget_14_search_pair_prune': stats_pair,
        'global_lower_bound_arcs': 15,
        'all_length_upper_bound_arcs': len(BASE),
        'sharp_global_min_arcs': 15,
        'witness_arcs': sorted('>'.join(e) for e in BASE),
        'witness_lift_profile': profile,
        'witness_final_support_4_to_11': support,
        'witness_positive_histogram': hist,
        'witness_stabilization_certificate': 'Exact equality D_10=D_11 of complete typed state sets (270 elements).',
        'scope': 'Existential root-return V17 holonomy supports under directed arc permissions and CNB. Does not measure native V29 Link/Port costs.',
        'remaining': 'Map arcs to native inventory/timing; classify the 15-arc extremal families and true future observer equivalences.'
    }

if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, sort_keys=True, ensure_ascii=False))
