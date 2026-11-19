"""Rational certificate for C83's improved high-precision constant bounds.

All reported bounds on the two-dimensional integrals use integer arithmetic.
Floating point supplies only an initial guess for an integer twentieth root;
the two inequalities defining that root are checked with integer powers.
"""
from argparse import ArgumentParser
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import json

PRECISION = 10**12
ROOT_PRECISION = 10**12
T0 = F(33,40)


def twentieth_root_bounds(num, den):
    if num == 0:
        return 0, 0
    q = int((num/den)**.05 * ROOT_PRECISION)
    target = num * ROOT_PRECISION**20
    while q**20 * den > target:
        q -= 1
    while (q+1)**20 * den <= target:
        q += 1
    assert q**20*den <= target < (q+1)**20*den
    return q, q+1


def radial_scaled(b, upper):
    """Outward bound for P* integral_0^1 r^2 min(r^.1*b,t0) dr."""
    p, q = T0.numerator, T0.denominator
    if b*q <= p*ROOT_PRECISION:
        num, den = 10*b*PRECISION, 31*ROOT_PRECISION
    else:
        power = b**30
        num = PRECISION*(31*p*q**30*power-p**31*ROOT_PRECISION**30)
        den = 93*q**31*power
    return (num+den-1)//den if upper else num//den


def area_numerator(a,b,c):
    """Twice N^2 times area, with a=R0*N,b=R2*N,c=2R1*N."""
    if c >= a+b:
        return 4*a*b
    if c <= abs(a-b):
        return 4*c*min(a,b)
    return 4*a*b-(a+b-c)**2


def face_bounds(n, face):
    # The integrand is separately concave. Tensor trapezoids give lower
    # bounds, tensor midpoints give upper bounds. x_i=(i/n)^4 resolves the
    # weak twentieth-root singularity at the coordinate axes.
    power=[i**4 for i in range(n+1)]
    delta=[power[i+1]-power[i] for i in range(n)]
    weights=[delta[0]]+[delta[i-1]+delta[i] for i in range(1,n)]+[delta[-1]]
    m=n**4
    lower=upper=0
    for i in range(n+1):
        for j in range(n+1):
            area=(area_numerator(m,power[j],2*power[i]) if face==0
                  else area_numerator(power[i],power[j],2*m))
            lo,_=twentieth_root_bounds(area,32*m*m)
            lower+=weights[i]*weights[j]*radial_scaled(lo,False)
    for i in range(n):
        for j in range(n):
            a,b=power[i]+power[i+1],power[j]+power[j+1]
            area=(area_numerator(2*m,b,2*a) if face==0
                  else area_numerator(a,b,4*m))
            _,hi=twentieth_root_bounds(area,128*m*m)
            upper+=delta[i]*delta[j]*radial_scaled(hi,True)
    return F(lower,4*PRECISION*m*m),F(upper,PRECISION*m*m)


def arctan_bounds(q,n=64):
    s=sum(((-1)**i*F(1,(2*i+1)*q**(2*i+1)) for i in range(n)),F())
    term=F(1,(2*n+1)*q**(2*n+1))
    return (s,s+term) if n%2==0 else (s-term,s)


def gamma_quarter_bounds():
    # Gamma(1/4)=4 integral_0^infinity exp(-u^4) du.
    # Odd/even Taylor polynomials enclose exp(-z) for every z>=0.
    # At u>=3 the tail is <= exp(-81)/27 < (3/8)^81/27.
    term=F(3);s=term;even=None
    for j in range(1,402):
        term*=-F(81,j)*F(4*j-3,4*j+1)
        s+=term
        if j==400:even=4*s
    return 4*s,even+F(3,8)**81/27


def prefactor_bounds():
    glo,ghi=gamma_quarter_bounds()
    def twentieth_power(g):
        return F(160,39)**20*F(8,4725)*(F(5,50176*108)*g)**2
    qlo=twentieth_power(glo);qhi=twentieth_power(ghi)
    lo,_=twentieth_root_bounds(qlo.numerator,qlo.denominator)
    _,hi=twentieth_root_bounds(qhi.numerator,qhi.denominator)
    return F(lo,ROOT_PRECISION),F(hi,ROOT_PRECISION)


