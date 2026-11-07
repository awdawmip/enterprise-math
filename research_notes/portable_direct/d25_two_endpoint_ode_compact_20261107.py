"""D25 finite-field two-endpoint source test, exact arithmetic, 2026-11-07."""
from math import comb

def primes(N):
    return [p for p in range(5,N+1) if all(p%d for d in range(2,__import__('math').isqrt(p)+1))]

def check(p,stream):
    if stream=='A':
        m=(p-1)//6;h=2*m+1;a,b=pow(6,-1,p),pow(3,-1,p)
        lower=(-1)**m*pow(18*comb(2*m,m),-1,p)%p
        upper=-pow(18,-1,p)%p
    else:
        k=(p-3)//8 if stream=='B3' else (p-5)//8;h=3*k+2
        a,b=(1,3) if stream=='B3' else (5,7)
        a=a*pow(8,-1,p)%p;b=b*pow(8,-1,p)%p
        lower=-3*pow(64*comb(3*k+1,k),-1,p)%p
        upper=-3*pow(64,-1,p)%p
    q=[0]*p;q[h]=lower*pow(h*h,-1,p)%p
    for n in range(h+1,p):
        q[n]=q[n-1]*(n-1+a)*(n-1+b)*pow(n*n,-1,p)%p
    for n in range(h,p+1):
        actual=(n*n*(q[n] if n<p else 0)-(n-1+a)*(n-1+b)*q[n-1])%p
        assert actual==(lower if n==h else upper if n==p else 0)
    M=p**3;v=1
    for n in range(p):
        if n>=h:assert v//(p*p)%p==q[n] and v%(p*p)==0
        if n<p-1:
            x,y=(1,6),(1,3) if stream=='A' else ((1,8),(3,8))
            if stream!='A':x,y=((1,8),(3,8)) if stream=='B3' else ((5,8),(7,8))
            v=v*(x[1]*n+x[0])*(y[1]*n+y[0])*pow(x[1]*y[1]*(n+1)**2,-1,M)%M
    return (p,stream,lower,upper)

if __name__=='__main__':
    counts={'A':0,'B3':0,'B5':0}
    for p in primes(2500):
        if p%6==1:check(p,'A');counts['A']+=1
        if p%8 in (3,5):
            typ='B3' if p%8==3 else 'B5';check(p,typ);counts[typ]+=1
    print('PASS',counts)
    for p in (13,19,43,67,109,373):
        print(check(p,'A'),check(p,'B3' if p%8==3 else 'B5'))
