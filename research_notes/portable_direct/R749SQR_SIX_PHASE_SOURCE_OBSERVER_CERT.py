#!/usr/bin/env python3
"""R749SQR exact 6-phase source-observer certificate (standard library only).

All equal weights are distinct labeled sources. Exact arithmetic is Python int/Fraction.
This verifies finite examples and a polynomial reconstruction whose all-r validity
is proved separately by the cyclotomic-pole argument in the accompanying paper.
"""
import json
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial

S = (1, 1, 1, 2, 2, 3, 3)
MARKS = (0, 3, 5)  # h=1,2,3
MAX_R = 8005
PIN = "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389"
EXPECTED_SMOOTH = {
    1: ("1/8", "1/4", "-77/48", "77/8", "-7189/96", "10479/16", "-1179983/192"),
    2: ("1/8", "-1/4", "7/48", "-7/8", "959/96", "-1869/16", "259693/192"),
    3: ("1/8", "-3/4", "49/16", "-147/8", "4473/32", "-19089/16", "700091/64"),
}

def mul(a, b, N):
    c = [F(0)] * (N + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= N:
                c[i + j] += x * y
    return c

def reciprocal_factor(s, N):
    # R_s(w)=s*w/[1-(1-w)^s], analytic at w=0, R_s(0)=1
    den = [F((-1)**j * comb(s, j+1), s) if j+1 <= s else F(0)
           for j in range(N + 1)]
    out = [F(1)] + [F(0)] * N
    for k in range(1, N + 1):
        out[k] = -sum(den[j]*out[k-j] for j in range(1,k+1))
    return out

def binomial_poly(k):
    # coefficients in increasing r powers of binom(r+k,k)
    p = [F(1)]
    for j in range(1, k+1):
        q = [F(0)] * (len(p)+1)
        for i, v in enumerate(p):
            q[i] += j*v
            q[i+1] += v
        p = q
    return [v / factorial(k) for v in p]

def smooth_mean(s, order, marked):
    # F_s(z) = z/(1-z) * product(1-z^s)^-1, z=1-w
    d, h = len(s), s[marked]
    a = [F(1)] + [F(0)]*order
    for w in s:
        a = mul(a, reciprocal_factor(w, order), order)
    a = mul(a, [F(1), F(-1)] + [F(0)]*(order-1), order)
    hp = [F((-1)**j * comb(h,j)) if j <= h else F(0)
          for j in range(order+1)]
    b = mul(mul(a, reciprocal_factor(h, order), order), hp, order)
    cc, nn = [], []
    for t in range(order+1):
        cc.append(sum(a[j]*binomial_poly(d-j)[d-t] for j in range(t+1)))
        nn.append(sum(b[j]*binomial_poly(d+1-j)[d+1-t] for j in range(t+1)))
    out = []
    for t in range(order+1):
        out.append((nn[t]-sum(cc[j]*out[t-j] for j in range(1,t+1))) / cc[0])
    return out

def prefix_dp(s, R):
    exact = [0]*R
    moments = {m:[0]*R for m in MARKS}
    exact[0] = 1
    for i, weight in enumerate(s):
        for t in range(weight,R):
            earlier = exact[t-weight]
            exact[t] += earlier
            for m in MARKS:
                moments[m][t] += moments[m][t-weight] + (earlier if i==m else 0)
    C = [0]*(R+1)
    M = {m:[0]*(R+1) for m in MARKS}
    for r in range(1,R+1):
        C[r] = C[r-1]+exact[r-1]
        for m in MARKS:
            M[m][r] = M[m][r-1]+moments[m][r-1]
    return C,M

def brute(s, bound, marked):
    @lru_cache(None)
    def rec(i, remain):
        if i==len(s):return 1,0
        count=total=0
        for k in range(remain//s[i]+1):
            c,m=rec(i+1,remain-k*s[i]);count+=c;total+=m+(k*c if i==marked else 0)
        return count,total
    return rec(0,bound-1)

def newton_coeffs(samples):
    diffs=[];a=list(samples)
    while a:
        diffs.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return diffs

def phase(r,h):
    P=F(2835,32) * (-3 if h==2 else 1)
    Q=F(280,3) * (-3 if h==3 else 1)
    return P*(-1)**r + Q*(2 if r%3==0 else -1)

def run():
    C,M=prefix_dp(S,MAX_R)
    checks={"marked_deletion":0,"independent_brute":0,
            "newton_full_grid":0,"smooth_coefficients":0,
            "period_and_shift":0,"cyclotomic_amplitudes":0}
    # Root A_{-1}=-1/256, A_{omega}=A_{omega^2}=-1/243.
    # d!W/(d+1)=7!*36/8=22680; marked source belongs to
    # root order -> multiplier ratio is -3 (m=2,d=7).
    assert F(22680,256)==F(2835,32)
    assert F(22680,243)==F(280,3)
    checks["cyclotomic_amplitudes"]+=2
    smooth={}
    for m in MARKS:
        h=S[m]
        coefficients=smooth_mean(S,6,m)
        assert tuple(map(str,coefficients))==EXPECTED_SMOOTH[h]
        checks["smooth_coefficients"]+=7
        smooth[h]=coefficients
        # Marked deletion: M_h(r)=sum_{k>=1} C(r-k*h)
        for r in range(1,MAX_R+1):
            predicted=(C[r-h]+M[m][r-h]) if r>=h else 0
            assert M[m][r]==predicted, (r,h)
            checks["marked_deletion"]+=1
        for r in range(1,21):
            assert (C[r],M[m][r])==brute(S,r,m)
            checks["independent_brute"]+=1
    # All-r theorem: proper rational generating functions have only
    # roots of orders 1,2,3; z=1 pole order 8 for C, order 9 for T.
    # Thus on each r=a+6*n, C is degree <=7 and T= h*M degree <=8.
    newton_summary=[]
    for a in range(6):
        cc=newton_coeffs([C[a+6*n] for n in range(9)])
        assert cc[8]==0
        tm={}
        for m in MARKS:
            h=S[m];tm[h]=newton_coeffs([h*M[m][a+6*n] for n in range(9)])
        for r in range(a,MAX_R+1,6):
            n=(r-a)//6
            assert sum(comb(n,j)*cc[j] for j in range(8))==C[r]
            checks["newton_full_grid"]+=1
            for m in MARKS:
                h=S[m]
                assert sum(comb(n,j)*tm[h][j] for j in range(9))==h*M[m][r]
                checks["newton_full_grid"]+=1
        newton_summary.append({"class":a,"C_forward_differences":list(map(str,cc[:8])),
                               "T_forward_differences":{str(h):list(map(str,tm[h])) for h in (1,2,3)}})
    values=[phase(r,1) for r in range(6)]
    assert len(set(values))==4
    assert len(set((values[r],values[(r+1)%6]) for r in range(6)))==6
    assert all(any(values[r]!=values[(r+p)%6] for r in range(6)) for p in (1,2,3))
    assert values==[F(26425,96),F(-17465,96),F(-455,96),F(9415,96),F(-455,96),F(-17465,96)]
    checks["period_and_shift"]+=4
    samples=[]
    for r in (1200,1201,1202,1203,4000,4001,4002,4003,8000,8001,8002,8003):
        for m in MARKS:
            h=S[m]
            exact=F(h*M[m][r],r*C[r])
            smooth_value=sum(v/F(r**i) for i,v in enumerate(smooth[h]))
            scaled=F(r**6)*(exact-smooth_value)
            error=scaled-phase(r,h)
            samples.append({"r":r,"marked_weight":h,
                            "phase":str(phase(r,h)),
                            "scaled":format(float(scaled),".9f"),
                            "error":format(float(error),".9f")})
    return {"status":"PASS","input_pin":PIN,"model":"distinct positive labeled-source multiplicities; total weight <= r-1",
            "exact_arithmetic":"Python int and fractions.Fraction",
            "analytic_validity":"all r>=0 by root-of-unity partial fractions; E_r defined r>=1",
            "finite_validation_range":[0,MAX_R],"checks":checks,
            "observer_weights":[1,2,3],
            "smooth_coefficients":{str(h):list(map(str,smooth[h])) for h in (1,2,3)},
            "periodic_amplitudes":{str(h):{"parity":str(F(2835,32)*(-3 if h==2 else 1)),
                                            "cubic":str(F(280,3)*(-3 if h==3 else 1))} for h in (1,2,3)},
            "one_mark_phase_r_mod6":list(map(str,values)),
            "instant_phase_classes":4,"one_shift_joint_classes":6,
            "newton_coefficients":newton_summary,"scaled_samples":samples,
            "review_state":"AUTHOR_EXACT_NOT_REVIEWED",
            "limitations":"finite checks support but do not prove all-r partial-fraction theorem; no native X6/BRC type lift"}

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
