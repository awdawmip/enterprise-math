#!/usr/bin/env python3
"""All two-prime completions after the fixed seven-prime prefix in R3.

No third-party packages.  The all-prime capacity proof is in proof.md.
This checker verifies complete factor inventories, deterministic primality,
exact orders, the fifty phase dictionaries, two hundred signed CRT starts,
and the exact cost of the smallest genuinely budget-nine starts using the
previously proved full budget-eight observer.
"""
from __future__ import annotations

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from math import comb, gcd, isqrt, lcm, prod
from pathlib import Path
import argparse
import json

A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
P = {7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417}
Q0 = {5,13,19,73}
Q7 = Q0 | {38737,246241,487824887233}
FIXED = {
    7:5,17:10,31:8,41:38,71:11,97:34,113:69,127:119,151:147,241:165,
    257:68,281:261,337:4,641:488,673:107,1321:475,14449:7695,29191:19665,
    65537:4080,6700417:65537,5:3,13:1,19:6,73:37,11:0,61:0,331:0,
    37:0,109:0,433:0,38737:38733,181:0,577:0,631:0,23311:0,54001:0,
    87211:0,246241:182629,262657:0,279073:0,18837001:0,29247661:0,
    487824887233:487823838657,
}
B = {0,3,5,8,10,15,21,23,26,28,30,31,33}
B4 = {9*b % 35 for b in B}
C = {t for t in range(105) if t % 35 in B4 and t % 3 in (0,2)}
BINARY = (193,1153,6337,22253377,38941695937,278452876033)
OLD216 = (33975937,138991501037953)
NEW432 = (209924353,4261383649,24929060818265360451708193)
TERNARY = tuple(sorted(OLD216 + NEW432))
ORDERS = {193:96,1153:288,6337:288,22253377:96,38941695937:288,
          278452876033:288,33975937:216,138991501037953:216,
          209924353:432,4261383649:432,24929060818265360451708193:432}
FACT216 = {3:4,5:1,7:1,13:1,17:1,19:1,37:1,73:1,109:1,241:1,433:1,
           38737:1,87211:1,246241:1,262657:1,279073:1,33975937:1,
           138991501037953:1}
FACT288 = {3:3,5:1,7:1,13:1,17:1,19:1,37:1,73:1,97:1,109:1,193:1,
           241:1,257:1,433:1,577:1,673:1,1153:1,6337:1,38737:1,65537:1,
           22253377:1,38941695937:1,278452876033:1,487824887233:1}
FACT432 = dict(FACT216)
FACT432.update({97:1,257:1,577:1,673:1,487824887233:1})
FACT432.update({q:1 for q in NEW432})
LUCAS = {
    138991501037953: ({2:7,3:3,79:1,509081623:1},5),
    209924353: ({2:8,3:3,11:2,251:1},10),
    4261383649: ({2:5,3:3,71:1,69467:1},7),
    24929060818265360451708193: ({2:5,3:4,9617693216923364371801:1},15),
    9617693216923364371801: ({2:3,3:1,5:2,6959:1,2303418407080367:1},11),
    2303418407080367: ({2:1,1151709203540183:1},5),
    1151709203540183: ({2:1,7:1,17:1,907481:1,5332469:1},5),
}

# These three alternatives plus the zero-W alternatives are the proved v13
# COMPLETE budget-eight predicate, not a necessary-prefix approximation.
J_FAMILIES = {
    'binary': (BINARY,(0,4)),
    'ternary': (OLD216,(0,2)),
    'modulo_five': ((61681,4562284561,168692292721,469775495062434961),(0,6,8)),
}
F7 = (29,43,1429,5419)
F14 = (3361,15790321,88959882481)
F35 = (122921,86171,106681,152041,7416361,47392381,211,1564921,664441,421,
       146919792181,1041815865690181)
VPOINTS = {1,2,10,11,12,16,17,22,25,26,30,31,32}
FREE8 = set().union(*(set(qs) for qs,_ in J_FAMILIES.values()), F7,F14,F35)


