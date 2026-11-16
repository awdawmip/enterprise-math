"""Certificate for the exact constants in the confluent singleton strip."""
from fractions import Fraction as Q
import json


def certificate():
    a, d, b = Q(40, 41), Q(42, 41), Q(7, 16)
    velocity = Q(9, 4 * 41**2)
    c_floor = a - Q(9, 41)
    c_rate = 8*velocity+(Q(9,4)+Q(41,4)*velocity/a)/41
    assert c_floor > Q(3,4) and c_rate < Q(1,12)
    log_slope = Q(14,3)+1-2-(Q(19,5)+9)*velocity/a-Q(1,9)
    m = 2*b*d**4
    separated = (a/d)**4*c_floor/(d+Q(9,41))*16/((1+m)*(1+d*m))
    assert separated>2 and log_slope>0
    return dict(level_curve_speed=str(velocity), log_C_speed_upper=str(c_rate),
                separation_factor_lower=str(separated), positive_slope_lower=str(log_slope))


if __name__ == '__main__':
    print(json.dumps(certificate(),indent=2))
