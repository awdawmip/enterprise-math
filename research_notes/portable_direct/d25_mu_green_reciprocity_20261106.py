"""D25 integer checks: gamma reflection, M/U Green port, signed moment."""
from math import comb, isqrt

def gamma(k): return comb(2*k,k)**2 * comb(3*k,k)

def remove_p(x,p):
    v=0
    while x%p==0: x//=p;v+=1
    return v,x%p

def verify(p):
    m=(p-1)//6; P=p**3
    b=[1]*p
    for n in range(1,p):
        b[n]=b[n-1]*6*(6*n-5)*(3*n-2)*pow(n*n,-1,P)%P
    h=[None]*(4*m+1)
    h[1]=(0,pow(24,-1,p))
    for r in range(1,4*m):
        x,y=remove_p(r*r*(6*r+1),p),remove_p((r+1)*(2*r+1)*(3*r+2),p)
        h[r+1]=(h[r][0]+x[0]-y[0],h[r][1]*x[1]*pow(y[1],-1,p)%p)
    M=U=0
    for k in range(1,3*m+1):
        prod=gamma(k)*gamma(p-k)
        assert prod%P==0
        assert prod//P%p==(-12 if k<=2*m else 6)*pow(k,-3,p)%p
    for k in range(2*m+1,3*m+1):
        r=p-k;g=gamma(k)
        assert g%p==0 and b[r]%(p*p)==0 and h[r][0]==0
        actual=(g//p)*(b[r]//(p*p))%p
        assert actual==72*pow(k,-1,p)*h[r][1]%p
        M=(M+k*actual)%p
    for r in range(1,m+1):
        k=p-r;g=gamma(k)
        assert g%P==0 and h[r][0]==0
        actual=(g//P)*b[r]%p
        assert actual==-144*pow(r,-1,p)*h[r][1]%p
        U=(U+k*actual)%p
    mid=sum(h[r][1] for r in range(3*m+1,4*m+1))%p
    up=sum(h[r][1] for r in range(1,m+1))%p
    assert (M,U)==(72*mid%p,144*up%p)
    prefix=1;J=0
    for t in range(1,m+1):
        J=(J+h[t][1]*prefix)%p
        prefix=(prefix+(6*t+1)*gamma(t)*pow(216,-t,p))%p
    assert (J-up)%p==sum(h[t][1]*(
        sum((6*k+1)*gamma(k)*pow(216,-k,p) for k in range(t))%p-1)
        for t in range(1,m+1))%p
    assert (-3*(M+U))%p==(-216*mid-432*up)%p
    return M,U,mid,up,J

if __name__=='__main__':
    primes=[p for p in range(7,998)
            if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]
    results={p:verify(p) for p in primes}
    print('PASS primes=',len(primes),'target_classes=',sum(p%24 in (13,19) for p in primes))
    print('reflection=',sum((p-1)//2 for p in primes),'M=',sum((p-1)//6 for p in primes),'U=',sum((p-1)//6 for p in primes))
    for p in (13,19,67,373): print(p,results[p])
