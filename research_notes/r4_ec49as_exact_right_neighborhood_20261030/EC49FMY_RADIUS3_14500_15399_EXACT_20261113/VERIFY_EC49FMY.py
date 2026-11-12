#!/usr/bin/env python3
"""Verify compact EC49FMY GitHub certificate, optionally extract complete witness."""
import base64,hashlib,json,pathlib,sys,zlib
D=pathlib.Path(__file__).resolve().parent
c=json.loads((D/'EXACT_CERTIFICATE_EC49FMY.json').read_text())
assert c['scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert (c['index_start'],c['index_end_inclusive'],c['case_count'])==(14500,15399,900)
v=zlib.decompress(base64.b64decode(c['vector_zlib_base64'],validate=True))
assert len(v)==900 and hashlib.sha256(v).hexdigest()==c['vector_sha256']
assert min(v)==c['minimum']==104 and max(v)==c['maximum']==214
assert [i+14500 for i,t in enumerate(v) if t==min(v)]==c['minimizer_indices']==[14750]
assert [i+14500 for i,t in enumerate(v) if t==max(v)]==c['maximizer_indices']==[15050,15214]
for idx,x in c['crosschecked_python'].items(): assert v[int(idx)-14500]==x
b=zlib.decompress(base64.b64decode(c['witness_zlib_base64'],validate=True))
assert hashlib.sha256(b).hexdigest()==c['witness_compact_json_sha256']
w=json.loads(b)
assert (w['pin'],w['case_index'],w['exact_optimal_cost'])==(c['scientific_pin'],14750,104)
assert w['distinct_nonempty_native_prefix_count']==104
entries=[e for r in w['root_certificates'] for e in r['witnesses']]
assert len(entries)==c['witness_legal_word_count']==24
assert len({tuple(e['label']) for e in entries})==24
prefix=set()
for e in entries:
 seq=[bytes.fromhex(h) for h in e['path_hex']]
 assert seq and all(len(p)==j+1 for j,p in enumerate(seq))
 assert all(seq[j+1].startswith(seq[j]) for j in range(len(seq)-1))
 prefix.update(seq)
assert len(prefix)==c['witness_native_prefix_count']==104
for r in w['root_certificates']:
 rs={bytes.fromhex(h) for e in r['witnesses'] for h in e['path_hex']}
 assert len(rs)==c['witness_first_root_prefix_counts'][r['root_hex']]==r['root_min_cost']
 assert all(p[0]==int(r['root_hex'],16) for p in rs)
print('PASS: 900 exact finite costs; unique 104 optimum at 14750; 24-word 104-prefix native witness.')
if '--extract' in sys.argv:
 dest=D/'WITNESS_14750_DECOMPRESSED.json'
 dest.write_text(json.dumps(w,indent=2,ensure_ascii=False)+'\n')
 print('EXTRACTED',dest)
