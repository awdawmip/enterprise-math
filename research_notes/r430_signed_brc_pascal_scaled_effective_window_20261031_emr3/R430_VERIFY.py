#!/usr/bin/env python3
"""R430 independent exact arithmetic checks for right-edge signed BRC.
Only finite tests: the infinite result is justified by the separate proof.
Python stdlib only. No float arithmetic or numerical root finding.
"""
from math import comb, factorial
from fractions import Fraction
from itertools import combinations
import json, hashlib
from pathlib import Path


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def signed_delta(r, h):
    """[t^r](1-t)(1+t)^(2(r-h))(1+t²)^h."""
    q = r - h
    out = 0
    for ell in range(h + 1):
        a = r - 2 * ell
        out += choose(h, ell) * (choose(2*q, a) - choose(2*q, a-1))
    return out


def signed_delta_dp(r, h):
    """Independent polynomial-convolution evaluator of the unsimplified signed carrier."""
    q = r - h
    poly = [choose(2*q, k) for k in range(2*q+1)]
    for _ in range(h):
        nxt = [0] * (len(poly)+2)
        for idx, val in enumerate(poly):
            nxt[idx] += val
            nxt[idx+2] += val
        poly = nxt
    return poly[r] - poly[r-1]


def catalan(n):
    return comb(2*n, n) // (n+1)


def normalized_right_edge(r, h):
    if h < 0 or h > r-2:
        return Fraction(0)
    q = r - h
    H = choose(r+q,2*q)*signed_delta(r,h)
    return Fraction(H,catalan(r)*r**h)


def det_exact(A):
    n = len(A)
    if n == 0:
        return Fraction(1)
    A = [[Fraction(z) for z in row] for row in A]
    ans = Fraction(1)
    for col in range(n):
        pivot = next((i for i in range(col,n) if A[i][col]),None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            A[pivot],A[col] = A[col],A[pivot]
            ans = -ans
        p = A[col][col]
        ans *= p
        for j in range(col+1,n):
            ratio = A[j][col]/p
            if ratio:
                for t in range(col+1,n):
                    A[j][t] -= ratio*A[col][t]
            A[j][col]=0
    return ans


def R_pfq(K,q):
    return 64*K**3*factorial(q)*q*2**((K+1)*q)


def R_pf2(K):
    return 256*K**4


def R429(K):
    return 2**(K+6)*K**3*factorial(K+1)*(K+1)*factorial(K)**(K+1)


def test_all():
    assertions=0
    checks=0
    minor_checks=0
    structural_positives=0
    structural_zeros=0
    term_bound_checks=0
    comparison=[]
    first_examples=[]
    for K in range(1,6):
        for r in (16*K*K, 32*K*K):
            assert r >= K+2
            c = [normalized_right_edge(r,h) for h in range(K+1)]
            epsilon=Fraction(32*K**3,r)
            for h in range(K+1):
                assert abs(c[h]-Fraction(1,factorial(h))) <= epsilon/factorial(h)
                assertions+=1
                # Independently convolve the original (1+t)^(2q)(1+t²)^h,
                # then apply the signed (1-t) branch without absolute values.
                assert signed_delta_dp(r,h)==signed_delta(r,h)
                checks+=1
            subs=[list(combinations(range(K+1),k)) for k in range(K+2)]
            for k in range(1,K+2):
                for u in subs[k]:
                    for v in subs[k]:
                        M=[[Fraction(factorial(vj),factorial(ui))*c[vj-ui] if vj>=ui else Fraction(0) for vj in v] for ui in u]
                        P=[[choose(vj,ui) for vj in v] for ui in u]
                        md=det_exact(M)
                        pd=det_exact(P)
                        active=all(vi>=ui for ui,vi in zip(u,v))
                        assert (pd>=1 if active else pd==0)
                        assert (md>0 if active else md==0)
                        if active:
                            structural_positives+=1
                        else:
                            structural_zeros+=1
                        minor_checks+=1
                        if len(first_examples)<6 and active and k>=2:
                            first_examples.append({"K":K,"r":r,"order":k,"u":u,"v":v,"pascal_det":str(pd),"signed_pascal_det":str(md)})
        for q in range(1,K+2):
            r=R_pfq(K,q)
            epsilon=Fraction(32*K**3,r)
            assert r>=16*K*K and epsilon<=1
            bound=factorial(q)*q*epsilon*2**((K+1)*q-1)
            assert bound<=Fraction(1,4)
            term_bound_checks+=1
        r=R_pf2(K)
        epsilon=Fraction(32*K**3,r)
        assert r>=16*K*K and epsilon <= Fraction(1,8*K)
        assert Fraction(1,K)-4*epsilon>=Fraction(1,2*K)
        term_bound_checks+=1
        comparison.append({"K":K,"R429":str(R429(K)),"R430_all_order":str(R_pfq(K,K+1)),"R430_PF2":str(R_pf2(K)),"all_order_improves":R_pfq(K,K+1)<R429(K)})
    # Check the algebraic 2-by-2 Pascal relative gap for all structural index sets.
    pair_gap_checks=0
    for K in range(2,31):
        for u1,u2 in combinations(range(K+1),2):
            for v1,v2 in combinations(range(K+1),2):
                if v1<u1 or v2<u2:
                    continue
                a=v1-u1; e=v2-v1; d=u2-u1
                if a<d:
                    rho=Fraction(0)
                else:
                    rho=Fraction(factorial(a)*factorial(a+e-d),factorial(a+e)*factorial(a-d))
                assert rho<=Fraction(K-1,K)
                pair_gap_checks+=1
    data={"status":"R430_EXACT_PASS","coefficient_exact_checks":checks,"r429_relative_error_checks":assertions,"full_window_exact_minor_checks":minor_checks,"strict_minor_checks":structural_positives,"zero_minor_checks":structural_zeros,"parametric_threshold_bound_checks":term_bound_checks,"two_by_two_gap_checks":pair_gap_checks,"selected_thresholds":comparison,"examples":first_examples,"scope":"K 1..5 r in {16K^2,32K^2} for finite minors; K<=5, q<=K+1 for threshold algebra checks; K 2..30 for ratio gap check; no sample proves universal theorem"}
    out=Path(__file__).with_name('R430_EVIDENCE.json')
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('R430_EXACT_PASS',checks,assertions,minor_checks,structural_positives,structural_zeros,term_bound_checks,pair_gap_checks)
    print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
    for t in comparison: print('K',t['K'],'R429',t['R429'],'new',t['R430_all_order'],'pf2',t['R430_PF2'])

if __name__=='__main__':
    test_all()
