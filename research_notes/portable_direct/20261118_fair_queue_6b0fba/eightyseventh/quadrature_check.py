"""Verify the original moment brackets, finite comparisons, Poisson and Gamma constants."""
import argparse
from fractions import Fraction as Fr
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import runpy

import mpmath as mp

SOURCE_SHA = "f2614e3723fa44159433a1fdcd80c8cfd98647a8b3479a0d959e98da2cd0e34a"


def horner(poly,x):
    acc=0
    for c in reversed(poly):
        acc=acc*x+c
    return acc


def ratio(r,x):
    return horner(r[0],x)/horner(r[1],x)


def real(x):
    return mp.mpf(x.numerator)/x.denominator


def mpratio(row,z):
    return horner(list(map(real,row[0])),z)/horner(list(map(real,row[1])),z)


def moments(n):
    return [Fr(2*4**j,(j+1)**2*comb(2*j+2,j+1)) for j in range(n)]


def width_leading(lo,hi,n):
    def coeff(x,y):
        return sum(x[i]*y[2*n-i] for i in range(len(x)) if 0<=2*n-i<len(y))
    return coeff(hi[0],lo[1])-coeff(lo[0],hi[1])


def rational_checks(pairs):
    out=[]
    for n in (1,2,4,8,16,32):
        low,high=pairs[n]
        for t in [Fr(1,100),Fr(1,10),Fr(1,6)]:
            z=4*t/(1+t)**2
            invsqrt=(1+t)/(1-t)
            gap=ratio(high,z)-ratio(low,z)
            # 22/7 exceeds pi, so checking against this larger expression validates the mathematical lower bound too.
            stronger=Fr(22,7)*invsqrt*t**(2*n)*(1-t*t)**2/(8*(1-t**(2*n+2)))
            upper=4*invsqrt*t**(2*n)/(1-t)
            assert 0<stronger<gap<upper
            assert gap==z**(2*n)*width_leading(low,high,n)/(horner(low[1],z)*horner(high[1],z))
            out.append({"n":n,"t":str(t),"z":str(z),
                        "gap_scaled":mp.nstr(real(gap/t**(2*n)),14)})
    return out


def constant(z):
    t=z/(1+mp.sqrt(1-z))**2
    x=mp.acos(mp.sqrt(z))/(2*mp.pi)
    weight=2*mp.pi*mp.gamma(1-x)*mp.gamma(mp.mpf('.5')+x)/(mp.gamma(x)*mp.gamma(mp.mpf('.5')-x))
    return mp.pi*(1+t)**2*weight


def numerical_integral(z):
    # u=atanh(sin(theta/2)), with integrable log singularity at u=0.
    with mp.workdps(50):
        def integrand(u):
            ch=mp.cosh(u)
            return mp.sqrt(1-z)*ch/(ch*ch-z)*mp.log(u)
        J=2/mp.pi*mp.quad(integrand,[0,1,4,mp.inf])
        t=z/(1+mp.sqrt(1-z))**2
        return mp.pi*(1+t)**2*mp.exp(J)


def calibration(pairs,original):
    values={}
    for q in (2,4,16,64):
        a=4*mp.sin(mp.pi/(2*q))**2
        lo,hi=original["_first_mode"](q,300)
        assert real(lo)<=a+mp.eps*20 and a<=real(hi)+mp.eps*20
        z=a/4
        t=z/(1+mp.sqrt(1-z))**2
        C=constant(z)
        assert abs(numerical_integral(z)-C) < mp.mpf('1e-44')
        exact=mp.asin(mp.sqrt(z))**2/z
        rows=[]
        for n in (2,4,8,16,32,48):
            low,high=pairs[n]
            g=mpratio(low,z)
            l=mpratio(high,z)
            scaled=(l-g)/t**(2*n)
            # Avoid recursive subtraction: independently compute the exact numerator monomial, then evaluate.
            width=real(width_leading(low,high,n))*z**(2*n)/(horner(list(map(real,low[1])),z)*horner(list(map(real,high[1])),z))
            assert abs((l-g)/width-1)<mp.mpf('1e-50')
            assert g<exact<l
            rows.append({"n":n,"width_over_leading_equivalent":mp.nstr(scaled/C,15),
                         "lower_error_fraction":mp.nstr((exact-g)/(l-g),15)})
        values[q]={"C":mp.nstr(C,18),"rows":rows}
    z=mp.mpf(0)
    assert abs(constant(z) - 4*mp.pi**4/mp.gamma(mp.mpf(1)/4)**4)<mp.eps*100
    assert abs(constant(z)-numerical_integral(z))<mp.mpf('1e-44')
    return values


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",type=Path,default=Path(__file__).resolve().parents[1]/"twelfth"/"wallis_t5.py")
    p.add_argument("--out",type=Path)
    opts=p.parse_args()
    assert sha256(opts.source.read_bytes()).hexdigest()==SOURCE_SHA
    source=runpy.run_path(str(opts.source))
    assert source["phase_moments"](98)==moments(98)
    mp.mp.dps=480
    pairs={n:source["phase_moment_fractions"](n) for n in (1,2,4,8,16,32,48)}
    result={"source_sha256":SOURCE_SHA,"rational_finite_bounds":rational_checks(pairs),
            "native_radicals_and_two_independent_constants":calibration(pairs,source),
            "critical_C0":mp.nstr(constant(mp.mpf(0)),18),
            "mpmath":mp.__version__}
    out=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if opts.out: opts.out.write_text(out)
    else: print(out,end="")


if __name__=="__main__":
    main()
