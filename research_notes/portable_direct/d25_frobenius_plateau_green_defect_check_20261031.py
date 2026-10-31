"""Exact modular checks for the author-side D25 Green quotient/plateau theorem.

No float, no third-party package, no native Enterprise Math execution claim.
"""
from math import comb
from fractions import Fraction


def primes_up_to(n):
    a = bytearray(b'\x01') * (n + 1)
    a[:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if a[i]:
            a[i * i::i] = b'\x00' * ((n - i * i) // i + 1)
    return [i for i in range(n + 1) if a[i]]


def q_coeffs(l):
    return [(-1) ** j * comb(l, j) * comb(3 * l - j, l) for j in range(l + 1)]


def q_independent(l):
    # Direct substitution of G_l(1-y), avoiding the closed Vandermonde formula.
    u = [comb(l, i) * comb(2 * l, i) for i in range(l + 1)]
    return [(-1) ** j * sum(u[i] * comb(i, j) for i in range(j, l + 1))
            for j in range(l + 1)]


def source_coeffs(l, p, q, direct=False):
    # B(y)=(1-y)^(p-1) G_l(1-y), computed by convolution.
    a = [((-1) ** i * comb(p - 1, i)) % p if direct else 1 for i in range(p)]
    b = [0] * (p + l)
    for j, c in enumerate(q):
        for i, v in enumerate(a):
            b[i + j] = (b[i + j] + c * v) % p
    return b


def quotient(l, p, b):
    M = 3 * l
    q = 0
    for k, v in enumerate(b):
        if k != M:
            d = k - M
            w = (1 - pow(2, M - k, p)) * pow(d, -1, p)
            q = (q + v * w) % p
    return q


def paired_quotient(l, p, q):
    M = 3 * l
    baseline = sum((pow(2, j, p) - pow(2, -j, p)) * pow(j, -1, p)
                   for j in range(1, M + 1)) % p
    C = 0
    repair = 0
    for k in range(l):
        C = (C + q[k]) % p
        repair += (1-C) * pow(2, M-k-1, p) * pow(k-M, -1, p)
    return (baseline + repair) % p


def harmonic_gamma(l, p):
    M = 3 * l
    u = [comb(l, i) * comb(2*l, i) for i in range(l+1)]
    H = -sum(pow(j, -1, p) for j in range(1, M+1))
    for i in range(1, l+1):
        H += (-1 if i%2 else 1) * u[i] * pow(i * comb(M, i), -1, p)
    S = sum(u[i] * comb(p-1+i, M) for i in range(l+1))
    pp = p*p
    assert S % p == (-1)**l % p
    gamma = ((-1)**l * pow(18*S, -1, pp)) % pp
    inv18 = pow(18, -1, pp)
    delta = (gamma - inv18) % pp
    assert delta % p == 0
    return H % p, delta // p, S


def rational_check(l):
    p = 6*l+1
    q = q_coeffs(l)
    b = [0]*(p+l)
    for j,c in enumerate(q):
        for i in range(p):
            b[i+j] += c*((-1)**i)*comb(p-1,i)
    M=3*l
    T=sum((Fraction(1)-Fraction(2)**(M-k))*Fraction(bk,k-M)
          for k,bk in enumerate(b) if k!=M)
    S=sum(comb(l,i)*comb(2*l,i)*comb(p-1+i,M) for i in range(l+1))
    gamma=Fraction((-1)**l,18*S)
    r=(gamma-Fraction(1,18))*b[M]
    e=(gamma-Fraction(1,18))*T
    assert r == Fraction(1-(-1)**l*S,18)
    def reduce_mod_p2(x):
        return (x.numerator*pow(x.denominator,-1,p*p))%(p*p)
    # r and e are p-integral with first digit zero.
    assert reduce_mod_p2(r)%p==0
    assert reduce_mod_p2(e)%p==0
    return reduce_mod_p2(r)//p,reduce_mod_p2(e)//p


def run():
    for l in range(1, 15):
        assert q_coeffs(l)==q_independent(l)
    ps=[p for p in primes_up_to(1200) if p%6==1]
    anchors={7,13,19,37,67,373}
    witnesses={}
    for p in ps:
        l=(p-1)//6
        M=3*l
        q=q_coeffs(l)
        assert sum(q)==1
        b=source_coeffs(l,p,q,direct=p in anchors)
        C=0
        for k in range(l):
            C=(C+q[k])%p
            assert b[k]==C
            assert b[p+k]==(1-C)%p
        assert all(b[k]==1 for k in range(l,p))
        T=quotient(l,p,b)
        assert T==paired_quotient(l,p,q)
        H,gamma_step,S=harmonic_gamma(l,p)
        inv18=pow(18,-1,p)
        assert gamma_step==(-H*inv18)%p
        log_step=(gamma_step*b[M])%p
        E_step=(gamma_step*T)%p
        assert log_step==(-H*inv18)%p
        assert E_step==(-H*T*inv18)%p
        if p in anchors:
            witnesses[p]={'ell':l,'H_mod_p':H,'T_mod_p':T,
                          'residue_over_p':log_step,'scalar_defect_over_p':E_step}
            if p<=37:
                assert (log_step,E_step)==rational_check(l)
    print('PASS_D25_FROBENIUS_PLATEAU_GREEN_QUOTIENT_DEFECT',
          'rational_ell=1..14',f'primes={len(ps)}','p<=1200')
    for p,v in witnesses.items():
        print('WITNESS',p,v)


if __name__ == '__main__':
    run()
