#!/usr/bin/env python3
"""Exact 160-pair R751/R752B conditional signed-port V29 PASS check."""
from itertools import combinations, product
from collections import defaultdict
import json

N=6; pairs=0; examples=[]
for ax in combinations(range(N),3):
    for sig in product((-1,1),repeat=3):
        if sig[0]<0: continue  # exactly one representative per global-sign pair
        for eps in (-1,1):
            ports=tuple((a,s) for a,s in zip(ax,sig))
            opposite=tuple((a,-s) for a,s in zip(ax,sig))
            order=(0,1,2) if eps==1 else (0,2,1)
            a,b=[ports[t] for t in order[:2]]
            aa,bb=[opposite[t] for t in order[:2]]
            # V29 native count PASS(c;a->b), all counts initially zero
            M1={(a,b):1};M2={(aa,bb):1}
            u1=defaultdict(int);u1[a]+=1;u1[b]-=1
            u2=defaultdict(int);u2[aa]+=1;u2[bb]-=1
            assert M1!=M2 and dict(u1)!=dict(u2)
            assert sum(u1.values())==sum(u2.values())==0
            pairs+=1
            if len(examples)<2:
                examples.append({'axes':list(ax),'signs':list(sig),
                                 'orientation':eps,'pass1':[a,b],
                                 'pass2':[aa,bb]})
assert pairs==160
print(json.dumps({'status':'R752_V29_SIGNED_PORT_PASS_FIBER_SPLIT_EXACT_PASS',
                  'global_sign_pairs_checked':pairs,
                  'distinct_M_and_u_after_one_PASS':pairs,
                  'witnesses':examples,
                  'scope':'declared signed local port alphabet in exact V29 nonnegative ledger; not a certified force TRIADIC_CLOSURE_E or V39 frame update'},indent=2))
