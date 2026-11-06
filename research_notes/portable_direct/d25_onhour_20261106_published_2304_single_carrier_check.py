#!/usr/bin/env python3
"""D25 original 216/2304 integer modular checks; author-side, not native H0/B0."""
import json
import sys
from math import comb
from pathlib import Path


def primes_upto(limit):
    composite = bytearray(limit + 1)
    for d in range(2, limit + 1):
        if not composite[d]:
            yield d
            for m in range(d * d, limit + 1, d):
                composite[m] = 1


def check_prime(p):
    modulus = p**4
    a, w = 1, 0
    for n in range(p):
        w = (w + (6 * n + 1) * a) % modulus
        if n + 1 < p:
            a = a * (2*n + 1) * (3*n + 1) * (3*n + 2) * pow(36 * (n+1)**3, -1, modulus) % modulus
    b, v = 1, 0
    h = (p-1)//2
    for k in range(h+1):
        v = (v + (8*k + 1) * b) % modulus
        if k + 1 <= h:
            b = b * (4*k + 1) * (2*k + 1) * (4*k + 3) * pow(288 * (k+1)**3, -1, modulus) % modulus
    chi = 1 if p%3 == 1 else -1
    assert w % p**3 == (p*chi) % p**3, ('W', p, w)
    assert v % p**3 == (p*chi) % p**3, ('V', p, v)
    if p <= 23:
        a0 = sum((6*n + 1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,modulus) for n in range(p)) % modulus
        b0 = sum((8*k + 1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,modulus) for k in range(h+1)) % modulus
        assert (a0,b0) == (w,v), ('binomial',p)
    return {'p':p, 'p_mod_24':p%24, 'chi':chi,
            'W_mod_p3': w%p**3, 'V_mod_p3':v%p**3,
            'W_next_digit': ((w-p*chi)%modulus)//p**3,
            'V_next_digit': ((v-p*chi)%modulus)//p**3,
            'difference_next_digit': ((w-v)%modulus)//p**3}


def main():
    rows = [check_prime(p) for p in primes_upto(997) if p>3]
    assert len(rows) == 166
    output = {'kind':'AUTHOR_FINITE_REGRESSION_NOT_NATIVE_NOT_ADMITTED',
              'scope':'All primes 5<=p<=997; original W,V modulo p^4, tests modulo p^3',
              'count':len(rows),
              'target_primes':sum(row['p_mod_24'] in (13,19) for row in rows),
              'all_W_eq_leg_p_mod_p3':True, 'all_V_eq_leg_p_mod_p3':True,
              'all_pair_equal_mod_p3':True, 'raw':rows}
    path = Path(sys.argv[1] if len(sys.argv)>1 else 'd25_published_2304_bridge_166primes.json')
    path.write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'count':len(rows),'target_primes':output['target_primes'],
         'p4_examples':[next(row for row in rows if row['p']==p) for p in (13,19,373)],
         'output':str(path)}, indent=2))


if __name__ == '__main__':
    main()
