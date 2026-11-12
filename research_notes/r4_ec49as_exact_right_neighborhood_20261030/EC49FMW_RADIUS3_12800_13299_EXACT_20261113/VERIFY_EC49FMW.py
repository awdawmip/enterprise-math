#!/usr/bin/env python3
"""EC49FMW: exact cost vector and native ordered-prefix witness verifier."""
from pathlib import Path
import base64, hashlib, json, zlib
P = Path(__file__).resolve().parent
x = json.loads((P/'EXACT_CERT_EC49FMW.json').read_text())
cost = zlib.decompress(base64.b64decode(x['cost_vector_uint8_zlib_base64'], validate=True))
assert len(cost)==x['case_count']==500
assert (x['index_start'], x['index_end_inclusive']) == (12800,13299)
assert hashlib.sha256(cost).hexdigest()==x['cost_vector_sha256']
assert min(cost)==x['min_cost']==114 and max(cost)==x['max_cost']==205
assert [i for i in range(12800,13300) if cost[i-12800]==114]==x['argmins']==[12875]
assert [i for i in range(12800,13300) if cost[i-12800]==205]==x['argmaxs']
assert (cost[0],cost[75],cost[-1])==(171,114,132)
raw=P/'EXACT_NATIVE_OUTPUT_12800_13299.txt'
if raw.exists():
    b=raw.read_bytes()
    assert hashlib.sha256(b).hexdigest()==x['raw_solver_lines_sha256']
    rows=[s.split() for s in b.decode().splitlines()]
    assert len(rows)==500 and [int(y[0]) for y in rows]==list(range(12800,13300))
    assert bytes(int(y[1]) for y in rows)==cost
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
def prefixes(word):
    p=b''; q=[]
    for op in word:
        for step in STEPS[op]:
            p+=bytes([step+4]);q.append(p)
    return q
w=x['witness_words']
assert len(w)==24 and len({(a,b) for a,b,_ in w})==24
assert all(len(word)==h for h,s,word in w)
assert sum(x['witness_root_costs'].values())==114
roots={}; seen=set()
for h,s,word in w:
    for prefix in prefixes(word):
        seen.add(prefix);roots.setdefault(prefix[:1].hex(),set()).add(prefix)
assert len(seen)==114
assert {k:len(v) for k,v in roots.items()}==x['witness_root_costs']=={'05':50,'06':52,'07':12}
try:
    from EC49FGW_RADIUS5_SCREEN import all_words,raw_key,PIN
    assert PIN==x['science_pin']
    catalogue=set(all_words());assert len(catalogue)==178850
    keys=sorted({raw_key(word) for lab,word in catalogue});assert len(keys)==94
    cases=json.loads((P/'cases.json').read_text());assert len(cases['cases'])==38169
    assert cases['cases'][12875]==x['witness_seven_keys']
    allowed={keys[j] for j in x['witness_seven_keys']}
    assert all(((h,s),word) in catalogue and raw_key(word) in allowed for h,s,word in w)
except ImportError:
    print('FROZEN_CATALOGUE_NOT_PRESENT: only structural witness checked; legality needs pinned generator')
print('EC49FMW_PASS',len(cost),min(cost),x['argmins'],max(cost),len(seen))
