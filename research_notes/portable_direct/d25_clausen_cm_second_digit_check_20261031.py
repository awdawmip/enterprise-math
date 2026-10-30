"""CM p^2 scalar observer of the terminating Clausen lower-denominator two-jet.

Independent direct finite t_n sum; reuses only the previous checked convolution/primes helpers.
"""
from math import comb
from d25_clausen_bottom_lift_check_20261031 import convolution, primes


def cm_observer(p):
    assert p % 24 in (13,19)
    l=(p-1)//6; N=2*l; M=p**3
    inv2=pow(2,-1,M); inv8=pow(8,-1,M)
    h=[0]*(N+1); h2=[0]*(N+1)
    for n in range(1,N+1):
        u=pow(n,-1,M)
        h[n]=(h[n-1]+u)%M
        h2[n]=(h2[n-1]+u*u)%M
    g=[comb(l,k)*comb(2*l,k)%M for k in range(l+1)]
    g1=[g[k]*h[k]%M for k in range(l+1)]
    g2=[g[k]*(h[k]*h[k]+h2[k])%M for k in range(l+1)]
    c=convolution(g,g,M)
    d=convolution(g,g1,M)
    g11=convolution(g1,g1,M)
    g02=convolution(g,g2,M)
    e=[((g11[n]+g02[n])*pow(4,-1,M)
         -3*inv2*h[n]*d[n]
         +inv8*(9*h[n]*h[n]-5*h2[n])*c[n])%M for n in range(N+1)]
    def ev(a,weight=False,deriv=False):
        result=0
        for n,v in enumerate(a):
            if deriv:
                if n==0: continue
                term=n*v*pow(inv2,n-1,M)
            else:
                term=v*pow(inv2,n,M)*(6*n+1 if weight else 1)
            result=(result+term)%M
        return result
    G=ev(g); assert G%p==0
    alpha=G//p
    dG=ev(g,deriv=True); J=ev(g1); dJ=ev(g1,deriv=True)
    WK=ev([c[n]*h[n]%M for n in range(N+1)],weight=True)
    WE=ev(e,weight=True)
    first=(6*alpha*dG+3*dG*J-3*inv2*WK)%(p*p)
    second=(alpha*alpha+alpha*J+3*alpha*dJ+WE)%p
    direct=[(-1)**n*comb(3*l,n)*comb(2*l,n)*comb(4*l,n)%M for n in range(N+1)]
    scalar=ev(direct,weight=True)
    assert scalar%p==0
    assert scalar//p%(p*p)==(first+p*second)%(p*p), (p,scalar//p,first,second)
    return p,scalar//p%(p*p),first,second,WE%p


def main():
    ps=[p for p in primes(2400) if p%24 in (13,19)]
    results=[cm_observer(p) for p in ps]
    print('PASS_D25_CLAUSEN_CM_SECOND_DIGIT_OBSERVER_EXACT',len(results),'target_class_primes')
    for p in (13,19,37,157,373):
        print(cm_observer(p))

if __name__=='__main__': main()
