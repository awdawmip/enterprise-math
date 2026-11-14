#!/usr/bin/env python3
"""Exact 6-observer equivalence certificate on frozen EC49FOP N2.
Usage: python VERIFY_EC49FOQ.py EC49FOP_PROFILES.csv EC49FOQ_COSTS.csv.gz.b64
Uses exact integer sums of four native trie-DP root costs.
"""
import base64, collections, csv, gzip, hashlib, itertools, sys
from pathlib import Path
E={5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),17:(3,6,7),19:(3,5,7),21:(3,6,7)}
R=(3,5,6,7); I=(439,314,342,8,42,266)
A=list(itertools.product(*(E[l] for l in E)))
assert len(A)==648
assert [A[i] for i in I]==[(7,6,7,5,3,7,6),(5,7,7,7,6,7,7),(7,6,6,3,7,3,3),(5,6,6,3,3,7,7),(5,6,6,5,6,7,3),(5,7,7,3,7,5,7)]
raw=collections.defaultdict(dict); d={}
with open(sys.argv[1],newline='') as f:
    for row in csv.DictReader(f):
        c,r,m,o,s,v=[int(row[k]) for k in ('config','root','must','opt','subset','cost')]
        assert s not in raw[c,r]
        raw[c,r][s]=v
        if (c,r) in d: assert d[c,r]==(m,o)
        d[c,r]=(m,o)
ids=sorted({c for c,r in d})
assert len(ids)==411 and 32315 in ids and sum(len(v) for v in raw.values())==69048
full=collections.defaultdict(list); small=collections.defaultdict(list)
rows=['config,'+','.join('cost_'+str(i) for i in I)+'\r\n']
for c in ids:
    assert all(d[c,r]==d[32315,r] for r in R)
    for r in R: assert len(raw[c,r])==(1<<d[c,r][1].bit_count())
    costs=[]
    for rho in A:
        costs.append(sum(raw[c,r][sum(1<<l for l,q in zip(E,rho) if q==r)] for r in R))
    full[tuple(costs)].append(c)
    v=tuple(costs[i] for i in I)
    small[v].append(c)
    rows.append(str(c)+','+','.join(map(str,v))+'\r\n')
assert len(full)==len(small)==178
assert sorted(map(sorted,full.values()))==sorted(map(sorted,small.values()))
assert sum(len(g)*(len(g)-1)//2 for g in full.values())==4068
stored=gzip.decompress(base64.b64decode(''.join(Path(sys.argv[2]).read_text().split())))
our=''.join(rows).encode()
assert stored==our,('compact certificate mismatch',len(stored),len(our))
print('EC49FOQ PASS: 411 configurations, 648 full assignments, 178 classes, 4068 equal pairs; six observers separate all classes')
print('costs_csv_sha256',hashlib.sha256(stored).hexdigest())
