#!/usr/bin/env python3
"""Author-side exact modular test for D25/LIFT GH-41, GH-42.

This is a finite test over integers modulo p^2, NOT a formal proof or native X6 run.
All division is by explicit p-adic units. Python standard library only.
"""


def primes_below(n):
    composite = bytearray(n)
    for k in range(2, int(n**0.5) + 1):
        if not composite[k]:
            for j in range(k*k, n, k):
                composite[j] = 1
    return [k for k in range(7, n) if not composite[k] and k % 4 == 3]


def verify(p):
    assert p % 4 == 3 and p >= 7
    d = (p - 3) // 4
    modulus = p*p
    def invert(n):
        assert n % p != 0, (p, n, "nonunit denominator")
        return pow(n % modulus, -1, modulus)

    a = [1]
    beta = [1]
    c = [1]
    harmonic = [0]
    for r in range(d):
        a.append(a[-1] * (8*r+1)**2 * invert(16*(4*r+3)*(r+1)) % modulus)
        beta.append(beta[-1] * 16*(r+1)*(4*r+3) * invert((8*r+13)**2) % modulus)
        c.append(c[-1] * (4*r+1)**3 * invert((4*r+2)*(4*r+3)*(4*r+4)) % modulus)
        h = (4*invert(8*r+13) - invert(4*r+4) - invert(4*r+3)) % p
        harmonic.append((harmonic[-1] + h) % p)

    # GH-41: [u^n] of A V, including the constant and upper boundary.
    # A = u(D+3/4)(D+1) - (D+5/8)^2.
    affine_coeffs = []
    for n in range(d+2):
        v = 0
        if n <= d:
            v -= (8*n+5)**2 * invert(64) * beta[n]
        if n >= 1:
            v += n*(4*n-1) * invert(4) * beta[n-1]
        affine_coeffs.append(v % modulus)
    assert affine_coeffs[0] == (-25 * invert(64)) % modulus
    assert all(x == 0 for x in affine_coeffs[1:d+1])
    assert affine_coeffs[d+1] == p*(d+1)*invert(4)*beta[d] % modulus
    assert affine_coeffs[d+1] % p == 0
    assert (affine_coeffs[d+1] // p) % p != 0

    # GH-42: exact p-adic reversal jet, retaining ordered source indices.
    assert all((a[d-r] - a[d]*beta[r]*(1+p*harmonic[r])) % modulus == 0
               for r in range(d+1))

    u = invert(9)
    wmoment = mmoment = jmoment = direct_tail = 0
    for r in range(d):
        vr = wr = direct_fiber = 0
        for i in range(r+1):
            j = r-i
            z = beta[i]*beta[j]
            vr += z
            wr += z*(harmonic[i]+harmonic[j])
            direct_fiber += a[d-i]*a[d-j]
        vr %= modulus
        wr %= modulus
        upower = pow(u, r, modulus)
        mmoment = (mmoment + vr*upower) % modulus
        wmoment = (wmoment + (8*r+11)*vr*upower) % modulus
        jmoment = (jmoment + (8*r+11)*wr*upower) % modulus
        direct_tail = (direct_tail + (8*(2*d-r)+1)*direct_fiber*
                       pow(9, 2*d-r, modulus)) % modulus

    fermat_quotient = (pow(3,p-1,modulus)-1)//p
    tail_formula = a[d]**2*invert(9)*(
        -wmoment+p*(4*mmoment-jmoment-fermat_quotient*wmoment)) % modulus
    assert direct_tail == tail_formula

    # Rational Clausen coefficient equality through degree d, and the
    # full (not silently truncated) Gauss product, both reduced mod p^2.
    gauss = sum(v*pow(9,i,modulus) for i,v in enumerate(a)) % modulus
    gauss_weighted = sum((16*i+1)*v*pow(9,i,modulus)
                         for i,v in enumerate(a)) % modulus
    original = sum((8*i+1)*v*pow(9,i,modulus)
                   for i,v in enumerate(c)) % modulus
    assert (gauss*gauss_weighted-direct_tail-original) % modulus == 0
    restored = (gauss*gauss_weighted + a[d]**2*invert(9)*(
        wmoment+p*(fermat_quotient*wmoment-4*mmoment+jmoment))) % modulus
    assert original == restored
    return (p, original, direct_tail, wmoment % p, mmoment % p,
            jmoment % p, fermat_quotient % p)


def main():
    ps = primes_below(2000)
    results = [verify(p) for p in ps]
    assert len(results) == 154, len(results)
    print("PASS_GH41_REVERSE_GAUSS_AFFINE_BOUNDARY", len(results), "primes; p<2000, p=3 mod4")
    print("PASS_GH42_PADIC_REVERSAL_JET_FULL_TAIL", len(results), "primes; mod p^2")
    for item in results:
        if item[0] in (7,11,19,43,67,127):
            print("CERTIFICATE (p,T_mod_p2,E_mod_p2,W_mod_p,M_mod_p,J_mod_p,q_p3)=", item)

if __name__ == "__main__":
    main()