@lru_cache(None)
def prime(n: int) -> bool:
    if n in LUCAS:
        factors,a = LUCAS[n]
        assert prod(p**e for p,e in factors.items()) == n-1
        assert all(prime(p) for p in factors)
        assert pow(a,n-1,n) == 1
        assert all(gcd(pow(a,(n-1)//p,n)-1,n) == 1 for p in factors)
        return True
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3,isqrt(n)+1,2))


def prime_divisors(n: int) -> list[int]:
    out,d = [],2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def exact_order(q: int, order: int, power: int=1) -> bool:
    return pow(2,power*order,q) == 1 and all(
        pow(2,power*(order//p),q) != 1 for p in prime_divisors(order))


def pair(q: int, exponent: int) -> tuple[int,int]:
    r = pow(2,-exponent,q)
    return r,(-r)%q


def w_pair(q: int,b: int) -> tuple[int,int]:
    return pair(q,16+18*b)


def v_pair(q: int,b: int) -> tuple[int,int]:
    return pair(q,4+6*b)


def budget_eight_detail(a: int) -> dict:
    residue = {q:a % q for q in FREE8}
    j = {name:all(any(residue[q] in w_pair(q,b) for q in qs) for b in phases)
         for name,(qs,phases) in J_FAMILIES.items()}
    phases = {q:[c for c in range(1,6) if residue[q] in v_pair(q,c)] for q in F7}
    no_w = False
    c = None
    via14 = via35 = False
    if all(len(hit)==1 for hit in phases.values()) and len({hit[0] for hit in phases.values()})==4:
        c = next(c for c in range(1,6) if c not in {hit[0] for hit in phases.values()})
        via14 = all(any(residue[q] in v_pair(q,b) for q in F14) for b in (c,c+7))
        points = [v for v in VPOINTS if v % 7 == c]
        via35 = len(points)==2 and all(any(residue[q] in v_pair(q,b) for q in F35) for b in points)
        no_w = via14 or via35
    return dict(result=any(j.values()) or no_w,prefix_branches=j,
                f7_hits=phases,missing_f7_class=c,via14=via14,via35=via35,
                residues={str(q):str(residue[q]) for q in sorted(FREE8)})


def crt_append(a: int,m: int,q: int,r: int) -> tuple[int,int]:
    assert gcd(m,q)==1
    a += m*((r-a)*pow(m,-1,q)%q)
    return a,m*q


def enumerate_starts(a0: int,m0: int,allow_binary=True,ternary=TERNARY) -> list[dict]:
    rows = []
    families = [('ternary',ternary,(0,8))]
    if allow_binary:
        families.insert(0,('binary',BINARY,(0,4)))
    for name,qs,phases in families:
        for assignment in permutations(qs,2):
            for signs in product((1,-1),repeat=2):
                a,m = a0,m0
                roots = {}
                for q,b,sign in zip(assignment,phases,signs):
                    r = sign*pow(2,-(16+18*b),q)%q
                    a,m = crt_append(a,m,q,r)
                    roots[q] = r
                assert 0 < a < m and a % m0 == a0
                assert all(a % q==r for q,r in roots.items())
                assert all(a % q==r for q,r in FIXED.items())
                structural8 = name=='binary' or set(assignment)==set(OLD216)
                detail = budget_eight_detail(a)
                assert not structural8 or detail['result']
                rows.append(dict(family=name,primes=assignment,w_phases=phases,signs=signs,
                                 root_residues={str(q):str(r) for q,r in roots.items()},
                                 first_root=str(a),modulus=str(m),
                                 structural_cost_eight=structural8,
                                 first_root_exact_cost=8 if detail['result'] else 9))
    return rows


def minimum_record(rows: list[dict],filter_nine=False) -> dict:
    eligible = [r for r in rows if not filter_nine or not r['structural_cost_eight']]
    row = min(eligible,key=lambda r:int(r['first_root']))
    # If the first positive root of the smallest eligible progression has
    # cost nine, it is the exact minimum over ALL eligible progressions.
    if filter_nine:
        assert row['first_root_exact_cost']==9
    a = int(row['first_root'])
    return dict(row,budget_eight=budget_eight_detail(a),digits=len(str(a)),
                progression_index_in_R3=str((a-A3)//S3),
                supplementary_primes=sorted(Q7 | set(row['primes'])),
                proper_factor_bound_verified=a*a*2-1>max(Q7 | set(row['primes'])))


def color_count(qs, k: int) -> int:
    """Each of k disjoint colors occupies two root residues at each q."""
    return sum((-1)**j*comb(k,j)*prod(q-2*j for q in qs) for j in range(k+1))


def fraction_record(value: Fraction) -> dict:
    with localcontext() as ctx:
        ctx.prec=65
        dec=str(Decimal(value.numerator)/Decimal(value.denominator))
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),decimal=dec)


def density_certificate() -> dict:
    rho_b=Fraction(color_count(BINARY,2),prod(BINARY))
    rho_d=Fraction(color_count(OLD216,2),prod(OLD216))
    c10=J_FAMILIES['modulo_five'][0]
    rho_c=Fraction(color_count(c10,3),prod(c10))
    rho_h=Fraction(color_count(F14,2),prod(F14))
    rho_i=Fraction(color_count(F35,2),prod(F35))
    rho_z=Fraction(384,prod(F7))*(5*rho_h+2*(1-rho_h)*rho_i)
    assert rho_z==Fraction(
        285422907465560159807695293455704125345345041831808795080156705564900074055499415643125990859013120,
        38921589948640367419592091203322874230719996088062678293992369566440235306976918089851085505247338952544774417)
    rho_k=Fraction(color_count(TERNARY,2),prod(TERNARY))
    rho9=(rho_k-rho_d)*(1-rho_b)*(1-rho_c)*(1-rho_z)
    rho4=Fraction(color_count(NEW432,2),prod(NEW432))
    assert rho_d==Fraction(8,prod(OLD216)) and rho9>0 and rho4>0
    return dict(scope='Natural relative density among positive roots of R3; Q7-containing exact-cost-nine class',
        formula='(rho_K-rho_D)*(1-rho_B)*(1-rho_C)*(1-rho_Z)',
        rho_K=fraction_record(rho_k),rho_D=fraction_record(rho_d),rho_B=fraction_record(rho_b),
        rho_C=fraction_record(rho_c),rho_Z=fraction_record(rho_z),
        R3_exact_nine_with_Q7=fraction_record(rho9),
        R4_exact_nine_with_Q7=fraction_record(rho4))


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('two_tail_certificate.json'))
    args=parser.parse_args()
    assert 0<A3<S3 and A3 % 3==0 and A3 % 2==1
    assert len(FIXED)==43 and S3==6*prod(FIXED)
    assert all(A3%q==r for q,r in FIXED.items())
    for q,h,b in ((38737,2,1),(246241,3,1),(487824887233,4,2)):
        assert exact_order(q,h,36)
        assert (A3*A3*pow(2,32+36*b,q)-1)%q==0
    for q,h,b in ((5,2,1),(13,6,0),(19,9,4),(73,9,1)):
        assert exact_order(q,h,2)
        assert (A3*A3*pow(2,2*b,q)-1)%q==0
    assert len(C)==26 and len(B4)==13
    incidences={g:[sum(t%g==b for t in C) for b in range(g)] for g in (1,3,5,7,15,21,35,105)}
    assert [max(cs) for cs in incidences.values()]==[26,13,10,6,5,3,2,1]
    # Exhaust the equality rows without introducing a numerical prime cap.
    assert {e for e in range(2,106) if Fraction(max(incidences[gcd(e,105)]),26*(e//gcd(e,105)))>=Fraction(1,2)}=={2,3}
    inventories={288:FACT288,432:FACT432}
    all_factors=set().union(*(set(fs) for fs in inventories.values()))
    assert all(prime(q) for q in all_factors)
    for e,fs in inventories.items():
        assert prod(q**k for q,k in fs.items())==2**e-1
    assert prod(NEW432)==2**144-2**72+1
    assert all(exact_order(q,d) for q,d in ORDERS.items())
    excluded=P | Q0 | {3} | {q for q,r in FIXED.items() if r==0}
    e1={q for q in FACT288 if pow(2,144,q)==1}
    e2={q for q in FACT288 if exact_order(q,2,144)}
    e3={q for q in FACT432 if exact_order(q,3,144)}
    assert e1 <= excluded | Q7
    assert e2-excluded-Q7==set(BINARY)
    assert e3-excluded-Q7==set(TERNARY)
    for q in Q7 | P:
        assert (A3*A3*pow(2,32,q)-1)%q or q not in e1
    # Direct reduced-period cover: independent of the particular CRT signs.
    reduced_receipts=[]
    for name,qs,phases in [('binary',BINARY,(0,4)),('ternary',TERNARY,(0,8))]:
        for assignment in permutations(qs,2):
            rows=[(2,1),(3,1),(4,2)]
            rows += [(ORDERS[q]//gcd(ORDERS[q],36),b%(ORDERS[q]//gcd(ORDERS[q],36)))
                     for q,b in zip(assignment,phases)]
            period=lcm(35,*(h for h,b in rows))
            missing=[w for w in range(period) if w%35 in B and not any(w%h==b for h,b in rows)]
            assert not missing
            reduced_receipts.append(dict(family=name,primes=assignment,rows=rows,period=period,missing=0))
    rows3=enumerate_starts(A3,S3)
    assert len(rows3)==200 and len(reduced_receipts)==50
    assert sum(not r['structural_cost_eight'] for r in rows3)==72
    minimum3=minimum_record(rows3,filter_nine=True)
    T8=prod(FREE8)
    assert len(FREE8)==31 and gcd(S3,T8)==1
    A4,S4=crt_append(A3,S3,T8,0)
    assert all(A4%q==0 for q in FREE8)
    rows4=enumerate_starts(A4,S4,allow_binary=False,ternary=NEW432)
    assert len(rows4)==24 and all(r['first_root_exact_cost']==9 for r in rows4)
    minimum4=minimum_record(rows4,filter_nine=True)
    cert=dict(schema='riesel-fixed-seven-two-tail-classification-v14',
        native_semantics='Fixed X6, x0=a^2-1, positive singleton BRC x->2x+1, weight=multiplicity=1',
        scope='Complete two-new-prime classification after Q7 in historical R3; not all nine-prime covers',
        A3=str(A3),S3=str(S3),fixed_root_residues=FIXED,B=sorted(B),B4=sorted(B4),C105=sorted(C),
        capacity_incidence_counts=incidences,
        complete_factorizations={str(e):{str(q):k for q,k in fs.items()} for e,fs in inventories.items()},
        lucas_primality_certificates={str(n):dict(factorization={str(p):e for p,e in fs.items()},witness=a,
            fermat_remainder=pow(a,n-1,n),gcd_checks={str(p):gcd(pow(a,(n-1)//p,n)-1,n) for p in fs})
            for n,(fs,a) in LUCAS.items()},
        deterministic_trial_primes=sorted(q for q in all_factors if q not in LUCAS),
        exact_orders=ORDERS,effective_t_inventories={'e1':sorted(e1),'e2':sorted(e2),'e3':sorted(e3)},
        phase_dictionary_count=50,signed_description_count=200,
        structural_cost_eight_signed_count=128,nonstructural_signed_count=72,
        start_cost_histogram=dict(Counter(r['first_root_exact_cost'] for r in rows3)),
        exact_relative_densities=density_certificate(),
        reduced_cover_certificates=reduced_receipts,R3_signed_CRT_starts=rows3,
        R3_exact_cost_nine_minimum_with_Q7=minimum3,
        R4=dict(A4=str(A4),S4=str(S4),killed_observer_primes=sorted(FREE8),
                phase_dictionary_count=6,signed_description_count=24,signed_CRT_starts=rows4,
                minimum_with_Q7=minimum4),
        status='PASS',formal_review='Not claimed')
    args.output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',phase_dictionaries=50,signed_CRT_starts=200,
        start_cost_histogram=cert['start_cost_histogram'],R3_minimum=minimum3,R4_minimum=minimum4),indent=2))


if __name__=='__main__':
    main()
