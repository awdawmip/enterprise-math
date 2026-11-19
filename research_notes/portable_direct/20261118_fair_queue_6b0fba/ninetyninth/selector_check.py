"""Single CM selector, integer modular polynomial and rigorous Arb intervals.

Usage: python selector_check.py [--out selector_checked.json]
Dependency: python-flint==0.9.0. No network or extra input files are used.
"""
import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, isqrt
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpz_poly


def reduced_forms(d):
    for a in range(1, isqrt(d // 3) + 1):
        for b in range(-a, a + 1):
            c, rem = divmod(b * b + d, 4 * a)
            boundary = abs(b) == a or a == c
            if not rem and a <= c and not (boundary and b < 0) and gcd(a, gcd(b, c)) == 1:
                yield (a, b, c)


def add_radius(z, radius):
    error = arb(0, radius.upper())
    return z + acb(error, error)


def nome_data(tau):
    q = (arb.pi() * acb(0, 1) * tau).exp()
    r = abs(q).upper()
    h = 16
    theta3 = 1 + 2 * sum(q ** (n*n) for n in range(1, h+1))
    theta3 = add_radius(theta3, 2*r**((h+1)**2)/(1-r))
    theta2_part = 1 + sum(q ** (n*(n+1)) for n in range(1, h+1))
    theta2_part = add_radius(theta2_part, r**((h+1)*(h+2))/(1-r))
    x = 16*q*(theta2_part/theta3)**4
    assert x.overlaps(tau.modular_lambda())
    w = theta3**4
    assert w.overlaps(acb(0).modular_theta(tau)[2]**4)
    u = q*q
    h = 64
    e2 = 1 - 24*sum(n*u**n/(1-u**n) for n in range(1, h+1))
    e2 = add_radius(e2, 24*(h+1)*r**(2*(h+1))/(1-r*r)**3)
    return x, (e2-3/(arb.pi()*tau.imag))/w


def marked_values(x, e):
    # Words designate composition, acting right-to-left.
    plain = (1-3*x-e)/(1-x)
    trans = 1+2*x-e
    cusp = 3+(e-2)/x
    for word, predicted in [('1', plain), ('T', trans), ('S', cusp),
                            ('I', 4-plain), ('IT', 4-trans), ('IS', 4-cusp)]:
        z, v = x, e
        for g in reversed(word):
            if g == 'S':
                z, v = 1-z, -v
            elif g == 'T':
                z, v = z/(z-1), v/(1-z)
            elif g == 'I':
                z, v = 1/z, v/z
        value = (1-3*z-v)/(1-z)
        assert predicted.overlaps(value)
        yield word, z, v, value


def analytic_constants():
    r = Fraction(1, 15)
    a = 2*r/(1-r**3)
    h = r*r/(1-r*r)
    d = 24*r*r/(1-r*r)**3
    assert 16*((1-h)/(1+a))**4 > 9 and 16*((1+h)/(1-a))**4 < 30
    assert ((1-a)/(1+a))**4 > Fraction(1, 3) and (1+d)/(1-a)**4 < 2
    pi = arb.pi()
    assert (-pi*arb(3).sqrt()/2).exp() < arb(1)/15
    # Uniform Lipschitz bounds in the disk r <= 1/20000.
    # |theta3/G-1| <= (2r/(1-r^3)+r^2/(1-r^2))/(1-r^2/(1-r^2)).
    t = Fraction(1, 20000)
    eps = (2*t/(1-t**3)+t*t/(1-t*t))/(1-t*t/(1-t*t))
    assert (1+eps)**4-1 < 10*t
    assert (1-2*t/(1-t**3))**(-4)-1 < 9*t
    assert 9 + 24*t/(1-t*t)**3/(1-2*t/(1-t**3))**4 < 12
    assert 1 + Fraction(13,10)*10/16 + 12*(1+10*t)/16 < 3
    ten = arb(10)
    assert ten.exp() > 20000 and arb(5).exp() > 140
    assert Fraction(140**2,16)-3 > 32+Fraction(4*140,9)
    assert pi**2*ten.exp()/1280 > 100
    l41 = pi*arb(41).sqrt()/2
    cutoff = (1+3/l41)*l41.exp()/16-3
    assert l41 > 10 and cutoff > 1800
    return {'large_abs_D_from':41, 'pole_radius_absolute_error_lt':3,
            'T_derivative_gt':100, 'T_41_minus_3_gt':1800,
            'reduced_nome_lt':'1/15', 'principal_nome_lt':'1/20000'}


def classical_phi(p):
    """Coefficients of Phi_p from the distinct leading poles of j(q^p)^i j(q)^j, i>=j."""
    bound = p*(p+1)
    order = bound+1
    sigma = [0]*order
    for k in range(1, order):
        for n in range(k, order, k):
            sigma[n] += k**3
    jshift = fmpz_poly([1]+[240*a for a in sigma[1:]]).pow_trunc(3, order)
    for k in range(1, order):
        factor = [0]*order
        for i in range((order-1)//k+1):
            factor[k*i] = comb(23+i, 23)
        jshift = (jshift*fmpz_poly(factor)).truncate(order)
    low = [jshift.pow_trunc(i, order) for i in range(p+2)]
    high = [s.inflate(p).truncate(order) for s in low]

    def term(i, j):
        weight = p*i+j
        return (high[i]*low[j]).truncate(weight+1).left_shift(bound-weight)

    jet = term(p+1, 0)+term(0, p+1)
    phi = {(p+1, 0):1, (0, p+1):1}
    for i in range(p, -1, -1):
        for j in range(i, -1, -1):
            coefficient = -int(jet[bound-(p*i+j)])
            if coefficient:
                phi[i, j] = coefficient
                jet += term(i, j)*coefficient
                if i != j:
                    phi[j, i] = coefficient
                    jet += term(j, i)*coefficient
    assert jet == 0
    return phi


def minus_eleven():
    j = -32768
    assert list(fmpz_poly.hilbert_class_poly(-11)) == [-j, 1]
    phi = classical_phi(11)

    def beta(a, b):
        return sum(c*comb(i, a)*comb(k, b)*j**(i+k-a-b)
                   for (i, k), c in phi.items() if i >= a and k >= b)

    assert beta(0, 0) == 0 and beta(0, 1) != 0
    slope = Fraction(beta(2, 0)-beta(1, 1)+beta(0, 2), beta(0, 1))
    psi = 6*j*slope+Fraction(7*j-6912, j-1728)
    assert slope == Fraction(289,8830976) and psi == Fraction(32,77)
    X = fmpz_poly([0, 1])
    A4 = 1-X+X*X
    twice_A6 = (1+X)*(1-2*X)*(2-X)
    P = A4**3+128*X**2*(1-X)**2
    U = 77*(-1-X)*A4-16*twice_A6   # b-2=U/V
    V = 77*(1-X)*A4
    assert P.resultant(V) != 0
    coeff = [1803649, 0, -1694495, 0, 426283, 0, 1331]
    relation = sum(c*U**i*V**(6-i) for i, c in enumerate(coeff))
    assert relation % P == 0
    tau = acb(-arb(1)/2, arb(11).sqrt()/2)
    x, e = nome_data(tau)
    A4 = 1-x+x*x
    A6 = (1+x)*(1-2*x)*(2-x)/2
    assert (77*e*A4-32*A6).contains(0)
    distinct_squares = []
    for _, xx, _, b in marked_values(x,e):
        assert sum(c*(b-2)**i for i,c in enumerate(coeff)).contains(0)
        w = ((1+xx)/(1-xx))**2
        v = (b-2)**2
        assert (64*(w+3)**3-j*(w-1)**2).contains(0)
        assert v.overlaps(w*(1+32*(9-w)/(154*(w+3)))**2)
        if all(not v.overlaps(s) for s in distinct_squares):
            distinct_squares.append(v)
    assert len(distinct_squares) == 3
    return {'j':j,'Taylor_quotient':str(slope),'E2star_E4_over_E6':str(psi),
            'chi_star':int((j-1728)*psi), 'b_minus_2_polynomial_ascending':coeff,
            'distinct_centered_squares':len(distinct_squares), 'hilbert_modulus':-44, 'ring_class_number':len(list(reduced_forms(44))),
            'q_jet_through_zero_after_shift':132}


def small_discriminants():
    values = []
    field_counts = {}
    for d in range(3, 41):
        shapes = list(reduced_forms(d))
        if not shapes:
            continue
        before = len(values)
        for a, b, c in shapes:
            tau = acb(-arb(b)/(2*a), arb(d).sqrt()/(2*a))
            x, e = nome_data(tau)
            local = []
            for word, xx, ee, beta in marked_values(x, e):
                if d in (3, 4):
                    assert ee.contains(0)
                    if any(xx.overlaps(prev) for prev in local):
                        continue
                    if d == 3:
                        assert (beta**2-4*beta+7).contains(0)
                assert abs(beta-2) < 1800
                local.append(xx)
                values.append(((-d, a, b, c, word), xx, beta))
            assert len(local) == {3:2, 4:3}.get(d, 6)
        field_counts[-d] = {'forms':shapes, 'marks':len(values)-before}
    closest = None
    largest = None
    for tag, _, beta in values:
        if largest is None or abs(beta-2) > largest[0]:
            largest = (abs(beta-2), tag)
    for (t, x, b), (u, y, c) in combinations(values, 2):
        assert not x.overlaps(y)
        distance = abs(b-c)
        assert distance > 0
        if closest is None or distance < closest[0]:
            closest = distance, [t, u]
    inverse = int((1/closest[0]).ceil().unique_fmpz())
    assert all(abs(v[2]-w[2]) > arb(1)/inverse for v,w in combinations(values, 2))
    max_ceil = int(largest[0].ceil().unique_fmpz())
    assert all(abs(beta-2)<max_ceil for _, _, beta in values)
    assert len(values) == 197 and len(field_counts) == 20
    return {'orders':field_counts, 'marks':len(values), 'unordered_pairs':comb(len(values),2),
            'minimum_single_b_distance_gt':'1/'+str(inverse), 'close_pair':closest[1],
            'maximum_abs_b_minus_2_lt':max_ceil, 'large_mark':largest[1]}


def check():
    ctx.prec = 224
    classes = {}
    for d in range(3,500,8):
        h = len(list(reduced_forms(d)))
        h2 = len(list(reduced_forms(4*d)))
        assert h2 == (1 if d==3 else 3)*h
        classes[-d] = [h, h2]
    return {'python_flint':flint.__version__, 'bits':ctx.prec, 'analytic':analytic_constants(),
            'small_discriminants':small_discriminants(), 'exact_D_minus_11':minus_eleven(),
            'h_D_and_h_4D_for_inert_2_abs_D_lt_500':classes}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    target = parser.parse_args().out
    data = json.dumps(check(), indent=2, sort_keys=True)+'\n'
    if target:
        target.write_text(data, encoding='utf-8')
    else:
        print(data, end='')
