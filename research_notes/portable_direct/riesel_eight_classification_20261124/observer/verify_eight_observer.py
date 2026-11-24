#!/usr/bin/env python3
"""Exact observer arithmetic for the complete budget-eight classification.

The companion prefix/tail proofs supply the all-prime classification and
prime inventory. This script counts their predicates, constructs every
essential-coordinate witness, and supplies exact-cost 8/9 roots with the
same former twelve-coordinate observation. It performs no native BRC run.
"""

from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import permutations, product
from math import comb, gcd, isqrt, lcm, prod
from pathlib import Path
import json

A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
P = [7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417]
FIXED = {
    7:5,17:10,31:8,41:38,71:11,97:34,113:69,127:119,151:147,241:165,
    257:68,281:261,337:4,641:488,673:107,1321:475,14449:7695,29191:19665,
    65537:4080,6700417:65537,5:3,13:1,19:6,73:37,11:0,61:0,331:0,
    37:0,109:0,433:0,38737:38733,181:0,577:0,631:0,23311:0,54001:0,
    87211:0,246241:182629,262657:0,279073:0,18837001:0,29247661:0,
    487824887233:487823838657,
}
J_FAMILIES = {
    "binary": ([193,1153,6337,22253377,38941695937,278452876033], [0,4]),
    "ternary": ([33975937,138991501037953], [0,2]),
    "modulo_five": ([61681,4562284561,168692292721,469775495062434961], [0,6,8]),
}
F7 = [29,43,1429,5419]
F14 = [3361,15790321,88959882481]
F35 = [122921,86171,106681,152041,7416361,47392381,
       211,1564921,664441,421,146919792181,1041815865690181]
A = [1,2,10,11,12,16,17,22,25,26,30,31,32]
C7 = [1,2,3,4,5]
Q432 = [209924353,4261383649]
Q432_RESIDUES = {Q432[0]:pow(2,-16,Q432[0]), Q432[1]:pow(2,-160,Q432[1])}


def exact_order(q, limit=432):
    x = 1
    for d in range(1, limit+1):
        x = x*2 % q
        if x == 1:
            return d
    raise AssertionError(("order exceeds declared finite limit",q,limit))


def pair(q, c):
    r = pow(2,-c,q)
    return tuple(sorted((r,(-r)%q)))


def j_pair(q, b):
    return pair(q,16+18*b)


def v_pair(q, b):
    return pair(q,4+6*b)


def j_predicate(residues):
    return any(all(any(residues[q] in j_pair(q,b) for q in qs) for b in phases)
               for qs,phases in J_FAMILIES.values())


def no_w_predicate(residues):
    phases=[]
    for q in F7:
        hit=[c for c in C7 if residues[q] in v_pair(q,c)]
        if len(hit)!=1:
            return False
        phases.append(hit[0])
    if len(set(phases))!=4:
        return False
    c=next(c for c in C7 if c not in phases)
    via14=all(any(residues[q] in v_pair(q,b) for q in F14) for b in (c,c+7))
    points=[h for h in A if h%7==c]
    via35=(len(points)==2 and all(any(residues[q] in v_pair(q,b) for q in F35)
                                 for b in points))
    return via14 or via35


def full_predicate(residues):
    return j_predicate(residues) or no_w_predicate(residues)


def crt(pairs):
    value,modulus=0,1
    for residue,n in pairs:
        assert gcd(modulus,n)==1
        value += modulus*((residue-value)*pow(modulus,-1,n)%n)
        modulus *= n
    return value,modulus


def missing_color_count(qs,k):
    return sum((-1)**j*comb(k,j)*prod(q-2*j for q in qs) for j in range(k+1))


def weighted_mask_count(qs,k):
    dp={0:1}
    for q in qs:
        nxt=defaultdict(int)
        for mask,n in dp.items():
            nxt[mask]+=n*(q-2*k)
            for b in range(k):
                nxt[mask|1<<b]+=2*n
        dp=nxt
    assert sum(dp.values())==prod(qs)
    return dp[(1<<k)-1]


def decimal_ratio(n,d):
    with localcontext() as ctx:
        ctx.prec=60
        return str(Decimal(n)/Decimal(d))


def count_record(n,d):
    f=Fraction(n,d)
    return dict(true_classes=str(n),modulus=str(d),
                reduced_numerator=str(f.numerator),reduced_denominator=str(f.denominator),
                decimal=decimal_ratio(n,d))


def zero_vector(primes):
    return {q:0 for q in primes}


