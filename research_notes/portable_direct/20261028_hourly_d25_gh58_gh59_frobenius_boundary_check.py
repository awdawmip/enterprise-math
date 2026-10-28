#!/usr/bin/env python3
"""Exact finite-field checks for GH-58/GH-59 (author-side, not admission).

All finite-field operations are integers modulo p. No floats, external packages,
or native Enterprise Math execution are involved.
"""
from math import comb


def primes_below(bound):
    sieve = bytearray(b"\x01") * bound
    sieve[:2] = b"\x00\x00"
    for i in range(2, int(bound ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:bound:i] = b"\x00" * len(sieve[i * i:bound:i])
    return (p for p in range(bound) if sieve[p])


def local_obstruction(p):
    """(A_p,B_p): w^(p-1) coefficient for initial (F(9), G(9))=(1,0),(0,1).

    The recursion builds the unique Taylor jet through degree p-1, using only the
    ordinary-point differential equation, not the globally truncated F polynomial.
    """
    inv = [0] * p
    inv[1] = 1
    for j in range(2, p):
        inv[j] = (p - (p // j) * inv[p % j] % p) % p
    inv2, inv8, inv72, inv144 = inv[2], inv[8], inv[72 % p], inv[144 % p]
    # Each vector: coefficients a_0,a_1 in the Taylor chart z=9+w.
    u0, u1 = 1, (-5 * inv144) % p
    v0, v1 = 0, inv144
    for n in range(p - 2):  # n=0,...,p-3: top coefficient is a_{p-1}.
        c = (n + 1) * ((34 * n + 29) * inv2 % p) % p
        d = ((n + 3 * inv8) % p) ** 2 % p
        invlead = inv72 * inv[n + 1] * inv[n + 2] % p
        u2 = -invlead * (c * u1 + d * u0) % p
        v2 = -invlead * (c * v1 + d * v0) % p
        u0, u1 = u1, u2
        v0, v1 = v1, v2
    return u1, v1


def source_ports(p):
    """Independent original GH-22 hypergeometric port recurrence at z=9."""
    m = (p - 3) // 8
    c, F, G = 1, 0, 0
    for r in range(m + 1):
        F = (F + c) % p
        G = (G + (16 * r + 5) * c) % p
        if r < m:
            c = c * (r - m) ** 2 * pow((r + 2*m + 2)*(r+1), -1, p) * 9 % p
    return F, G


def rational_legendre_G_modulus(m, N):
    """Compute t P'_{2m}(t)-P_{2m}(t) at t^2=8/9 modulo odd N coprime 3.

    Exact Legendre polynomial identity (integer binomials, denominators 2 and 3):
    P_n(t)=2^-n sum_{k=0}^{floor(n/2)} (-1)^k C(n,k) C(2n-2k,n)t^(n-2k).
    """
    n = 2*m
    assert N % 2 and N % 3
    t2 = 8 * pow(9, -1, N) % N
    value = sum((n-2*k-1) * (-1)**k * comb(n,k) * comb(2*n-2*k,n)
                * pow(t2,m-k,N) for k in range(m+1))
    return value * pow(2,-n,N) % N


def main():
    cases = [p for p in primes_below(10000) if p >= 11 and p % 8 == 3]
    branch_11 = branch_19 = 0
    for p in cases:
        A, B = local_obstruction(p)
        F, G = source_ports(p)
        assert (A, B) != (0, 0), (p, "zero obstruction")
        assert (A*F + B*G) % p == 0, (p, "wrong kernel")
        # A=0/B!=0 selects G=0; B=0/A!=0 selects F=0.
        if p % 24 == 11:
            assert (A, B, F, G)[0] == 0 and B != 0 and F != 0 and G == 0, p
            branch_11 += 1
        else:
            assert p % 24 == 19 and A != 0 and B == 0 and F == 0 and G != 0, p
            branch_19 += 1
    assert len(cases) == 310 and (branch_11, branch_19) == (155, 155)

    # A local jet with initial (F(9),G(9))=(1,1) obeys all low-order ODE
    # coefficients, yet violates the first obstructed Frobenius coefficient.
    A11, B11 = local_obstruction(11)
    assert (A11, B11) == (0, 7)
    assert (A11+B11) % 11 == 7

    # Composite extrapolation is genuinely false even when 2 and 3 are units.
    witness = rational_legendre_G_modulus(37, 299)
    assert witness == 250, witness

    print('PASS_GH58_GH59_FROBENIUS_KERNEL',len(cases),'primes; class11',branch_11,'class19',branch_19)
    print('SAMPLE p=11: A=0 B=7; (F,G)=(1,1) has terminal obstruction 7')
    print('COMPOSITE_BOUNDARY m=37 N=299: derivative observer =', witness, 'mod 299 (nonzero)')
    for p in [11,19,43,59,67,83]:
        print('CASE', p, 'A,B=',local_obstruction(p), 'F,G=',source_ports(p))

if __name__ == '__main__':
    main()
