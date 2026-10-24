#!/usr/bin/env python3
"""D25 original fixed-prime LOW-SEED parity certificate.
Author-side exact modular evidence, UNREVIEWED / NOT_ADMITTED; not native benchmark.
Works without source mutation; uses the frozen original factorial summand exactly.
"""
from fractions import Fraction
from math import factorial


def mod_fraction(x, p, exponent):
    """Reduce an integral rational x in Z_(p) modulo p**exponent."""
    mod = p**exponent
    a, b = x.numerator, x.denominator
    while b % p == 0:
        assert a % p == 0, "nonintegral p-adic rational"
        a //= p
        b //= p
    return (a % mod) * pow(b % mod, -1, mod) % mod


def valuation_fraction(x, p):
    if not x:
        return None
    a, b = x.numerator, x.denominator
    v = 0
    while a % p == 0:
        v += 1
        a //= p
    while b % p == 0:
        v -= 1
        b //= p
    return v


def original_terms(r, end):
    """Exact original WZ T(r,n), in rational numbers."""
    A = Fraction(factorial(6*r), 3**(6*r) * factorial(2*r)**3)
    out, R = [], Fraction(1)
    for n in range(end + 1):
        out.append(A * (6*n + 12*r + 1) * R)
        if n < end:
            R *= Fraction((4*r+2*n+1)*(3*n+1)*(3*n+2),
                          36*(n+1)*(2*r+n+1)*(4*r+n+1))
    return out


def fact_unit_table(p, exponent, max_n):
    mod = p**exponent
    U, val = [1], [0]
    u, v = 1, 0
    for n in range(1,max_n+1):
        k=n
        while k % p == 0:
            k //= p
            v += 1
        u=u*k % mod
        U.append(u);val.append(v)
    return U,val


def seed_modular_terms(p, exponent=3):
    assert p > 7 and p % 6 == 1
    m=(p-1)//6
    r=(m+1)//2
    nn=4*r
    mod=p**exponent
    M=12*r
    U,V=fact_unit_table(p,exponent,M)
    assert M < 2*p
    def item(n):
        indices=[6*r,4*r+2*n,3*n]
        denom=[2*r,n,n,2*r+n,2*r+n,4*r+n]
        v=sum(V[x] for x in indices)-sum(V[x] for x in denom)
        linear=6*n+12*r+1
        while linear%p==0:
            linear//=p
            v+=1
        numer=linear*U[6*r]*U[4*r+2*n]*U[3*n]
        den=pow(3,6*r,mod)*pow(216,n,mod)
        den*=U[2*r]*U[n]*U[n]*U[2*r+n]*U[2*r+n]*U[4*r+n]
        assert den%p != 0
        assert v>=0
        return (pow(p,v,mod)*numer*pow(den,-1,mod)) % mod,v
    return [item(n) for n in range(nn+1)]


def is_prime(n):
    if n<2: return False
    for k in range(2,int(n**0.5)+1):
        if n%k==0:return False
    return True


def run():
    checked=0; even=odd=0
    residues=[]
    for p in range(13,1001):
        if p % 6 != 1 or not is_prime(p):continue
        m=(p-1)//6
        r=(m+1)//2
        terms=seed_modular_terms(p)
        v=[x[1] for x in terms]
        if m%2==0:
            assert v==[1]+[0]*(4*r), (p,"even valuations",v)
            even+=1
        else:
            assert v==[0]*(4*r-2)+[1,2,2],(p,"odd valuations",v)
            odd+=1
            u=terms[4*r-2][0]
            # The two final tail terms have a universal relative coefficient.
            pair=(terms[4*r-1][0]+terms[4*r][0])%(p**3)
            rhs = (p*103*pow(1500,-1,p**3)*u)%(p**3)
            assert pair == rhs,(p,pair,rhs)
            if p==103:
                assert pair==0, pair
            else:
                assert pair%(p**3)!=0 and pair%(p*p)==0
            residues.append((p, (pair//(p*p))%p, (u//p)%p))
        if p<=211:
            ori=original_terms(r,4*r)
            assert [mod_fraction(x,p,3) for x in ori]==[x for x,_ in terms]
            assert [valuation_fraction(x,p) for x in ori]==v
            if p==103:
                pair_exact=ori[4*r-1]+ori[4*r]
                assert valuation_fraction(pair_exact,p)==3
                print('p=103: v_p(last_two_tail_sum)=', valuation_fraction(pair_exact,p),
                      'individual terms v=',valuation_fraction(ori[4*r-1],p),valuation_fraction(ori[4*r],p))
            if p==211:
                assert sum(x for x,_ in terms)%(p**3)==2938597
        checked+=1
    print('seed primes checked:',checked,'even m:',even,'odd m:',odd)
    print('odd sample p, pair/p^2 mod p, boundary/p mod p:')
    print(residues[:14]);print('PASS all parity, unit-factorial, universal tail-pair checks')

if __name__=='__main__': run()
