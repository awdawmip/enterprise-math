"""Tiny arithmetic observer counterexamples; no factor search or RSA input.

All semiprime labels are formed from bounded prime fixtures below 1,000.
Only the existing brc_shadow_signature readout is called from the tool library.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json
import sys


def h3(p, q):
    s, n = p+q, p*q
    return 2*s**3-9*n*s


def centered_scaled(p, q, degree):
    mean = Fraction(p+q, 3)
    value = sum((Fraction(x)-mean)**degree for x in (0, p, q))
    scaled = value*3**(degree-1)
    assert scaled.denominator == 1
    return scaled.numerator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--enterprise-root', required=True, type=Path)
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root/'src'))
    from enterprise_math.brc_opportunistic_shortcuts import brc_shadow_signature

    # Four local residue pairs supplied explicitly, not obtained by factoring.
    modulus = 55
    residues = [(3, 13), (8, 53), (47, 2), (52, 42)]
    crt_rows = []
    for a, b in residues:
        n, s = a*b, a+b
        assert centered_scaled(a,b,3) == h3(a,b)
        crt_rows.append({
            'a':a, 'b':b, 'product_mod55':n%55, 'sum_square_mod55':s*s%55,
            'H3_mod55':h3(a,b)%55, 'H3_square_mod55':h3(a,b)**2%55,
            'H3_mod5':h3(a,b)%5, 'H3_mod11':h3(a,b)%11,
            'even_scaled_moments_mod55': [centered_scaled(a,b,d)%55 for d in (2,4,6,8,10,12)],
        })
    assert len({r['product_mod55'] for r in crt_rows}) == 1
    assert len({r['sum_square_mod55'] for r in crt_rows}) == 1
    assert len({r['H3_square_mod55'] for r in crt_rows}) == 1
    assert len({tuple(r['even_scaled_moments_mod55']) for r in crt_rows}) == 1
    assert len({r['H3_mod55'] for r in crt_rows}) == 4

    primes = (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    rows = []
    for p, q in combinations(primes, 2):
        n, s = p*q, p+q
        root = isqrt(n)
        remainder = n-root*root
        signature = brc_shadow_signature(n, root, remainder, modulus=5)
        rows.append({'p':p, 'q':q, 'N':n, 'bits':n.bit_length(), 'J':root,
                     'R':remainder, 'S2_mod5':s*s%5, 'H3_mod5':h3(p,q)%5,
                     'signature':signature})
    rows.sort(key=lambda r:r['N'])

    def witness_for(keys, population, target_modulus):
        seen = {}
        for row in population:
            if row['N']%target_modulus == 0:
                continue
            key = tuple(row[k] for k in keys)
            old = seen.get(key)
            if old is not None and old['H3_residue'] != row['H3_residue']:
                return [old, row]
            seen.setdefault(key,row)
        return None

    for row in rows:
        row['H3_residue'] = row['H3_mod5']
    actual_signature_witness = witness_for(('signature',),rows,5)
    augmented_witness = witness_for(('signature','S2_mod5'),rows,5)
    bit_augmented_witness = witness_for(('signature','S2_mod5','bits'),rows,5)
    assert actual_signature_witness is not None
    assert augmented_witness is not None
    # Absence of a particular stronger witness would remain a finite observation.
    former = [next(r for r in rows if r['N']==n) for n in (39,119)]
    assert former[0]['signature'] != former[1]['signature']

    # One predetermined second fixture checks the API's actual default modulus.
    # This only generates known small products; there is no unknown-N input.
    prime_mask = [True]*1000
    prime_mask[0] = prime_mask[1] = False
    for divisor in range(2,isqrt(999)+1):
        if prime_mask[divisor]:
            for multiple in range(divisor*divisor,1000,divisor):
                prime_mask[multiple] = False
    default_primes = [p for p in range(3,1000) if prime_mask[p]]
    default_rows = []
    for p,q in combinations(default_primes,2):
        n,s = p*q,p+q
        assert n < 1_000_000
        j = isqrt(n)
        r = n-j*j
        default_rows.append({'p':p,'q':q,'N':n,'bits':n.bit_length(),
            'J':j,'R':r,'S2_mod64':s*s%64,'H3_residue':h3(p,q)%64,
            'signature':brc_shadow_signature(n,j,r)})
    default_rows.sort(key=lambda row:row['N'])
    default_witness = witness_for(('signature','S2_mod64','bits','J'),default_rows,64)
    for witness in (actual_signature_witness,augmented_witness,bit_augmented_witness,default_witness):
        for row in witness or ():
            assert centered_scaled(row['p'],row['q'],3) == h3(row['p'],row['q'])

    module = args.enterprise_root/'src/enterprise_math/brc_opportunistic_shortcuts.py'
    result = {
        'researcher_id':'EM-HME-0CE4FD',
        'global_snapshot':'c1c3610234637bd1309e29474c306a0db3040ad8',
        'reference_tool_snapshot':'c5d6e6ed4aa4c899706e2a895f55733dc2eb3cb8',
        'reference_tool_blob':'1214aa09770893fb3de7f85b994d1994ff56bffe',
        'executed_module_sha256':sha256(module.read_bytes()).hexdigest(),
        'scope':'bounded arithmetic/readout audit; no challenge modulus or factor-search routine',
        'known_prime_pairs_checked':len(rows),
        'maximum_N':max(r['N'] for r in rows),
        'signature_modulus':5,
        'former_witness_is_separated_by_actual_signature':former,
        'actual_signature_collision':actual_signature_witness,
        'actual_signature_plus_S2_collision':augmented_witness,
        'actual_signature_plus_S2_and_bits_collision':bit_augmented_witness,
        'default_modulus_audit':{
            'modulus':64,'known_prime_pairs_checked':len(default_rows),
            'maximum_N':max(r['N'] for r in default_rows),
            'signature_plus_S2_bits_and_exact_J_collision':default_witness,
        },
        'crt_residue_rows':crt_rows,
        'proof_scope':'finite witnesses refute only the stated observers; the CRT statement is over residue pairs, not multiple factorizations of a single complete integer',
        'verdict':'PASS_SMALL_OBSERVER_COUNTEREXAMPLES; NO_NONLY_MOMENT_EXTRACTOR',
    }
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'observer_audit_certificate.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

