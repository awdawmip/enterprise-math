#!/usr/bin/env python3
"""Finite 1,000-node BRC single-key edge spectrum verification; no BRC solver rerun."""
import base64
import hashlib
import itertools
import lzma
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
blob = base64.b64decode((ROOT/'EDGE_VECTOR_EC49FNP.u8x11.xz.b64').read_text().strip(),validate=True)
raw = lzma.decompress(blob,format=lzma.FORMAT_XZ)
assert len(raw) == 11000
assert hashlib.sha256(raw).hexdigest() == '4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b'
rows = [list(raw[i*11:(i+1)*11]) for i in range(1000)]
assert all(len(set(r[:7]))==7 and r[8]>0 and r[9]>0 for r in rows)
assert len(set(tuple(r[:7]) for r in rows)) == 1000
edges = set()
signatures = Counter()
for i,j in itertools.combinations(range(1000),2):
    a,b = set(rows[i][:7]),set(rows[j][:7])
    if len(a-b)!=1 or len(b-a)!=1: continue
    edges.add((i,j))
    x,y=rows[i],rows[j]
    sig=''.join(str(int(x[k]==y[k])) for k in (7,8,9))
    signatures[sig]+=1
six=defaultdict(list)
for i,r in enumerate(rows):
    keys=set(r[:7])
    for key in keys:
        six[tuple(sorted(keys-{key}))].append(i)
reconstructed=set()
for ids in six.values():
    for i,j in itertools.combinations(sorted(ids),2):
        assert (i,j) not in reconstructed
        reconstructed.add((i,j))
assert edges==reconstructed and len(edges)==27942
expected={'000':3613,'001':4700,'010':2287,'011':3862,'100':501,'101':830,'110':575,'111':11574}
assert signatures==expected
for a,b,t0,t1 in [(32273,32354,(176,2,1),(176,12,1)),(32280,32505,(135,1,4),(135,1,1)),(32807,32813,(125,1,1),(204,1,1))]:
    x,y=rows[a-32000],rows[b-32000]
    assert (a-32000,b-32000) in edges
    assert tuple(x[7:10])==t0 and tuple(y[7:10])==t1
print('VERIFIED finite 1000-node, 27942-edge spectrum:',dict(sorted(signatures.items())))
