"""Exact checks of polynomial value functions on a p-adic residue ball."""
from collections import Counter
from itertools import product, combinations_with_replacement
from math import comb, factorial


def valuation(x, p):
    assert x > 0
    result = 0
    while x % p == 0:
        x //= p
        result += 1
    return result


def weight(j, p, s):
    return s*j + valuation(factorial(j), p)


def value(coefficients, x, modulus):
    acc = 0
    for c in reversed(coefficients):
        acc = (x*acc + c) % modulus
    return acc


def differences(values, modulus):
    out = []
    row = list(values)
    while row:
        out.append(row[0] % modulus)
        row = [(b-a) % modulus for a,b in zip(row, row[1:])]
    return tuple(out)


def statistic(coeff, p, s, a, k):
    modulus = p**k
    count = sum(weight(j,p,s)<k for j in range(len(coeff)))
    return differences([value(coeff,a+p**s*t,modulus) for t in range(count)], modulus)


def evaluate_differences(stat, t, modulus):
    return sum(c * comb(t,j) for j,c in enumerate(stat) if j<=t) % modulus


def child_stat(stat, p, s, b, k):
    modulus=p**k
    count=sum(weight(i,p,s+1)<k for i in range(len(stat)))
    return differences([evaluate_differences(stat,b+p*h,modulus) for h in range(count)],modulus)


def all_maps(p,s,a,k,d):
    modulus=p**k
    signatures={}
    for coeff in product(range(modulus), repeat=d+1):
        stat=statistic(coeff,p,s,a,k)
        for j,u in enumerate(stat):
            assert u%p**weight(j,p,s)==0
        direct=tuple(value(coeff,a+p**s*t,modulus) for t in range(p**(k-s)))
        assert all(evaluate_differences(stat,t,modulus)==v for t,v in enumerate(direct))
        if stat not in signatures:
            for b in range(p):
                assert child_stat(stat,p,s,b,k)==statistic(coeff,p,s+1,a+p**s*b,k)
            signatures[stat]=direct
        else:
            assert signatures[stat]==direct
    exponent=sum(max(0,k-weight(j,p,s)) for j in range(d+1))
    assert len(set(signatures.values()))==len(signatures)==p**exponent
    return len(signatures)


def declared_quadratics():
    # Monic quadratics above x^2 modulo 5, observed only on 0+5 Z_5 modulo 125.
    p,s,k=5,1,3
    modulus=p**k
    maps=set();roots=Counter()
    for B,C in product(range(25),repeat=2):
        coeff=(5*C,5*B,1)
        vals=tuple(value(coeff,5*t,modulus) for t in range(25))
        maps.add(vals)
        roots[tuple(i for i,x in enumerate(vals) if x==0)]+=1
    assert len(maps)==125
    return len(maps),len(roots)


def fewer_queries(p,s,a,k,d):
    modulus=p**k
    need=sum(weight(j,p,s)<k for j in range(d+1))
    domain=tuple(a+p**s*t for t in range(p**(k-s)))
    # For every possible transcript of zero answers of length need-1
    # (up to order), construct the witness that vanishes at exactly those probes
    # or possibly more, and differs somewhere in the required ball.
    seen=0
    for probes in combinations_with_replacement(domain,need-1):
        def witness(x):
            y=1
            for q in probes:
                y=y*(x-q)%modulus
            return y
        assert all(witness(q)==0 for q in probes)
        assert any(witness(x)!=0 for x in domain)
        seen+=1
    return need,seen


if __name__=='__main__':
    for example in [(2,0,0,2,3),(2,1,1,3,3),(3,0,0,2,2),(3,1,2,2,2)]:
        print(example, all_maps(*example), 'distinct value tables')
    print('monic quadratics, p=5, precision=3:', declared_quadratics(),
          '(value tables, zero-only subsets)')
    print('p=2, k=3, degree<=4:', fewer_queries(2,0,0,3,4),
          '(minimum, shorter probe multisets tested)')
    print('p=5, s=1, k=8, d>=6:',
          [8-weight(j,5,1) for j in range(7)],'digit lengths')

