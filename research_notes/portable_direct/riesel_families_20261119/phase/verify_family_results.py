"""Independent arbitrary-precision reconstruction and pinned native BRC check.

This verifies every per-shift winning witness, both global new certificates,
and the mathematical finite-family counting invariants. It does not repeat
the minimization or constitute an independent institutional Review.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import sys

from prepare_family import (DIRECTORY, ROOT, PRIOR, STRUCTURE, PRIMES, PERIODS,
                            PHASES, ROWS, M, L, GROUP7, GROUP5, PAIR24, PAIR32,
                            FIXED, INDEX, decode, membership, phase_coordinate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, default=ROOT/'vendor_src')
    args = parser.parse_args()
    prior_result = json.loads((PRIOR/'results.json').read_text())
    for name, expected in prior_result['project_source_blobs'].items():
        data = (args.source_dir/'enterprise_math'/name).read_bytes()
        assert sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == expected
    sys.path.insert(0, str(args.source_dir.resolve()))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (0,)), 1)])

    def advance(packet, x):
        (point, weights), = packet.evaluate((x,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    def rem(x, p):
        return euclidean_digits(x, (p,))[1][0]

    masks = [[sum(1 << u for u in range(c, L, e)) for c in range(e)] for e in PERIODS]
    full = (1 << L)-1

    def cover(vector):
        union = 0
        for i, c in enumerate(vector):
            union |= masks[i][c]
        return union == full

    assert cover(PHASES)
    assert [t for t in range(L) if membership([(c+t) % e for c,e in zip(PHASES, PERIODS)])] == list(range(0,L,240))
    # Verify the component group actions on the whole u-domain, not merely
    # coverage for separate changes. This certifies their arbitrary products.
    group_action_counts = []
    for group, q, coordinates in [(GROUP5,5,range(4)),(GROUP7,7,range(7))]:
        indices = [INDEX[p] for p in group]
        old_coordinates = [PHASES[i] % q for i in indices]
        count = 0
        for perm in permutations(coordinates):
            mapping = dict(zip(old_coordinates, perm))
            for r in range(q):
                mapping.setdefault(r, r)
            # Coordinate permutation phi(u) modulo q, identity modulo L/q.
            # Every labelled channel transforms into its prescribed new phase.
            for i, (e,c) in enumerate(zip(PERIODS, PHASES)):
                if e % q == 0:
                    new_c = phase_coordinate(PRIMES[i], q, mapping[c % q])
                    if i not in indices:
                        assert new_c == c
                else:
                    new_c = c
                if i in indices:
                    assert new_c == phase_coordinate(PRIMES[i],q,perm[indices.index(i)])
            count += 1
        assert count == factorial(len(group))
        group_action_counts.append({'coordinate_modulus':q,'permutations':count,'domain_action_verified':True})
    for group in [PAIR24, PAIR32]:
        i,j = [INDEX[p] for p in group]
        assert PERIODS[i] == PERIODS[j] and PHASES[i] != PHASES[j]
        assert (masks[i][PHASES[i]] | masks[j][PHASES[j]]) == (masks[i][PHASES[j]] | masks[j][PHASES[i]])

    certificates = []
    for branch, input_name, old_name, factor in [
        ('unrestricted','minimum_M.json','optimized_results.json',1),
        ('divisible3','minimum_3M.json','optimized_results_mod3.json',3)]:
        computation = json.loads((DIRECTORY/input_name).read_text())
        assert int(computation['modulus']) == factor*M
        assert computation['left_count'] == 645120 and computation['right_count'] == 786432
        assert computation['shift_count'] == 240 and len(computation['minima']) == 240
        assert [r['translation'] for r in computation['minima']] == list(range(240))
        assert computation['minimum'] == min(computation['minima'],key=lambda r:int(r['root']))
        for witness in computation['minima']:
            a = int(witness['root'])
            assert 0 < a < factor*M and a % 2 == 1
            if factor == 3:
                assert a % 3 == 0
            decoded = decode(witness['a_code'],witness['b_code'],witness['translation'])
            assert membership([r['base_u_phase'] for r in decoded['rows']])
            assert cover([r['u_phase'] for r in decoded['rows']])
            root, modulus = (3,6) if factor == 3 else (1,2)
            for row in decoded['rows']:
                p,b,r = row['p'],row['exponent_phase'],row['a_residue']
                assert a % p == r
                assert a*a*pow(2,b,p) % p == 1
                root += modulus * ((r-root) * pow(modulus,-1,p) % p)
                modulus *= p
            assert root == a and modulus == 2*factor*M
        winner = computation['minimum']
        a = int(winner['root'])
        k = a*a
        old_minimum = int(json.loads((STRUCTURE/old_name).read_text())['minimum_positive_odd_root'])
        assert a < old_minimum
        decoded = decode(winner['a_code'],winner['b_code'],winner['translation'])
        cycles = {}
        checked_rows = []
        for row in decoded['rows']:
            p,d,b = row['p'],row['order'],row['exponent_phase']
            current = rem(k-1,p)
            cycle = []
            for n in range(d):
                cycle.append(current)
                current = rem(advance(step,current),p)
            assert current == cycle[0]
            assert [n for n,v in enumerate(cycle) if v == 0] == [b]
            cycles[p] = cycle
            checked_rows.append(dict(row,cycle_closed=True,unique_zero_phase=b,residual_cycle=cycle))
        hits = [[r['p'] for r in decoded['rows'] if cycles[r['p']][n % r['order']] == 0]
                for n in range(2*L)]
        holes = [n for n,hit in enumerate(hits) if not hit]
        assert all(n % 2 == 0 for n in holes)
        assert sum(bool(hits[n]) for n in range(1,2*L,2)) == L
        assert 2*k-1 > max(PRIMES)
        least_hole = min(n for n in holes if n>0)
        b = a
        for _ in range(least_hole//2):
            b = advance(double,b)
        value = k-1
        for _ in range(least_hole):
            value = advance(step,value)
        assert value == (b-1)*(b+1) and 1 < b-1 < b+1 < value
        residue3 = rem(k-1,3)
        residue3_odd = rem(advance(step,residue3),3)
        assert rem(advance(step,residue3_odd),3) == residue3
        if a % 3 != 0:
            assert residue3 == 0 and all(hit or n%2==0 for n,hit in enumerate(hits))
        else:
            assert residue3 != 0 and residue3_odd != 0
        compact = {'a':str(a),'k':str(k),'crt_modulus':str(2*factor*M),
                   'root_digits':len(str(a)),'square_digits':len(str(k)),
                   'a_mod3':a%3,'search_provenance':winner,
                   'permutation5':decoded['permutation5'],'permutation7':decoded['permutation7'],
                   'swap24':decoded['swap24'],'swap32':decoded['swap32'],
                   'sign_masks':decoded['sign_masks'],'rows':decoded['rows']}
        (DIRECTORY/('new_table_'+branch+'.json')).write_text(json.dumps(compact,indent=2)+'\n')
        certificates.append(dict(compact,
            checked_rows=checked_rows,
            previous_radius2_minimum=str(old_minimum),
            previous_to_new_ratio=str(Fraction(old_minimum,a)),
            old_minimum_strictly_improved=True,
            all_240_witnesses_reconstructed=True,
            odd_classes_covered=L,
            even_classes_covered=sum(bool(hits[n]) for n in range(0,2*L,2)),
            uncovered_classes=holes,
            proper_factor_bound=True,
            first_fixed_prime_hole={'n':least_hole,'value':str(value),'left_factor':str(b-1),'right_factor':str(b+1)},
            P_union_3_full_cover=(a%3!=0)))
    overlap_count = L//240
    family_size = factorial(4)*factorial(7)*4
    translated_shapes = family_size*L//overlap_count
    distinct_root_classes = translated_shapes*2**len(PRIMES)
    assert distinct_root_classes == computation['left_count']*computation['right_count']*computation['shift_count']
    input_report = json.loads((DIRECTORY/'family_input.json').read_text())
    assert distinct_root_classes == input_report['odd_root_classes_per_branch']
    result = {'schema':'RIESEL_FULL_PERMUTATION_FAMILY_VERIFICATION_V1',
              'researcher_id':'EM-DIRECT-970E1C',
              'research_activity_id':'RA-D2EC212845B63844081F9A14',
              'status':'AUTHOR_PROOF_AND_EXACT_FINITE_COMPUTATION; NOT_INDEPENDENT_PROJECT_REVIEW',
              'project_source_commit':prior_result['project_source_commit'],
              'project_source_blobs':prior_result['project_source_blobs'],
              'source_blobs_verified':True,
              'native_carrier':'Fixed arbitrary X6 anchor; internal integer residual registers; singleton positive BRC. Exponent is not physical time.',
              'shared_prime_order_proof':str((PRIOR/'results.json').relative_to(ROOT)),
              'shared_prime_order_proof_sha256':sha256((PRIOR/'results.json').read_bytes()).hexdigest(),
              'group_actions':group_action_counts,
              'distinct_translation_shape_classes':family_size//overlap_count,
              'distinct_translated_phase_vectors':translated_shapes,
              'odd_root_classes_per_branch':distinct_root_classes,
              'certificates':certificates,
              'scope':'Exact minimum in the specified permutation/swap/translation/sign family in each branch. Not a classification or minimum of all fixed-P covers or all Riesel squares.'}
    (DIRECTORY/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'source_blobs_verified':True,
                      'per_branch_class_count':result['odd_root_classes_per_branch'],
                      'certificates':[{k:c[k] for k in ['a','k','a_mod3','root_digits','square_digits','odd_classes_covered','even_classes_covered','P_union_3_full_cover']} for c in certificates]},indent=2))


if __name__ == '__main__':
    main()
