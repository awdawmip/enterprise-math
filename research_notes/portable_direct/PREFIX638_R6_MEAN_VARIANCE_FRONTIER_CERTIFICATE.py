#!/usr/bin/env python3
"""Exact 21-check rational implication certificate for PREFIX-638.
Inputs m,M and central envelopes are frozen, cited PREFIX-635/636 premises;
this script does not rerun their 189-layer certificate or the native graph.
"""
from fractions import Fraction as Q
import json

t0,t1=Q(1,24),Q(1,12)
m,M=Q(299**2,51000),Q(311**2,22000)
mc,Mc=Q(9,5),Q(961,230)
i=(t1*t1-t0*t0)/2
checks=0
def check(name,x):
    global checks
    assert x,name
    checks+=1

check("range",0<t0<t1)
check("integral",i==Q(1,384))
check("m positive",m>0)
check("m less than M",m<M)
check("mc positive",mc>0)
check("mc less than Mc",mc<Mc)
check("mc stronger than m",mc>m)
check("Mc stronger than M",Mc<M)
check("strip inverse lower",1/M==Q(22000,96721))
check("strip inverse upper",1/m==Q(51000,89401))
check("centre inverse lower",1/Mc==Q(230,961))
check("centre inverse upper",1/mc==Q(5,9))
check("strip variance lower",m*i==Q(89401,19584000))
check("strip variance upper",M*i==Q(96721,8448000))
check("centre variance lower",mc*i==Q(3,640))
check("centre variance upper",Mc*i==Q(961,88320))
check("strip variance strict",m*i<M*i)
check("centre variance strict",mc*i<Mc*i)
check("mean lower",m*(t1-t0)==Q(89401,1224000))
check("mean upper",M*(t1-t0)==Q(96721,528000))
check("variance positive",m*i>0)
def rat(v):return {"numerator":v.numerator,"denominator":v.denominator,"approx":float(v)}
out={"research":"PREFIX-638-R6","frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
"scope":{"p1":"[4/25,161/1000]","p2":"[19/128-2^-33,19/128+2^-33]","t":"[1/24,1/12]"},
"dependency":"Exact analytic premises PREFIX-635 and PREFIX-636; this is an implication checker",
"curvature_strip":[rat(1/M),rat(1/m)],"curvature_centre":[rat(1/Mc),rat(1/mc)],
"variance_gap_strip":[rat(m*i),rat(M*i)],"variance_gap_centre":[rat(mc*i),rat(Mc*i)],
"checks":checks,"result":"ALL_CHECKS_PASS","review":"UNREVIEWED / NOT_ADMITTED"}
with open("PREFIX638_R6_RESULTS.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write("\n")
print("ALL_CHECKS_PASS",checks)
