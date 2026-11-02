"""D25 original 216: p^2 high-strip hypergeometric mirror (finite exact replay).

Source carrier: (6k+1)*binom(2k,k)^2*binom(3k,k)/216^k.
The independent direct computation uses exact integer binomials modulo p^3.
The mirror carrier uses an F_p rational recurrence and a finite-field ODE.
The D25 full-value checks are FINITE observations, not a universal proof.
"""
from math import comb
from json import dump


def primes(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, int(n ** 0.5) + 1):
        if sieve[k]:
            sieve[k * k::k] = b'\x00' * ((n - k * k) // k + 1)
    return (k for k in range(n + 1) if sieve[k])


def term(k, p, weighted=True):
    mod = p**3
    integer_coefficient = comb(2*k, k)**2 * comb(3*k, k)
    unit_denominator = pow(216, -k, mod)
    weight = 6*k+1 if weighted else 1
    return (weight*integer_coefficient*unit_denominator) % mod


def high_strip(p):
    assert p % 6 == 1 and p >= 7
    r = (p-1)//6
    h = 3*r
    legendre = pow(6, (p-1)//2, p)
    assert legendre in (1, p-1)
    sign = 1 if legendre == 1 else -1
    mirror = [1]  # c_t = (1)_t (5/6)_t (7/6)_t / ((3/2)_t^3 2^t)
    for t in range(1, r):
        ratio = (t*(6*t-1)*(6*t+1)*pow(9*(2*t+1)**3, -1, p)) % p
        mirror.append(mirror[-1]*ratio % p)

    base = sign*pow(9, -1, p) % p
    upper_sum = 0
    for s in range(1, r+1):
        k = h+s
        original = term(k, p, weighted=False)
        assert original % (p*p) == 0
        quotient = original//(p*p)
        predicted = base*mirror[s-1] % p
        assert quotient == predicted, (p, s, quotient, predicted)
        signed_weight = (6*s-2)%p
        assert term(k, p)//(p*p) == signed_weight*predicted % p
        upper_sum = (upper_sum+signed_weight*predicted)%p

    # ODE: theta(theta+1/2)^3 R = (x/2)(theta+1)^2
    #                                       (theta+5/6)(theta+7/6) R.
    # Check every coefficient through degree r (including terminating edge).
    inv2 = pow(2, -1, p)
    inv6 = pow(6, -1, p)
    for t in range(0, r+1):
        lhs = t*pow((t+inv2)%p, 3, p)*(mirror[t] if t < r else 0)
        rhs = 0 if t == 0 else inv2*t*t*(t-inv6)*(t+inv6)*mirror[t-1]
        assert (lhs-rhs)%p == 0, (p, t, lhs%p, rhs%p)
    mirror_value = sum(mirror) % p
    mirror_theta = sum(t*v for t, v in enumerate(mirror)) % p
    assert upper_sum == sign*pow(9, -1, p)*(4*mirror_value+6*mirror_theta)%p
    return upper_sum, sign, mirror_value, mirror_theta


if __name__ == '__main__':
    target = []
    nprimes = 0
    checked_terms = 0
    for p in primes(2000):
        if p < 7 or p % 6 != 1:
            continue
        nprimes += 1
        checked_terms += (p-1)//6
        high, sign, mv, mj = high_strip(p)
        if p%24 in (13, 19):
            half_idx = (p-1)//2
            mod = p**3
            half = sum(term(k, p) for k in range(half_idx+1)) % mod
            assert (half-p)%(p*p) == 0
            half_digit = ((half-p)//(p*p))%p
            full_mod = (half+p*p*high)%mod
            target.append({'p':p,'character_6':sign, 'half_digit':half_digit,
                           'high_strip_digit':high, 'mirror_value':mv, 'mirror_theta':mj, 'signed_total':(half_digit+high)%p,
                           'full_mod_p3':full_mod})
    assert nprimes == 148
    assert checked_terms == 22952
    assert len(target) == 77
    assert all(t['signed_total']==0 for t in target)
    out = {'schema':'D25_216_HIGH_STRIP_MIRROR_CERTIFICATE_V1',
           'scope':'all primes 7<=p<=2000, p=6r+1',
           'prime_count':nprimes,'termwise_positions':checked_terms,
           'p2_normalized_source_recurrence':'PASS',
           'mirror_4F3_polynomial_ODE':'PASS',
           'finite_target_prime_count':len(target),
           'finite_original_D25_cancellation':'PASS_FINITE_NOT_GENERAL_PROOF',
           'samples':[z for z in target if z['p'] in (13,19,37,43,181,373,1171)]}
    with open('/mnt/data/d25_reflected_high_strip_20261103_results.json','w') as fp:
        dump(out, fp, indent=2)
    print(out)
