"""Exact inputs and exhaustive reduced phase check for all five-channel covers.

The all-prime reductions are proved in proof.md. This verifier checks their
complete small factorizations, incidence data, rational inequalities, and every
phase left by those reductions. There is no empirical prime-size cutoff.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
from math import gcd, lcm, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = {7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
     1321,14449,29191,65537,6700417}
H = [0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,
     55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100]
U = [11,61,331]
W = [19,37,73,109]
Z = [29,43,1429,5419]


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def order(base, p):
    value = p-1
    for q in factor(p-1):
        while value % q == 0 and pow(base, value//q, p) == 1:
            value //= q
    assert pow(base, value, p) == 1
    assert all(pow(base, value//q, p) != 1 for q in factor(value))
    return value


def phase_u(q, epsilon, category):
    d = order(4,q)
    return next(c for c in range(d) if c % 5 == category
                and (q == 11 or c % 3 == 1)
                and (q != 61 or c % 2 == epsilon))


def canonical(rows):
    return tuple(sorted(rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=HERE/'global_certificate.json')
    args = ap.parse_args()
    assert len(H)==len(set(H))==36
    H0=[h for h in H if h%3==0]
    H1=[h for h in H if h%3==1]
    assert len(H0)==23 and len(H1)==13
    assert not any(h%3==2 for h in H)
    gs=[1,3,5,7,15,21,35,105]
    maxima=[max(Counter(h%g for h in H).values()) for g in gs]
    assert maxima==[36,23,11,7,6,4,2,1]
    assert [sum(h%5==r for h in H0) for r in range(5)]==[6,6,0,6,5]
    assert [sum(h%5==r for h in H1) for r in range(5)]==[5,5,0,0,3]
    assert max(Counter(h%7 for h in H0).values())==4
    assert max(Counter(h%7 for h in H1).values())==3

    powers=[6,12,14,16,18,20,24,30,36,42,48,60,84]
    factorizations={n:factor((1<<n)-1) for n in powers}
    for n,fs in factorizations.items():
        assert prod(p**e for p,e in fs.items())==(1<<n)-1
        assert all(factor(p)=={p:1} for p in fs)

    exceptional={3,5,11,13,19,43,73,331}
    for d in [1,2,3,4,5,6,7,8,9,10,12,15]:
        assert set(factor(4**d-1)) <= P|exceptional
    minimum_d=[11,18,20,14,30,21,35,105]
    bulk_bounds=[F(k,36*(d//g)) for g,k,d in zip(gs,maxima,minimum_d)]
    assert max(bulk_bounds)==F(1,9)
    for g,d in zip(gs,minimum_d):
        assert gcd(d,105)==g
        assert all(set(factor(4**j-1)) <= P|exceptional
                   for j in range(1,d) if gcd(j,105)==g)
    caps={11:F(33,108),19:F(23,108),73:F(23,108),
          43:F(21,108),331:F(18,108)}
    for q,cap in caps.items():
        d=order(4,q);g=gcd(d,105);e=d//g
        assert max(F(sum(h%g==c%g for h in H),36*e) for c in range(d))==cap
    no11=sum(caps[q] for q in [19,73,43,331])+F(1,9)
    no19=sum(caps[q] for q in [11,73,43,331])+F(1,9)
    assert no11==F(97,108)<1 and no19==F(107,108)<1
    assert F(33+13+13+21+18,108)==F(98,108)<1
    assert F(33+23+13+21+18,108)==1
    assert F(13+15+9,108)==F(37,108)<F(13,36)

    # On a parity fiber, after excluding 11, the old loose 1/4 entry
    # disappears because no eligible prime can have ord_q(16)=4.
    parity_excluded=P|{3,5,11,13}
    for e in [1,2,3,4,5,6]:
        assert set(factor(16**e-1)) <= parity_excluded
    minimum_e=[8,9,10,7,15,21,35,105]
    parity_bounds=[F(k,36*(e//g)) for g,k,e in zip(gs,maxima,minimum_e)]
    assert max(parity_bounds)==F(23,108)
    assert F(11,36)+3*F(23,108)==F(17,18)<1

    # H1 without a parity restriction: v=(u-1)/3, period35.
    excluded_h1=P|{3,5,13,19,73}
    for e in [1,2,3,4]:
        assert set(factor((1<<(6*e))-1)) <= excluded_h1
    f5=sorted(q for q in factorizations[30] if q not in excluded_h1 and order(64,q)==5)
    f7=sorted(q for q in factorizations[42] if q not in excluded_h1 and order(64,q)==7)
    assert f5==[11,331] and f7==[43,5419]
    h1_other_bounds=[F(1,6),F(5,26),F(3,13),F(1,13)]
    assert max(h1_other_bounds)==F(3,13)
    leftover=[h for h in H1 if h%5==4]
    assert leftover==[49,64,79] and len({h%7 for h in leftover})==3

    excluded=P|{3,5,13}
    effective_sets={f:sorted(q for q in factorizations[12*f]
                             if q not in excluded and order(4096,q)==f)
                    for f in [3,4,5,7]}
    assert effective_sets=={3:W,4:[],5:U,7:Z}

    # Analytically predicted 108 dictionaries, root signs not counted.
    predicted={}
    for epsilon in [0,1]:
        for assignment in permutations(U):
            rows=[(5,1-epsilon),(13,3*epsilon)]
            rows += [(q,phase_u(q,epsilon,c)) for c,q in zip([0,1,4],assignment)]
            predicted[canonical(rows)]='U_H1'
        for t in [0,1]:
            u0=next(i for i in range(6) if i%2==epsilon and i%3==1-t)
            c13=next(i for i in range(6) if i%2==epsilon and i%3==t)
            for primes in combinations(W,3):
                for assigned in permutations([0,1,2]):
                    rows=[(5,1-epsilon),(13,c13)]
                    rows += [(q,(u0+6*r)%order(4,q)) for q,r in zip(primes,assigned)]
                    predicted[canonical(rows)]='W_H'+str(1-t)
    assert len(predicted)==108
    assert Counter(predicted.values())=={'U_H1':12,'W_H1':48,'W_H0':48}

    # Exhaust every phase system left by the all-prime reduction. The
    # effective period is 3, 5 or 7, whose lcm with 35 is 105 in v.
    found={};trials=0
    for epsilon,t in product([0,1],[0,1]):
        u0=next(i for i in range(6) if i%2==epsilon and i%3==1-t)
        c13=next(i for i in range(6) if i%2==epsilon and i%3==t)
        A=[v for v in range(105) if (u0+6*v)%105 in H]
        assert len(A)==3*(13 if t==0 else 23)
        full=(1<<len(A))-1
        candidates=W+U+Z if t==0 else W
        options={}
        for q in candidates:
            d=order(4,q);f=order(4096,q)
            options[q]=[]
            for r in range(f):
                c=(u0+6*r)%d
                mask=sum(1<<i for i,v in enumerate(A) if v%f==r)
                options[q].append((c,mask))
        for primes in combinations(candidates,3):
            for choices in product(*(options[q] for q in primes)):
                trials+=1
                if choices[0][1]|choices[1][1]|choices[2][1] != full:
                    continue
                rows=[(5,1-epsilon),(13,c13)]
                rows += [(q,c) for q,(c,_) in zip(primes,choices)]
                key=canonical(rows)
                assert key in predicted
                found[key]=predicted[key]
    assert found==predicted

    # Check each predicted dictionary against complete old-hole periods,
    # and exhibit a private old-hole witness for every new channel.
    dictionaries=[]
    for rows,kind in sorted(predicted.items()):
        period=lcm(105,*(order(4,q) for q,c in rows))
        holes=[u for u in range(1,period+1) if u%105 in H]
        private={q:None for q,c in rows}
        for u in holes:
            hit=[q for q,c in rows if u%order(4,q)==c]
            assert hit
            if len(hit)==1 and private[hit[0]] is None:private[hit[0]]=u
        assert all(v is not None for v in private.values())
        dictionaries.append({'type':kind,'rows':[{'q':q,'period_u':order(4,q),
                              'phase_u':c,'root_residues':sorted({pow(2,-c,q),-pow(2,-c,q)%q})}
                              for q,c in rows],
                             'period_u':period,'private_u':private})

    result={'schema':'riesel-all-five-channel-classification-v1',
            'status':'AUTHOR_PROOF_AND_EXACT_ARITHMETIC; NOT_INDEPENDENT_REVIEW',
            'source_dependency':{'commit':'a2ae4d93398425e67dacbb4c99b7f3a6755e5771',
                                 'path':'research_notes/portable_direct/riesel_observers_20261122/staircase/proof.md'},
            'scope':'Every positive old-class root with 3|a; every supplement of at most 5 distinct new primes covering all old holes. Prime sizes and orders are unrestricted before analytic reduction.',
            'P':sorted(P),'H':H,
            'order_bound_from_four_channel_gap':70,
            'complete_factorizations':{str(n):fs for n,fs in factorizations.items()},
            'global_bulk_minimum_periods':minimum_d,
            'global_bulk_density_bounds':[str(x) for x in bulk_bounds],
            'exceptional_caps':{str(q):str(v) for q,v in caps.items()},
            'absence_bounds':{'no11':str(no11),'no19_or73':str(no19),
                              'exactly_one5_or13_parity_coverage':'17/18',
                              'mixed9phase_H1_coverage':'37/108',
                              'H1_mass_relative_H':'39/108'},
            'parity_bulk_bounds':[str(x) for x in parity_bounds],
            'H1_effective_period5_primes':f5,'H1_effective_period7_primes':f7,
            'H1_last_three_u':leftover,
            'fixed_parity_mod3_effective_primes':effective_sets,
            'phase_trials_after_analytic_reduction':trials,
            'complete_phase_dictionary_count':len(dictionaries),
            'type_counts':dict(Counter(predicted.values())),
            'dictionaries':dictionaries,
            'conclusion':'All complete five-prime supplements contain 5 and 13 with opposite u parity. If the phase of 13 is 0 modulo 3, the remaining triple is either U in categories 0, 1, 4 or three distinct W primes covering all three effective phases. If the phase of 13 is 1 modulo 3, only the W type occurs.',
            'properness':'Every prime in a classified supplement is at most 331; all positive old-class roots are at least a_star > 6700417, so all assigned new and old divisors are proper.',
            'root_signs':'Each phase has exactly two allowed root residues; signs are independent by CRT. Different dictionaries may overlap as root sets.',
            'native_scope':'The existing fixed X6 anchor, typed integer register, positive weight 1 and multiplicity 1 BRC update are unchanged. This file checks new arithmetical classification inputs; prior native execution is reused.'}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','output':str(args.output),'dictionaries':108,
                      'types':result['type_counts'],'phase_trials':trials,
                      'maximum_factor':max(q for fs in factorizations.values() for q in fs)}))


if __name__=='__main__':main()
