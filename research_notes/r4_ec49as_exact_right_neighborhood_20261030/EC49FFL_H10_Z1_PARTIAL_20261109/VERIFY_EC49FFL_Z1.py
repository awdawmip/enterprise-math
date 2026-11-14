#!/usr/bin/env python3
"""Reproduce all h=10,z=1 four-low-signature BRC prefix minima."""
import json,sys
from pathlib import Path
d=Path(__file__).resolve().parent
sys.path.insert(0,str(d.parent/'EC49FFJ_NATIVE_PREFIX_TRIE_20261109'))
from VERIFY_EC49FFJ_TRIE import admissible_keys,solve
p=json.loads((d/'EXACT_REPORT_EC49FFL_H10_Z1.json').read_text())
exp={(x,y,1):v for x,y,v in p['rows_x_y_minimum']}
keys=[k for k in admissible_keys(10) if k[2]==1]
assert len(keys)==len(exp)==45 and set(keys)==set(exp)
words=nodes=0
for key in keys:
    r=solve(10,key)
    assert r['prefix_optimum']==exp[key], (key,r['prefix_optimum'],exp[key])
    words+=r['word_count'];nodes+=r['trie_nodes']
assert (words,nodes)==(383420,3317389)
assert sorted(k for k,v in exp.items() if v==56)==[(x,12-x,1) for x in range(4,11)]
print('EXACT_PASS H10 z=1 all 45 keys, minimum 56 (seven minimizing keys)')
