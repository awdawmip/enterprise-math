"""Author-side exact mod-p^3 validation of D25 A216 two-zone jets; no native H0/B0."""
from math import comb, factorial


def check(p):
    m=(p-1)//6; M=p**3
    x=(-3*m,-2*m,-4*m)
    l=(pow(2,-1,M),pow(3,-1,M),2*pow(3,-1,M)%M)
    c=[1,0,0]; U=[0,0,0]; z=[0,0]
    a=1; raw=0
    for n in range(3*m+1):
        w=6*n+1
        assert (c[0]==0)==(n>2*m)
        assert (c[0]+p*c[1]+p*p*c[2]-a)%M==0
        raw=(raw+w*a)%M
        for j in range(3): U[j]=(U[j]+w*c[j])%M
        k=int(n>2*m); z[k]=(z[k]+w*c[2])%M
        if n==3*m:break
        v=[t+n for t in x]
        f0=v[0]*v[1]*v[2]
        f1=l[0]*v[1]*v[2]+l[1]*v[0]*v[2]+l[2]*v[0]*v[1]
        f2=l[0]*l[1]*v[2]+l[0]*l[2]*v[1]+l[1]*l[2]*v[0]
        d=pow(2*(n+1)**3,-1,M)
        c=[c[0]*f0*d%M,(c[1]*f0+c[0]*f1)*d%M,
           (c[2]*f0+c[1]*f1+c[0]*f2)*d%M]
        a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,M)%M
    assert raw==(U[0]+p*U[1]+p*p*U[2])%M
    if p in (7,13,19,31,37,373):
        assert raw==sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,M)
                        for n in range(3*m+1))%M
    if p%24 not in (13,19):return None
    assert (U[0]+p*U[1]-p)%(p*p)==0 and (raw-p)%(p*p)==0
    K=((U[0]+p*U[1]-p)%M)//(p*p)
    J=((raw-p)%M)//(p*p)
    assert J==(K+U[2])%p
    C=3*pow(216,2*m,p)*pow(factorial(2*m),5,p)*pow(factorial(4*m+1),-1,p)%p
    h=1; H=0
    for s in range(m):
        H=(H+h)%p
        if s<m-1:
            h=h*4*(2*s+3)*(3*s+2)**3*pow(3*(2*s+1)*(6*s+7)*(3*s+4)*(s+1),-1,p)%p
    Q=C*H%p
    assert (J+Q)%p==0
    return (p,K,z[0]%p,z[1]%p,U[2]%p,J,C,H,Q)


def main():
    upper=1500
    primes=[n for n in range(7,upper) if n%6==1 and
            all(n%d for d in range(2,int(n**0.5)+1))]
    rows=[v for p in primes if (v:=check(p)) is not None]
    assert len(primes)==115 and len(rows)==60
    print('PASS 115 primes p<1500; 60 frozen primes; original terms and 3-jet validated')
    for row in rows:
        if row[0] in (13,19,373):print('p K U2low U2cross U2 J C H Q:',*row)
    print('PASS independent original binomials at 7,13,19,31,37,373')


if __name__=='__main__':main()
