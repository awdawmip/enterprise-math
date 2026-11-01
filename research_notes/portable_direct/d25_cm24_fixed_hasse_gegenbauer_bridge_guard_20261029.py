"""D25 author-side Hasse/Gegenbauer bridge: exact Z/p²Z[x]/(x²-8/9), not native H0/B0."""
from math import comb

def primes_under(n):
    sieve = [True]*n
    sieve[:2]=[False,False]
    for i in range(2,int(n**.5)+1):
        if sieve[i]:
            sieve[i*i:n:i]=[False]*len(range(i*i,n,i))
    return [i for i in range(5,n) if sieve[i]]

def certificate(p):
    m=p*p
    q=8*pow(9,-1,m)%m
    def pair(a,b=0):return (a%m,b%m)
    def add(a,b):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
    def neg(a):return ((-a[0])%m,(-a[1])%m)
    def sub(a,b):return add(a,neg(b))
    def scale(a,n):return ((a[0]*n)%m,(a[1]*n)%m)
    def mul(a,b):return ((a[0]*b[0]+q*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
    x=pair(0,1);one=pair(1);z=pair(0)
    e=(p-1)//4;k=(p-1)//2
    inv=[0]+[pow(i,-1,m) for i in range(1,2*e+2)]
    t=scale(sub(one,x),inv[2]);s=scale(add(one,x),pow(8,-1,m))
    h=z;power=one
    for j in range(e+1):
        h=add(h,scale(power,comb(k,2*j)*comb(2*j,j)))
        power=mul(power,s)
    b0=one;b1=scale(x,-2*k)
    if e==0:b=one
    elif e==1:b=b1
    else:
        for n in range(1,e):
            b2=scale(add(scale(mul(x,b1),2*(n-k)),scale(b0,2*k-n+1)),inv[n+1])
            b0,b1=b1,b2
        b=b1
    l0=one;l1=x
    if e==0:leg=one
    elif e==1:leg=x
    else:
        for n in range(1,e):
            l2=scale(sub(scale(mul(x,l1),2*n+1),scale(l0,n)),inv[n+1])
            l0,l1=l1,l2
        leg=l1
    a=1;hm=0;jb=z;power=one
    for j in range(1,e+1):
        a=a*(-e+j-1)*(e+j)*inv[j]*inv[j]%m
        hm=(hm+inv[e+j])%m
        power=mul(power,t)
        jb=add(jb,scale(power,a*hm))
    he=sum(inv[1:e+1])%m
    sj=add(scale(leg,he),jb)
    lhs=sub(b,scale(h,(-1)**e))
    rhs=scale(sj,-p*inv[2])
    assert lhs==rhs,(p,lhs,rhs)
    assert all(v%p==0 for v in lhs)
    w=pow(q,(p-1)//2,m)
    xp=(0,w)
    ph=neg(mul(xp,h)) if e%2 else mul(xp,h)
    ps=scale(mul(xp,sj),-p*inv[2])
    # For even e the bridge reads B=H-p*S/2, not -H-p*S/2.
    if e%2==0:ph=mul(xp,h)
    assert add(ph,ps)==mul(xp,b)
    if e%2:
        assert add(ph,ps)[1]==0
    return (p,e,h,b,sj,ph,ps,mul(xp,b))

if __name__=='__main__':
    ps=primes_under(1200)
    for p in ps:certificate(p)
    print('PASS_D25_CM24_HASSE_GEGENBAUER_FIRST_ORDER_ALL_P_LT_1200',len(ps))
    for p in (13,23,37,373):
        p,e,h,b,s,ph,ps,composed=certificate(p)
        print('p=',p,'e=',e,'H=',h,'B=',b,'-x^pH=',ph,'-p*x^p*S/2=',ps,'x^pB=',composed)
