"""R725: exhaustive classification of sharp 15-arc rooted V17/CNB S3 carriers.
Exact integer/set computation, Python 3 standard library.
Run: python R725_15ARC_CLASSIFY_VERIFY.py > R725_15ARC_RESULTS.json
"""
import json
from collections import defaultdict
from itertools import combinations, permutations

ROOT = '012'
TRIADS = tuple(''.join(t) for t in combinations('01234', 3))
ARCS = tuple((a, b) for a in TRIADS for b in TRIADS if len(set(a)&set(b)) == 2)
ARC_ID = {e: i for i, e in enumerate(ARCS)}
FRAMES = tuple(sorted(''.join(t) for t in permutations(ROOT)))
NEIGHBORS = {a: tuple(b for x, b in ARCS if x == a) for a in TRIADS}
WITNESS_TEXT = '''012>024 012>123 012>124 013>012 013>023 023>012 023>013
024>023 024>124 123>013 123>023 123>134 124>123 124>134 134>013'''
WITNESS = frozenset(tuple(x.split('>')) for x in WITNESS_TEXT.split())
assert len(TRIADS) == 10 and len(ARCS) == 60 and len(WITNESS) == 15

def step(frame, target):
    left = next(x for x in frame if x not in target)
    right = next(x for x in target if x not in frame)
    return frame.replace(left, right)

def catalog(length):
    found = defaultdict(set)
    def visit(prev, cur, first, frame, depth, mask):
        if depth == length:
            if cur == ROOT and prev != first:
                found[frame].add(mask)
            return
        for nxt in NEIGHBORS[cur]:
            if nxt != prev:
                visit(cur, nxt, nxt if first is None else first,
                      step(frame, nxt), depth+1, mask | (1 << ARC_ID[cur,nxt]))
    visit(None, ROOT, None, ROOT, 0, 0)
    return {f: tuple(sorted(found[f])) for f in FRAMES}

CATS = {m: catalog(m) for m in (4, 5)}
GROUPS = tuple((m, f, CATS[m][f]) for m in (4, 5) for f in FRAMES)
assert [[len(CATS[m][f]) for f in FRAMES] for m in (4,5)] == [
    [12,16,16,6,6,16], [60,40,40,66,66,40]]

def enumerate_fifteen(strategy='adaptive'):
    """Complete witness-union search with 15-bit budget.
    R723 independently excludes <=14 feasible solutions.
    """
    visited, solutions = set(), set()
    calls = 0
    def visit(mask):
        nonlocal calls
        calls += 1
        if mask in visited:
            return
        visited.add(mask)
        remaining = 15 - mask.bit_count()
        if remaining < 0:
            return
        missing = []
        for idx, (_, _, paths) in enumerate(GROUPS):
            if any((p & mask) == p for p in paths):
                continue
            feasible = tuple(p for p in paths if (p & ~mask).bit_count() <= remaining)
            if not feasible:
                return
            missing.append((idx, feasible))
        if not missing:
            assert mask.bit_count() == 15
            solutions.add(mask)
            return
        if strategy == 'adaptive':
            idx, paths = min(missing, key=lambda g: (len(g[1]),
                       -min((p & ~mask).bit_count() for p in g[1]), g[0]))
        else:
            idx, paths = missing[-1]
        for nxt in sorted({mask | p for p in paths}):
            visit(nxt)
    visit(0)
    return solutions, {'calls': calls, 'unique_masks': len(visited)}

def orbit(mask):
    out = set()
    for root_perm in permutations('012'):
        for spare_perm in permutations('34'):
            mapping = dict(zip('01234', root_perm + spare_perm))
            def relabel(t):
                return ''.join(sorted(mapping[x] for x in t))
            newmask = 0
            for i, (a, b) in enumerate(ARCS):
                if (mask >> i) & 1:
                    newmask |= 1 << ARC_ID[relabel(a),relabel(b)]
            out.add(newmask)
    return out

def evaluate(mask):
    outgoing = {u: tuple(v for i,(a,v) in enumerate(ARCS)
               if a == u and (mask >> i) & 1) for u in TRIADS}
    states = {(ROOT, v, step(ROOT, v), v) for v in outgoing[ROOT]}
    visited = {frozenset(states): 1}
    supports = {}
    for m in range(2, 100):
        states = {(cur,v,step(frame,v),first) for prev,cur,frame,first
                  in states for v in outgoing[cur] if v != prev}
        if m >= 4:
            supports[m] = tuple(sorted({frame
                  for prev,cur,frame,first in states if cur == ROOT and prev != first}))
            if len(supports[m]) != 6:
                return {'all_lengths': False, 'first_failed_length': m,
                        'reachable_at_failure': supports[m]}
        frozen = frozenset(states)
        if frozen in visited:
            return {'all_lengths': True, 'repeat_pair': [visited[frozen],m],
                    'repeat_state_size': len(states),
                    'checked_support_lengths': [4,m]}
        visited[frozen] = m
    raise AssertionError('No finite-period certificate before 100')

def edges(mask):
    return ['>'.join(e) for i,e in enumerate(ARCS) if (mask >> i) & 1]

def main():
    adaptive, a_stats = enumerate_fifteen('adaptive')
    reverse, b_stats = enumerate_fifteen('reverse')
    assert adaptive == reverse and len(adaptive) == 72
    orbit_reps = sorted({min(orbit(mask)) for mask in adaptive})
    assert len(orbit_reps) == 6
    assert {len(orbit(rep)) for rep in orbit_reps} == {12}
    assert set().union(*(orbit(rep) for rep in orbit_reps)) == adaptive
    classes = [(rep, evaluate(rep)) for rep in orbit_reps]
    assert [x['all_lengths'] for rep,x in classes] == [True]*4 + [False]*2
    assert all(x.get('first_failed_length') == 6 for rep,x in classes[4:])
    witness_mask = sum(1 << ARC_ID[x] for x in WITNESS)
    witness_class = next(i+1 for i,rep in enumerate(orbit_reps)
                         if witness_mask in orbit(rep))
    assert witness_class == 4
    return {'schema': 'R725_SHARP_FIFTEEN_ARC_CLASSIFICATION_V1',
      'status': 'R725_15ARC_EXHAUSTIVE_CLASSIFICATION_PASS',
      'frozen_science': 'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'model': 'Rooted 012; five X6 axes 01234; V17 slot transport; directed CNB; S3 support',
      'catalog_counts': {str(m): {f:len(CATS[m][f]) for f in FRAMES} for m in (4,5)},
      'solver_adaptive': a_stats, 'solver_reverse': b_stats,
      'qualifying_fifteen_arc_sets_for_m4_and_m5': len(adaptive),
      'root_preserving_symmetry_group_order': 12,
      'orbit_count': len(orbit_reps), 'orbit_size_each': 12,
      'orbits': [{'orbit':i+1, 'canonical_mask':rep, 'edges':edges(rep),
         'all_length_certificate':cert} for i,(rep,cert) in enumerate(classes)],
      'all_length_orbits': sum(cert['all_lengths'] for _,cert in classes),
      'all_length_exact_fifteen_arc_sets': 48,
      'short_horizon_only_sets': 24,
      'r721b_witness_orbit': witness_class,
      'scope': 'Complete 15-arc H4=H5=S3 catalog and full-length classification by lifted-set repeat/first failure.'}

if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, indent=2, sort_keys=True))
