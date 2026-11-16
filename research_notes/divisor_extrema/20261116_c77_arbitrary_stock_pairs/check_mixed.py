"""Fraction controls for coarse/physical width identities and edge exponents."""
from fractions import Fraction as Q
from itertools import product
from math import prod
import json


def coefficient(n, s, K):
    numerator = prod(range(n + K + 1, n + 4 * K + 1))
    denominator = 28 * Q(4*s+K-1, s+K-1) * prod(range(s+K,s+4*K))
    a = numerator / denominator
    rho = 4 * prod(Q(4*j+K,4*(j+K)) for j in range(s,n+1))
    return a, a/rho


def width(a, t, l, h):
    left, right = (1+t*l)/(1+a*l), (1+t*h)/(1+a*h)
    return max(left/right, right/left)-1


def main():
    counts = dict(coarse_secants=0, physical_secants=0, edge_slopes=0)
    for c, extra, gap in product((9,17,31,50),(1,2),(0,1,2)):
        v, C = c-gap, c+extra
        a, t = coefficient(c,v,5)
        upper, actual = coefficient(C,v,5)
        k, kp = upper/a, actual/t
        for l, h in ((Q(3,7),Q(5,9)),(Q(7,10),Q(4,5)),(Q(18,17),Q(11,10))):
            for lower_t in (0,t):
                assert a > lower_t
                coarse = width(upper,0,l,h)/(k*width(a,lower_t,l,h))
                assert coarse == a/(a-lower_t)*(1+a*l)/(1+k*a*l)*(1+lower_t*h)
                counts['coarse_secants'] += 1
            if upper > actual:
                physical = width(upper,actual,l,h)/width(a,t,l,h)
                assert physical == (k*a-kp*t)/(a-t)*(1+a*l)/(1+k*a*l)*(1+t*h)/(1+kp*t*h)
                counts['physical_secants'] += 1

    A, T, R = Q(1,112),Q(1,448),Q(4)
    assert Q(8,11)*Q(33,4)-9 == -3
    assert 12*Q(8,11)-9 == Q(-3,11)
    assert -Q(5,4)-Q(15,113)-Q(75,1796)+Q(15*32,112+32) > 0
    assert 32<4**4 and Q(9,4)*Q(-18,11)>-4
    for r,D,e in product((Q(101,100), Q(9,8),Q(2)),(Q(1,30),Q(1),Q(4)),(Q(0),Q(3,4))):
        k,kp=r**4,r**5
        H=(9-15/(1+k*A)-e)/(12-e)
        log_der_D=Q(9,4)*(H-1)
        assert log_der_D > -4
        first=(k*R-kp)/(R-1)
        term1=(kp-k)*Q(15,4)*R/(R-1)**2/first
        def log_der_factor(S, p, m):
            return (1/(1+m*S/D)-1/(1+S/D))*(p+log_der_D)
        # For a quotient (1+s)/(1+ms), s=A/D, logarithmic slope is
        # [1/(1+ms)-1/(1+s)]*(-p-D'/D).
        term2=-log_der_factor(A,Q(15),k)
        term3=-log_der_factor(T,Q(75,4),kp)
        assert min(term1,term2,term3)>0
        counts['edge_slopes']+=1
    return dict(**counts, split_k=32, minimum_coarse_log_derivative_at_k32=str(
        -Q(5,4)-Q(15,113)-Q(75,1796)+Q(10,3)),
        mixed_tail_exponents=['8/11','-3','-3/11'])


if __name__ == '__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
