#!/usr/bin/env python3
"""R5 exact m=4, all true-event overlaps, signed cyclotomic jets."""
from math import lcm
from pathlib import Path
import json,sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'r5_m2_o1_exact_period_20261122'))
import VERIFY_R5_M2_O1 as base

CAP=3

def by_price(d,mask):
    union,sigs=base.data_for(mask)
    events=[i for i in range(5) if mask>>i&1]
    idx={i:j for j,i in enumerate(events)}
    E=tuple([0]*len(events))
    dp={E:([1]+[0]*(d-1),[0]*d)}
    for p in union:
        affected=tuple(idx[i] for i in events if sigs[p]>>i&1)
        nxt={counts:(v[:],dv[:]) for counts,(v,dv) in dp.items()}
        for counts,(v,dv) in dp.items():
            lim=min(CAP-counts[j] for j in affected)
            for r in range(1,lim+1):
                new=tuple(counts[j]+(r if j in affected else 0) for j in range(len(events)))
                a=base.cyclic_shift(v,p*r)
                b=[u+p*r*x for u,x in zip(base.cyclic_shift(dv,p*r),a)]
                if new in nxt:
                    z,y=nxt[new];nxt[new]=base.add(z,a),base.add(y,b)
                else:nxt[new]=a,b
        dp=nxt
    q,dq=[0]*d,[0]*d
    for v,dv in dp.values():q,dq=base.add(q,v),base.add(dq,dv)
    return base.prod_factor_jet(q,dq,union)


def hgroup(d,prices):
    """Complete homogeneous functions H0..H3 by group-specific generating product."""
    h=[([1]+[0]*(d-1),[0]*d)]+[([0]*d,[0]*d) for _ in range(CAP)]
    for p in prices:
        for r in range(1,CAP+1):
            q,dq=h[r]
            prev,preved=h[r-1]
            v=base.cyclic_shift(prev,p)
            w=[x+p*y for x,y in zip(base.cyclic_shift(preved,p),v)]
            h[r]=base.add(q,v),base.add(dq,w)
    return h


def by_group(d,mask):
    union,sigs=base.data_for(mask)
    events=[i for i in range(5) if mask>>i&1]
    idx={i:j for j,i in enumerate(events)}
    groups={}
    for p,s in sigs.items():groups.setdefault(s,[]).append(p)
    dp={tuple([0]*len(events)):([1]+[0]*(d-1),[0]*d)}
    for s,prices in groups.items():
        affected=tuple(idx[i] for i in events if s>>i&1)
        H=hgroup(d,prices)
        nxt={}
        for counts,(q,dq) in dp.items():
            lim=min(CAP-counts[j] for j in affected)
            for r in range(lim+1):
                new=tuple(counts[j]+(r if j in affected else 0) for j in range(len(events)))
                a,b=H[r]
                v=base.cyclic_mul(q,a)
                w=base.add(base.cyclic_mul(dq,a),base.cyclic_mul(q,b))
                if new in nxt:
                    x,y=nxt[new];nxt[new]=base.add(x,v),base.add(y,w)
                else:nxt[new]=v,w
        dp=nxt
    q,dq=[0]*d,[0]*d
    for v,dv in dp.values():q,dq=base.add(q,v),base.add(dq,dv)
    return base.prod_factor_jet(q,dq,union)


def numerator(d,fn):
    q,dq=[0]*d,[0]*d
    for mask in range(1,32):
        a,b=fn(d,mask)
        if mask.bit_count()%2:q,dq=base.add(q,a),base.add(dq,b)
        else:q,dq=base.sub(q,a),base.sub(dq,b)
    return base.cyclotomic_reduce(q,d),base.cyclotomic_reduce(dq,d)


def verify():
    rows=[]
    for d in base.WITNESS_ORDERS:
        a=numerator(d,by_price)
        b=numerator(d,by_group)
        assert a==b,('full jet mismatch',d)
        v0,v1=a
        j=0 if any(v0) else 1 if any(v1) else 2
        nd=sum(p%d==0 for p in base.PRICES)
        coeff= None if j==2 else next((i,x) for i,x in enumerate(a[j]) if x)
        print(d,nd,j,nd-j,coeff,flush=True)
        rows.append((d,nd,j,nd-j,coeff))
    survive=[r[0] for r in rows if r[2]<=1 and r[3]>=3]
    print('L_necessary_witness',lcm(*survive),'L_ceiling',base.EXPECTED_L)
    assert len(survive)==len(base.WITNESS_ORDERS),('must investigate higher jets for missing roots',survive)
    assert lcm(*survive)==base.EXPECTED_L
    print('ALL CHECKS PASS')
    return rows

if __name__=='__main__':verify()
