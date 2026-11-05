"""D25 diagonal-prime-square certificate, exact modular arithmetic; AUTHOR-SIDE ONLY."""
from math import comb, prod

def primes(limit):
    return [p for p in range(5,limit+1) if all(p%i for i in range(2,int(p**0.5)+1))]

def check(q):
    n=(q*q-1)//6
    N,r=divmod(n,q)
    s=[(i*r)%q for i in (2,3,4)]
    M=[i*N+(i*r)//q for i in (2,3,4)]
    assert sorted(s)==sorted(M)
    mod=q*q
    a=(-pow(2,-1,mod))%mod
    u=[pow(a,j,mod)*prod(comb(x,j) for x in s)%mod for j in range(min(s)+1)]
    U=sum(u)%mod
    L=sum((6*j+1)*v for j,v in enumerate(u))%mod
    Z=U%q
    D=sum(j*v for j,v in enumerate(u))%q
    assert (L-Z-6*D)%q==0 and L%q==0
    h=[0]*q
    fac=[1]*q
    for j in range(1,q):
        h[j]=(h[j-1]+pow(j,-1,q))%q
        fac[j]=fac[j-1]*j%q
    a1=a%q
    phi=(pow(2,q-1,mod)-1)//q
    def tau(x,j):
        return ((-1)**(j-x+1)*fac[x]*fac[j-x-1]*pow(fac[j],-1,q))%q
    V=[]; W=[]; K=[]
    for i in range(3):
        x=s[i]
        V.append(sum((6*j+1)*u[j]*(h[x]-h[x-j]) for j in range(len(u)))%q)
        W.append(sum((6*j+1)*u[j]*(h[x-j]-h[j]) for j in range(len(u)))%q)
        K.append(sum((6*j+1)*pow(a1,j,q)*tau(x,j)*prod(comb(s[t],j) for t in range(3) if t!=i)
                     for j in range(x+1,min(s[t] for t in range(3) if t!=i)+1))%q)
    A=(2*N*phi*L+sum(M[i]*(V[i]+K[i]) for i in range(3)))%q
    B=(6*Z-phi*L+sum(W[i]-K[i] for i in range(3)))%q
    lam=L//q
    eps=1 if q%6==1 else -1
    assert (lam+A-eps)%q==0
    assert (B-6*eps)%q==0
    scalar=(lam+A-B*pow(6,-1,q))%q
    assert Z*scalar%q==0
    direct=None
    if q<=43:
        direct=sum((6*k+1)*(-1)**k*pow(2,2*n-k,mod)*prod(comb(i*n,k) for i in (2,3,4))
                   for k in range(2*n+1))%mod
        assert direct==0
    return q,n,Z,D,lam,A,B,scalar,direct

if __name__=='__main__':
    rows=[check(q) for q in primes(1000)]
    print('PASS',len(rows),'prime-square palindrome and observed epsilon patterns',
          'Z=0',sum(t[2]==0 for t in rows),'Z!=0',sum(t[2]!=0 for t in rows))
    for r in rows[:12]: print(r)
