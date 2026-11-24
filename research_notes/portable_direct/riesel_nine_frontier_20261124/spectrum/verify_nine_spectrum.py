#!/usr/bin/env python3
"""Exact arithmetic for the R4 consecutive-cost construction.

All-prime exclusion of costs <=8 is reused from the complete v13 observer.
The universal chain and coprimalization are proved in proof.md. The 73-digit
cofactor is never assumed prime: every prime divisor has exact order 864.
This checker performs scalar arithmetic, not a new native BRC execution.
"""

from itertools import combinations
from math import gcd, lcm, prod
from pathlib import Path
import json

A3=191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
P=[7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417]
NP=[37,3,89,5,293,117,413,113,41,33,87,233,773,207,237,257,53,593,63,111]
FIXED={7:5,17:10,31:8,41:38,71:11,97:34,113:69,127:119,151:147,241:165,
257:68,281:261,337:4,641:488,673:107,1321:475,14449:7695,29191:19665,
65537:4080,6700417:65537,5:3,13:1,19:6,73:37,11:0,61:0,331:0,37:0,
109:0,433:0,38737:38733,181:0,577:0,631:0,23311:0,54001:0,87211:0,
246241:182629,262657:0,279073:0,18837001:0,29247661:0,487824887233:487823838657}
Q0=[5,13,19,73]
NQ0=[6,12,152,20]
FREE8=[193,1153,6337,22253377,38941695937,278452876033,
33975937,138991501037953,61681,4562284561,168692292721,469775495062434961,
29,43,1429,5419,3361,15790321,88959882481,
211,421,86171,106681,122921,152041,664441,1564921,7416361,47392381,
146919792181,1041815865690181]
B={0,3,5,8,10,15,21,23,26,28,30,31,33}
Q=4261383649
T2=209924353
X=68016300334849
C=7311824282729722035859309520826138827918372038863677678267962656996811009

# Full n-1 Lucas certificates. Every factor is recursively certified.
PC={
2:({},0),3:({},0),5:({2:2},2),11:({2:1,5:1},2),41:({2:3,5:1},6),
7:({2:1,3:1},3),43:({2:1,3:1,7:1},3),947:({2:1,11:1,43:1},2),
1553081:({2:3,5:1,41:1,947:1},7),820026769:({2:4,3:1,11:1,1553081:1},19),
9840321229:({2:2,3:1,820026769:1},6),68016300334849:({2:8,3:3,9840321229:1},7),
251:({2:1,5:3},6),209924353:({2:8,3:3,11:2,251:1},10),
71:({2:1,5:1,7:1},7),23:({2:1,11:1},5),47:({2:1,23:1},5),
739:({2:1,3:2,41:1},3),69467:({2:1,47:1,739:1},2),
4261383649:({2:5,3:3,71:1,69467:1},7)}


