#!/usr/bin/env python3
"""Exact rational implication certificate for PREFIX-653-R6.
Inputs: PREFIX-643 center-strip convexity and PREFIX-649 cumulant envelopes.
No new 189-layer or 96-port native dynamics run.
"""
from fractions import Fraction as Q
from json import dumps
checks = 0
def check(s, label):
    global checks
    assert s, label
    checks += 1
L, R = Q(3,20), Q(1,6)
mid = (L+R)/2
z0, h = Q(19,128), Q(1,2**18)
check(R-L == Q(1,60), "width")
check(mid == Q(19,120), "midpoint")
check((mid-L)*(R-mid) == Q(1,14400), "product")
check(z0-h < z0+h, "strip nonempty")
check(Q(1930,2)*(mid-L)*(R-mid) == Q(193,2880), "F gap")
check(12**2*Q(193,2880) == Q(193,20), "var gap q12")
check(24**2*Q(193,2880) == Q(193,5), "var gap q24")
nodes = [Q(1), Q(1,2), Q(1,4), Q(1,8)]
weights = [Q(-1,21), Q(2,3), Q(-8,3), Q(64,21)]
for k in range(4):
    check(sum(w*x**k for w,x in zip(weights,nodes)) == int(k==0), "degree %s"%k)
check(sum(w*x**4 for w,x in zip(weights,nodes)) == Q(-1,64), "degree4")
check(Q(1,24*64) == Q(1,1536), "remainder")
a,b,minus_c,d = 110,338,1266,86111
t = Q(1,12)
B0 = 325
U1 = Q(15*a**3,16)*(a*a*t*t+5*a*b*t+63*a*minus_c+120*b*b)/(B0**5*18)
U2 = Q(24*a*a)*(5*a*a*d+11*a*b*b*t+6*a*a*minus_c*t+24*a*b*minus_c+19*b**3)/(B0**6)
check(U1>0,"bound1 positive")
check(U2>0,"bound2 positive")
check(U1<Q(1,2),"g1 fourth")
check(U2<Q(7,4),"g2 fourth")
q=12
e1=Q(1,3072*q**4)
e2=Q(7,6144*q**4)
check(e1==Q(1,63700992),"q12 skew")
check(e2==Q(7,127401984),"q12 kurt")
check(e1<Q(1,10**7),"skew error")
check(e2<Q(1,10**7),"kurt error")
out={
"schema":"EM_PREFIX653_EXACT_IMPLICATION_V1",
"frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
"upstream":["PREFIX-643","PREFIX-649","PREFIX-650","PREFIX-651"],
"observer":"signed BRC dual-informative-direction first-stop statistical observer",
"max_exclusion":{"p_interval":[str(L),str(R)],"z_center":str(z0),
"z_half_width":str(h),"q_interval":[12,24],
"strict_Fpp_lower":1930,"midpoint_p":str(mid),
"strict_var_gap_q12":str(Q(193,20)),
"strict_var_gap_q24":str(Q(193,5))},
"four_slot":{"q_multipliers":[1,2,4,8],
"weights":[str(w) for w in weights],
"skew_derivative_lower":"-1/2",
"skew_derivative_upper":"0",
"kurt_derivative_lower":"0",
"kurt_derivative_upper":"7/4",
"skew_derivative_upper_bound_exact":str(U1),
"kurt_derivative_upper_bound_exact":str(U2),
"skew_extrap_error_q12":["0",str(e1)],
"kurt_extrap_error_q12":[str(-e2),"0"]},
"assertions_passed":checks,"result":"ALL_CHECKS_PASS",
"evidence_scope":"Exact rational implications of inherited upstream inequalities; no native experiment"}
print(dumps(out,ensure_ascii=False,indent=2))
print("ALL_CHECKS_PASS",checks)
