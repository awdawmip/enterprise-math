#!/usr/bin/env python3
"""PREFIX-694: exact rational BRC observer crossover convexity implication.
This is an implication checker for published PREFIX-693 sixth-order jets,
NOT a new full 189-row survivor replay.
"""
import json
from fractions import Fraction as F
from math import factorial

T = F(647, 5000000)
# Conservative A[5] envelope covers the published paper/checker vs JSON discrepancy.
jets = {
 'A': [44000296,-168056589514,-6667624082229,39352687679231,3189837819999830,-36266294695911140],
 'B': [789752024,12845959424,-99127959112,-1326952329685,-14895243921676,-1960958310350017]
}
m6 = {'A':201273663850076722544640,'B':17896441402901698560}

def abs_second_bound(name):
    f = jets[name]
    ub = F(max(abs(f[2]),abs(f[2]+1)),10**8)
    for j in range(3,6):
        ub += F(max(abs(f[j]),abs(f[j]+1)),10**8)*T**(j-2)/factorial(j-2)
    ub += F(m6[name])*T**4/factorial(4)
    return ub

ba, bb = abs_second_bound('A'),abs_second_bound('B')
assert ba < 2500000 and bb < 1500
amin,amax = F(329,1000),F(657,1000)
bmin,bmax = F(785,100),F(795,100)
nmin = 2*bmin*1611**2-bmax*amax*2500000-1500*amax**2
nmax = 1500*amax**2+bmax*amax*2500000+2*129*amax*1751+2*bmax*1751**2
assert nmin > 0 and nmin/amax**3 > 90000000
assert nmax/amin**3 < 1800000000
qpmin = (128*amin+bmin*1611)/amax**2
qpmax = (129*amax+bmax*1751)/amin**2
assert qpmin > 29000 and qpmax < 130000
assert F(90000000,130000**3)>F(4,10**8)
assert F(1800000000,29000**3)<F(8,10**5)
# Previous certified q=12,18,24 brackets (all endpoint inequalities strict).
z12_upper=F(528708,10**7)
z18_lower=F(53000730,10**9)
z24_upper=F(530659,10**7)
midgap=z18_lower-(z12_upper+z24_upper)/2
assert midgap>=F(3238,10**8)

result={
 'title':'PREFIX-694-R6',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'source':'PREFIX-693 exact jets and sixth-derivative envelope; PREFIX-692 A,B positivity; PREFIX-688/691 root brackets',
 'interval':'[0.0528706,0.0530659]',
 'certified':{'A_second_abs_lt':'2500000','B_second_abs_lt':'1500',
   'Q_prime':'29000 < Qprime < 130000',
   'Q_second':'90000000 < Qsecond < 1800000000',
   'inverse_second':'-8/100000 < zsecond < -4/100000000'},
 'exact_rational_details':{'A_second_upper':str(ba),
   'B_second_upper':str(bb),'Q_numerator_lower':str(nmin),
   'Q_numerator_upper':str(nmax),'Q_prime_lower':str(qpmin),
   'Q_prime_upper':str(qpmax),'q18_midpoint_gap_lower':str(midgap)},
 'source_reconciliation':{'A_5_floor_paper_checker':-36266294695911132,
   'A_5_floor_results_json':-36266294695911140,
   'method':'Broader of both published signed fifth-jet magnitudes; reconcile upstream exact replay separately.'},
 'scope':'Inherited frozen model exact jets and global sixth-order envelope; implication check only',
 'status':'AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED',
 'verification':'ALL_CHECKS_PASS PREFIX694-R6'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
