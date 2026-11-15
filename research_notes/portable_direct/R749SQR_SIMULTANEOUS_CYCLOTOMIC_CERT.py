#!/usr/bin/env python3
"""R749SQR exact finite checks for simultaneous order-2/order-3 source phases.
Model: labeled nonnegative counts, sum(s_i*k_i)<=r-1; pure integer/Fraction.
No claim that finite samples prove a large-r asymptotic statement.
"""
import json
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache

WEIGHTS=(1,1,2,3,6)
SAMPLES=(120,121,122,123,124,125,600,601,602,603,604,605,6000,6001,6002,6003,6004,6005)


def poly_mul(a,b,n):
    c=[F(0)]*(n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n:c[i+j]+=x*y
    return c


def reciprocal_weight(s,n):
    # 1 / ((1-(1-w)**s)/(s*w))
    den=[F((-1)**j*comb(s,j+1),s) if j+1<=s else F(0) for j in range(n+1)]
    a=[F(1)]+[F(0)]*n
    for k in range(1,n+1):
        a[k]=-sum(den[j]*a[k-j] for j in range(1,k+1))
    return a


def shifted_binomial(k):
    # binom(r+k,k), from [z^(r-1)](1-z)^(-k-1)
    p=[F(1)]
    for j in range(1,k+1):
        q=[F(0)]*(len(p)+1)
        for i,v in enumerate(p):
            q[i]+=j*v
            q[i+1]+=v
        p=q
    return [v/factorial(k) for v in p]


def smooth_mean(s,order,mark):
    d,h=len(s),s[mark]
    assert order<=d
    a=[F(1)]+[F(0)]*order
    for v in s:a=poly_mul(a,reciprocal_weight(v,order),order)
    a=poly_mul(a,[F(1),F(-1)]+[F(0)]*(order-1),order)
    hp=[F((-1)**j*comb(h,j)) if j<=h else F(0) for j in range(order+1)]
    b=poly_mul(poly_mul(a,reciprocal_weight(h,order),order),hp,order)
    c=[];t=[]
    for k in range(order+1):
        c.append(sum(a[j]*shifted_binomial(d-j)[d-k] for j in range(k+1)))
        t.append(sum(b[j]*shifted_binomial(d+1-j)[d+1-k] for j in range(k+1)))
    mean=[]
    for k in range(order+1):
        mean.append((t[k]-sum(c[j]*mean[k-j] for j in range(1,k+1)))/c[0])
    return mean


def prefix_counts(s,n):
    d=len(s)
    exact=[0]*n;exact[0]=1
    mk=[[0]*n for _ in range(d)]
    for j,w in enumerate(s):
        for t in range(w,n):
            exact[t]+=exact[t-w]
            for i in range(d):
                mk[i][t]+=mk[i][t-w]+(exact[t-w] if i==j else 0)
    C=[0]*(n+1);T=[[0]*(n+1) for _ in range(d)]
    for r in range(1,n+1):
        C[r]=C[r-1]+exact[r-1]
        for j,w in enumerate(s):T[j][r]=T[j][r-1]+w*mk[j][r-1]
    return C,T


def brute_counts(s,r):
    @lru_cache(None)
    def visit(j,budget):
        if j==len(s):return (1,)+(0,)*len(s)
        out=[0]*(len(s)+1)
        for k in range(budget//s[j]+1):
            z=visit(j+1,budget-k*s[j]);out[0]+=z[0]
            for i in range(len(s)):
                out[i+1]+=z[i+1]+(s[j]*k*z[0] if i==j else 0)
        return tuple(out)
    return visit(0,r-1)


def phase(r,h):
    a2=F(15,4) if h%2 else -F(15,2)
    a3=F(40,9) if h%3 else -F(80,9)
    return a2*((-1)**r)+a3*(2 if r%3==0 else -1)


def run():
    s=WEIGHTS
    smooth={str(j):[str(x) for x in smooth_mean(s,4,j)] for j in (0,2,3,4)}
    assert smooth['0']==['1/6','1/2','-115/36','115/6','-16315/108']
    assert phase(0,1)==F(455,36)
    assert [phase(r,1) for r in range(6)]==[F(455,36),-F(295,36),-F(25,36),F(185,36),-F(25,36),-F(295,36)]
    assert [phase(r,1) for r in range(6)]==[phase(r+6,1) for r in range(6)]
    for j in (0,2,3,4):
        assert all(phase(r+6,s[j])==phase(r,s[j]) for r in range(6))
        assert any(phase(r+2,s[j])!=phase(r,s[j]) for r in range(6))
        assert any(phase(r+3,s[j])!=phase(r,s[j]) for r in range(6))
    pairs=[(phase(r,1),phase(r+1,1)) for r in range(6)]
    assert len(set(pairs))==6
    assert len(set(phase(r,1) for r in range(6)))==4
    for r in range(12):
        assert phase(r,1)-phase(r,2)==F(45,4)*(-1)**r
        assert phase(r,1)-phase(r,3)==F(40,3)*(2 if r%3==0 else -1)
    C,T=prefix_counts(s,max(SAMPLES))
    independent=0
    for r in range(1,33):
        z=brute_counts(s,r)
        assert z==(C[r],)+(tuple(t[r] for t in T))
        independent+=1
    # Check T_j(r)=h sum_{a>=1} C_{r-ah}, exact deletion of marked copies.
    deletion=0
    for j in (0,2,3,4):
        h=s[j]; recurrence=[0]*1001
        for r in range(1,1001):
            recurrence[r]=(C[r-h]+recurrence[r-h]) if r>h else 0
            assert T[j][r]==h*recurrence[r]
            deletion+=1
    comparison=[]
    for r in SAMPLES:
        m=F(T[0][r],r*C[r]); coeff=[F(x) for x in smooth['0']]
        residual=r**4*(m-sum(v/F(r**i) for i,v in enumerate(coeff)))
        predicted=phase(r,1)
        comparison.append({'r':r,'phase_class':r%6,'predicted_scaled_residual':str(predicted),
                          'scaled_residual_error':str(residual-predicted),
                          'numeric_error':float(residual-predicted)})
    return {'status':'PASS','model':'positive labeled source alphabet, strict prefix sum <= r-1',
            'source_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'source_weights':list(s),'mark_indices_checked':[0,2,3,4],
            'smooth_coefficients_by_mark':smooth,
            'phase_1_by_mod_6':[str(phase(r,1)) for r in range(6)],
            'phase_1_two_step_by_mod_6':[[str(v) for v in pair] for pair in pairs],
            'phase_by_mark':{str(j):[str(phase(r,s[j])) for r in range(6)] for j in (0,2,3,4)},
            'checks':{'independent_small_r':independent,'marked_deletion':deletion,
                      'periodic_pattern':24,'two_step_distinct':6,'difference_decompositions':24},
            'largest_exact_prefix':max(SAMPLES),'samples':comparison,
            'math_proof_scope':'root-of-unity rational generating function proof in companion note; finite checks are supporting evidence',
            'formal_review':'NOT_REVIEWED'}


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
