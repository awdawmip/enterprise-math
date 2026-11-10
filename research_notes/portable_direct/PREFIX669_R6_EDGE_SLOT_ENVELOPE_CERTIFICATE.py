#!/usr/bin/env python3
"""PREFIX-669: exact rational implication checks for the frozen BRC edge-slot envelope.

Consumes AUTHOR-CERTIFIED published PREFIX-659, 660, 668 strict rational bounds.
It does not rerun the 189-layer frozen path recurrence, and is not independent review.
No floating-point predicates are used to validate a mathematical claim.
"""
from fractions import Fraction as F
import json

SCIENCE_PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

def run():
    checks=0
    def check(cond, label):
        nonlocal checks
        assert cond, label
        checks+=1
    qlo,qhi=F(12),F(24)
    delta=F(1,4096)
    z0=F(19,128)
    # PREFIX-659 exact center Q=(0,19/128); PREFIX-668 mean Q.
    v12_q_lo,v12_q_hi=F('86048.098'),F('86048.099')
    v24_q_lo,v24_q_hi=F('346339.323'),F('346339.324')
    mu_q_lo,mu_q_hi=F('89.455'),F('89.456')
    wqlo=(v12_q_lo+qlo*mu_q_lo)/(qlo*qlo)
    wqhi=(v12_q_hi+qlo*mu_q_hi)/(qlo*qlo)
    # PREFIX-660: 42<W'(z0)<43 and -92000<W''<-88000 throughout I.
    wprime_lo=F(42)-F(92000)*delta
    wprime_hi=F(43)+F(92000)*delta
    check(F(19)<wprime_lo,'uniform positive W_z lower')
    check(wprime_hi<F(66),'uniform W_z upper')
    wlo=wqlo-F(66)*delta
    whi=wqhi+F(66)*delta
    check(F(604)<wlo,'uniform W>604')
    check(whi<F(606),'uniform W<606')
    # PREFIX-660: -52,000,000 < V_zz < -12,800,000 for q in [12,24].
    # V_zz/q=q W_zz - mu_zz is affine and W_zz<0.
    curvature_denom_lo=F(12800000)
    curvature_denom_hi=F(52000000)
    qslot_curv_lower=2*F(604)
    qslot_curv_upper=2*F(606)+(qhi*66)**2/curvature_denom_lo
    check(qslot_curv_upper<F(1213),'slot-envelope M_qq upper <1213')
    check(qslot_curv_lower==F(1208),'slot-envelope M_qq lower 1208')
    # IFT: z_star'(q) = q W_z / (-V_zz) >0.
    dzlo=qlo*19/curvature_denom_hi
    dzhi=qhi*66/curvature_denom_lo
    check(F(0)<dzlo<dzhi,'moving maximizer strict derivative bounds')
    # Boundary mu=25+sum_{m=0}^{188} a_m s_m <=25+189=214.
    derivative_lower=2*qlo*604-214
    check(derivative_lower==14282,'M_q>14282 across slot interval')
    # PREFIX-660 edge-maximum intervals, q=12 and q=24.
    m12lo,m12hi=F('86048.1065484294'),F('86048.1065484353')
    m24lo,m24hi=F('346340.5678394088'),F('346340.5678394320')
    chord_loss_lower=F(1208,2)*F(36)
    chord_loss_upper=F(1213,2)*F(36)
    check(chord_loss_lower==21744,'midpoint chord gap lower')
    check(chord_loss_upper==21834,'midpoint chord gap upper')
    m18_by_chord_lo=(m12lo+m24lo)/2-chord_loss_upper
    m18_by_chord_hi=(m12hi+m24hi)/2-chord_loss_lower
    # Exact identity V_18(Q)=3/4 V_12(Q)+3/8 V_24(Q).
    check(F(3,4)*12**2+F(3,8)*24**2==18**2,'q=18 W identity')
    check(F(3,4)*12+F(3,8)*24==18,'q=18 mu identity')
    witness18lo=F(3,4)*v12_q_lo+F(3,8)*v24_q_lo
    witness18hi=F(3,4)*v12_q_hi+F(3,8)*v24_q_hi
    check(witness18lo>m18_by_chord_lo,'improved midpoint competitor lower')
    check(witness18hi<m18_by_chord_hi,'nonempty midpoint interval')
    # PREFIX-660 dyadic maximizer brackets.
    sep_lo=F(3682+583,2**24)
    sep_hi=F(3683+584,2**24)
    check(sep_lo==F(4265,2**24),'strict dyadic separation lower')
    check(sep_hi==F(4267,2**24),'strict dyadic separation upper')
    check(0<sep_lo<sep_hi<2*delta,'dyadic bounds stay within band width')
    check(wlo<whi,'nonempty W interval')
    check(v12_q_lo<v12_q_hi and v24_q_lo<v24_q_hi,
          'nonempty source enclosures')
    return {
      'schema':'EM_PREFIX669_R6_EDGE_SLOT_ENVELOPE_V1',
      'scientific_input_pin':SCIENCE_PIN,
      'scope':{'p':'0','z':['607/4096','609/4096'],'q':['12','24']},
      'source_status':'AUTHOR_CERTIFICATES_PREFIX659_660_668; NO_INDEPENDENT_ADMISSION',
      'certified_implications':{
        'W_range':'604 < W(0,z) < 606',
        'W_z_range':'19 < W_z(0,z) < 66',
        'maximizer_motion':'12*19/52000000 < z_star_prime < 24*66/12800000',
        'edge_max_derivative':'M_prime(q) > 14282',
        'edge_max_second_derivative':'1208 < M_double_prime(q) < 1213',
        'midpoint_chord_deficit':'21744 < (M(12)+M(24))/2-M(18) < 21834',
        'midpoint_lower_bound':str(witness18lo),
        'midpoint_upper_bound':str(m18_by_chord_hi),
        'optimizer_separation':'4265/16777216 < z_star(24)-z_star(12) < 4267/16777216'
      },
      'exact_auxiliary':{
        'W_center_lower':str(wqlo),'W_center_upper':str(wqhi),
        'W_band_lower':str(wlo),'W_band_upper':str(whi),
        'W_z_lower_derived':str(wprime_lo),'W_z_upper_derived':str(wprime_hi),
        'M_qq_upper_derived':str(qslot_curv_upper),
        'z_star_prime_lower_derived':str(dzlo),'z_star_prime_upper_derived':str(dzhi),
        'M_18_chord_lower':str(m18_by_chord_lo),
        'M_18_chord_upper':str(m18_by_chord_hi),
        'V_18_Q_lower':str(witness18lo),
        'V_18_Q_upper':str(witness18hi)
      },
      'checks_passed':checks,'result':'ALL_CHECKS_PASS',
      'mathematical_status':'AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED'
    }
if __name__=='__main__':
    out=run()
    print(json.dumps(out,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',out['checks_passed'])
