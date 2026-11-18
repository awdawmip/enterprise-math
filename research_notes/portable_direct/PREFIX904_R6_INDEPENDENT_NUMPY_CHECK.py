#!/usr/bin/env python3
"""PREFIX-904 independent exact int64 vectorized overlap recount.
Requires numpy. Run alongside PREFIX904_R6_TWO_SOURCE_GAP_RESULTS.json.
Checks all 241 gap rows; no sampling, no floating arithmetic.
"""
import json
import numpy as np
p=32
N=1<<p
T=33*N
LO,HI=262145,524287
Q=np.arange(LO,HI+1,2,dtype=np.int64)
S={262147,280001,300001,320003,340007,360007,380003,400009,
   420001,440003,460001,480007,500383,510007,520001,524285}
U={int(q) for q in Q if any(((1<<h)-1)%int(q)==0 or ((1<<h)+1)%int(q)==0
                           for h in range(1,32))}
U|=S|set(range(400011,400522,2))|set(range(480011,480522,2))
P={510000+k+194*j for k in (1,3,5) for j in range(64)}
Uflag=np.array([int(q) in U for q in Q])
Pflag=np.array([int(q) in P for q in Q])
assert sum(Uflag)==552 and sum(Pflag)==192
r=json.load(open('PREFIX904_R6_TWO_SOURCE_GAP_RESULTS.json'))
for row in r['gaps']:
    d=row['d']
    a=Q[d//2:]
    b=Q[:-d//2]
    assert np.all(a-b==d)
    e=((a*b<T)|Uflag[d//2:]|Uflag[:-d//2]|
       ((a//np.gcd(a,b))*b<N)|
       (33*((N+a-1)//a)>b)|(33*((N+b-1)//b)>a))
    pr=Pflag[d//2:]|Pflag[:-d//2]
    got=(len(a),int(e.sum()),int(pr.sum()),int((e&pr).sum()),
         int((e|pr).sum()),int((~(e|pr)).sum()))
    want=tuple(row[k] for k in
               ('pairs','E','P','E_and_P','already_C902','new_C903'))
    assert got==want,(d,got,want)
print('INDEPENDENT_EXACT_VECTOR_RECOUNT_PASS',
      len(r['gaps']),r['ordered_new_pairs_relative_to_PREFIX903'],
      r['certified_904_union'])