def assign_four_f7(v,c):
    for q,b in zip(F7,[b for b in C7 if b!=c]):
        v[q]=v_pair(q,b)[0]


def realize(v,all_free):
    pairs=[(A3,S3)] + [(v[q],q) for q in all_free]
    pairs += [(Q432_RESIDUES[q],q) for q in Q432]
    a,m=crt(pairs)
    assert a%S3==A3
    assert all(a%q==v[q] for q in all_free)
    assert all(a%q==Q432_RESIDUES[q] for q in Q432)
    return a,m


def cover_check(a,primes):
    rows=[]
    for q in primes:
        d=exact_order(q)
        hits=[n for n in range(d) if (a%q)**2*pow(2,n,q)%q==1]
        assert len(hits)==1
        rows.append((q,d,hits[0]))
    period=lcm(*(d for _,d,_ in rows))
    covered=bytearray(period)
    for q,d,b in rows:
        for n in range(b,period,d):
            covered[n]=1
    assert all(covered)
    assert a*a-1>max(primes)
    return dict(period=period,uncovered=0,orders={str(q):d for q,d,_ in rows},
                zero_phases={str(q):b for q,d,b in rows})


def main():
    J=sorted(q for qs,_ in J_FAMILIES.values() for q in qs)
    all_free=sorted(J+F7+F14+F35)
    assert len(J)==12 and len(all_free)==len(set(all_free))==31
    assert gcd(prod(all_free),S3)==1
    assert S3==6*prod(FIXED)
    assert all(A3%q==r for q,r in FIXED.items())
    orders={q:exact_order(q) for q in all_free}
    assert max(orders.values())==420
    assert [orders[q]//gcd(orders[q],12) for q in F7]==[7]*4
    assert [orders[q]//gcd(orders[q],12) for q in F14]==[14]*3
    assert [orders[q]//gcd(orders[q],12) for q in F35]==[35]*12
    assert max(orders[q] for q in J)==360

    # Root categories are pairwise disjoint for each prime in its family.
    root_categories={}
    for name,(qs,bs) in J_FAMILIES.items():
        for q in qs:
            cats={str(b):j_pair(q,b) for b in bs}
            assert len({x for pair_ in cats.values() for x in pair_})==2*len(bs)
            root_categories[str(q)]={b:[str(x) for x in p] for b,p in cats.items()}
    for qs,bs in ((F7,C7),(F14,range(14)),(F35,A)):
        for q in qs:
            cats={str(b):v_pair(q,b) for b in bs}
            assert len({x for pair_ in cats.values() for x in pair_})==2*len(bs)
            root_categories[str(q)]={b:[str(x) for x in p] for b,p in cats.items()}

    j_counts={}
    for name,(qs,phases) in J_FAMILIES.items():
        n=missing_color_count(qs,len(phases))
        assert n==weighted_mask_count(qs,len(phases))
        j_counts[name]=(prod(qs),n)
    U=prod(m for m,n in j_counts.values())
    NJ=U-prod(m-n for m,n in j_counts.values())
    V7,V14,V35=map(prod,(F7,F14,F35))
    N14=missing_color_count(F14,2)
    N35=missing_color_count(F35,2)
    assert N14==weighted_mask_count(F14,2)
    assert N35==weighted_mask_count(F35,2)
    phase_counts=Counter()
    for bs in product(C7,repeat=4):
        if len(set(bs))==4:
            c=next(c for c in C7 if c not in bs)
            phase_counts[c]+=2**4
    assert dict(phase_counts)=={c:384 for c in C7}
    by_missing={}
    for c in C7:
        points=[v for v in A if v%7==c]
        n=(N14*V35 if len(points)==3 else
           N14*V35+N35*V14-N14*N35)
        by_missing[str(c)]=dict(A_points=points,f7_root_class_count=384,
                                completion_class_count=str(n),total_true_classes=str(384*n))
    N0=sum(int(r["total_true_classes"]) for r in by_missing.values())
    assert N0==384*(5*N14*V35+2*N35*V14-2*N14*N35)
    V=V7*V14*V35
    T=U*V
    N=T-(U-NJ)*(V-N0)

    # Two extra high-order primes give a complete nine-prime supplement for
    # every root realizing their two fixed phases. Primality is checked here.
    for q in Q432:
        assert q>2 and all(q%d for d in range(2,isqrt(q)+1))
        assert exact_order(q)==432
        assert orders.get(q) is None and gcd(q,S3*T)==1
        assert 432//gcd(432,420)==36>32
    displayed_coordinates=sorted(set(FIXED)|set(all_free)|set(Q432))
    assert len(displayed_coordinates)==76
    nine=P+[5,13,19,73,38737,246241,487824887233]+Q432

    # Each coordinate has a true and a false completion of the full predicate.
    witnesses=[]
    for q in all_free:
        v=zero_vector(all_free)
        group=None
        for name,(qs,bs) in J_FAMILIES.items():
            if q in qs:
                group=name
                others=[p for p in qs if p!=q]
                for p,b in zip(others,bs[:-1]):
                    v[p]=j_pair(p,b)[0]
                v[q]=j_pair(q,bs[-1])[0]
                break
        if q in F7:
            group="f7"
            for p,b in zip([p for p in F7 if p!=q],[2,3,4]):
                v[p]=v_pair(p,b)[0]
            v[q]=v_pair(q,5)[0]
            v[F14[0]]=v_pair(F14[0],1)[0]
            v[F14[1]]=v_pair(F14[1],8)[0]
        elif q in F14:
            group="f14"
            assign_four_f7(v,2)
            p=next(p for p in F14 if p!=q)
            v[p]=v_pair(p,2)[0]
            v[q]=v_pair(q,9)[0]
        elif q in F35:
            group="f35"
            assign_four_f7(v,1)
            p=next(p for p in F35 if p!=q)
            v[p]=v_pair(p,1)[0]
            v[q]=v_pair(q,22)[0]
        assert group is not None and full_predicate(v)
        false=dict(v);false[q]=0
        assert not full_predicate(false)
        ap,m=realize(v,all_free)
        am,mm=realize(false,all_free)
        assert m==mm and (ap-am)%(S3*(T//q)*prod(Q432))==0
        shared_coordinates=[p for p in displayed_coordinates if ap%p==am%p]
        changed_coordinates=[p for p in displayed_coordinates if ap%p!=am%p]
        assert len(shared_coordinates)==75 and changed_coordinates==[q]
        witnesses.append(dict(q=str(q),group=group,true_root=str(ap),false_root=str(am),
                              common_modulus_without_q=str(S3*(T//q)*prod(Q432)),
                              full_root_progression_modulus=str(m),
                              true_coordinate=str(v[q]),false_coordinate="0",
                              true_exact_delta=8,false_exact_delta=9,
                              shared_displayed_prime_count=75,
                              shared_displayed_primes=[str(p) for p in shared_coordinates],
                              changed_displayed_primes=[str(q)],
                              high_order_nine_cover_coordinates={str(p):str(r) for p,r in Q432_RESIDUES.items()},
                              true_vector={str(p):str(r) for p,r in v.items()}))

    # A concrete all-zero old-J observer supports both exact costs eight and
    # nine. The eight-cover omits 19 and 73, with all other free coordinates zero.
    good=zero_vector(all_free)
    for q,c in zip(F7,[2,3,4,5]):
        good[q]=pow(2,-(4+6*c),q)
    good[F14[0]]=pow(2,-(4+6*1),F14[0])
    good[F14[1]]=pow(2,-(4+6*8),F14[1])
    bad=zero_vector(all_free)
    assert not j_predicate(good) and no_w_predicate(good)
    assert not full_predicate(bad)
    a8,m=realize(good,all_free)
    a9,mm=realize(bad,all_free)
    assert m==mm
    assert a8%U==a9%U==0
    common55=lcm(S3,U)
    common57=common55*prod(Q432)
    assert (a8-a9)%common57==0
    shared_coordinates=[p for p in displayed_coordinates if a8%p==a9%p]
    changed_coordinates=[p for p in displayed_coordinates if a8%p!=a9%p]
    assert len(shared_coordinates)==70
    assert changed_coordinates==sorted(F7+F14[:2])
    common70=6*prod(shared_coordinates)
    assert (a8-a9)%common70==0
    eight=P+[5,13]+F7+F14[:2]
    check8=cover_check(a8,eight)
    check9=cover_check(a9,nine)

    # The general finite candidate bound uses all 13 basic-pair progressions.
    # For the displayed complete examples, all extra order-432 primes have
    # effective order 36 and are excluded from every budget-eight dictionary.
    assert all(d//gcd(d,420)<=32 for d in orders.values())
    reduced_A=sorted((2+3*b)%35 for b in (0,3,5,8,10,15,21,23,26,28,30,31,33))
    assert A==reduced_A

    result=dict(
        schema="riesel-complete-budget-eight-observer-v13",
        source_scope="All-prime completeness is supplied by companion prefix/tail proofs; exact arithmetic and finite witness checks here",
        R3=dict(base_root=str(A3),step=str(S3),fixed_prime_residues={str(q):str(r) for q,r in FIXED.items()}),
        candidate_groups={**{name:[str(q) for q in qs] for name,(qs,_) in J_FAMILIES.items()},
                          "f7":[str(q) for q in F7],"f14":[str(q) for q in F14],"f35":[str(q) for q in F35]},
        all_free_prime_count=31,prime_orders={str(q):d for q,d in orders.items()},
        root_categories=root_categories,
        J_family_counts={name:count_record(n,m) for name,(m,n) in j_counts.items()},
        J_complete_count=count_record(NJ,U),
        f7_modulus=str(V7),f14_count=count_record(N14,V14),f35_count=count_record(N35,V35),
        no_W_by_missing_class=by_missing,no_W_count=count_record(N0,V),
        complete_cost_eight_count=count_record(N,T),
        no_W_without_J_count=count_record((U-NJ)*N0,T),
        joint_partition={
            "neither":str((U-NJ)*(V-N0)),"J_only":str(NJ*(V-N0)),
            "no_W_only":str((U-NJ)*N0),"both":str(NJ*N0)},
        observer=dict(least_additional_root_modulus=str(T),least_progression_parameter_period=str(T),
                      root_preserving_translation_period=str(S3*T),
                      sufficient_moduli="exactly the positive multiples of the displayed modulus",
                      exact_maximum_prime_order=420,additional_prime_channels=31,total_with_fixed_R3=74,
                      full_future_residue_version="same iff condition and same maximum-order value"),
        essential_coordinate_witnesses=witnesses,
        displayed_prime_coordinates=[str(q) for q in displayed_coordinates],
        common_observation_counterexample=dict(
            root8=str(a8),root9=str(a9),full_progression_modulus=str(m),
            J_observer_modulus=str(U),J_observer_residue="0",
            shared_root_modulus_55_primes=str(common55),shared_root_modulus_57_primes=str(common57),
            shared_root_residue_57_primes=str(a8%common57),
            shared_displayed_prime_count=70,
            shared_displayed_primes=[str(p) for p in shared_coordinates],
            changed_displayed_primes=[str(p) for p in changed_coordinates],
            shared_root_modulus_70_primes=str(common70),
            shared_root_residue_70_primes=str(a8%common70),
            exact_costs=[8,9],unrestricted_total_upper_bounds=[28,29],
            root8_forced_prefix=dict(primes=["5","13","19","73"],
                exact_supplementary_cost=9,unrestricted_supplementary_cost=8,
                exact_cost_penalty=1,
                proof="J is false; the common nine-cover contains the whole prefix; every eight-cover omits both 19 and 73"),
            scalar_complete_period_checks={"eight":check8,"nine":check9}),
        finite_candidate_bound=dict(after_forced_5_13_remaining_slots=6,
            progression_step=420,effective_order_upper_bound=32,
            base2_order_upper_bound=13440,
            finite_killing_product="product_{e=1}^{32}(2^(420e)-1)",
            proof="private point plus the 2^5 interval-cover theorem; see proof.md"),
        high_order_nine_cover=dict(primes=[str(q) for q in Q432],orders=[432,432],
            w_period=12,w_phases=[0,8],root_residues={str(q):str(r) for q,r in Q432_RESIDUES.items()},
            primality_method="deterministic trial division through the integer square root"),
        native_BRC_execution=False,independent_project_review=False)
    assert sum(map(int,result["joint_partition"].values()))==T
    assert N==sum(int(result["joint_partition"][s]) for s in ("J_only","no_W_only","both"))
    path=Path(__file__).with_name("eight_observer_certificate.json")
    path.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(status="PASS",candidate_count=31,max_order=420,
        complete_frequency=decimal_ratio(N,T),J_frequency=decimal_ratio(NJ,U),
        extra_no_W_frequency=decimal_ratio((U-NJ)*N0,T),
        essential_witness_pairs=len(witnesses),
        essential_pair_shared_displayed_primes=75,
        example_pair_shared_displayed_primes=70,
        shared_observation_exact_costs=[8,9],
        root_digits=[len(str(a8)),len(str(a9))],
        scalar_periods=[check8["period"],check9["period"]],output=str(path)),indent=2))


if __name__=="__main__":
    main()
