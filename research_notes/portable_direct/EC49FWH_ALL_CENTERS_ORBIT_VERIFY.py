#!/usr/bin/env python3
"""Exact finite integer verifier for EC49FWH; Python >=3.8, stdlib only."""
import json
from collections import Counter, defaultdict
from math import gcd

SLOPES = {(0, 0): {3}, (0, 1): {0, 3, 4, 'inf'},
          (1, 0): {2, 3, 4, 'inf'}, (1, 1): {2, 3}}


def p10(h, n):
    h, n = h % 10, n % 10
    if h % 5 == n % 5 == 0:
        return False
    q = 'inf' if h % 5 == 0 else n * pow(h % 5, -1, 5) % 5
    return q in SLOPES[(h % 2, n % 2)]


def source_word(a, b, modulus):
    base = next((h, n) for h in range(modulus) for n in range(modulus)
                if ((b-a)*h-a*n+1) % modulus == 0)
    return {t for t in range(modulus)
            if p10(base[0]+a*t, base[1]+(b-a)*t) and
            (modulus == 10 or (9*(base[0]+a*t)+10*(base[1]+(b-a)*t)) % 11 != 0)}


def defect_centers(S, modulus):
    defects = [len(S ^ {(c-t) % modulus for t in S}) for c in range(modulus)]
    value = min(defects)
    return value, [c for c, v in enumerate(defects) if v == value]


def orbit_repair(S, modulus, centers):
    parent = list(range(modulus))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for c in centers:
        for t in range(modulus):
            i, j = root(t), root((c-t) % modulus)
            if i != j:
                parent[i] = j
    groups = defaultdict(list)
    for t in range(modulus):
        groups[root(t)].append(t)
    cost, tie = 0, 0
    for orbit in groups.values():
        occupied = sum(t in S for t in orbit)
        cost += min(occupied, len(orbit)-occupied)
        tie += (2*occupied == len(orbit))
    return cost, tie


def full_from_crt(U, V):
    return {t for t in range(110) if (t % 10 in U) and (t % 11 in V)}


def verify():
    assert sum(p10(h,n) for h in range(10) for n in range(10)) == 44
    counts = Counter()
    by_modulus = Counter()
    sample = {}
    n_checked = 0
    for a in range(10):
        for b in range(10):
            if gcd(gcd(a,b),10) != 1:
                continue
            U = source_word(a,b,10)
            d10, c10 = defect_centers(U,10)
            k10, t10 = orbit_repair(U,10,c10)
            counts[(d10,len(c10),k10,t10)] += 1
            for F in (10,11):
                V = set(range(11)) if F == 11 else set(range(1,11))
                W = full_from_crt(U,V)
                d110, c110 = defect_centers(W,110)
                k110,t110 = orbit_repair(W,110,c110)
                expected_centers = {c for c in range(110) if c % 10 in c10 and
                                    (F == 11 or c % 11 == 0)}
                assert (d110,k110,set(c110)) == (F*d10,F*k10,expected_centers)
                by_modulus[(F,d10,len(c10),k10,t10,t110)] += 1
                n_checked += 1
    assert sum(counts.values()) == 72 and n_checked == 144
    assert Counter({k:v for k,v in counts.items()}) == Counter({
        (0,1,0,0):8, (2,1,1,1):24, (2,2,2,0):4,
        (2,2,3,0):8, (2,2,5,1):12, (2,4,3,0):8, (2,4,5,1):8})
    for a,b in ((1,7),(1,10),(1,2),(5,6),(2,9),(3,11),(7,17),(13,22)):
        U=source_word(a,b,10);W=source_word(a,b,110)
        V={t%11 for t in W}
        assert W == full_from_crt(U,V)
        d,c=defect_centers(W,110)
        k,t=orbit_repair(W,110,c)
        sample[f'{a}/{b}']={'F':len(V),'defect':d,'centers':len(c),
                             'simultaneous_min_flips':k,'minimizer_count':str(2**t)}
    summary = []
    for (d,N,k,t),n in sorted(counts.items()):
        summary.append({'d10':d,'N10':N,'joint_min_flips_10':k,
                        'log2_optimal_repairs_10':t,'classes':n})
    spectrum = Counter()
    for (F,d,N,k,t,tfull),n in by_modulus.items():
        lifts = 110 if F==10 else 10
        spectrum[(F,F*k)] += n*lifts
    assert sum(spectrum.values()) == 8640
    return {'status':'ALL PASS','frozen_pin':'BRC16943',
            'exact_scope':'44 P10 cells; 72 primitive mod10 classes; 144 CRT product checks; 8 independently based full mod110 anchors',
            'ten_cycle_census':summary,
            'full_mod110_joint_repair_spectrum':[
                {'F':f,'min_flips':k,'primitive_mod110_classes':n}
                for (f,k),n in sorted(spectrum.items())],
            'lift_tie_spectrum':[
                {'F':f,'d10':d,'N10':n,'k10':k,'tie_exponent_10':t,
                 'tie_exponent_110':tf,'mod10_classes':count}
                for (f,d,n,k,t,tf),count in sorted(by_modulus.items())],
            'independently_based_anchor_cases':sample,
            'proof_limit':'Group-orbit theorem is analytic; frozen 44-cell identity and Bernoulli reduction inherited; joint census exact finite check; no independent review'}


if __name__ == '__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2,sort_keys=True))
