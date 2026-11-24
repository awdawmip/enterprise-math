#!/usr/bin/env python3
"""Exact cost-gap-one seeds for the general R3 dyadic refinement theorem.

The proof supplies every k>=1 by Bang primes of distinct base-two orders.
This standard-library script verifies the fixed-prime compatibility and
constructs ordinary exact-cost examples for k=1,2 (delta=10,11). All gcd
checks use complete integer terms, reduced by the exact difference identity.
No native BRC execution or independent project Review is claimed.
"""

from itertools import combinations
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
P = [7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417]
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
BASE_ROOT = 323364408543007321903311572653400317900622306273030390762905871847856938179871543582589560419967265786024995230650782386881939058243788541171427741450118743
BASE_EXTRA = [5,13,73,29,43,5419,92737,649657]
PARENT = 1429
CASE_PRIMES = {
    1: {'D':[3361], 'T':15790321},
    2: {'D':[3361,2017], 'T':5153},
}


def factors(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:n //= p
        p += 1
    if n > 1:out.append(n)
    return out


def exact_order(q,d):
    return pow(2,d,q) == 1 and all(pow(2,d//p,q) != 1 for p in factors(d))


def prime_trial(q):
    return q >= 2 and all(q % d for d in range(2,isqrt(q)+1))


def crt_step(a,m,r,q):
    assert gcd(m,q) == 1
    return a + m*((r-a)*pow(m,-1,q) % q),m*q


def small_crt(conditions):
    a,m = 0,1
    for r,q in conditions:a,m = crt_step(a,m,r,q)
    return a


def new_indices(k):
    ds = []
    for j in range(1,k+1):
        i = small_crt([(3+(1 << (j-1)),1 << j),(3,9),(1,5)])
        ds.append({'kind':'D','level':j,'parent_phase':(3+(1 << (j-1))) % (1 << j),
                   'parent_period':1 << j,'i':i,'n':68+84*i,'base2_order':84*(1 << j)})
    i = small_crt([(3,1 << max(k,2)),(3,9),(1,5)])
    ds.append({'kind':'T','level':k,'parent_phase':3 % (1 << k),
               'parent_period':1 << k,'i':i,'n':68+84*i,'base2_order':28*(1 << k)})
    return ds


def fixed_geometry():
    source = json.loads((HERE/'base_geometry.json').read_text())
    fixed_orders = {int(q):d for q,d in source['fixed_orders'].items()}
    fixed_phases = {int(q):b for q,b in source['fixed_phases'].items()}
    fixed = {q:A3 % q for q in fixed_orders}
    witnesses = {int(q):n for q,n in source['witnesses'].items()}
    base = sorted((set(P)-{113})|set(BASE_EXTRA))
    assert len(fixed) == 43 and S3 == 6*prod(fixed)
    assert 0 < A3 < S3 and BASE_ROOT % S3 == A3 and A3 % 6 == 3
    assert set(witnesses) == set(base) and len(base) == 27
    assert all(exact_order(q,d) for q,d in fixed_orders.items())
    assert max(fixed_orders.values()) == 180
    assert not set(fixed_orders.values()) & {56,112,168}
    for q,d in fixed_orders.items():
        actual = [n for n in range(d) if (A3*A3*pow(2,n,q)-1) % q == 0]
        assert actual == ([] if fixed_phases[q] is None else [fixed_phases[q]])
    base_orders = dict(fixed_orders)
    for q,d in [(29,28),(43,14),(5419,42),(92737,63),(649657,63)]:
        assert exact_order(q,d)
        base_orders[q] = d
    phases = {q:next(n for n in range(base_orders[q]) if (BASE_ROOT*BASE_ROOT*pow(2,n,q)-1) % q == 0)
              for q in base}
    hits = {}
    for q,n in witnesses.items():
        assert n % 28 != 12
        assert [p for p in base if n % base_orders[p] == phases[p]] == [q]
        hits[q] = [p for p,b in fixed_phases.items() if b is not None and n % fixed_orders[p] == b]
        if q in P:
            assert hits[q] == [q] and n % 2 == 1
        elif q in [5,13,73]:
            assert hits[q] == [q]
        elif q == 649657:
            assert hits[q] == [19]
        else:
            assert not hits[q]
        if q not in P:
            assert all(n % fixed_orders[p] != fixed_phases[p] for p in P)
    assert max(witnesses.values()) == 4640
    # The corrected shift has uniform incidence for every level j>=3;
    # the following finite examples include both exceptional low levels.
    geometry_examples = []
    for k in [1,2,3,4]:
        rows = new_indices(k)
        hitsets = []
        for row in rows:
            n,i = row['n'],row['i']
            assert i % 45 == 21
            assert [p for p in base if n % base_orders[p] == phases[p]] == []
            h = [p for p,b in fixed_phases.items() if b is not None and n % fixed_orders[p] == b]
            want = [38737] if row['kind'] == 'D' and row['level'] == 1 else (
                   [487824887233] if row['kind'] == 'D' and row['level'] == 2 else [])
            assert h == want,(k,row,h,want)
            hitsets.append(h)
        for p in fixed:
            assert sum(p in h for h in list(hits.values())+hitsets) <= 1
        geometry_examples.append({'k':k,'new_rows':rows,'fixed_hitsets':hitsets})
    return source,fixed,fixed_orders,fixed_phases,base,base_orders,phases,witnesses,hits,geometry_examples


def construct_case(k,data):
    source,fixed,fixed_orders,fixed_phases,base,base_orders,base_phases,old_n,old_hits,geometry = data
    selected = dict(CASE_PRIMES[k])
    rows = new_indices(k)
    assert len(rows) == k+1
    for row,q in zip(rows,selected['D']+[selected['T']]):
        row['prime'] = q
        assert prime_trial(q) and exact_order(q,row['base2_order'])
        assert q not in fixed and q not in base
        assert row['base2_order']//gcd(row['base2_order'],84) == row['parent_period']
    assert len({r['prime'] for r in rows}) == k+1
    selected_primes = base+[r['prime'] for r in rows]
    assert len(selected_primes) == len(set(selected_primes)) == 28+k
    supplemental = [q for q in selected_primes if q not in P]
    assert len(supplemental) == 9+k
    a_phase,phase_modulus = A3,S3
    for q in base:
        if q not in fixed:
            a_phase,phase_modulus = crt_step(a_phase,phase_modulus,BASE_ROOT % q,q)
    for row in rows:
        q,b = row['prime'],row['parent_phase']
        residue = pow(2,-(34+42*b),q)
        row['root_residue'] = residue
        a_phase,phase_modulus = crt_step(a_phase,phase_modulus,residue,q)
    assert 0 < a_phase < phase_modulus
    all_fixed = sorted(set(fixed)|set(selected_primes))
    assert phase_modulus == 6*prod(all_fixed)
    indices = [(q,old_n[q]) for q in base]+[(r['prime'],r['n']) for r in rows]
    assert len({n for q,n in indices}) == len(indices)
    incidence = {q:[] for q in all_fixed}
    for assigned,n in indices:
        hit = [q for q in all_fixed if (a_phase*a_phase*pow(2,n,q)-1) % q == 0]
        assert assigned in hit
        assert [q for q in selected_primes if q in hit] == [assigned]
        if assigned in supplemental:assert not set(hit) & set(P)
        for q in hit:incidence[q].append(assigned)
    assert all(len(v) <= 1 for v in incidence.values())
    orders = {q:base_orders[q] for q in base}
    orders.update({r['prime']:r['base2_order'] for r in rows})
    phases = {q:next(n for n in range(d) if (a_phase*a_phase*pow(2,n,q)-1) % q == 0)
              for q,d in orders.items()}
    period = lcm(*orders.values())
    assert period == 20160
    assert all(any(n % orders[q] == phases[q] for q in selected_primes) for n in range(period))
    differences = sorted({abs(n-m) for (_,n),(_,m) in combinations(indices,2)})
    collision = 1
    for d in differences:collision = lcm(collision,(1 << d)-1)
    C = collision
    removed = []
    while True:
        common = gcd(C,phase_modulus)
        if common == 1:break
        removed.append(str(common))
        C //= common
    assert gcd(C,phase_modulus) == 1 and collision % C == 0
    root,joint = crt_step(a_phase,phase_modulus,0,C)
    if root*root-1 <= max(selected_primes):
        root += joint*((isqrt(max(selected_primes))+2-root+joint-1)//joint)
    assert root % phase_modulus == a_phase and root % C == 0
    assert root % S3 == A3 and root*root-1 > max(selected_primes)
    squared = root*root
    full_terms = [(q,n,(squared << n)-1) for q,n in indices]
    terms = []
    P_product = prod(P)
    for q,n,value in full_terms:
        quotient,remainder = divmod(value,q)
        assert remainder == 0 and quotient > 1
        p_gcd = gcd(value,P_product)
        if q in supplemental:assert p_gcd == 1
        terms.append({'assigned_prime':q,'exponent':n,'integer_bits':value.bit_length(),
                      'assigned_quotient_bits':quotient.bit_length(),'assigned_remainder':0,
                      'gcd_with_P_product':str(p_gcd),'supplemental_witness':q in supplemental,
                      'full_integer_definition':'(root*root << exponent)-1; complete root_hex is retained'})
    gcds = []
    for (q,n,value),(p,m,other) in combinations(full_terms,2):
        lower = value if n < m else other
        difference = abs(n-m)
        g = gcd(lower,(1 << difference)-1)
        assert g == 1
        gcds.append([q,p,1])
    assert len(gcds) == (28+k)*(27+k)//2
    return {'k':k,'delta':9+k,'tau':28+k,'old_prime_saving':1,
            'new_rows':rows,'selected_dictionary':selected_primes,'supplemental_dictionary':supplemental,
            'base2_orders':orders,'zero_phases':phases,'complete_cover_period':period,
            'uncovered_positions':0,'phase_root':str(a_phase),'phase_modulus':str(phase_modulus),
            'fixed_and_selected_prime_incidence':incidence,
            'private_indices':indices,'distinct_positive_differences':differences,
            'collision_lcm_bits':collision.bit_length(),'saturated_factors_removed':removed,
            'unfixed_collision_cofactor_hex':hex(C),'unfixed_collision_cofactor_bits':C.bit_length(),
            'root_hex':hex(root),'root_bits':root.bit_length(),
            'whole_progression_modulus_hex':hex(joint),'whole_progression_modulus_bits':joint.bit_length(),
            'full_integer_terms':terms,'full_pair_gcds':gcds,'pair_gcd_count':len(gcds),
            'gcd_evaluation':'Exact gcd(F_min,2^abs(n-m)-1), with complete F_min evaluated, equals gcd(F_n,F_m)',
            'all_pair_gcds_one':True,'P_free_supplemental_witnesses':len(supplemental),
            'infinite_progression':'root + t*whole_progression_modulus, every integer t>=0',
            'exact_delta_lower_bound_uses_complete_eight_observer':False,
            'native_BRC_execution':False}


def main():
    started = time.monotonic()
    data = fixed_geometry()
    examples = []
    for k in [1,2]:
        example = construct_case(k,data)
        examples.append(example)
        print(json.dumps({'finished_k':k,'delta':example['delta'],'tau':example['tau'],
                          'root_bits':example['root_bits'],'witnesses':len(example['full_integer_terms']),
                          'gcd_pairs':example['pair_gcd_count']}),flush=True)
    result = {
        'schema':'RIESEL_R3_FINITE_JOINT_SPECTRUM_GAP_ONE_V15','status':'PASS',
        'integer_state':'F_n(a)=a^2*2^n-1 at fixed Heartbeat X6 anchor; x -> 2*x+1',
        'theorem':'For every integer s>=9, infinitely many a in R3 have delta_P(a)=s and tau(a^2)=s+19',
        'all_k_basis':'Written dyadic-class proof, distinct-order Bang primes, fixed-prime incidence proof and exact collision-cofactor CRT',
        'cost9_seed_source':'../one/proof.md and its retained exact integer certificate',
        'fixed_geometry':data[0],'new_geometry_examples':data[-1],
        'failure_of_earlier_ternary_route':
            'A permanent i=1 modulo3 row is entirely hit by fixed19, which also hits every P-free old649657 private term; replacing both by19 lowers the proposed cost',
        'corrected_prime_orders':{'D_j':'84*2^j, 1<=j<=k','T_k':'28*2^k, k>=1'},
        'corrected_dyadic_shift':3,
        'new_witness_i_congruence':'i=21 mod45, plus its dyadic class; T uses i=3 mod2^max(k,2)',
        'examples':examples,'elapsed_seconds':time.monotonic()-started,
        'native_BRC_execution':False,'independent_project_review':False,
    }
    target = HERE/'gap_spectrum_certificate.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','examples':[(x['delta'],x['tau']) for x in examples],
                      'elapsed_seconds':result['elapsed_seconds'],'output':str(target)}),flush=True)


if __name__ == '__main__':
    main()
