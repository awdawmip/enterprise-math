#!/usr/bin/env python3
"""Native integer BRC execution of the new 43-observer cost-eight root.

The actual run covers one full coverage-predicate period (7560 updates).
The separate sufficient prime-residue-value period is 60480, not executed here.
All 45 prime readouts retain their cofactors, and a native joint mixed-radix
readout is recomposed to the complete integer at every step.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
import json
from math import gcd, lcm, prod
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
NATIVE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
NATIVE_BLOBS = {
    'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
    'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
    'brc_rational_holonomy.py':'2591640fe348da9cd7f293a957bea9ae92c82943',
    'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb',
}
P = (7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417)
P_ORDERS = (3,8,5,20,35,48,28,7,15,24,16,70,21,64,48,60,84,105,32,64)
H = {0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,
     55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100}
A_STAR = 690786768637635218740714348513373826260012289
M = 1397394912916194098609132326092145093313722687204526281
R1_EXTRA = (5,13,11,61,331,19,37,73,109)
R2_EXTRA = (433,38737)
T_PRIMES = (181,577,631,23311,54001,87211,246241,262657,279073,
            18837001,29247661,487824887233)
T = 35095524795781473254136196580356738045833417602831290421525609131
RT = 21450781839625171583347380029424471704699683386785900439176732195
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
ROOT = 125881617004399660936368886076947194311916726055055408371127347321463572549463017011507634869211696849333543777014426253559019210427608296334538652533279482688323
NEW = (33975937,138991501037953)
EXTRA_ORDERS = {
    5:4,13:12,11:10,61:60,331:30,19:18,37:36,73:9,109:36,
    433:72,38737:72,181:180,577:144,631:45,23311:45,54001:180,
    87211:54,246241:108,262657:27,279073:108,18837001:90,
    29247661:180,487824887233:144,33975937:216,138991501037953:216,
}
ROWS = ((5,1),(13,0),(19,4),(73,1),(38737,34),(246241,34),
        (33975937,16),(138991501037953,52))


def git_blob(data):
    return sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def prime_factors(n):
    out, d = set(), 2
    while d*d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def unsigned_bytes(n):
    return n.to_bytes((n.bit_length()+7)//8, 'big')


def digest_integer(target, n):
    data = unsigned_bytes(n)
    target.update(len(data).to_bytes(8, 'big'))
    target.update(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path,
                        help='Directory containing the pinned enterprise_math package, normally repository src/.')
    parser.add_argument('--output', type=Path, default=HERE/'native_cost8_certificate.json')
    args = parser.parse_args()
    if args.source_dir is None:
        args.source_dir = next((candidate for ancestor in (HERE,*HERE.parents)
                                for candidate in (ancestor/'src',ancestor/'vendor_src')
                                if (candidate/'enterprise_math/brc_transport.py').is_file()),None)
    if args.source_dir is None:
        parser.error('Pass --source-dir pointing to the frozen native package.')

    # The four scientific dependencies are checked once, before importing them.
    source_checks = {}
    for filename, expected in NATIVE_BLOBS.items():
        observed = git_blob((args.source_dir/'enterprise_math'/filename).read_bytes())
        assert observed == expected, (filename,observed,expected)
        source_checks[filename] = observed
    sys.path.insert(0,str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits, recompose

    step = EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])
    twice = step.then(step)
    assert step.entries == ((Fraction(1),Affine(((2,),),(1,)),1),)
    assert twice.entries == ((Fraction(1),Affine(((4,),),(3,)),1),)

    def evaluate(effect, value):
        (point, weight), = effect.evaluate((value,)).items()
        assert weight.entries == ((Fraction(1),1),)
        assert point[0].denominator == 1
        return int(point[0])

    fixed43 = tuple(sorted(set(P+R1_EXTRA+R2_EXTRA+T_PRIMES)))
    channels = tuple(sorted(set(fixed43+NEW)))
    assert len(fixed43) == 43 and len(channels) == 45
    assert prod(P) == M and prod(T_PRIMES) == T
    assert A3 % T == ROOT % T == RT
    assert (ROOT-A3) % S3 == 0
    assert S3 == 6*prod(fixed43)
    assert (ROOT-A_STAR) % (6*M) == 0
    assert ROOT % 80754838636615 == 12926327728523
    assert (ROOT % 433,ROOT % 38737) == (0,38733)
    assert (ROOT % 246241,ROOT % 487824887233) == (182629,487823838657)
    assert (ROOT % NEW[0],ROOT % NEW[1]) == (27805045,78995000769671)
    assert all(ROOT % q == A3 % q for q in fixed43)
    orders = dict(zip(P,P_ORDERS))
    orders.update(EXTRA_ORDERS)
    assert set(orders) == set(channels)
    for q,d in orders.items():
        assert pow(2,d,q) == 1
        assert all(pow(2,d//p,q) != 1 for p in prime_factors(d))
    selected = {q for q,c in ROWS}
    dictionary = set(P)|selected
    assert len(selected) == 8 and len(dictionary) == 28
    coverage_period = lcm(210,*(orders[q] for q in selected))
    residue_period = lcm(*(orders[q] for q in channels))
    assert coverage_period == 7560 and residue_period == 60480
    assert lcm(*(orders[q] for q in P)) == 6720
    for q,c in ROWS:
        assert ROOT*ROOT*pow(4,c,q) % q == 1
    assert 2*ROOT*ROOT-1 > max(channels)
    prefix_sets = [set(q for q,c in ROWS[:i]) for i in range(9)]
    joint_modulus = prod(channels)
    radix_weights, radix_product = [],1
    for q in channels:
        radix_weights.append(radix_product)
        radix_product *= q
    assert radix_product == joint_modulus

    x = scalar_x = previous_even = ROOT*ROOT-1
    reference_x = A3*A3-1
    states_digest, joint_digest, residue_digest = sha256(),sha256(),sha256()
    missing = [0]*9
    private_dictionary, private_supplement = {},{}
    channel_hit_counts = {q:0 for q in channels}
    native_single = native_double = prime_reads = joint_reads = joint_recompose = 0
    fixed_comparisons = scalar_comparisons = formula_comparisons = 0
    started = time.monotonic()
    for n in range(1,coverage_period+1):
        x = evaluate(step,x)
        native_single += 1
        scalar_x = 2*scalar_x+1
        reference_x = 2*reference_x+1
        assert x == scalar_x
        scalar_comparisons += 1
        assert x == (ROOT*ROOT << n)-1
        formula_comparisons += 1
        if n % 2 == 0:
            assert evaluate(twice,previous_even) == x
            native_double += 1
            previous_even = x
        digest_integer(states_digest,x)
        hits, residues, cofactors = set(),{},{}
        for q in channels:
            quotient,(residual,) = euclidean_digits(x,(q,))
            prime_reads += 1
            assert (quotient,residual) == divmod(scalar_x,q)
            assert quotient*q+residual == x and 0 <= residual < q
            assert residual == (ROOT*ROOT*pow(2,n,q)-1) % q
            residues[q],cofactors[q] = residual,quotient
            digest_integer(residue_digest,residual)
            if q in fixed43:
                assert residual == reference_x % q
                fixed_comparisons += 1
            if residual == 0:
                assert 1 < q < x
                hits.add(q)
                channel_hit_counts[q] += 1

        quotient,digits = euclidean_digits(x,channels)
        joint_reads += 1
        assert len(digits) == len(channels)
        assert all(0 <= d < q for d,q in zip(digits,channels))
        packed = sum(d*w for d,w in zip(digits,radix_weights))
        assert (quotient,packed) == divmod(scalar_x,joint_modulus)
        assert quotient*joint_modulus+packed == x
        assert recompose(quotient,digits,channels) == x
        joint_recompose += 1
        digest_integer(joint_digest,quotient)
        for d in digits:
            digest_integer(joint_digest,d)

        old_hole = not bool(hits & set(P))
        assert old_hole == (n % 2 == 0 and (n//2) % 105 in H)
        for q,c in ROWS:
            assert (q in hits) == (n % orders[q] == (2*c) % orders[q])
        if old_hole:
            for i,subset in enumerate(prefix_sets):
                if not hits & subset:
                    missing[i] += 1
            supplement_hits = hits & selected
            assert supplement_hits
            if len(supplement_hits) == 1:
                q, = supplement_hits
                private_supplement.setdefault(q,{'n':n,'state_hex':hex(x),
                    'cofactor_hex':hex(cofactors[q]),'residue':0})
        dictionary_hits = hits & dictionary
        assert dictionary_hits
        if len(dictionary_hits) == 1:
            q, = dictionary_hits
            private_dictionary.setdefault(q,{'n':n,'state_hex':hex(x),
                'cofactor_hex':hex(cofactors[q]),'residue':0})
        if n == coverage_period:
            final = {'index':n,'state_hex':hex(x),'state_bits':x.bit_length(),
                'state_sha256_unsigned_big_endian':sha256(unsigned_bytes(x)).hexdigest(),
                'joint_cofactor_hex':hex(quotient),'joint_mixed_radix_digits':digits,
                'joint_packed_remainder':str(packed),'prime_residues':residues,
                'all_prime_cofactors_hex':{q:hex(c) for q,c in cofactors.items()},
                'reference_root_state_hex':hex(reference_x),
                'full_residue_period_executed':False,
                'residue_vector_equals_initial':all(residues[q] == (ROOT*ROOT-1)%q for q in channels)}
        if n % 2520 == 0:
            print(json.dumps({'native_steps':n,'target':coverage_period,
                              'elapsed_seconds':round(time.monotonic()-started,3)}),flush=True)

    assert missing[-1] == 0 and missing[0] == coverage_period*6//35
    assert set(private_supplement) == selected
    assert set(private_dictionary) == dictionary
    assert native_single == joint_reads == joint_recompose == scalar_comparisons == formula_comparisons == 7560
    assert native_double == 3780 and prime_reads == 340200 and fixed_comparisons == 325080
    counts = {'native_single_step_updates':native_single,
        'native_two_step_evaluations':native_double,'native_effect_evaluations':native_single+native_double,
        'native_individual_prime_readouts':prime_reads,'native_joint_readouts':joint_reads,
        'native_joint_recompositions':joint_recompose,
        'native_euclidean_digits_calls':prime_reads+joint_reads,
        'scalar_full_integer_comparisons':scalar_comparisons,
        'closed_formula_full_integer_comparisons':formula_comparisons,
        'individual_division_comparisons':prime_reads,'individual_formula_comparisons':prime_reads,
        'fixed43_direct_reference_comparisons':fixed_comparisons,
        'joint_scalar_division_comparisons':joint_reads}
    result = {'schema':'riesel-fixed43-cost-eight-native-v1',
        'status':'PASS_AUTHOR_NATIVE_EXECUTION_NOT_INDEPENDENT_REVIEW',
        'native_source_commit':NATIVE_COMMIT,'native_source_blobs':source_checks,
        'reused_harness':'riesel_seven_cover_20261124/native/verify_native.py',
        'root':str(ROOT),'root_digits':len(str(ROOT)),
        'root_scope':'Minimum of the eight explicitly constructed progressions; not asserted global cost-eight minimum.',
        'fixed_R3_base':str(A3),'fixed_R3_step':str(S3),
        'fixed43_root_residues':{q:ROOT%q for q in fixed43},
        'fixed43_channels':fixed43,'readout_channels':channels,'channel_count':len(channels),
        'exact_base2_orders':orders,
        'ordered_supplement_rows':[{'q':q,'phase_u':c,'order2':orders[q],'root_residue':ROOT%q} for q,c in ROWS],
        'coverage_predicate_period':coverage_period,'native_updates_actually_executed':native_single,
        'complete_coverage_periods_executed':1,
        'sufficient_residue_value_period':residue_period,'complete_residue_value_period_executed':False,
        'uncovered_counts_after_prefixes':missing,'native_zero_hit_counts':channel_hit_counts,
        'proper_private_supplement_witnesses':private_supplement,
        'proper_private_dictionary_witnesses':private_dictionary,
        'joint_modulus':str(joint_modulus),'final_complete_state_and_readouts':final,
        'native_integer_stream_sha256':states_digest.hexdigest(),
        'native_joint_cofactor_digit_stream_sha256':joint_digest.hexdigest(),
        'native_prime_residue_stream_sha256':residue_digest.hexdigest(),
        'actual_counts':counts,'elapsed_seconds':round(time.monotonic()-started,6),
        'coverage_argument':'The inherited old-P hole predicate has period 210. The selected eight prime-zero predicates have the verified orders. Their common coverage period is 7560, actually executed completely with zero uncovered indices. Every hit is a proper prime divisor.',
        'fixed_observer_argument':'The new root differs from A3 by a multiple of S3. Its 43 fixed prime residue values therefore agree with the A3 trajectory for every index; 325080 direct scalar-reference comparisons were executed on indices 1 through 7560.',
        'integer_retention':'Each native step receives the entire previous integer. All prime cofactors and residues represent that integer, and a native 45-radix quotient-chain readout is recomposed exactly at every step. Complete final integers and all final cofactors are retained in hex.',
        'native_semantics':'Fixed X6 anchor, typed integer register, positive singleton BRC weight1/multiplicity1, native update2x+1 and composed4x+3. Prime channels are observations; the arithmetic index does not assert physical time.',
        'mathematical_scope':'This execution validates the explicit compact root, its coverage and lossless readouts. Exact supplementary cost8 uses the inherited all-seven-cover classification. The total cost of this compact root is bounded above by28. Exact total cost28 belongs to the separate coprimalized construction, not this native run.',
        'independent_project_review':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','coverage_period':coverage_period,
        'residue_period':residue_period,'uncovered_counts':missing,'counts':counts,
        'private_dictionary_witnesses':len(private_dictionary),'output':str(args.output)},indent=2))


if __name__ == '__main__':
    main()
