"""Two separated windows: exact limiting masses and certified finite bin statistics."""
from collections import Counter
from fractions import Fraction as Q
from math import comb, isqrt
import json
from grid.critical_bins import UNIT, bin_number, block, full_width, prepare, terminal

def spline(x):
    return sum((-1)**j * comb(4,j) * max(Q(0), x+2-j)**3 for j in range(5)) / 6

def laws():
    for den in (1,2,7,23):
        for n in range(-3*den,3*den+1):
            m=Q(n,den)
            weights={k:spline(k-m) for k in range(-6,7)}
            assert all(v>=0 for v in weights.values())
            assert sum(weights.values())==1
            for power,answer in ((1,0),(2,Q(1,3)),(3,0)):
                assert sum((k-m)**power*v for k,v in weights.items())==answer
    return {str(m):{str(k):str(spline(k-m)) for k in range(-3,4) if spline(k-m)}
            for m in (Q(0),Q(1,2),Q(1,3))}

def finite(c):
    p=((c**9).bit_length()-1)//4
    radii=sorted({isqrt(isqrt(c)),isqrt(c),isqrt(c)*2})
    indices=sorted({0,1,*radii,*(r+1 for r in radii)})
    prepare(c+max(indices))
    terminal.cache_clear()
    histogram={r:Counter() for r in radii}
    second={r:[0,0] for r in radii}
    for v in range(2,c+1):
        for w in range(2,v+1):
            middle=block(v,w,3,terminal(w))
            read={j:full_width(c+j,v,middle) for j in indices}
            k={j:bin_number(q,p,(0,1)) for j,q in read.items()}
            for r in radii:
                mixed=k[r+1]-k[r]-k[1]+k[0]
                histogram[r][mixed]+=1
                # Outward enclosure for the exact, unrounded mixed difference.
                lo=(read[r+1][0]-read[r][1]-read[1][1]+read[0][0]) << p
                hi=(read[r+1][1]-read[r][0]-read[1][0]+read[0][1]) << p
                a,b=mixed*UNIT-hi,mixed*UNIT-lo
                assert -2*UNIT<=a<=b<=2*UNIT
                second[r][0]+=0 if a<=0<=b else min(a*a,b*b)
                second[r][1]+=max(a*a,b*b)
    n=comb(c,2)
    output=[]
    for r in radii:
        h=histogram[r]
        assert sum(h.values())==n
        # Report rigorous decimal brackets, each endpoint in millionths.
        low,high=second[r]
        den=n*UNIT*UNIT
        output.append(dict(r=r,mass_zero=h[0],histogram_min=min(h),
                           histogram_max=max(h),templates=n,
                           mse_millionths=[10**6*low//den,-(-10**6*high//den)]))
    return dict(c=c,p=p,rows=output)

if __name__=='__main__':
    print(json.dumps(dict(limiting_masses=laws(),finite=[finite(c) for c in (32,64,128,256)]),
                     indent=2))
