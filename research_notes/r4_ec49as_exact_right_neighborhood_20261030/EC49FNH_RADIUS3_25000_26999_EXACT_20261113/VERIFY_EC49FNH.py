#!/usr/bin/env python3
"""EC49FNH reproducible finite certificate check (full evidence directory).

Requires the frozen original input, solver output, C++ solver source, original
BRC generator, complete root function tables and the seven run receipts.
Re-run the C++17 optimizer to independently regenerate all 2,000 lower bounds.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, base64, zlib, json
from EC49FGW_RADIUS5_SCREEN import all_words, pref, raw_key, PIN

P = Path(__file__).resolve().parent
H = lambda b: hashlib.sha256(b).hexdigest()
C = json.loads((P / 'EXACT_CERTIFICATE_EC49FNH.json').read_text())
assert C['scientific_pin'] == PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert H((P / 'master_and_radius3_cases.txt').read_bytes()) == C['frozen_master_input_sha256']
assert H((P / 'scan_cached_radius3.cpp').read_bytes()) == C['optimizer_cpp_sha256']
raw = (P / 'EXACT_NATIVE_OUTPUT_25000_26999.txt').read_bytes()
assert H(raw) == C['raw_solver_output_sha256']
costs = zlib.decompress(base64.b85decode(C['cost_zlib_base85']))
assert len(costs) == 2000 and H(costs) == C['cost_bytes_sha256']
rows = [s.split() for s in raw.decode().splitlines()]
assert len(rows) == 2000 and all(int(r[0]) == 25000 + j and int(r[1]) == costs[j]
                                 for j, r in enumerate(rows))
for a, b in [(25000,25299), (25300,25499), (25500,25699), (25700,25799),
             (25800,26099), (26100,26499), (26500,26999)]:
    assert 'FINISHED' in (P / f'SCAN_{a}_{b}.stderr.log').read_text()
assert min(costs) == C['minimum'] == 92 and max(costs) == C['maximum'] == 219
assert [25000+j for j,v in enumerate(costs) if v == 92] == C['minimizers'] == [26955,26966]
assert [25000+j for j,v in enumerate(costs) if v == 219] == C['maximizers'] == [26323]
assert len(set(costs)) == C['distinct_cost_count'] == 102
cases = json.loads((P / 'cases.json').read_text())
assert cases['pin'] == PIN and len(cases['cases']) == 38169
words = list(all_words())
assert len(words) == 178850
keytypes = sorted({raw_key(w) for lab,w in words})
assert len(keytypes) == 94
legals = {(lab,w):raw_key(w) for lab,w in words}

for cert in C['witnesses']:
    i = cert['index']
    assert cert['keys'] == cases['cases'][i]
    allowed = {keytypes[k] for k in cert['keys']}
    labels, prefix, roots = set(), set(), defaultdict(set)
    assert len(cert['words']) == 24
    for labels0,w in cert['words']:
        lab = tuple(labels0)
        assert lab not in labels and (lab,w) in legals and legals[(lab,w)] in allowed
        labels.add(lab)
        paths = pref(w)
        prefix.update(paths)
        roots[paths[0].hex()].update(paths)
    assert len(labels) == 24 and len(prefix) == 92
    assert {k:len(v) for k,v in roots.items()} == {'05':46, '06':46}
    f = P / f'rootfunc_{i}.txt'
    assert H(f.read_bytes()) == C['root_shadow'][str(i)]['rootfunc_sha256']
    dat = {}
    for ln in f.read_text().splitlines():
        r,ls,vs = ln.split()
        dat[int(r)] = ([int(x) for x in ls.strip(',').split(',')],
                       [int(x) for x in vs.strip(',').split(',')])
    a,fa = dat[5]; b,fb = dat[6]; q,fq = dat[7]
    assert len(a)==len(b)==12 and len(q)==8 and set(a).isdisjoint(b)
    assert len(set(a)|set(b))==24 and set(q)<=set(a)|set(b)
    assert [fa[-1],fb[-1],fq[-1]] == [46,46,40]
    margins = []
    for mask in range(256):
        T = {v for j,v in enumerate(q) if mask>>j&1}
        ua = sum(1<<j for j,v in enumerate(a) if v not in T)
        ub = sum(1<<j for j,v in enumerate(b) if v not in T)
        margins.append(fa[ua]+fb[ub]+fq[mask]-92)
    assert margins[0]==0 and min(margins[1:])==8 and margins.count(0)==1
    assert {str(k):v for k,v in Counter(margins).items()} == {
        str(k):v for k,v in C['root_shadow'][str(i)]['margin_counts'].items()}
    print('WITNESS_AND_256_MASKS_PASS',i,'cost=92','margin=8')
print('CERTIFICATE_PASS',C['range'],'n=2000','min=92','max=219')
