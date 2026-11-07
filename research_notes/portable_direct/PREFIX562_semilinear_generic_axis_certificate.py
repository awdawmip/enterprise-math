#!/usr/bin/env python3
"""PREFIX-562 semilinear source dependency for PREFIX-563.
Frozen native BRC model pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter
import PREFIX550_shared_gauge_compact_certificate as b
import PREFIX561_native_port_bijection_certificate as prev
F=prev.construct_lift()
ORBS=sorted({tuple(sorted({i,F[i]})) for i in range(96)})
REP=tuple(o[0] for o in ORBS)
IDX={i:k for k,o in enumerate(ORBS) for i in o}
MIR=tuple(i!=REP[IDX[i]] for i in range(96))
ZERO=(0,)*7
def sigmamon(m):return m[:4]+(m[5],m[4])+m[6:]
def sigma_poly(p):return Counter({sigmamon(m):c for m,c in p.items()})
def rows64_twisted(r):
    assert prev.sigma_root(r)==r
    return [Counter((IDX[j],MIR[j],w) for a in b.A for j,w in [b.edge(i,a,r)]) for i in REP]
def step64(rows,vector):
    out=[]
    for row in rows:
        acc=Counter()
        for (j,flip,w),n in row.items():
            for mon,c in vector[j].items():
                if flip:mon=sigmamon(mon)
                acc[tuple(mon[k]+w[k] for k in range(7))]+=n*c
        out.append(acc)
    return out
