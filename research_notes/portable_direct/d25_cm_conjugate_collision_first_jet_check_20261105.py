#!/usr/bin/env python3
"""Exact CM conjugate collision and jet observer test; no native benchmark claims."""
from sympy import symbols, sqrt, simplify, factorint, diff, primerange, legendre_symbol, Rational
T=sqrt(2)
u,v=symbols("u v")
J3=lambda x:27*(1+8*x)**3/(x*(1-x)**3)
J4=lambda x:64*(1+3*x)**3/(x*(1-x)**2)
a,b=2417472,1707264
assert factorint(b)=={2:8,3:3,13:1,19:1}
assert a*a-2*b*b==14670139392
for sign in (1,-1):
    u0=Rational(1,2)+sign*T/4
    v0=Rational(1,2)+sign*T/3
    assert simplify(J3(u0)-a-sign*b*T)==0
    assert simplify(J4(v0)-a-sign*b*T)==0
    u_dot=-sign*T/4
    v_dot=-sign*3*T/16
    jet=simplify(diff(J3(u),u).subs(u,u0)*u_dot/(diff(J4(v),v).subs(v,v0)*v_dot))
    assert simplify(jet-sign*8*T/27)==0
assert simplify((16*T/27)**2)==Rational(512,729)
records={}
target_count=0
for p in primerange(5,10000):
    if p%24 not in (13,19):
        continue
    target_count+=1
    assert legendre_symbol(2,p)==-1
    exceptional=p in (13,19)
    assert (b%p==0)==exceptional
    assert 16*pow(27,-1,p)%p != 0
    if p in (13,19,139,373):
        records[p]={"j_constant":a%p,"j_odd":b%p,
            "gap_valuation":int(exceptional),
            "gap_div_p_T": (2*(b//p))%p if exceptional else None,
            "jet_plus_T":8*pow(27,-1,p)%p,
            "jet_gap_T":16*pow(27,-1,p)%p}
assert target_count==312
assert records[13]["gap_div_p_T"]==4
assert records[19]["gap_div_p_T"]==10
print({"count":target_count,"exceptions":[13,19],"samples":records,"status":"PASS"})
