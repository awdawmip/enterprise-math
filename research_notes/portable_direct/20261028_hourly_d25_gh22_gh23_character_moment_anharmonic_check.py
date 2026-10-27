#!/usr/bin/env python3
"""Exact finite-field certificates for GH-22/GH-23, no floating-point arithmetic.
Author research only; not native Enterprise Math execution or formal acceptance.
"""
from itertools import permutations
from math import comb


def primes_below(n):
    flag = bytearray(b'\x01') * n
    flag[:2] = b'\x00\x00'
    for d in range(2, int(n ** 0.5) + 1):
        if flag[d]:
            flag[d*d:n:d] = b'\x00' * ((n - 1 - d*d)//d + 1)
    return [j for j in range(2, n) if flag[j]]


def hyper_channels(p):
    assert p >= 11 and p % 8 == 3
    m = (p-3)//8
    a, zpower, f, g = 1, 1, 0, 0
    for r in range(m+1):
        f = (f+a*zpower) % p
        g = (g+(16*r+5)*a*zpower) % p
        if r < m:
            a = a*(m-r)**2*pow((2*m+2+r)*(r+1), -1, p) % p
            zpower = zpower*9 % p
    return m, f, g


def binomial_channels(p, m):
    coeff = [comb(3*m+1, m-r)*comb(m, r) for r in range(m+1)]
    d = comb(3*m+1, m) % p
    assert d
    b = sum(coeff[r]*pow(9, r, p) for r in range(m+1)) % p
    bg = sum((16*r+5)*coeff[r]*pow(9, r, p) for r in range(m+1)) % p
    return d, b, bg


def character_channels(p, m):
    sf = sg = 0
    for x in range(p):
        chi = pow(x, (p-1)//2, p) # 0, +1 or -1 modulo p
        base = pow(x*(1+x), 3*m+1, p)
        sf += chi*base*pow(1+9*x, m, p)
        sg += chi*base*pow(1+9*x, m-1, p)*(5-9*x)
    return (-sf) % p, (-sg) % p


def cr(q, p):
    a,b,c,d = q
    # cross ratio (a-c)(b-d)/((a-d)(b-c)) on P^1(F_p)
    if a is None: return (b-d)*pow(b-c, -1, p)%p
    if b is None: return (a-c)*pow(a-d, -1, p)%p
    if c is None: return (b-d)*pow(a-d, -1, p)%p
    if d is None: return (a-c)*pow(b-c, -1, p)%p
    return (a-c)*(b-d)*pow((a-d)*(b-c), -1, p)%p


def stabilizer_size(p):
    assert p > 3
    quadruple = [None, 0, (-pow(9, -1, p))%p, (-1)%p]
    assert len(set(quadruple))==4
    invariant = cr(quadruple,p)
    assert invariant == 9%p
    return sum(cr(v,p)==invariant for v in permutations(quadruple))


def main():
    primes = [p for p in primes_below(2000) if p >= 11 and p%8 == 3]
    assert primes
    n_f = n_g = 0
    for p in primes:
        m, f, g = hyper_channels(p)
        d,b,bg = binomial_channels(p,m)
        sf,sg = character_channels(p,m)
        assert f*d%p == b == sf, ('F',p, f,d,b,sf)
        assert g*d%p == bg == sg, ('G',p,g,d,bg,sg)
        assert stabilizer_size(p)==4, ('support group',p)
        n_f += (p%24==19 and f==0)
        n_g += (p%24==11 and g==0)
    assert [(p, stabilizer_size(p)) for p in (5,7,17,73,11,19,43)] == [
        (5,8),(7,8),(17,8),(73,12),(11,4),(19,4),(43,4)]
    # Integer-only exact coefficient identity at z=9 and derivative weight.
    for m in range(1,30):
        coeff=[comb(3*m+1,m-r)*comb(m,r) for r in range(m+1)]
        assert sum(coeff[r]*9**r for r in range(m+1))==sum(
            comb(3*m+1,k)*sum(comb(m,j)*9**j for j in [m-k] if 0<=j<=m)
            for k in range(m+1))
        assert sum((16*r+5)*coeff[r]*9**r for r in range(m+1)) == \
            5*sum(coeff[r]*9**r for r in range(m+1)) + 16*sum(r*coeff[r]*9**r for r in range(m+1))
    print('PASS_GH22_EXACT_CHARACTER_SUM_TWO_DISTINCT_PORTS',len(primes),'primes p<2000, p%8=3')
    print('PASS_GH23_FOUR_POINT_STABILIZER_NO_CUBIC_MOBIUS',len(primes),'target primes; exceptions 5/7/17/73 classified')
    print('OBS_TARGET_BRANCHES',n_f,'F-zero and',n_g,'G-zero; finite samples only')
    for p in (11,19,43,59,67,73,139,163):
        if p%8==3:
            m, f, g=hyper_channels(p)
            d,b,bg=binomial_channels(p,m)
            print('CERT',{'p':p,'m':m,'F':f,'G':g,'D':d,'character_F':b,'character_G':bg,'mobius_support_group_order':stabilizer_size(p)})
        else: print('EXCEPTION',{'p':p,'mobius_support_group_order':stabilizer_size(p)})


if __name__=='__main__':main()
