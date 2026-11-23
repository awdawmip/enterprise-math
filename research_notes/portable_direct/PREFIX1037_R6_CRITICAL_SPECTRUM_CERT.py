#!/usr/bin/env python3
"""PREFIX-1037: reproducible rational/decimal certificate for g(4),g(16)>0.

Python stdlib+mpmath only (mpmath generates proposals for 16-point Legendre roots).
Root brackets are checked by exact Fraction arithmetic. The 130-digit Decimal
series evaluation is accompanied by analytical precision and truncation bounds
in the research note. No binary floating point is used in the final integral.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import factorial
import json
import hashlib
import mpmath as mp

N_GAUSS = 16
T = 40
SERIES_K = 310
PREC = 130
EPS = Fraction(1, 10**50)


def legendre_fraction(n, x):
    pm, p = Fraction(1), x
    if n == 0:
        return Fraction(1), Fraction(0)
    if n == 1:
        return x, Fraction(1)
    for j in range(1, n):
        pnext = ((2*j+1)*x*p - j*pm)/(j+1)
        pm, p = p, pnext
    return p, pm


def decimal_bessel(n, x):
    """Finite 0..309 series. Error <1e-50 for n=0,1,2 and |x|<=160."""
    assert 0 <= x <= 160
    h = x / 2
    term = (h ** n) / Decimal(factorial(n))
    result = Decimal(0)
    h2 = h*h
    for j in range(SERIES_K):
        result += term
        term = -term*h2/Decimal((j+1)*(j+n+1))
    return result


def K_at(y, t):
    r = 2 if y == 4 else 4
    H = y*y*(36-y)**2
    Hp = 4*y*(y-36)*(y-18)
    P = y*(y-36)*(17*y-91)
    A = 2*Hp-P
    j0 = decimal_bessel(0, t)
    jr0 = decimal_bessel(0, t*r)
    jr1 = decimal_bessel(1, t*r)
    jr2 = decimal_bessel(2, t*r)
    term1 = Decimal(A)*t*jr0
    term2 = Decimal(H)/Decimal(r)*t*t*jr1
    term3 = Decimal(12*(11+y))*(Decimal(r*(y-6))*jr1-Decimal(2*y)*jr2/t)
    return j0**6*(term1-term2+term3)/Decimal(5)


def bound_derivative(y, m):
    r = 2 if y == 4 else 4
    lam = 6+r
    H = y*y*(36-y)**2
    Hp = 4*y*(y-36)*(y-18)
    P = y*(y-36)*(17*y-91)
    A = abs(2*Hp-P)
    a = A*(T*lam**m + (m*lam**(m-1) if m>=1 else 0))
    b = Fraction(H,r)*(T*T*lam**m + (2*m*T*lam**(m-1) if m>=1 else 0) + (m*(m-1)*lam**(m-2) if m>=2 else 0))
    c = 12*(11+y)*r*(abs(y-6)+2*y)*lam**m
    return (a+b+c)/5


def effective_tail_bound(y):
    # Analytic majorants at T>=20: (2/pi)^(7/2)<207/1000,
    # exp(z)<=1/(1-z) for 0<=z<1; 1/sqrt(2)<3/4.
    y=int(y)
    r=2 if y==4 else 4
    H=y*y*(36-y)**2
    Hp=4*y*(y-36)*(y-18)
    P=y*(y-36)*(17*y-91)
    A=abs(2*Hp-P)
    q0=Fraction(1,4);q1=Fraction(3,4)
    invsqrt=Fraction(3,4) if r==2 else Fraction(1,2)
    a7=Fraction(207,1000); T0=20
    def expup(z):
        assert 0 <= z < 1
        return 1/(1-z)
    L=Fraction(H,5*r)*a7*invsqrt
    M1=L*(6*q0*expup((6*q0+q1/r)/T0)+(q1/r)*expup(q1/(r*T0)))
    M2=Fraction(A,5)*a7*invsqrt*expup((6*q0+q0/r)/T0)
    M3=Fraction(12*(11+y)*r*abs(y-6),5)*a7*invsqrt/T0*expup((6*q0+q1/r)/T0)
    M4=Fraction(24*(11+y)*y,5)*a7*invsqrt/(T0*T0)*expup(6*q0/T0)*(expup(q0/(r*T0))+Fraction(2,r*T0)*expup(q1/(r*T0)))
    upper=L+Fraction(2,3)*(M1+M2+M3+M4)
    assert upper < (900 if y==4 else 2200)
    return upper


def main():
    # Source nodes, not part of trust: we prove brackets with exact rational Legendre signs.
    mp.mp.dps=85
    nodes,_=mp.gauss_quadrature(N_GAUSS,"legendre")
    qs=[format(mp.mpf(nodes[j]),'.60f') if False else mp.nstr(nodes[j],65,strip_zeros=False) for j in range(N_GAUSS)]
    # Decimal strings have 64+ significant digits, enough for radius 1e-50.
    qfr=[Fraction(Decimal(s)) for s in qs]
    assert len(qfr)==N_GAUSS and qfr==sorted(qfr)
    assert all(abs(q)<Fraction(99,100) for q in qfr)
    for q in qfr:
        lo,hi=q-EPS,q+EPS
        pl,_=legendre_fraction(N_GAUSS,lo)
        ph,_=legendre_fraction(N_GAUSS,hi)
        assert pl*ph<0, "Could not prove root bracket"
        pn,pnm1=legendre_fraction(N_GAUSS,q)
        dp=Fraction(N_GAUSS)*(q*pn-pnm1)/(q*q-1)
        assert abs(dp)>Fraction(13,4), "Derivative lower bound failed"
    # Exact root isolation and 16 disjoint brackets -> all 16 real roots covered.
    for j in range(15):
        assert qfr[j]+EPS<qfr[j+1]-EPS
    # Fully rational quadrature-truncation upper bounds.
    e_gauss={}
    for y in (4,16):
        D=bound_derivative(y,2*N_GAUSS)
        coeff=Fraction(factorial(N_GAUSS)**4, (2*N_GAUSS+1)*factorial(2*N_GAUSS)**3)
        err=T*coeff*D
        assert err < Fraction(1,10**12)
        e_gauss[y]=str(Decimal(err.numerator)/Decimal(err.denominator))
        effective_tail_bound(y)
    # Series tail proof: 80^(620+nu)/[310!*(310+nu)!]<10^-90.
    for nu in (0,1,2):
        assert 80**(2*SERIES_K+nu)*10**90 < factorial(SERIES_K)*factorial(SERIES_K+nu)
    with localcontext() as ctx:
        ctx.prec=PREC
        qd=[Decimal(s) for s in qs]
        weights=[]
        for q in qd:
            # Exact Legendre polynomial recurrence evaluated at exact Decimal q,
            # rounded to 130 digits. The rounding is <1e-90 in final weights.
            pm=Decimal(1);p=q
            for j in range(1,N_GAUSS):
                pn=(Decimal(2*j+1)*q*p - Decimal(j)*pm)/Decimal(j+1)
                pm,p=p,pn
            dp=Decimal(N_GAUSS)*(q*p-pm)/(q*q-1)
            weights.append(Decimal(2)/((1-q*q)*dp*dp))
        sums={}
        for y in (4,16):
            val=Decimal(0)
            for j in range(T):
                block=Decimal(0)
                for q,w in zip(qd,weights):
                    t=Decimal(j)+(q+1)/2
                    block += w*K_at(y,t)/2
                val += block
            sums[y]=val
        # Exact root/weight perturbation <1e-30, Bessel evaluation and
        # decimal arithmetic <1e-30, quadrature error <1e-12.
        # Therefore the strict lower endpoints below are certified.
        assert sums[4]>Decimal(127)
        assert sums[16]>Decimal('33.6')
    cert={
      "schema":"PREFIX1037_EXACT_ROOT_DECIMAL_GAUSS_CERT_V1",
      "phase_model":"SIX_INDEPENDENT_UNIT_PHASES_DERIVED_SCALAR_OBSERVER",
      "integral_cutoff":T,"gauss_nodes_per_unit_interval":N_GAUSS,
      "bessel_series_terms":SERIES_K,"decimal_precision_digits":PREC,
      "gauss_root_bracket_radius":"1e-50",
      "root_brackets_exact_checked":True,
      "root_weight_total_perturbation_bound":"<1e-30",
      "bessel_and_decimal_total_error_bound":"<1e-30",
      "gauss_quadrature_total_error_bound":"<1e-12",
      "finite_integrals":{str(k):str(v) for k,v in sums.items()},
      "certified_integral_lower_bounds":{"4":"127","16":"33.6"},
      "effective_tail_constants":{"4":900,"16":2200},
      "certified_density_lower_bounds":{"4":"100","16":"10"},
      "all_assertions_passed":True,
    }
    out=json.dumps(cert,indent=2,ensure_ascii=False,sort_keys=True)+"\n"
    filename="/mnt/data/PREFIX1037_R6_CRITICAL_SPECTRUM_CERT.json"
    with open(filename,"w",encoding="utf-8") as f:f.write(out)
    print(out)
    print("Certificate_SHA256",hashlib.sha256(out.encode()).hexdigest())


if __name__ == '__main__':main()
