#!/usr/bin/env python3
"""Reproduce EC49FIR; place frozen EC49FGW module and witness JSON beside me."""
import collections as C
import itertools as I
import json
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, raw_key, validate_profile, index_all

assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
catalog = list(all_words())
assert len(catalog) == 178850
coverage = C.defaultdict(set)
for lab, word in catalog: coverage[raw_key(word)].add(lab)
assert len(coverage) == 94

def feasible(labs, fixed, slots, forbidden):
    missing = [lab for lab in labs if not any(lab in coverage[k] for k in fixed)]
    if not missing: return True
    target = (1 << len(missing)) - 1
    masks = {sum(1 << i for i, lab in enumerate(missing) if lab in obs)
             for k, obs in coverage.items() if k not in fixed and k != forbidden}
    masks.discard(0)
    reach = {0}
    for _ in range(slots):
        reach |= {s | m for s in tuple(reach) for m in masks}
        if target in reach: return True
    return False

profiles = []
for profile in W['profiles']:
    rows, paths = validate_profile(profile)
    labs = [(row['window'], row['signature']) for row in rows]
    key_sup = C.defaultdict(int); prefix_sup = C.defaultdict(int)
    for i, (row, ps) in enumerate(zip(rows, paths)):
        key_sup[raw_key(row['word'])] |= 1 << i
        for p in ps: prefix_sup[p] |= 1 << i
    assert len(key_sup) == 7 and len(prefix_sup) == 94
    keys0 = set(key_sup)
    trie, base, count, _ = index_all((lab, w) for lab, w in catalog if raw_key(w) in keys0)
    assert sum(count.values()) == 9838
    ext = [tuple((p, v[lab]-len(p)) for p, v in trie.items()
                 if p in prefix_sup and lab in v) for lab in labs]
    counts = C.Counter(); budget = C.Counter(); candidates = []
    for Q in I.combinations(range(24), 6):
        q = sum(1 << i for i in Q)
        released = {k for k, support in key_sup.items() if support & q == support}
        b = sum(support & q == support for support in prefix_sup.values()) - 1
        counts['all'] += 1
        if not released:
            counts['retained_seven'] += 1
            continue
        counts['key_release'] += 1
        if b < 0:
            counts['release_fixed94'] += 1
            continue
        counts['release_nontrivial'] += 1
        fixed = keys0 - released; r = len(released); selected = [labs[i] for i in Q]
        assert feasible(selected, fixed, r, None)
        mandatory = {k for k in released if not feasible(selected, fixed, r, k)}
        if mandatory != released:
            counts['reallocation_possible'] += 1
            candidates.append([list(Q), b, [list(k) for k in sorted(released)],
                               [list(k) for k in sorted(mandatory)]])
            budget[(b,'reallocation')] += 1
            continue
        counts['all_keys_forced'] += 1
        budget[(b,'forced')] += 1
        lower_bound_exceeds_b = False
        for i in Q:
            m = base[labs[i]]
            for p, d in ext[i]:
                if prefix_sup[p] & q != prefix_sup[p] and d < m: m = d
            if m > b:
                lower_bound_exceeds_b = True
                break
        if lower_bound_exceeds_b:
            counts['exact_94_singleton'] += 1
            budget[(b,'singleton_proved')] += 1
        else: counts['forced_singleton_open'] += 1
    assert counts == C.Counter(all=134596,retained_seven=69462,key_release=65134,
       release_fixed94=11623,release_nontrivial=53511,all_keys_forced=53221,
       reallocation_possible=290,exact_94_singleton=26540,forced_singleton_open=26681)
    profiles.append(dict(profile=profile['profile_id'],counts=dict(counts),
        budget=[dict(B=k[0],kind=k[1],count=v) for k,v in sorted(budget.items())],
        reallocation_candidates=candidates))
    print('EC49FIR_PROFILE_PASS',profile['profile_id'],counts)
result = dict(schema='EC49FIR_REPRO_EXACT_V1',frozen_pin=PIN,profiles=profiles)
Path('EC49FIR_REPRO_REPORT.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print('EC49FIR_REPRO_PASS')
