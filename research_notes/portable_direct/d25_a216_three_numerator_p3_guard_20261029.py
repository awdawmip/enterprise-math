#!/usr/bin/env python3
"""Author-side exact check of original A216 three-numerator valuation ports.

This verifier does not run or replace native H0/B0 divided-power computation,
make a source-native CLAIM/Result, or prove the target prime-dependent cancellation.
"""
from math import comb, isqrt


def primes(limit):
    for p in range(7, limit):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p)+1)):
            yield p


def published_theta_digits(p):
    """Independent prior 2026-10-28 factorial-reflection theorem, NOT our new result.

    Source: enterprise-math@321f924, original216_p3_middle_tail_reflection.md.
    Returns tau_{p,r} for 0 <= r < m, and its sum modulo p.
    """
    m = (p-1)//6
    factorial = [1]*p
    for n in range(1,p):
        factorial[n] = factorial[n-1]*n % p
    power = pow(216,2*m,p)
    digits=[]
    for r in range(m):
        den = factorial[4*m+1+2*r]*factorial[3*r+1] % p
        tau = 3*(2*r+1)*power*pow(factorial[2*m+r],5,p)*pow(den,-1,p)%p
        digits.append(tau)
        power = power*216 % p
    return digits, sum(digits)%p


def source_ledger(p):
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 6
    modulus = p**3
    two_inv = pow(2, -1, modulus)
    # Three distinct source factors, never treated as an unlabelled sum.
    sources = ((3*m, 1, 2), (2*m, 1, 3), (4*m, 2, 3))
    u = 1  # hit-removed unit product / (2**n * (n!)**3)
    c = 1  # product of hit slopes
    hits = 0
    s1 = s2 = 0  # first and diagonal second-order numerator jets
    direct = 1
    tier = [0, 0, 0, 0]
    ports = [0] * 6  # (h0 zeroth/first/second, h1 zeroth/first, h2 zeroth)
    midpoint_weight = None
    midpoint_coefficient_modp = None
    independent = 0
    binomial = 0
    inv216 = pow(216, -1, modulus)
    z216 = 1
    exact_terms = []
    original_double_hit = {}
    for n in range(p):
        corr = (1 + p*s1 + p*p*two_inv*(s1*s1 - s2)) % modulus
        predicted = (p**hits * c * u * corr) % modulus
        assert predicted == direct, (p, n, hits, predicted, direct)
        weight = 6*n + 1
        tier[hits] = (tier[hits] + weight*predicted) % modulus
        if hits == 2:
            assert (weight*predicted)%modulus % (p*p) == 0
            original_double_hit[4*m-n] = ((weight*predicted)%modulus)//(p*p)
        if n == m:
            midpoint_weight = weight
            midpoint_coefficient_modp = int(predicted % p)
        terms = []
        if hits == 0:
            terms = [(0, u), (1, p*u*s1),
                     (2, p*p*u*two_inv*(s1*s1-s2))]
        elif hits == 1:
            terms = [(3, p*c*u), (4, p*p*c*u*s1)]
        elif hits == 2:
            terms = [(5, p*p*c*u)]
        for pos, term in terms:
            ports[pos] = (ports[pos] + weight*term) % modulus
        independent = (independent + weight*direct) % modulus
        if p <= 373:
            # Independent integer binomial summation (not the 3-stream recurrence)
            binomial = (binomial + weight * comb(2*n,n)**2 * comb(3*n,n)*z216) % modulus
            z216 = z216 * inv216 % modulus
        if p == 373 and (n in [0,2*m,2*m+1,3*m,3*m+1,4*m,4*m+1,p-1]):
            exact_terms.append((n,hits, int(predicted)))
        if n == p-1:
            break
        j = n
        for hit_index, num, den in sources:
            slope = num * pow(den, -1, modulus) % modulus
            q = j - hit_index
            if q == 0:
                hits += 1
                c = c * slope % modulus
            else:
                u = u * q % modulus
                port = slope * pow(q, -1, modulus) % modulus
                s1 = (s1 + port) % modulus
                s2 = (s2 + port*port) % modulus
        u = u * two_inv * pow((n+1)**3, -1, modulus) % modulus
        direct = direct * (2*n+1)*(3*n+1)*(3*n+2) * pow(36*(n+1)**3, -1, modulus) % modulus
    assert hits == 3 and tier[3] == 0, (p,hits,tier)
    assert midpoint_weight == p
    assert sum(ports) % modulus == independent
    assert ((ports[0]+ports[1]+ports[2])%modulus) == tier[0]
    assert ((ports[3]+ports[4])%modulus) == tier[1]
    assert ports[5] == tier[2]
    old_tau, old_theta = published_theta_digits(p)
    assert len(original_double_hit) == m
    assert all(original_double_hit[r] == old_tau[r] for r in range(m)), p
    assert old_theta == (tier[2]//(p*p)), (p, old_theta, tier[2])
    assert sum(tier) % modulus == independent
    if p <= 373:
        assert binomial == independent
    assert independent % p**2 == (p if p % 6 == 1 else -p) % p**2  # informational baseline
    return {"p":p,"m":m,"tier0":tier[0],"tier1":tier[1],"tier2":tier[2],
            "tier3":tier[3],"prior_Theta": old_theta if p in (13,19,373) else None,"middle_n_m_unit":midpoint_coefficient_modp if p==373 else None,"six_ports":ports if p in (13,19,373) else None,"A":independent,"A_over_p2_residue":((independent-p)%modulus)//p**2,
            "boundary_terms":exact_terms}


def main():
    tested = list(primes(1500))
    result = [source_ledger(p) for p in tested]
    target = [a for a in result if a['p'] % 24 in (13,19)]
    print('PASS_ORIGINAL_A216_THREE_NUMERATOR_COEFFICIENTWISE_P3',len(result),
          'p=1 mod6 primes <1500, target_classes',len(target))
    for a in result:
        if a['p'] in (7,13,19,31,37,43,73,157,211,373,421):
            print('SOURCED_TIERS',a)
    counts={c:sum(a['p'] %24 ==c for a in target) for c in (13,19)}
    print('TARGET_COUNTS',counts)
    # Finite observation only, not an all-prime proof.
    print('TARGET_A_EQUALS_P_EXACT_CHECK', all(a['A']==a['p'] for a in target))

if __name__ == '__main__':
    main()
