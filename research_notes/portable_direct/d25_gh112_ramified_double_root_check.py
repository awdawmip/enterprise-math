#!/usr/bin/env python3
"""Independent exact source recursion and tame ramification certificate, p=3347.

Only p-local arithmetic; this is a portable checker, not an Enterprise Math
native execution, publication, formal review, or proof checker.
"""
from math import comb

P = 3347
D = (P - 3) // 4
A = 9
P2 = P*P


def reflected_coefficients(modulus):
    h = [1]
    for j in range(D):
        num = (4*j + 3)**3
        den = (4*j + 4)*(4*j + 5)*(4*j + 6)
        h.append(h[-1]*num*pow(den, -1, modulus) % modulus)
    return h


def jet_coefficient(k, modulus, h):
    """Coefficient of t^k in R_p(9+t), from literal reflected source."""
    out = 0
    for j, hj in enumerate(h):
        n = D + 1 + j
        if k <= n:
            out += ((8*j + 5)*hj*pow(n, -1, modulus)
                    *comb(n,k)*pow(A, n-k, modulus))
    return out % modulus


def mul(x,y,modulus,c):
    a,b = x; d,e = y
    return ((a*d + P*c*b*e) % modulus, (a*e + b*d) % modulus)


def add(x,y,modulus):
    return ((x[0]+y[0]) % modulus, (x[1]+y[1]) % modulus)


def eval_poly_at_ramified(x, modulus, c, h):
    """Evaluate R_p(x) in (Z/p²)[pi]/(pi²-p*c)."""
    powers = (1,0)
    acc = (0,0)
    for n in range(2*D+2):
        if n >= D+1:
            j = n-D-1
            coeff = (8*j+5)*h[j]*pow(n,-1,modulus) % modulus
            acc = add(acc, (coeff*powers[0] % modulus,
                            coeff*powers[1] % modulus), modulus)
        powers = mul(powers,x,modulus,c)
    return acc


def main():
    h2 = reflected_coefficients(P2)
    h1 = [v % P for v in h2]
    r0 = jet_coefficient(0,P2,h2)
    r1 = jet_coefficient(1,P2,h2)
    v = 2*jet_coefficient(2,P,h1) % P
    w = 6*jet_coefficient(3,P,h1) % P
    assert r0 % P == 0 and r1 % P == 0 and v != 0
    u = (r0//P) % P
    b0 = (r1//P) % P
    c = (-2*u * pow(v,-1,P)) % P
    assert c % P != 0
    # pi^2=p*c; the sqrt(pi) residue slope is normalized to +/-1.
    b = -(b0*pow(c,-1,P) + w*pow(6,-1,P))*pow(v,-1,P) % P
    euler = pow(c,(P-1)//2,P)
    assert (r0,r1%P2,v,u,b0,c,euler)==(3969542,r1,v,1186,2098,1465,P-1)
    assert v==2331
    # First two ramified digits of two actual K-root branches.
    for s in (+1,-1):
        x = ((A + b*P*c)%P2,s%P2)
        residue = eval_poly_at_ramified(x,P2,c,h2)
        assert residue == (0,0), (s,residue)
        print('branch',s,'x_as_pair',x,'R_in_ring_mod_p2',residue)
    # Independent quotient calculation in (Z/p²)[z]/(z²-S*z+Q).
    # F_local(z) = (z-9)^2 - 2*b*p*c*(z-9) - p*c.
    S = (2*A + 2*b*P*c) % P2
    Q = (A*A + 2*A*b*P*c - P*c) % P2
    z_power = (1,0)  # coefficients of 1 and z in monomial remainder
    rem = (0,0)
    for n in range(2*D+2):
        if n >= D+1:
            j = n-D-1
            coeff = (8*j+5)*h2[j]*pow(n,-1,P2) % P2
            rem = ((rem[0] + coeff*z_power[0])%P2,
                   (rem[1] + coeff*z_power[1])%P2)
        # z*(v0 + v1*z) = -Q*v1 + (v0+S*v1)*z.
        z_power = ((-Q*z_power[1])%P2, (z_power[0]+S*z_power[1])%P2)
    assert rem == (0,0), rem
    print('quadratic_divisor_coefficients', (1,(-S)%P2,Q),
          'R_mod_quadratic',rem)
    # Both roots are quadratic-tame; Q_p(sqrt(p*c)) differs from Q_p(sqrt(p)).
    print('p',P,'d',D,'R(9)_mod_p2',r0,'Rprime(9)_mod_p2',r1)
    print('u',u,'b0',b0,'Rsecond_mod_p',v,'Rthird_mod_p',w)
    print('c',c,'legendre_c',-1 if euler==P-1 else 1,'b',b)
    print('PASS_GH112_TWO_RAMIFIED_LIFTS_MOD_PI4_AND_NONSQUARE_FIELD')


if __name__ == '__main__':
    main()
