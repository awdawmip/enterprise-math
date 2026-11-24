#!/usr/bin/env python3
"""Exact arithmetic for the complete cost-nine class on the fixed R4 fiber.

The companion proofs supply the all-prime reductions. This calculator proves
the new finite inventories, enumerates all classified CRT starts, counts their
union without multiplicity, constructs thirteen exact-cost 9/10 witness pairs,
and certifies the compact global R4 minimum's unrestricted total cost.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
import json
from math import comb, gcd, isqrt, lcm, prod
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
P = (7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417)
Q0 = (5,13,19,73)
Q7 = Q0+(38737,246241,487824887233)
FIXED43 = {
    7:5,17:10,31:8,41:38,71:11,97:34,113:69,127:119,151:147,241:165,
    257:68,281:261,337:4,641:488,673:107,1321:475,14449:7695,29191:19665,
    65537:4080,6700417:65537,5:3,13:1,19:6,73:37,11:0,61:0,331:0,
    37:0,109:0,433:0,38737:38733,181:0,577:0,631:0,23311:0,54001:0,
    87211:0,246241:182629,262657:0,279073:0,18837001:0,29247661:0,
    487824887233:487823838657,
}
OLD_FREE31 = (193,1153,6337,22253377,38941695937,278452876033,
    33975937,138991501037953,61681,4562284561,168692292721,469775495062434961,
    29,43,1429,5419,3361,15790321,88959882481,
    211,421,86171,106681,122921,152041,664441,1564921,
    7416361,47392381,146919792181,1041815865690181)
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
G7 = tuple(sorted((92737,649657,77158673929,40388473189,118750098349)))
R12 = (209924353,4261383649,24929060818265360451708193)
H20 = tuple(sorted((4278255361,394783681,46908728641,8369281,
                   750016890283777055704738227247474485366338380663681)))
B = {0,3,5,8,10,15,21,23,26,28,30,31,33}
G_PHASES = (0,1,2,3,5)
X864 = 68016300334849
C864 = 7311824282729722035859309520826138827918372038863677678267962656996811009
MINIMUM_INDEX = 75240521932528635
MINIMUM_WITNESSES = (
    (5,6),(7,16),(13,12),(17,3),(19,152),(31,89),(41,5),(71,293),
    (73,20),(97,213),(113,413),(127,113),(151,41),(241,33),(257,87),
    (281,233),(337,773),(641,207),(673,237),(1321,257),(14449,53),
    (29191,593),(38737,140),(65537,63),(246241,1472),(6700417,111),
    (209924353,320),(4261383649,32),(487824887233,968))
NATIVE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
NATIVE_BLOBS = {
    'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
    'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
    'brc_rational_holonomy.py':'2591640fe348da9cd7f293a957bea9ae92c82943',
    'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb',
}


@lru_cache(None)
def phi2(n):
    value = (1<<n)-1
    for d in range(1,n):
        if n % d == 0:
            factor = phi2(d)
            assert value % factor == 0
            value //= factor
    return value


def order_two(q):
    value = 1
    for d in range(1,865):
        value = 2*value % q
        if value == 1:
            return d
    raise AssertionError(('order exceeds declared inventory range',q))


def verify_inventory(path):
    inventory = json.loads(path.read_text())
    verified = set()

    def verify(q):
        if q in verified:
            return
        row = inventory['certificates'][str(q)]
        if row['kind'] == 'trial':
            assert q >= 2 and all(q%d for d in range(2,isqrt(q)+1))
        else:
            assert row['kind'] == 'lucas_n_minus_one'
            factors = {int(p):e for p,e in row['factorization'].items()}
            assert prod(p**e for p,e in factors.items()) == q-1
            for p in factors:
                verify(p)
            a = row['witness']
            assert pow(a,q-1,q) == 1
            assert all(gcd(pow(a,(q-1)//p,q)-1,q) == 1 for p in factors)
        verified.add(q)

    for q in inventory['roots']:
        verify(q)
    new = []
    for row in inventory['new_H20_cyclotomic_factorizations']:
        d = row['order']
        fs = {int(q):e for q,e in row['factors'].items()}
        assert prod(q**e for q,e in fs.items()) == int(row['value']) == phi2(d)
        for q in fs:
            assert q in verified and order_two(q) == d
            new.append(q)
    assert tuple(sorted(new)) == H20
    return inventory,verified


def root_pair(q,w):
    r = pow(2,-(16+18*w),q)
    return tuple(sorted((r,q-r)))


def crt(pairs):
    a,m = 0,1
    for residue,q in pairs:
        assert gcd(m,q) == 1
        a += m*((residue-a)*pow(m,-1,q)%q)
        m *= q
    return a,m


def color_predicate(vector,primes,phases):
    return all(any(vector[q] in root_pair(q,b) for q in primes) for b in phases)


def budget_nine(vector):
    return (color_predicate(vector,G7,G_PHASES)
            or color_predicate(vector,R12,(0,8))
            or color_predicate(vector,H20,(0,8,16)))


def color_count(primes,k):
    count = sum((-1)**j*comb(k,j)*prod(q-2*j for q in primes) for j in range(k+1))
    dp = {0:1}
    for q in primes:
        nxt = defaultdict(int)
        for mask,value in dp.items():
            nxt[mask] += value*(q-2*k)
            for b in range(k):
                nxt[mask|1<<b] += 2*value
        dp = nxt
    assert count == dp[(1<<k)-1] and sum(dp.values()) == prod(primes)
    return count


def fraction_record(n,d):
    f = Fraction(n,d)
    with localcontext() as ctx:
        ctx.prec = 80
        decimal = str(Decimal(n)/Decimal(d))
    return dict(numerator=str(f.numerator),denominator=str(f.denominator),decimal=decimal,
                residue_classes=str(n),modulus=str(d))


def cover_rows(rows):
    period = lcm(35,*(m for q,m,b in rows))
    assert all(any(w % m == b for q,m,b in rows)
               for w in range(period) if w % 35 in B)
    return period


def native_minimum(a,A4,channels,selected,source_dir,terms):
    for filename,expected in NATIVE_BLOBS.items():
        data = (source_dir/'enterprise_math'/filename).read_bytes()
        assert sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == expected
    sys.path.insert(0,str(source_dir))
    from enterprise_math.brc_transport import Affine,EffectHistogram,euclidean_digits,recompose
    step = EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])
    twice = step.then(step)
    assert twice.entries == ((Fraction(1),Affine(((4,),),(3,)),1),)

    def evaluate(effect,x):
        (point,weight), = effect.evaluate((x,)).items()
        assert weight.entries == ((Fraction(1),1),) and point[0].denominator == 1
        return int(point[0])

    x = previous_even = a*a-1
    reference = A4*A4-1
    fixed74 = set(FIXED43)|set(OLD_FREE31)
    found = {}
    counts = dict(one_step_updates=0,two_step_evaluations=0,prime_readouts=0,
                  joint_readouts=0,joint_recompositions=0,fixed74_comparisons=0)
    digest = sha256()
    for n in range(1,max(terms)+1):
        x = evaluate(step,x)
        reference = 2*reference+1
        assert x == (a*a<<n)-1
        counts['one_step_updates'] += 1
        if n % 2 == 0:
            assert evaluate(twice,previous_even) == x
            previous_even = x
            counts['two_step_evaluations'] += 1
        for q in channels:
            quotient,(residue,) = euclidean_digits(x,(q,))
            assert (quotient,residue) == divmod(x,q)
            counts['prime_readouts'] += 1
            if q in fixed74:
                assert residue == reference % q
                counts['fixed74_comparisons'] += 1
        quotient,digits = euclidean_digits(x,channels)
        assert recompose(quotient,digits,channels) == x
        counts['joint_readouts'] += 1
        counts['joint_recompositions'] += 1
        data = x.to_bytes((x.bit_length()+7)//8,'big')
        digest.update(len(data).to_bytes(8,'big'))
        digest.update(data)
        if n in terms:
            found[n] = x
    assert found == terms
    return dict(source_commit=NATIVE_COMMIT,source_blobs=NATIVE_BLOBS,counts=counts,
                channels=channels,channel_count=len(channels),last_state_hex=hex(x),
                last_state_bits=x.bit_length(),integer_stream_sha256=digest.hexdigest(),
                scope='Native witness production through index 1472, with all 87 prime observations and full integer reconstruction; complete cover is separately checked over its full 60480-phase period.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory',type=Path,default=HERE/'prime_inventory.json')
    parser.add_argument('--source-dir',type=Path)
    parser.add_argument('--output',type=Path,default=HERE/'r4_nine_certificate.json')
    args = parser.parse_args()
    started = time.monotonic()
    inventory,verified = verify_inventory(args.inventory)
    all_free = tuple(sorted(G7+R12+H20))
    assert len(all_free) == len(set(all_free)) == 13
    T8 = prod(OLD_FREE31)
    S4 = S3*T8
    A4 = A3+S3*((-A3)*pow(S3,-1,T8)%T8)
    assert 0 < A4 < S4 and A4 % T8 == 0 and A4 % S3 == A3
    assert S3 == 6*prod(FIXED43)
    assert all(A4 % q == residue for q,residue in FIXED43.items())
    assert all(gcd(S4,q) == 1 for q in all_free)
    fixed74 = {**FIXED43,**{q:0 for q in OLD_FREE31}}
    assert len(fixed74) == 74
    orders = {q:order_two(q) for q in all_free}
    assert {orders[q] for q in G7} == {63,126,252}
    assert {orders[q] for q in R12} == {432}
    assert {orders[q] for q in H20} == {80,240,720}
    assert max(orders.values()) == 720
    assert {b%7 for b in B} == set(G_PHASES)
    for primes,phases in ((G7,G_PHASES),(R12,(0,8)),(H20,(0,8,16))):
        for q in primes:
            assert len({r for b in phases for r in root_pair(q,b)}) == 2*len(phases)
    families = (
        ('five_seven',G7,G_PHASES,7,(),120,3840),
        ('two_twelve',R12,(0,8),12,((38737,2,1),(246241,3,1),(487824887233,4,2)),6,24),
        ('three_twelve',R12,(0,4,8),12,((38737,2,1),(487824887233,4,2)),6,48),
        ('three_twenty',H20,(0,8,16),20,((38737,2,1),(487824887233,4,2)),60,480),
    )
    family_results = []
    for name,primes,phases,period,fixed,expected_phase,expected_signed in families:
        phase_count = signed_count = 0
        best = None
        digest = sha256()
        for assigned in permutations(primes,len(phases)):
            rows = fixed+tuple((q,period,b) for q,b in zip(assigned,phases))
            assert len(rows) == 5
            full_period = cover_rows(rows)
            phase_count += 1
            for signs in product((-1,1),repeat=len(phases)):
                pairs = [(A4,S4)]+[((sign*pow(2,-(16+18*b),q))%q,q)
                                    for q,b,sign in zip(assigned,phases,signs)]
                a,modulus = crt(pairs)
                assert all(a*a*pow(2,32+36*b,q)%q == 1 for q,m,b in rows)
                vector = {q:a%q for q in all_free}
                assert budget_nine(vector)
                assert a % T8 == 0 and (a-A4) % S4 == 0
                record = dict(root=str(a),modulus=str(modulus),R4_index=str((a-A4)//S4),
                              assigned_primes=assigned,w_phases=phases,signs=signs,
                              supplementary_dictionary=Q0+tuple(q for q,m,b in rows))
                digest.update((json.dumps(record,separators=(',',':'))+'\n').encode())
                signed_count += 1
                if best is None or a < int(best['root']):
                    best = record
        assert phase_count == expected_phase and signed_count == expected_signed
        family_results.append(dict(name=name,phase_dictionaries=phase_count,
                                   signed_CRT_descriptions=signed_count,
                                   full_CRT_enumeration_sha256=digest.hexdigest(),minimum=best))
    assert sum(r['phase_dictionaries'] for r in family_results) == 192
    assert sum(r['signed_CRT_descriptions'] for r in family_results) == 4392
    minimum = min((r['minimum'] for r in family_results),key=lambda r:int(r['root']))
    assert int(minimum['R4_index']) == MINIMUM_INDEX
    a = int(minimum['root'])
    assert a == A4+MINIMUM_INDEX*S4 and len(str(a)) == 371

    # Count the union of three root predicates, rather than adding descriptions.
    group_records = {}
    components = []
    for name,primes,k in (('G7',G7,5),('R12',R12,2),('H20',H20,3)):
        n,d = color_count(primes,k),prod(primes)
        if name == 'G7':
            assert n == 3840
        group_records[name] = fraction_record(n,d)
        components.append((n,d))
    M9 = prod(all_free)
    N9 = M9-prod(d-n for n,d in components)
    density = fraction_record(N9,M9)

    # All thirteen coordinates are individually indispensable, with finite
    # exact-cost 9/10 roots. The common order-864 composite only specifies a
    # residue; its least prime divisor supplies one ordinary prime channel.
    assert X864*C864 == (1<<288)-(1<<144)+1 and gcd(X864,C864) == 1
    assert order_two(X864) == 864
    assert C864 > 1 and gcd(S4*M9,X864*C864) == 1
    assert pow(2,432,C864) == C864-1 and C864 % 3 == 1
    assert cover_rows(((38737,2,1),(487824887233,4,2),(246241,3,1),
                       (R12[0],12,8),(X864,24,12),('least_prime_factor_of_C864',24,0))) == 840
    pairs_results = []
    for target in all_free:
        vector = {q:0 for q in all_free}
        permanent_R = next(q for q in R12 if q != target)
        vector[permanent_R] = root_pair(permanent_R,8)[0]
        if target in R12:
            vector[target] = root_pair(target,0)[0]
        elif target in H20:
            selected = (target,)+tuple(q for q in H20 if q != target)[:2]
            for q,b in zip(selected,(0,8,16)):
                vector[q] = root_pair(q,b)[0]
        else:
            for q,b in zip(G7,G_PHASES):
                vector[q] = root_pair(q,b)[0]
        assert budget_nine(vector)
        false_vector = dict(vector)
        false_vector[target] = 0
        assert not budget_nine(false_vector)
        common_extra = [(pow(2,-232,X864),X864),(pow(2,-16,C864),C864)]
        on,modulus = crt([(A4,S4)]+[(vector[q],q) for q in all_free]+common_extra)
        off,off_modulus = crt([(A4,S4)]+[(false_vector[q],q) for q in all_free]+common_extra)
        assert modulus == off_modulus
        assert on != off and on % target != off % target == 0
        common_modulus = modulus//target
        assert (on-off) % common_modulus == 0
        assert all(on%q == off%q for q in set(fixed74)|set(all_free)-{target}|{X864})
        assert all(x*x-1 > max(C864,*all_free,X864) for x in (on,off))
        pairs_results.append(dict(target_prime=target,target_order=orders[target],
            cost_nine_root=str(on),cost_ten_root=str(off),
            root_modulus=str(modulus),common_modulus=str(common_modulus),
            common_named_prime_count=87,
            common_named_primes=sorted((set(fixed74)|set(all_free)|{X864})-{target}),
            common_additional_modulus=str(C864),permanent_432_prime=permanent_R,
            target_on_residue=vector[target],target_off_residue=0))
    assert len(pairs_results) == 13

    # This minimum has an unrestricted 29-prime lower bound as well.
    selected = sorted(set(P)|set(minimum['supplementary_dictionary']))
    assert len(selected) == 29 and set(q for q,n in MINIMUM_WITNESSES) == set(selected)
    selected_orders = {q:order_two(q) for q in selected}
    phase = {q:next(n for n in range(selected_orders[q]) if a*a*pow(2,n,q)%q == 1)
             for q in selected}
    period = lcm(*selected_orders.values())
    assert period == 60480
    covered = bytearray(period)
    for q in selected:
        for n in range(phase[q],period,selected_orders[q]):
            covered[n] = 1
    assert all(covered) and a*a-1 > max(selected)
    terms = {n:(a*a<<n)-1 for q,n in MINIMUM_WITNESSES}
    assert len(terms) == 29 and max(terms) == 1472
    assert all(gcd(terms[n],terms[m]) == 1 for n,m in combinations(terms,2))
    witnesses = []
    for q,n in MINIMUM_WITNESSES:
        assert [r for r in selected if terms[n]%r == 0] == [q]
        witnesses.append(dict(prime=q,n=n,state_hex=hex(terms[n]),cofactor_hex=hex(terms[n]//q)))
    result = dict(schema='RIESEL_R4_COMPLETE_NINE_V14',status='PASS',
        R3=dict(base=str(A3),step=str(S3)),
        R4=dict(base=str(A4),step=str(S4),fixed_prime_count=74,fixed_prime_residues=fixed74,
                zero_modulus_T8=str(T8),minimum_cost=9),
        new_prime_groups=dict(G7=G7,R12=R12,H20=H20),exact_base2_orders=orders,
        certified_prime_nodes=len(verified),new_cyclotomic_factorizations=inventory['new_H20_cyclotomic_factorizations'],
        complete_dictionary_families=family_results,phase_dictionary_count=192,
        signed_CRT_description_count=4392,canonical_root_predicate_descriptions=4344,
        description_overlap='The three_R12 family is absorbed by two_R12 at the root-predicate level; all density calculations use a Boolean union.',
        global_cost_nine_minimum=minimum,minimum_root_digits=371,
        observer_modulus=str(M9),essential_prime_count=13,minimum_maximum_prime_order=720,
        observer_theorem='On all R4, root residue modulo N and all-future residue trajectory modulo N decide delta_P<=9 iff observer_modulus divides N.',
        exact_cost_nine_density=density,group_densities=group_records,
        coordinate_essentiality_witnesses=pairs_results,
        common_cost_ten_support=dict(X=str(X864),C=str(C864),C_primality_claim=False,
            chosen_second_order864_prime='least prime divisor of C; every such prime has exact order 864'),
        minimum_exact_total_cost=dict(delta=9,tau=29,complete_phase_period=period,uncovered=0,
            pairwise_coprime_witnesses=witnesses,gcd_one_pair_count=406,max_witness_index=1472),
        native_execution=False,independent_project_review='Not claimed')
    if args.source_dir:
        channels = sorted(set(fixed74)|set(all_free))
        assert len(channels) == 87
        result['native_execution'] = True
        result['native_minimum'] = native_minimum(a,A4,channels,selected,args.source_dir,terms)
    result['elapsed_seconds'] = time.monotonic()-started
    args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(dict(status='PASS',phase_dictionaries=192,signed_CRT=4392,
        minimum_root_digits=371,minimum_R4_index=MINIMUM_INDEX,omega9_R4=720,
        exact_density=density['decimal'],tau_minimum=29,
        native=result.get('native_minimum',{}).get('counts'),seconds=result['elapsed_seconds'])))


if __name__ == '__main__':
    main()
