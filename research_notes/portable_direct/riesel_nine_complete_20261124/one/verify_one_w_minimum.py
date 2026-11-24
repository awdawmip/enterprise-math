#!/usr/bin/env python3
"""Exhaust the complete R3 one-W nine-cover class and certify its minimum.

The all-prime one-W classification and complete budget-eight observer are
inherited at their exact v14/v13 scopes. This script uses standard-library
integer arithmetic to enumerate every signed CRT first root, checks the
minimum against the full eight predicate, deletes a redundant old prime,
and verifies 28 pairwise-coprime full integer terms. No native run is claimed.
"""

from itertools import combinations, permutations, product
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
P = [7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417]
P_ORDERS = [3,8,5,20,35,48,28,7,15,24,16,70,21,64,48,60,84,105,32,64]
A = {1,2,10,11,12,16,17,22,25,26,30,31,32}
Z = [29,43,1429,5419]
K = [92737,649657,77158673929,40388473189,118750098349]
F14 = [3361,15790321,88959882481]
F35 = [211,421,86171,106681,122921,152041,664441,1564921,
       7416361,47392381,146919792181,1041815865690181]
J_FAMILIES = {
    'binary': ([193,1153,6337,22253377,38941695937,278452876033], [0,4]),
    'ternary': ([33975937,138991501037953], [0,2]),
    'modulo_five': ([61681,4562284561,168692292721,469775495062434961], [0,6,8]),
}
FREE31 = sorted(Z + F14 + F35 + [q for qs,_ in J_FAMILIES.values() for q in qs])
FIXED = {
    7:5,17:10,31:8,41:38,71:11,97:34,113:69,127:119,151:147,241:165,
    257:68,281:261,337:4,641:488,673:107,1321:475,14449:7695,29191:19665,
    65537:4080,6700417:65537,5:3,13:1,19:6,73:37,11:0,61:0,331:0,
    37:0,109:0,433:0,38737:38733,181:0,577:0,631:0,23311:0,54001:0,
    87211:0,246241:182629,262657:0,279073:0,18837001:0,29247661:0,
    487824887233:487823838657,
}
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
EXPECTED = 323364408543007321903311572653400317900622306273030390762905871847856938179871543582589560419967265786024995230650782386881939058243788541171427741450118743
Q7_MINIMUM = 112755110470612891256156246069109596727720684467884590849485136661471023397130974501713495184000901218767521913670185762743636668514043005915407753161112053


def prime_trial(q):
    if q == 2:
        return True
    return q > 2 and q % 2 and all(q % d for d in range(3,isqrt(q)+1,2))


def order_two(q):
    value = 1
    for d in range(1,421):
        value = 2*value % q
        if value == 1:
            return d
    raise AssertionError(('order outside inherited range',q))


def v_pair(q,b):
    r = pow(2,-(4+6*b),q)
    return r,(-r) % q


def j_pair(q,b):
    r = pow(2,-(16+18*b),q)
    return r,(-r) % q


def eight_observer(a):
    retained = {
        name: all(any(a % q in j_pair(q,b) for q in qs) for b in phases)
        for name,(qs,phases) in J_FAMILIES.items()
    }
    zphases = []
    for q in Z:
        bs = [b for b in range(1,6) if a % q in v_pair(q,b)]
        if len(bs) != 1:
            return {'retained':retained,'Z_phases':zphases,'zero_W':False,
                    'complete_predicate':any(retained.values())}
        zphases.append(bs[0])
    if len(set(zphases)) != 4:
        return {'retained':retained,'Z_phases':zphases,'zero_W':False,
                'complete_predicate':any(retained.values())}
    missing = next(b for b in range(1,6) if b not in zphases)
    via14 = all(any(a % q in v_pair(q,b) for q in F14)
                for b in [missing,missing+7])
    points = [v for v in A if v % 7 == missing]
    via35 = len(points) == 2 and all(any(a % q in v_pair(q,b) for q in F35)
                                   for b in points)
    return {'retained':retained,'Z_phases':zphases,'missing_row':missing,
            'via14':via14,'via35':via35,'zero_W':via14 or via35,
            'complete_predicate':any(retained.values()) or via14 or via35}


