#!/usr/bin/env python3
"""PREFIX-692-R6: exact rational verification of inherited BRC bridge certificates."""
from fractions import Fraction as Q
from json import dumps
PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
L,R=Q("0.0528706"),Q("0.0530659")
QMIN,QMAX=Q(63055771,5256000),Q(660614143,27500000)
D=10**8
B0=(789752024,789752025)
B1=(12845959424,12845959425)
B2=(-99127959112,-99127959111)
B3=69527880576
T=max(abs(L-Q("0.053")),abs(R-Q("0.053")))
assert T==Q(647,5000000)
E1=Q(max(map(abs,B1)),D)*T
E2=Q(max(map(abs,B2)),D)*T*T/2
E3=Q(B3)*T**3/6
LOW=Q(B0[0],D)-E1-E2-E3
HIGH=Q(B0[1],D)+E1+E2+E3
assert LOW==Q(4909863349354430849559,625000000000000000000)
assert HIGH==Q(4962036956895569150441,625000000000000000000)
assert Q("7.85")<LOW<HIGH<Q("7.95")
F12L=Q(2028625,10**9);F24R=-Q(7369716,10**9)
AL=(Q(".656"),Q(".657"));AR=(Q(".329"),Q(".330"))
def left(q):return F12L+(q-12)*(AL[1] if q<=12 else AL[0])
def right(q):return F24R+(q-24)*(AR[0] if q<=24 else AR[1])
assert QMIN==12-F12L/AL[1] and QMAX==24-F24R/AR[1]
assert 0<QMIN<12<18<24<QMAX<Q("24.023")
MARGINS={}
for q in (QMIN,Q(12),Q(18),Q(24),QMAX):
    assert left(q)>=0 and right(q)<=0
    MARGINS[str(q)]=[str(left(q)),str(right(q))]
assert Q("7.85")/QMAX==Q(215875000,660614143)>Q(".326")
out={"result":"ALL_CHECKS_PASS PREFIX692-R6","frozen_pin":PIN,
"dependencies":["PREFIX680 center-jet and third-derivative certificate @2c91711f60aa74d93880780929f532da24140ec0",
"PREFIX690 endpoint-sign envelope @e1394a13ec0627a579db9414242a3633b773304e"],
"bridge":[str(L),str(R)],"q_interval":[str(QMIN),str(QMAX)],
"max_center_distance":str(T),"B_lower_exact":str(LOW),"B_upper_exact":str(HIGH),
"all_root_A_lower_strict":str(Q("7.85")/QMAX),"endpoint_margins":MARGINS,
"proved_analytically":["nested nonnegative-sign sets","strict increase of least and greatest roots",
"least-root left continuity","greatest-root right continuity"],
"scope":"exact inherited-certificate implications; no new 189-state recurrence",
"status":"AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED"}
print(dumps(out,indent=2))
