#!/usr/bin/env python3
"""Exact rational certificate for R238. Uses fractions only."""
from fractions import Fraction as F
import json
c=F(5,18)
slo,shi=F(39,100),F(41,100)
xlo,xhi=F(49,50),F(99,100)
rlo,rhi=F(9847337,10000000),F(9847338,10000000)
def t(s):return (1691*s-2615)/(2615*s-3539)
def q(s,j,x):
    a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t(s)]
    b=[F(13,60)]+[c*abs(F(1,2)-z) for z in a[1:]]
    return b[j]/(x-a[j])
def f4(s,x):return sum(q(s,j,x) for j in range(7) if j!=4)-1
def qstr(v):return str(v.numerator)+"/"+str(v.denominator)
def run():
    assert t(slo)<t(shi)<F(4,5)<xlo
    assert xlo<rlo<rhi<xhi
    q4max=q(slo,4,xlo)
    assert q4max==F(55,1062)
    margins={str(j):qstr(q(slo,j,xhi)-q4max) for j in (1,2,5,6)}
    assert all(q(slo,j,xhi)-q4max>0 for j in (1,2,5,6))
    lo=f4(slo,xlo)
    hi=f4(shi,xhi)
    lower_root=f4(shi,rlo)
    upper_root=f4(shi,rhi)
    assert lo==F(74402159402,14279825475603)>0
    assert hi==F(-316533456883,20880995759343)<0
    assert lower_root>0>upper_root
    assert rhi/F(594323,600000)==F(14771007,14858075)
    return {"status":"PASS","arithmetic":"exact Fraction",
            "s_interval":"(39/100,41/100)",
            "competing_block":"D_{-4}={0,1,2,3,5,6}",
            "q4_upper_rectangle":qstr(q4max),
            "other_q_lower_margins":margins,
            "f4_left_xlo":qstr(lo),"f4_right_xhi":qstr(hi),
            "optimal_uniform_secondary_radius_bracket":[qstr(rlo),qstr(rhi)],
            "f4_right_at_bracket_lower":qstr(lower_root),
            "f4_right_at_bracket_upper":qstr(upper_root),
            "sharper_relative_error_ratio_upper":qstr(rhi/F(594323,600000)),
            "continuum_proof":"secular monotonicity plus order comparisons and rank-one interlacing; see MD",
            "independent_review":"NOT_REVIEWED","native_BRC_execution":"NOT_EXECUTED"}
if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
