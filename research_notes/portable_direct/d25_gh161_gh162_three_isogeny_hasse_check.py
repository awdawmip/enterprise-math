#!/usr/bin/env python3
"""Exact finite-field checks for the marked 3-isogeny Hasse-jet theorem.

This is an author-side checker, not a native D25 divided-power experiment.
No floating point arithmetic or external packages are used.
"""
from math import comb

PRIMES = [11, 19, 43, 59, 67, 83, 107, 131, 139, 163, 179,
          211, 227, 251, 283, 307, 331, 347, 379, 3347]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** .5) + 1))


class Fp2:
    """F_p[rho] where rho**2=2; p=3 mod 8."""
    def __init__(self, p):
        self.p = p
        self.zero = (0, 0)
        self.one = (1, 0)
        self.rho = (0, 1)

    def n(self, a, b=0):
        return a % self.p, b % self.p

    def add(self, x, y):
        return self.n(x[0] + y[0], x[1] + y[1])

    def neg(self, x):
        return self.n(-x[0], -x[1])

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        return self.n(x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

    def scal(self, x, n):
        return self.n(n*x[0], n*x[1])

    def inv(self, x):
        norm = (x[0]*x[0] - 2*x[1]*x[1]) % self.p
        if norm == 0:
            raise ZeroDivisionError(x)
        t = pow(norm, -1, self.p)
        return self.n(x[0]*t, -x[1]*t)

    def div(self, x, y):
        return self.mul(x, self.inv(y))

    def pow(self, x, n):
        if n < 0:
            return self.pow(self.inv(x), -n)
        y = self.one
        while n:
            if n & 1:
                y = self.mul(y, x)
            x = self.mul(x, x)
            n >>= 1
        return y

    def poly_hasse(self, b):
        n = (self.p - 1)//2
        h = self.zero
        hprime = self.zero
        powers = self.one
        prev = self.one
        for k in range(n//2 + 1):
            coeff = comb(n, 2*k)*comb(2*k, k)
            h = self.add(h, self.scal(powers, coeff))
            if k:
                hprime = self.add(hprime, self.scal(prev, k*coeff))
            prev, powers = powers, self.mul(powers,b)
        return h, hprime


def eval_mark(p):
    assert prime(p) and p % 8 == 3 and p >= 11
    f = Fp2(p)
    inv = lambda i: pow(i, -1, p)
    b = f.n(inv(8), inv(12))
    bs = f.sub(f.n(inv(4)), b)
    r = f.n(-inv(3), -inv(4))
    assert f.sub(f.pow(r, 4), f.pow(r, 4)) == f.zero
    # The 3-division polynomial has a simple root at r0.
    poly = f.sub(f.add(f.add(f.scal(f.pow(r, 4), 3),
                                 f.scal(f.pow(r,3), 4)),
                                 f.scal(f.mul(b, f.pow(r,2)),6)),f.pow(b,2))
    assert poly == f.zero, (p,'psi3',poly)
    pr = f.add(f.add(f.scal(f.pow(r,3),12),f.scal(f.pow(r,2),12)),
               f.scal(f.mul(b,r),12))
    pb = f.sub(f.scal(f.pow(r,2),6),f.scal(b,2))
    rp = f.neg(f.div(pb,pr))
    assert rp == f.n(6,3), (p,'root-derivative',rp)

    r2 = f.scal(f.sub(f.div(b,r),r),2)
    A = f.add(f.one,f.scal(r2,3))
    a4 = f.sub(b, f.scal(f.add(f.add(f.scal(f.pow(r,2),3),f.scal(r,2)),b),10))
    b3 = f.div(f.add(f.add(a4,f.scal(r2,2)),f.scal(f.pow(r2,2),3)),f.pow(A,2))
    assert A == f.n(3) and b3 == bs, (p,'marked-isogeny',A,b3)
    r2prime = f.scal(f.sub(f.div(f.sub(r, f.mul(b,rp)),f.pow(r,2)), rp),2)
    Aprime = f.scal(r2prime,3)
    a4prime = f.sub(f.one,
                    f.scal(f.add(f.add(f.scal(f.mul(r,rp),6),f.scal(rp,2)),f.one),10))
    num = f.add(f.add(a4, f.scal(r2,2)),f.scal(f.pow(r2,2),3))
    numprime = f.add(f.add(a4prime,f.scal(r2prime,2)),
                     f.scal(f.mul(r2,r2prime),6))
    b3prime = f.sub(f.div(numprime,f.pow(A,2)),
                    f.div(f.scal(f.mul(num,Aprime),2),f.pow(A,3)))
    assert Aprime == f.n(0,-72) and b3prime == f.one, (p,Aprime,b3prime)

    h,hprime = f.poly_hasse(b)
    hs,hps = f.poly_hasse(bs)
    assert hs == h and hps == f.neg(hprime), (p,'reflection')
    n=(p-1)//2
    lambda_hasse = f.pow(A,-n)
    expected_sign = f.n(1 if p%24==11 else -1)
    assert lambda_hasse == expected_sign, (p,lambda_hasse)
    assert hs == f.mul(lambda_hasse,h), (p,'isogeny-Hasse')
    lhs = f.mul(hps,b3prime)
    rhs = f.mul(lambda_hasse,
                f.sub(hprime, f.scal(f.mul(f.div(Aprime,A),h),n)))
    assert lhs == rhs, (p,'first jet covariance',lhs,rhs)
    if p%24==11:
        assert f.sub(hprime,f.scal(f.mul(f.rho,h),6)) == f.zero
        assert h != f.zero, (p,'ordinary nonzero')
    else:
        assert h == f.zero and hprime != f.zero, (p,'inert simple zero')
    if p==3347:
        assert h==f.n(783) and hprime==f.n(0,1351)
    return h, hprime, Aprime, b3prime


def generic_isogeny_tests(p):
    """Check every nondegenerate rational 3-subgroup x-coordinate over F_p."""
    n=(p-1)//2
    def H(b):
        return sum(comb(n,2*k)*comb(2*k,k)*pow(b,k,p)
                   for k in range(n//2+1))%p
    done=0; nonsquare=0
    for b in range(1,p):
        if 4*b%p == 1:
            continue
        for r in range(1,p):
            if (3*r**4+4*r**3+6*b*r*r-b*b)%p:
                continue
            r2=2*(b*pow(r,-1,p)-r)%p
            A=(1+3*r2)%p
            if not A:
                continue
            a4=(b-10*(3*r*r+2*r+b))%p
            b3=(a4+2*r2+3*r2*r2)*pow(A,-2,p)%p
            if b3*(1-4*b3)%p == 0:
                continue
            assert H(b3) == pow(A,-n,p)*H(b)%p, (p,b,r)
            done+=1
            if pow(A,n,p)==p-1 and H(b):
                nonsquare+=1
    assert done>0
    return done,nonsquare


def reflected_tail_at_nine(p):
    """Direct GH-153 reflected-R definition, independent of its f/K factorization."""
    m=(p-3)//8
    h=1
    rv=0
    rp=0
    for j in range(2*m+1):
        power=pow(9,2*m+j,p)
        term=((8*j+5)*h*power)%p
        rp=(rp+term)%p
        rv=(rv+term*9*pow(2*m+1+j,-1,p))%p
        if j<2*m:
            den=(4*j+4)*(4*j+5)*(4*j+6)%p
            h=h*pow(4*j+3,3,p)*pow(den,-1,p)%p
    return rv,rp


def main():
    for p in PRIMES:
        h,hp,ap,bp=eval_mark(p)
        rv, rpv=reflected_tail_at_nine(p)
        assert rpv==0, (p,'reflected derivative',rpv)
        print('marked',p,'R9',rv,'Rprime9',rpv,'branch','split' if p%24==11 else 'inert',
              'H',h,'Hprime',hp,'A_prime',ap,'B3_prime',bp)
    total = nontriv = 0
    for p in PRIMES[:6]:
        n,k=generic_isogeny_tests(p)
        print('generic',p,'checked',n,'nontrivial quadratic twist',k)
        total+=n; nontriv+=k
    assert nontriv>0
    print('PASS_GH161_GH162_THREE_ISOGENY_HASSE_JET_ALL_PRIME_STATIONARITY')
    print('marked_primes',len(PRIMES),'generic_3_isogenies',total,
          'nontrivial_quadratic_twist_checks',nontriv)

if __name__ == '__main__':
    main()
