#!/usr/bin/env python3
"""Exact author-side check: mu_d(k)-restricted gauge, Frobenius and H^1 labels.

Reuses the previously published local exact finite-field arithmetic module.
The checks enumerate every k^r vector and all H-orbits for declared cases.
Nothing here executes the original H0/B0 operator.
"""
from collections import Counter
from itertools import product
from math import gcd
import json

from d25_restricted_gauge_galois_descent_checker_20261028 import Field


def one_case(p, e, r, d):
    F = Field(p, e)
    q = F.q
    assert (q-1) % d == 0 and r >= 1
    H = tuple(x for x in range(1, q) if F.power(x, d) == 1)
    assert len(H) == d

    def canon(v):
        return min(tuple(F.mul(h,x) for x in v) for h in H)

    reps = set(canon(v) for v in product(range(q), repeat=r))
    assert len(reps) == 1 + (q**r-1)//d
    fixed_rows = []
    permutation_by_j = []
    for j in range(e):
        g = gcd(e,j)
        S = (q-1)//(p**g-1)
        t = gcd(d,p**g-1)
        h = gcd(d,S)
        c = h*t//d
        assert h*t % d == 0 and c >= 1
        frob = tuple(F.power(x,p**j) for x in range(q))
        fixed = [v for v in reps if canon(tuple(frob[x] for x in v)) == v]
        expected_fixed = 1+h*(p**(g*r)-1)//d
        base = {canon(v) for v in product((x for x in range(q) if frob[x]==x),repeat=r)}
        expected_base = 1+(p**(g*r)-1)//t
        assert len(fixed)==expected_fixed and len(base)==expected_base
        assert set(base).issubset(set(fixed))

        ker_norm = tuple(z for z in H if F.power(z,S)==1)
        cob = {F.power(z,p**j-1) for z in H}
        assert len(ker_norm)==h and len(cob)==d//t
        assert cob.issubset(set(ker_norm))
        classes = {min(F.mul(z,b) for b in cob) for z in ker_norm}
        assert len(classes)==c
        counts=Counter()
        zero=(0,)*r
        for v in fixed:
            if v==zero:
                continue
            i=next(i for i,x in enumerate(v) if x)
            z=F.mul(frob[v[i]],F.power(v[i],q-2))
            assert z in ker_norm
            assert all(frob[x] == F.mul(z,x) for x in v)
            label=min(F.mul(z,b) for b in cob)
            counts[label]+=1
        expected_per_label = (p**(g*r)-1)//t
        assert len(counts)==c and set(counts)==classes
        assert all(n==expected_per_label for n in counts.values())
        base_from_labels={zero} | {v for v in fixed if v!=zero and
            min(F.mul(F.mul(frob[next(x for x in v if x)],F.power(next(x for x in v if x),q-2)),b) for b in cob)==1}
        assert base==base_from_labels, (p,e,r,d,j,'descent-label mismatch')
        assert len(fixed)-len(base)==(c-1)*expected_per_label
        fixed_rows.append({'j':j,'g':g,'S':S,'t':t,'h':h,
            'H1_size':c,'frobenius_fixed_H_orbits':len(fixed),
            'fixed_orbits_with_base_representative':len(base),
            'fixed_orbits_without_base_representative':len(fixed)-len(base),
            'nonzero_orbits_per_cocycle_label':expected_per_label,
            'uniform_label_counts':dict(sorted(counts.items()))})
        permutation_by_j.append({v:canon(tuple(frob[x] for x in v)) for v in reps})

    # Independently traverse the Frobenius permutation on H-orbits.
    seen=set()
    cycles=Counter()
    for v in reps:
        if v in seen: continue
        x=v
        orbit=[]
        while x not in seen:
            orbit.append(x)
            seen.add(x)
            x=permutation_by_j[1][x] if e>1 else x
        assert x==v
        cycles[len(orbit)]+=1
    semilinear=sum(cycles.values())
    assert semilinear==sum(x['frobenius_fixed_H_orbits'] for x in fixed_rows)//e
    return {'p':p,'e':e,'r':r,'d':d,'q':q,'modulus_low_to_high':F.modulus,
        'raw_vectors':q**r,'linear_H_orbits':len(reps),
        'semilinear_orbits':semilinear,'cycle_length_counts':dict(sorted(cycles.items())),
        'fixed_rows':fixed_rows,'check':'PASS'}


def p373_exact_row():
    p=373; e=2; r=1; d=p+1; q=p*p
    assert pow(2,(p-1)//2,p)==p-1
    assert pow(p-2,(p-1)//2,p)==p-1
    # H=ker(N:k^*->F_p^*), and N(t)=-2 when t^2=2.
    fixed=1 + (d*(p-1))//d
    base=1+(p-1)//gcd(d,p-1)
    total=1+(q-1)//d
    assert total==fixed==p
    assert base==(p+1)//2
    return {'p':p,'extension':'F_373[t]/(t^2-2)','r':r,'d':d,
        'restricted_gauge':'H=mu_374(F_373^2)=kernel(norm_to_F_373)',
        'linear_H_orbits':total,'frobenius_fixed_H_orbits':fixed,
        'fixed_orbits_with_F_373_representative':base,
        'fixed_orbits_without_F_373_representative':fixed-base,
        'H1_size':2,'semilinear_H_orbits':p,
        'specific_source':'t','frobenius_of_source':'-t',
        'source_norm_mod_373':p-2,'source_norm_quadratic_character':-1,
        'base_field_norm_is_always_square':True,
        'claim':'auxiliary finite-field model only; not original-class H0/B0'}


def main():
    cases=[
        (2,2,1,3),(2,4,2,3),(2,4,2,5),(2,4,2,15),
        (3,2,1,2),(3,2,1,4),(3,2,2,4),(3,2,2,8),
        (3,3,1,13),(3,4,1,8),(3,4,2,8),
        (5,2,1,6),(5,2,2,3),(5,2,2,6),(5,2,2,8),
        (7,2,1,8),(7,2,2,8),
    ]
    out=[one_case(*z) for z in cases]
    result={'title':'general field-defined cyclic scalar gauge and Galois cohomology obstruction',
        'evidence_level':'AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_NATIVE',
        'coverage':'complete state and restricted-gauge orbit enumeration for each listed small finite field; p373 exact formula only',
        'cases':out,'case_count':len(out),'raw_vector_visits':sum(v['raw_vectors'] for v in out),
        'configuration_weighted_group_actions':sum(v['raw_vectors']*v['d'] for v in out),
        'p373':p373_exact_row(),'all_assertions':'PASS'}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
