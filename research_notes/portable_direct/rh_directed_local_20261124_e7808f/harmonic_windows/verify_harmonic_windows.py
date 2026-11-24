#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json


def one(L,x,R):
    a,b=x-L,R-x
    weights={n:min(F(n-L,a),F(R-n,b))/n for n in range(L+1,R)}
    values={n:F((n*n+7*n+L+x)%29-14,(n%5)+1) for n in weights}
    thresholds=sorted(set([F(0),F(1)]+[x*w for w in weights.values()]))
    integral=positive_sq=F(0)
    segments=[]
    for z0,z1 in zip(thresholds,thresholds[1:]):
        z=(z0+z1)/2
        low=F(L)/(1-F(a,x)*z)
        high=F(R)/(1+F(b,x)*z)
        selected=[n for n in weights if low<n<high]
        assert selected==[n for n,w in weights.items() if x*w>z]
        deficit=sum((values[n] for n in selected),F(0))
        integral+=(z1-z0)*deficit
        positive_sq+=(z1-z0)*max(F(0),deficit)**2
        segments.append([str(z0),str(z1),str(deficit)])
    direct=sum((weights[n]*values[n] for n in weights),F(0))
    assert integral==x*direct
    assert max(F(0),integral)**2<=positive_sq
    return len(segments)


def main():
    count=segments=0
    for L in range(1,6):
        for R in range(L+2,L+18):
            for x in range(L+1,R):
                segments+=one(L,x,R);count+=1
    data={'schema':'RH_HARMONIC_WINDOW_EXACT_CHECK_V1',
          'packages':count,'exact_threshold_segments':segments,
          'superlevel_sets_exact':True,'signed_layercake_identity_exact':True,
          'directed_jensen_bound_exact':True,
          'source':'deterministic signed rational sequence, not arithmetic prime data'}
    Path(__file__).with_name('harmonic_window_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))


if __name__=='__main__':main()
