#!/usr/bin/env python3
"""PREFIX-627 exact-bound certificate, conditional on PREFIX-626's proved edge gradient."""
import json
from pathlib import Path
from fractions import Fraction as Q

M = 189
A = sum(n for n in range(M))
B = sum(2*n*(n-1) for n in range(M))
D = sum(2*n*(n-1)*(n+1) for n in range(M))
W2 = 2*D + 2*A*A + 4*M*B
L = W2 + Q(B,2)
delta = Q(1, 2**24)
margin = Q(332)-L*delta
checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

for condition in (
    M == 189, A == 17766, B == 4429656, D == 631225980,
    W2 == 5242533408, L == 5244748236,
    L*delta < 313, margin > 19
):
    check(condition)
for q in (2,12,24,48):
    check(q*q*W2+q*B <= q*q*L)
    check(332*q*q-(q*q*W2+q*B)*delta>19*q*q)

result = {
    "schema":"PREFIX627_R6_UNIFORM_INWARD_STRIP_CERTIFICATE_V1",
    "date":"2026-11-09",
    "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "model":"frozen signed-direction d=2, q>=2, beta=1/40, width=1/4",
    "dependency":"PREFIX-626 exact edge-gradient bound, PREFIX-621 finite survivor horizon",
    "M":M,"A":A,"B":B,"D":D,"W_second_derivative_bound":W2,
    "variance_Hessian_bound_divided_by_q_squared":int(L),
    "strip_width":str(delta),"strict_margin_divided_by_q_squared":str(margin),
    "conclusion":"For p2 in [37/256,39/256], 0<=p1<=2^-24, q>=2: partial1 Var(T_q)<-19q^2; for p1>0, V_q(p1,p2)<V_q(0,p2)-19q^2 p1.",
    "verification":"ALL_CHECKS_PASS","assertions_executed":checks,
    "scope":"New bound exact arithmetic; prior exact survivor certificate and original native graph not rerun.",
    "admission":"AUTHOR_PROVED / EXACT_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
out=Path(__file__).with_name("PREFIX627_R6_RESULTS.json")
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS",checks)
print("L",L,"h",delta,"strict_margin",margin)
