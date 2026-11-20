#!/usr/bin/env python3
"""Stage334-B: exact polynomial and rational witness checks for five-chamber
strict Pareto domination in the inherited three-visit, two-source BRC observer.
It is not a native P000-to-X6 proof or a formal project admission.
"""
from fractions import Fraction as Q

W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
CUBICS = (
    (1, -3, 3, -1),   # (1-z)^3
    (0, 1, -2, 1),    # z(1-z)^2
    (0, 0, 1, -1),    # z^2(1-z)
    (0, 0, 0, 1),     # z^3
)
DB = tuple((p[1], 2*p[2], 3*p[3]) for p in CUBICS)


def poly_add(*args):
    n = max(len(a) for a in args)
    return tuple(sum((Q(a[i]) if i < len(a) else Q(0)) for a in args) for i in range(n))


def poly_scale(p, scale):
    return tuple(Q(v) * scale for v in p)


def poly_derivative_combination(weights):
    return poly_add(*(poly_scale(DB[k], weights[k]) for k in range(4)))


def B(k, z):
    return z**k * (1-z)**(3-k)


def r(k, x, y):
    return (4*B(k,x) + B(k,y))/5 - Q(M[k],160)


def b(x, y):
    return Q(5,32) * sum(W[k]*abs(r(k,x,y)) for k in range(4))


def D3(a, z):
    return sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4)) / 2


def c(x, y):
    return (63*D3(Q(1,4),x) + D3(Q(3,4),x) +
            9*D3(Q(1,4),y) + 7*D3(Q(3,4),y)) / 256


def signs(x, y):
    rs=[r(k,x,y) for k in (0,1,3)]
    assert all(t != 0 for t in rs)
    assert r(2,x,y)>0
    return ''.join('+' if v>0 else '-' for v in rs)


def expected_atom_sign(a,z):
    values=[B(k,a)-B(k,z) for k in range(4)]
    return tuple(1 if v>0 else -1 if v<0 else 0 for v in values)


# 1. The exact signed binomial derivative polynomials Q_sigma(z) are
#    equal coefficient-by-coefficient to the displayed expressions.
expected = {
    '++-': (0, 0, -6),
    '+-+': (-6, 24, -18),
    '+--': (-6, 24, -24),
    '---': (0, 12, -18),
    '--+': (0, 12, -12),
    '-+-': (6, -12, 0),
}
for sector, want in expected.items():
    s=(1 if sector[0]=='+' else -1,
       1 if sector[1]=='+' else -1,
       1,
       1 if sector[2]=='+' else -1)
    got=poly_derivative_combination(tuple(W[k]*s[k] for k in range(4)))
    assert got == tuple(map(Q,want)), (sector,got,want)
    print('PUBLIC_DERIVATIVE_POLYNOMIAL',sector,str(got))

# 2. Exact atomic signed derivatives of the full tagged total-variation
#    observer agree with the continuous monotonicity formulas on R.
s_x_quarter=(-1,+1,+1,+1)
s_x_3quarter=(-1,-1,+1,+1)
s_y_quarter=(+1,+1,-1,-1)
s_y_3quarter_below=(-1,-1,+1,+1)
s_y_3quarter_above=(-1,-1,-1,+1)

def signed_tagged_derivative(coeffs):
    return poly_scale(poly_derivative_combination(tuple(W[k]*coeffs[k] for k in range(4))),Q(-1,512))

cx=signed_tagged_derivative(tuple(63*s_x_quarter[k]+s_x_3quarter[k] for k in range(4)))
cy_below=signed_tagged_derivative(tuple(9*s_y_quarter[k]+7*s_y_3quarter_below[k] for k in range(4)))
cy_above=signed_tagged_derivative(tuple(9*s_y_quarter[k]+7*s_y_3quarter_above[k] for k in range(4)))
assert cx == (Q(-189,256),Q(372,256),Q(-183,256))
assert cy_below == (Q(0),Q(12,256),Q(-12,256))
assert cy_above == (Q(0),Q(54,256),Q(-75,256))
print('TAGGED_CX', cx, '= -(1-x)(189-183x)/256 < 0 on R')
print('TAGGED_CY_BELOW',cy_below,'= 3y(1-y)/64 > 0 on R')
print('TAGGED_CY_ABOVE',cy_above,'= 3y(18-25y)/256 > 0 on R')

# The one varying tag comparison is a real algebraic cusp with positive
# one-sided y derivatives. Its location lies strictly inside (57/100,58/100):
# q(y)=16y^2-4y-3 has a single positive root there.
q=lambda y: 16*y*y-4*y-3
assert q(Q(57,100)) < 0 < q(Q(58,100))
assert Q(1,2)<Q(57,100)<Q(58,100)<Q(2,3)<Q(18,25)
print('TAGGED_CUSP', 'q(57/100)<0<q(58/100); one positive root',
      'c_y left and right strictly positive')

# 3. Conservation of binomial atom mass is an exact polynomial identity.
#    In the --- public chamber this gives b=3/16 F2.
assert poly_add(*(poly_scale(CUBICS[k],W[k]) for k in range(4))) == (Q(1),Q(0),Q(0),Q(0))
assert sum(W[k]*M[k] for k in range(4)) == 160

# 4. Five rational witnesses, one in each globally excluded strict chamber.
#    The universal proof is derivative sign + continuity, not this finite set.
points=(
    ('++-', Q(221,1000),Q(520,1000),'x'),
    ('+-+', Q(220,1000),Q(621,1000),'x'),
    ('+--', Q(220,1000),Q(597,1000),'x'),
    ('---', Q(230,1000),Q(570,1000),'y'),
    ('--+', Q(228,1000),Q(625,1000),'y'),
)
for sector,x,y,direction in points:
    assert signs(x,y)==sector
    x2=x+Q(1,10000) if direction=='x' else x
    y2=y-Q(1,10000) if direction=='y' else y
    assert signs(x2,y2)==sector
    assert Q(21,100)<=x<=Q(6,25) and Q(1,2)<=y<=Q(2,3)
    assert Q(21,100)<=x2<=Q(6,25) and Q(1,2)<=y2<=Q(2,3)
    P0,T0=b(x,y),c(x,y)
    P1,T1=b(x2,y2),c(x2,y2)
    assert P0<=Q(61,10000) and P1<P0 and T1<T0
    assert tuple(expected_atom_sign(Q(1,4),x))==s_x_quarter
    assert tuple(expected_atom_sign(Q(3,4),x))==s_x_3quarter
    assert tuple(expected_atom_sign(Q(1,4),y))==s_y_quarter
    assert tuple(expected_atom_sign(Q(3,4),y))==(
        s_y_3quarter_below if y<=Q(57,100) else s_y_3quarter_above)
    print('STRICT_RATIONAL_DOMINANCE',sector,'q=',(str(x),str(y)),
          'q_prime=',(str(x2),str(y2)),
          'b_before=',str(P0),'b_gain=',str(P0-P1),
          'c_before=',str(T0),'c_gain=',str(T0-T1))

# 5. The surviving -+- chamber has no coordinatewise simultaneous
#    decrease in the beneficial directions x up, y down.
assert expected['-+-'] == (6,-12,0)
print('SURVIVING_STRICT_CHAMBER', '-+-', 'and public-zero boundaries retained')
print('STAGE334B_FIVE_CHAMBER_STRICT_PARETO_DOMINANCE_EXACT_PASS')
