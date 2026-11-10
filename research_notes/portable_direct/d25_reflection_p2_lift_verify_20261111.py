#!/usr/bin/env python3
"""D25 harmonic p-adic reflection mod p^2: exact author-side verification.
Frozen scientific source: c47e13e4aba0e006366f989d6334d443f6333ae3.
Not a native H0/B0 Source experiment; not independent review or admission.
"""
import json
from math import factorial, isqrt

def primes(bound):
    for p in range(5, bound + 1):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p

def a_coefficients(p):
    modulus = p**5
    a = [1]
    for k in range(p - 1):
        numerator = (2*k+1)*(3*k+1)*(3*k+2)
        denominator = 36*(k+1)**3
        a.append(a[-1]*numerator*pow(denominator, -1, modulus) % modulus)
    return a

def factorial_independent(p, a):
    modulus = p**5
    fact = [1]*(3*p)
    for j in range(1, 3*p):
        fact[j] = fact[j-1]*j % modulus
    for k, ak in enumerate(a):
        direct = (fact[2*k]*fact[3*k]*pow(216, -k, modulus)
                  *pow(fact[k], -5, modulus)) % modulus
        assert ak == direct, (p,k,'independent factorial')

def verify_prime(p, independent=False):
    assert p > 3
    a = a_coefficients(p)
    if independent:
        factorial_independent(p, a)
    H = [0]*p
    for j in range(1,p):
        H[j] = (H[j-1] + pow(j,-1,p))%p
    q216 = (pow(216,p-1,p*p)-1)//p
    modulus = p**5
    for k in range(1,p):
        q2,r2 = divmod(2*k,p)
        q3,r3 = divmod(3*k,p)
        d = (2*H[r2-1]+3*H[r3-1]-5*H[k-1]-q216)%p
        lead = ((-1)**(q2+q3+1)*factorial(q3)*factorial(2-q3)
                *pow(36*k**3,-1,p*p)) % (p*p)
        predicted = lead*(1+p*d) % (p*p)
        product = a[k]*a[p-k] % modulus
        assert product % p**3 == 0, (p,k,'valuation')
        actual = product//p**3
        assert predicted == actual, (p,k,'p2 reflected product',predicted,actual)
    row = {'p':p,'reflection_pairs':p-1}
    if p%24 in (13,19):
        m = (p-1)//6
        tail = sum((6*k+1)*a[k] for k in range(4*m+1,p))%modulus
        assert tail%p**3 == 0
        f2 = tail//p**3
        reconstructed = 0
        for j in range(1,2*m+1):
            d = (2*H[2*j-1]+3*H[3*j-1]-5*H[j-1]-q216)%p
            reconstructed += ((6*j-1-6*p)*pow(18*j**3*a[j],-1,p*p)
                              *(1+p*d))
        reconstructed %= p*p
        assert reconstructed == f2, (p,'p5 upper band',reconstructed,f2)
        row.update({'fourth_band_digit_0':f2%p,
                    'fourth_band_digit_1':f2//p,
                    'fourth_band_normalized_p2':f2})
    return row

def main():
    selected = [p for p in primes(10000) if p%24 in (13,19)]
    assert len(selected) == 312
    records = [verify_prime(p, p in (13,19,157,373)) for p in selected]
    others = [5,7,11,17,23,29,31,41,47,53,59]
    for p in others:
        verify_prime(p,p in (5,11))
    pairs = sum(record['reflection_pairs'] for record in records)
    assert pairs == 1475586
    total = pairs+sum(p-1 for p in others)
    assert total == 1475898
    samples = [r for r in records if r['p'] in (13,19,157,373)]
    result = {
      'science_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
      'status':'AUTHOR_PROVED_EXACT_INTEGER_VERIFIED_UNREVIEWED_NOT_ADMITTED',
      'domain':'all primes p>3 theorem; finite test p<=10000 in {13,19} mod24',
      'selected_primes':len(selected),
      'selected_reflection_pairs':pairs,
      'extra_prime_pairs':sum(p-1 for p in others),
      'total_reflection_pairs':total,
      'selected_fourth_bands_checked':len(selected),
      'factorial_crosschecks':[5,11,13,19,157,373],
      'samples':samples,
      'all_selected_primes':records,
    }
    with open('d25_reflection_p2_lift_certificate_20261111.json','w') as out:
        json.dump(result,out,indent=2,sort_keys=True)
    print('PASS',len(selected),'primes',total,'reflections',
          len(selected),'fourth-band double-digit checks')
    print('samples',samples)

if __name__=='__main__':
    main()
