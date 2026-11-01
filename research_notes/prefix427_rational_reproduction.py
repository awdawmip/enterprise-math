#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt
B=F(1,10**6); GRID=10**20
def sq(x):
 z=isqrt(x.numerator*GRID**2//x.denominator)
 lo=F(z,GRID); hi=lo if lo*lo==x else F(z+1,GRID)
 assert lo*lo<=x<=hi*hi
 return lo,hi
JL=45-F(49,2)*B; JH=45+4*B
HL=sq(JL)[0]; HH=sq(JH)[1]
GL=F(372); GH=GL+427*B
DL=GL/(16000*HH); DH=GH/(16000*HL)
CL=F(1024000)*JL*HL/GH**2
CH=F(1024000)*JH*HH/GL**2
TL=1287-705*B; TH=1287+61*B
ML=TL/(8000*HH); MH=TH/(8000*HL)
checks=[
 ('J range',44<JL<JH<46),('H range',F(67,10)<HL<HH<7),
 ('D range',F(34,10000)<DL<DH<F(35,10000)),
 ('M positive',0<ML<MH<F(1,25)),
 ('sharp C enclosure',2233<CL<CH<2235),
 ('radial bound',500*(F(1,26784)+F(1,26800))<F(1,25)),
 ('quadratic lower',26800*F(197,700)**2>2100),
 ('negative corner slope',5-2*(1+B)/F(99,100)>F(29,10)),
 ('negative square root',1-B-B**2>F(99,100)**2),
 ('coordinate lipschitz',F(101,100)/(F(99,100)*F(29,10))<F(36,100)),
 ('joint observer lipschitz',(12+F(1,20)*F(101,100))/(F(99,100)*F(29,10))<5),
 ('normalized source',8/F(67,10)<F(6,5)),
 ('phase gap',82+F(5,10**6)-F(8,1000)*F(6,10)+F(32,10**6)<82-F(4,1000)),
 ('small delta',CH*F(1,10**12)<F(1,100000)),
 ('joint h margin',F(1,50)-F(1,10**6)>F(1,100))]
for name,ok in checks:
 assert ok,name
 print('PASS',name)
print('PASS_PREFIX427_RATIONAL_REPRODUCTION',len(checks))
print('Coefficient interval',float(CL),float(CH))
