"""Finite arithmetic check for the P022 midpoint moment and its first-order transport."""
import json
from fractions import Fraction
from math import comb, isqrt


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def franel(stop, mod):
    f = [1,2]
    for j in range(1, stop):
        f.append(((7*j*j+7*j+2)*f[-1]+8*j*j*f[-2])*pow(j+1,-2,mod)%mod)
    return f[:stop+1]


def half_moment(p):
    m, N = (p-1)//2, (p-1)//4
    square_weight, total = 1, 0
    for i in range((N-1)//2+1):
        total = (total + square_weight*(pow(8*i+1,-1,p)+pow(8*i+3,-1,p)))%p
        square_weight = square_weight*(2*i+1)**2*pow(2*i+2,-2,p)%p
    return 3*pow(2,m+1,p)*total%p


def whipple_quotient(p, f_n):
    k,n = (p+1)//6,(p-2)//3
    mod = p*p
    third, five_sixths = pow(3,-1,mod),5*pow(6,-1,mod)%mod
    term, base, harmonic, correction = 1,0,0,0
    for j in range(k):
        base = (base+term)%mod
        correction = (correction+term*harmonic)%p
        if j+1 < k:
            harmonic = (harmonic+pow(j+third,-1,p)-pow(j+five_sixths,-1,p))%p
            term = term*(j+third)**2*(j+five_sixths)*pow(j+1,-3,mod)%mod
    correction = correction*pow(6,-1,p)%p
    assert (base+p*correction)%mod == f_n*pow(2,-n,mod)%mod
    return base, correction


def owner_midpoint(p, midpoint_quotient):
    m, mod = (p-1)//2, p*p
    value, scalar, harmonic, U = 1,0,0,0
    for j in range(m+1):
        scalar = (scalar+value)%mod
        U = (U+value*harmonic)%p
        if j<m:
            harmonic = (harmonic+pow(j+1,-1,p))%p
            value = -value*(2*j+1)**3*pow(2*j+2,-3,mod)%mod
    assert scalar == 0 and 2*midpoint_quotient%p == -3*U%p


def transfer(p, max_d, f):
    """Compare J(p), its first jet, and an independent backward rational matrix."""
    m, mod = (p-1)//2,p*p
    old, J, slope_old, slope = 0,1,0,0
    P_old, P = 0,1   # J evaluated at X=p
    D = 1
    # L(0) multiplies F_m; G(0) multiplies F_(m-1).
    l_old, l, g_old, g = 1,0,0,1
    rows=[]
    for d in range(1,max_d+1):
        assert (P-J-p*slope)%mod == 0
        assert J%p == D*g%p
        lhs = f[m-d]%p
        assert lhs == g*f[m-1]%p
        if lhs==0:
            assert P%p == J%p == g%p == 0 and l%p
            assert f[m-d]%p == 0 and f[m]%p == 0 and f[m-1]%p
            norm = (J//p+slope)%p
            Fjet = f[m-d]//p
            Mjet = f[m]//p
            delta = f[m-1]*norm*pow(D,-1,p)%p
            assert Fjet == (l*Mjet+delta)%p
            rows.append(dict(p=p,d=d,diagonal=(d==(p+1)//6),Fjet=Fjet,
                             Mjet=Mjet,l=l,delta=delta,K_signed_over_p=J//p,
                             tangent=slope,normalized_offset=norm))
        a,b=-(28*d*d+1),8*(2*d-1)**4
        slope_old,slope=slope,(a*slope+b*slope_old+28*d*J-32*(2*d-1)**3*old)%p
        old,J=J,(a*J+b*old)%mod
        P_old,P = P, (-(7*(p-2*d)**2+1)*P+8*(p-2*d+1)**4*P_old)%mod
        D=D*8*(2*d+1)**2%p
        inv=pow(8*(2*d+1)**2,-1,p)
        l_old,l=l,((2*d-1)**2*l_old+a*l)*inv%p
        g_old,g=g,((2*d-1)**2*g_old+a*g)*inv%p
    return rows


def integral_check(N):
    # Coefficients of P_N from the explicit monomial expansion.
    coeff={N-2*j:Fraction((-1)**j*comb(N,j)*comb(2*N-2*j,N),2**N)
           for j in range(N//2+1)}
    lhs=sum(cx*cy/Fraction(x+y) for x,cx in coeff.items() for y,cy in coeff.items())
    rhs=sum(Fraction(comb(2*i,i)**2,16**i)*(Fraction(1,N-2*i)-Fraction(1,N+2*i+1))
            for i in range((N-1)//2+1))
    assert lhs==rhs
    return str(lhs)


if __name__ == "__main__":
    counts=dict(forced_primes=0, diagonal_sector_primes=0, diagonal_Hasse_hits=0,
                midpoint_jet_zeros=0,forced_window_zero_pairs=0)
    spectrum={}
    examples={}
    for p in range(5,1500,2):
        if not prime(p) or p%8 not in (5,7):
            continue
        m=(p-1)//2
        f=franel(m,p*p)
        assert f[m]%p == 0 and f[m-1]%p
        if p<50:
            assert all(f[j]==sum(comb(j,i)**3 for i in range(j+1))%(p*p) for j in range(m+1))
        q=f[m]//p
        counts['forced_primes']+=1
        counts['midpoint_jet_zeros']+=int(q==0)
        assert q==half_moment(p)
        owner_midpoint(p,q)
        if p%6==5:
            k=(p+1)//6
            counts['diagonal_sector_primes']+=1
            base, correction=whipple_quotient(p,f[2*k-1])
            counts['diagonal_Hasse_hits']+=int(base%p==0)
        rows=transfer(p,m-1,f)
        counts['forced_window_zero_pairs']+=len(rows)
        for row in rows:
            key='F{}_M{}_offset{}'.format(int(row['Fjet']!=0),int(row['Mjet']!=0),
                                         int(row['delta']!=0))
            spectrum[key]=spectrum.get(key,0)+1
            examples.setdefault(key,row)
    moments={N:integral_check(N) for N in range(1,20,2)}
    print(json.dumps(dict(prime_bound_exclusive=1500,counts=counts,off_diagonal_types=spectrum,
                          first_examples=examples,exact_rational_moments=moments),indent=2))
