#!/usr/bin/env python3
"""R4-EC12 independent count-only verification, no SymPy or floating point."""
from collections import defaultdict
EDGES={0:((2,-1,-1),(2,+1,-1)),1:((0,-1,-1),(0,+1,-1)),2:((1,+1,+1),(2,+1,-1))}
def step(key,letter):
    q,r,e,t=key
    qp,eta,b=EDGES[q][letter]
    rp=2 if r==2 else (0 if letter else (1 if r==0 else 2))
    ee=eta*e
    return (qp,rp,ee,t+ee*b)
def alias(state):
    q,r,e,t=state
    return (q,r,-1 if q in (0,1) and r==2 else e,t)
def observe(hist):
    result=defaultdict(int)
    for (q,r,e,t),cnt in hist.items():
        result[(q,int(r==2),e,t)]+=cnt
    return dict(result)
def propagate(hist,collapse):
    result=defaultdict(int)
    for key,cnt in hist.items():
        for bit in (0,1):
            nxt=step(key,bit)
            if collapse:nxt=alias(nxt)
            result[nxt]+=cnt
    return dict(result)
fine={(0,0,1,0):1}
hidden={(0,0,1,0):1}
for n in range(1,129):
    fine=propagate(fine,False)
    readout=observe(propagate(hidden,False))
    assert observe(fine)==readout,("histogram mismatch",n)
    assert sum(fine.values())==2**n,("path mass mismatch",n)
    hidden=propagate(hidden,True)
    if n in (1,2,3,7,13,32,64,96,128):
        print("EXACT_PASS",n,len(fine),len(hidden),2**n)
print("PASS all depths n=1..128; positive integer histograms agree")
