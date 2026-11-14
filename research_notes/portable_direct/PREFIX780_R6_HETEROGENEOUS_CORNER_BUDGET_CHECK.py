#!/usr/bin/env python3
"""Exact rational regression for PREFIX-780's seven-pair nonuniform budgets.
This checks analytic identities and sharpness witnesses, not the inherited 189-layer coefficients.
"""
from fractions import Fraction as F
from itertools import product


def bounds(A1, A2, B1, B2, p1, p2, c, delta):
    assert B2 > B1 > 0 and A1 > 0 and A2 > 0
    D = A2 * B1 - A1 * B2
    assert D > 0
    S1, S2 = sum(p1), sum(p2)
    d = min(delta, 2*c)
    H = B2*S1 + B1*S2 + (B2-B1)*c + B1*d
    return D,H


def threshold_scale(D, B1, B2, S1, S2, c, delta):
    W = B2*S1 + B1*S2 + (B2-B1)*c
    T = W + 2*B1*c
    assert T > 0
    t1 = D / T
    if t1 <= 1 and 2*t1*c <= delta:
        t=t1
    else:
        assert W > 0
        t=(D-B1*delta)/W
    assert 0 < t <= 1
    assert t*W + B1*min(delta, 2*t*c) == D
    return t


def check_case(A1, A2, B1, B2, p1, p2, c, delta):
    D,H=bounds(A1,A2,B1,B2,p1,p2,c,delta)
    assert all(x >= 0 for x in (*p1,*p2,c,delta))
    # Cross-check exact corner support by enumerating the 2D polygon vertices.
    candidates={(F(s)*c,F(t)*c) for s in (-1,1) for t in (-1,1)}
    for s in (-1,1):
        for z in (-1,1):
            candidates.add((F(s)*c,F(s)*c+F(z)*delta))
            candidates.add((F(s)*c+F(z)*delta,F(s)*c))
    candidates={(e,f) for e,f in candidates if abs(e)<=c and abs(f)<=c and abs(e-f)<=delta}
    assert candidates
    expected=(B2-B1)*c+B1*min(delta,2*c)
    assert max((B2*e-B1*f for e,f in candidates)) == expected
    assert max((B2*f-B1*e for e,f in candidates)) == expected
    if H < D:
        gap=(D-H)/(B1+B2)
        assert gap>0
        return 'CERTIFIED',gap
    S1,S2=sum(p1),sum(p2)
    t=threshold_scale(D,B1,B2,S1,S2,c,delta)
    d=min(delta,2*t*c)
    # Coefficients of the three private corners in each cell are +,-,-.
    signs=(1,-1,-1)
    e1=[t*a*s for a,s in zip(p1,signs)]
    f1=e1[:]
    e2=[-t*a*s for a,s in zip(p2,signs)]
    f2=e2[:]
    ec=t*c; fc=t*c-d
    assert abs(ec)<=c and abs(fc)<=c and abs(ec-fc)<=delta
    for a,e,f in zip((*p1,*p2),(*e1,*e2),(*f1,*f2)):
        assert abs(e)<=a and abs(f)<=a and e==f
    L1e=sum(s*v for s,v in zip(signs,e1))+ec
    L1f=sum(s*v for s,v in zip(signs,f1))+fc
    L2e=sum(s*v for s,v in zip(signs,e2))+ec
    L2f=sum(s*v for s,v in zip(signs,f2))+fc
    q=(A1+t*(S1+c))/B1
    assert q>0
    x1=A1-q*B1; x2=A2-q*B2
    y1=x1+L1e; z1=-x1-L1f
    y2=x2+L2e; z2=-x2-L2f
    assert (y1,z1,y2,z2) == (0,d,d,0)
    return 'SHARP_WITNESS', (t,q,d)


def R(n,d=1): return F(n,d)


def main():
    tests=[]
    # Two unrelated rational coefficient families with D>0.
    families=[(R(1),R(2),R(2),R(3)), (R(1,8),R(3,10),R(4,5),R(6,5))]
    ppatterns=[(R(0),R(0),R(0)), (R(1,80),R(1,60),R(1,40)),
               (R(1,3),R(1,4),R(1,5)), (R(1),R(1,2),R(1,4))]
    for A1,A2,B1,B2 in families:
        for p1,p2 in product(ppatterns,ppatterns):
            for c in (R(0),R(1,50),R(1,6),R(1)):
                for delta in (R(0),R(1,40),R(1,2),R(4)):
                    tests.append(check_case(A1,A2,B1,B2,p1,p2,c,delta)[0])
    assert 'CERTIFIED' in tests and 'SHARP_WITNESS' in tests
    print('ALL_CHECKS_PASS PREFIX780 HETEROGENEOUS_SHARP_CORNER_BUDGET')
    print('exact_cases=',len(tests),'certified=',tests.count('CERTIFIED'),'sharp=',tests.count('SHARP_WITNESS'))


if __name__=='__main__':
    main()
