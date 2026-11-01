#!/usr/bin/env python3
"""Exact quadratic-cutoff Frobenius swap/carry certificate (source-preserving)."""
from d25_legendre_p2_reflection_antitrace_20261101 import (
    quadratic_pullback_coefficients, evaluate_quad, mul_quad, tuple_power_quad,
    gauss_beta, period_coefficients, primes_to)


def add(x,y,N): return ((x[0]+y[0])%N,(x[1]+y[1])%N)
def scalar(x,a,N): return (x[0]*a%N,x[1]*a%N)
def conj(x,N): return (x[0]%N,-x[1]%N)

def legendre_root_selector_check(p):
    """Independent O(p) recurrence in F_p[s]/(s^2-2), s=√2.

    This is finite evidence of CM selection, never an all-prime proof.
    """
    assert p % 24 == 13
    n=(p-1)//4
    x=(0,2*pow(3,-1,p)%p)  # 1-2t_-=2sqrt(2)/3
    prev=(1,0)
    cur=x
    for k in range(1,n):
        step=mul_quad(scalar(x,2*k+1,p),cur,p)
        nxt=scalar(add(step,scalar(prev,-k,p),p),pow(k+1,-1,p),p)
        prev,cur=cur,nxt
    assert cur==(0,0),(p,cur)
    return cur


def check(p):
    assert p%8==5
    N=p*p; inv2=pow(2,-1,N)
    t=(inv2,-pow(3,-1,N)%N)
    s=conj(t,N)
    h=quadratic_pullback_coefficients(p)
    H=evaluate_quad(h,t,N)
    Hs=evaluate_quad(h,s,N)
    period=evaluate_quad(period_coefficients(p),t,N)
    # Verify that the finite CM selector has its original p13 precision.
    original_first=gauss_beta(p)%p
    period_first=(period[0]%p,period[1]%p)
    if p%24==13:
        assert original_first==0 and period_first==(0,0), (p,original_first,period_first)
        assert H[0]%p==H[1]%p==0, (p,H)
    tp=tuple_power_quad(t,p,N)
    # Fermat quotient in the algebraic quadratic ring: componentwise lift.
    dr=(tp[0]-s[0])%N
    di=(tp[1]-s[1])%N
    assert dr%p==di%p==0,(p,dr,di)
    D=(dr//p,di//p)
    Ds=conj(D,p)
    # Leading Frobenius exchange, plus one labelled p-adic carry.
    main=scalar(add(mul_quad(s,H,N),mul_quad(t,Hs,N),N),inv2,N)
    carry=scalar(add(mul_quad(D,H,N),mul_quad(Ds,Hs,N),N),p*inv2,N)
    assert main[1]==carry[1]==0
    gamma=gauss_beta(p)
    assert (main[0]+carry[0])%N==gamma,(p,main,carry,gamma)
    if p%24==13:
        assert carry==(0,0), (p,carry)
        assert main[0]%p==0, (p,main)
        h_over_p=(H[0]//p,H[1]//p)
        # The p-adic Frobenius error vanishes because the entire high tail is order p.
        even_reduced=mul_quad(scalar(add(mul_quad(s,h_over_p,p),
                             mul_quad(t,conj(h_over_p,p),p),p),pow(2,-1,p),p), (1,0),p)
        assert even_reduced[1]==0 and even_reduced[0]==gamma//p, (p,even_reduced,gamma)
    original_t=mul_quad(tp,H,N)
    assert add(original_t,conj(original_t,N),N)==(2*gamma%N,0)
    return {'p':p,'F':gamma,'D':D,'H':H,'main':main[0],'carry':carry[0],
            'main_first':main[0]//p if main[0]%p==0 else None,
            'carry_first':carry[0]//p if carry[0]%p==0 else None}

if __name__=='__main__':
    # Finite evidence for the p13 CM root input with independent Legendre recursion.
    target=[p for p in primes_to(10000) if p%24==13]
    assert len(target)==157
    for p in target:
        legendre_root_selector_check(p)
    print('PASS_P13_LEGENDRE_CM_ROOT_FINITE 157 primes <=10000')
    for p in (13,29,37,53,61,109,157,181,229,373):
        print(check(p))
