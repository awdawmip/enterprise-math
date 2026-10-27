#!/usr/bin/env python3
"""Author-side exact Z/(p^3) checks of the two distinct D25 weighted sums.
No native CM / driver evidence; no floating point arithmetic.
"""
from math import comb, factorial, isqrt


def is_prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def window(p: int) -> range:
    m = (p - 1) // 6
    return range(4*m + 1, (3*p - 1) // 4 + 1)


def s_exact_mod(p: int, k: int) -> int:
    mod = p**3
    return ((8*k + 1)*comb(4*k, 2*k)*comb(2*k,k)**2*pow(2304, -k, mod)) % mod


def direct_tail(p: int) -> int:
    # Independent integer/binomial construction, divide by p^2 only after checking.
    mod = p**3
    values = [s_exact_mod(p,k) for k in window(p)]
    assert all(t % (p**2) == 0 for t in values)
    return (sum(values) % mod)//(p**2)


def factorial_tail(p: int) -> int:
    # Second computation, one p-adic factorial reduction of each high summand.
    return sum(2*(8*k+1)*factorial(4*k-2*p)
               * pow(factorial(k), -4, p)*pow(2304,-k,p)
               for k in window(p)) % p


def reflected_tail(p: int) -> int:
    # Wilson/Fermat with j=p-1-k, complementary factorial remains <p.
    m = (p-1)//6
    return sum(2*(8*j+7)*pow(2304,j,p)*pow(factorial(j),4,p)
               *pow(factorial(4*j-6*m+2),-1,p)
               for j in range(3*m//2,2*m)) % p


def weighted_sums(p: int) -> tuple[int,int,int,int]:
    # Modular exact rational-coefficient recurrences (independent of binomial path).
    mod=p**3
    inv_w=pow(36,-1,mod)
    inv_s=pow(288,-1,mod)
    wa=sa=1
    W=S=core=0
    m=(p-1)//6
    for k in range(p):
        term_w=(6*k+1)*wa%mod
        term_s=(8*k+1)*sa%mod
        W=(W+term_w)%mod
        S=(S+term_s)%mod
        if k<=4*m:
            core=(core+term_w-term_s)%mod
        else:
            assert term_w==0, (p,k,'W extra')
            if k>=(3*p+3)//4:
                assert term_s==0, (p,k,'S high')
        if k+1<p:
            d=pow(k+1,-3,mod)
            wa=(wa*(2*k+1)*(3*k+1)*(3*k+2)*inv_w*d)%mod
            sa=(sa*(4*k+1)*(2*k+1)*(4*k+3)*inv_s*d)%mod
    return W,S,core,(W-S)%mod


def run() -> None:
    primes=[p for p in range(7,998) if p%6==1 and is_prime(p)]
    assert len(primes)==80
    exceptional=[]
    for p in primes:
        a,b,c=direct_tail(p),factorial_tail(p),reflected_tail(p)
        assert a==b==c,(p,a,b,c)
        if a==0: exceptional.append(p)
    assert exceptional==[181],exceptional
    targets=[7,13,19,31,37,43,61,67,73,103,181,211,373,733]
    for p in targets:
        t=reflected_tail(p)
        W,S,D,diff=weighted_sums(p)
        assert (D-p*p*t)%p**3==diff,(p,D,t,diff)
        # Both exact summands are distinct; the previously established bridge is a test, not this theorem.
        assert diff==0,(p,diff)
        assert W==S==p,(p,W,S)  # all selected p=1 mod3
        print(f'p={p:<3} tail=[{window(p).start},{window(p).stop-1}] T={t:<3} D={D:<9} W-S={diff}')
    print(f'PASS: {len(primes)} p=6m+1 primes <=997, three independent T computations; T==0 only at p=181 in this finite set')
    print('PASS: 14 selected full binomial-ratio weighted-sum recurrences, exact mod p^3 sector split')


if __name__ == '__main__':
    run()
