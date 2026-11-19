"""Exact rational certificates for macro-fiber counts and fold maxima."""
from fractions import Fraction as F
from pathlib import Path
import json


def h(a, d):
    m = F(7, 16) * a**4 * d
    return 1 / (a - 1) + 5 - 4 * m / (1 + m) - 5 * m * a / (1 + m * a)


def a_bracket(H, d, side, bits=90):
    lo, hi = (F(0), F(1)) if side == 0 else (F(1), F(4))
    if side == 0:
        assert H < 4
    else:
        assert H >= h(F(4), d)
    for _ in range(bits):
        mid = (lo + hi) / 2
        if h(mid, d) > H:
            lo = mid
        else:
            hi = mid
    return lo, hi


def g15_box(a, A, d, D):
    """Natural exact interval for G^15, valid within synchronization quadrants."""
    e0, e1 = sorted((abs(a-1), abs(A-1)))
    f0, f1 = sorted((abs(d-1), abs(D-1)))
    ml, mh = F(7, 16)*a**4*d, F(7, 16)*A**4*D
    low = a**57*d**70*(e0*f0/((1+mh)*(1+mh*A)))**15
    high = A**57*D**70*(e1*f1/((1+ml)*(1+ml*a)))**15
    return low, high


def at_g15(H, d, side):
    a, A = a_bracket(H, d, side)
    return g15_box(a, A, d, d)


def upper_peak(H, side, threshold, subdivisions=64):
    """A global upper bound: every maximum occurs after d=8/11."""
    points = [F(8, 11)+F(3, 11)*i/subdivisions for i in range(subdivisions+1)]
    for d, D in zip(points, points[1:]):
        a = a_bracket(H, D, side)[0]
        A = a_bracket(H, d, side)[1]
        assert g15_box(a, A, d, D)[1] < threshold**15


def decimal_interval(lo, hi, root=1, digits=12):
    scale = 10**digits
    def lower(v):
        a, b = 0, 4*scale
        while b-a > 1:
            t = (a+b)//2
            if F(t, scale)**root <= v:
                a = t
            else:
                b = t
        return a
    low, high = lower(lo), lower(hi)
    return [low, high + int(F(high, scale)**root < hi)]


def maximum(side):
    H = F(1, 5)
    lo, hi = F(8, 11), F(99, 100)
    for _ in range(70):
        mid = (lo+hi)/2
        a, A = a_bracket(H, mid, side)
        m, M = F(7,16)*a**4*mid, F(7,16)*A**4*mid
        below = F(14,3)-M/(1+M)-A*M/(1+A*M)-mid/(1-mid)
        above = F(14,3)-m/(1+m)-a*m/(1+a*m)-mid/(1-mid)
        assert below > 0 or above < 0
        if below > 0:
            lo = mid
        else:
            hi = mid
    a = a_bracket(H, hi, side)[0]
    A = a_bracket(H, lo, side)[1]
    gl, gh = g15_box(a, A, lo, hi)
    return {'side': ['left','right'][side], 'h':'1/5',
            'A_1e12': decimal_interval(a, A),
            'd_1e12': decimal_interval(lo, hi),
            'G_1e12': decimal_interval(gl, gh, root=15)}


def main():
    # Boundary fold polynomial has exactly one sign change.
    p = lambda d: 138469703680*d**5 -19897995264*d**4-62426382592*d**3-510517280*d**2-1650459*d-70
    lo, hi = F(8,11), F(1)
    for _ in range(80):
        mid=(lo+hi)/2
        if p(mid)<0: lo=mid
        else: hi=mid
    assert p(lo)<0<p(hi)
    # Strict regular-value examples. At h=0 both negative lobes exceed 10^-4.
    for side in [0,1]:
        assert at_g15(F(0),F(1,2),side)[0]>F(1,10000)**15
        assert at_g15(F(0),F(4),side)[0]>F(1,10)**15
    # Four roots at (h,G)=(0,1/100).
    upper_peak(F(0),0,F(1,100))
    assert at_g15(F(0),F(3,4),1)[0]>F(1,100)**15
    # Two roots at (0,1/10), and one or three at h=6.
    upper_peak(F(0),1,F(1,10))
    upper_peak(F(6),1,F(1,10))
    assert at_g15(F(6),F(1,2),1)[0]>F(1,10000)**15
    assert at_g15(F(6),F(4),1)[0]>F(1,10)**15
    # Right h=0 entry A=4 occurs at a positive G below 10^-4, above 10^-10.
    d0, D0=F(0),F(1,100)
    for _ in range(90):
        mid=(d0+D0)/2
        if h(F(4),mid)>0:d0=mid
        else:D0=mid
    gl,gh=g15_box(F(4),F(4),d0,D0)
    assert F(1,10**10)**15<gl<gh<F(1,10000)**15
    result={'boundary_fold': {'d_1e12':decimal_interval(lo,hi),
                             'h_lower':str(h(F(4),hi)), 'h_upper':str(h(F(4),lo))},
            'global_lobe_maxima':[maximum(0),maximum(1)],
            'regular_count_examples':[
                {'h':'6','G':'1/10','count':1},
                {'h':'0','G':'1/10','count':2},
                {'h':'6','G':'1/10000','count':3},
                {'h':'0','G':'1/100','count':4},
                {'h':'0','G':'1/10000000000','count':5},
                {'h':'0','G':'1/10000','count':6}]}
    path=Path(__file__).with_name('fiber_certificates.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
