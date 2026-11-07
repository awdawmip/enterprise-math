"""CM-class p^2 unweighted vanishing; conditional exact signed Fricke jet regression."""
from math import isqrt

def prime(p): return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def check(p):
    q=p*p; a=b=1; A=J=B=K=0
    for n in range(p):
        if n:
            a=a*(2*n-1)*(3*n-2)*(3*n-1)*pow(36*n**3,-1,q)%q
            b=b*(4*n-3)*(2*n-1)*(4*n-1)*pow(288*n**3,-1,q)%q
        A=(A+a)%q; J=(J+n*a)%q
        B=(B+b)%q; K=(K+n*b)%q
    inert=p%24 in (13,17,19,23)
    target=p%24 in (13,19)
    both=(A==0 and B==0)
    assert both==inert,(p,A,B,inert)
    chi=1 if p%3==1 else -1
    assert (A+6*J-p*chi)%q==0 and (B+8*K-p*chi)%q==0,(p,A,J,B,K)
    if inert:
        assert J%p==K%p==0
        # E'(t_+) = (-2J+7B/8+4K) + s*(3J/2-5B/8-3K)
        ereal=(-2*J+7*B*pow(8,-1,q)+4*K)%q
        eimag=(3*J*pow(2,-1,q)-5*B*pow(8,-1,q)-3*K)%q
        expectreal=p*chi*pow(6,-1,q)%q
        expectimag=-p*chi*pow(8,-1,q)%q
        assert (ereal,eimag)==(expectreal,expectimag),(p,ereal,eimag,expectreal,expectimag)
    return (p,inert,target,A,B,J,K)

if __name__=='__main__':
    ps=[p for p in range(5,2000) if prime(p)]
    rows=[check(p) for p in ps]
    print('PASS',len(ps),'primes p<2000, 4 inert classes:',sum(x[1] for x in rows),
          '2 target classes:',sum(x[2] for x in rows))
    for p in (13,19,43,67,373):
        x=next(x for x in rows if x[0]==p)
        print(p,'A/p=',x[3]//p,'B/p=',x[4]//p,'J/p=',x[5]//p,'K/p=',x[6]//p)

# Completely independent factorial/binomial coefficient witness for selected primes.
if __name__=='__main__':
    from math import comb
    for p in (13, 19, 43, 67, 373):
        q = p*p
        AA=JJ=BB=KK=0
        t216=t2304=1
        for n in range(p):
            x=comb(2*n,n)**2*comb(3*n,n)*t216%q
            y=comb(4*n,2*n)*comb(2*n,n)**2*t2304%q
            AA=(AA+x)%q; JJ=(JJ+n*x)%q
            BB=(BB+y)%q; KK=(KK+n*y)%q
            t216=t216*pow(216,-1,q)%q
            t2304=t2304*pow(2304,-1,q)%q
        assert (AA,BB,JJ,KK)==check(p)[3:]
    print('Independent integer-binomial cross-check passed for 5 chosen primes')
