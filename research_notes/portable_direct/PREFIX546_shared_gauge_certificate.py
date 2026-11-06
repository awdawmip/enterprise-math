#!/usr/bin/env python3
"""PREFIX-546 exact 28-class gauge certificate. Requires adjacent PREFIX545_compact_exact_certificate.py, at GitHub commit dd9f068d02cddf62783e553de974ab4d682df9e8. Scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import Counter
import json
import PREFIX545_compact_exact_certificate as b

def ell(r,s):
    t=abs(s-r)-abs(s)-abs(r)
    assert t%2==0
    return t//2

def shared():
    labels,Q0,_=b.quotient(0); signs={}
    for i,(phase,bit) in enumerate(b.V):
        c=labels[i];s=b.sign(phase)
        if c in signs:assert signs[c]==s
        else:signs[c]=s
    assert len(signs)==28
    Q={0:Q0}
    for r in (-1,1):
        Q[r]={}
        for c,row in Q0.items():
            out=Counter()
            for (dest,p,h),n in row.items():
                k=p+ell(r,signs[c])-ell(r,signs[dest]);assert k in (0,1)
                out[dest,k,h]+=n
            Q[r][c]=out
    return labels,Q,signs

def run(D=24):
    ids,Q,signs=shared();polynomial_checks=0;edge_checks=0;totals={}
    for r in (-1,0,1):
        direct_ids,direct_Q,_=b.quotient(r)
        assert all((ids[i]==ids[j])==(direct_ids[i]==direct_ids[j]) for i in range(96) for j in range(96))
        ren={direct_ids[i]:ids[i] for i in range(96)}
        assert len(ren)==28
        for c,row in direct_Q.items():
            want=Counter({(ren[d],p,h):n for (d,p,h),n in row.items()})
            assert want==Q[r][ren[c]]
            edge_checks+=sum(row.values())
        counts=Counter()
        for row in Q[r].values():
            for (d,p,h),n in row.items():counts[(p,h)]+=n
        totals[str(r)]={f'q^{p}z^{h}':n for (p,h),n in sorted(counts.items())}
        base=[{(0,0):1} for _ in b.V]
        quot=[{(0,0):1} for _ in range(28)]
        for d in range(D+1):
            for i in range(96):
                assert base[i]==quot[ids[i]]
                polynomial_checks+=1
            if d<D:base=b.step(r,base);quot=b.qstep(Q[r],quot)
    assert edge_checks==504 and polynomial_checks==3*96*(D+1)
    assert len(set(tuple(sorted(t.items())) for t in totals.values()))==3
    return {'status':'ALL_CHECKS_PASS','classes':28,'class_sign_counts':dict(Counter(signs.values())),'gauge_weight_checks':edge_checks,'full_polynomial_checks':polynomial_checks,'depths':[0,D],'all_quotient_weights':totals}

if __name__=='__main__':
    import sys
    print(json.dumps(run(int(sys.argv[1]) if len(sys.argv)>1 else 24),ensure_ascii=False,indent=2,sort_keys=True))
