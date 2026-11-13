#!/usr/bin/env python3
"""Verify EC49FMT GitHub vector and native BRC witness; use frozen inputs from FMS evidence alongside this script."""
import hashlib,json,zlib,base64,collections
from pathlib import Path
D=Path(__file__).resolve().parent
v=json.loads((D/'EXACT_VECTOR_EC49FMT.json').read_text())
cost=zlib.decompress(base64.b64decode(v['cost_uint8_zlib_base64']))
assert len(cost)==v['count']==1400 and (v['index_start'],v['index_end_inclusive'])==(10000,11399)
assert hashlib.sha256(cost).hexdigest()==v['cost_uint8_sha256']
assert min(cost)==v['min_cost']==102 and max(cost)==v['max_cost']==205
assert [10000+i for i,n in enumerate(cost) if n==102]==v['argmins']==[11121]
assert [10000+i for i,n in enumerate(cost) if n==205]==v['argmaxs']==[10864,10909]
r=D/'EXACT_NATIVE_OUTPUT_10000_11399.txt'
if r.exists():
 assert hashlib.sha256(r.read_bytes()).hexdigest()==v['complete_raw_rows_sha256']
 rows=[x.split() for x in r.read_text().splitlines()]
 assert len(rows)==1400 and [int(x[0]) for x in rows]==list(range(10000,11400))
 assert bytes(int(x[1]) for x in rows)==cost
from EC49FGW_RADIUS5_SCREEN import all_words,pref,raw_key,PIN
assert v['scientific_input_pin']==PIN
cat=list(all_words());assert len(cat)==178850
cset=set(cat);keys=sorted({raw_key(word) for _,word in cat});assert len(keys)==94
w=json.loads((D/'WITNESS_11121_EC49FMT.json').read_text())
cases=json.loads((D/'cases.json').read_text())
assert cases['cases'][11121]==w['seven_key_indices'] and cases['pin']==PIN
assert w['case_index']==11121 and w['cost']==102 and len(w['words'])==24
allowed={keys[k] for k in w['seven_key_indices']}
labels=set();prefixes=set();roots=collections.defaultdict(set)
for h,s,word in w['words']:
 assert ((h,s),word) in cset and raw_key(word) in allowed
 labels.add((h,s)); pp=pref(word);prefixes.update(pp);roots[pp[0].hex()].update(pp)
assert len(labels)==24 and len(prefixes)==102
assert {k:len(p) for k,p in roots.items()}==w['root_costs']=={'05':46,'06':44,'07':12}
print('EC49FMT_PASS',len(cost),min(cost),max(cost),len(labels),len(prefixes))
