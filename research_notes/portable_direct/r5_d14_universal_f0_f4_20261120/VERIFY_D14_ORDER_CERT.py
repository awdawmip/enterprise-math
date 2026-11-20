#!/usr/bin/env python3
"""Verify all 1906 class values for f<=4 against exact solver outputs.
Inputs: f0.csv, f1.csv, f2.csv, f3.csv, f4roots.csv from EXACT_D14_BELLMAN.cpp,
classes_1906.tsv, dominance_edges_1906.bin, F4_ROOT_IDS_334.txt.
This is an order propagation audit; the C++ DP is the root-value kernel.
"""
import csv,hashlib
from pathlib import Path
P=Path(__file__).parent
D=lambda name:list(csv.DictReader((P/name).open()))
classes=list(csv.DictReader((P/'classes_1906.tsv').open(),delimiter='\t'))
assert len(classes)==1906
assert sum(int(x['members']) for x in classes)==29646
matrix=(P/'dominance_edges_1906.bin').read_bytes()
assert hashlib.sha256(matrix).hexdigest()=='c5c7c38b678aa5e3830e05895fc59f781bf72f926e5b3c19ea9aeeb262776fa6'
assert len(matrix)==1906**2 and sum(matrix)==38127
roots=[int(x.strip()) for x in (P/'F4_ROOT_IDS_334.txt').read_text().splitlines() if x.strip()]
assert len(roots)==len(set(roots))==334
for f in range(4):
    rows=D(f'f{f}.csv')
    assert len(rows)==1906
    for i,r in enumerate(rows):
        assert int(r['class'])==i and int(r['f'])==f
        assert (int(r['u']),int(r['v']),int(r['members']),int(r['actions']))==tuple(int(classes[i][k]) for k in ('u','v','members','actions'))
        assert int(r['value'])==735+950*f,(i,f,r['value'])
f4=D('f4roots.csv')
assert len(f4)==334 and {int(r['class']) for r in f4}==set(roots)
for r in f4:
    i=int(r['class'])
    assert int(r['value'])==4535 and int(r['f'])==4
    assert (int(r['u']),int(r['v']),int(r['members']),int(r['actions']))==tuple(int(classes[i][k]) for k in ('u','v','members','actions'))
assert all(any(matrix[i*1906+j] for j in roots) for i in range(1906))
print('PASS_D14_F0_F4', 'classes=1906', 'pairs=29646', 'f4_roots=334', 'all_covered=true')
