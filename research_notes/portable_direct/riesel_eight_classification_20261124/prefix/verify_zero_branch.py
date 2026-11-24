#!/usr/bin/env python3
"""Exact evidence for the zero-W budget-eight classification on R3.

Universal reductions are proved in proof.md. This standard-library checker
verifies all residual geometries, exact inventories with recursive prime
certificates, and the 15360 CRT descriptions of one explicit counterexample
subfamily. It does not enumerate every cost-eight root.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
import json
from math import gcd,isqrt,lcm,prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = {1,2,10,11,12,16,17,22,25,26,30,31,32}
OCCUPIED = (1,2,3,4,5)
Z = (29,43,1429,5419)
J = (3361,15790321,88959882481)
U = (211,421,86171,106681,122921,152041,664441,1564921,
     7416361,47392381,146919792181,1041815865690181)
Z_ORDERS = (28,14,84,42)
J_ORDERS = (168,56,168)
P = (7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417)
P_ORDERS = (3,8,5,20,35,48,28,7,15,24,16,70,21,64,48,60,84,105,32,64)
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
FACTORS168 = {3:2,5:1,7:2,13:1,17:1,29:1,43:1,113:1,127:1,
              241:1,337:1,1429:1,3361:1,5419:1,14449:1,15790321:1,88959882481:1}


def prime_trial(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))


def prime_factors(n):
    result,d = set(),2
    while d*d <= n:
        while n%d == 0:
            result.add(d)
            n//=d
        d+=1
    if n>1:
        result.add(n)
    return result


def exact_order(q,d):
    return pow(2,d,q)==1 and all(pow(2,d//p,q)!=1 for p in prime_factors(d))


@lru_cache(None)
def cyclotomic_at_two(n):
    result = (1<<n)-1
    for d in range(1,n):
        if n%d == 0:
            factor=cyclotomic_at_two(d)
            assert result%factor == 0
            result//=factor
    return result


def category_max(points,g):
    return max(Counter(r%g for r in points).values(),default=0)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory',type=Path,default=HERE/'auxiliary_inventory_certificate.json')
    parser.add_argument('--output',type=Path,default=HERE/'zero_branch_certificate.json')
    args=parser.parse_args()
    inventory=json.loads(args.inventory.read_text())
    certificates=inventory['certificates']
    verified=set()

    def verify_prime(n):
        if n in verified:
            return
        cert=certificates.get(str(n))
        if cert is None or cert['kind']=='trial':
            assert prime_trial(n)
        else:
            assert cert['kind']=='lucas_n_minus_one'
            factors={int(q):int(e) for q,e in cert['factorization'].items()}
            assert prod(q**e for q,e in factors.items())==n-1
            for q in factors:
                verify_prime(q)
            witness=cert['witness']
            assert pow(witness,n-1,n)==1
            assert all(gcd(pow(witness,(n-1)//q,n)-1,n)==1 for q in factors)
        verified.add(n)

    for q in inventory['roots']:
        verify_prime(q)
    f35=[]
    for row in inventory['cyclotomic_factorizations']:
        d=row['order']
        factors={int(q):int(e) for q,e in row['factors'].items()}
        assert cyclotomic_at_two(d)==int(row['cyclotomic_value'])==prod(q**e for q,e in factors.items())
        assert d//gcd(d,12)==35
        for q in factors:
            verify_prime(q)
            assert exact_order(q,d)
            if q not in P:
                f35.append(q)
    assert tuple(sorted(f35))==U
    assert prod(q**e for q,e in FACTORS168.items())==(1<<168)-1
    for q in FACTORS168:
        verify_prime(q)
    f14=[]
    for q in FACTORS168:
        if pow(2,168,q)==1 and pow(2,84,q)!=1 and pow(2,24,q)!=1:
            # Directly select exact effective order14 for base2^12.
            assert pow(pow(2,12,q),14,q)==1
            assert pow(pow(2,12,q),7,q)!=1 and pow(pow(2,12,q),2,q)!=1
            f14.append(q)
    assert tuple(sorted(f14))==J
    for q,d in zip(Z+J,Z_ORDERS+J_ORDERS):
        verify_prime(q)
        assert exact_order(q,d)
    assert all(gcd(q,S3)==1 for q in Z+J+U)

    rows={c:sorted(r for r in A if r%7==c) for c in OCCUPIED}
    assert [len(rows[c]) for c in OCCUPIED]==[2,3,3,3,2]
    assert [sum(r%5==c for r in A) for c in range(5)]==[3,5,5,0,0]
    assert rows[1]==[1,22] and rows[5]==[12,26]
    assert all(len({r%5 for r in points})==len(points) for points in rows.values())
    five_cases=[]
    zero_cases=[]
    for m in range(5):
        for removed in combinations(OCCUPIED,m):
            residual={r for r in A if r%7 not in removed}
            mass=max(F(len(residual),6),F(category_max(residual,5),2),
                     F(category_max(residual,7),2),F(1))
            assert (5-m)*mass < len(residual)
            five_cases.append({'removed_rows':removed,'size':len(residual),
                'column_max':category_max(residual,5),'row_max':category_max(residual,7),
                'per_non7_class_bound':str(mass),'total_bound':str((5-m)*mass)})
            if m in (2,3):
                mass8=max(F(len(residual),8),F(category_max(residual,5),2),
                          F(category_max(residual,7),2),F(1))
                assert (6-m)*mass8<len(residual)
                zero_cases.append({'removed_rows':removed,'size':len(residual),
                    'per_non7_class_bound':str(mass8),'total_bound':str((6-m)*mass8)})
    assert len(five_cases)==31 and len(zero_cases)==20
    assert 2*F(5,26)+4*F(1,8)==F(23,26)<1
    assert F(3,13)+2*F(5,26)+3*F(1,8)==F(103,104)<1

    # Exhaust the five surviving mod7-row geometries at their full lift period.
    shape_checks=[]
    for c in OCCUPIED:
        rows7=[(7,b) for b in OCCUPIED if b!=c]
        binary=rows7+[(14,c),(14,c+7)]
        period=lcm(35,*(h for h,b in binary))
        holes=[v for v in range(period) if v%35 in A]
        assert all(any(v%h==b for h,b in binary) for v in holes)
        private=[sum(v%h==b and all(v%h2!=b2 for j,(h2,b2) in enumerate(binary) if i!=j)
                     for v in holes) for i,(h,b) in enumerate(binary)]
        assert all(private)
        item={'remaining_row':c,'split14_period':period,'split14_private_counts':private}
        if c in (1,5):
            points=rows[c]
            isolated=rows7+[(35,b) for b in points]
            assert all(any(v%h==b for h,b in isolated) for v in sorted(A))
            item['point35_phases']=points
        shape_checks.append(item)

    # Exactly the requested explicit subfamily: both of the two small J primes.
    free_primes=Z+(3361,15790321)
    free_modulus=prod(free_primes)
    weights={q:(free_modulus//q)*pow(free_modulus//q,-1,q) for q in free_primes}
    s_inverse={q:pow(S3,-1,q) for q in free_primes}
    roots_by_phase={q:{b:pow(pow(2,4+6*b,q),-1,q) for b in range(14)} for q in free_primes}
    minimum=None
    starts=set()
    phase_count=0
    for c in OCCUPIED:
        active_classes=[b for b in OCCUPIED if b!=c]
        for chosen in permutations(Z):
            assignments=dict(zip(chosen,active_classes))
            for final_primes in permutations((3361,15790321)):
                assignments.update(zip(final_primes,(c,c+7)))
                phase_count+=1
                for signs in product((1,-1),repeat=6):
                    residues={q:(sign*roots_by_phase[q][assignments[q]])%q
                              for q,sign in zip(free_primes,signs)}
                    index=sum(((residues[q]-A3)*s_inverse[q]%q)*weights[q]
                              for q in free_primes)%free_modulus
                    root=A3+S3*index
                    assert root%S3==A3
                    assert all(root%q==residues[q] for q in free_primes)
                    assert all(root*root*pow(2,8+12*assignments[q],q)%q==1 for q in free_primes)
                    starts.add(root)
                    if minimum is None or root<int(minimum['root']):
                        minimum={'root':str(root),'R3_index':str(index),'digits':len(str(root)),
                            'remaining_mod7_class':c,'v_phases':dict(assignments),
                            'root_residues':residues,'root_signs':dict(zip(free_primes,signs)),
                            'progression_modulus':str(S3*free_modulus)}
    assert phase_count==240 and len(starts)==15360
    root=int(minimum['root'])
    orders=dict(zip(P,P_ORDERS))
    orders.update(dict(zip(Z,Z_ORDERS)))
    orders.update({5:4,13:12,3361:168,15790321:56})
    dictionary=set(P)|{5,13}|set(free_primes)
    assert len(dictionary)==28 and set(orders)==dictionary
    assert 19 not in dictionary and 73 not in dictionary
    selected_period=lcm(*orders.values())
    coverage_period=lcm(420,*(orders[q] for q in free_primes))
    assert selected_period==6720 and coverage_period==840
    values={q:(root*root-1)%q for q in dictionary}
    hit_counts={q:0 for q in dictionary}
    private={}
    for n in range(1,selected_period+1):
        for q in dictionary:
            values[q]=(2*values[q]+1)%q
        hits=[q for q in sorted(dictionary) if values[q]==0]
        assert hits
        for q in hits:
            hit_counts[q]+=1
        if len(hits)==1:
            private.setdefault(hits[0],n)
    assert all(values[q]==(root*root-1)%q for q in dictionary)
    assert 2*root*root-1>max(dictionary)
    assert set(private)==dictionary
    total_phases=5*24*3*2+2*24*12*11
    assert total_phases==7056 and total_phases*64==451584
    result={'schema':'riesel-r3-zero-W-complete-eight-classification-v1',
        'status':'PASS_AUTHOR_PROOF_AND_EXACT_ARITHMETIC_NOT_INDEPENDENT_REVIEW',
        'A':sorted(A),'A_rows_mod7':rows,
        'five_class_lemma_cases':five_cases,'zero_W_m2_m3_cases':zero_cases,
        'zero_W_m0_m1_bounds':['23/26','103/104'],
        'surviving_geometries':shape_checks,
        'f7_primes':Z,'f14_primes':J,'f35_primes':U,
        'auxiliary_primality_nodes_verified':len(verified),
        'phase_dictionary_counts':{'split14':720,'points35':6336,'total':7056},
        'signed_CRT_description_count':451584,
        'explicit_small_J_subfamily':{'phase_count':phase_count,'signed_progressions':len(starts),
            'minimum_scope':'Only the split14 subfamily using 3361 and 15790321; not the global R3 minimum.',
            'minimum':minimum,'delta_P':8,'tau_upper_bound':28},
        'counterexample_dictionary':sorted(dictionary),
        'counterexample_supplement':sorted(dictionary-set(P)),
        'complete_coverage_predicate_period':coverage_period,
        'scalar_selected_dictionary_residue_cycle_executed':selected_period,
        'counterexample_hit_counts_in_cycle':hit_counts,
        'counterexample_private_indices':private,
        'native_BRC_execution_performed':False,
        'source_scope':'The all-prime classification is proof.md; this calculator checks its exact arithmetic and explicit construction.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','five_class_cases':len(five_cases),
        'zero_branch_cases':len(zero_cases),'minimum':minimum,'output':str(args.output)},indent=2))


if __name__=='__main__':
    main()
