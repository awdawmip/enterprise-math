"""C64: exact high-prefix gluing constants and three two-block TV responses."""
from fractions import Fraction as Q
from math import gcd, lcm, prod
import json


def integer_matrix(values):
    rationals = tuple(map(Q, values))
    d = lcm(*(v.denominator for v in rationals))
    raw = tuple(int(v*d) for v in rationals)
    common = gcd(*raw)
    return tuple(v//common for v in raw)


def times(left, right):
    a,b,c,d = left
    e,f,g,h = right
    return integer_matrix((a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))


def block(r, c, m):
    rates = Q(1,4), Q(1), Q(4)
    likelihoods = []
    for start, z in enumerate(rates):
        kappa = 2*r+1
        h = prod(j*z/(kappa+j*z) for j in range(c,c-m,-1))
        stock = c-m
        h *= r/(kappa+stock*z)
        h *= r/(kappa-1+stock*rates[min(start+1,2)])
        likelihoods.append(h)
    a,b,c = likelihoods
    return integer_matrix((0,7*a,b-c,7*a+c))


def tail(stock):
    l0,l1,l2 = [prod(j*z/(1+j*z) for j in range(stock,2,-1))
                for z in (Q(1,4),Q(1),Q(4))]
    return integer_matrix((-l2,l2,l1-l2,7*l0+l2))


def response(m2, m1):
    mat = times(tail(3-m2-m1), block(1,3-m2,m1))
    return times(mat, block(2,3,m2))


def determinant(m):
    p,q,h,t = m
    return abs(p*t-q*h)


def limits(m, n):
    weights = sorted(Q(n[3]+i*n[2], m[3]+i*m[2]) for i in (0,1))
    return [Q(determinant(m),determinant(n))*w*w for w in weights]


def check():
    unweighted = Q(377,378)
    for bound in (unweighted*Q(21,10)*600, unweighted*Q(21,10)**32*2,
                  unweighted*256*Q(99,100)):
        assert bound > 252
    assert Q(100*64**2*9,10*80*16) == 288
    assert Q(131,65)**3/16 < Q(3,5)
    assert Q(100*64**2,640)*Q(2,5) == 256
    assert 64**2*(3*64+4)//64 == 12544
    matrices = [response(*x) for x in [(1,0),(0,1),(0,0)]]
    ab, ac = (limits(m,matrices[0]) for m in matrices[1:])
    assert 14 < ab[0] < ab[1] < 16 < 23 < ac[0] < ac[1] < 25
    return dict(matrices=matrices,
                B_over_A=[str(x) for x in ab], C_over_A=[str(x) for x in ac],
                any_high_defect_gap='>252')

if __name__=='__main__':
    print(json.dumps(check(),indent=2))
