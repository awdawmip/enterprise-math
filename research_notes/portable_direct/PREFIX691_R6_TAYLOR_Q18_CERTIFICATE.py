#!/usr/bin/env python3
"""PREFIX-691 exact rational Taylor implication checker for frozen PREFIX-680 center jets."""
from fractions import Fraction as Q
from json import dumps
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
D=10**8
AJ=(44000296,-168056589514,-6667624082229)
BJ=(789752024,12845959424,-99127959112)
A3=218571424275456
B3=69527880576
B=Q(53,1000)
TL,TU=Q(730,10**9),Q(755,10**9)
QL,QH=Q('17.9998'),Q('18.0002')
def pjet(j):return Q(j,D),Q(j+1,D)
def values(jet,M,t):
    outlo=outhi=Q(0)
    for k,v in enumerate(jet):
        lo,hi=pjet(v)
        term=t**k/(1 if k<2 else 2)
        outlo+=lo*term;outhi+=hi*term
    err=Q(M)*t**3/6
    return outlo-err,outhi+err
def fs(q,t):
    aa=values(AJ,A3,t);bb=values(BJ,B3,t)
    return q*aa[0]-bb[1],q*aa[1]-bb[0]
def deriv(jet,M):
    l=Q(jet[1],D)+Q(jet[2],D)*TU-Q(M)*TU*TU/2
    h=Q(jet[1]+1,D)+Q(jet[2]+1,D)*TL+Q(M)*TU*TU/2
    return l,h
AL,AU=values(AJ,A3,TL),values(AJ,A3,TU)
Ap=deriv(AJ,A3);Bp=deriv(BJ,B3)
assert Ap[1]<0
abox=(AU[0],AL[1])
fp=(QH*Ap[0]-Bp[1],QL*Ap[1]-Bp[0])
fl=fs(18,TL);fr=fs(18,TU)
FL=(fl[0]-(18-QL)*abox[1],fl[1]+(QH-18)*abox[1])
FR=(fr[0]-(18-QL)*abox[1],fr[1]+(QH-18)*abox[1])
assert FL[0]>0 and FR[1]<0
assert Q('0.4386')<abox[0] and abox[1]<Q('0.4389')
assert Q(-32000)<fp[0] and fp[1]<Q(-29000)
sl=(abox[0]/(-fp[0]),abox[1]/(-fp[1]))
assert Q(139,10**7)<sl[0] and sl[1]<Q(15,10**6)
out={
  'result':'ALL_CHECKS_PASS PREFIX691-R6',
  'science_pin':PIN,
  'source':'PREFIX680_R6_RESULTS.json@2c91711f60aa74d93880780929f532da24140ec0',
  'center':str(B),'q_band':[str(QL),str(QH)],
  'z_bracket':[str(B+TL),str(B+TU)],
  'F18_left_bounds':[str(x) for x in fl],
  'F18_right_bounds':[str(x) for x in fr],
  'full_q_band_left_bounds':[str(x) for x in FL],
  'full_q_band_right_bounds':[str(x) for x in FR],
  'A_bounds':[str(x) for x in abox],
  'A_prime_bounds':[str(x) for x in Ap],
  'B_prime_bounds':[str(x) for x in Bp],
  'Fprime_bounds':[str(x) for x in fp],
  'root_derivative_bounds':[str(x) for x in sl],
  'center_jet_floor_denominator':D,
  'A_jet_floors':AJ,'B_jet_floors':BJ,
  'global_third_derivative_limits':{'A3':A3,'B3':B3},
  'method':'Exact integer / Fraction Taylor interval; inherited exact model floors and third derivative bounds',
  'status':'AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED',
  'crossing_is_unique_within_bracket':True
}
print(dumps(out,ensure_ascii=False,indent=2))
