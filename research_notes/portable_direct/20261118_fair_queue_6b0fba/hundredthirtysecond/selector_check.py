"""CM moments of the six CP19 markings; python-flint 0.9, SymPy 1.13+."""
from fractions import Fraction
from itertools import permutations
from math import gcd, isqrt
import json

from flint import acb, arb, ctx
import sympy as sp


def j_value(z):
    return 256 * (1-z+z*z)**3 / (z*(1-z))**2


def triple(z, v):
    return (1+z+v)/(1-z), -1+2*z-v, 1+(v-2)/z


def mirror(z, v):
    w = z*(4-2*z+v)/(4*z+v-2)
    return w, 2*(z+w)-v-2


def symbolic():
    z, v, psi = sp.symbols('z v psi')
    x, y, t = triple(z, v)
    w, u = mirror(z, v)
    r4 = 1-z+z*z
    r6 = (1+z)*(1-2*z)*(2-z)/2
    j = j_value(z)
    s1 = x*x+y*y+t*t
    s2 = (x*y)**2+(y*t)**2+(t*x)**2
    s3 = (x*y*t)**2
    rel = [
        x*y+x*t+y*t+9, (x+y)/(x+3)-z,
        (s2-81)**2-4*(s1-18)*s3,
        s1.subs(v,psi*r6/r4)/3-6-(j-1728)*(psi-2)**2/768,
        r6**2/r4**3 - (j-1728)/j,
        mirror(w,u)[0]-z, mirror(w,u)[1]-v
    ]
    rel.extend(a+b for a,b in zip(triple(w,u), (x,y,t)))
    # Certify the factors in the invariant mirror j before cubing them.
    num, den = z*(4-2*z+v), 4*z+v-2
    xi = (4*z+v-2)*(v-2*z+4)*(v-2-2*z)
    rel.extend([den*num*(den-num)-z*(1-z)*xi,
                num**2-num*den+den**2-(r4*v**2-4*r6*v+4*r4**2),
                xi-(v**3-12*r4*v+16*r6)])
    assert all(sp.cancel(eq) == 0 for eq in rel)
    return len(rel)


def reduced(d):
    for a in range(1, isqrt(d//3)+1):
        for b in range(-a,a+1):
            c, rem = divmod(d+b*b,4*a)
            if rem or c < a or gcd(gcd(a,b),c) != 1:
                continue
            if b >= 0 or (abs(b) < a and a < c):
                yield a,b,c


def analytic(form):
    a,b,c = form
    d = 4*a*c-b*b
    tau = acb(-arb(b)/(2*a), arb(d).sqrt()/(2*a))
    q2 = (2*arb.pi()*acb(0,1)*tau).exp()
    r = abs(q2).upper()
    h = 80
    tail = (24*(h+1)*r**(h+1)/(1-r)**3).upper()
    err = arb(0, tail)
    e2 = 1-24*sum(k*q2**k/(1-q2**k) for k in range(1,h+1))
    z = tau.modular_lambda()
    W = acb(0).modular_theta(tau)[2]**4
    v = (e2+acb(err,err)-3/(arb.pi()*tau.imag))/W
    return tau,z,v


def ceil_ball(z):
    return int(z.upper().ceil().unique_fmpz())


def floor_ball(z):
    return int(z.lower().floor().unique_fmpz())


def cm_window():
    previous = arb(18).sqrt()
    rows = []
    forms_count = moments_count = mirror_count = 0
    for d in range(7,41):
        shapes = list(reduced(d))
        if not shapes:
            continue
        principal = None
        other_bounds = []
        for shape in shapes:
            tau,z,v = analytic(shape)
            x,y,t = triple(z,v)
            a,b,M = sorted(map(abs,(x,y,t)))
            upper = (M**2 + a**2 + b**2).sqrt()
            if shape[0] == 1:
                lower = (M**2 - a**2 - b**2).sqrt()
                principal = lower,upper
                mirror_j = j_value(mirror(z,v)[0])
                assert mirror_j.is_finite() and not mirror_j.overlaps(tau.modular_j())
                mirror_count += 1
            else:
                other_bounds.append(upper)
            assert tau.modular_j().overlaps(j_value(z))
            # The centered moment uses each of the six true transformed b values.
            six = []
            for word in ('', 'T','S','I','IT','IS'):
                Z,E = z,v
                for op in reversed(word):
                    if op == 'I':
                        Z,E = 1/Z,E/Z
                    elif op == 'T':
                        Z,E = Z/(Z-1),E/(1-Z)
                    else:
                        Z,E = 1-Z,-E
                six.append((1-3*Z-E)/(1-Z)-2)
            for m in (1,2,3,11):
                value = sum(u**(2*m) for u in six)/6
                assert value.overlaps(sum(u**(2*m) for u in (x,y,t))/3)
                assert sum(u**(2*m-1) for u in six).contains(0)
                moments_count += 1
            forms_count += 1
        lower, upper = principal
        assert lower > previous and all(lower > bound for bound in other_bounds)
        rows.append(dict(d=d, forms=len(shapes), lower_floor=floor_ball(lower),
                         upper_ceil=ceil_ball(upper),
                         nonprincipal_max_ceil=max(map(ceil_ball,other_bounds),default=0)))
        previous = upper
    L = arb.pi()*arb(41).sqrt()/2
    T = (1+3/L)*L.exp()/16
    assert previous < 1679 < T-5 and T-3 > 1700
    return dict(precision_bits=ctx.prec, nonelliptic_forms=forms_count,
                direct_six_mark_moment_checks=moments_count, distinct_mirror_j_principal=mirror_count,
                rows=rows, largest_small_radius_ceiling=ceil_ball(previous),
                first_large_T_floor=floor_ball(T))


def exact():
    q = Fraction
    x,y = q(1),q(3,2)
    t = (-9-x*y)/(x+y)
    candidates = set()
    for sign in (1,-1):
        for a,b,c in permutations((x,y,t)):
            candidates.add(j_value(sign*(a+b)/(sign*a+3)))
    assert candidates == {q(470596,225),q(3631696,2025)}
    # Independent input from the level-seven modular polynomial and fixed isogeny in W123.
    j,psi = q(-3375),q(5,21)
    r = 1-1728/j
    mirror_j = j/r*(r*(psi**2-4*psi)+4)**3/(r*psi**3-12*psi+16)**2
    moment = 6+(j-1728)*(psi-2)**2/768
    assert moment == q(-26211,1792) and mirror_j == q(-99252847,416025)
    return dict(generic_j_pair=sorted(map(str,candidates)), discriminant_minus_seven=
                dict(j=int(j),psi=str(psi),first_moment=str(moment),mirror_j=str(mirror_j)))


if __name__ == '__main__':
    ctx.prec = 256
    print(json.dumps(dict(rational_identity_checks=symbolic(),cm_window=cm_window(),
                          exact=exact()),indent=2,sort_keys=True))
