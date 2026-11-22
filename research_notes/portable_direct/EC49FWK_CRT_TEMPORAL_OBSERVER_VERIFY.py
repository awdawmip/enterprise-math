#!/usr/bin/env python3
"""EC49FWK: exact temporal probes for the frozen EC49/Farey affine residue observer.
Python 3 standard library only; all operations are exact integer/rational.
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd

MOD, MASK, CRT_PERIOD, PRIME = 10, (1 << 10) - 1, 110, 11
SLOPES = {(0, 0): {3}, (0, 1): {0, 3, 4, 'inf'},
          (1, 0): {2, 3, 4, 'inf'}, (1, 1): {2, 3}}

def mod_p(x):
    return x.numerator * pow(x.denominator, -1, PRIME) % PRIME

def frozen_p10_from_original_rows():
    # The projective parent values and exclusion criterion are frozen, not refit.
    U = Fraction(4822040484, 8132285009)
    GAMMA = Fraction(141024, 1653649)
    u, gamma, inv = mod_p(U), mod_p(GAMMA), pow(637, -1, PRIME)
    rows = []
    for z in range(PRIME):
        la, lb = (637-3*z)*inv % PRIME, u*(1+gamma*z) % PRIME
        aa, bb = (1-(1-z)*la) % PRIME, (1-(1-z)*lb) % PRIME
        rows.append((z, aa, bb, la, lb))
    c, d = -3*inv % PRIME, u*gamma % PRIME
    return {(h, n) for h in range(MOD) for n in range(MOD)
            if all((pow(aa, h, PRIME)*pow(la, n, PRIME)
                    - pow(bb, h, PRIME)*pow(lb, n, PRIME))
                   * pow((la-lb) % PRIME, -1, PRIME) % PRIME
                   for z, aa, bb, la, lb in rows if z != 3)
            and (pow(c, h+n, PRIME)-pow(d, h+n, PRIME))
                   * pow((c-d) % PRIME, -1, PRIME) % PRIME}

def frozen_p10_from_four_fibers():
    out = set()
    for h in range(MOD):
        for n in range(MOD):
            if h % 5 == n % 5 == 0:
                continue
            slope = 'inf' if h % 5 == 0 else n * pow(h % 5, -1, 5) % 5
            if slope in SLOPES[(h % 2, n % 2)]:
                out.add((h, n))
    return out

def support_word(a, b, p10):
    # Same exact determinant-one affine base-point convention as EC49FWJ.
    h0, n0 = next((h, n) for h in range(MOD) for n in range(MOD)
                  if ((b-a)*h-a*n+1) % MOD == 0)
    return sum(1 << t for t in range(MOD)
               if ((h0+a*t) % MOD, (n0+(b-a)*t) % MOD) in p10)

def sites(mask, n=MOD):
    return [t for t in range(n) if (mask >> t) & 1]

def reflect(mask, center):
    return sum(1 << ((center-t) % MOD) for t in sites(mask))

def defects(mask):
    return tuple((mask ^ reflect(mask, c)).bit_count() for c in range(MOD))

def fibers(words, weighted):
    result = defaultdict(list)
    for w in sorted(words):
        result[(defects(w), w.bit_count()) if weighted else defects(w)].append(w)
    return result

def circular_gaps(event_positions, period):
    v = sorted(event_positions)
    assert v
    return [((v[(i+1) % len(v)]-v[i]) % period) or period
            for i in range(len(v))]

def predicted_hole_gap(difference):
    # The gaps around each deleted event merge; no two consecutive events
    # can be deleted as each adjacent gap <= 10 < 11.
    g = circular_gaps(difference, MOD)
    return max(g[i-1]+g[i] for i in range(len(g)))

def bits_110(word, hole):
    return [int(((word >> (t % MOD)) & 1) and
                (hole is None or t % PRIME != hole))
            for t in range(CRT_PERIOD)]

def backward_deficits(bits):
    period = len(bits)
    assert any(bits)
    return [next(k for k in range(period) if bits[(t-k) % period])
            for t in range(period)]

def horizon(trace1, trace2):
    assert len(trace1) == len(trace2)
    difference = [i for i, (x,y) in enumerate(zip(trace1,trace2)) if x != y]
    length = len(trace1)
    return max(circular_gaps(difference,length)), len(difference), difference

def worst_start(trace1, trace2, horizon_length):
    # Find a start with an equal prefix of L-1 sites and inequality on Lth.
    T = len(trace1)
    for t0 in range(T):
        if all(trace1[(t0+j)%T] == trace2[(t0+j)%T]
               for j in range(horizon_length-1)) and \
           trace1[(t0+horizon_length-1)%T] != trace2[(t0+horizon_length-1)%T]:
            return t0
    raise AssertionError('no tight witness')

def main():
    original = frozen_p10_from_original_rows()
    fibers_p10 = frozen_p10_from_four_fibers()
    assert len(original) == 44 and original == fibers_p10
    directions = [(a,b) for a in range(MOD) for b in range(MOD)
                  if gcd(gcd(a,b),MOD)==1]
    assert len(directions) == 72
    words = {support_word(a,b,original) for a,b in directions}
    assert len(words) == 50
    results = {}
    raw_rows = []
    for weighted in (False,True):
        groups = fibers(words,weighted)
        pairs = [tuple(v) for v in groups.values() if len(v)==2]
        assert len(groups)==(40 if weighted else 38)
        assert len(pairs)==(10 if weighted else 12)
        assert max(map(len,groups.values()))==2
        # General finite CRT gap theorem over all 1023 nonempty base masks.
        for D in range(1,1<<MOD):
            dsites = sites(D)
            for z in range(PRIME):
                E=[t for t in range(CRT_PERIOD) if (D>>(t%MOD))&1
                   and t%PRIME!=z]
                assert max(circular_gaps(E,CRT_PERIOD)) == predicted_hole_gap(dsites)
            E_full=[t for t in range(CRT_PERIOD) if (D>>(t%MOD))&1]
            assert max(circular_gaps(E_full,CRT_PERIOD))==max(circular_gaps(dsites,MOD))
        case_rows=[]
        for i,(A,B) in enumerate(sorted(pairs)):
            D=sites(A^B)
            base_gaps=circular_gaps(D,MOD)
            case={'support_a':A, 'support_b':B, 'difference':D,
                  'base_max_gap':max(base_gaps),
                  'punctured_predicted_max_gap':predicted_hole_gap(D)}
            for name,hole in [('full',None),('one_hole_z0',0)]:
                E1,E2=bits_110(A,hole),bits_110(B,hole)
                r1,r2=backward_deficits(E1),backward_deficits(E2)
                occ,nocc,diffo=horizon(E1,E2)
                rr,nrr,diffr=horizon(r1,r2)
                assert occ == (max(base_gaps) if hole is None else predicted_hole_gap(D))
                assert rr<=occ
                case[name]={'membership_horizon':occ,
                            'backward_deficit_horizon':rr,
                            'membership_difference_sites':nocc,
                            'backward_deficit_difference_sites':nrr,
                            'worst_start_membership':worst_start(E1,E2,occ),
                            'worst_start_deficit':worst_start(r1,r2,rr)}
            case_rows.append(case)
        key='weighted' if weighted else 'unweighted'
        results[key]={'fiber_count':len(groups),'collision_pairs':len(pairs),
                      'full':{'membership_max_horizon':max(x['full']['membership_horizon'] for x in case_rows),
                              'deficit_max_horizon':max(x['full']['backward_deficit_horizon'] for x in case_rows)},
                      'single_hole':{'membership_max_horizon':max(x['one_hole_z0']['membership_horizon'] for x in case_rows),
                                     'deficit_max_horizon':max(x['one_hole_z0']['backward_deficit_horizon'] for x in case_rows)},
                      'pair_tables':case_rows}
        if weighted:raw_rows=case_rows
    # Explicit sharp horizon witness in the weighted fiber: two sites separated by 5.
    witnesses=[r for r in raw_rows if r['difference']==[2,7]]
    assert len(witnesses)==1
    witness=witnesses[0]
    a,b=witness['support_a'],witness['support_b']
    b1,b2=bits_110(a,0),bits_110(b,0)
    r1,r2=backward_deficits(b1),backward_deficits(b2)
    start=witness['one_hole_z0']['worst_start_deficit']
    witness_out={ 'pair':[a,b], 'difference':[2,7], 'start':start,
                  'phases':[(start+i)%110 for i in range(10)],
                  'deficit_a':[r1[(start+i)%110] for i in range(10)],
                  'deficit_b':[r2[(start+i)%110] for i in range(10)],
                  'membership_a':[b1[(start+i)%110] for i in range(10)],
                  'membership_b':[b2[(start+i)%110] for i in range(10)]}
    assert witness_out['deficit_a'][:9]==witness_out['deficit_b'][:9]
    assert witness_out['deficit_a'][9]!=witness_out['deficit_b'][9]
    # Check phase independence for all eleven hole positions, just once per weighted fiber.
    for A,B in [tuple(v) for v in fibers(words,True).values() if len(v)==2]:
        D=sites(A^B)
        for hole in range(PRIME):
            a,b=bits_110(A,hole),bits_110(B,hole)
            assert horizon(a,b)[0]==predicted_hole_gap(D)
            assert horizon(backward_deficits(a),backward_deficits(b))[0] <= predicted_hole_gap(D)
    output={'status':'ALL PASS','identifier':'EC49FWK','scientific_pin':'BRC16943',
            'source_parent':'EC49FWJ@95ab4672c9251e155c44049b007330277fa83603',
            'coverage':{'projective_p10_positions':100,'source_primitive_directions':72,
                        'distinct_source_supports':50,
                        'all_nonempty_ten_site_difference_masks':1023,
                        'mod11_hole_phases':11,
                        'exhaustive_gap_formula_checks':1023*11,
                        'full_reflection_centers':10,
                        'crt_period':110},
            'results':results, 'sharp_weighted_witness':witness_out,
            'scope':'Finite affine-residue observer; t is the determinant-one line parameter. Not a full moving-Farey or native X6 dynamic.'}
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
