"""Exact algebra and finite inventory checks for COMPACT_FINITE_REDUCTION.md."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json
import sympy as sp


def run():
    checks={
        'short_column_bound': F(4,3)<F(11,10)**4,
        'long_column_bound': F(101,20)<F(9,4)**2,
        'covering_radius_bound': (F(11,10)+F(9,4))/2==F(67,40),
        'supnorm_vector_bound': 4*F(67,40)/F(1,4)==F(134,5),
        'first_integer_coordinate_bound': F(134,5)**2*2*F(9,4)**2<86**2,
        'second_integer_coordinate_bound': F(134,5)**2*2*F(11,10)**2<42**2,
    }
    count=sum(gcd(abs(m),abs(n))==1 for m in range(-85,86) for n in range(-41,42))
    checks['oriented_primitive_count']=count==8696
    x,y,z=sp.symbols('x y z')
    vertices=[sp.Rational(1),sp.Rational(2),sp.Rational(4),sp.Rational(7)]
    linear=1+x+3*y+6*z
    for q in [0,1,2]:
        got=sum(vertices[i]**(q+3)/sp.prod(vertices[i]-vertices[j] for j in range(4) if j!=i)
                for i in range(4))/((q+1)*(q+2)*(q+3))
        direct=sp.integrate(linear**q,(z,0,1-x-y),(y,0,1-x),(x,0,1))
        checks['simplex_identity_degree_'+str(q)]=sp.simplify(got-direct)==0
    return {'status':'exact_arithmetic_checks','all_passed':all(checks.values()),
            'checks':checks,'oriented_primitive_vectors':count,'unoriented_directions':count//2,
            'scope':'Phase-uniform finite reduction on y<=5, positions [1/4,3/4]; compact integral unevaluated.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_name('compact_reduction_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
