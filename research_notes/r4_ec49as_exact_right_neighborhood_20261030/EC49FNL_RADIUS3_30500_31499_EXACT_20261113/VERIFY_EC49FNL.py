#!/usr/bin/env python3
"""Check compact EC49FNL finite certificate; use raw files if present."""
from pathlib import Path
from collections import Counter
import base64,hashlib,json,zlib
D=Path(__file__).resolve().parent
c=json.loads((D/'EXACT_CERTIFICATE_EC49FNL.json').read_text())
dec=lambda key:json.loads(zlib.decompress(base64.b85decode(c[key])).decode())
sha=lambda path:hashlib.sha256((D/path).read_bytes()).hexdigest()
assert c['schema']=='EC49FNL_BRC_7KEY_RADIUS3_EXACT_V1'
assert c['scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
start,end=c['range']; assert (start,end)==(30500,31500)
vals=dec('cost_vector_zlib_b85');assert len(vals)==end-start
assert all(isinstance(v,int) and v>0 for v in vals)
assert min(vals)==c['min_cost']==94
assert [start+j for j,v in enumerate(vals) if v==94]==c['min_indices']==[31310,31323]
assert max(vals)==c['max_cost']==206
assert [start+j for j,v in enumerate(vals) if v==206]==c['max_indices']==[30697,31130]
roots=dec('root_function_all_masks_zlib_b85')
assert set(roots)=={'5','6','7'}
for r,n in [('5',4096),('6',4096),('7',256)]:
    assert len(roots[r]['labels'])==n.bit_length()-1
    assert len(roots[r]['costs'])==n and roots[r]['costs'][0]==0
    assert roots[r]['costs'][-1]>0
assert roots['5']['costs'][-1]==roots['6']['costs'][-1]==47
Q=roots['7']['labels']; assert len(Q)==8
G=[]
for mask in range(256):
    T={Q[j] for j in range(8) if (mask>>j)&1}
    saved=0
    for r in ('5','6'):
        data=roots[r]
        required=sum(1<<i for i,label in enumerate(data['labels']) if label not in T)
        saved+=data['costs'][-1]-data['costs'][required]
    G.append(roots['7']['costs'][mask]-saved)
assert G==dec('gap_vector_common_zlib_b85')
assert G[0]==0 and min(G[1:])==c['exchange_margin_min_nonempty']==8
assert [i for i in range(1,256) if G[i]==8]==c['exchange_sharp_masks']==[85,170,255]
witnesses=dec('witnesses_zlib_b85')
assert set(witnesses)=={'31310','31323'}
for key in ('31310','31323'):
    x=witnesses[key]
    assert len(x['keys'])==7 and len(x['word_paths'])==24 and x['cost']==94
    selected={tuple(e['label']) for e in x['word_paths']};assert len(selected)==24
    pp=set()
    for item in x['word_paths']:
        ps=item['path_hex'];assert ps and all(len(p)==2*(j+1) for j,p in enumerate(ps))
        assert all(ps[j].startswith(ps[j-1]) for j in range(1,len(ps)))
        assert int(ps[0],16) in (5,6)
        pp.update(ps)
    assert len(pp)==94
    assert len([p for p in pp if p.startswith('05')])==47
    assert len([p for p in pp if p.startswith('06')])==47
    assert vals[int(key)-start]==94
    print('WITNESS_PASS',key,'words',len(x['word_paths']),'prefixes',len(pp))
for file_path,expected in c['frozen_inputs_sha256'].items():
    if (D/file_path).is_file():assert sha(file_path)==expected
raw='EXACT_NATIVE_OUTPUT_30500_31499.txt'
if (D/raw).is_file():
    assert sha(raw)==c['original_native_output_sha256']
    lines=[s.split() for s in (D/raw).read_text().splitlines()]
    assert len(lines)==1000 and [(int(a[0]),int(a[1])) for a in lines]==list(zip(range(start,end),vals))
    assert dict(Counter(s[2] for s in lines))==c['ways_histogram']
    print('RAW_SCAN_1000_PASS')
for ix in c['min_indices']:
    p=f'rootfunc_{ix}.txt'
    if (D/p).is_file():
        assert sha(p)==c['root_table_hash_both']
        rr={}
        for line in (D/p).read_text().splitlines():
            root,labs,costs=line.split()
            rr[root]={'labels':list(map(int,labs.strip(',').split(','))), 'costs':list(map(int,costs.strip(',').split(',')))}
        assert rr==roots
        print('RAW_ROOT_ALL_MASKS_PASS',ix)
print('CERTIFICATE_PASS',len(vals),'min',min(vals),'max',max(vals),'common_root_masks',sum(len(x['costs']) for x in roots.values()))
