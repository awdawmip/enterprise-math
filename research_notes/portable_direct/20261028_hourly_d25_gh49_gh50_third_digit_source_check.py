"""GH49/GH50 minimal independent ordered-pair p^3 checker (author evidence)."""
from math import isqrt

def primes(N):
    s=[1]*N;s[0]=s[1]=0
    for n in range(2,isqrt(N-1)+1):
        if s[n]:
            for j in range(n*n,N,n):s[j]=0
    return [p for p in range(7,N) if s[p] and p%4==3]

def check(p):
    d=(p-3)//4;m=p**3;u=pow(9,-1,m)
    beta=[1];gamma=[1];a=[1];c=[1];H=[0];L=[0]
    for r in range(d):
        beta.append(beta[-1]*16*(r+1)*(4*r+3)*pow((8*r+13)**2,-1,m)%m)
        gamma.append(gamma[-1]*4*(4*r+4-p)*(4*r+3-p)*pow((8*r+13-2*p)**2,-1,m)%m)
        a.append(a[-1]*(8*r+1)**2*pow(16*(4*r+3)*(r+1),-1,m)%m)
        c.append(c[-1]*(4*r+1)**3*pow((4*r+2)*(4*r+3)*(4*r+4),-1,m)%m)
        aa=pow(4*r+4,-1,m);bb=pow(4*r+3,-1,m);cc=pow(8*r+13,-1,m)
        H.append((H[-1]+4*cc-aa-bb)%m)
        delta=(8*cc*cc-aa*aa-bb*bb)%m
        L.append(((H[-1]**2+2*L[-1]-H[-2]**2+delta)*pow(2,-1,m))%m)
    assert all(gamma[r]==beta[r]*(1+p*H[r]+p*p*L[r])%m for r in range(d+1))
    v=[0]*(2*d+1);j=[0]*(2*d+1);k=[0]*(2*d+1);g=[0]*(2*d+1)
    for i in range(d+1):
        for l in range(d+1):
            n=i+l;b=beta[i]*beta[l]
            v[n]=(v[n]+b)%m
            j[n]=(j[n]+b*(H[i]+H[l]))%m
            k[n]=(k[n]+b*(L[i]+L[l]+H[i]*H[l]))%m
            g[n]=(g[n]+gamma[i]*gamma[l])%m
    assert all(g[n]==(v[n]+p*j[n]+p*p*k[n])%m for n in range(2*d+1))
    def moment(coef,w=0):
        return sum((8*n+11 if w else 1)*coef[n]*pow(u,n,m) for n in range(d))%m
    M0=moment(v);M1=moment(j);W0=moment(v,1);W1=moment(j,1);W2=moment(k,1)
    B=sum(a[r]*pow(9,r,m) for r in range(d+1))%m
    Q=sum((16*r+1)*a[r]*pow(9,r,m) for r in range(d+1))%m
    T=sum((8*r+1)*c[r]*pow(9,r,m) for r in range(d+1))%m
    q=(pow(3,p-1,m)-1)//p
    predicted=(B*Q+a[d]*a[d]*u*(W0+p*(q*W0+W1-4*M0)
                +p*p*(W2+q*W1-4*M1-4*q*M0)))%m
    assert predicted==T,(p,predicted,T)
    # Exact reversal of the omitted ordered-pair band, not an assumed cancellation.
    E=sum((8*n+1)*sum(a[i]*a[n-i] for i in range(max(0,n-d),min(d,n)+1))*pow(9,n,m)
          for n in range(d+1,2*d+1))%m
    assert E==a[d]*a[d]*pow(9,2*d,m)*(4*p*moment(g)-moment(g,1))%m
    assert (B*Q-E)%m==T
    return T,W2%p

if __name__=='__main__':
    ps=primes(1000)
    for p in ps:check(p)
    print('PASS_GH50_INDEPENDENT_ORDERED_PAIR_P3',len(ps),'primes')
    for p in (7,11,19,23,43,67):print('CASE',p,check(p))
