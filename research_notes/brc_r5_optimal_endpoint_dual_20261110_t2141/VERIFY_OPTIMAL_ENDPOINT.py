#!/usr/bin/env python3
"""Exact rational verifier: 2D bridge certificate and optimal terminal v."""
from fractions import Fraction as F

DATA={
"00":(F(570031933801575355927,3025154085489542635200),F(2003,2025)),
"33":(F(9386098186912477,52340117054042400),F(335783,32400)),
"43":(F(5506094603075,179341701138288),F(281443,43200)),
"45":(F(95758167010,1245428480127),F(26371,6000)),
"65":(F(239395417525,4981713920508),F(509,416)),
"66":(F(16939155808730941927,3025154085489542635200),F(1017037,324000)),
"ell":(F(1196977087625,89670850569144),F(13493,9936)),
}
V0,V1=F(1,10),F(13,40)
S0,S1=F(7933,36000),F(3761,12000)
def S(v): return S0+F(67,162)*(v-V0)
def gamma(k,v):
    s=S(v)
    return {"00":s,"33":1-2*s,"43":F(0),"45":F(0),"65":F(0),"66":s,"ell":F(0)}[k]
def r(k,t,v):
    beta,eta=DATA[k]
    return ((1-t)*beta+t*gamma(k,v))/eta
A=DATA["66"][0]/DATA["66"][1]
Bmin=S0/DATA["66"][1]
Bmax=S1/DATA["66"][1]
C=DATA["43"][0]/DATA["43"][1]
to=(C-A)/(Bmax-A+C)
ro=C*(1-to)
tu=(C-A)/(Bmin-A+C)
ru=C*(1-tu)
assert S(V0)==S0 and S(V1)==S1
assert A==F(254087337130964128905,142439520168704998753514)
assert Bmin==F(71397,1017037)
assert Bmax==F(101547,1017037)
assert C==F(550609460307500,116839042577461087)
assert to==F(27506071400619459894935030258545,965242855541993161664216604137419)
assert ro==F(4419128514205873438322431365000,965242855541993161664216604137419)
assert 0<to<tu<1 and A<C<Bmin<Bmax
# 20 exact corner inequalities. Each difference is multi-affine.
for k in ("00","33","45","65","ell"):
    for t in (F(0),F(1)):
        for v in (V0,V1):
            assert r(k,t,v)>=r("43",t,v),(k,t,v)
# Test complete seven-envelope identity at rational interior sentinels.
for t in (F(0),F(1,100),to,F(1,25),tu,F(1,2),F(1)):
    for v in (V0,F(7,40),V1):
        assert min(r(k,t,v) for k in DATA)==min(r("66",t,v),r("43",t,v))
def vreq(t):
    beta,eta=DATA["66"]
    return V0+F(162,67)*(((eta*C-beta)*(1-t)/t)-S0)
assert vreq(to)==V1 and vreq(tu)==V0
mid=(to+tu)/2
vm=vreq(mid)
assert V0<vm<V1 and r("66",mid,vm)==r("43",mid,vm)
assert r("66",mid,(V0+vm)/2)<r("43",mid,V0)
assert r("66",mid,(V1+vm)/2)>r("43",mid,V1)
assert ro>ru and ro/A>F(5,2)
print("FROZEN_GLOBAL a01383f825ef9d43b4b754254303298c64041568")
print("FROZEN_EM 86149263e38c22292c9def1e0f69092efa1be77e")
print("RANGE_V",V0,V1,"S",S0,S1)
print("A",A,"B_MIN",Bmin,"B_MAX",Bmax,"C",C)
print("T_OPT",to,"approx",float(to))
print("R_OPT",ro,"approx",float(ro))
print("T_UNIFORM",tu,"approx",float(tu))
print("R_UNIFORM",ru,"approx",float(ru))
print("OPT_OVER_UNIFORM",ro/ru,"approx",float(ro/ru))
print("OPT_OVER_P7_START",ro/A,"approx",float(ro/A))
print("ALL_V_ENVELOPE min{((1-t)*beta66+t*S(v))/eta66,C*(1-t)}")
print("VALIDATION twenty corner inequalities, exact extrema and threshold")
print("INHERITED_PREDECESSOR 30-column duals, polygon minima and lift not reexecuted")
print("PASS_EXACT_TWO_PARAMETER_ENDPOINT_OPTIMAL_SEVEN_DUAL")
