#!/usr/bin/env python3
"""R253B: exact scaled-integer labelled observer and bit-size certificate.
Frozen positive scalar model 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Only Python standard library; no use of earlier R252/R253 implementation.
"""
from fractions import Fraction as F
from math import lcm
import json, hashlib
from pathlib import Path

W=(144,576,1440,4320,17280,86400,518400)
PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def setup(j):
    s=F(j,1000)
    t=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    assert sum(rho)==1
    P=[[a[i]*(i==q)+(1-a[i])*pi[q] for q in range(7)] for i in range(7)]
    assert all(all(x>0 for x in row) and sum(row)<=1 for row in P)
    return P,rho

def idx(m):
    return [0]+[u+1 for u in range(6) if m>>u&1]

def mm(A,B):
    d=len(A)
    return [[sum(A[i][h]*B[h][j] for h in range(d)) for j in range(d)] for i in range(d)]

def fast_power_on_ones(A,k):
    d=len(A); v=[1]*d
    while k:
        if k&1: v=[sum(A[i][j]*v[j] for j in range(d)) for i in range(d)]
        k//=2
        if k: A=mm(A,A)
    return v

def direct(P,rho,ix,w,k):
    v=[F(1)]*len(ix)
    for _ in range(k):
        v=[sum(P[i][j]*v[t] for t,j in enumerate(ix)) for i in ix]
    return w*sum(rho[i]*v[t] for t,i in enumerate(ix))

def check():
    rows=[]; tests=0; strict_bounds=0
    for j in (390,400,410):
        P,rho=setup(j)
        L=lcm(*(x.denominator for row in P for x in row))
        J=lcm(*((W[m.bit_count()]*rho[i]).denominator
                for m in range(63) for i in idx(m)))
        assert all((L*x).denominator==1 for row in P for x in row)
        for m in range(63):
            ix=idx(m); weight=W[m.bit_count()]
            A=[[int(L*P[i][q]) for q in ix] for i in ix]
            B=[int(J*weight*rho[i]) for i in ix]
            assert all(sum(row)<=L for row in A)
            for k in (0,1,2,8,32):
                v=fast_power_on_ones(A,k)
                N=sum(B[t]*v[t] for t in range(len(ix)))
                D=J*pow(L,k)
                assert 0<N<=J*weight*pow(L,k)
                reduced=F(N,D)
                assert reduced==direct(P,rho,ix,weight,k),(j,m,k)
                assert D%reduced.denominator==0
                assert reduced.numerator.bit_length() <= (J*weight*pow(L,k)).bit_length()
                tests+=1; strict_bounds+=1
        rows.append({'s':str(F(j,1000)),'L':str(L),'J':str(J),
                     'L_bits':L.bit_length(),'J_bits':J.bit_length(),
                     'mask_count':63,'k_values':[0,1,2,8,32],'exact_mask_checks':315})
    nonuniform=[]
    for q in (101,103,127,1009):
        s=F(2,5)+F(1,q)
        assert F(39,100)<s<F(41,100)
        p44=F(13,18)*s+F(5,36)
        assert p44==F(77*q+130,180*q)
        assert p44.denominator%q==0
        nonuniform.append({'prime':q,'s':str(s),'P44':str(p44),
                           'denominator_divisible_by_prime':True})
    manifest={'schema':'EM_R253B_FIXED_PARAMETER_OUTPUT_BITS_V1','frozen_science_pin':PIN,
      'theorem':'fixed rational s: 63 labelled reduced rational outputs have total bit length Theta(k), and integer-scaled binary matrix powers admit O_s(k^2) schoolbook-bit upper bound',
      'verified_parameter_anchors':rows,'compared_exponents':[0,1,2,8,32],
      'exact_fraction_vs_integer_scaled_matrix_checks':tests,
      'positive_and_denominator_bound_checks':strict_bounds,
      'nonuniform_rational_parameter_witnesses':nonuniform,
      'global_L_over_all_rational_parameters':'impossible: P44(s)=13s/18+5/36 has unbounded denominators as s=2/5+1/q, q prime>100',
      'status':'AUTHOR_PROVED_EXACT_COMPUTATION_NOT_REVIEWED',
      'scope':'63 positive scalar mask observer, fixed rational s; no native BRC port/histogram preservation; no sharp running-time claim',
      'all_pass':True}
    raw=json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    outfile=Path(__file__).with_name('R253B_verification.json')
    outfile.write_text(raw,encoding='utf-8')
    print('PASS exact comparisons',tests,'parameter primes',len(nonuniform))
    print('SHA256',hashlib.sha256(raw.encode()).hexdigest())
    print('PARAMS',[(r['s'],r['L'],r['J']) for r in rows])
    return manifest

if __name__=='__main__': check()
