"""Exact coefficientwise prefix filtration for weighted original-216 polynomials.
Scope: 5 <= p < 12000 exhaustive prime certificate, exact valuations only.
"""
from math import comb


def primes_below(limit):
    sieve=bytearray(b'\1')*limit
    sieve[:2]=b'\0\0'
    for i in range(2,int(limit**0.5)+1):
        if sieve[i]: sieve[i*i::i]=b'\0'*len(sieve[i*i::i])
    return [p for p in range(5,limit) if sieve[p]]


def coefficient_weight_valuation(p,n):
    result=2*n//p+3*n//p
    w=6*n+1
    while w%p==0:
        result+=1
        w//=p
    return result


def expected_prefix(p,k):
    if k==1: return (p-1)//3
    if k==2: return (p-1)//2
    if k==3: return 2*p//3
    if k in (4,5): return p-2 if p==5 else p-1
    if k==6: return p-1
    raise ValueError(k)


def main():
    primes=primes_below(12000)
    checks=0
    direct=[5,7,11,13,17,19,37,43,67,157,373]
    for p in primes:
        vals=[coefficient_weight_valuation(p,n) for n in range(p)]
        for k in range(1,7):
            rightmost=max(n for n in range(p) if vals[n]<k)
            assert rightmost==expected_prefix(p,k),(p,k,rightmost)
            checks+=1
        if p in direct:
            for n in range(p):
                x=(6*n+1)*comb(2*n,n)**2*comb(3*n,n)
                for k in range(1,7):
                    assert (x%p**k==0)==(vals[n]>=k),(p,n,k)
    print('PASS_D25_ALL_PRIME_SHARP_PRECISION_PREFIX_FILTRATION')
    print('primes',len(primes),'precision_endpoint_checks',checks)
    print('direct_integer_binomial_anchor_primes',direct)
    print('p373_q_for_k1_to_k6',[expected_prefix(373,k) for k in range(1,7)])
    print('p5_q_for_k1_to_k6',[expected_prefix(5,k) for k in range(1,7)])


if __name__=='__main__':
    main()
