"""R594 - exact rational Rouché discs for the auxiliary scalar F and F_4096.
Uses R590's published full-degree coefficient envelope for the finite tail.
All assertions use integer/Fraction arithmetic; printed decimals are diagnostics.
"""
from fractions import Fraction as Q
from math import comb, factorial

K, J = 4096, 26
R, DELTA = Q(12), Q(1, 100000)


def z_mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def z_add(z, w):
    return z[0]+w[0], z[1]+w[1]


def z_abs_sq(z):
    return z[0]*z[0]+z[1]*z[1]


def ratios(k, j):
    P=Q(1)
    for h in range(1,j+1):
        P *= (1+Q(h+3,2*k)) * (1-Q(h,2*k))
    S=Q(0); U=Q(1)
    for q in range((j+1)//2+1):
        if q: U *= 1 + Q(3,2*(k-q+1)-1)
        S += comb(j+1,2*q)*U
    return P*S/Q(2**j)


def coefficients(k=None):
    a=[Q(24*8**j, factorial(2*j+4)) for j in range(J+1)]
    if k is not None: a=[x*ratios(k,j) for j,x in enumerate(a)]
    return [(-1)**j*x for j,x in enumerate(a)]


def eval_poly(c, z):
    out=(Q(0), Q(0))
    for a in c[::-1]:
        out=z_add(z_mul(out,z),(a,Q(0)))
    return out


def bound_second(c):
    return sum((Q(j*(j-1))*abs(c[j])*R**(j-2) for j in range(2,len(c))), Q(0))


def tail_bound(k=None):
    jj=J+1
    first=Q(24*8**jj,factorial(2*jj+4))*R**jj
    q=Q(8)*R/Q((2*jj+6)*(2*jj+5))
    assert q<1
    value=first/(1-q)
    if k is not None: value*=21*(k+1)*(2*k+1)
    return value


def cert(k, center):
    c=coefficients(k)
    val=eval_poly(c,center)
    dp=eval_poly([j*c[j] for j in range(1,len(c))], center)
    second=bound_second(c)
    tail=tail_bound(k)
    rest=DELTA**2*second/2+tail
    residual_ceiling=Q(1,10**7)
    slope_floor=Q(1,21)
    assert z_abs_sq(center)<(R-DELTA)**2
    assert z_abs_sq(val)<residual_ceiling**2
    assert z_abs_sq(dp)>slope_floor**2
    assert rest<Q(1,10**8)
    assert residual_ceiling + rest < slope_floor*DELTA
    print('R594_RATIONAL_ROUCHE_DISC_PASS', 'function', 'F' if k is None else f'F_{k}',
        'center', f'{center[0]}+i*{center[1]}','radius',DELTA,
        'residual_lt',float(residual_ceiling),
        'slope_gt',float(slope_floor),
        'remainder_lt',float(rest),
        'tail_lt',float(tail))

z0=(Q(6339235,10**6),Q(9480952,10**6))
z1=(Q(6338165,10**6),Q(9476771,10**6))
cert(None,z0)
cert(K,z1)

# Separate upper half-plane discs are disjoint, and enclosed in the R593 annulus.
for z in (z0,z1):
    assert z[1] > DELTA
    assert (10+DELTA)**2<z_abs_sq(z)<(13-DELTA)**2
assert (z0[1]-DELTA) - (z1[1]+DELTA)>Q(4,1000)
# Strict radial ordering through rational lower/upper bounds on center moduli.
assert z_abs_sq(z0)>Q(114049,10000)**2    # |z0| > 11.4049
assert z_abs_sq(z1)<Q(114011,10000)**2    # |z1| < 11.4011
assert Q(114049-114011,10000)-2*DELTA>Q(3,1000)
print('R594_ROOT_SEPARATION_PASS', 'imag_gap_gt',Q(4,1000), 'radial_gap_gt',Q(3,1000))
print('R594_EXACT_TWO_SIMPLE_ROOT_DISCS_PASS')
