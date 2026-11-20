#!/usr/bin/env python3
"""Exact X6 signed primitive + frozen A3 weighted-field fiber checks.

Scientific source: enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03
Historical A3 source: enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3
No imported/deployed/native benchmark claims: formulas independently reimplemented.
"""
from __future__ import annotations
from itertools import product
from math import gcd, factorial
from functools import reduce
from hashlib import sha256
import json



def extended_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    d, x, y = extended_gcd(b, a % b)
    return d, y, x - (a // b) * y


def bezout_for_sizes(m: tuple[int,...]):
    g, coeff = m[0], [1]
    for mm in m[1:]:
        gg, x, y = extended_gcd(g, mm)
        coeff = [q*x for q in coeff] + [y]
        g = gg
    if sum(u*q for u,q in zip(coeff,m)) != g:
        raise RuntimeError('Bezout witness failed')
    return g, tuple(coeff)


def representative_from_field(m, Z):
    g, u = bezout_for_sizes(m)
    rows = tuple(sum(u[j]*Z[i][j] for j in range(6)) for i in range(6))
    if any(x % g for x in rows):
        raise ValueError('Field has no integer source representative')
    z0 = tuple(x//g for x in rows)
    if weighted_field(m,z0) != Z:
        raise RuntimeError('Recovered representative does not reproduce field')
    return z0

def ceiling_div(n: int, d: int) -> int:
    if d == 0:
        raise ValueError('division by zero')
    return -((-n) // d)


def weighted_field(m: tuple[int, ...], z: tuple[int, ...]):
    return tuple(tuple(m[j]*z[i]-m[i]*z[j] for j in range(6)) for i in range(6))


def recover_with_total(m: tuple[int, ...], Z, C: int):
    # Exact frozen A3 production formula, independently implemented.
    T = sum(m)
    out = []
    for i in range(6):
        numer = m[i]*C+sum(Z[i])
        if numer % T:
            raise ValueError('not integer-compatible')
        out.append(numer//T)
    if sum(out)!=C or weighted_field(m, tuple(out))!=Z:
        raise ValueError('source formula failed')
    return tuple(out)


def affine_interval(m: tuple[int, ...], z: tuple[int, ...], M: int):
    g=reduce(gcd, m)
    v=tuple(u//g for u in m)
    low, high = None, None
    for signs in product((-1,1), repeat=6):
        slope=sum(signs[i]*v[i] for i in range(6))
        b=sum(signs[i]*z[i] for i in range(6))
        if slope==0:
            if b>M:
                return (), None
        elif slope>0:
            bound=(M-b)//slope
            high = bound if high is None else min(high,bound)
        else:
            bound=ceiling_div(M-b,slope)
            low = bound if low is None else max(low,bound)
    if low is None or high is None or low>high:
        return (), (low,high,0)
    Q=sum(v)
    if Q%2==0:
        if (M-sum(z))%2:
            return (), (low,high,0)
        step, first=1,low
    else:
        step=2
        first=low+((M-sum(z)-low)%2)
    if first>high:
        return (), (low,high,step)
    return tuple(range(first,high+1,step)), (low,high,step)


def brute_interval(m: tuple[int, ...], z: tuple[int, ...], M: int):
    g=reduce(gcd,m)
    v=tuple(q//g for q in m)
    Q=sum(v)
    S=sum(z)
    # L1(x) >= abs(sum(x)), bounds follow without using sign-plane algorithm.
    low=ceiling_div(-M-S,Q)
    high=(M-S)//Q
    return tuple(t for t in range(low,high+1) if
      sum(abs(z[i]+t*v[i]) for i in range(6))<=M and
      (M-sum(z[i]+t*v[i] for i in range(6)))%2==0)


def check(cond: bool, detail: str):
    if not cond: raise RuntimeError(detail)


def main():
    capacity_vectors = [
       (1,1,1,1,1,1),      # previous Unit184 special case Q=6 even
       (1,2,1,1,1,1),      # Q=7 odd, two-step parity lattice
       (2,2,2,2,2,4),      # gcd=2, primitive Q=7 odd
       (1,1,1,1,1,2),      # Q=7 odd
       (2,3,4,5,6,7),      # Q=27 odd
       (2,2,2,2,2,2),      # constant weights, Q=6 even
       (1,1,1,1,2,2),      # Q=8 even
       (2,3,2,3,2,4),      # Q=16 even
    ]
    # Reproducible, bounded integer-state corpus with deliberate negative coordinates.
    states=list(product(range(-2,3),repeat=6))[::7]
    states.extend([(0,)*6,(1,)*6,(-1,)*6,(3,-3,1,-2,0,4)])
    counts={"cases":0,"nonempty":0,"empty":0,"multi":0,
            "odd_step_two":0,"even_step_one":0,
            "production_total_reconstructions":0,"bezout_repairs_checked":0,"native_brc_endpoints_checked":0,
            "max_fiber":0,"failures":0}
    witness=[]
    for m in capacity_vectors:
        g=reduce(gcd,m); v=tuple(x//g for x in m); Q=sum(v)
        check(reduce(gcd,v)==1, f'not primitive {m}')
        for z in states:
            Z=weighted_field(m,z)
            zref=representative_from_field(m,Z)
            check(weighted_field(m,zref)==Z,'canonical representative field mismatch')
            check(all((z[i]-zref[i])%v[i]==0 for i in range(6)), 'kernel integrality')
            counts['bezout_repairs_checked']+=1
            for k in (0,1,2):
                M=sum(abs(x) for x in z)+k
                predicted,span=affine_interval(m,z,M)
                brute=brute_interval(m,z,M)
                check(predicted==brute, f'fiber mismatch m={m},z={z},M={M}: {predicted},{brute}')
                from_field, _ = affine_interval(m,zref,M)
                native_from_field = {tuple(zref[i]+t*v[i] for i in range(6)) for t in from_field}
                native_from_original = {tuple(z[i]+t*v[i] for i in range(6)) for t in brute}
                check(native_from_field==native_from_original, f'field-only recovery mismatch: {m},{z},{M}')
                counts['cases']+=1
                if predicted: counts['nonempty']+=1
                else: counts['empty']+=1
                if len(predicted)>1:counts['multi']+=1
                counts['max_fiber']=max(counts['max_fiber'],len(predicted))
                if span and span[2]==2: counts['odd_step_two']+=1
                elif span and span[2]==1: counts['even_step_one']+=1
                for j,t in enumerate(predicted):
                    zz=tuple(z[i]+t*v[i] for i in range(6))
                    check(weighted_field(m,zz)==Z, f'field not invariant for m={m},t={t}')
                    C=sum(zz)
                    got=recover_with_total(m,Z,C)
                    check(got==zz,f'grand-total inverse mismatch {m},{zz}')
                    check(C==sum(z)+Q*t,'C arithmetic progression mismatch')
                    counts['production_total_reconstructions']+=1
                if m==(1,2,1,1,1,1) and z==(0,)*6 and M in (7,14):
                    witness.append({"m":list(m),"M":M,"t":list(predicted)})
    # Explicit weighted-vs-diagonal observer nonfactorization witness.
    m=(1,2,1,1,1,1); z0=(0,)*6; d=(1,)*6; v=m
    check(weighted_field(m,z0)!=weighted_field(m,d),'nonuniform field must change under diagonal shift')
    check(weighted_field(m,z0)==weighted_field(m,v),'kernel m shift must be invisible')
    can=lambda x: tuple(y-min(x) for y in x)
    check(can(z0)==can(d) and can(z0)!=can(v),'observer incompatibility witness')
    # At horizon M=7, zero field hides endpoints +/- primitive capacity vector.
    zero_fiber,span=affine_interval(m,z0,7)
    check(zero_fiber==(-1,1),f'Q odd sparse lift witness: {zero_fiber}')
    # Fixed signed-unit axis endpoints have N_7(+/-m)=7!/2!=2520 shortest words.
    B=factorial(7)
    for coord in v: B//=factorial(coord)
    check(B==2520,'BRC path-count witness')
    counts['native_brc_endpoints_checked']=2
    second,_=affine_interval(m,z0,14)
    check(second==(-2,0,2),f'Q odd parity progression M=14: {second}')
    doc={
      'schema':'X6_UNIT187_EXACT_WEIGHTED_RELATION_FIBER_CHECK_V1',
      'frozen_science_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
      'historical_source_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
      'input_capacity_vectors':[list(m) for m in capacity_vectors],
      'states_per_capacity':len(states),
      'horizon_offsets':[0,1,2],
      'counts':counts,
      'witness_nonuniform_capacity':{
        'm':[1,2,1,1,1,1], 'g':1,'v':[1,2,1,1,1,1], 'Q':7,
        'M':7,'field_all_zero':True,
        'allowed_lifts':[-1,1],
        'signed_axis_path_counts':{'negative':2520,'positive':2520},
        'relative_q_collision': 'q(0)=q((1,1,1,1,1,1)) but their weighted fields differ',
        'weighted_field_collision': 'field(0)=field((1,2,1,1,1,1))=0 but their q differ',
      },
      'witnesses':witness,
      'direct_original_module_imported':False,
      'original_native_R063_benchmark_rerun':False,
      'violations':0,
    }
    with open('/mnt/data/x6_unit187/exact_results.json','w',encoding='utf-8') as f:
        json.dump(doc,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({'counts':counts,'witness':doc['witness_nonuniform_capacity']},ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