def calculate(n):
    started=perf_counter()
    f0=face_bounds(n,0)
    f1=face_bounds(n,1)
    lo,hi=2*f0[0]+f1[0],2*f0[1]+f1[1]
    # Exact elementary remainder: (40/19)*k*2^(-1/20)-2*k*t0.
    # Rational pi and root bounds give a wholly rational final lower bound.
    pi_lower=F(314159265358979323846264338327950288419716939937510,10**50)
    pi_upper=pi_lower+F(1,10**50)
    a,b=arctan_bounds(5),arctan_bounds(239)
    assert pi_lower < 16*a[0]-4*b[1] < 16*a[1]-4*b[0] < pi_upper
    k_lower=F(161,80)/pi_upper**2
    k_upper=F(161,80)/pi_lower**2
    tlo,thi=twentieth_root_bounds(1,2)
    coefficient_lo=F(40,19)*F(tlo,ROOT_PRECISION)-2*T0
    coefficient_hi=F(40,19)*F(thi,ROOT_PRECISION)-2*T0
    assert coefficient_lo>0
    lb=lo+k_lower*coefficient_lo
    ub=hi+k_upper*coefficient_hi
    pref_lo,pref_hi=prefactor_bounds()
    # F3(a)>=(8/15)*a^(3/2) for a<=1/4. Split at a=43/200.
    split=F(43,200)
    slo,shi=twentieth_root_bounds(split.numerator,split.denominator)
    slo,shi=F(slo,ROOT_PRECISION),F(shi,ROOT_PRECISION)
    i_upper=shi-F(8,15)*slo**31/31+k_upper*slo**(-19)/19
    a_lower,a_upper=pref_lo*lb,pref_hi*i_upper
    # Exact large-a portion of the two-versus-three-readings difference.
    gap_lower=pref_lo*F(49,760)/pi_upper**2*F(tlo,ROOT_PRECISION)
    assert a_lower>F(73486,100000)
    assert a_upper<F(820351,1000000)
    return {'grid':n,'grid_nodes':'x_i=(i/n)^4; separate concavity gives tensor trapezoid/midpoint enclosures',
      't0':str(T0),'root_precision':ROOT_PRECISION,
      'integrand_rounding_precision':PRECISION,
      'capped_minkowski_moment':{'lower':str(lo),'upper':str(hi)},
      'pi_interval':[str(pi_lower),str(pi_upper)],
      'improved_I3_lower_bound_expression':{
        'lower':str(lb),'upper':str(ub),'lower_float':float(lb),'upper_float':float(ub)},
      'high_precision_prefactor':{'lower':str(pref_lo),'upper':str(pref_hi)},
      'improved_A3_lower_bound':{'exact':str(pref_lo*lb),'display':float(pref_lo*lb)},
      'I3_enclosure':{'lower':str(lb),'upper':str(i_upper),
                      'display':[float(lb),float(i_upper)]},
      'A3_enclosure':{'lower':str(a_lower),'upper':str(a_upper),
                      'display':[float(a_lower),float(a_upper)],
                      'short_outward_interval':['0.73486','0.820351']},
      'outer_endpoint_leading_constant_gap_lower':{'exact':str(gap_lower),'display':float(gap_lower)},
      'elementary_constant_certificates':{'pi':'Machin arctangent, 64 alternating terms each',
        'Gamma_1_4':'exp(-u^4) Taylor bounds of degrees 400 and 401 on [0,3], plus tail <(3/8)^81/27'},
      'meaning':'The exact improved lower-bound expression lies in this interval; I3 is at least its lower endpoint.',
      'elapsed_seconds':perf_counter()-started}


if __name__=='__main__':
    p=ArgumentParser();p.add_argument('--grid',type=int,default=512)
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('constant_certificate.json'))
    args=p.parse_args();out=calculate(args.grid)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
