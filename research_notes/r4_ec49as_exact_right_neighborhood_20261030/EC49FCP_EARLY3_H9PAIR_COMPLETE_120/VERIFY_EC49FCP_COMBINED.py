#!/usr/bin/env python3
"""Exact exhaustive 120-group signed-prefix calculation; two representations.
Requires frozen_model.py from EC49FCN (Git blob c21336ba1f3719cfa03b07c3a7e9722e4cd1e84b).
"""
from itertools import combinations
import json, hashlib
from frozen_model import build, REQ, candidates, W, observe, primpref
PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def run():
    chosen, early, late, pools, original = build()
    h9 = [k for k in late if k.startswith('9:')]
    groups = [(*e, *h9) for e in combinations(early, 3)]
    assert len(groups) == 120 and len(chosen) == 24 and len(h9) == 2
    words = {k: candidates(int(k.split(':')[0]))[int(k.split(':')[1])]
             for k in set(k for group in groups for k in group)}
    literal = {w: frozenset(primpref(w))
               for w in set(chosen.values()) | {w for ws in words.values() for w in ws}}
    records = []
    raw_total = checks_total = 0
    for idx, keys in enumerate(groups):
        selected = set(keys)
        fixed = 0
        for k, v in original.items():
            if k not in selected: fixed |= v
        cap = 158 - fixed.bit_count()
        bitpools = [{v & ~fixed for v in pools[k] if (v & ~fixed).bit_count() < cap} for k in keys]
        triples = {a | b | c for a in bitpools[0] for b in bitpools[1]
                   for c in bitpools[2] if (a | b | c).bit_count() < cap}
        checks = 0
        improved = False
        for e in triples:
            for a in bitpools[3]:
                if (e | a).bit_count() >= cap: continue
                for b in bitpools[4]:
                    checks += 1
                    if (e | a | b).bit_count() < cap: improved = True; break
                if improved: break
            if improved: break
        assert not improved, (idx, keys)
        literal_fixed = frozenset().union(*(literal[w] for k,w in chosen.items() if k not in selected))
        assert len(literal_fixed) == fixed.bit_count()
        lpools = [{literal[w] - literal_fixed for w in words[k]
                   if len(literal[w] - literal_fixed) < cap} for k in keys]
        ltriples = {a | b | c for a in lpools[0] for b in lpools[1]
                    for c in lpools[2] if len(a | b | c) < cap}
        limproved = any(len(e | a | b) < cap for e in ltriples for a in lpools[3]
                        if len(e | a) < cap for b in lpools[4])
        assert not limproved, (idx, keys)
        raw = 1
        for k in keys: raw *= len(pools[k])
        raw_total += raw
        checks_total += checks
        records.append({'index': idx, 'slots': list(keys), 'fixed_edges': fixed.bit_count(),
                        'minimum': 158, 'early_triple_states': len(triples),
                        'last_stage_checks': checks, 'raw_cartesian': str(raw)})
    assert raw_total == 2231276544000 and checks_total == 81432
    result = {'schema': 'EC49FCP_COMBINED_V1', 'pin': PIN, 'total_groups': 120,
              'raw_cartesian_total': str(raw_total), 'last_stage_checks': checks_total,
              'every_minimum': 158, 'bit_and_literal_crosscheck': 'ALL_120_PASS', 'rows': records}
    data = json.dumps(result, sort_keys=True, separators=(',', ':')).encode() + b'\n'
    with open('EC49FCP_COMBINED_RESULT.json', 'wb') as f: f.write(data)
    print('PASS groups=120 min=158 checks=', checks_total,
          'SHA256=', hashlib.sha256(data).hexdigest())
if __name__ == '__main__': run()
