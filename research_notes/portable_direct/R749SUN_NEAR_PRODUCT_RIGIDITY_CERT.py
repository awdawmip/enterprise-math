#!/usr/bin/env python3
"""R749SUN: standard-library exact integer/rational checks for universal two-Port defect rigidity.
This finite regression is supplementary to the written all-integer proof.
Frozen model: ad-uv=1, 1<=a,u,v,d<=M, tau=max(u,v)*ad, Q=u+v-a-d.
"""
import json
from math import isqrt
from fractions import Fraction

def near_product(M):
    assert M>=9999
    n=M+1
    t=isqrt(n)
    k=n-t*t
    j=1 if k<=t else 2
    target=j*t-k
    z=0
    while z*(z+j)<target:
        z+=1
    r=t-z
    s=t+z+j
    u=r*s-1
    delta=M-u
    A=u-r
    D=u-s
    V=u-r-s+1
    assert all(1<=w<=M for w in (A,u,V,D))
    assert A*D-u*V==1
    assert u>=V and u+V-A-D==1
    assert 0<=delta<=2*(isqrt(t)+int(isqrt(t)**2<t))+1
    return t,k,j,z,r,s,u,delta,A,V,D

def verify_all(t_min,t_max):
    count=0
    worst_slack=None
    worst_bound=Fraction(0)
    for t in range(t_min,t_max+1):
        for k in range(2*t+1):
            M=t*t+k-1
            T,K,j,z,r,s,u,delta,A,V,D=near_product(M)
            S_c=3*delta+r+s
            C=2
            # Exact product inequality, with no cube roots or floats.
            W=u*A*D
            assert 27*W >= (3*M-S_c-C)**3
            assert 6*u >= (r+s+2)**2
            B=2*t+6*(isqrt(t)+int(isqrt(t)**2<t))+7
            assert S_c+2<= B
            # General q-obstruction with S <= S_c+2: ((S^2)/4+1)/(M-S) < 2.
            SB=S_c+2
            assert SB < M
            assert SB*SB+4 < 8*(M-SB)
            bound=Fraction(SB*SB+4,4*(M-SB))
            if bound>worst_bound:
                worst_bound=bound
                worst_slack=(M,t,k,S_c+2)
            count+=1
    return count,worst_slack,f'{worst_bound.numerator}/{worst_bound.denominator}'

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            c[i+j]+=ai*bj
    return c

def poly_add(a,b):
    r=[0]*max(len(a),len(b))
    for i,v in enumerate(a):r[i]+=v
    for i,v in enumerate(b):r[i]+=v
    return r

def check_polynomial():
    # B=2x^2+6x+13 and F=8(x^4-1-B)-(B^2+4).
    B=[13,6,2]
    F=poly_add(poly_add([0,0,0,0,8],[-8]),[-8*x for x in B])
    F=poly_add(F,[-x for x in poly_mul(B,B)])
    F[0]-=4
    assert F==[-285,-204,-104,-24,4]
    # F(y+10) positive for y>=0: 4y4+136y3+1576y2+6516y+3275.
    from math import comb
    shifted=[sum(F[i]*comb(i,j)*10**(i-j) for i in range(j,len(F))) for j in range(len(F))]
    assert shifted==[3275,6516,1576,136,4]
    assert min(shifted)>0
    return shifted

def brute_small(M):
    best=-1; qs=set(); w=[]
    for a in range(1,M+1):
        for d in range(1,M+1):
            p=a*d-1
            if p<=0:continue
            for u in range(1,M+1):
                if p%u:continue
                v=p//u
                if v<1 or v>M:continue
                q=u+v-a-d
                canonical=(a==d and min(u,v)==a-1 and max(u,v)==a+1)
                assert (q==0)==canonical
                if canonical:continue
                score=max(u,v)*a*d
                if score>best:best=score;qs.clear();w=[]
                if score==best:qs.add(q);w.append((a,u,v,d))
    return best,sorted(qs),len(w)

if __name__=='__main__':
    small={str(M):brute_small(M) for M in range(2,27)}
    near=verify_all(100,150)
    poly=check_polynomial()
    o={"record":"R749SUN","status":"PASS","math":"exact_integers_only", "analytic_proof_domain":"all_M>=9999", "finite_source_dependency":"R749SUK@0b292a4181f3729b2bda282cf35e6df2166531e5 (exhaustive M=2..10000)","test_t_range":"100..150 complete k=0..2t", "test_cases":near[0],"worst_observed_integer_bound":near[2], "worst_case":near[1], "positive_shift_polynomial_coeffs_low_to_high":poly, "independent_small_brute_range":"2..26", "small_regressions":small, "not_reviewed":True}
    print(json.dumps(o,ensure_ascii=False,indent=2))
