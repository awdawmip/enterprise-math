"""Independent source-labelled finite arithmetic for the D25 B2304 dual-cutoff lemma.
Uses only the Python standard library. No native H0/B0 experiment is attempted.
"""
from math import comb


def math_fact_mod(n,p):
    out=1
    for j in range(2,n+1):
        out=out*j%p
    return out


def prime_list(bound):
    sieve = [True] * bound
    sieve[0:2] = [False, False]
    for d in range(2, int(bound ** 0.5) + 1):
        if sieve[d]:
            for j in range(d * d, bound, d):
                sieve[j] = False
    return [p for p in range(5, bound) if sieve[p]]


def original_ports(p):
    """Preserve coefficients and original (6n+1)/(8n+1) weights modulo p^4."""
    mod = p**4
    unit = [1] * (4 * p)
    for k in range(1, 4 * p):
        unit[k] = unit[k - 1] * (k if k % p else 1) % mod
    fact = unit[:p]
    inv_fact = [pow(f, -1, mod) for f in fact]
    a_inv, b_inv = pow(216, -1, mod), pow(2304, -1, mod)
    pa = pb = 1
    a_tier = [0, 0, 0, 0]
    b_tier = [0, 0, 0, 0]
    b_mid = {}
    for n in range(p):
        ae = 2 * n // p + 3 * n // p
        be = 4 * n // p
        ai = inv_fact[n]
        # Multiples kp contribute p^e * e!, not just p^e.
        factorial_small = (1, 1, 2, 6)
        a_u = (factorial_small[2*n//p]*factorial_small[3*n//p]
               * unit[2*n]*unit[3*n]*pow(ai,5,mod)) % mod
        b_u = (factorial_small[be]*unit[4*n]*pow(ai,4,mod)) % mod
        a_term = (6*n+1) * a_u * (p**ae) * pa % mod
        b_term = (8*n+1) * b_u * (p**be) * pb % mod
        a_tier[ae] = (a_tier[ae] + a_term) % mod
        b_tier[be] = (b_tier[be] + b_term) % mod
        if be == 2:
            b_mid[n] = b_term
        pa, pb = pa * a_inv % mod, pb * b_inv % mod

    # Independently evaluate the PROVED earlier B2304 reflected leading coefficient.
    reflected = 0
    for r in range(p // 4, (p - 3)//2 + 1):
        t = 4*r+3-p
        assert 0 <= t < p
        reflected_term = (2*(8*r+7)*pow(2304, r, p)
                          * pow(fact[r], 4, p)*pow(fact[t], -1, p)) % p
        n = p - 1 - r
        assert (b_mid[n]//(p*p))%p == reflected_term, (p,n,"per-term reflection")
        reflected = (reflected + reflected_term) % p
    b2 = b_tier[2]
    assert b2 % (p*p) == 0
    assert (b2//(p*p)) % p == reflected, (p, 'reflection mismatch')
    assert reflected == 0, (p, 'B2304 tier-2 cancellation failure')
    assert b2 % p**3 == 0

    # Published Guo--Zudilin 2019 theorem has BOTH cutoffs, not merely full p-1.
    chi = 1 if p % 3 == 1 else -1  # (-3/p) is the quadratic character modulo 3 for p>3.
    b_half = (b_tier[0] + b_tier[1]) % mod
    b_full = sum(b_tier) % mod
    assert b_half % p**3 == (p*chi) % p**3, (p, 'half-cutoff regression')
    assert b_full % p**3 == (p*chi) % p**3, (p, 'full-cutoff regression')
    return a_tier, b_tier, reflected


def direct_binomial_crosscheck(p, a_tier, b_tier):
    mod = p**4
    a_orig = [0,0,0,0]
    b_orig = [0,0,0,0]
    for n in range(p):
        a_orig[(2*n)//p+(3*n)//p] = (a_orig[(2*n)//p+(3*n)//p]
             + (6*n+1)*comb(2*n,n)**2 *comb(3*n,n)*pow(216,-n,mod))%mod
        b_orig[(4*n)//p] = (b_orig[(4*n)//p]
             +(8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,mod))%mod
    assert a_orig == a_tier, (p, 'original A coefficient disagreement')
    assert b_orig == b_tier, (p, 'original B coefficient disagreement')


def main():
    ps = prime_list(1500)
    target = 0
    nonzero_fourth = 0
    for p in ps:
        a, b, r = original_ports(p)
        if b[2] % p**4:
            nonzero_fourth += 1
        if p % 24 not in (13, 19):
            continue
        target += 1
        # Proven D24 first digit makes the following quotients legitimate.
        assert sum(a) % p**2 == p
        a_low = (a[0] + a[1]) % p**4
        b_low = (b[0] + b[1]) % p**4
        assert (a_low - p) % (p*p) == 0
        c_low = (a_low - 2*b_low + p) % p**4
        assert c_low % p**2 == 0
        j = (c_low//(p*p)) % p
        q_original = ((a[2] - 2*b[2])//(p*p)) % p
        # The new all-prime B2 lemma removes the B model from the second-digit port.
        q_short = (a[2]//(p*p)) % p
        low_short = ((a_low - p)//(p*p)) % p
        assert j == low_short, (p, 'low-port equality')
        assert q_original == q_short, (p, 'valuation-two elimination')
        # Reuse the earlier proved A216 tier-2 reflection, with original signs.
        m=(p-1)//6
        a_reflected=0
        for r in range(2*m,3*m):
            t2,t3=2*r+1,3*r+2-p
            term=((6*r+5)*pow(216,r,p)*pow(math_fact_mod(r,p),5,p)
                  *pow(math_fact_mod(t2,p)*math_fact_mod(t3,p),-1,p))%p
            a_reflected=(a_reflected+term)%p
        assert a_reflected == q_short, (p, 'A tier-2 reflection port')
        assert (j+q_short) % p == 0, (p, 'finite LIFT regression')
        if p in (13, 19, 373):
            print('TARGET',p, 'J',j, 'A2/p2',q_short,
                  'B2/p3', (b[2]//p**3)%p, 'B3/p3',(b[3]//p**3)%p)
        if p in (13, 19, 373):
            direct_binomial_crosscheck(p, a, b)
    for p in (5, 7, 11, 31, 373):
        if p % 24 not in (13, 19):
            a,b,_ = original_ports(p)
            direct_binomial_crosscheck(p,a,b)
    print('PASS_B2304_DUAL_CUTOFF_TIER2_ALL_PRIMES',len(ps),
          'TARGET_CLASS_PRIMES',target,'B2_NONZERO_MOD_P4',nonzero_fourth)
    print('PASS_REFLECTED_FINITE_FIELD_IDENTITY_AND_ORIGINAL_RAW_CROSSCHECK')
    print('FINITE_CHECK_IS_NOT_A_UNIVERSAL_LIFT_PROOF; NATIVE_H0_B0_NOT_EXECUTED')

if __name__ == '__main__':
    main()
