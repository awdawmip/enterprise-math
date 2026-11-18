"""Gaussian Mellin signals, exact local pole constants, and an Eisenstein Euler check.

Python 3 and python-flint 0.9.0. Uses real Arb balls plus exact integers/fractions.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json
from flint import arb, ctx

ctx.prec = 256
PI = arb.pi()
A = arb(5)/6


def endpoint(x, digits, upper):
    n = x * 10**digits
    z = (n.upper().ceil() if upper else n.lower().floor()).unique_fmpz()
    z = int(z)
    return ("-" if z<0 else "")+str(abs(z)//10**digits)+"."+str(abs(z)%10**digits).zfill(digits)


def enclosure(x, digits=12):
    return [endpoint(x,digits,False),endpoint(x,digits,True)]


def peak_constants():
    # I_m / pi for I_m = integral_(R) (1+t^2)^(-m) dt.
    ratio = Q(1)
    out = []
    for m in range(1,13):
        coeff = 2**(2*m-2)*ratio
        assert coeff == comb(2*m-2,m-1)
        assert (factorial(2*m-2)/coeff)==factorial(m-1)**2
        out.append(int(coeff))
        ratio *= Q(2*m-1,2*m)
    return out


def model():
    q = 97
    b,h = arb(15)/16, arb(q).log()
    def phi(x):
        return ((A-b)*x-x*x/4).exp()/(2*PI.sqrt())
    def gamma(k):
        return 2*PI*k/h
    def time_profile(x):
        return sum(phi(x-n*h) for n in range(-16,17))
    def frequency_profile(x):
        y = ((b-A)**2).exp()
        for k in range(1,17):
            t = gamma(k)
            y += 2*((b-A)**2-t*t).exp()*(t*x+2*(b-A)*t).cos()
        return y/h
    points = []
    tolerance=arb(10)**-60
    for j in range(17):
        x = h*j/16
        y,z=time_profile(x),frequency_profile(x)
        # Bounds for omitted terms on [0,h]; |A-b|<1/4, 4<h<5.
        err=2*(-arb(2*16**2)).exp()/(1-(-arb(66)).exp())
        err+=2*(-arb(17**2)).exp()/(1-(-arb(35)).exp())
        assert abs(y-z)+err < tolerance
        if j in (0,5,11):
            points.append([j,enclosure(y+arb(0,"1e-200"))])
    def g(m,x):
        return sum(comb(n+m-1,m-1)*phi(x-n*h) for n in range(40))
    # (1 - backward shift)^m g_m = phi. Omitted tails for these x are <1e-200.
    samples=0
    for m in range(1,5):
        for j in range(-3,12):
            x=h*j/2
            actual=sum((-1)**i*comb(m,i)*g(m,x-i*h) for i in range(m+1))
            assert abs(actual-phi(x)) < tolerance
            samples+=1
    # Direct real Gaussian autocorrelation and spectral Parseval sum.
    fac=(2*(b-A)**2).exp()
    ac=fac*sum((-(j*h)**2/8).exp() for j in range(-16,17))/(2*(2*PI).sqrt()*h)
    spec=fac*sum((-2*gamma(k)**2).exp() for k in range(-16,17))/h**2
    assert abs(ac-spec)+4*(-arb(17**2)).exp() < tolerance
    mass={}
    for m in (1,2,3):
        val=comb(2*m-2,m-1)*spec/h**(2*m-2)
        # For all m here the omitted Fourier squared amplitudes sum to <1e-200.
        mass[str(m)] = enclosure(val+arb(0,"1e-200"))
    return {"q":q,"b":"15/16","samples_physical_and_spectral":17,
            "period_samples_u_over_h_equals_j_over_16":points,
            "backward_shift_checks":samples,"critical_energy_limits":mass}


def reciprocal_coeffs(N):
    # Actual ζ_F with all primes above 2 and 3 omitted: multiply finite inverse Euler factors.
    sieve=[True]*(N+1)
    for p in range(2,N+1):
        if not sieve[p]:
            continue
        for n in range(2*p,N+1,p):
            sieve[n]=False
    a=[0]*(N+1)
    a[1]=1
    for p in range(5,N+1):
        if not sieve[p]:
            continue
        factors=((-2,p),(1,p*p)) if p%3==1 else ((-1,p*p),)
        for n in range(N//p,0,-1):
            if a[n]:
                for coeff,m in factors:
                    if n*m<=N:
                        a[n*m]+=coeff*a[n]
    return a


def actual_euler():
    N=1024
    a=reciprocal_coeffs(N)
    assert [a[n] for n in (3,4,7,25,49,91)] == [0,0,-2,-1,1,4]
    checks=[]
    for k in (4,6):
        s=arb(k)
        l=(s.zeta(arb(1)/3)-s.zeta(arb(2)/3))/(arb(3)**s)
        exact=1/(s.zeta()*l*(1-arb(3)**(-s))*(1-arb(4)**(-s)))
        approx=sum(arb(a[n])/n**k for n in range(1,N+1))
        tail=2*arb(N)**(arb(3)/2-k)/(k-arb(3)/2)
        assert abs(exact-approx) < tail
        checks.append({"s":k,"reciprocal":enclosure(exact),"absolute_tail_bound":enclosure(tail,16)})
    normalized=-(arb(1)/36).exp()*6*arb(3).sqrt()/PI
    return {"field_discriminant":-3,"omitted_prime_norms":[3,4],"norm_cutoff":N,
            "right_half_plane_checks":checks,
            "Abel_log_moment_divided_by_H_at_1":enclosure(normalized)}


if __name__=="__main__":
    print(json.dumps({"plancherel_binomial_constants_m_1_through_12":peak_constants(),
                      "log_lattice_model":model(),"actual_principal_character":actual_euler()},indent=2))
