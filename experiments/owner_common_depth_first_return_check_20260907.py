"""Small exact normalization checks only; no walk enumeration or infinite-tail fit."""

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NATIVE = ROOT / 'experiments/x6_signed_native_spatial_v16_20260905'
sys.path.insert(0, str(NATIVE))
from signed_brc import endpoint_multiplicity


def derivative(coefficients):
    return tuple(i * x for i, x in enumerate(coefficients) if i)


def value(coefficients, x):
    return sum((coefficient * x**i for i, coefficient in enumerate(coefficients)), Q(0))


def reciprocal_jet(coefficients):
    output = [1 / coefficients[0]]
    for n in range(1, len(coefficients)):
        output.append(-sum((coefficients[k] * output[n-k] for k in range(1, n+1)), Q(0))
                      / coefficients[0])
    return tuple(output)


def main():
    # K(theta)=pi^4 P(theta/pi). The rational P pieces isolate every pi factor.
    plus = (Q(1,45), Q(0), Q(-1,6), Q(1,6), Q(-1,24))
    minus = (Q(1,45), Q(0), Q(-1,6), Q(-1,6), Q(-1,24))
    integral = sum((x/Q(i+1) for i,x in enumerate(plus)), Q(0))
    integral += sum((x*(0**(i+1)-(-1)**(i+1))/Q(i+1) for i,x in enumerate(minus)), Q(0))
    assert integral == 0
    left, right = minus, plus
    endpoint_checks = []
    for order in range(5):
        assert value(left,Q(-1)) == value(right,Q(1))
        if order < 3:
            assert value(left,Q(0)) == value(right,Q(0))
        if order == 3:
            assert value(right,Q(0)) - value(left,Q(0)) == 2
        endpoint_checks.append({'derivative_order':order, 'periodic_endpoint_value':str(value(left,Q(-1)))})
        left, right = derivative(left), derivative(right)
    # Independent algebra check of the reciprocal's third-derivative jump sign.
    mass = Q(7,3)
    u_minus = (mass,Q(2,5),Q(-1,7),Q(-2,3))
    u_plus = (mass,Q(2,5),Q(-1,7),Q(5,6))
    jump_u = 6*(u_plus[3]-u_minus[3])
    jump_inverse = 6*(reciprocal_jet(u_plus)[3]-reciprocal_jet(u_minus)[3])
    assert jump_inverse == -jump_u/mass**2
    # Existing native BRC functions are used only for the two analytically identified coefficients.
    f20 = Q(endpoint_multiplicity(2,(0,)*6),12**2)
    f61 = Q(endpoint_multiplicity(6,(1,)*6),12**6)
    f6minus1 = Q(endpoint_multiplicity(6,(-1,)*6),12**6)
    assert f20 == Q(1,12)
    assert f61 == f6minus1 == Q(5,20736)
    # G_6 coefficient 3/pi^3 times |hD|^-4 = (6h^2)^-2.
    assert Q(3,6**2) == Q(1,12)
    output = {'status':'PASS', 'kernel_mean_zero':True, 'periodic_endpoint_checks':endpoint_checks,
              'third_derivative_jump_over_pi':'2', 'reciprocal_jump_multiplier':str(-1/mass**2),
              'green_constant_times_pi_cubed':'1/12', 'f_2_0':str(f20),
              'f_6_plus_or_minus_1':str(f61),
              'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in (NATIVE/'signed_brc.py',Path(__file__))},
              'scope':'exact finite normalization only; no numerical S, F-tail calculation, simulation or tail certification'}
    destination = ROOT/'experiments/owner_common_depth_first_return_check_20260907.json'
    destination.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({key:output[key] for key in ('status','green_constant_times_pi_cubed','f_2_0','f_6_plus_or_minus_1')}))


if __name__ == '__main__':
    main()
