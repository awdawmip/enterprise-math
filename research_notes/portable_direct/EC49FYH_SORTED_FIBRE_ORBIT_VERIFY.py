#!/usr/bin/env python3
"""Exact finite verification of the S_k multiset quotient of EC49FYG.
Run: python3 EC49FYH_SORTED_FIBRE_ORBIT_VERIFY.py
No dependencies; no floating-point arithmetic; fixed BRC16943 50-mask atlas.
"""
import json
from collections import Counter, defaultdict

F = (23, 86, 91, 101, 123, 157, 175, 203, 211, 243, 245, 281, 287,
     299, 301, 327, 346, 367, 371, 389, 394, 410, 412, 447, 457, 460,
     486, 491, 567, 599, 602, 613, 615, 646, 673, 697, 701, 718, 721,
     753, 788, 789, 828, 833, 857, 867, 949, 965, 980, 1005)
assert len(F) == len(set(F)) == 50
M50 = (1 << 50) - 1
M600 = (1 << 600) - 1
ROW = tuple(sum(1 << i for i, U in enumerate(F) if (U >> t) & 1)
            for t in range(10))
YES = tuple(tuple(sum(1 << (12*i + z+1)
                          for i, U in enumerate(F) if U >> t & 1
                          for z in range(-1, 11) if z != j)
                  for j in range(11)) for t in range(10))
# For an unobserved hole column, full and unseen-hole physical states are retained.
A_PHYS = tuple(tuple(sum(1 << (12*i + m) for m in [0, *range(k+1, 12)])
                     for i in range(50)) for k in range(12))
B_PHYS = tuple(tuple(1 << (12*i + j+1) for i in range(50)) for j in range(11))

def bits(x):
    while x:
        low = x & -x
        yield low.bit_length() - 1
        x ^= low

def expand(s):
    k, A, B = s
    out = 0
    for i in bits(A): out |= A_PHYS[k][i]
    for j, m in enumerate(B):
        for i in bits(m): out |= B_PHYS[j][i]
    return out

def update(s, t, j, b):
    k, A, B = s
    good = ROW[t] if b else M50 ^ ROW[t]
    if j < k:
        nextB = tuple((0 if b else v) if h == j else v & good
                      for h, v in enumerate(B))
        return (k, A & good, nextB)
    assert j == k < 11
    return (k+1, A & good, tuple(v & good for v in B) + (0 if b else A,))

def key(s):
    return (s[0], s[1], tuple(sorted(s[2])))

def signature(s):
    """All attainable (question, two answer-child orbit) options; seen columns unlabeled."""
    k = s[0]
    pairs = []
    for t in range(10):
        for j in range(k+1):
            if j == 11: continue
            zero, one = update(s,t,j,0), update(s,t,j,1)
            if expand(zero) == 0 or expand(one) == 0: continue
            pairs.append((key(zero),key(one)))
    return tuple(sorted(pairs))

level = {(0, M50, tuple()): M600}
summary = []
oracle_checks = 0
nonempty_transitions = 0
orbit_signature_classes_checked = 0
for depth in range(5):
    counts = Counter()
    orbit_representatives = {}
    sizes = defaultdict(int)
    for s, oracle in level.items():
        if expand(s) != oracle:
            raise AssertionError(f'600-state oracle mismatch at depth {depth}')
        oracle_checks += 1
        counts[s[0]] += 1
        q = key(s)
        sizes[q] += 1
        orbit_representatives.setdefault(q,s)
    summary.append({
        'depth':depth, 'ordered_states':len(level), 'multiset_orbits':len(sizes),
        'by_seen_columns':dict(sorted(counts.items())),
        'largest_orbit':max(sizes.values())})
    # Invariance test across every reachable ordered state through depth 3.
    if depth <= 3:
        sigs = {}
        for s in level:
            q = key(s)
            v = signature(s)
            if q in sigs and v != sigs[q]:
                raise AssertionError(f'orbit transition mismatch at depth {depth}')
            sigs[q] = v
        orbit_signature_classes_checked += len(sigs)
    if depth == 4: break
    nextlevel = {}
    for s, oracle in level.items():
        for t in range(10):
            for j in range(min(s[0]+1, 11)):
                for b in (0,1):
                    child = update(s,t,j,b)
                    physical = oracle & (YES[t][j] if b else M600 ^ YES[t][j])
                    if not physical: continue
                    nonempty_transitions += 1
                    if child in nextlevel:
                        if nextlevel[child] != physical:
                            raise AssertionError('state alias oracle mismatch')
                    else: nextlevel[child] = physical
    level = nextlevel

assert [x['ordered_states'] for x in summary] == [1,20,555,11639,185224]
assert [x['multiset_orbits'] for x in summary] == [1,20,410,5443,45888]
output = {
    'schema':'EC49FYH_SEEN_COLUMN_MULTISET_QUOTIENT_V1',
    'science_pin':'BRC16943',
    'source_parent':'EC49FYG@b76275e1968a006005b16e96c9cb1c0f18b08bd6',
    'claim':'Exact S_k quotient by sorting seen-hole masks; preserve physical-label decoder',
    'status':'ALL_PASS',
    'arithmetic':'Python arbitrary-precision integers, exact',
    'original_states':600,
    'physical_sites':110,
    'frozen_support_masks':50,
    'depth_range_exhaustive':'0..4 canonical query histories',
    'layer_counts':summary,
    'ordered_states_oracle_checked':oracle_checks,
    'nonempty_transitions_generated':nonempty_transitions,
    'distinct_orbit_signature_classes_tested_depth0_to3':orbit_signature_classes_checked,
    'max_depth4_compression_ratio':f"{summary[4]['ordered_states']}/{summary[4]['multiset_orbits']}",
    'unresolved':'Global depth-14 feasibility vs known depth-15 construction'
}
print(json.dumps(output, ensure_ascii=False, indent=2))
