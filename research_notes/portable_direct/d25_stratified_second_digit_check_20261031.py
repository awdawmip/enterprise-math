"""D25 original 216: exact low/middle/high p-adic jet certificate.
AUTHOR-SIDE finite exact checks, not a native H0/B0 experiment.
"""
from math import comb


def primes_upto(n):
    composite = [False]*(n+1)
    out=[]
    for x in range(2,n+1):
        if not composite[x]:
            out.append(x)
            for y in range(x*x,n+1,x):
                composite[y]=True
    return out


def check(p):
    assert p>5 and p%6==1
    l=(p-1)//6; m=2*l; h=3*l; q=4*l
    M=p**3
    fact=[1]*(p+1)
    for n in range(1,p+1):fact[n]=(fact[n-1]*n)%M
    invfact=[1]*p
    invfact[p-1]=pow(fact[p-1],-1,M)
    for n in range(p-1,0,-1): invfact[n-1]=invfact[n]*n%M
    inv=[0]*p
    for n in range(1,p):inv[n]=fact[n-1]*invfact[n]%M
    harmonic=[0]*p; harmonic2=[0]*p
    for n in range(1,p):
        harmonic[n]=(harmonic[n-1]+inv[n])%M
        harmonic2[n]=(harmonic2[n-1]+inv[n]**2)%M
    def delta(N,n): return (harmonic[N]-harmonic[N-n])%M
    def delta2(N,n):return(harmonic2[N]-harmonic2[N-n])%M
    def binom(N,n):
        if n>N:return 0
        return fact[N]*invfact[n]*invfact[N-n]%M
    inv2=pow(2,-1,M); inv3=pow(3,-1,M)
    inv4=pow(4,-1,M); inv6=pow(6,-1,M); inv9=pow(9,-1,M)
    pow_inv2=[1]*(p+1)
    for n in range(1,p+1):pow_inv2[n]=pow_inv2[n-1]*inv2%M

    S=HA=A2=U0=U1=V0=0
    for n in range(m+1):
        w=6*n+1
        t=(-1 if n%2 else 1)*pow_inv2[n]*binom(h,n)*binom(m,n)*binom(q,n)%M
        kappa=(inv2*delta(h,n)+inv3*delta(m,n)+2*inv3*delta(q,n))%M
        lam=(inv4*delta2(h,n)+inv9*delta2(m,n)+4*inv9*delta2(q,n))%M
        S=(S+w*t)%M
        HA=(HA-w*t*kappa)%M
        A2=(A2+w*t*(kappa*kappa-lam)*inv2)%M
    for n in range(m+1,h+1):
        w=6*n+1;s=n-m-1
        u=(fact[m]*fact[s]*binom(h,n)*binom(q,n)*invfact[n]*pow_inv2[n]*inv3)%M
        defect=(inv2*delta(h,n)+2*inv3*delta(q,n)+inv3*(harmonic[m]-harmonic[s]))%M
        U0=(U0+w*u)%M
        U1=(U1+w*u*defect)%M
    for n in range(h+1,q+1):
        w=6*n+1;s=n-m-1;t=n-h-1
        v=((-1 if (h+m+n)%2 else 1)*fact[h]*fact[m]*fact[s]*fact[t]*binom(q,n)*invfact[n]**2*pow_inv2[n]*inv6)%M
        V0=(V0+w*v)%M

    # Direct original source recurrence through n=p-1.
    x=1
    A=x
    a_coeff=[1]
    for n in range(1,p):
        ratio=(2*n-1)*(3*n-2)*(3*n-1)*pow(36*n*n*n,-1,M)%M
        x=x*ratio%M
        a_coeff.append(x)
        A=(A+(6*n+1)*x)%M
    reconstruction=(S+p*(HA+U0)+p*p*(A2-U1+V0))%M
    assert reconstruction==A, (p,"third order failed",reconstruction,A)

    # Verify each individual coefficient against original recurrence, not only total.
    x=1
    for n in range(p):
        if n<=m:
            t=(-1 if n%2 else 1)*pow_inv2[n]*binom(h,n)*binom(m,n)*binom(q,n)%M
            kappa=(inv2*delta(h,n)+inv3*delta(m,n)+2*inv3*delta(q,n))%M
            lam=(inv4*delta2(h,n)+inv9*delta2(m,n)+4*inv9*delta2(q,n))%M
            y=t*(1-p*kappa+p*p*(kappa*kappa-lam)*inv2)%M
        elif n<=h:
            s=n-m-1
            u=fact[m]*fact[s]*binom(h,n)*binom(q,n)*invfact[n]*pow_inv2[n]*inv3%M
            defect=(inv2*delta(h,n)+2*inv3*delta(q,n)+inv3*(harmonic[m]-harmonic[s]))%M
            y=p*u*(1-p*defect)%M
        elif n<=q:
            s=n-m-1;t=n-h-1
            v=(-1 if (h+m+n)%2 else 1)*fact[h]*fact[m]*fact[s]*fact[t]*binom(q,n)*invfact[n]**2*pow_inv2[n]*inv6%M
            y=p*p*v%M
        else:y=0
        assert x==y,(p,"coefficient",n,x,y)
        if n<p-1:
            ratio=(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,M)%M
            x=x*ratio%M
    # E.2 is an independent original source, with distinct (-1)^n and endpoint.
    b=1; B=1; D0=a_coeff[0]-b
    for n in range(1,m+1):
        b=(-b*(3*n-2)**3*pow(27*n**3,-1,M))%M
        B=(B+(6*n+1)*b)%M
        D0=(D0+(6*n+1)*(a_coeff[n]-b))%M
    D1=sum((6*n+1)*a_coeff[n] for n in range(m+1,h+1))%M
    assert B==p%M,(p,"E2 theorem evaluation mismatch",B)
    # Independent original integer binomial coefficient witnesses at fixed anchors.
    if p in (13,19,37,43,67,157,373):
        for n in range(p):
            orig=comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,M)%M
            assert orig==a_coeff[n],(p,"binomial independent",n)
    first=(S-p+p*(HA+U0))%(p*p)
    if p%24 in (13,19):
        assert first==0,(p,"first digit",first)
        carry=((S-p+p*(HA+U0))%(p**3))//(p*p)
        low=(A2-U1+V0)%p
        residue=(carry+low)%p
        assert residue==((A-p)%(p**3))//(p*p), (p,"second residual",residue)
        assert (D0+D1)%(p*p)==0,(p,"D0D1 divisibility",D0,D1)
        bridge=((D0+D1)%M)//(p*p)
        assert bridge==(carry+A2-U1)%p,(p,"low middle 3-port",bridge)
        assert bridge==(-V0)%p,(p,"signed high port",bridge)
        return (p,carry,A2%p,(-U1)%p,V0%p,residue,bridge, A)
    return (p,)

if __name__=='__main__':
    pp=[p for p in primes_upto(5000) if p%6==1]
    rows=[]
    for p in pp:
        rows.append(check(p))
    target=[r for r in rows if len(r)>1]
    print('primes',len(rows),'target',len(target),'max',max(pp))
    print('examples')
    for r in target:
        if r[0] in [13,19,37,43,67,157,373]:print(r)
    print('nonzero-target-residuals',[(r[0],r[5]) for r in target if r[5]])
    print('PASS_D25_STRATIFIED_LOW_MID_HIGH_P3_JET_AND_CARRY_EXACT')
