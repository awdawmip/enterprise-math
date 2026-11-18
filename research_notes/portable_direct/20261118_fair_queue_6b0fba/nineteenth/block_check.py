"""Rational certificates for periodic Ramanujan partial sums and their energies."""
import json
from fractions import Fraction as F
from itertools import accumulate
from functools import lru_cache
from math import gcd
from road_check import atan_inverse


def primes(s):
    n=s
    for p in range(2,s+1):
        if p*p>n:break
        if n%p==0:
            k=0
            while n%p==0:n//=p;k+=1
            yield p,k
    if n>1:yield n,1


@lru_cache(None)
def mu(s):
    f=list(primes(s))
    return 0 if any(k>1 for _,k in f) else (-1)**len(f)


@lru_cache(None)
def phi(s):
    n=s
    for p,_ in primes(s):n=n//p*(p-1)
    return n


@lru_cache(None)
def divisors(s):
    return [d for d in range(1,s+1) if s%d==0]


@lru_cache(None)
def ram_period(s):
    v=[0]
    for r in range(1,s+1):
        g=gcd(r,s)
        a=sum(d*mu(s//d) for d in divisors(g))
        h=s//g
        assert a*phi(h)==mu(h)*phi(s)
        v.append(v[-1]+a)
    assert s==1 or v[-1]==0
    return tuple(v)


def A(s,n):
    return n if s==1 else ram_period(s)[n%s]


SCALE=10**14

def record(I):
    lo,hi=I
    return [lo.numerator*SCALE//lo.denominator,-((-hi.numerator*SCALE)//hi.denominator)]


def period_energy(v,target=40000):
    # v[r] is the signed cumulative difference for n=r+1 modulo L.
    L=len(v);K=max(1,(target+L-1)//L); W=sum(x*x for x in v)
    lo=0;rounded=0
    for j in range(K):
        for r,x in enumerate(v,1):
            n=j*L+r
            a=(x*x*SCALE)//(n*n)
            lo+=a
            rounded+=int(a*(n*n)!=x*x*SCALE)
    # Each later L-block has W total numerator. Bound its decreasing weights by endpoints.
    lower=F(W,(K+1)*L*L)
    upper=F(W,L*L)*(F(1,K)+F(1,K*K))
    return (F(lo,SCALE)+lower,F(lo+rounded,SCALE)+upper),{
        'period':L,'period_sum_of_squares':W,'whole_blocks':K,'prefix_end':K*L,
        'rational_tail_interval':[str(lower),str(upper)]}


def log_series(y,n=24):
    t=(y-1)/(y+1);assert 0<=t<=F(1,3)
    cur=t;z=F(0)
    for j in range(n):z+=2*cur/(2*j+1);cur*=t*t
    return z,z+2*cur/((2*n+1)*(1-t*t))


def log_interval(x):
    a=0;x=F(x)
    while x>=2:x/=2;a+=1
    assert a>=0 and x>=1
    lo,hi=log_series(x);l2,h2=log_series(F(2))
    return lo+a*l2,hi+a*h2


def prime_constant():
    a,b=atan_inverse(5,10),atan_inverse(239,10)
    pi=(16*a[0]-4*b[1],16*a[1]-4*b[0])
    l,h=log_interval(2*pi[0])[0],log_interval(2*pi[1])[1]
    M=100000;hs=sum(SCALE//k for k in range(1,M+1))
    # H_M - ln(M+1) < gamma < H_M - ln M, with outward-rounded H_M.
    return l-F(hs+M,SCALE)+log_interval(M)[0],h-F(hs,SCALE)+log_interval(M+1)[1]


def C_m(m,T=12000):
    H=max(map(abs,ram_period(m)))
    lo=0;rounded=0
    for k in range(1,T+1):
        n=k*(k+1);w=A(m,k)**2*SCALE
        lo+=w//n
        rounded+=int(w%n!=0)
    row=[A(m,k)**2 for k in range(T+1,T+m+1)]
    mean=F(sum(row),m)
    P=max(abs(x) for x in accumulate(v-mean for v in row))
    center=mean/(T+1)
    error=P/((T+1)*(T+2))
    return F(lo,SCALE)+center-error,F(lo+rounded,SCALE)+center+error


def second_m(m,T=12000):
    H=max(map(abs,ram_period(m)))
    Abar=F(sum(A(m,k) for k in range(1,m+1)),m)
    assert Abar==-F(phi(m),2)
    P=max(abs(v) for shift in range(m) for v in accumulate(A(m,shift+j)-Abar for j in range(m)))
    lam=0
    ps=list(primes(m))
    if len(ps)==1:
        assert ps[0][1]==1
        lam=ps[0][0]
    loglam=log_interval(lam) if lam else (F(0),F(0))
    deriv=[F(0),F(0)]
    lin=[F(0),F(0)]
    for k in range(1,T+1):
        a=A(m,k);den=k*k*(k+1)**2
        u=a*a*(2*k+1)*SCALE
        deriv[0]+=u//den;deriv[1]-=(-u)//den
        w=a*SCALE;n=k*(k+1)
        lin[0]+=w//n;lin[1]-=(-w)//n
    assert max(lin[0]/SCALE-F(H,T+1),-loglam[1])<=min(lin[1]/SCALE+F(H,T+1),-loglam[0])
    Em,_=period_energy([A(m,k) for k in range(1,m+1)])
    D=(Em[0]+deriv[0]/(2*SCALE)-phi(m)*loglam[1],
       Em[1]+deriv[1]/(2*SCALE)+F(H*H,2*(T+1)**2)-phi(m)*loglam[0])
    bound=F(2,3)*H**2+2*H*abs(Abar)+4*H*P
    return D,bound


def main():
    prime_pairs=((5,7),(11,13),(19,23),(31,37),(101,103))
    mixed=((2,11,13),(3,19,23),(6,31,37),(15,101,103))
    constant=prime_constant()
    cs={m:C_m(m) for m in (2,3,6,15)}
    seconds={m:second_m(m) for m in cs}
    psi=atan_inverse(5,10);chi=atan_inverse(239,10)
    pi=(16*psi[0]-4*chi[1],16*psi[1]-4*chi[0])
    seconds[1]=((-F(1,2)-pi[1]**2/12,-F(1,2)-pi[0]**2/12),F(1,3))
    tests=[]
    for m,p,q in [*((1,p,q) for p,q in prime_pairs),*mixed]:
        assert gcd(m,p*q)==1 and mu(m)!=0 and phi(p)==p-1 and phi(q)==q-1
        d=q-p;K=p//d;assert 2*d<=p
        L=m*p*q
        am=ram_period(m)
        assert sum((am[r]-am[r-1])**2 for r in range(1,m+1))==m*phi(m)
        v=[];overlap=0;separated=0
        for n in range(1,L+1):
            i,j=n//p,n//q
            v.append(A(m*p,n)-A(m*q,n))
            assert A(m*p,n)==p*A(m,i)-A(m,n) and A(m*q,n)==q*A(m,j)-A(m,n)
            assert v[-1]==p*A(m,i)-q*A(m,j)
            if 1<=i<=K and n<(K+1)*p:
                if n<i*q:
                    assert j==i-1 and v[-1]==p*(A(m,i)-A(m,i-1))-d*A(m,i-1)
                    separated+=1
                else:
                    assert j==i and v[-1]==-d*A(m,i)
                    overlap+=1
        D,cert=period_energy(v)
        diag,dcert=period_energy([A(m*p,n) for n in range(1,m*p+1)])
        c=constant if m==1 else cs[m]
        dag=(diag[0]-p*c[1],diag[1]-p*c[0])
        Dm,second_bound=seconds[m]
        centered=(dag[0]-Dm[1],dag[1]-Dm[0])
        assert -second_bound/p<=centered[0]<=centered[1]<=second_bound/p
        if m==1:
            harmonic=d*sum(F(1,k) for k in range(1,K+1))
            assert harmonic-2*d<=D[0]<=D[1]<=harmonic+5*d
        logs=log_interval(F(p,d))
        tests.append({'m_p_q':[m,p,q],'D':record(D),'E_mp':record(diag),
            'E_mp_minus_pC':record(dag),'D_m_second_term':record(Dm),
            'p_times_E_mp_minus_pC_minus_Dm':record((p*centered[0],p*centered[1])),
            'uniform_second_remainder_coefficient_bound':str(second_bound),
            'D_over_phi_m_d_log_p_over_d':record(
                (D[0]/(phi(m)*d*logs[1]),D[1]/(phi(m)*d*logs[0]))),
            'D_tail_certificate':cert,'E_tail_certificate':dcert,
            'I_size':separated,'J_size':overlap,'prime_harmonic_bound':(
                [str(harmonic-2*d),str(harmonic+5*d)] if m==1 else None)})
    data={'unit':'10^-14 inclusive outward integer endpoints','C_log_2pi_minus_gamma':record(constant),
          'C_m':{str(m):record(v) for m,v in cs.items()},'cases':tests,
          'scope':'identities on each full period, with exact positive tail brackets; the finite ratios do not prove the asymptotic'}
    print(json.dumps(data,sort_keys=True,indent=1))


if __name__=='__main__':
    main()
