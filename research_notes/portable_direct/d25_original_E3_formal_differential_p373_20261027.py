#!/usr/bin/env python3
"""Exact original E3 formal differential at the fixed branch lambda=1/2.

Source Chisholm et al. (2013) Lemma 12, E3(t): y^2+xy+t*y/27=x^3,
local parameter z=-x/y. Not the native H0/B0 Frobenius experiment.
"""
from math import comb


def run(p):
    assert p % 24 in (13, 19) and p > 3
    modulus = p**3

    def q(a, b=0):
        return (a % modulus, b % modulus)

    def add(a, b):
        return q(a[0]+b[0], a[1]+b[1])

    def neg(a):
        return q(-a[0], -a[1])

    def sub(a, b):
        return add(a, neg(b))

    def mul(a, b):
        return q(a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])

    def smul(a, k):
        return q(a[0]*k, a[1]*k)

    def divunit(a, k):
        return smul(a, pow(k % modulus, -1, modulus))

    one, zero, T = q(1), q(0), q(0, 1)
    t = divunit(sub(q(2), T), 4)
    c = divunit(t, 27)
    d = [one, q(-2), one, smul(c, -4)]
    dt = [zero, zero, zero, divunit(q(-4), 27)]
    n = p-1
    h = [zero]*(n+1)
    g = [zero]*(n+1)
    h[0] = one

    # Exact ODE for H(z)=((1-z)^2-4c*z^3)^(-1/2) and g=partial_t H.
    for k in range(1, n+1):
        raw = zero
        grad = zero
        for j in range(1, min(3,k)+1):
            w = 2*k-j
            raw = add(raw, smul(mul(d[j], h[k-j]), w))
            grad = add(
                grad,
                smul(add(mul(d[j],g[k-j]),mul(dt[j],h[k-j])),w),
            )
        h[k] = neg(divunit(raw,2*k))
        g[k] = neg(divunit(grad,2*k))

    H, H_t = h[n], g[n]
    # Independent original-model exact finite polynomial of Lemma 12.
    H_comb, H_c = zero, zero
    power, prev = one, one
    for j in range(n//3+1):
        factor = comb(2*j,j)*comb(n-j,2*j)
        H_comb = add(H_comb,smul(power,factor))
        if j:
            H_c = add(H_c, smul(prev,factor*j))
        prev = power
        power = mul(power,c)
    H_t_comb = divunit(H_c,27)
    assert (H,H_t) == (H_comb,H_t_comb)
    assert H[0]%p == H[1]%p == 0

    H_over_p = q(H[0]//p,H[1]//p)
    H_lambda = divunit(mul(T,H_t),4)   # dt/dlambda = sqrt(2)/4
    naive_companion = add(H,smul(H_lambda,6)) # formal fixed-z jet only
    product = mul(H_over_p,naive_companion)
    return {
        "p":p,
        "modulus_p3":modulus,
        "H_original":H,
        "H_over_p_mod_p2":(H_over_p[0]%(p*p),H_over_p[1]%(p*p)),
        "partial_lambda_fixed_z":H_lambda,
        "naive_formal_companion":naive_companion,
        "naive_product_over_p_mod_p":(product[0]%p, product[1]%p),
        "crosscheck":"PASS: differential-ODE and independent exact Lemma-12 polynomial",
    }


if __name__ == "__main__":
    for prime in (13,19,37,43,61,67,211,373):
        witness = run(prime)
        assert witness["naive_product_over_p_mod_p"] == (prime-1,2)
        print(witness)