def all_signed_minima():
    """Each index is the least residue in [0, product(free primes))."""
    groups = []
    best = None
    count = 0
    for kqs in combinations(K,2):
        qs = Z + list(kqs)
        modulus = prod(qs)
        weights = {q:(modulus//q)*pow(modulus//q,-1,q) for q in qs}
        choices = {
            q:{b:[((r-A3)*pow(S3,-1,q) % q)*weights[q] for r in v_pair(q,b)]
               for b in range(21)}
            for q in qs
        }
        for W,r in [(19,0),(73,1)]:
            for missing in range(1,6):
                bs = [b for b in range(21) if b % 7 == missing and b % 3 != r]
                assert len(bs) == 2
                group_best = None
                local_count = 0
                for zbs in permutations([b for b in range(1,6) if b != missing]):
                    for tailbs in [bs,bs[::-1]]:
                        phases = list(zbs) + tailbs
                        for signs in product([0,1],repeat=6):
                            index = sum(choices[q][b][s] for q,b,s in zip(qs,phases,signs)) % modulus
                            a = A3 + S3*index
                            assert 0 < a < S3*modulus
                            if group_best is None or a < group_best['root']:
                                group_best = dict(root=a,R3_index=index,W=W,missing_mod7_row=missing,
                                                  free_primes=qs,v_phases=phases,sign_bits=signs,
                                                  progression_modulus=S3*modulus)
                            count += 1
                            local_count += 1
                assert local_count == 3072
                for q,b,s in zip(group_best['free_primes'],group_best['v_phases'],group_best['sign_bits']):
                    assert group_best['root'] % q == v_pair(q,b)[s]
                groups.append({'W':W,'missing_mod7_row':missing,'K_pair':kqs,
                               'signed_starts':local_count,'minimum':group_best})
                if best is None or group_best['root'] < best['root']:
                    best = group_best
    assert len(groups) == 100 and count == 307200
    assert best['root'] == EXPECTED and best['R3_index'] == 811311504227722
    return best,groups,count


def coverage_and_coprime(a,supplement):
    full = sorted(P + supplement)
    qs = [q for q in full if q != 113]
    assert len(full) == 29 and len(qs) == len(set(qs)) == 28
    orders = {q:order_two(q) for q in full}
    assert all(orders[q] == d for q,d in zip(P,P_ORDERS))
    phases = {q:next(n for n in range(orders[q]) if (a*a*pow(2,n,q)-1) % q == 0)
              for q in full}
    period = lcm(*orders.values())
    assert period == 20160
    private_full = {q:[] for q in full}
    private = {q:[] for q in qs}
    values = {q:(a*a-1) % q for q in full}
    for n in range(1,period+1):
        for q in full:
            values[q] = (2*values[q]+1) % q
            assert (values[q] == 0) == (n % orders[q] == phases[q])
        hits = [q for q in full if values[q] == 0]
        assert hits
        if len(hits) == 1:
            private_full[hits[0]].append(n)
        reduced_hits = [q for q in hits if q != 113]
        assert reduced_hits
        if len(reduced_hits) == 1:
            private[reduced_hits[0]].append(n)
    assert not private_full[113] and all(private[q] for q in qs)
    assert all(values[q] == (a*a-1) % q for q in full)
    assert a*a-1 > max(full)
    # A short symbolic cover of all old-113 hits n=21+28t.
    tclasses = {7:(3,1),92737:(9,2),649657:(9,5),73:(9,8),
                241:(6,3),97:(12,0),673:(12,6)}
    for q,(d,b) in tclasses.items():
        assert orders[q]//gcd(orders[q],28) == d
        assert (a*a*pow(2,21+28*b,q)-1) % q == 0
    assert all(any(t % d == b for d,b in tclasses.values()) for t in range(36))
    # The successful finite witness order. It is a construction, not a
    # universal guarantee of greedy compatibility for arbitrary roots.
    ordering = [649657] + [q for q in qs if q != 649657]
    chosen = []
    rejected = []
    for q in ordering:
        for n in private[q]:
            value = (a*a << n)-1
            conflicts = [(p,m,gcd(value,w)) for p,m,w in chosen if gcd(value,w) != 1]
            if conflicts:
                rejected.append({'assigned_prime':q,'exponent':n,
                                 'conflicts':[[p,m,str(g)] for p,m,g in conflicts]})
                continue
            chosen.append((q,n,value))
            break
        else:
            raise AssertionError(('finite witness search failed',q))
    assert len(chosen) == 28 and max(n for q,n,v in chosen) == 2912
    pairs = []
    for (q,n,value),(p,m,other) in combinations(chosen,2):
        g = gcd(value,other)
        assert g == 1
        pairs.append([q,p,g])
    assert len(pairs) == 378
    terms = []
    for q,n,value in chosen:
        assert value % q == 0 and value > q
        assert [p for p in qs if value % p == 0] == [q]
        terms.append({'assigned_prime':q,'exponent':n,'full_integer_hex':hex(value),
                      'bit_length':value.bit_length(),'quotient_hex':hex(value//q),'remainder':0})
    # A second finite witness set is useful for later cost-preserving
    # refinements: all nine supplemental witnesses must avoid every P prime.
    p_free_private = {q:(private_full[q] if q in supplement else private[q]) for q in qs}
    strong = []
    strong_rejections = []
    for q in ordering:
        for n in p_free_private[q]:
            value = (a*a << n)-1
            conflicts = [(p,m,gcd(value,w)) for p,m,w in strong if gcd(value,w) != 1]
            if conflicts:
                strong_rejections.append({'assigned_prime':q,'exponent':n,
                                          'conflicts':[[p,m,str(g)] for p,m,g in conflicts]})
                continue
            strong.append((q,n,value))
            break
        else:
            raise AssertionError(('P-free seed witness search failed',q))
    assert len(strong) == 28 and max(n for q,n,v in strong) == 6512
    strong_pairs = []
    for (q,n,value),(p,m,other) in combinations(strong,2):
        g = gcd(value,other)
        assert g == 1
        strong_pairs.append([q,p,g])
    assert len(strong_pairs) == 378
    strong_terms = []
    p_product = prod(P)
    for q,n,value in strong:
        assert value % q == 0 and value > q
        assert [p for p in qs if value % p == 0] == [q]
        p_gcd = gcd(value,p_product)
        if q in supplement:
            assert p_gcd == 1
        strong_terms.append({'assigned_prime':q,'exponent':n,'full_integer_hex':hex(value),
                             'bit_length':value.bit_length(),'quotient_hex':hex(value//q),
                             'remainder':0,'gcd_with_old_P_product':str(p_gcd),
                             'supplemental_witness':q in supplement})
    assert sum(row['supplemental_witness'] for row in strong_terms) == 9
    # Exact private geometry of q1429: n=68+84*i. This is a useful finite
    # seed invariant, not a completed unbounded-refinement theorem.
    private1429 = []
    p_free1429 = []
    for i in range(240):
        n = 68+84*i
        p_free = all((a*a*pow(2,n,p)-1) % p for p in P)
        lone = [q for q in full if (a*a*pow(2,n,q)-1) % q == 0] == [1429]
        assert p_free == (i % 5 in [1,3])
        assert lone == (i % 5 in [1,3] and i % 3 != 2)
        if p_free:p_free1429.append(i)
        if lone:private1429.append(i)
    assert len(private1429) == 64
    return {'full_dictionary':full,'optimal_reduced_dictionary':qs,
            'base2_orders':orders,'zero_phases':phases,'complete_period':period,
            'scalar_recurrence_readouts':period*len(full),'uncovered_full':0,'uncovered_reduced':0,
            'full_dictionary_private_counts':{q:len(ns) for q,ns in private_full.items()},
            'reduced_dictionary_private_counts':{q:len(ns) for q,ns in private.items()},
            'redundant_old_prime':113,'old113_hit_parameterization':'n=21+28*t',
            'old113_cover_classes_in_t':tclasses,
            'witness_selection_order':ordering,'rejected_witness_candidates':rejected,
            'selected_terms':terms,'maximum_witness_exponent':2912,
            'pairwise_gcds':pairs,'pairwise_gcd_count':378,'all_pairwise_gcds_one':True,
            'P_free_refinement_seed':{
                'selected_terms':strong_terms,'maximum_witness_exponent':6512,
                'pairwise_gcds':strong_pairs,'pairwise_gcd_count':378,
                'all_pairwise_gcds_one':True,'P_free_supplemental_witness_count':9,
                'rejected_witness_candidates':strong_rejections,
                'direct_delta_lower_bound':9,'direct_total_lower_bound':28,
                'delta_lower_bound_uses_eight_observer':False,
                'q1429_private_geometry':{'parameterization':'n=68+84*i',
                    'P_free_condition':'i=1 or 3 modulo 5',
                    'private_condition':'i=1 or 3 modulo 5 and i!=2 modulo 3',
                    'checked_i_period':240,'private_i_count':64,
                    'private_i_residues':private1429,
                    'unbounded_refinement_claimed':False}},
            'proper_factor_basis':'a^2-1 exceeds every selected prime',
            'native_BRC_execution_claimed':False}


def serializable(value):
    """Keep large integers exact in JSON clients with IEEE-754 numbers."""
    if isinstance(value,bool) or value is None:
        return value
    if isinstance(value,int):
        return str(value) if abs(value) > 2**53-1 else value
    if isinstance(value,dict):
        return {str(k):serializable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [serializable(v) for v in value]
    return value


def constant_cost_progression(a,coverage):
    exponents = [row['exponent'] for row in coverage['selected_terms']]
    differences = sorted({abs(n-m) for n,m in combinations(exponents,2)})
    assert differences and differences[0] > 0
    joint = lcm(S3,prod(FREE31),92737*649657)
    for d in differences:
        joint = lcm(joint,(1 << d)-1)
    assert joint % S3 == 0 and joint % prod(FREE31) == 0
    assert all(joint % q == 0 for q in coverage['optimal_reduced_dictionary'])
    assert all(joint % ((1 << d)-1) == 0 for d in differences)
    return {'first_root':str(a),'modulus_hex':hex(joint),'modulus_bits':joint.bit_length(),
            'distinct_witness_differences':differences,
            'definition':'L=lcm(S3, product(FREE31), 92737*649657, {2^d-1: d=abs(n_i-n_j), i<j})',
            'progression':'a=first_root+L*t, every integer t>=0',
            'exact_supplementary_minimum':9,'exact_unrestricted_total_minimum':28,
            'proof_basis':'Fixed root residues preserve the full cover and false complete eight predicate; gcd(F_n,F_m)=gcd(F_min(n,m),2^abs(n-m)-1) preserves all coprime witnesses',
            'infinite_claim_is_algebraic_not_finite_extrapolation':True}


def main():
    assert 0 < A3 < S3 and len(FIXED) == 43 and S3 == 6*prod(FIXED)
    assert all(A3 % q == r for q,r in FIXED.items())
    assert gcd(S3,prod(Z+K)) == 1 and len(FREE31) == len(set(FREE31)) == 31
    certified = sorted(set(P+[5,13,19,73]+Z+K))
    assert all(prime_trial(q) for q in certified)
    best,groups,count = all_signed_minima()
    a = best['root']
    observer = eight_observer(a)
    assert observer['complete_predicate'] is False
    assert all(a % q == r for q,r in FIXED.items())
    supplement = [5,13,best['W']]+best['free_primes']
    coverage = coverage_and_coprime(a,supplement)
    progression = constant_cost_progression(a,coverage)
    assert a > Q7_MINIMUM and (Q7_MINIMUM-A3)//S3 == 282899156086651
    assert Q7_MINIMUM % S3 == a % S3 == A3
    result = {
        'schema':'riesel-r3-complete-one-W-nine-cover-minimum-v15',
        'status':'PASS_EXACT_CRT_ENUMERATION_PERIODIC_COVER_AND_FULL_INTEGER_GCD',
        'R3':{'A3':A3,'S3':S3,'fixed43':FIXED},
        'inherited_complete_one_W_classification':
            '9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/prefix/proof.md',
        'inherited_complete_eight_observer':
            'e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124/observer/proof.md',
        'deterministically_trial_verified_primes':certified,
        'phase_dictionaries':4800,'signed_CRT_starts':count,'group_count':len(groups),
        'group_minima':groups,'global_one_W_minimum':best,'minimum_digits':len(str(a)),
        'complete_eight_observer31_residues':{q:a % q for q in FREE31},
        'complete_eight_observer_result':observer,'supplementary_minimum':9,
        'unrestricted_total_minimum':28,'coverage_and_coprime_certificate':coverage,
        'infinite_constant_cost_progression':progression,
        'smaller_known_Q7_conditional_minimum':Q7_MINIMUM,
        'same_R3_and_same_delta_different_tau':{
            'new_one_W_minimum':{'root':a,'delta':9,'tau':28},
            'inherited_Q7_minimum':{'root':Q7_MINIMUM,'delta':9,'tau':29},
            'inherited_Q7_total_cost_source':'9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/totals/proof.md',
            'same_fixed43_complete_future_trajectories':True},
        'minimum_scope':'Entire R3 exact-cost-nine roots admitting a nine-prime supplement containing exactly one of 19 and 73',
        'proof_of_minimum':'Every positive root in a signed CRT progression is at least its first root; the global first root already fails the complete eight predicate',
        'unbounded_progressions_discarded_due_to_cost8_first_root':False,
        'native_semantics':'Full integer register at fixed Heartbeat X6 anchor; x -> 2*x+1; residue projections preserve only declared observation predicates',
        'native_BRC_execution_claimed':False,'independent_project_review_claimed':False,
    }
    target = HERE/'one_w_minimum_certificate.json'
    target.write_text(json.dumps(serializable(result),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','signed_CRT_starts':count,'minimum':str(a),
                      'R3_index':best['R3_index'],'delta':9,'tau':28,
                      'period':coverage['complete_period'],'full_integer_witnesses':28,
                      'gcd_pairs':378,'maximum_witness_exponent':2912,
                      'additional_P_free_seed_witnesses':28,'P_free_supplemental_witnesses':9,
                      'P_free_seed_gcd_pairs':378,'P_free_seed_maximum_exponent':6512,
                      'certificate':str(target)}))


if __name__ == '__main__':
    main()
