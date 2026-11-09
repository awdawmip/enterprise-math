#!/usr/bin/env python3
"""PREFIX-652 exact rational interval witness from PREFIX-645 center cumulants.
Full-precision Fraction interval computation; integer-isqrt enclosing at 1e18.
No float is used in any mathematical assertion.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

S=10**18
checks=[]
def test(label,truth):
    assert truth,label
    checks.append(label)

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo)
        self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,other):
        b=iv(other);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-iv(other)
    def __rsub__(self,other):return iv(other)+-self
    def __mul__(self,other):
        b=iv(other)
        p=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def inverse(self):
        assert self.lo*self.hi>0
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,other):return self*iv(other).inverse()
    def __rtruediv__(self,other):return iv(other)*self.inverse()
    def __pow__(self,n):
        assert type(n)==int and n>=0
        ans=I(1)
        for _ in range(n):ans=ans*self
        return ans
    def sqrt(self):
        assert self.lo>0
        def floor_root(x):return isqrt(x.numerator*S*S//x.denominator)
        return I(F(floor_root(self.lo),S),F(floor_root(self.hi)+1,S))

def iv(x):return x if isinstance(x,I) else I(x)
a=I(F(54327837,500000),F(4346227,40000))
b=I(F(42102733,125000),F(67364373,200000))
c=I(F(-1209500201,1000000),F(-6047501,5000))
d=I(F(25187126503,500000),F(50374253007,1000000))
test("a_positive",a.lo>0)
test("b_positive",b.lo>0)
test("c_negative",c.hi<0)
test("d_positive",d.lo>0)
def g1(t):
    B=b-a*t
    assert B.lo>0
    return (c-3*b*t+a*t*t)/(B*B.sqrt())
def g2(t):
    B=b-a*t
    assert B.lo>0
    return (d-6*c*t+7*b*t*t-a*t*t*t)/(B**2)
display={}
for name,fn in (("skewness",g1),("excess_kurtosis",g2)):
    at={str(q):fn(F(1,q)) for q in (12,24,48)}
    at["infinity"]=fn(F(0))
    R=at["12"]/3-2*at["24"]+F(8,3)*at["48"]
    e=R-at["infinity"]
    display[name]={
        "gamma_48":[float(at["48"].lo),float(at["48"].hi)],
        "extrapolation":[float(R.lo),float(R.hi)],
        "signed_error":[float(e.lo),float(e.hi)]}
    if name=="skewness":
        test("gamma48_skew_lo",at["48"].lo>F(-201083135,10**9))
        test("gamma48_skew_hi",at["48"].hi<F(-201083133,10**9))
        test("skew_error_lo",e.lo>-F(1,300000))
        test("skew_error_hi",e.hi<-F(1,400000))
        test("skew_651_sign",e.hi<0)
        test("skew_651_magnitude",e.lo>-F(1,276480))
    else:
        test("gamma48_kurt_lo",at["48"].lo>F(451414521,10**9))
        test("gamma48_kurt_hi",at["48"].hi<F(451414524,10**9))
        test("kurt_error_lo",e.lo>F(1,160000))
        test("kurt_error_hi",e.hi<F(1,120000))
        test("kurt_651_sign",e.lo>0)
        test("kurt_651_magnitude",e.hi<F(11,829440))
assert len(checks)==16
payload={
  "record":"PREFIX-652-R6",
  "status":"AUTHOR_DERIVED_EXACT_RATIONAL_INTERVAL_CHECKED_UNREVIEWED_NOT_ADMITTED",
  "frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
  "center":{"p":"1/6","z":"19/128"},
  "source":"PREFIX-645 exact certified cumulant rational six-decimal intervals",
  "interval_witnesses":{
    "gamma1_48":"-201083135/10^9 < gamma1(48) < -201083133/10^9",
    "gamma2_48":"451414521/10^9 < gamma2(48) < 451414524/10^9",
    "skew_error":"-1/300000 < R1-gamma1_inf < -1/400000",
    "kurt_error":"1/160000 < R2-gamma2_inf < 1/120000"},
  "exact_checks_passed":len(checks),"check_names":checks,
  "display_only_approximate_ranges":display,
  "model_189_layers_recomputed":False,"native_96_port_recomputed":False}
Path(__file__).with_name("PREFIX652_R6_RESULTS.json").write_text(
    json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS",len(checks))
for k,v in display.items():print(k,v)
