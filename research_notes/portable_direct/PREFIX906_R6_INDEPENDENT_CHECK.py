#!/usr/bin/env python3
"""Independent NumPy check of all 247 additional multiplier-gap CSV slices."""
import csv
from pathlib import Path
import numpy as np

N=1<<32
Q=np.arange(262145,524288,2,dtype=np.int64)
M=len(Q)
S={262147,280001,300001,320003,340007,360007,380003,400009,
   420001,440003,460001,480007,500383,510007,520001,524285}
U=S|set(range(400011,400522,2))|set(range(480011,480522,2))
for h in range(1,32):
    t=1<<h
    U.update(int(q) for q in Q if (t-1)%int(q)==0 or (t+1)%int(q)==0)
assert len(U)==552
P={c+194*j for c in (510001,510003,510005,510009) for j in range(64)}
ue=np.zeros(524288,dtype=bool);ue[list(U)]=True
pe=np.zeros(524288,dtype=bool);pe[list(P)]=True

seen={1<<h for h in range(1,18)}
new=set()
for k in (1,3,5,7,9,11,13):
    for i in range(2,23):
        for j in range(1,i):
            for w in ((1<<i)+(1<<j),(1<<i)-(1<<j)):
                if w%k==0 and 0<w//k<=262142 and (w//k)%2==0:
                    d=w//k
                    if d not in seen and k>1:
                        new.add(d)
                    seen.add(d)
assert len(new)==247
path=Path(__file__).resolve().with_name("PREFIX906_R6_MULTIPLIER_GAPS_RESULTS.csv")
with path.open() as fh:
    rows={int(r["gap"]):r for r in csv.DictReader(fh)}
assert set(rows)==new
stats={n:0 for n in ("ordered_all","ordered_old_E","ordered_panel_P4",
                    "ordered_both","ordered_new")}
for d in sorted(new):
    b=Q[:M-d//2];a=b+d
    g=np.gcd(a,b)
    e=(a*b<33*N)|ue[a]|ue[b]|((a//g)*b<N)|(33*((N+a-1)//a)>b)|(33*((N+b-1)//b)>a)
    p=pe[a]|pe[b]
    vals={"ordered_all":2*len(a),"ordered_old_E":2*int(e.sum()),
          "ordered_panel_P4":2*int(p.sum()),"ordered_both":2*int((e&p).sum()),
          "ordered_new":2*int((~e&~p).sum())}
    for key,v in vals.items():
        assert int(rows[d][key])==v,(d,key,v,rows[d][key])
        stats[key]+=v
assert stats=={"ordered_all":52935484,"ordered_old_E":23629430,
              "ordered_panel_P4":175064,"ordered_both":2012,"ordered_new":29133002}
assert 7663771438+stats["ordered_new"]==7692904440
print("PASS",stats,"union",7692904440,"outside",17179869184-7692904440)
