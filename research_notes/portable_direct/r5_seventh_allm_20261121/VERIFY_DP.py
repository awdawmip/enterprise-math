#!/usr/bin/env python3
"""Independent exact 3-event multiplicity recurrence; not the rational-series algorithm."""
from collections import defaultdict
from VERIFY_GENERATOR import Z,ZETA,zero,one,inv1,coefficients

S=[set(range(214,219)),{214,216,217,218,219,220,221},set(range(215,222))]

def ratio(mask):
    U=set().union(*(S[j] for j in range(3) if (mask>>j)&1))
    t=one
    for p in sorted(U-S[0]):t*=one-ZETA[p%7]
    for p in sorted(S[0]-U):t*=inv1(p%7)
    return t

def local(mask,m):
    active=[j for j in range(3) if (mask>>j)&1]
    U=sorted(set().union(*(S[j] for j in active)))
    states={tuple([0]*len(active)):[1,0,0,0,0,0,0]}
    for p in U:
        dims=[i for i,j in enumerate(active) if p in S[j]]
        nxt=defaultdict(lambda:[0]*7)
        for state,v in states.items():
            limit=min(m-1-state[i] for i in dims)
            for n in range(limit+1):
                dest=list(state)
                for i in dims:dest[i]+=n
                target=nxt[tuple(dest)]
                off=(n*p)%7
                for i,a in enumerate(v):target[(i+off)%7]+=a
        states=nxt
    s=[0]*7
    for v in states.values():
        for i,a in enumerate(v):s[i]+=a
    return Z(s)

def direct(m):
    raw=sum((((1 if mask.bit_count()%2 else -1)*ratio(mask)*local(mask,m)) for mask in range(1,8)),zero)
    return (one-ZETA[1])*raw

if __name__=='__main__':
    import sys
    maxm=int(sys.argv[1]) if len(sys.argv)>1 else 12
    seq=coefficients(maxm)
    for m in range(1,maxm+1):
        d=direct(m)
        assert d==seq[m-1],f'mismatch {m}: {d} vs {seq[m-1]}'
        print('independent exact check',m,'PASS')
    print('TOTAL',maxm,'PASS')
