#!/usr/bin/env python3
"""Verify class identities and D14 closure of six author-solved Bellman root classes.
This checks coverage arithmetic, NOT independent root Bellman calculations.
"""
import csv, hashlib, json
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
assert hashlib.sha256((P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
a=np.fromfile(P/'dominance_edges_1906.bin',dtype=np.uint8).reshape(1906,1906)
assert int(a.sum())==38127
cl=list(csv.DictReader((P/'classes_1906.tsv').open(),delimiter='\t'))
prior=list(csv.DictReader((P/'CERTIFIED_52_CLASSES.csv').open()))
assert len(cl)==len(prior)==1906
w=np.array([int(z['members']) for z in cl])
assert int(w.sum())==29646
cov=np.array([int(p['certified'])==1 for p in prior],dtype=bool)
assert cov.sum()==1220 and w[cov].sum()==25896
rows=list(csv.DictReader((P/'ROOTS_NEW6.csv').open()))
assert len(rows)==6
for x in rows:
    j=int(x['class']); u=int(x['u']); v=int(x['v'])
    assert (int(cl[j]['u']),int(cl[j]['v']))==(u,v)
    assert int(x['V8'])==8335 and int(x['nonterminal_states'])>0
    fresh=(a[:,j].astype(bool))&~cov
    assert int(fresh.sum())==int(x['new_signature_classes'])
    assert int(w[fresh].sum())==int(x['new_named_pairs'])
    cov|=fresh
r=json.loads((P/'RESULT.json').read_text())
assert int(cov.sum())==r['updated_coverage']['signatures']==1265
assert int(w[cov].sum())==r['updated_coverage']['named_pairs']==26388
assert int((~cov).sum())==r['updated_coverage']['unresolved_signatures']==641
assert int(w[~cov].sum())==r['updated_coverage']['unresolved_named_pairs']==3258
print('PASS',int(cov.sum()),'certified classes',int(w[cov].sum()),'certified pairs',int((~cov).sum()),'unresolved classes',int(w[~cov].sum()),'unresolved pairs')
