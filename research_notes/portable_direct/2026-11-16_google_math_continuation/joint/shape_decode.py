"""Nearest translated, scaled phase templates, in exact rational arithmetic."""
from fractions import Fraction as Q
from itertools import combinations
import json
from finite_thresholds import W,SIGNATURE,counts


def orbit_distance(y,template,floor,sign):
    # At a minimum one that minimizes the range may be taken to be either the
    # gain floor or a point where two residual coordinates exchange order.
    candidates={floor}
    for i,j in combinations(range(len(y)),2):
        slope=sign*(template[i]-template[j])
        if slope:
            cross=Q(y[i]-y[j],slope)
            if cross>=floor:
                candidates.add(cross)
    best=None
    for mag in candidates:
        a=sign*mag
        delta=[v-a*p for v,p in zip(y,template)]
        hi,lo=max(delta),min(delta)
        fit=(Q(hi-lo,2),a,Q(hi+lo,2))
        if best is None or fit[0]<best[0]:best=fit
    return best


def decoder(y,floor,unknown_sign=False):
    if floor<=0 or len(y)<3:
        raise ValueError('Need a positive gain floor and at least three fourth differences.')
    signs=(-1,1) if unknown_sign else (1,)
    scores=[]
    for phase in range(6):
        template=[SIGNATURE[(phase+i)%6] for i in range(len(y))]
        fit=min((orbit_distance(y,template,floor,s) for s in signs),key=lambda z:z[0])
        scores.append(fit[0])
    return [i for i,score in enumerate(scores) if score==min(scores)]


def example_block(r0):
    # Precompute the exact counts through the required window.

    C,T=counts(r0+17)
    out=[]
    for v in [Q(-3,10),Q(-1,2),Q(1,2)]:
        delta=abs(v)
        floor=1/(1+delta)**2
        fixed,shape=[],[]
        for r in range(r0,r0+6):
            # Truncate toward zero, so |4320*d/r^5| <= delta.
            d=int(v*r**5/4320)
            raw=[Q(q**3*T[q],C[q]+d) for q in range(r,r+7)]
            z=[sum(w*x for w,x in zip(W,raw[j:]))-4 for j in range(3)]
            ds=[max(abs(z[i]-SIGNATURE[(a+i)%6]) for i in range(3)) for a in range(6)]
            fixed.append([a for a,t in enumerate(ds) if t==min(ds)])
            shape.append(decoder(z,floor))

        out.append(dict(v=str(v),starts=[r0,r0+5],fixed=fixed,shape=shape))
    return out


def examples():
    out=[case for r in (1200,12000,120000) for case in example_block(r)]
    assert all(case['shape']==[[a] for a in range(6)] for case in out[-3:])
    assert out[0]['fixed']!=out[0]['shape']
    assert out[1]['shape']!=[[a] for a in range(6)]
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    examples()
