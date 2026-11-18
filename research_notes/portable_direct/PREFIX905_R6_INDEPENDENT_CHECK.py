#!/usr/bin/env python3
"""Independent NumPy exact vector census of the 256 non-dyadic two-power gaps.

Usage: python3 PREFIX905_R6_INDEPENDENT_CHECK.py
Requires: numpy. Read the companion per-gap CSV in the same directory.
All arithmetic is signed int64 with values < 2^53.
"""
import csv
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, M = 2**32, 131072
Q = np.arange(262145, 524288, 2, dtype=np.int64)
S = {262147,280001,300001,320003,340007,360007,380003,400009,
     420001,440003,460001,480007,500383,510007,520001,524285}
U = S | set(range(400011,400522,2)) | set(range(480011,480522,2))
for h in range(1,32):
    v = 1 << h
    U.update(int(q) for q in Q if (v-1)%int(q)==0 or (v+1)%int(q)==0)
assert len(U) == 552
P = {c+194*j for c in (510001,510003,510005,510009) for j in range(64)}
assert len(P) == 256
used = np.zeros(524288, dtype=np.bool_)
used[list(U)] = True
panel = np.zeros(524288, dtype=np.bool_)
panel[list(P)] = True
D = {1 << h for h in range(1,18)}
G = set()
for i in range(2,19):
    for j in range(1,i):
        G.add((1<<i)+(1<<j))
        G.add((1<<i)-(1<<j))
G = {d for d in G if 0 < d < 262144 and d%2==0} - D
assert len(G)==256
with (BASE/"PREFIX905_R6_TWO_POWER_GAPS_RESULTS.csv").open() as fh:
    src = {int(r["gap"]):r for r in csv.DictReader(fh)}
assert G == set(src)
totals = dict.fromkeys(("ordered_all","ordered_old_E","ordered_panel_P4",
                        "ordered_both","ordered_new"),0)
for d in sorted(G):
    a = Q[:M-d//2]
    b = a+d
    gcd = np.gcd(a,b)
    e = ((a*b<33*N) | used[a] | used[b] | ((a//gcd)*b<N) |
         (33*((N+a-1)//a)>b) | (33*((N+b-1)//b)>a))
    p = panel[a] | panel[b]
    line = {"ordered_all":2*len(a),
            "ordered_old_E":2*int(e.sum()),
            "ordered_panel_P4":2*int(p.sum()),
            "ordered_both":2*int((e & p).sum()),
            "ordered_new":2*int((~e & ~p).sum())}
    for key,value in line.items():
        assert int(src[d][key])==value,(d,key,value,src[d][key])
        totals[key]+=value
assert totals == {"ordered_all":55705582,"ordered_old_E":24697804,
                  "ordered_panel_P4":184006,"ordered_both":2250,
                  "ordered_new":30826022}
assert 7632945416 + totals["ordered_new"] == 7663771438
print("PASS",totals,"certified_union",7663771438,
      "uncertified_complement",M*M-7663771438)
