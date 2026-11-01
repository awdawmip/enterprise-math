#!/usr/bin/env python3
"""PREFIX-429: exact-rational sufficient inequalities for a uniform full-source theorem.
The analytic proof linking these inequalities is in the companion Markdown note.
No floating-point quantity enters any of the  assertions.
"""
from fractions import Fraction as F

B = F(1,10**6)
RHO = F(1,1000)
HLO = F(67082,10000)
HHI = F(670821,100000)
HPOS = F(608277,100000)
DLO = F(34658,10**7)
DHI = F(34660,10**7)
MLO = F(239817,10**7)
MHI = F(239819,10**7)
TMAX = F(2491,10000)
LMID = F(173,100)
LMAX = F(2199,1250)
ETA_LOW = F(1956,100000) # 0.01956
ETA_MID = F(21,1000)
ETA_SAT_HI = F(239864,10**7)
assert ETA_LOW == F(489,25000)
checks=[]

def check(name, condition):
    if not condition: raise AssertionError(name)
    checks.append(name)

# Enclose J and the radicals for all epsilon in [0,B].
check('h_lower_square', HLO*HLO < 45-F(49,2)*B)
check('h_upper_square', HHI*HHI > 45+4*B)
check('D_lower', DLO < F(372)/(16000*HHI))
check('D_upper', (F(372)+427*B)/(16000*HLO) < DHI)
check('M_lower', MLO < (F(1287)-705*B)/(8000*HHI))
check('M_upper', (F(1287)+61*B)/(8000*HLO) < MHI)
check('sat_upper', F(709,64)*B+MHI-F(53,8)*B < ETA_SAT_HI)
check('sat_above_eta_low', MLO-F(53,8)*B > ETA_LOW)
check('quadratic_discriminant_positive', 2*MLO > ETA_SAT_HI-ETA_LOW)
check('delta_max_at_tmax', ETA_SAT_HI-ETA_LOW < (2*DLO*TMAX+2*MLO*TMAX*TMAX)/(1+TMAX*TMAX))
check('delta_mid_at_t=1/5', ETA_SAT_HI-ETA_MID < (2*DLO*F(1,5)+2*MLO*F(1,25))/(1+F(1,25)))
check('tmax_below_1', TMAX<1)
check('lambda_enclosure', 16*HHI*RHO*TMAX/(DLO*(1-TMAX*TMAX)+2*MLO*TMAX) < LMAX)
check('positive_radial_quadratic', 16-F(53,8)*LMAX > 0)

# Full negative-phase baseline rectangle: |a|<=B, 1-B <= q <= 1+B,
# |q_s|<=B/(2(1-B))<B and 0<q_r<.501.
check('q_lower', (1-B)**2 < 1-B-B*B)
check('q_upper', (1+B)**2 > 1+B)
check('q_s_bound', B/(2*(1-B))<B)
check('q_r_bound', (1+B)/(2*(1-B))<F(501,1000))
check('J_r_negative', -5+2*(1+B)/(1-B)<-F(299,100))
check('J_s_positive', F(39,2)-2*B/(1-B)>F(1949,100))
check('J_neg_gt_6p7_sq', 45-F(57,2)*B>F(67,10)**2)
check('pk_negative_norm', (F(31,4)**2+F(93,4)**2)<25**2)
check('pk_x_abs_bound', F(61,8)+23*B<F(31,4))
check('pk_y_abs_bound', 23+23*B<F(93,4))
check('R_above_radial_threshold', 8*F(67,10)-LMAX*25>2*16*RHO)
check('pf_r_derivative', 4*(5+10*F(501,1000))<72)
check('pf_s_derivative', 4*(5+10*B)<24)
check('pk_r_derivative', (184+368*F(501,1000))/16<36)
check('pk_s_derivative', (184+368*B)/16<12)
check('m_r_strict_negative', -F(299,100)+RHO*(72+36*LMAX)<0)
check('m_s_low_lambda', F(1949,100)-LMID*F(709,64)-RHO*(24+12*LMID)>0)

