"""p^3 Gauss 3-band jet and signed Clausen residual: exact stdlib checker."""
from math import comb, isqrt

def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

def run(p):
    assert p>3 and p%6==1 and prime(p)
    m=(p-1)//6; q=p**3; q2=p*p
    inv2=pow(2,-1,q)
    fac=[1]*p
    for k in range(1,p):fac[k]=fac[k-1]*k%q
    invfac=[pow(a,-1,q) for a in fac]
    H=[0]*(2*m+1); H2=[0]*(2*m+1)
    for i in range(1,2*m+1):
        H[i]=(H[i-1]+pow(i,-1,q))%q
        H2[i]=(H2[i-1]+pow(i,-2,p))%p
    def hh(n,k):return (H[n]-H[n-k])%q
    def hh2(n,k):return (H2[n]-H2[n-k])%p
    inv6=pow(6,-1,q); inv3=pow(3,-1,q)
    inv36=pow(36,-1,p); inv9=pow(9,-1,p); invtwo=pow(2,-1,p)
    A0=A1=A2=E0=E1=0
    A2low=A2mid=A2high=0
    coeff_low=[]; coeff_mid=[]; coeff_high=[]
    for k in range(p):
        zk=pow(inv2,k,q)
        if k<=m:
            d=(comb(m,k)*comb(2*m,k)*zk)%q
            delta=(-hh(m,k)*inv6-hh(2*m,k)*inv3)%q
            sig=(hh2(m,k)*inv36+hh2(2*m,k)*inv9)%p
            eta=((delta%p)**2-sig)*invtwo%p
            A0=(A0+d)%q
            A1=(A1+d*delta)%q2
            A2=(A2+d*eta)%p
            A2low=(A2low+d*eta)%p
            E0=(E0+(12*k+1)*d)%q2
            E1=(E1+(12*k+1)*d*delta)%p
            coeff_low.append((d,delta,eta))
        elif k<=2*m:
            b=(((-1)**(m+k))*fac[m]*fac[k-m-1]*fac[2*m]*inv6
                *invfac[2*m-k]*invfac[k]**2*zk)%q
            lam=((H[k-m-1]-H[m])*inv6-hh(2*m,k)*inv3)%q
            A1=(A1+b)%q2
            A2=(A2+b*lam)%p
            A2mid=(A2mid+b*lam)%p
            E1=(E1+(12*k+1)*b)%p
            coeff_mid.append((b,lam))
        else:
            c=(((-1)**m)*fac[m]*fac[2*m]*fac[k-m-1]*fac[k-2*m-1]
                *pow(18,-1,q)*invfac[k]**2*zk)%q
            A2=(A2+c)%p
            A2high=(A2high+c)%p
            coeff_high.append(c)
    u=1; F=E=0; uf=[]
    w=1; W=0
    for k in range(p):
        scaled=u*pow(inv2,k,q)%q
        F=(F+scaled)%q
        E=(E+(12*k+1)*scaled)%q
        uf.append(scaled)
        W=(W+(6*k+1)*w)%q
        if k<p-1:
            u=u*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,q)%q
            w=w*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,q)%q
    for k,(d,delta,eta) in enumerate(coeff_low):
        assert uf[k]==(d+p*d*delta+p*p*d*eta)%q,(p,k,'low')
    for idx,(b,lam) in enumerate(coeff_mid):
        k=idx+m+1
        assert uf[k]==(p*b+p*p*b*lam)%q,(p,k,'mid')
    for idx,c in enumerate(coeff_high):
        k=idx+2*m+1
        assert uf[k]==p*p*c%q,(p,k,'high')
    assert A2==(A2low+A2mid+A2high)%p
    assert F==(A0+p*A1+p*p*A2)%q
    assert E%q2==(E0+p*E1)%q2
    h=pow(10,-1,p)
    power2=1; alpha=beta=0; K=0
    for i in range(1,m+1):
        power2=power2*2%p
        alpha=(alpha+h*power2)%p
        beta=(beta+i*h*power2)%p
        K=(K+uf[i]*((6*i+1)*alpha-6*beta))%p
        if i<m:
            h=h*18*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
    assert (F*E-p*p*K)%q==W,(p,'signed',K,F,E,W)
    if A0%p==0:
        quotient=(A0//p+A1+p*A2)%q2
        transfer=(quotient*(E0+p*E1)-p*K)%q2
        assert transfer==(W//p)%q2,(p,'third-digit')
        return (p,A0//p%p,A1%p,A2,A2low,A2mid,A2high,E0%p,E1,K,W//p%q2)
    return (p,None,A1%p,A2,A2low,A2mid,A2high,E0%p,E1,K,None)

if __name__=='__main__':
    vals=[run(p) for p in range(7,2000) if p%6==1 and prime(p)]
    assert len(vals)==148
    target=[x for x in vals if x[0]%24 in (13,19)]
    assert len(target)==77
    assert all(x[-1]==1 for x in target)
    extra=run(5113)
    print('PASS',len(vals),'primes <=1999 + 5113; target77 W/p=1 modp²')
    for row in vals+[extra]:
        if row[0] in (13,19,31,67,373,5113):print(row)
