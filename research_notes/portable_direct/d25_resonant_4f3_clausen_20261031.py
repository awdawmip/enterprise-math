#!/usr/bin/env python3
"""Author-side exact finite-field verifier for D25 4F3 resonance/Clausen bridge.

No floating point, no native H0/B0 or Frobenius execution. Mathematical proofs
are in the accompanying report; finite checks are implementation evidence.
"""
from math import factorial


def primes(limit):
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[:2] = b'\x00\x00'
    for q in range(2, int(limit ** 0.5) + 1):
        if is_prime[q]:
            is_prime[q*q::q] = b'\x00' * ((limit-q*q)//q + 1)
    return [p for p in range(7, limit+1) if is_prime[p] and p % 6 == 1]


def polynomials(p):
    ell = (p-1)//6
    h = [1]
    for n in range(1, ell):
        num = n*(n-ell)*(n+ell)
        den = (n-3*ell)**3
        h.append(h[-1]*num*pow(den, -1, p) % p)

    g = [1]
    for n in range(1, ell+1):
        g.append(g[-1]*(n-1-ell)*(n-1-2*ell)*pow(n*n, -1, p) % p)

    c = [1]
    for n in range(1, 2*ell+1):
        c.append(c[-1]*(2*n-1)*(3*n-2)*(3*n-1)*pow(18*n**3, -1, p) % p)

    H = h + [0]*(p-len(h))
    J = [0]*p
    for r, value in enumerate(c):
        J[3*ell+r] = value
    return ell, H, J, g, c


def L4_coeff(f, n, ell, p):
    curr = f[n] if n < len(f) else 0
    prev = f[n-1] if n-1 < len(f) else 0
    return (n*(n-3*ell)**3*curr - n*n*(n-ell)*(n+ell)*prev) % p


def L3_coeff(f, n, p):
    curr = f[n] if n < len(f) else 0
    prev = f[n-1] if n-1 < len(f) else 0
    # theta^3-z(theta+1/2)(theta+1/3)(theta+2/3)
    return (18*n**3*curr - (2*n-1)*(3*n-2)*(3*n-1)*prev) % p


def jets_at_half(poly, p):
    z = pow(2, -1, p)
    power = 1
    vals = [0, 0, 0]
    for n, co in enumerate(poly):
        term = co*power % p
        vals[0] = (vals[0]+term) % p
        vals[1] = (vals[1]+2*n*term) % p
        vals[2] = (vals[2]+4*n*(n-1)*term) % p
        power = power*z % p
    return tuple(vals)


def evaluate(poly, z, p):
    val = 0
    for co in reversed(poly):
        val = (val*z+co)%p
    return val


def run(limit=5000):
    test_primes = primes(limit)
    frozen_count = 0
    coeff_checks = 0
    full_clausen_checks = 0
    first_digit_checks = 0
    anchors = {}
    for p in test_primes:
        ell, H, J, g, c = polynomials(p)
        assert len(H) == len(J) == p
        assert H[0] == J[3*ell] == 1
        assert H[ell:] == [0]*(p-ell)
        assert all(not J[n] for n in list(range(3*ell))+list(range(5*ell+1,p)))
        assert c[-1] != 0
        for n in range(1, p+1):
            assert L4_coeff(H,n,ell,p) == 0, (p,n,'H')
            assert L4_coeff(J,n,ell,p) == 0, (p,n,'J')
        for n in range(1, p+1):
            assert L3_coeff(c,n,p) == 0, (p,n,'Clausen')
        coeff_checks += p

        # Evaluations of the Clausen polynomial identity at four independent points.
        for z in (0, 1, pow(2,-1,p), 2):
            assert evaluate(c,z,p) == evaluate(g,z,p)**2 % p, (p,z)

        # Full coefficient-wise direct convolution for a bounded independent subset.
        if p <= 500 or p in (373, 1327):
            conv = [0]*(2*ell+1)
            for i, a in enumerate(g):
                for j, b in enumerate(g):
                    conv[i+j] = (conv[i+j] + a*b) % p
            assert conv == c, p
            full_clausen_checks += 1

        H0,H1,H2 = jets_at_half(H,p)
        J0,J1,J2 = jets_at_half(J,p)
        g0,g1,g2 = jets_at_half(g,p)
        assert J0 == pow(2,-3*ell,p)*g0*g0 % p
        assert J1 == pow(2,-3*ell,p)*(6*ell*g0*g0+2*g0*g1) % p
        # Test exact signed readout relation with original low-range 216 coefficients.
        inv2pow = pow(2,-3*ell,p)
        low_weighted = sum((6*r+1)*c[r]*pow(2,-r,p) for r in range(2*ell+1))%p
        assert (4*J0+3*J1)%p == inv2pow*low_weighted%p
        if low_weighted == 0:
            first_digit_checks += 1

        if p % 24 in (13,19):
            frozen_count += 1
            assert g0 == 0, (p,'CM root')
            assert g1 != 0, (p,'CM root not simple')
            assert J0 == J1 == 0
            assert J2 == (2*inv2pow*g1*g1)%p
            assert J2 != 0
            assert (4*J0+3*J1)%p == 0
        if p in (7,13,19,37,157,373,1327):
            K = (pow(2,3*ell,p)*pow(factorial(3*ell-1),2,p)
                 *pow(36*factorial(4*ell)*factorial(2*ell),-1,p))%p
            I = K*(4*H0+3*H1)%p
            anchors[p] = {
                'ell':ell, 'G_half':g0, 'Gprime_half':g1,
                'J_doubleprime_half':J2, 'H_weighted':(4*H0+3*H1)%p,
                'K':K, 'I':I
            }
    assert len(test_primes)==330 and frozen_count==166
    assert {p:anchors[p]['I'] for p in (7,13,19,37,157,373,1327)} == {
        7:5, 13:10, 19:9, 37:20, 157:98, 373:266, 1327:1070}
    assert anchors[373]['Gprime_half'] == 215
    assert anchors[373]['J_doubleprime_half'] == 54
    assert anchors[373]['H_weighted'] == 217
    print('PRIMES',len(test_primes),'TARGET_CLASSES',frozen_count)
    print('L4_AND_L3_COEFFICIENT_CHECKS',coeff_checks,'FULL_CLAUSEN_CONVOLUTIONS',full_clausen_checks)
    print('FIRST_DIGIT_ZERO_SAMPLE_COUNT',first_digit_checks)
    for p,rec in sorted(anchors.items()):
        print('ANCHOR',p,rec)
    print('PASS_D25_RESONANT_4F3_CLAUSEN_JET_KERNEL_EXACT')


if __name__ == '__main__':
    run()
