#!/usr/bin/env python3
"""Author-side D25 mathematical evidence; no Source session, native benchmark or Result.

All arithmetic is exact, with denominators prime to p for n < p.  The test
uses a p-adic truncation determined by the *second* numerator zero; it does
not equate finite checks with a uniform supercongruence proof.
"""
from collections import defaultdict

LIMIT = 5000


def primes_below(limit):
    prime = bytearray(b"\x01") * limit
    prime[0:2] = b"\x00\x00"
    for q in range(2, int(limit**0.5) + 1):
        if prime[q]:
            prime[q*q:limit:q] = b"\x00" * len(range(q*q, limit, q))
    return [q for q in range(5, limit) if prime[q]]


def cutoffs(p):
    k1 = next((m*p - 1)//8 for m in (1, 3, 5, 7) if (m*p-1) % 8 == 0)
    k3 = next((m*p - 3)//8 for m in (1, 3, 5, 7) if (m*p-3) % 8 == 0)
    assert 0 <= min(k1, k3) < max(k1, k3) < p
    return k1, k3, max(k1, k3)


def coefficient_valuation(p, n):
    # Exact integer-factor valuation: denominator n! is a p-unit for n < p.
    v = 0
    for r in range(n):
        for factor in (8*r+1, 8*r+3):
            while factor % p == 0:
                v += 1
                factor //= p
    return v


def companion(p, power=2):
    k1, k3, b = cutoffs(p)
    mod = p**power
    x = total = 1
    derivative = 0
    for n in range(b):
        numerator = (8*n+1)*(8*n+3)
        denominator = 576*(n+1)**2
        x = (x * numerator * pow(denominator, -1, mod)) % mod
        total = (total+x) % mod
        derivative = (derivative + (n+1)*x) % mod
    return total, derivative


def independent_factorial(p, power=2):
    k1, k3, b = cutoffs(p)
    mod = p**power
    numerator = denominator = 1
    total = 0
    for n in range(b+1):
        if n:
            numerator = numerator * (8*n-7)*(8*n-5) % mod
            denominator = denominator * 576*n*n % mod
        total += numerator * pow(denominator, -1, mod)
    return total % mod


def legendre_minus_six(p):
    return (-1 if pow(-6 % p, (p-1)//2, p) == p-1 else +1)


def poly_mod_cm_check():
    """Verify the exact rational J-remainder using 36*t^2-36*t+1=0."""
    # 64(1+3t)^3 -(5121792t-143424)t(1-t)^2
    # = -64(36t^2-36t+1)(2223t^2-2286t-1).
    def mul(a, b):
        z = [0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): z[i+j] += x*y
        return z
    def sub(a,b):
        return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
                for i in range(max(len(a),len(b)))]
    lhs = [64*y for y in mul(mul([1,3],[1,3]),[1,3])]
    rhs = mul([ -143424,5121792],mul([0,1],mul([1,-1],[1,-1])))
    fact = [-64*y for y in mul([1,-36,36],[-1,-2286,2223])]
    assert sub(lhs,rhs)==fact
    # If J=5121792*t-143424, t+t'=1, t*t'=1/36:
    S = 5121792-2*143424
    P = 5121792**2//36-143424*5121792+143424**2
    assert S==4834944 and P==14670139392
    return S,P


def main():
    S,P=poly_mod_cm_check()
    print('CM24_EXACT_POLYNOMIAL x^2-%d*x+%d' %(S,P))
    grouped=defaultdict(list)
    higher=[]
    exceptional_exact=[]
    for p in primes_below(100):
        r1,r3,b=cutoffs(p)
        for n in range(p):
            baseline = (n>r1)+(n>r3)
            v = coefficient_valuation(p,n)
            assert v >= baseline
            if v != baseline:
                exceptional_exact.append((p,n,baseline,v))
            if n>b: assert v>=2
    assert exceptional_exact==[(5,4,1,2)], exceptional_exact
    for p in primes_below(LIMIT):
        k1,k3,b=cutoffs(p)
        K,D=companion(p)
        assert K==independent_factorial(p) if p in (5,7,11,13,17,19,23,29,37,43,47,61,73,109,373) else True
        phase = 'SPLIT' if legendre_minus_six(p)==1 else 'INERT'
        v = 0 if K%p else 1 if K%(p*p) else 2
        grouped[p%24].append((p,v,phase))
        if v==2 and p < 1000:
            K3,D3=companion(p,3)
            higher.append((p,K3//(p*p)))
    expected={1:(0,'SPLIT'),5:(0,'SPLIT'),7:(0,'SPLIT'),11:(0,'SPLIT'),
              13:(2,'INERT'),17:(1,'INERT'),19:(1,'INERT'),23:(2,'INERT')}
    for r in sorted(expected):
        values=grouped[r]
        wanted,sign=expected[r]
        bad=[(p,v,phase) for p,v,phase in values if (v,phase)!=(wanted,sign)]
        assert not bad,(r,bad)
        first=values[:4]
        print('class=%02d n=%d v_trunc=%d split=%s first=%s' %
              (r,len(values),wanted,sign,first))
    print('EXTRA_NUMERATOR_VALUATION_SMALL_P', exceptional_exact)
    print('SHARP_SAMPLE_K37_P3',companion(37,3)[0],
          'SHARP_SAMPLE_K23_P3',companion(23,3)[0])
    print('EXCEPTIONAL_HIGHER_V_P_<_1000',[(p,k2) for p,k2 in higher if k2==0])
    print('PASS_D25_CM24_PULLBACK_EIGHT_CLASS_P2',len(primes_below(LIMIT)),'primes')


if __name__ == '__main__': main()
