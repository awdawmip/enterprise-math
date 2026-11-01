#!/usr/bin/env python3
"""PREFIX-344: exact-rational 16-panel convex integral enclosure.
No floating-point, angle grid, trig, pi, or native X6 simulation.
The algebraic BRC data N, q and predecessor five-contact bound B are pinned.
"""
from fractions import Fraction as F
from math import isqrt
import json

N = F(347150,115351)
q = F(29125,29768)
L = F(1062562,458329)
B = F(16322694483,6250000000)  # strict five-contact MEB^2 lower bound, PREFIX-342
RLOW = F(808027,500000)         # strict lower rational bound for sqrt(B)
H_MINUS = F(193153,125000)    # 1.545224
H_PLUS = F(61809,40000)      # 1.545225
D = 10**12
PANELS = 16

def integer_sqrt_interval(r):
    assert r >= 0
    k = isqrt((r.numerator*D*D)//r.denominator)
    lo = F(k,D)
    hi = F(k+1,D)
    assert lo*lo <= r < hi*hi
    return lo,hi

def f_interval(t):
    assert F(0) <= t and t*t < q
    return integer_sqrt_interval(N/(q-t*t))

def integral_brackets(h):
    a = F(1,2)
    b = h-F(1)
    assert b >= a and b*b < q
    step = (b-a)/PANELS
    # Midpoint lower bound and composite trapezoid upper bound, f''(t)>0.
    low = step*sum((f_interval(a+(F(2*j+1,2))*step)[0] for j in range(PANELS)),F(0))
    up = step*(F(1,2)*f_interval(a)[1]
        + sum((f_interval(a+j*step)[1] for j in range(1,PANELS)),F(0))
        + F(1,2)*f_interval(b)[1])
    assert low < up
    return low,up

assert RLOW*RLOW < B
assert B > L
lm,um = integral_brackets(H_MINUS)
lp,up = integral_brackets(H_PLUS)
rad = RLOW-um
assert rad > 0 and rad*rad > L
lb_sqrt_L,ub_sqrt_L = integer_sqrt_interval(L)
lb_sqrt_B,ub_sqrt_B = integer_sqrt_interval(B)
assert ub_sqrt_B-lp < lb_sqrt_L
assert lm <= um and lp <= up
assert lp > lm

results={
  'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL_CONDITIONAL_ON_PREFIX342_FIVE_CONTACT',
  'method':'16-panel convex midpoint/trapezoid enclosure; sqrt brackets D=10^12',
  'exact_input':{ 'N':str(N),'q':str(q),'L':str(L),'B':str(B)},
  'h_lower':str(H_MINUS),'h_upper':str(H_PLUS),
  'h_lower_decimal':float(H_MINUS),'h_upper_decimal':float(H_PLUS),
  'I_lower_at_h_lower':str(lm),'I_upper_at_h_lower':str(um),
  'I_lower_at_h_upper':str(lp),'I_upper_at_h_upper':str(up),
  'RLOW':str(RLOW),
  'RLOW_minus_Iupper_at_h_lower':str(rad),
  'strict_super_L_margin':str(rad*rad-L),
  'strict_upper_failure_at_h_upper':str(lb_sqrt_L-(ub_sqrt_B-lp)),
  'panels':PANELS,'sqrt_scale':D,
  'predecessor_dependency':'PREFIX342 contact set existence and strict B lower; not six-orbit exhaustiveness',
  'native_x6_claim':False,
}
print(json.dumps(results,ensure_ascii=False,indent=2))
