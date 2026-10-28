#!/usr/bin/env python3
"""GH-34/GH-35 exact prime-field checks; standard library only.

All divisions use modular inverses of verified nonzero factors. The check is
finite evidence; it does not replace the general proofs in the companion note.
"""
from math import isqrt


def primes_under(bound):
    return [p for p in range(11, bound) if all(p % k for k in range(2, isqrt(p) + 1))]


def inv(x, p):
    x %= p
    assert x != 0, (p, x)
    return pow(x, -1, p)


def gauss_and_clausen(p):
    assert p % 8 == 3
    m, d = (p - 3) // 8, (p - 3) // 4
    f = [1]
    for r in range(m):
        f.append(f[-1] * (r - m) ** 2 * inv((2 * m + 2 + r) * (r + 1), p) % p)
    h = [1]
    for r in range(d):
        h.append(h[-1] * (4 * r + 3) ** 3 * inv((4 * r + 4) * (4 * r + 5) * (4 * r + 6), p) % p)
    square = [sum(f[i] * f[s - i] for i in range(len(f))
                  if 0 <= s - i < len(f)) % p for s in range(d + 1)]
    assert h == square, (p, 'Clausen-square')
    z = 9
    F = sum(f[r] * pow(z, r, p) for r in range(m + 1)) % p
    Fprime = sum(r * f[r] * pow(z, r - 1, p) for r in range(1, m + 1)) % p
    K = sum(h[r] * pow(z, r, p) for r in range(d + 1)) % p
    Kprime = sum(r * h[r] * pow(z, r - 1, p) for r in range(1, d + 1)) % p
    H = sum((8 * r + 5) * h[r] * pow(z, r, p) for r in range(d + 1)) % p
    assert K == F * F % p and Kprime == 2 * F * Fprime % p
    assert H == (16 * z * Fprime + 5 * F) * F % p
    if p % 24 == 19:
        assert F == K == Kprime == H == 0
        assert Fprime != 0
        Ksecond = sum(r * (r - 1) * h[r] * pow(z, r - 2, p)
                      for r in range(2, d + 1)) % p
        assert Ksecond == 2 * Fprime ** 2 % p and Ksecond != 0
    return (F, Fprime, K, H)


def finite_residue_branches(p, z):
    """GH-35 three-polynomial formula, independent recurrences for k and h."""
    assert p % 4 == 3 and p > 3 and z % p not in (0, 1)
    d, j0 = (p - 3) // 4, (p + 1) // 2
    # q_d = C_d/z**d. At denominator zeros, remove the 4*epsilon factor.
    q = 1
    for i in range(d):
        q = q * (4 * i + 1) ** 3 * inv((4*i+2)*(4*i+3)*(4*i+4),p) % p
    C_d = q * pow(z, d, p) % p
    alpha, log0 = 1, 0
    for i in range(j0):
        num = (4 * i + 1) % p
        assert num != 0
        factors = [(4 * i + b) % p for b in (2, 3, 4)]
        den = 1
        for v in factors:
            den = den * (4 if v == 0 else v) % p
        alpha = alpha * num**3 * inv(den,p) % p
        log0 = (log0 + 12 * inv(num,p)
                - sum(4 * inv(v,p) for v in factors if v)) % p
    k, h, harmonic = 1, 1, 0
    Q = K = H = Dh = 0
    for s in range(d + 1):
        z_s = pow(z,s,p)
        Q = (Q + (8*s+3)*k*z_s) % p
        K = (K + h*z_s) % p
        H = (H + (8*s+5)*h*z_s) % p
        Dh = (Dh + (8*s+5)*h*harmonic*z_s) % p
        if s < d:
            k = k * (4*s+2)**3 * inv((4*s+3)*(4*s+4)*(4*s+5),p) % p
            h = h * (4*s+3)**3 * inv((4*s+4)*(4*s+5)*(4*s+6),p) % p
            harmonic = (harmonic + 12 * inv(4*s+3,p) - 4*inv(4*s+4,p)
                        - 4*inv(4*s+5,p) - 4*inv(4*s+6,p)) % p
    single = 2 * C_d * z * Q % p
    double = alpha * pow(z,j0,p) * (log0*H+8*K+Dh) % p
    den = inv(z-1,p)
    A = alpha * pow(z,j0,p) * H * den % p
    B = (single+double)*den%p
    return dict(A=A,B=B,Q=Q,K=K,H=H,Dh=Dh,C_d=C_d,
                alpha=alpha,log0=log0,single=single,double=double)


def direct_laurent_cyclic(p,z):
    """Independent exact Laurent-jet traversal of the ungrouped cyclic sum."""
    d = (p-3)//4
    u, slope, poles = 1, 0, 0
    A = B = 0
    for j in range(3*d+3):
        f = (8*j+1)%p
        term = u*pow(z,j,p)%p
        if poles == 1:
            B = (B + f*term)%p
        elif poles == 2:
            A = (A + f*term)%p
            B = (B + term*(8+f*slope))%p
        if j == 3*d+2:
            break
        n = (4*j+1)%p
        assert n!=0
        factors = [(4*j+b)%p for b in (2,3,4)]
        den = 1
        for v in factors:
            if v == 0:
                poles += 1
                den = den*4%p
            else:
                den = den*v%p
        u = u*n**3*inv(den,p)%p
        slope = (slope+12*inv(n,p)-sum(4*inv(v,p) for v in factors if v))%p
    assert poles==2
    return A*inv(z-1,p)%p,B*inv(z-1,p)%p


def main():
    ps=[p for p in primes_under(2001) if p%8==3]
    targets=0
    cases=0
    for p in ps:
        gauss_and_clausen(p)
        for z in (2,9):
            result=finite_residue_branches(p,z)
            assert (result['A'],result['B'])==direct_laurent_cyclic(p,z),(p,z)
            if p%24==19 and z==9:
                targets+=1
                assert result['K']==result['H']==0
                shortened=(result['single']+result['alpha']*pow(9,(p+1)//2,p)*result['Dh']) * inv(8,p)%p
                assert shortened==result['B']
            cases+=1
    print('PASS_GH34_CLAUSEN_DOUBLE_ZERO',len(ps),'prime cases, target',targets)
    print('PASS_GH35_FIRST_RESIDUE_TWO_SOURCE_RECONSTRUCTION',cases,'(p,z) cases')
    for p in (19,43,67):
        d=finite_residue_branches(p,9)
        print('EXACT',p,'Q',d['Q'],'Dh',d['Dh'],'single',d['single'],
              'double',d['double'],'B',d['B'])


if __name__=='__main__':
    main()
