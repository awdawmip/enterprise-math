"""Axial polarized Fourier kernel. Python 3 and python-flint 0.9.0 (Arb)."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import isqrt
import json
from flint import arb, ctx, fmpq

ctx.prec = 128
PI = arb.pi()


def to_ball(f):
    return arb(fmpq(f.numerator, f.denominator))


def decimal_endpoint(value, digits, upper):
    scaled = value * (10**digits)
    integer = (scaled.upper().ceil() if upper else scaled.lower().floor()).unique_fmpz()
    n = int(integer)
    return ('-' if n < 0 else '') + str(abs(n)//10**digits) + '.' + str(abs(n)%10**digits).zfill(digits)


def interval(lo, hi, digits):
    return [decimal_endpoint(lo,digits,False), decimal_endpoint(hi,digits,True)]


def r2_sieve(limit):
    counts = [0]*(limit+1)
    for d in range(1,limit+1,2):
        add = 4 if d%4==1 else -4
        for m in range(d,limit+1,d):
            counts[m] += add
    return counts


def finite_ball(K, N, r2):
    box = range(-isqrt(N), isqrt(N)+1)
    dx, dxy, dy = Fraction(0), Fraction(0), Fraction(0)
    for x,y,t in product(box, repeat=3):
        m = x*x+y*y
        r,s = m+t*t,m+(K-t)**2
        if not m or r>N:
            continue
        w=Fraction(K*m,r*r*s*s)
        dx += w*(s-x*x)
        dy += w*(s-y*y)
        dxy -= w*x*y
    grouped=Fraction(0)
    for t in box:
        for m in range(1,N-t*t+1):
            r,s=m+t*t,m+(K-t)**2
            grouped += Fraction(K*m*r2[m]*(2*s-m),2*r*r*s*s)
    assert dx == grouped == dy and not dxy
    return grouped


def coefficients(y):
    phi = (y*y+15*y+28)/(2*(y+4)**3)
    rem = (3*y*y+22*y+8)/(64*(y+4)**3)
    beta = (y*y+3*y+4)/(2*(y+4)**2)
    return phi,rem,beta


def vertical_test():
    tests = 0
    for K,m in product((1,2,5,9),(1,2,8,25,37)):
        N = 36
        f = Fraction(0)
        for t in range(-N,N+1):
            r,s=m+t*t,m+(K-t)**2
            f += Fraction(K*m*(2*s-m),2*r*r*s*s)
        v=arb(m).sqrt()
        y=arb(K*K)/m
        phi,_,beta=coefficients(y)
        exact=K*PI*phi*(PI*v).coth()/(v*m)+PI**2*beta*(PI*v).csch()**2/K
        gap=exact-to_ball(f)
        assert gap > 0 and gap < to_ball(Fraction(8*K*m,5*N**5))
        tests += 1
    return tests


def epstein():
    H=3
    norms = Counter(x*x+y*y+z*z for x,y,z in product(range(-H,H+1), repeat=3) if (x,y,z)!=(0,0,0))
    C=-3*PI
    for r, n in norms.items():
        root=arb(r).sqrt()
        C += n*((-PI*r).exp()/r+PI*(PI.sqrt()*root).erfc()/root)
    tail=52*(-PI*(H+1)**2).exp()/(1-(-PI*(2*H+3)).exp())
    return C, C+tail


def dirichlet(s):
    h=arb(s)/2
    beta=(h.zeta(arb(1)/4)-h.zeta(arb(3)/4))/(arb(4)**h)
    return 4*h.zeta()*beta


def axial_enclosures(r2, M, ks):
    J=isqrt(M//2)
    mroot=arb(M).sqrt()
    geom=1-(-2*PI*mroot).exp()
    z3,z5=dirichlet(3),dirichlet(5)
    sums={K:PI*K*(7*z3/32-3*K*K*z5/64) for K in ks}
    for m in range(1,M+1):
        if not r2[m]:
            continue
        root=arb(m).sqrt()
        t=(-2*PI*root).exp()
        coth_excess=2*t/(1-t)
        csch_sq=4*t/(1-t)**2
        for K in ks:
            y=arb(K*K)/m
            phi,rem,beta=coefficients(y)
            sums[K] += r2[m]*(PI*K/(m*root)*(y*y*rem+phi*coth_excess)+PI**2*beta*csch_sq/K)
    q=(-2*PI).exp()
    shell=8*q**(J+1)*((J+1)-J*q)/(1-q)**2
    rows={}
    for K,v in sums.items():
        tail=PI*K**5/(80*J**5)+(7*PI*K/(16*mroot**3*geom)+2*PI**2/(K*geom**2))*shell
        rows[str(K)]=interval(v,v+tail,8)
    return rows


def off_axis():
    R, scale = 128, 10**12
    total, terms = 0, 0
    # Reflection in z and swapping x,y preserve both denominator and numerator.
    for x in range(-R,R+1):
        for y in range(-R,x+1):
            r0=x*x+y*y
            s0=(1-x)**2+(1-y)**2
            u=(x-y)**4
            parity_weight=1 if x==y else 2
            for z in range(0,R+1):
                w=z*z
                r,s=r0+w,s0+w
                if r*s:
                    term_weight=parity_weight*(2 if z else 1)
                    total += (scale*term_weight*(u-4*w*w))//(2*r*r*s*s)
                    terms += 1
    tail = Fraction(8*22,7*R)*Fraction(R+2,R-1)**4
    low=Fraction(total,scale)
    high=Fraction(total+terms,scale)
    assert low>tail
    return {"cube_radius":R,"scale":scale,"rounded_numerator":total,"orbit_terms":terms,
            "absolute_exterior_bound":str(tail),
            "sqrt2_times_polarization_gap":interval(to_ball(low-tail),to_ball(high+tail),8)}


def run():
    M=256**2
    r2=r2_sieve(M)
    direct=Counter(x*x+y*y for x,y in product(range(-256,257),repeat=2) if 0<x*x+y*y<=M)
    assert all(r2[m]==direct[m] for m in range(1,M+1))
    finite={}
    for K,N in ((1,2),(2,5),(3,7),(5,16),(8,25)):
        finite[f"K={K},squared_radius={N}"]=str(finite_ball(K,N,r2))
    C,D=epstein()
    return {"finite_ball_scalars":finite,"r2_norms_compared":M,"vertical_tail_checks":vertical_test(),
            "off_axis_1_1_0":off_axis(),"continuum":interval(3*PI**3/8,3*PI**3/8,12),
            "epstein_C":interval(C,D,14),"correction_2C_over_3":interval(2*C/3,2*D/3,14),
            "axial_infinite_sums":{"horizontal_squared_cutoff":M,
                   "integer_K_enclosures":axial_enclosures(r2,M,(1,2,4,8,16,32,64))}}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
