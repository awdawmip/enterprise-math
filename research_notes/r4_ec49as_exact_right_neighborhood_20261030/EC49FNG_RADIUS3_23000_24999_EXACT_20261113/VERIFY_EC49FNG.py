#!/usr/bin/env python3
"""Verify EC49FNG compact certificate against preserved native input/output.

For the 2000 exact lower bounds, rerun scan_cached_radius3.cpp. This script
checks vector integrity, lawful original words, native prefixes and 256-mask margins.
"""
from pathlib import Path
from collections import Counter,defaultdict
import base64,hashlib,json,lzma,zlib
from EC49FGW_RADIUS5_SCREEN import all_words,pref,raw_key,PIN
D=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
packed=(D/'EXACT_CERTIFICATE_EC49FNG.json.xz.b64').read_text().strip()
decoded=lzma.decompress(base64.b64decode(packed))
assert sha(decoded)=='db7a2adaaee468ecd8dec251c15dfd6a9d59ae3f191494cd7259f17951fb0bab'
c=json.loads(decoded)
assert c['scientific_pin']==PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert c['count']==2000 and c['range']==[23000,24999]
assert sha((D/'master_and_radius3_cases.txt').read_bytes())==c['frozen_master_input_sha256']
raw=(D/'EXACT_NATIVE_OUTPUT_23000_24999.txt').read_bytes()
assert sha(raw)==c['raw_cpp_output_sha256']
costs=zlib.decompress(base64.b85decode(c['cost_base85']))
assert len(costs)==2000 and sha(costs)==c['cost_bytes_sha256']
rows=[s.split() for s in raw.decode().splitlines()]
assert len(rows)==2000 and all(int(r[0])==23000+i and int(r[1])==costs[i] for i,r in enumerate(rows))
assert (min(costs),max(costs),len(set(costs)))==(c['minimum'],c['maximum'],c['distinct_costs'])
assert [23000+i for i,x in enumerate(costs) if x==c['minimum']]==c['minimizers']
assert [23000+i for i,x in enumerate(costs) if x==c['maximum']]==c['maximizers']
case=json.loads((D/'cases.json').read_text()); assert case['pin']==PIN and len(case['cases'])==38169
catalog=list(all_words());assert len(catalog)==178850
keytypes=sorted({raw_key(w) for lab,w in catalog});assert len(keytypes)==94
pairs={(lab,w):raw_key(w) for lab,w in catalog}
for w in c['witnesses']:
 idx=w['index']; allowed={keytypes[k] for k in w['keys']}
 assert w['keys']==case['cases'][idx] and int(costs[idx-23000])==96
 seen=set(); prefixes=set(); rset=defaultdict(set)
 assert len(w['legal_words'])==24
 for x in w['legal_words']:
  lab=tuple(x['label']);word=x['word'];assert lab not in seen
  assert (lab,word) in pairs and pairs[(lab,word)] in allowed
  seen.add(lab);p=pref(word);prefixes.update(p);rset[p[0].hex()].update(p)
 assert len(seen)==24 and len(prefixes)==96
 assert {k:len(v) for k,v in rset.items()}=={k:v for k,v in w['root_costs'].items() if v>0}
 assert sha((D/f'rootfunc_{idx}.txt').read_bytes())==w['root_function_dump_sha256']
 print('LEGAL_WORDS_AND_NATIVE_PREFIXES',idx,len(seen),len(prefixes),flush=True)
for i,reported in c['root07_shadow_report']['cases'].items():
 idx=int(i);F={}
 for s in (D/f'rootfunc_{idx}.txt').read_text().splitlines():
  r,labs,vals=s.split();F[int(r)]=([int(x) for x in labs.strip(',').split(',')],[int(x) for x in vals.strip(',').split(',')])
 assert set(F)=={5,6,7}
 l5,f5=F[5];l6,f6=F[6];l7,f7=F[7]
 assert len(l5)==12 and len(l6)==12 and len(l7)==8
 assert len(set(l5)|set(l6))==24 and set(l7)<=set(l5)|set(l6)
 assert l7==reported['root07_labels']
 s=f5[-1]+f6[-1];assert s==96==reported['full_no_07_cost']
 margins=[]
 for t in range(256):
  T={lab for j,lab in enumerate(l7) if (t>>j)&1}
  a=sum(1<<j for j,lab in enumerate(l5) if lab not in T)
  b=sum(1<<j for j,lab in enumerate(l6) if lab not in T)
  margins.append(f5[a]+f6[b]+f7[t]-s)
 assert margins[0]==0 and min(margins[1:])==8 and margins.count(0)==1
 assert {str(k):v for k,v in sorted(Counter(margins).items())}==reported['margin_counts']
 assert sha(bytes(margins))==reported['margins_sha256']
 print('SHADOW_MARGIN_PASS',idx,'nonempty_masks',255,'minimum_gap',min(margins[1:]),flush=True)
print('EC49FNG_CERTIFICATE_VERIFIED','range',c['range'],'min',c['minimum'],'count',c['count'])
