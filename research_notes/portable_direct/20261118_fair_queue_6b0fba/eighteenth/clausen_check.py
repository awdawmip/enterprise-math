"""Cross-check the closed singular coefficient against the frozen backward recurrence."""
from fractions import Fraction as F
from math import comb, isqrt
import json


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def residue(x, modulus):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def source(n):
    return (6*n+1)*comb(2*n-1, n)*(comb(3*n, n)//(2*n+1))


def backward(p, target_multiple=1):
    p2 = p*p
    H = (p-1)//2
    t = -target_multiple*pow(216, p-1, p2)*pow((2*p+1)*comb(2*p, p), -1, p2) % p2
    for n in range(p-1, H-1, -1):
        t = ((2*n+3)*t-source(n))*pow(108*n, -1, p2) % p2
    return t


def term(k, modulus):
    return comb(2*k, k)**2 * comb(3*k, k) * pow(216, -k, modulus) % modulus


def tail_sum(p):
    # Integer-binomial rendering; no Pochhammer ratio or backward recurrence.
    L = (p+1)//6
    return sum((3*j-1)*pow(-32, j, p)*comb(L,j)*comb(L+j-1,j)
               * pow(j*comb(2*j,j)**3,-1,p) for j in range(1,L+1))%p


def lower_core(p):
    """Compute the old prefix directly then independently reconstruct its p-linear strip."""
    H, r = (p-1)//2, (p-2)//3
    s, p2, p3 = H-1, p*p, p**3
    core = sum((6*k+1)*term(k,p3) for k in range(r+1))%p3
    b_r = term(r,p2)
    D = 1
    correction = 0
    strip = 0
    third = pow(3,-1,p2)
    for j in range(1,s-r):
        i = j-1
        # D_j=2^(-j) (-1/6)_j (-1/3)_j (j-1)! / (3 (1/3)_j^3).
        # At j=1 the zero from the old r+2/3 is divided out before reduction.
        shift = F(1,3) if i == 0 else i
        ratio = F(1,2)*(i-F(1,6))*(i-F(1,3))*shift/(i+F(1,3))**3
        D = D*residue(ratio,p2)%p2
        dH = 1/(i-F(1,6)) + 1/(i-F(1,3)) - 3/(i+F(1,3))
        if i:
            dH += F(1,i)
        correction = (correction+residue(dH,p))%p
        stripped = b_r*D*(1+p*third*correction)%p2
        actual = term(r+j,p3)
        assert actual % p == 0 and actual//p == stripped
        strip += (6*(r+j)+1)*stripped
    rebuilt = (core+p*strip)%p3
    direct = sum((6*k+1)*term(k,p3) for k in range(s))%p3
    assert rebuilt == direct
    denom = s*(2*s+1)*comb(2*s,s)
    return direct*pow(216,s-1,p3)*pow(denom,-1,p3)%p3


def run(p):
    p2, p3 = p*p, p**3
    H, L, s = (p-1)//2, (p+1)//6, (p-3)//2
    tau = (-1)**H
    chi = 1 if pow(6,H,p) == 1 else -1
    q2, q6 = (pow(2,p-1,p2)-1)//p,(pow(6,p-1,p2)-1)//p
    C = residue(1-2*q2+F(3*q6,2),p)
    Xi = tail_sum(p)
    bh = term(H,p3)
    assert bh%p == 0 and bh//p%p != 0
    upper = sum((6*(H+j)+1)*term(H+j,p3) for j in range(1,L+1))%p3
    assert upper == p*p*(bh//p)*Xi%p3
    U = pow(216,H-1,p2)*pow(H*comb(p-1,H),-1,p2)%p2
    assert U*(bh//p)%p2 == residue(tau*F(1+4*p,54),p2)
    assert U == residue(-tau*F(chi,108)*(1+p*C),p2)
    target = residue(tau*F(1,108)*(chi+4+p*(chi*C+10-2*Xi)),p2)
    assert target == backward(p)
    assert source(s)%p == 0
    rs = source(s)//p%p2
    assert rs == residue(tau*F(1,54)*(-F(72,35)-p*F(5427,1225)),p2)
    scalar = residue(tau*F(1,108)*(chi+F(284,35)+p*(chi*C+F(23104,1225)-2*Xi)),p2)
    assert scalar == (target-rs)%p2
    a_s = lower_core(p)
    B = (108*s*a_s+source(s)-p*target)%p3
    assert B == (108*s*a_s-p*scalar)%p3
    U3 = pow(216,H-1,p3)*pow(H*comb(p-1,H),-1,p3)%p3
    weighted = sum((6*k+1)*term(k,p3) for k in range(H+L+1))%p3
    E = 0
    summand = 1
    for k in range(H+L+1):
        E = (E + (6*k+1)*summand)%p3
        summand = -summand * (3*k+1)**3 * pow(27*(k+1)**3,-1,p3)%p3
    bridge = (2*weighted-E)%p3
    assert (E+2*p)%p3 == 0
    assert B == U3*(weighted+p)%p3 == U3*pow(2,-1,p3)*bridge%p3
    # A target of -2p gives a nonzero sensitivity check of the unit U.
    shifted = (108*s*a_s+source(s)-p*backward(p,target_multiple=2))%p3
    assert shifted == U3*(weighted+2*p)%p3 and (shifted-B)%p3 == U3*p%p3
    if p%24 in (17,23):
        assert B == 0  # Bounded regression only.
    without_tail = (B + residue(-tau*p*p*F(Xi,54),p3))%p3
    return dict(p=p, H=H, L=L, q2=q2, q6=q6, Xi=Xi, T_mod_p2=target,
                Rs_over_p_mod_p2=rs, singular_rhs_over_p_mod_p2=scalar, rhs_base_p_digits=[0,scalar%p,scalar//p],
                common_unit_mod_p3=U3, B_with_target_minus_2p_mod_p3=shifted,
                companion_mod_p3=a_s, B_mod_p3=B,
                B_if_Xi_omitted_mod_p3=without_tail)


def exact_bridge(p):
    M, H, s = (2*p-1)//3, (p-1)//2, (p-3)//2
    p3 = p**3
    b, sw = F(1), F(1)
    total = sw_total = F(0)
    prefix = F(0)
    for k in range(M+1):
        weighted = (6*k+1)*b
        total += weighted
        if k < s:
            prefix += weighted
        sw_total += (6*k+1)*sw
        b *= (k+F(1,2))*(k+F(1,3))*(k+F(2,3))/(2*(k+1)**3)
        sw *= -(k+F(1,3))**3/(k+1)**3
    a_s = 216**(s-1)*prefix / (s*(2*s+1)*comb(2*s,s))
    assert residue(a_s,p3) == lower_core(p)
    B = 108*s*a_s+source(s)-p*backward(p)
    assert residue(B,p3) == 0 and residue(2*total-sw_total,p3) == 0
    return dict(p=p,exact_core_numerator=a_s.numerator,
                exact_core_denominator=a_s.denominator,
                W_mod_p3=residue(total,p3), E_mod_p3=residue(sw_total,p3),
                B_mod_p3=residue(B,p3), C_mod_p3=residue(2*total-sw_total,p3))


if __name__ == "__main__":
    rows = [run(p) for p in range(11,601,6) if prime(p)]
    counts = dict(primes_checked=len(rows),
                  target_primes=sum(r['p']%24 in (17,23) for r in rows),
                  nonzero_Xi=sum(bool(r['Xi']) for r in rows),
                  nonzero_B=sum(bool(r['B_mod_p3']) for r in rows),
                  zero_first_coefficient=[r['p'] for r in rows if r['rhs_base_p_digits'][1] == 0])
    keys = (11,17,23,29,41,47,71,83,89)
    selected = [r for r in rows if r['p'] in keys or r['Xi'] == 0]
    print(json.dumps(dict(bounds="7 < p <= 600, p = 5 mod 6",counts=counts,
                          selected=selected, exact_bridge=[exact_bridge(p) for p in (17,23)]),indent=2))
