"""Exact dual sparse scalar observer recovering D25 labelled-source tangent."""
from math import isqrt

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for j in range(2,isqrt(n)+1):
        if sieve[j]: sieve[j*j::j]=b'\x00'*len(sieve[j*j::j])
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]

def check(p,s):
    m=(p-1)//6; a,b,c=2*m,3*m,4*m
    modulus=p**s
    f=[1]*p
    for i in range(1,p): f[i]=f[i-1]*i%modulus
    fi=[1]*p;fi[-1]=pow(f[-1],-1,modulus)
    for i in range(p-1,0,-1):fi[i-1]=fi[i]*i%modulus
    def C(n,k):
        if k<0:return 0
        if n<0:return (-1)**k*C(-n+k-1,k)%modulus
        if k>n:return 0
        return f[n]*fi[k]*fi[n-k]%modulus
    def g(t,j):return C(t-a,j)*C(t,j)%modulus
    S=list(range(a))+list(range(c,c+m+1))
    n=len(S)
    A=[[g(t,j) for j in range(i+1)] for i,t in enumerate(S)]
    assert n==b+1
    H=[0]*(c+1)
    for k in range(1,c+1):H[k]=(H[k-1]+pow(k,-1,modulus))%modulus
    L=[]
    for j in range(n):
        if j<=a:
            d=C(a,j)*C(c,j)*(H[a]-H[a-j]+H[c]-H[c-j])%modulus
        else:
            d=(-1)**(j-a-1)*f[a]*f[j-a-1]*fi[j]*C(c,j)%modulus
        L.append(d)
    alpha=[0]*n
    for j in range(b,-1,-1):
        rhs=(L[j]-sum(alpha[i]*A[i][j] for i in range(j+1,n)))%modulus
        alpha[j]=rhs*pow(A[j][j],-1,modulus)%modulus
    assert sum(alpha)%modulus==0
    last=(-1)**(m-1)*f[2*m]**2*f[4*m]*pow(m*f[3*m]*f[5*m],-1,modulus)%modulus
    assert last==alpha[-1] and last%p
    for arbitrary in (False,True):
        if arbitrary:
            u=[(73+97*j+37*j*j+j**3)%modulus for j in range(n)]
        else:
            q=pow(-2,-1,modulus)
            u=[(6*j+1)*pow(q,j,modulus)*C(b,j)%modulus for j in range(n)]
        Y=[sum(u[j]*row[j] for j in range(len(row)))%modulus for row in A]
        exact=sum(x*y for x,y in zip(u,L))%modulus
        observed=sum(x*y for x,y in zip(alpha,Y))%modulus
        assert observed==exact
        if not arbitrary:
            assert u[0]==1
            assert sum(alpha[i]*(Y[i]-1) for i in range(1,n))%modulus==exact
            if s>=2 and p in (13,109,373):
                assert exact%(p*p)==p*{13:12,109:40,373:180}[p]%(p*p)
    return n,last,alpha

if __name__=='__main__':
    ps=primes_upto(1000)
    cnt=0
    for p in ps:
        for s in (1,2):check(p,s);cnt+=2
    for p in (13,109,373):check(p,3);cnt+=2
    print('primes',len(ps),'coefficient-family checks',cnt,'ALL PASS')
    for p in (13,109,373):
        n,last,v=check(p,2)
        zero=[i for i,x in enumerate(check(p,1)[2]) if x==0]
        print('prime',p,'sample_count',n,'last_dual',last,'mod_p_zero_indices',zero,
              'mod_p2_lifts',[(i,v[i]) for i in zero])
    assert check(373,2)[2][135]==373*162
    assert check(109,2)[2][17]==109*63
    assert check(13,2)[2][0]==13*8
