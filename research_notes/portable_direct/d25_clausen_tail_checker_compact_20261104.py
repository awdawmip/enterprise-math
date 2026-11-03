"""D25 Clausen-tail certificate: exact modular integers, author-only."""
from math import comb


def primes(n):
    a = [True] * (n+1)
    a[:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            for j in range(i*i, n+1, i): a[j] = False
    return [p for p in range(5, n+1) if a[p]]


def coefficients(p, pairs, base):
    m = p**3
    a = [1]
    for k in range(p-1):
        num = 1
        for u, v in pairs: num *= u*k+v
        a.append(a[-1]*num*pow(base*(k+1)**2,-1,m)%m)
    return a


def square_tail(a, w, m):
    n = len(a)
    s0 = sum(a)%m
    s1 = sum(i*x for i,x in enumerate(a))%m
    full = (s0*s0+2*w*s0*s1)%m
    suffix = [0]*(n+1)
    weighted = [0]*(n+1)
    for j in range(n-1,-1,-1):
        suffix[j] = (suffix[j+1]+a[j])%m
        weighted[j] = (weighted[j+1]+j*a[j])%m
    tail = sum(a[i]*((1+w*i)*suffix[n-i]+w*weighted[n-i])
               for i in range(1,n))%m
    return tail, (full-tail)%m


def original(p, factors, base, weight):
    m = p**3
    v = 1
    total = 0
    for k in range(p):
        total = (total+(weight*k+1)*v)%m
        if k+1 < p:
            num = 1
            for u,t in factors: num *= u*k+t
            v = v*num*pow(base*(k+1)**3,-1,m)%m
    return total


P = primes(2000)
counts = [0,0,0,0]
for p in P:
    mod = p**3
    aa = coefficients(p, [(6,1),(3,1)], 36)
    cc = coefficients(p, [(8,1),(8,3)], 576)
    ta, wa = square_tail(aa,6,mod)
    tc, wc = square_tail(cc,8,mod)
    chi = 1 if p%3 == 1 else -1
    assert wa == original(p,[(2,1),(3,1),(3,2)],36,6)
    assert wc == original(p,[(4,1),(4,2),(4,3)],576,8)
    assert wa == wc == (p*chi)%mod
    if p%6 == 1:
        counts[0] += 1
        assert ta%(p*p)==0
    else:
        counts[1] += 1
        assert ta%(p*p) == p*((7*pow(2,-1,p))%p)
    if p%8 in (1,3):
        counts[2] += 1
        assert tc%(p*p)==0
    else:
        counts[3] += 1
        assert tc%(p*p)==p*((-chi)%p)
    if p in (13,19,373):
        db = sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)
                 for k in range(p))%mod
        dc = sum((8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,mod)
                 for k in range(p))%mod
        assert (db,dc)==(wa,wc)
        print('WITNESS',p,'T216',ta,'T2304',tc,'W',wa,'S',wc)
print('PASS',len(P),'primes [5,2000]; class_counts',counts)
print('The mod-p^2 tail signatures are finite observations, not proofs for all primes.')
