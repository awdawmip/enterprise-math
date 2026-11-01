#!/usr/bin/env python3
"""GH-139: exact F_{p^2} tests for marked upper-half character moments."""
from math import comb

class Fp2:
    def __init__(self, p):
        self.p = p
        self.zero = (0, 0)
        self.one = (1, 0)
        self.rho = (0, 1)

    def scalar(self, n):
        return n % self.p, 0

    def add(self, a, b):
        return ((a[0] + b[0]) % self.p, (a[1] + b[1]) % self.p)

    def neg(self, a):
        return ((-a[0]) % self.p, (-a[1]) % self.p)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        p = self.p
        return ((a[0]*b[0] + 2*a[1]*b[1]) % p,
                (a[0]*b[1] + a[1]*b[0]) % p)

    def pow(self, a, n):
        assert n >= 0
        ans = self.one
        while n:
            if n & 1: ans = self.mul(ans, a)
            a = self.mul(a, a)
            n >>= 1
        return ans

    def inv(self, a):
        assert a != self.zero
        n = (a[0]*a[0] - 2*a[1]*a[1]) % self.p
        return self.mul((a[0] * pow(n, -1, self.p) % self.p,
                         -a[1] * pow(n, -1, self.p) % self.p), self.one)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def chi(self, a):
        return self.pow(a, (self.p*self.p-1)//2)


def roots_original(p, F):
    assert p >= 11 and p % 8 == 3
    ip = lambda n: pow(n, -1, p)
    T = F.mul(F.rho, F.scalar(2*ip(3)))
    B = F.mul(F.add(F.one, T), F.scalar(ip(8)))
    if pow(6, (p-1)//2, p) == 1:
        eta = F.scalar(pow(6, (p+1)//4, p))
        u = (ip(4) + eta[0] * ip(12)) % p
    else:
        assert pow(3, (p-1)//2, p) == 1
        eta = (0, pow(3, (p+1)//4, p))
        t = F.div(F.rho, eta)
        assert t[1] == 0
        u = (ip(4) - t[0] * ip(2)) % p
    assert F.mul(eta, eta) == F.scalar(6)
    s = F.div(F.sub(F.rho, F.one), eta)
    alpha = F.mul(F.add(F.neg(F.one), s), F.scalar(ip(2)))
    beta = F.mul(F.sub(F.neg(F.one), s), F.scalar(ip(2)))
    for x in (alpha, beta):
        assert F.add(F.add(F.mul(x, x), x), B) == F.zero
    assert alpha != beta
    norm = (alpha[0]*alpha[0] - 2*alpha[1]*alpha[1]) % p
    assert norm == (2 * u * u) % p and u != 0
    assert F.chi(alpha) == F.chi(beta) == F.scalar(-1)
    return B, T, alpha, beta


def moment_direct(F, B, max_t):
    p = F.p
    totals = [F.zero for _ in range(max_t + 1)]
    roots = 0
    for a in range(p):
        for b in range(p):
            x = (a, b)
            g = F.add(F.add(F.mul(x, x), x), B)
            if g == F.zero:
                roots += 1
                continue
            w = F.chi(x)
            if max_t:
                inv_g = F.inv(g)
            for t in range(max_t+1):
                totals[t] = F.add(totals[t], w)
                if t != max_t: w = F.mul(w, inv_g)
    return totals, roots


def moment_partial_fraction(F, alpha, beta, t):
    p = F.p
    e = (p*p-1)//2
    if t == 0:
        return F.neg(F.add(F.chi(alpha), F.chi(beta)))
    result = F.zero
    for a, b in ((alpha, beta), (beta, alpha)):
        delta = F.sub(a, b)
        for j in range(1, t+1):
            coef = (-1)**(t-j)*comb(2*t-j-1, t-j)
            c = F.mul(F.scalar(coef), F.inv(F.pow(delta, 2*t-j)))
            L = F.neg(F.mul(F.scalar(comb(e, j)), F.pow(a, e-j)))
            L = F.sub(L, F.div(F.chi(b), F.pow(F.sub(b, a), j)))
            result = F.add(result, F.mul(c, L))
    return result


def test_original():
    runs = 0
    for p in (11,19,43,59,67,83,107):
        F = Fp2(p)
        B, T, a, b = roots_original(p,F)
        direct, num_roots = moment_direct(F, B, 3)
        assert num_roots == 2
        expect = [F.scalar(2), F.mul(F.scalar(-72), T),
                  F.scalar(7308), F.mul(F.scalar(-903312), T)]
        assert direct == expect, (p, direct, expect)
        assert expect[1] == F.mul(F.scalar(-48),F.rho)
        assert expect[3] == F.mul(F.scalar(-602208),F.rho)
        for t in range(4):
            assert moment_partial_fraction(F,a,b,t) == direct[t], (p,t)
            runs += 1
    print('PASS_GH139_ORIGINAL_DIRECT_CHAR_SUM_AND_ROOT_RESOLVENT', 'prime_cases=7', 'moment_cases='+str(runs))


def test_general_split():
    runs = 0
    for p in (11,19,43):
        F = Fp2(p)
        a,b = F.scalar(2), F.scalar(-3)
        B = F.scalar(-6)
        assert F.sub(F.add(a,b), F.scalar(-1)) == F.zero
        direct, num_roots = moment_direct(F,B,5)
        assert num_roots == 2
        for t in range(6):
            assert moment_partial_fraction(F,a,b,t) == direct[t], (p,t,direct[t])
            runs += 1
        assert direct[0] == F.scalar(-2)
    print('PASS_GH139_GENERAL_SPLIT_RESOLVENT','prime_cases=3','moment_cases='+str(runs))


def test_p3347_no_full_enumeration():
    p=3347
    F=Fp2(p)
    B,T,a,b = roots_original(p,F)
    check = [moment_partial_fraction(F,a,b,t) for t in range(4)]
    expect = [F.scalar(2),F.mul(F.scalar(-48),F.rho),F.scalar(7308),F.mul(F.scalar(-602208),F.rho)]
    assert check == expect
    print('P3347_EXACT', 'B='+str(B),'root='+str(a),'moments='+str(check))
    print('PASS_GH139_P3347_ROOT_NORM_AND_FOUR_UPPER_MOMENTS_NO_Q_ENUMERATION')

if __name__ == '__main__':
    test_original()
    test_general_split()
    test_p3347_no_full_enumeration()
    print('PASS_GH139_ALL_EXACT')
