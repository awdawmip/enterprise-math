#!/usr/bin/env python3
"""PREFIX-551 independent compact 5-exponent/12-endpoint BRC checker.
Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires published sibling PREFIX550_shared_gauge_compact_certificate.py.
"""
from collections import Counter, defaultdict
import json
import PREFIX550_shared_gauge_compact_certificate as old


def root(phase):
    v=old.P[phase][2]
    return tuple((1 if v>0 else -1) if a==abs(v) else 0 for a in range(1,7))


def check(depth=8):
    ids, growth=old.classes(old.ROOTS[0])
    assert growth==[1,12,51]
    roots=old.ROOTS
    idx={r:i for i,r in enumerate(roots)}
    phase={ids[p]:old.V[p][0] for p in range(96)}
    signature={c:root(phase[c]) for c in range(51)}
    q0=old.quotient(ids,old.ZERO_ROOT)
    # Fold Q_0 into 51 source-state rows of exact (target,gate,multiplicity).
    kernel={}
    for c in range(51):
        row=Counter()
        a=abs(old.P[phase[c]][2])-1
        for (j,w),n in q0[c].items():
            assert sum(w[:6])==1 and w[a]==1
            row[j,w[6]]+=n
        assert sum(row.values())==6
        kernel[c]=row
    # An entry has 5 BRC exponents + one gate exponent; 6th BRC is d - sum(first5).
    f=[[{} for _ in range(12)] for _ in range(51)]
    for c in range(51):f[c][idx[signature[c]]][(0,)*6]=1
    exact={r:[{old.ZERO_MON:1} for _ in range(51)] for r in roots}
    Qr={r:old.quotient(ids,r) for r in roots}
    checks=0;positions=0
    for d in range(depth+1):
        for port in range(96):
            r=root(old.V[port][0]); rix=idx[r]; axis=abs(old.P[old.V[port][0]][2])-1
            poly=defaultdict(int)
            for e,channel in enumerate(f[ids[port]]):
                for m,n in channel.items():
                    six=d-sum(m[:5]);q=list(m[:5])
                    if e!=rix:
                        if axis==5:six-=1
                        else:q[axis]-=1
                    assert min(q+[six])>=0
                    assert sum(q)+six==d-1+int(e==rix)
                    poly[tuple(q)+(six,m[5])]+=n
            assert dict(poly)==exact[r][ids[port]],(port,d)
            assert sum(poly.values())==6**d
            checks+=1;positions+=len(poly)
        if d==depth:break
        nxt=[[{} for _ in range(12)] for _ in range(51)]
        for c in range(51):
            axis=abs(old.P[phase[c]][2])-1
            for (target,gate),multiplicity in kernel[c].items():
                for e,ch in enumerate(f[target]):
                    dst=nxt[c][e]
                    for m,n in ch.items():
                        q=list(m)
                        if axis<5:q[axis]+=1
                        q[5]+=gate
                        t=tuple(q)
                        dst[t]=dst.get(t,0)+multiplicity*n
        f=nxt
        for r in roots:exact[r]=old.evo(Qr[r],exact[r])
    return dict(status='ALL_CHECKS_PASS',depth=depth,rooted_polynomials=checks,
                nonzero_coefficient_positions=positions,
                terminal_channels=12,quotient_states=51)


if __name__=='__main__':print(json.dumps(check(),indent=2))
