#!/usr/bin/env python3
"""Rational enclosures and exact disk pair counts for the planar Gaussian at alpha=1."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import subprocess
import sys

SCALE = 10**19
SOURCE = {"build/main.tex": "bfa619a454d49596b65f310f0bfdce3ae3f5ed6545bd9058d0c6316843ded2a6",
          "verification/check_certificate.py": "5689152e970b652a8e40c3c120eda3b45320c8745968a5cb416fa9b9dbdc5385"}


def lower(x):
    return F((x*SCALE).__floor__(), SCALE)


def upper(x):
    return -lower(-x)


def sqrt_box(x):
    a = isqrt((x*SCALE*SCALE).__floor__())
    return F(a, SCALE), F(a+1, SCALE)


def atan_box(q):
    x = F(1, q)
    total = 0
    for j in range(24):
        total += (-1)**j*x**(2*j+1)/(2*j+1)
    return total, total+x**49/49


def exp_negative(x):
    # Evaluate exp(-x/8) with alternating bounds, then take its eighth power.
    t, a = 1, 1
    for j in range(1, 33):
        t *= -x/(8*j)
        a += t
    return lower((a-t*x/(8*33))**8), upper(a**8)


def rational_interval(a, b, places=12):
    d = 10**places
    def fmt(n):
        sign = '-' if n < 0 else ''
        k = abs(n)
        return f'{sign}{k//d}.{k%d:0{places}d}'
    return [fmt((a*d).__floor__()), fmt((b*d).__ceil__())]


def quad(m, n):
    return m*m+m*n+n*n


def disk(bound):
    size = isqrt(2*bound)
    return {(m,n) for m in range(-size,size+1) for n in range(-size,size+1)
            if quad(m,n) <= bound}


def elementary_checks():
    # Rational polynomial identity in Q[r]/(r^2-9r+12), tested through its factors.
    # Represent each coefficient as a+b*r.
    def pairadd(x,y):
        return x[0]+y[0], x[1]+y[1]
    def mul(x,y):
        a,b = x
        c,d = y
        return a*c-12*b*d, a*d+b*c+9*b*d
    r, one = (0,1), (1,0)
    G = mul((-1,1),(-8,3))   # 1/u
    s = (-9,2)
    v_over_u = pairadd(one,(F(-4),F(3,2)))
    # Coefficients of P/u from 1/(2u)+(v/u)L1-L3.
    left = [pairadd(mul((F(1,2),0),G),pairadd(v_over_u,(-1,0))),
            pairadd((3,0),mul((-1,0),v_over_u)), (F(-3,2),0),(F(1,6),0)]
    r2 = mul(r,r)
    right = [mul(r2,s),pairadd(r2,mul((0,-2),s)),pairadd(s,(0,-2)),one]
    assert [mul((6,0),x) for x in left] == right
    assert mul(r,pairadd(mul(r,r),pairadd(mul((-9,0),r),(12,0)))) == (0,0)

    # Numerical witnesses in the bandlimited-majorant estimates are all rational.
    c, S = 2**17, 32
    assert (F(16,25)**4)/4 >= F(1,32)
    assert F(32*8*3**4,6) < 4096
    assert 100*(4+F(33,32))**4 <= c
    assert 4096*100*(1+F(33,128))**4/16 <= c
    assert 112*S < 2**12
    assert 16*S*8 + F(32*3**4*16,127*S) < 2**13
    assert (2+2**29)*2**32 < 2**62
    assert 2*(2**16+2**61) < 2**63


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path,
                        help='optional directory containing pinned build/ and verification/')
    args = parser.parse_args()
    if args.source_dir:
        for filename, expected in SOURCE.items():
            assert hashlib.sha256((args.source_dir/filename).read_bytes()).hexdigest() == expected
        result = subprocess.run([sys.executable,'-I','verification/check_certificate.py'],
                                cwd=args.source_dir, capture_output=True, check=True)
        assert result.stdout == result.stderr == b''
    elementary_checks()
    a,b = atan_box(5)
    c,d = atan_box(239)
    pi_lo, pi_hi = lower(16*a-4*d), upper(16*b-4*c)
    rt_lo, rt_hi = sqrt_box(F(3))
    beta_lo,beta_hi = lower(2/rt_hi),upper(2/rt_lo)
    u_lo = exp_negative(pi_hi*beta_hi)[0]
    u_hi = exp_negative(pi_lo*beta_lo)[1]
    assert 0 < u_lo <= u_hi < F(1,32)
    cut = 24
    powers_lo = [F(1)]
    powers_hi = [F(1)]
    for _ in range(cut):
        powers_lo.append(powers_lo[-1]*u_lo)
        powers_hi.append(powers_hi[-1]*u_hi)
    vectors = sorted(disk(cut)-{(0,0)})
    h0 = h1 = length0 = length1 = err0 = err1 = F(0)
    for m,n in vectors:
        i = quad(m,n)
        low,high = powers_lo[i],powers_hi[i]
        l0,l1 = sqrt_box(beta_lo*i)[0],sqrt_box(beta_hi*i)[1]
        h0 += low
        h1 += high
        length0 += l0*low
        length1 += l1*high
        err0 += (gcd(m,n)+beta_lo*i)*low
        err1 += (gcd(m,n)+beta_hi*i)*high
    # On shell t the population is <=16t, length <=2t, gcd+length^2 <=4t.
    # The ratio of consecutive t^2/32^t is at most 1/8.
    tail = F(64*8*(cut+1)**2, 7*32**(cut+1))
    h1 += tail
    length1 += tail
    err1 += tail
    A0,A1 = (1+h0)/2, (1+h1)/2
    r33a,r33b = sqrt_box(F(33))
    dl,du = (7-r33b)/8,(7-r33a)/8
    eps2 = F(1,32)
    # At R=2^70 and N>=pi R^2 the certified RHS is at least A/(1+1/(64 pi))+A-1.
    sharp_example = A0/(1+1/(64*pi_lo))+A0-1
    explicit_A = (1+dl)/2
    independent_example = explicit_A/(1+1/(64*pi_lo))+explicit_A-1
    assert independent_example > F(3,20) and sharp_example > F(3,20)
    slices=[]
    for n in (16,64,256,1024):
        points = disk(n)
        N = len(points)
        loss0,loss1 = F(0), F(0)
        for m,j in vectors:
            t = quad(m,j)
            loss = sum((x+m,y+j) not in points for x,y in points)
            loss0 += loss*powers_lo[t]
            loss1 += loss*powers_hi[t]
            c0 = 2*beta_lo*sqrt_box(F(n*t))[0]
            c1 = 2*beta_hi*sqrt_box(F(n*t))[1]
            assert max(loss-c0,c1-loss) <= gcd(m,j)+beta_lo*t
        loss1 += N*tail
        R0 = sqrt_box(beta_lo*n)[0]
        R1 = sqrt_box(beta_hi*n)[1]
        assert loss0 >= 2*R1*length1-err0 and loss1 <= 2*R0*length0+err0
        slices.append({"disk_parameter":n,"N":N,"R":rational_interval(R0,R1),
                       "N_times_energy_deficit":rational_interval(loss0,loss1),
                       "R_times_energy_deficit":rational_interval(R0*loss0/N,R1*loss1/N)})
    answer={"source_sha256":SOURCE, "shell_quadratic_form_cutoff":cut,
            "Gaussian_root_u":rational_interval(u_lo,u_hi),
            "Theta_minus_one":rational_interval(h0,h1),
            "sharp_hat_g_at_0":rational_interval(A0,A1),
            "sharp_g_at_0":rational_interval(1-A1,1-A0),
            "sharp_min_hat_g_on_radius_sqrt_1_over_32_enclosure":
                rational_interval(A0-pi_hi*eps2,A1),
            "optimal_cubic_energy_constant":rational_interval(dl,du),
            "coefficient_of_1_over_R":rational_interval(2*length0/pi_hi,2*length1/pi_lo),
            "necessary_denominator_perimeter_coefficient":rational_interval(2*length0/A1,2*length1/A0),
            "uniform_unnormalized_residual_upper_interval":rational_interval(err0,err1),
            "perimeter_denominator_constant":2**64,
            "R_2pow70_density_at_least_one_lower_bounds_rounded_down":{
                "source_sharp":rational_interval(sharp_example,sharp_example)[0],
                "source_free_cubic":rational_interval(independent_example,independent_example)[0]},
            "exact_disk_displacement_tests":len(vectors)*len(slices),
            "triangular_samples":slices}
    print(json.dumps(answer,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
