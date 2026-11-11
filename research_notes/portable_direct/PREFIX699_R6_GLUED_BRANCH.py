#!/usr/bin/env python3
"""PREFIX-699: exact rational implication certificate for glued BRC observer crossover.

Source dependency: PREFIX-698 (J* endpoints, jets), PREFIX-687 (near-zero I).
Frozen model: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
The script tests inherited-certificate implications, not the 189-row recurrence.
"""
from fractions import Fraction as F
from math import factorial
import json

A_JETS = (44000296, -168056589514, -6667624082229,
          39352687679231, 3189837819999830, -36266294695911132)
B_JETS = (789752024, 12845959424, -99127959112,
          -1326952329685, -14895243921676, -1960958310350017)
SIXTH_A = 201273663850076722544640
SIXTH_B = 17896441402901698560
J_LEFT, J_RIGHT = F(211, 4000), F(213, 4000)
NEAR_LEFT, NEAR_RIGHT = F(2663, 50000), F(53261, 1000000)
CENTER = F(53, 1000)

def jet_interval(floors, bound6, k, radius):
    # |G^(j)(CENTER)| enclosed by adjacent integer floor ticks / 10^8.
    err = sum(F(max(abs(floors[j]), abs(floors[j]+1)), 10**8)
              *radius**(j-k)/factorial(j-k) for j in range(k+1, 6))
    err += F(bound6)*radius**(6-k)/factorial(6-k)
    return F(floors[k], 10**8)-err, F(floors[k]+1, 10**8)+err

def run():
    radius = NEAR_LEFT-CENTER
    assert radius == F(13, 50000)
    assert NEAR_LEFT-J_RIGHT == F(1,100000)
    a2lo,a2hi = jet_interval(A_JETS, SIXTH_A, 2, radius)
    b1lo,b1hi = jet_interval(B_JETS, SIXTH_B, 1, radius)
    assert -40_000_000 < a2lo < a2hi < 40_000_000
    assert 128 < b1lo < b1hi < 129
    # PREFIX-687: -1800 < A'(z) < -1600 on [NEAR_LEFT, NEAR_RIGHT].
    # MVT gives A'(z) < -1600 + 40e6 * 1e-5 = -1200 on connector.
    bridge_upper = F(-1600)+F(40_000_000)*(NEAR_LEFT-J_RIGHT)
    assert bridge_upper == -1200
    # Exact predecessor endpoint enclosures (not recomputed here).
    Q_left_low, Q_left_high = F(9166464293188,10**12), F(9166464293189,10**12)
    Q_right_low, Q_right_high = F(446012343644423,10**12), F(446012343644424,10**12)
    Q_near_low, Q_near_high = F(9872453419496357,10**12), F(9872453419496358,10**12)
    assert 9 < Q_left_low < Q_left_high < 10
    assert 446 < Q_right_low < Q_right_high < 447
    assert 9872 < Q_near_low < Q_near_high < 9873
    assert J_LEFT<J_RIGHT<NEAR_LEFT<NEAR_RIGHT
    # Across connector, A(z)<A(J_RIGHT)<0.018 and B(z)>B(J_RIGHT)>7.92.
    # Therefore Q'(z) > (7.92*1200)/(0.018)^2 > 29,000,000.
    inv_slope_lower = F(792,100)*F(1200)/(F(18,1000)**2)
    assert inv_slope_lower > 29_000_000
    # Inherited: A(R)>17/1000, A(NEAR_LEFT)>0, B(J_LEFT)>786/100,
    # B(NEAR_LEFT)>0, unique A-zero z_A in (NEAR_LEFT, NEAR_RIGHT),
    # and A'<0, B'>0 on J* and near-zero interval I.
    result = {
      'id':'PREFIX-699-R6',
      'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'join_interval':['213/4000','2663/50000'],
      'join_radius_from_center':'13/50000',
      'A_second_interval_num_den':[[str(a2lo.numerator),str(a2lo.denominator)],
                                     [str(a2hi.numerator),str(a2hi.denominator)]],
      'B_first_interval_num_den':[[str(b1lo.numerator),str(b1lo.denominator)],
                                    [str(b1hi.numerator),str(b1hi.denominator)]],
      'A_second_abs_bound':40000000,
      'A_first_join_upper_strict':'-1200',
      'B_first_join_lower_strict':'128',
      'Q_first_join_lower_strict':'29000000',
      'integer_neighbor_root_gap_upper_strict':'1/29000000 (for consecutive q in 447..9872)',
      'Q_interval_left_floor12':'9166464293188',
      'Q_interval_right_floor12':'446012343644423',
      'Q_near_zero_floor12':'9872453419496357',
      'integer_partition':{'Jstar':'10..446', 'join':'447..9872', 'near_zero':'9873..infinity'},
      'main_theorem':'For all real q>Q(211/4000), exactly one z in (211/4000,z_A) solves q A(z)=B(z). For integer q>=0 this is iff q>=10.',
      'verification':'ALL_CHECKS_PASS PREFIX699-R6',
      'scope':'Exact rational implication of inherited PREFIX-698 and PREFIX-687 certificates; no fresh 189-row recomputation',
      'review':'UNREVIEWED / NOT_ADMITTED'
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__=='__main__':
    run()
