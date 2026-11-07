#!/usr/bin/env python3
"""Exact Stage392-B native X6 T_i^± / signed shortest-path BRC observer test.

Source model: pinned P000-V5 native six-axis torsor & V17 signed shortest paths;
Bernoulli test sidecars are inherited verbatim from Stage391-B, not native physics.
No floats, propagators, trig or matrix exponential are used.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
from math import factorial
from pathlib import Path
import json

EM_SCIENCE_PIN = '2af3fc484eb11060b69e0afc1b562bcaf5ad1419'
GK_SCIENCE_PIN = 'bf84bd7c61a2444b59b1da96be57df0e9ae47e53'
P000_BLOB = 'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'
D = (1,)*6
TRIPLES = tuple(combinations(range(6),3))
PARAMS = {'P': (Q(1,4),Q(3,4)), 'Q': (Q(1,3),Q(2,3))}
M = (61,21,9,9)


def bernstein(k,z):
    return z**k*(1-z)**(3-k)


def source_sidecar(sigma):
    u,v = PARAMS[sigma]
    audits = tuple(bernstein(k,z)-bernstein(k,q) for z,q in
                   ((u,Q(1,4)),(u,Q(3,4)),(v,Q(1,4)),(v,Q(3,4))) for k in range(4))
    residuals = tuple((4*bernstein(k,u)+bernstein(k,v))/5-Q(M[k],160) for k in range(4))
    assert len(audits)==16 and len(residuals)==4
    return (audits,residuals)


def relative_20(a):
    out = []
    for i,j,k in TRIPLES:
        z = (a[i],a[j],a[k])
        v = min(z)
        out.append(tuple(x-v for x in z))
    return tuple(out)


def native_brc(a):
    counts = tuple(abs(x) for x in a)
    n = sum(counts)
    denom = 1
    for u in counts:
        denom *= factorial(u)
    return (n, factorial(n)//denom)


def observer(a, sigma='P', index=0):
    return (relative_20(a), native_brc(a), index, sigma, source_sidecar(sigma))


def native_step(a,i,sign):
    out = list(a)
    out[i] += sign
    return tuple(out)


def chart_reconstruct(r,h):
    # Recover relative offsets against selected E1, then restore the minimum.
    offsets = [0]
    for target in range(1,6):
        tri_index = next(j for j,tri in enumerate(TRIPLES) if 0 in tri and target in tri)
        tri = TRIPLES[tri_index]
        values = r[tri_index]
        offsets.append(values[tri.index(target)]-values[tri.index(0)])
    base = min(offsets)
    return tuple(v-base+h for v in offsets)


def family(t,k):
    assert t>=0 and k>=1
    a = (-(t+k),)*3 + (t,)*3
    b = (-t,)*3 + (t+k,)*3
    assert b == tuple(v+k for v in a)
    return a,b


def rational_pair(x):
    return [x.numerator,x.denominator]


def main():
    assert len(TRIPLES)==20
    assert source_sidecar('P')!=source_sidecar('Q')
    family_cases=0
    ratio_cases=0
    zero_cases=0
    for sigma in PARAMS:
        for t in range(11):
            for k in range(1,13):
                a,b = family(t,k)
                assert observer(a,sigma)==observer(b,sigma)
                assert native_brc(a)[0] == 6*t+3*k
                a1,b1 = native_step(a,0,+1),native_step(b,0,+1)
                assert observer(a1,sigma,1)!=observer(b1,sigma,1)
                if t==0:
                    assert native_brc(b1)[0]-native_brc(a1)[0]==2
                    zero_cases+=1
                else:
                    na,ma = native_brc(a1)
                    nb,mb = native_brc(b1)
                    assert na==nb==6*t+3*k-1
                    assert Q(mb,ma)==Q(t,t+k)
                    ratio_cases+=1
                family_cases+=1
    assert (family_cases,zero_cases,ratio_cases)==(264,24,240)

    translation_checks=0
    reconstruction_checks=0
    for raw in product((-1,0,1),repeat=6):
        r = relative_20(raw)
        assert chart_reconstruct(r,min(raw))==raw
        reconstruction_checks+=1
        for k in (-2,1,3):
            translated=tuple(x+k for x in raw)
            assert relative_20(translated)==r
            for i in range(6):
                for sign in (-1,1):
                    assert relative_20(native_step(raw,i,sign)) == relative_20(native_step(translated,i,sign))
                    translation_checks+=1
    assert (reconstruction_checks,translation_checks)==(729,26244)

    # A second two-step calculation witnesses that an arbitrary chosen finite
    # residue (in particular parity) is not a full future-safe repair.
    for modulus in range(1,21):
        a,b=family(2,modulus)
        assert (min(a)-min(b))%modulus==0
        assert observer(a)==observer(b)
        assert native_brc(native_step(b,0,1))[1] * (2+modulus) == native_brc(native_step(a,0,1))[1]*2

    a,b = family(1,2)
    a1,b1=native_step(a,0,1),native_step(b,0,1)
    sidecars={sigma:{'audits':[rational_pair(x) for x in source_sidecar(sigma)[0]],
                      'residuals':[rational_pair(x) for x in source_sidecar(sigma)[1]]}
              for sigma in PARAMS}
    cert={
        'schema':'EM_STAGE392B_NATIVE_T_BRC_FIBER_V1',
        'scientific_pins':{'enterprise_math':EM_SCIENCE_PIN,'global_knowledge':GK_SCIENCE_PIN,'p000_blob':P000_BLOB},
        'native_operations':'T_i^+ and T_i^- on a fixed-anchor signed X6 Cell chart',
        'observer':'all twenty three-component can3 observers, native shortest-path N_min and B_min, abstract step index, source-labelled Bernoulli test sidecars',
        'source_sidecars':sidecars,
        'parametric_family':'a=(-t-k)*3 concatenated with (t)*3; b=(-t)*3 concatenated with (t+k)*3; t>=0,k>=1',
        'parametric_theorem':'O(a)=O(b); for t>=1 after +E1 the N_min agree and B_min(b+e1)/B_min(a+e1)=t/(t+k); for t=0 after +E1 N_min differ by two',
        'witness_t1_k2':{'a':list(a),'b':list(b),'before_BRC':list(native_brc(a)),'after_a_BRC':list(native_brc(a1)),'after_b_BRC':list(native_brc(b1)),'after_ratio':rational_pair(Q(native_brc(b1)[1],native_brc(a1)[1]))},
        'all_finite_words_theorem':'relative-only quotient is T-descending; for observer including anchored native N_min, all-word future equivalence is equality of full signed X6 state; can6+integer common depth h is a sufficient lossless repair',
        'finite_checks':{'family_both_sources':family_cases,'t_zero_boundary':zero_cases,'positive_t_ratio':ratio_cases,'relative_reconstruction_grid':reconstruction_checks,'translation_descent_grid':translation_checks,'tested_moduli':20},
        'scope':'exact internal X6 signed raw displacement relative to fixed chosen anchor; BRC counts not amplitudes, cell addresses or physical heartbeat transitions; conditional on source-defined T_i coordinate steps; not formally Driver-admitted'
    }
    encoded=(json.dumps(cert,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n').encode()
    out=Path(__file__).with_name('CERTIFICATE_STAGE392B_NATIVE_T_BRC.json')
    out.write_bytes(encoded)
    print('STAGE392B_NATIVE_T_BRC_FIBER_PASS')
    for label,value in cert['finite_checks'].items():
        print(label,value)
    print('witness_t1_k2',cert['witness_t1_k2'])
    print('certificate_bytes',len(encoded))
    print('certificate_sha256',sha256(encoded).hexdigest())


if __name__=='__main__':
    main()
