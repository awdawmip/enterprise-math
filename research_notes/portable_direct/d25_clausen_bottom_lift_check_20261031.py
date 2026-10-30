"""Exact coefficient checks for the denominator-deformed terminating Clausen identity.

Portable author-side arithmetic only. No Source/native experiment claim.
"""
from math import comb, isqrt, factorial
from fractions import Fraction


def primes(n):
    out=[]
    for p in range(7,n+1):
        if all(p%q for q in range(2,isqrt(p)+1)):
            out.append(p)
    return out


def convolution(a,b,M):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b):
            c[i+j]=(c[i+j]+x*y)%M
    return c


def check_prime(p):
    assert p>5 and p%6==1
    l=(p-1)//6; N=2*l; M=p**3
    inv2=pow(2,-1,M); inv4=pow(4,-1,M); inv8=pow(8,-1,M)
    H=[0]*(N+1); H2=[0]*(N+1)
    for n in range(1,N+1):
        t=pow(n,-1,M)
        H[n]=(H[n-1]+t)%M
        H2[n]=(H2[n-1]+t*t)%M
    G=[comb(l,k)*comb(2*l,k)%M for k in range(l+1)]
    G1=[G[k]*H[k]%M for k in range(l+1)]
    G2=[G[k]*(H[k]**2+H2[k])%M for k in range(l+1)]
    c=convolution(G,G,M)
    d=convolution(G,G1,M)
    e1=convolution(G1,G1,M)
    e2=convolution(G,G2,M)
    e=[(x+y)*inv4%M for x,y in zip(e1,e2)]
    t=[((-1)**n)*comb(3*l,n)*comb(2*l,n)*comb(4*l,n)%M for n in range(N+1)]
    pred=[]
    for n in range(N+1):
        hn=H[n]; hn2=H2[n]
        val=(c[n]+p*(d[n]-3*inv2*hn*c[n])+p*p*(e[n]-3*inv2*hn*d[n]+inv8*(9*hn*hn-5*hn2)*c[n]))%M
        assert val==t[n],(p,n,val,t[n])
        pred.append(val)
    def w_eval(x):
        out=0; power=1
        for n,a in enumerate(x):
            out=(out+(6*n+1)*a*power)%M
            power=(power*inv2)%M
        return out
    Tg=w_eval(t)
    assert Tg==w_eval(pred)
    corollary=None
    if p%24 in (13,19):
        z=inv2
        g0=sum(G[k]*pow(z,k,M) for k in range(l+1))%M
        assert g0%p==0,(p,g0%p)
        dG=sum(k*G[k]*pow(z,k-1,M) for k in range(1,l+1))%M
        j0=sum(G1[k]*pow(z,k,M) for k in range(l+1))%M
        WK=sum((6*n+1)*c[n]*H[n]*pow(z,n,M) for n in range(N+1))%M
        assert Tg%p==0
        f=(6*(g0//p)*dG+3*dG*j0-3*inv2*WK)%p
        assert Tg//p%p==f,(p,Tg//p%p,f)
        corollary={"g_over_p_mod_p":g0//p%p,"Gprime_mod_p":dG%p,"G_harmonic_mod_p":j0%p,"weighted_H_G2_mod_p":WK%p,"first_digit":f}
    return {"p":p,"l":l,"weighted_T_mod_p3":Tg,"G_half_mod_p":sum(G[k]*pow(inv2,k,p) for k in range(l+1))%p,"cm_jet":corollary}


def check_rational_clausen(l):
    """Independent exact terminating 2F1^2 / 3F2 crosscheck over Q."""
    p=6*l+1
    g=[Fraction(comb(l,k)*comb(2*l,k))*Fraction(factorial(k),1) /
       (Fraction(1,1) if k==0 else __import__('math').prod(Fraction(j,1)-Fraction(p,2) for j in range(1,k+1)))
       for k in range(l+1)]
    left=[Fraction(0) for _ in range(2*l+1)]
    for i,a in enumerate(g):
        for j,b in enumerate(g):
            left[i+j]+=a*b
    for n in range(2*l+1):
        t=(-1)**n*comb(3*l,n)*comb(2*l,n)*comb(4*l,n)
        ratio=Fraction(1)
        for j in range(1,n+1):
            ratio*=Fraction(j*j,1)/(Fraction(j-p,1)*(Fraction(j,1)-Fraction(p,2)))
        assert left[n]==t*ratio,(l,n,left[n],t*ratio)


def main():
    for l in range(1,7): check_rational_clausen(l)
    ps=[p for p in primes(2400) if p%6==1]
    ans=[check_prime(p) for p in ps]
    targets=[r for r in ans if r['p']%24 in (13,19)]
    print('PASS_D25_CLAUSEN_DENOMINATOR_TWO_JET_COEFFICIENTWISE_EXACT',
          'primes',len(ps), 'coefficients',sum((p-1)//3+1 for p in ps),
          'cm_class',len(targets),'rational_exact_ell',6)
    for p in (7,13,19,37,157,373,1327,2377):
        if p<=2400 and p%6==1:
            print(check_prime(p))

if __name__=='__main__':main()
