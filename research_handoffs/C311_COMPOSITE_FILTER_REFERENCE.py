#!/usr/bin/env python3
"""C311 exact composite-sample content certificates for 19 frozen paths.

Run alongside frozen C305_MODULAR_NEWTON_CONTENT.py,
C310_JOINT_BRANCH_PRIME_CERT.py, EM_C301_EXACT_PORTABLE/.
Output is author-level auxiliary scalar math, never native X6/BRC.
"""
import json
from math import gcd
from functools import reduce
from pathlib import Path
import C310_JOINT_BRANCH_PRIME_CERT as prior
import C305_MODULAR_NEWTON_CONTENT as src

def value(coefficients, t):
    acc = 0
    for c in reversed(coefficients):
        acc = acc * t + c
    return acc

def normalize(prepared, L):
    result = []
    for coefficient, numerators, powers in prepared:
        contents = [reduce(gcd, poly, 0) for poly in numerators]
        scalar = coefficient
        for c in contents:
            assert c != 0
            scalar *= c
        assert scalar % L == 0
        primitive_numerators = [tuple(x // c for x in poly)
                                for poly, c in zip(numerators, contents)]
        result.append((scalar // L, primitive_numerators, powers))
    return result

def sample_mod(t, factors, normalized, modulus):
    values = {factor: value(factor, t) % modulus for factor in factors}
    total = 0
    for scalar, numerators, powers in normalized:
        term = scalar % modulus
        if not term:
            continue
        for factor, max_exponent in factors.items():
            deficit = max_exponent - powers.get(factor, 0)
            if deficit:
                term = term * pow(values[factor], deficit, modulus) % modulus
            if not term:
                break
        for numerator in numerators:
            term = term * value(numerator, t) % modulus
        total = (total + term) % modulus
    return total

def exact_factorization(n):
    assert n >= 1
    factors = {}
    prime = 2
    while prime * prime <= n:
        if n % prime == 0:
            count = 0
            while n % prime == 0:
                n //= prime
                count += 1
            factors[prime] = count
        prime += 1 if prime == 2 else 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def nonzero(poly, modulus):
    for degree, coefficient in enumerate(poly):
        residue = int(coefficient) % modulus
        if residue:
            return [degree, residue]
    return None

def run():
    freeze = json.loads((src.ROOT / 'C293_125_REFINED_BRACKETS.json').read_text())
    paths, _ = src.c288.build_paths()
    weights, _ = src.src.floor_fixed_masses()
    certificates = []
    for index in prior.EXCEPTIONAL:
        s, factors, prepared, _, degree = src.prepare(
            index, paths[index], int(freeze['records'][index][1]), weights)
        L = prior.term_content_lower(s, prepared)
        assert s % L == 0
        modulus = s // L
        p = 3 if index in prior.PRIME_THREE else 2
        terms = normalize(prepared, L)
        samples = [sample_mod(t, factors, terms, modulus) for t in range(5)]
        H = gcd(modulus, *samples)
        prime_support = exact_factorization(H)
        assert p in prime_support, (index, p, H)
        checks = []
        for q in prime_support:
            coefficients, *_ = prior.poly_branch_mod(q, factors, prepared, L)
            witness = nonzero(coefficients, q)
            if q == p:
                assert witness is None
                coefficients_p2, *_ = prior.poly_branch_mod(
                    p * p, factors, prepared, L)
                witness_p2 = nonzero(coefficients_p2, p * p)
                assert witness_p2 is not None
                checks.append({'prime': q, 'zero_mod_p': True,
                               'witness_mod_p2': witness_p2})
            else:
                assert witness is not None, (index, q)
                checks.append({'prime': q, 'witness_mod_q': witness})
        certificates.append({
            'path': index, 'candidate_prime': p, 'degree': degree,
            'M': str(modulus), 'M_bits': modulus.bit_length(),
            'samples_mod_M': [str(v) for v in samples],
            'H': str(H), 'H_bits': H.bit_length(),
            'complete_H_factorization': prime_support,
            'coefficient_certificates': checks,
            'proven_gcd_s_content_P': str(L * p)})
        print('C311_PASS', index, len(checks))
    assert len(certificates) == 19
    assert sum(len(x['coefficient_certificates']) for x in certificates) == 162
    Path('C311_REFERENCE_CERT.json').write_text(
        json.dumps(certificates, ensure_ascii=False, indent=2) + '\n')
    print('C311_ALL_19_PASS / 95_SAMPLES / 162_COEFFICIENT_CHECKS')

if __name__ == '__main__':
    run()
