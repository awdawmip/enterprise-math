#!/usr/bin/env python3
"""Exact arithmetic for budget-nine basic-pair and one-W classification.

The proof uses all-order gcd-column bounds. This script verifies their finite
incidence input and complete order inventories, then realizes a proper cover
whose complete budget-eight predicate is false. It performs scalar arithmetic,
not a native BRC execution or an independent project Review.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
H = {0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,
     55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100}
A = {1,2,10,11,12,16,17,22,25,26,30,31,32}
P = [7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417]
P_ORDERS = [3,8,5,20,35,48,28,7,15,24,16,70,21,64,48,60,84,105,32,64]
INACTIVE = {3,11,61,331,37,109}
BASIC = {5,13}
Z = [29,43,1429,5419]
K = [92737,649657,77158673929,40388473189,118750098349]
K_ORDERS = {92737:63,649657:63,77158673929:126,
            40388473189:252,118750098349:252}
H6 = [33975937,138991501037953]
H10 = [61681,4562284561,168692292721,469775495062434961]
F14 = [3361,15790321,88959882481]
F35 = [211,421,86171,106681,122921,152041,664441,1564921,
       7416361,47392381,146919792181,1041815865690181]
J_FAMILIES = {
    "binary": ([193,1153,6337,22253377,38941695937,278452876033], [0,4]),
    "ternary": ([33975937,138991501037953], [0,2]),
    "modulo_five": ([61681,4562284561,168692292721,469775495062434961], [0,6,8]),
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


def factor_small(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1:
        out[n]=out.get(n,0)+1
    return out


@lru_cache(None)
def phi2(d):
    z=2**d-1
    for e in range(1,d):
        if d%e==0:
            z0=phi2(e)
            assert z%z0==0
            z//=z0
    return z


def order2(q, limit=420):
    x=1
    for d in range(1,limit+1):
        x=x*2%q
        if x==1:
            return d
    raise AssertionError(("order not within proved bound",q,limit))


def verify_inventory():
    data=json.loads((HERE/"inventory_certificate.json").read_text())
    certs=data["prime_certificates"]
    checked=set()
    def prime(q):
        if q in checked:
            return
        row=certs[str(q)]
        if row["kind"]=="trial":
            assert 2<=q<100000
            assert all(q%d for d in range(2,isqrt(q)+1)),q
        else:
            assert row["kind"]=="lucas_n_minus_one"
            factors={int(p):e for p,e in row["factors"].items()}
            assert prod(p**e for p,e in factors.items())==q-1
            for p in factors:
                prime(p)
            witness=row["witness"]
            assert pow(witness,q-1,q)==1
            assert all(gcd(pow(witness,(q-1)//p,q)-1,q)==1 for p in factors)
        checked.add(q)
    for q in data["roots"]:
        prime(q)
    cyclo={}
    for row in data["cyclotomic_factorizations"]:
        d=row["order"]
        factors={int(q):e for q,e in row["factors"].items()}
        assert prod(q**e for q,e in factors.items())==int(row["value"])==phi2(d)
        assert all(q in checked for q in factors)
        cyclo[d]=factors
    mersenne={}
    for row in data["mersenne_factorizations"]:
        d=row["exponent"]
        factors={int(q):e for q,e in row["factors"].items()}
        assert prod(q**e for q,e in factors.items())==2**d-1
        assert all(q in checked for q in factors)
        mersenne[d]=factors
    def eligible(base_power, period):
        factors=mersenne[base_power*period]
        return sorted(q for q in factors
                      if order2(q)//gcd(order2(q),base_power)==period
                      and q not in set(P)|BASIC|INACTIVE)
    t_expected={1:[],2:[],3:[],4:[],5:[],6:[],7:[43],8:[],
                9:[19,73],10:[],11:[23,89,683],12:[],14:[29],
                15:[],18:[],21:[5419]}
    e_expected={1:[],2:[],3:[],4:[],5:[],6:[],7:[29,43],8:[],
                9:[19,73],10:[61681],12:[],14:[15790321],15:[],
                18:[433,38737],21:[1429,5419]}
    assert {t:eligible(2,t) for t in t_expected}==t_expected
    assert {e:eligible(4,e) for e in e_expected}==e_expected
    for q in K:
        assert order2(q)==K_ORDERS[q]
        assert K_ORDERS[q]//gcd(K_ORDERS[q],12)==21
    assert set(K)==set(cyclo[63])|set(cyclo[126])|set(cyclo[252])
    assert set(H6)==set(cyclo[216])
    assert set(H10)==set(cyclo[40])|set(cyclo[120])|set(cyclo[360])
    assert all(order2(q)//gcd(order2(q),36)==6 for q in H6)
    assert all(order2(q)//gcd(order2(q),36)==10 for q in H10)
    # These equations derive the finite base-order inventories themselves.
    divisors=lambda n:[d for d in range(1,n+1) if n%d==0]
    assert [21*g for g in divisors(12) if gcd(21*g,12)==g]==[63,126,252]
    assert [6*g for g in divisors(36) if gcd(6*g,36)==g]==[216]
    assert [10*g for g in divisors(36) if gcd(10*g,36)==g]==[40,120,360]
    return {"root_prime_count":len(data["roots"]),"recursive_nodes_verified":len(checked),
            "t_inventory":t_expected,"e_inventory":e_expected,
            "f21_base_orders":K_ORDERS,"h6_inventory":H6,"h10_inventory":H10}


def max_incidence(R,g):
    return max(Counter(x%g for x in R).values())


def basic_pair_geometry():
    assert [max_incidence(H,g) for g in [1,3,5,7,15,21,35,105]]==[36,23,11,7,6,4,2,1]
    global_bounds=[F(1,13),F(23,288),F(11,144),F(7,144),F(1,12),F(1,18),F(1,18),F(1,36)]
    assert max(global_bounds)==F(1,12)
    neither=F(7,36)+2*F(13,108)+F(1,9)+F(7,72)+3*F(1,11)+F(1,12)
    assert neither==F(2375,2376)
    assert F(6,35)*(1-neither)==F(1,13860)
    rows=sorted({x%7 for x in H})
    assert rows==[0,1,2,3,5,6]
    cases=[]
    summary=[]
    for m in range(3):
        ratios=[]
        gaps=[]
        for deleted in combinations(rows,m):
            R={x for x in H if x%7 not in deleted}
            n=len(R)
            c={g:max_incidence(R,g) for g in [1,3,5,7,15,21,35,105]}
            r1=sum(x%3==1 for x in R)
            G=max(F(n,11),F(c[3],8),F(c[5],4),F(c[7],4),
                  F(c[15],2),F(c[21],2),F(c[35]),F(c[105]))
            caps=[F(c[21]),F(c[21]),F(c[5],2),F(c[7],2),
                  F(c[3],6),F(c[3],6),F(r1,3),F(r1,3)]+[G]*8
            best=sorted(caps,reverse=True)[:8-m]
            U=sum(best)
            assert U<n,(deleted,U,n)
            ratios.append(U/n)
            gaps.append(n-U)
            cases.append({"deleted_mod7_rows":deleted,"remaining_H":sorted(R),
                          "incidence_maxima":c,"fixed_W_compatible_points":r1,
                          "generic_mass_bound":str(G),"chosen_upper_masses":[str(x) for x in best],
                          "union_mass_upper_bound":str(U),"residual_gap":str(n-U)})
        summary.append({"m":m,"case_count":len(ratios),"max_ratio":str(max(ratios)),
                        "min_absolute_gap":str(min(gaps))})
    assert [r["max_ratio"] for r in summary]==["25/27","155/174","10/11"]
    assert [r["min_absolute_gap"] for r in summary]==["8/3","19/6","2"]
    assert F(3,35)*F(2,36)==F(1,210)
    # Direct fixed-phase counts on both parity fibers.
    for eps in [0,1]:
        old=[u for u in range(630) if u%105 in H and u%2==eps]
        assert len(old)==108
        for b in [1,4]:
            assert sum(u%9==b for u in old)==13
    return {"neither_basic_relative_union_bound":str(neither),
            "neither_basic_full_exponent_gap":"1/13860",
            "exactly_one_basic_full_exponent_gap":"1/210",
            "parity_cases":cases,"parity_case_summary":summary}


def six_class_geometry():
    rows=sorted({x%7 for x in A})
    assert rows==[1,2,3,4,5]
    assert [sum(x%7==c for x in A) for c in rows]==[2,3,3,3,2]
    assert [sum(x%5==c for x in A) for c in range(5)]==[3,5,5,0,0]
    assert all(len({x%5 for x in A if x%7==c})==sum(x%7==c for x in A) for c in rows)
    assert 2*F(5,2)+2*F(13,6)+2*F(5,3)==F(38,3)<13
    assert 3*F(5,2)+2*F(13,6)+F(5,3)==F(27,2)
    assert F(27,2)-1<13
    assert 3*F(5,2)+3==F(21,2)<13
    assert 4*F(5,2)+2*F(13,6)==F(43,3)
    assert F(43,3)-2==F(37,3)<13
    assert 4*F(5,2)+2*F(3,4)==F(23,2)<13
    # Complete arithmetic solutions to the equality-period equations.
    assert [k*g for g in [1,5] for k in [3] if gcd(k*g,5)==g]==[3,15]
    assert [k*g for g in [1,5] for k in [7] if gcd(k*g,5)==g]==[7,35]
    assert [2*g for g in [1,2,5,10] if gcd(2*g,10)==g]==[4,20]
    subset_cases=[]
    for m in [1,2,3]:
        for deleted in combinations(rows,m):
            R={x for x in A if x%7 not in deleted}
            n=len(R)
            c5=max_incidence(R,5)
            c7=max_incidence(R,7)
            if m==1:
                bound=4*F(2)+F(11,6)
            else:
                each=max(F(n,6),F(c5,2),F(c7,2),F(1))
                bound=(6-m)*each
            assert bound<n
            subset_cases.append({"deleted_rows":deleted,"R":sorted(R),
                                 "absolute_union_upper_bound":str(bound),"target_mass":n})
    return {"no_seven_branch_bounds":{"j_at_most_2":"38/3","j3_initial":"27/2",
                                      "j3_after_forced_small_column":"21/2",
                                      "j4_initial":"43/3","j4_after_forced_small_parity":"23/2"},
            "residual_cases":subset_cases}


def v_pair(q,b):
    r=pow(2,-(4+6*b),q)
    return (r,(-r)%q)


def j_pair(q,b):
    r=pow(2,-(16+18*b),q)
    return (r,(-r)%q)


def eight_predicate(a):
    retained=any(all(any(a%q in j_pair(q,b) for q in qs) for b in bs)
                 for qs,bs in J_FAMILIES.values())
    phases=[]
    for q in Z:
        bs=[b for b in range(1,6) if a%q in v_pair(q,b)]
        if len(bs)!=1:
            return retained
        phases.append(bs[0])
    if len(set(phases))!=4:
        return retained
    c=next(b for b in range(1,6) if b not in phases)
    via14=all(any(a%q in v_pair(q,b) for q in F14) for b in [c,c+7])
    points=[v for v in A if v%7==c]
    via35=len(points)==2 and all(any(a%q in v_pair(q,b) for q in F35) for b in points)
    return retained or via14 or via35


def crt(pairs):
    a,m=0,1
    for r,q in pairs:
        assert gcd(m,q)==1
        a += m*((r-a)*pow(m,-1,q)%q)
        m *= q
    return a,m


def classify_phase_check():
    pattern_count=0
    geometries=[]
    for W,r in [(19,0),(73,1)]:
        for c in range(1,6):
            bs=[b for b in range(21) if b%7==c and b%3!=r]
            assert len(bs)==2
            for zbs in permutations([b for b in range(1,6) if b!=c]):
                for q1,q2 in permutations(K,2):
                    # The congruence phases, rather than prime magnitudes,
                    # determine this complete residual-period calculation.
                    tail=[(q,7,b) for q,b in zip(Z,zbs)]+[(q1,21,bs[0]),(q2,21,bs[1])]
                    private={q:None for q,_,_ in tail}
                    private[W]=None
                    for v in range(105):
                        if v%35 not in A:
                            continue
                        hits=([W] if v%3==r else [])+[q for q,h,b in tail if v%h==b]
                        assert hits
                        if len(hits)==1 and private[hits[0]] is None:
                            private[hits[0]]=v
                    assert all(b is not None for b in private.values())
                    pattern_count+=1
            geometries.append({"W":W,"W_mod3_phase":r,"missing_mod7_phase":c,
                               "f21_phases_mod21":bs})
    assert pattern_count==4800
    return {"geometries":geometries,"phase_dictionary_count":pattern_count,
            "signed_CRT_description_count":pattern_count*64,"residual_v_period":105,
            "supplement_with_P_cover_predicate_period":1260}


def scalar_cover(a,supplement):
    selected=P+supplement
    assert len(selected)==len(set(selected))==29
    orders={q:order2(q) for q in selected}
    assert all(orders[q]==d for q,d in zip(P,P_ORDERS))
    L=lcm(*orders.values())
    prime_phases={}
    for q,d in orders.items():
        hits=[n for n in range(d) if (a%q)**2*pow(2,n,q)%q==1]
        assert len(hits)==1
        prime_phases[q]=hits[0]
    residues={q:(a*a-1)%q for q in selected}
    private={q:None for q in selected}
    hit_counts={q:0 for q in selected}
    uncovered=[]
    for n in range(1,L+1):
        for q in selected:
            residues[q]=(2*residues[q]+1)%q
            assert (residues[q]==0)==(n%orders[q]==prime_phases[q])
        hits=[q for q in selected if residues[q]==0]
        assert hits
        for q in hits:
            hit_counts[q]+=1
        if len(hits)==1 and private[hits[0]] is None:
            private[hits[0]]=n
    assert all(private[q] is not None for q in supplement)
    assert all(residues[q]==(a*a-1)%q for q in selected)
    assert a*a-1>max(selected)
    final_integer=(a*a<<L)-1
    return {"selected_prime_count":len(selected),"scalar_executed_full_residue_period":L,
            "scalar_residue_updates":L*len(selected),"uncovered_indices":0,
            "base2_orders":orders,"zero_phases":prime_phases,
            "private_exponents":private,"hit_counts":hit_counts,
            "final_full_integer_hex":hex(final_integer),
            "final_integer_bit_length":final_integer.bit_length(),
            "proper_factor_check":"a^2-1 exceeds every selected prime",
            "native_BRC_execution_claimed":False}


def actual_roots():
    assert len(FIXED)==43 and S3==6*prod(FIXED)
    assert all(A3%q==r for q,r in FIXED.items())
    assert len(FREE31)==31 and len(set(FREE31))==31
    assert gcd(prod(FREE31+K),S3)==1
    assert len(set(FREE31+K))==36
    # One specified phase pattern: W=19, omitted c=1, f21 phases 1 and 8.
    phases={29:2,43:3,1429:4,5419:5,92737:1,649657:8}
    qs=list(phases)
    candidates=[]
    for signs in product([0,1],repeat=6):
        pairs=[(A3,S3)]+[(v_pair(q,phases[q])[s],q) for q,s in zip(qs,signs)]
        a,m=crt(pairs)
        candidates.append((a,m,signs))
    a,m,signs=min(candidates)
    # The following direct application of the complete predicate is decisive:
    # it is not inferred merely from irredundancy of the selected nine primes.
    assert not eight_predicate(a)
    assert all(a%q==r for q,r in FIXED.items())
    assert all(a%q in v_pair(q,b) for q,b in phases.items())
    supplement=[5,13,19]+qs
    compact={"root":str(a),"digits":len(str(a)),"progression_modulus":str(m),
             "R3_index":str((a-A3)//S3),"minimum_scope":"The 64 sign choices for this one fixed phase dictionary only",
             "signed_starts_compared":64,"sign_bits":signs,"v_phases":phases,
             "root_residues":{q:a%q for q in phases},
             "supplement":supplement,"fixed43_residues":{q:a%q for q in FIXED},
             "complete_eight_observer31_residues":{q:a%q for q in FREE31},
             "complete_eight_predicate":False,"supplementary_minimum":9,
             "total_minimum_upper_bound":29,"coverage":scalar_cover(a,supplement)}
    # A separate zeroed-observer realization makes the exact-cost construction
    # uniform across every classified phase dictionary and every sign choice.
    killed=[q for q in FREE31 if q not in Z]
    assert len(killed)==27
    zero_a,zero_m=crt([(a,m)]+[(0,q) for q in killed])
    assert all(zero_a%q==0 for q in killed)
    assert not eight_predicate(zero_a)
    assert zero_a%m==a
    zeroed={"root":str(zero_a),"digits":len(str(zero_a)),
            "progression_modulus":str(zero_m),"killed_free_coordinates":killed,
            "supplementary_minimum":9,"total_minimum_upper_bound":29,
            "complete_eight_predicate":False,
            "coverage_inherited_by_identical_selected_prime_residues":True}
    return compact,zeroed


def main():
    inventory=verify_inventory()
    basic=basic_pair_geometry()
    six=six_class_geometry()
    classification=classify_phase_check()
    compact,zeroed=actual_roots()
    output={"schema":"riesel-r1-budget9-basic-pair-and-r3-irredundant-one-W-classification-v1",
            "status":"PASS_AUTHOR_EXACT_ARITHMETIC_COLLABORATIVE_CHECK_NOT_INDEPENDENT_REVIEW",
            "basic_pair_theorem_scope":"All R1 complete supplements with at most nine primes",
            "one_W_theorem_scope":"All inclusion-minimal R3 supplements of at most nine primes containing exactly one of 19,73",
            "inventory":inventory,"basic_pair_geometry":basic,"six_class_geometry":six,
            "classification":classification,"compact_exact_cost9_root":compact,
            "zeroed_observer_exact_cost9_progression":zeroed,
            "all_prime_basis":"proof.md gcd-column bounds and cross-phase proof; no prime magnitude cutoff",
            "native_semantics":"Fixed-X6 full integer register; x -> 2x+1; residues are observations",
            "native_BRC_execution_claimed":False,"independent_project_review_claimed":False}
    target=HERE/"nine_prefix_certificate.json"
    target.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":"PASS","certificate":str(target),
                      "basic_H_cases":len(basic["parity_cases"]),
                      "one_W_phase_dictionaries":classification["phase_dictionary_count"],
                      "compact_root_digits":compact["digits"],
                      "scalar_period":compact["coverage"]["scalar_executed_full_residue_period"]}))


if __name__=="__main__":
    main()
