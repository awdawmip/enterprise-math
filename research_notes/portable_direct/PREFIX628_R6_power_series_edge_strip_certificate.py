#!/usr/bin/env python3
"""PREFIX-628: exact survivor-word Taylor majorants, BRC 1024x variance strip.
Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run next to PREFIX621_R6_stochastic_tail_certificate.py. Python stdlib only.
"""
import contextlib, io, json, hashlib
from decimal import Decimal, localcontext
from math import comb
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX621_R6_stochastic_tail_certificate as source

N=189
assert source.first==25 and source.surv[N]==0 and len(source.rows)==N+1
den=1<<14
H=den**(N-2)
R0_num=0
R1_num=0
endpoint_checks=0
for n,row in enumerate(source.rows[:N]):
    c=[0]*(n+1)
    for k,A in row.items():
        for j in range(k,n+1):
            c[j]+=(-1 if (j-k)%2 else 1)*A*comb(n-k,j-k)
    assert c[0]==row.get(0,0)
    assert sum(c)==row.get(n,0)
    endpoint_checks+=2
    for j in range(2,n+1):
        v=j*abs(c[j])*den**((N-2)-(j-1))
        R0_num+=v
        R1_num+=(n+1)*v
assert endpoint_checks==378
assert R0_num>0 and 8*R0_num<7*H
assert R1_num>0 and R1_num<30*H
# Moment witnesses: mu(0,a)>87, U(0,b)>4, J(0,a)<182.
# R0<7/8, R1<30 => mu>87, U>25/8, J<212 everywhere in strip.
# dW=2J-2muU < -479/4 < -119, dVar_q=q^2*dW-q*U < -119*q^2.
assert 4*(2*212)-2*87*25 < -119*4
with localcontext() as ctx:
    ctx.prec=35
    r0=str(Decimal(R0_num)/Decimal(H))
    r1=str(Decimal(R1_num)/Decimal(H))
output={
 "schema":"PREFIX628_R6_POWER_SERIES_STRIP_V1",
 "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "dependency":"PREFIX621 exact 189-layer recurrence; PREFIX624 shape lemma; PREFIX626 exact endpoint witnesses",
 "p2_interval":["37/256","39/256"],"h":"1/16384","q":"all real q>=2",
 "integer_denominator":"2^(14*187)",
 "R0_decimal_display":r0,"R1_decimal_display":r1,
 "R0_exact_bound":"R0 < 7/8","R1_exact_bound":"R1 < 30",
 "R0_numerator_digits":len(str(R0_num)),
 "R1_numerator_digits":len(str(R1_num)),
 "R0_numerator_sha256":hashlib.sha256(str(R0_num).encode()).hexdigest(),
 "R1_numerator_sha256":hashlib.sha256(str(R1_num).encode()).hexdigest(),
 "endpoint_checks":endpoint_checks,
 "theorem":"partial_p1 Var(T_q) < -119*q^2 on rectangle; 1024x wider than PREFIX627",
 "verification":"ALL_CHECKS_PASS",
 "status":"AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
Path(__file__).with_name("PREFIX628_R6_RESULTS.json").write_text(
    json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS")
print("R0=",r0,"< 7/8")
print("R1=",r1,"< 30")
