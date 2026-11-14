"""EC49FFD exact observer-staircase audit; Python >=3.9, standard library only.
Frozen source model: EC49FFC/VERIFY_EC49FFC_COMPACT.py at PR #1730@2dd856c4.
"""
import json
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import combinations, product
from math import prod

ALPHABET = 'acdefg'
TRANSITIONS = ((1,2,3,1,4,5), (1,6,7,1,1,1), (2,2,8,2,2,2),
               (3,8,3,3,3,3), (4,2,7,4,4,4), (5,6,3,5,5,5),
               (6,6,8,6,6,6), (7,8,7,7,7,7), (8,8,8,8,8,8))
LABELS = (0,0,4,1,16,32,8,2,0)

@lru_cache(maxsize=None)
def terminal_states(counts):
    """Bits of DFA states reached by all orderings of one operation multiset."""
    if not any(counts):
        return 1  # DFA start state 0
    answer = 0
    for letter in range(6):
        if counts[letter] == 0:
            continue
        prior = list(counts)
        prior[letter] -= 1
        statebits = terminal_states(tuple(prior))
        for q in range(9):
            if statebits & (1 << q):
                answer |= 1 << TRANSITIONS[q][letter]
    return answer

def dfa_signature_support(counts):
    states = terminal_states(counts)
    result = 0
    for q, label in enumerate(LABELS):
        if states & (1 << q):
            result |= label
    return result

def analytic_signature_support(t, f, g):
    return 15 if t >= 1 else ((16 if f else 0) | (32 if g else 0))

def key_horizon_census():
    rows = []
    total_pairs = 0
    strict_pairs = 0
    bad = []
    unique_keys = set()
    for h in range(2, 10):
        profiles = Counter()
        for z in range(1, (h + 1) // 2 + 1):
            n = h + 1 - 2 * z
            for t in range(n + 1):
                for f in range(n - t + 1):
                    g = n - t - f
                    key = (t + 2*z + f, t + g, z)
                    unique_keys.add(key)
                    total_pairs += 1
                    strict_pairs += int(min(key) > 0)
                    actual = 0
                    for c in range(t + 1):
                        actual |= dfa_signature_support((z - 1, c, t - c, z, f, g))
                    predicted = analytic_signature_support(t, f, g)
                    if actual != predicted:
                        bad.append((h, key, predicted, actual))
                    category = {0:'zero', 15:'all_low', 16:'only_16', 32:'only_32', 48:'both_high'}[actual]
                    profiles[category] += 1
        rows.append(dict(horizon=h, **{p:profiles[p] for p in
                            ('all_low','only_16','only_32','both_high','zero')}))
    assert not bad, bad
    assert (total_pairs, len(unique_keys), strict_pairs) == (294,164,270)
    assert [(r['all_low'],r['only_16'],r['only_32'],r['both_high'],r['zero']) for r in rows] == [
       (1,1,1,0,0),(3,1,1,1,1),(7,2,2,2,0),(13,2,2,4,1),
       (22,3,3,6,0),(34,3,3,9,1),(50,4,4,12,0),(70,4,4,16,1)]
    return rows, {'count_admissible_pairs':total_pairs,'distinct_full_keys':len(unique_keys),
                  'strict_positive_pairs':strict_pairs, 'dfa_mismatches':len(bad),
                  'cached_dfa_count_states':terminal_states.cache_info().currsize}

def high_options(h):
    """Full-B keys at h, ordered by z and f (one key per horizon)."""
    options = []
    for z in range(1, (h + 1)//2 + 1):
        n = h + 1 - 2*z
        for f in range(1, n):
            g = n - f
            options.append((2*z + f, g, z))
    assert len(options) == (h - 1)**2 // 4
    return options

def covers_prior_low(key, h):
    x,y,z = key
    top = x + y - 1
    return top - min(x - 2*z, y) <= h < top

def five_key_census():
    rows = []
    for late_high in combinations(range(4, 10), 4):
        high = (3,) + late_high
        low = tuple(sorted(set(range(2, 10)) - set(high)))
        keysets = product(*(high_options(h) for h in high))
        feasible = 0
        total = 0
        for keys in keysets:
            total += 1
            if all(any(covers_prior_low(k, l) for k in keys) for l in low):
                feasible += 1
        rows.append({'high_horizons':list(high), 'low_horizons':list(low),
                     'inventories':total,'signature_feasible':feasible,
                     'signature_infeasible':total-feasible})
    assert len(rows) == 15
    assert sum(row['inventories'] for row in rows) == 42048
    assert sum(row['signature_feasible'] for row in rows) == 27732
    assert sum(row['signature_infeasible'] for row in rows) == 14316
    return rows

if __name__ == '__main__':
    per_h, summary = key_horizon_census()
    per_fam = five_key_census()
    print(json.dumps({'result':'EXACT_PASS', 'frozen_scientific_pin':
          'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
          'model':'original nine-state DFA and full-BRC-key count constraints',
          'source':'PR1730@2dd856c416f111d90d523dcb10cde952248ec814',
          'by_horizon':per_h,'summary':summary,
          'five_key_22_path_family_census':per_fam},
          ensure_ascii=False, indent=2))
