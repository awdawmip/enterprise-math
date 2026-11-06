"""D25 sparse labelled-source BRC two-window codec, independent exact tests."""
from math import isqrt

def prime_list(limit):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2,isqrt(limit)+1):
        if sieve[i]: sieve[i*i::i]=b'\x00'*len(sieve[i*i::i])
    return [p for p in range(7,limit+1) if sieve[p] and p%6==1]

def verify(p,power,synthetic=False):
    m=(p-1)//6; a,b,c=2*m,3*m,4*m; mod=p**power
    fac=[1]*p
    for k in range(1,p): fac[k]=fac[k-1]*k%mod
    invfac=[1]*p; invfac[-1]=pow(fac[-1],-1,mod)
    for k in range(p-1,0,-1): invfac[k-1]=invfac[k]*k%mod
    def cp(n,k):
        if k<0: return 0
        if n<0: return (-1)**k*cp(-n+k-1,k)%mod
        if k>n: return 0
        return fac[n]*invfac[k]*invfac[n-k]%mod
    def g(t,j): return cp(t-a,j)*cp(t,j)%mod
    if synthetic:
        u=[(73+97*j+37*j*j+j**3)%mod for j in range(b+1)]
    else:
        v=pow(2,-1,mod)
        u=[(6*j+1)*pow(-v,j,mod)*cp(b,j)%mod for j in range(b+1)]
    S=list(range(a))+list(range(c,c+m+1))
    assert len(S)==b+1==(p+1)//2
    Y=[sum(u[k]*g(t,k) for k in range(j+1))%mod for j,t in enumerate(S)]
    got=[]
    for j,t in enumerate(S):
        d=g(t,j)
        assert d%p
        got.append((Y[j]-sum(got[k]*g(t,k) for k in range(j)))*pow(d,-1,mod)%mod)
    assert u==got
    if not synthetic:
        assert u[0]==1
        inferred=[1]
        for j,t in enumerate(S[1:],start=1):
            inferred.append((Y[j]-sum(inferred[k]*g(t,k) for k in range(j)))*pow(g(t,j),-1,mod)%mod)
        assert inferred==u
    for t in set([a,c-1,p-1,(a+c)//2]):
        assert sum(u[k]*g(t,k) for k in range(b+1))%mod==sum(got[k]*g(t,k) for k in range(b+1))%mod
    inv=[0]+[pow(k,-1,mod) for k in range(1,c+1)]
    H=[0]*(c+1)
    for k in range(1,c+1): H[k]=(H[k-1]+inv[k])%mod
    def derivative_from(coeffs):
        normal=carry=0
        for j,weight in enumerate(coeffs):
            if j<=a:
                gd=cp(a,j)*cp(c,j)*(H[a]-H[a-j]+H[c]-H[c-j])%mod
                normal=(normal+weight*gd)%mod
            else:
                gd=(-1)**(j-a-1)*fac[a]*fac[j-a-1]*invfac[j]*cp(c,j)%mod
                carry=(carry+weight*gd)%mod
        return normal,carry,(normal+carry)%mod
    assert derivative_from(u)==derivative_from(got)
    if not synthetic and power>=2 and p in {13,109,373}:
        assert derivative_from(got)[-1]%(p*p)==p*{13:12,109:40,373:180}[p]%(p*p)
    assert all(g(t,b)==0 for t in S[:-1])
    assert g(S[-1],b)%p
    return len(S),S[:2],S[-2:],got[-1]

if __name__=='__main__':
    ps=prime_list(1000); count=0
    for p in ps:
        for s in (1,2):
            for synthetic in (False,True):
                verify(p,s,synthetic); count+=1
    for p in (13,109,373):
        for synthetic in (False,True):
            verify(p,3,synthetic); count+=1
    print('p=1 mod6 primes <=1000:',len(ps),'source-recovery cases:',count,'ALL PASS')
    for p in (13,109,373):
        print('witness:',p,'result:',verify(p,2,False))