# Sharper R_s on lambda in [1.73, 1.7592].  For q_s in [-B,B],
# p_lambda=(px,py), (p_lambda)_s=(psx,psy): px,psx,psy>0, py<0.
pfx_lo,pfx_hi=24-40*B,24+40*B
pfy_lo,pfy_hi=-48-40*B,-48+40*B
pkx_lo,pkx_hi=F(61,8)-23*B,F(61,8)+23*B
pky_lo,pky_hi=-23-23*B,-23+23*B
pxlo=pfx_lo-LMAX*pkx_hi
pxhi=pfx_hi-LMID*pkx_lo
pylo=pfy_lo-LMID*pky_hi
pyhi=pfy_hi-LMAX*pky_lo
pfsx_lo,pfsx_hi=14-12*B,14+12*B
pfsy_lo,pfsy_hi=-6-28*B,-6+28*B
pksx_lo,pksx_hi=F(245,32)-F(123,16)*B,F(245,32)+F(123,16)*B
pksy_lo,pksy_hi=-F(123,32)-F(245,16)*B,-F(123,32)+F(245,16)*B
psxlo=pfsx_lo-LMAX*pksx_hi
psxhi=pfsx_hi-LMID*pksx_lo
psylo=pfsy_lo-LMID*pksy_hi
psyhi=pfsy_hi-LMAX*pksy_lo
check('high_lambda_px_positive', pxlo>10)
check('high_lambda_py_negative', pyhi<0)
check('high_lambda_psx_positive', psxlo>0)
check('high_lambda_psy_positive', psylo>0)
# Since py<0 and psy>0, all products have the indicated monotonicity.
dot_up=pxhi*psxhi+pyhi*psylo
check('high_lambda_R_s_numerator_upper_positive', dot_up>0)
rs_up=dot_up/pxlo
check('high_lambda_R_s_less_than_1', rs_up<1)
check('high_lambda_m_s_positive', F(39,2)-2*B/(1-B)-LMAX*F(709,64)-RHO>0)

# Positive phase: independent of eta when the fifth observer is inactive.
check('positive_h_upper', HPOS**2>37+F(57,2)*B)
check('positive_F_global_bound', (HPOS+4*RHO)**2 < F(37049,1000))
# lambda_p=3/2 gives a full-source fifth-observer upper bound on the small eta window.
check('positive_pk_linear_radius', (F(27,2)+F(149,2)*B)**2 +(F(55,16)+F(149,2)*B)**2<14**2)
pos_small = 37+F(57,2)*B+F(3,2)*(ETA_MID+12*B)+(16-F(53,8)*F(3,2))*B+14*RHO
check('positive_F_low_eta_bound', pos_small < F(37046,1000))
# Witness at the negative global minimizer; F decreases with eta since t decreases.
neg_small=(HHI-4*RHO)**2+16*RHO*HHI*TMAX*TMAX/(1+TMAX*TMAX)
neg_large=(HHI-4*RHO)**2+16*RHO*HHI*F(1,25)/(1+F(1,25))
check('negative_F_low_eta_bound', neg_small<F(44953,1000))
check('negative_F_high_eta_bound', neg_large<F(44951,1000))
check('phase_witness_low', F(44953,1000)+F(37046,1000)<82)
check('phase_witness_high', F(44951,1000)+F(37049,1000)<=82)
check('first_observer_slack', 2*RHO+RHO**2 < ETA_LOW)
check('negative_F_gt_41', (F(67,10)-4*RHO)**2>41)
check('positive_F_lt_41', (HPOS+4*RHO)**2<41)

print('PASS_PREFIX429_UNIFORM_FULL_SOURCE_FROM_ETA_0p01956_TO_PLATEAU')
print('EXACT_RATIONAL_ASSERTIONS',len(checks))
print('lambda_upper',LMAX,'high_lambda_R_s_upper',rs_up)
print('small_phase_upper',pos_small+neg_small,'large_phase_upper',F(37049,1000)+neg_large)
