#!/usr/bin/env python3
"""PREFIX-689: exact rational consequence certificate for frozen 189-level BRC observer.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
Inputs are integer floors copied from PREFIX688_R6_RESULTS.json (pinned predecessor).
The 189-row recurrence and PREFIX-680 global third-derivative proof are inherited, not rerun.
"""
from fractions import Fraction as F
from json import dumps
A3=218571424275456
B3=69527880576
D=10**6
T=10**9
DATA=(
 dict(q0=12,l='0.0528706',u='0.0528708',delta='0.003',
      a0=656742,a1=-1671941380,a2=-66726857069,
      b1=128587655,b2=-989565080,
      fl=2028625,fr=-2009751,a_min='0.656',a_max='0.657',
      fp_min=-20220,fp_max=-20170),
 dict(q0=24,l='0.0530655',u='0.0530659',delta='0.022',
      a0=329445,a1=-1684945674,a2=-66650317279,
      b1=128394438,b2=-992151722,
      fl=8857119,fr=-7369717,a_min='0.329',a_max='0.330',
      fp_min=-40720,fp_max=-40420),
)
def floor_interval(m):return F(m,D),F(m+1,D)
def absmax(interval):return max(abs(interval[0]),abs(interval[1]))
def certify(d):
 q0=d['q0'];lo=F(d['l']);hi=F(d['u']);c=(lo+hi)/2;r=(hi-lo)/2;delta=F(d['delta'])
 a0=floor_interval(d['a0']);a1=floor_interval(d['a1']);a2=floor_interval(d['a2'])
 b1=floor_interval(d['b1']);b2=floor_interval(d['b2'])
 a_error=absmax(a1)*r+absmax(a2)*r*r/2+F(A3)*r**3/6
 amin,amax=F(d['a_min']),F(d['a_max'])
 assert amin<a0[0]-a_error and a0[1]+a_error<amax
 ap_error=absmax(a2)*r+F(A3)*r*r/2
 apmax=absmax(a1)+ap_error
 fp_center=q0*a1[0]-b1[1],q0*a1[1]-b1[0]
 fppmax=q0*absmax(a2)+absmax(b2)
 fp_error=fppmax*r+F(q0*A3+B3)*r*r/2
 fp_lower=fp_center[0]-fp_error-delta*apmax
 fp_upper=fp_center[1]+fp_error+delta*apmax
 assert F(d['fp_min'])<fp_lower and fp_upper<F(d['fp_max'])<0
 left_margin=F(d['fl'],T)-delta*amax
 right_margin=F(d['fr']+1,T)+delta*amax
 assert left_margin>0 and right_margin<0
 dz_lower=amin/F(-d['fp_min']);dz_upper=amax/F(-d['fp_max'])
 assert 0<dz_lower<dz_upper
 return {'q_center':q0,'q_interval':[str(F(q0)-delta),str(F(q0)+delta)],
   'z_window':[str(lo),str(hi)],'A_bounds':[str(amin),str(amax)],
   'Fprime_bounds':[d['fp_min'],d['fp_max']],
   'Fleft_guaranteed_gt':str(left_margin),'Fright_guaranteed_lt':str(right_margin),
   'slope_bounds':[str(dz_lower),str(dz_upper)],
   'exact_A_interval':[str(a0[0]-a_error),str(a0[1]+a_error)],
   'exact_Fprime_interval':[str(fp_lower),str(fp_upper)],
   'status':'EXACT_FRACTION_CERTIFIED'}
if __name__=='__main__':
 out={'result':'ALL_CHECKS_PASS PREFIX689-R6',
   'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
   'source':'PREFIX688_R6_RESULTS.json and PREFIX680_R6_RESULTS.json',
   'scope':'exact rational implication; inherited model certificates',
   'status':'AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED',
   'bands':[certify(d) for d in DATA]}
 print(dumps(out,ensure_ascii=False,indent=2))
