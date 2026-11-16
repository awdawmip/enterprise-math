#!/usr/bin/env python3
"""Optional exact SymPy proof: derive odd-BRC boundary D4 from Catalan ratios."""
import sympy as S
k=S.symbols('k', integer=True, positive=True)
def b(s):
    # For r=2k+1, H(r,s)/H(r,2), valid k>=2 and 2<=s<=6.
    pref=S.Rational(24,S.factorial(2*s))
    for m in list(range(2-s,0))+list(range(4,s+2)):
        pref*=2*k+m
    sm=S.Integer(0)
    for q in range((s-1)//2+1):
        num=S.prod((k-i)*(k+1-i) for i in range(q))
        den=S.prod(2*k-i for i in range(2*q))
        sm+=S.binomial(s-1,2*q)*4**q*S.cancel(S.sympify(num)/S.sympify(den))
    return S.factor(S.cancel(pref*sm))
bs={s:b(s) for s in range(2,7)}
D=S.factor(bs[3]**4-3*bs[3]**2*bs[4]+bs[4]**2+2*bs[3]*bs[5]-bs[6])
P=7936*k**7-309248*k**6-3408516*k**5-14300148*k**4-33616293*k**3-46354824*k**2-35761465*k-11787442
assert bs[2]==1
assert S.cancel(D+(k+2)*P/S.Integer(436590000))==0
assert P.subs(k,48)==-71552034705250 and P.subs(k,49)==52661023196976
print('R440_SYMBOLIC_PASS','b2..b6 derived','D4=-((k+2)*P(k))/436590000')
