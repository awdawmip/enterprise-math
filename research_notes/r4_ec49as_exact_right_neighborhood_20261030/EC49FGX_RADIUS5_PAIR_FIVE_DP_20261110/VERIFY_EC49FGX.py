#!/usr/bin/env python3
"""EC49FGX complete radius-five zero-key-release pair + small-budget audit.
Requires the preceding EC49FGW_RADIUS5_SCREEN.py and witness JSON in that
module's directory, as published by immutable PR #1730 research history.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREV = HERE.parent / 'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'
if PREV.exists():
    sys.path.insert(0, str(PREV))
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, pref, raw_key, validate_profile


def candidates(words, Qmask, B):
    out = []
    for L, word, old in words:
        retained = 0
        for depth, support in reversed(old):
            if (support & Qmask) != support:
                retained = depth
                break
        if L - retained <= B:
            out.append((L - retained, retained, word))
    return out


def pair_possible(a, b, B):
    a = sorted(a, key=lambda t: t[0])
    b = sorted(b, key=lambda t: t[0])
    for da, ka, wa in a:
        if da + b[0][0] <= B:
            return True
        for db, kb, wb in b:
            common = 0
            for u, v in zip(wa, wb):
                if u != v:
                    break
                common += 1
            if da + db - max(0, common - max(ka, kb)) <= B:
                return True
    return False


def include_antichain(active, mask):
    if any(existing & mask == existing for existing in active):
        return
    active[:] = [existing for existing in active if existing & mask != mask]
    active.append(mask)


def five_possible(groups, B):
    # Distinct signed/native microstep prefixes are distinct exact set atoms.
    atoms = {}
    options = []
    for group in groups:
        masks = set()
        for cost, retained, native in group:
            m = 0
            for depth in range(retained + 1, len(native) + 1):
                atom = native[:depth]
                if atom not in atoms:
                    atoms[atom] = len(atoms)
                m |= 1 << atoms[atom]
            assert m.bit_count() == cost
            masks.add(m)
        options.append(masks)
    active = [0]
    for group in sorted(options, key=len):
        following = []
        for existing in active:
            for m in group:
                together = existing | m
                if together.bit_count() <= B:
                    include_antichain(following, together)
        active = following
        if not active:
            return False
    return True


def analyze(profile, catalog):
    rows, prefixes = validate_profile(profile)
    labels = [(r['window'], r['signature']) for r in rows]
    keys = [raw_key(r['word']) for r in rows]
    assert len(set(keys)) == 7
    support = collections.defaultdict(int)
    key_support = collections.defaultdict(int)
    for i, (pre, k) in enumerate(zip(prefixes, keys)):
        key_support[k] |= 1 << i
        for p in pre:
            support[p] |= 1 << i
    assert len(support) == 94
    indexed = collections.defaultdict(list)
    accepted = set(keys)
    for lab, word in catalog:
        if raw_key(word) not in accepted:
            continue
        ps = pref(word)
        indexed[lab].append((len(ps), ps[-1],
                             [(len(p), support[p]) for p in ps if p in support]))
    assert sum(map(len, indexed.values())) == 9838
    tally = collections.Counter()
    survivor_budget = collections.Counter()
    pair_excluded_budget = collections.Counter()
    small_excluded_budget = collections.Counter()
    for Q in itertools.combinations(range(24), 5):
        m = sum(1 << i for i in Q)
        if any(support_mask & m == support_mask for support_mask in key_support.values()):
            continue
        tally['no_key_release'] += 1
        B = sum((s & m) == s for s in support.values()) - 1
        if B < 0:
            tally['fixed_background_blocked'] += 1
            continue
        opts = [candidates(indexed[labels[i]], m, B) for i in Q]
        if any(not o for o in opts):
            tally['singleton_blocked'] += 1
            continue
        tally['singleton_survived'] += 1
        if any(not pair_possible(opts[i], opts[j], B)
               for i, j in itertools.combinations(range(5), 2)):
            tally['pair_blocked'] += 1
            pair_excluded_budget[B] += 1
            continue
        tally['pair_survived'] += 1
        survivor_budget[B] += 1
        if B <= 9:
            if five_possible(opts, B):
                tally['small_budget_93_found'] += 1
            else:
                tally['small_budget_five_blocked'] += 1
                small_excluded_budget[B] += 1
    return {'id': profile['profile_id'], 'counts': dict(tally),
            'pair_excluded_by_budget': dict(sorted(pair_excluded_budget.items())),
            'pair_survived_by_budget': dict(sorted(survivor_budget.items())),
            'five_blocked_by_budget': dict(sorted(small_excluded_budget.items()))}


if __name__ == '__main__':
    catalog = list(all_words())
    assert len(catalog) == 178850
    result = {'schema': 'EC49FGX_EXACT_FINITE_RADIUS5_V1',
              'frozen_scientific_pin': PIN,
              'word_count': len(catalog),
              'result': [analyze(p, catalog) for p in W['profiles']]}
    for r in result['result']:
        c = r['counts']
        assert c['no_key_release'] == 25158
        assert c['fixed_background_blocked'] == 3992
        assert c['singleton_blocked'] == 10008
        assert c['singleton_survived'] == 11158
        if r['id'] == 'A':
            assert (c['pair_blocked'], c['pair_survived']) == (7884, 3274)
        else:
            assert (c['pair_blocked'], c['pair_survived']) == (7910, 3248)
        assert c['small_budget_five_blocked'] == 464
        assert c.get('small_budget_93_found', 0) == 0
    (HERE / 'EXACT_REPORT_EC49FGX_PORTABLE.json').write_text(json.dumps(result, indent=2) + '\n')
    print('EC49FGX_FINITE_PASS')
