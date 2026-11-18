#!/usr/bin/env python3
"""Exact fixed-generator V39 frame-only observability of signed relative links."""
from itertools import product
from collections import defaultdict
import json

contexts=0
for j in range(3):
    for a in (x for x in product((-1,1),repeat=3) if x[0]*x[1]*x[2]==-1):
        frame2=defaultdict(set)
        frame3=defaultdict(set)
        for s in product((-1,1),repeat=3):
            def step(v):return tuple(a[(i-1)%3]*v[(i-1)%3] for i in range(3))
            u=step(s);v=step(u)
            y=(s[j],u[j],v[j])
            b=tuple((n+1)//2 for n in y)
            h1=b[0];h2=(b[0]+b[1])%3;h3=sum(b)%3
            r=tuple(s[i]*a[i]*s[(i+1)%3] for i in range(3))
            frame2[h2,h3].add(r)
            frame3[h1,h2,h3].add(r)
        assert len(frame2)==6 and sorted(map(len,frame2.values()))==[1,1,1,1,2,2]
        assert len(frame3)==8 and all(len(v)==1 for v in frame3.values())
        contexts+=1
print(json.dumps({'contexts':contexts,'two_frame_cells':6,'ambiguous_cells':2,
                  'three_frame_cells':8,'status':'PASS'},indent=2))
