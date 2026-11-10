#!/usr/bin/env python3
"""Exact Fraction slot-band certificate for PREFIX-678-R6.
Frozen center jets come from d344451396a9bace91a9cbcdb14475c6641a9223.
"""
from fractions import Fraction as Q
import json

Alo,Ahi=Q(11,25),Q(441,1000)
Blo,Bhi=Q(789,100),Q(79,10)
A2,B2=281945567232,133031808
R0=Q(332788,25)
rho=Q(1,330000000)
dA=1681*rho+Q(A2,2)*rho**2
dB=129*rho+Q(B2,2)*rho**2
Am,Ax=Alo-dA,Ahi+dA
Bm,Bx=Blo-dB,Bhi+dB
L=B2*Ax+A2*Bx
Rm=R0-L*rho
assert Am>Q(439,1000)>0
assert Ax<Q(442,1000)
assert Bm>0 and Rm>6500
assert Q(6500)/Q(442,1000)**2>33000
assert Bm>Q(1789,100)*Ax and Bx<Q(449,25)*Am
cl,cu=Q(17948788665,10**9),Q(17948788666,10**9)
ql,qu=Q(1794869,100000),Q(1794888,100000)
assert cu-33000*rho<ql<qu<cl+33000*rho
old_width=Q(17948794,10**6)-Q(17948783,10**6)
width=qu-ql
assert width/old_width==Q(190,11)
result={'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'predecessor_jet':'d344451396a9bace91a9cbcdb14475c6641a9223',
'preceding_result':'b1cda0db8097c4addac67899ecfe32dc7aa1446e',
'center':'53/1000','radius':str(rho),
'R_lower':str(Rm),'R_floor_strict':6500,'q0_prime_floor_strict':33000,
'fixed_q_band':['1794869/100000','1794888/100000'],
'width_gain_exact':str(width/old_width),
'A2':A2,'B2':B2,
'check':'ALL_CHECKS_PASS',
'status':'AUTHOR_DERIVED_EXACT_FRACTION_IMPLICATION_CHECKED_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(result,indent=2))