def certify(n,seen):
    if n in seen:return
    f,a=PC[n]
    if n in (2,3):
        assert not f
    else:
        assert prod(p**e for p,e in f.items())==n-1
        for p in f:
            assert p<n
            certify(p,seen)
        assert pow(a,n-1,n)==1
        assert all(gcd(pow(a,(n-1)//p,n)-1,n)==1 for p in f)
    seen.add(n)


def order(q):
    for d in range(1,865):
        if pow(2,d,q)==1:return d
    raise AssertionError((q,"order exceeds 864"))


def crt(congruences):
    a,m=0,1
    for r,n in congruences:
        assert gcd(m,n)==1
        a+=m*((r-a)*pow(m,-1,n)%n)
        m*=n
    return a,m


def row(label,m,b,q=None):
    return dict(label=label,w_modulus=m,w_phase=b,order=36*m,
                root_exponent=16+18*b,modulus=q)


def rows(k):
    assert k>=2
    r=[row("D1",2,1,38737),row("D2",4,2,487824887233),
       row("R",3,1,246241),row("Q",12,8,Q)]
    if k==2:r.append(row("T2",12,0,T2))
    else:
        r.append(row("X",24,12,X))
        r += [row(f"D{j}",2**j,2**(j-1)) for j in range(4,k+1)]
        r.append(row(f"T{k}",3*2**k,0,C if k==3 else None))
    assert len(r)==k+3
    return r


def private_w(r):
    known={"D1":3,"D2":30,"R":28,"Q":68,"X":108}
    name=r['label']
    if name in known:return known[name]
    if name.startswith('T'):return 0
    j=int(name[1:])
    for t in range(35):
        w=3*2**(j-1)+(3*2**j)*t
        if w%35 in B:return w
    raise AssertionError(name)


def private_indices(k):
    return NP+NQ0+[32+36*private_w(r) for r in rows(k)]


def all_scalar_rows(k):
    r=[]
    for q in P+Q0:
        d=order(q)
        phases=[n for n in range(d) if FIXED[q]**2*pow(2,n,q)%q==1]
        assert len(phases)==1
        r.append((str(q),d,phases[0]))
    r += [(x['label'],x['order'],(32+36*x['w_phase'])%x['order']) for x in rows(k)]
    return r


def structure_check(k):
    rr=rows(k)
    period=3*2**k
    assert all(any((w-r['w_phase'])%r['w_modulus']==0 for r in rr)
               for w in range(period))
    for r in rr:
        w=private_w(r)
        assert w%35 in B
        hits=[s['label'] for s in rr if (w-s['w_phase'])%s['w_modulus']==0]
        assert hits==[r['label']]
    indices=private_indices(k)
    sr=all_scalar_rows(k)
    assert len(indices)==len(sr)==27+k and len(set(indices))==len(indices)
    for i,n in enumerate(indices):
        hits=[j for j,(_,d,b) in enumerate(sr) if (n-b)%d==0]
        assert hits==[i],(k,i,n,hits)
    return dict(k=k,exact_supplementary_size=7+k,total_size=27+k,
                w_period=period,all_w_covered=True,
                private_indices=indices,
                row_descriptions=[dict(label=r['label'],w_modulus=r['w_modulus'],
                    w_phase=r['w_phase'],prime_order=r['order'],
                    private_w=private_w(r),root_exponent=r['root_exponent']) for r in rr])


def change_floor(k):
    return 432 if k==2 else 72*2**k


def start_index(bound):
    k=2
    while change_floor(k)<=bound:k+=1
    return k


def strip_supported_factors(d,k):
    e=d
    while True:
        h=gcd(e,k)
        if h==1:return e
        e//=h


def evaluated_example(k,a4,s4):
    assert k in (2,3)
    rr=rows(k)
    extra=[r for r in rr if s4%r['modulus']]
    c,K=crt([(a4,s4)]+[(pow(2,-r['root_exponent'],r['modulus']),r['modulus'])
                      for r in extra])
    ns=private_indices(k)
    D=1
    for ni,nj in combinations(ns,2):
        D=lcm(D,(1<<abs(ni-nj))-1)
    E=strip_supported_factors(D,K)
    a=c+K*((-c)*pow(K,-1,E)%E)
    assert a%K==c and a%E==0
    assert a%s4==a4
    assert all(a%q==0 for q in FREE8)
    assert all(a%q==r for q,r in FIXED.items())
    assert all((a*a*pow(2,32+36*r['w_phase'],r['modulus'])-1)%r['modulus']==0
               for r in rr)
    values=[(a*a<<n)-1 for n in ns]
    assert all(gcd(u,v)==1 for u,v in combinations(values,2))
    sr=all_scalar_rows(k)
    period=lcm(*(d for _,d,b in sr))
    cover=bytearray(period)
    for _,d,b in sr:
        for n in range(b,period,d):cover[n]=1
    assert all(cover)
    assert a*a-1>max(P+Q0+[r['modulus'] for r in rr])
    return dict(k=k,exact_delta=7+k,exact_total=27+k,
        compact_start=str(c),compact_step=str(K),
        compact_start_cost_claim="upper bound only; exact lower bound uses the coprimalized root",
        root_hex=hex(a),progression_step_hex=hex(K*E),E_hex=hex(E),
        root_bits=a.bit_length(),D_bits=D.bit_length(),E_bits=E.bit_length(),
        progression_step_bits=(K*E).bit_length(),
        private_indices=ns,private_term_count=len(ns),
        all_pairwise_gcds_one=True,pairwise_gcd_count=len(ns)*(len(ns)-1)//2,
        scalar_complete_period=period,uncovered_positions=0,
        scalar_modulus_variant=("All named moduli are certified primes" if k==2 else
          "C is used as a composite-permitted CRT modulus; choose any prime divisor of C for the one T3 covering prime"),
        extra_moduli={r['label']:str(r['modulus']) for r in extra})


def main():
    seen=set()
    for q in [X,Q,T2]:certify(q,seen)
    assert order(X)==864 and order(Q)==order(T2)==432
    phi=(1<<288)-(1<<144)+1
    assert phi==X*C and gcd(X,C)==1 and C>1 and phi%3!=0
    assert pow(2,432,C)==C-1
    assert gcd(C,(1<<288)-1)==1
    assert len(FREE8)==len(set(FREE8))==31
    T8=prod(FREE8)
    assert gcd(S3,T8)==1
    assert S3==6*prod(FIXED)
    assert all(A3%q==r for q,r in FIXED.items())
    assert max(order(q) for q in FREE8)==420
    a4,s4=crt([(A3,S3),(0,T8)])
    assert s4==S3*T8
    assert len(FIXED)+len(FREE8)==74
    structure=[structure_check(k) for k in range(2,13)]
    transitions=[]
    for k in range(2,12):
        before={r['label']:r for r in rows(k)}
        after={r['label']:r for r in rows(k+1)}
        kept=before.keys()&after.keys()
        assert all(before[n]==after[n] for n in kept)
        removed=[before[n] for n in before.keys()-after.keys()]
        added=[after[n] for n in after.keys()-before.keys()]
        changed=[r['order'] for r in removed+added]
        assert min(changed)==change_floor(k)
        transitions.append(dict(k=k,removed=[r['label'] for r in removed],
            added=sorted(r['label'] for r in added),changed_orders=sorted(changed),
            minimum_changed_order=change_floor(k)))
    boundaries=[dict(B=b,first_k=start_index(b),first_cost=start_index(b)+7)
                for b in [1,420,431,432,575,576,863,864,1151,1152,2303,2304]]
    examples=[]
    for k in [2,3]:
        ex=evaluated_example(k,a4,s4)
        examples.append(ex)
        print(json.dumps(dict(stage='coprimalized_example',cost=ex['exact_delta'],
            root_bits=ex['root_bits'],pairwise_gcd_count=ex['pairwise_gcd_count'],
            period=ex['scalar_complete_period'],status='PASS')),flush=True)
    result=dict(schema='riesel-r4-consecutive-spectrum-v14',
        fixed_family=dict(base_root=str(a4),step=str(s4),prime_coordinate_count=74,
            fixed_inactive_new_primes=[str(q) for q in FREE8],
            historical_root=str(A3),historical_step=str(S3),
            inherited_fixed_residues={str(q):str(r) for q,r in FIXED.items()},
            minimum_extra_cost=9,finite_spectrum='all integers at least nine'),
        special_order_864=dict(phi=str(phi),certified_prime_factor=str(X),
            cofactor=str(C),coprime_factors=True,cofactor_primality_claim=False,
            every_cofactor_prime_has_order=864,
            chosen_T3='least prime divisor of the displayed cofactor'),
        small_prime_certificates={str(n):dict(factorization={str(q):e for q,e in PC[n][0].items()},
                                            witness=PC[n][1]) for n in sorted(seen)},
        structural_checks=structure,transition_checks=transitions,
        observation_threshold=dict(first_transition_order=432,
            later_transition_order='72*2^k, k>=3',first_cost='j_N+7',
            j_N='min{k>=2: (432 if k=2 else 72*2^k)>B_N}',
            same_residue_for_all_costs=True,arbitrary_finite_prime_powers=True,
            order_lower_bound_budget9=432,
            order_lower_bound_later='(9/16)*2^b, every integer b>=10',
            applies_to=['R4','R3','R2','R1'],boundary_examples=boundaries),
        coprimalized_examples=examples,
        source_scope='Complete <=8 exclusion reused from v13; universal chain and observer statement proved in accompanying proof.md',
        native_BRC_execution=False,independent_project_review=False)
    path=Path(__file__).with_name('nine_spectrum_certificate.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='PASS',fixed_prime_coordinates=74,
        finite_spectrum='9,10,11,...',checked_structural_costs=list(range(9,20)),
        evaluated_exact_costs=[9,10],evaluated_exact_totals=[29,30],
        budget9_observer_order_lower_bound=432,
        later_order_lower_bound='(9/16)*2^b for b>=10',output=str(path)),indent=2))


if __name__=='__main__':main()
