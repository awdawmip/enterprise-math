"""Check the two raw center columns, their determinant and reduced-numerator gcd."""
from fractions import Fraction
from math import gcd, lcm, prod
from itertools import combinations_with_replacement
import json

def rising(value, length):
    return prod(range(value, value + length))

def raw_column(edges, tail):
    a, b = 1680, 1680 + tail
    for n, d in reversed(edges):
        a, b = d*b, d*b + n*a
    return a, b

def fraction_column(edges, tail):
    z = Fraction(1680, 1680+tail)
    for n, d in reversed(edges):
        z = 1/(1 + Fraction(n, d)*z)
    return z

def verify(c, landings):
    r = len(landings)
    w = landings[-1]
    Wnum = (w+2)*(w+3)*(w+4)
    edges = []
    for i, (old,v) in enumerate(zip((c,)+landings, landings)):
        k = 2*(r-i)+1
        n = (v+k-1)*rising(old+k+1, 3*k)
        d = 28*(4*v+k-1)*rising(v+k, 3*k)
        edges.append((n,d))
    d1 = edges[0][1]
    k1 = 2*r+1
    scale = rising(c+k1+1, 3*k1)
    Q = landings[0]+k1-1
    columns = []
    corrections = []
    numerators = []
    for k in [1,10]:
        z = fraction_column(edges,k*Wnum)
        a,b = raw_column(edges[1:],k*Wnum)
        columns.append((a,b))
        N,D = d1*b,Q*a
        obs = scale*z/(1-z)
        assert obs == Fraction(N,D)
        numerators.append(obs.numerator)
        corrections.append(gcd(N,D))
    (a,b),(a2,b2) = columns
    assert a*b2 - a2*b == 1680*9*Wnum*prod(-n*d for n,d in edges[1:])
    h = gcd(b,b2)
    L = lcm(*corrections)
    k = gcd((b//h)*(L//corrections[0]),(b2//h)*(L//corrections[1]))
    assert (L*L//prod(corrections)) % k == 0
    assert gcd(*numerators)*L == d1*h*k

if __name__ == '__main__':
    output = {}
    for r in range(1,13):
        count = 0
        for c in [3,4,5,6]:
            for ordered in combinations_with_replacement(range(2,c+1), r):
                verify(c, ordered[::-1])
                count += 1
        output[r] = count
    print(json.dumps({'depths_and_all_words':output,'total':sum(output.values())},indent=2))
