#!/usr/bin/env python3
"""Complete raw cache-key coverage and exact input for released-one-key B=20,21,22.

Frozen science input generator: EC49FGW_RADIUS5_SCREEN.py
Frozen witnesses: EC49FGJ_SEVEN_KEY_94_WITNESSES.json
This produces the independent C++ trie proof input, without using the proof result.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, raw_key, validate_profile

assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab', PIN
C = list(all_words())
cov = defaultdict(set)
with open('EC49FJO_CATALOG.tsv', 'w') as fp:
    for lab, w in C:
        k = raw_key(w)
        cov[k].add(lab)
        fp.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
assert len(C) == 178850 and len(cov) == 94

cnt = Counter()
records = []
with open('EC49FJO_CASES.tsv', 'w') as fp:
    for profile in W['profiles']:
        rows, paths = validate_profile(profile)
        assert len(rows) == 24 and len(set().union(*paths)) == 94
        sp, sk = defaultdict(int), defaultdict(int)
        for i, (r, ps) in enumerate(zip(rows, paths)):
            sk[raw_key(r['word'])] |= 1 << i
            for p in ps:
                sp[p] |= 1 << i
        assert len(sp) == 94 and len(sk) == 7
        oldkeys = set(sk)
        for Q in combinations(range(24), 6):
            mask = sum(1 << i for i in Q)
            removed = sum((v & mask) == v for v in sp.values())
            # As the original witness has 94 prefixes, B=removed-1.
            B = removed - 1
            if B not in (20, 21, 22):
                continue
            released = {k for k, v in sk.items() if (v & mask) == v}
            if len(released) != 1:
                continue
            F = {p for p, v in sp.items() if (v & mask) != v}
            assert len(F) == 93 - B
            fixed = oldkeys - released
            assert len(fixed) == 6
            labels = [(rows[i]['window'], rows[i]['signature']) for i in Q]
            uncovered = {lab for lab in labels if not any(lab in cov[k] for k in fixed)}
            candidates = [k for k in cov if k not in fixed and uncovered.issubset(cov[k])]
            assert len(candidates) == 1 and set(candidates) == released, (profile['profile_id'], B, Q, candidates, released)
            def keytext(keys):
                return ';'.join(','.join(map(str, k)) for k in sorted(keys))
            opts = '|'.join(keytext(fixed | {k}) for k in candidates)
            fp.write(f'{profile["profile_id"]}\t{",".join(map(str, Q))}\t{ ";".join(f"{h},{sig}" for h, sig in labels) }\t{opts}\t{ ";".join(p.hex() for p in sorted(F)) }\n')
            cnt[(profile['profile_id'], B)] += 1
            records.append({'profile': profile['profile_id'], 'B': B, 'Q': list(Q), 'retained_prefixes': len(F),
                            'key_choice_count': len(candidates), 'original_new_prefixes': 94-len(F)})
expected = {('A',20):240, ('B',20):240, ('A',21):69, ('B',21):69, ('A',22):40, ('B',22):40}
assert dict(cnt) == expected, (cnt,expected)
assert len(records) == 698
Path('EC49FJO_INPUT_SUMMARY.json').write_text(json.dumps({'schema':'EC49FJO_EXACT_INPUT_V1', 'scientific_pin':PIN,
    'raw_words':len(C),'raw_cache_keys':len(cov),'full_positions_per_witness':134596,
    'by_profile_and_budget':{f'{p}_B{b}':n for (p,b),n in sorted(cnt.items())},
    'cases':len(records),'complete_seventh_key_choices':698,
    'records':records},indent=2,ensure_ascii=False)+'\n')
print('EC49FJO_INPUT_698_PASS',dict(cnt))
