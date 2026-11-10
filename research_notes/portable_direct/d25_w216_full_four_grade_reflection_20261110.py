"""Original W216 full four-grade reflection, exact modulo p^4.
Author-side checker only; not native H0/B0.
"""
from math import comb

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0:2]=b'\x00\x00'
    for j in range(2,int(n**.5)+1):
        if sieve[j]:
            sieve[j*j:n+1:j]=b'\x00'*((n-j*j)//j+1)
    return [p for p in range(5,n+1) if sieve[p] and p%6==1]

def band(k,m):
    if k<=2*m:return 0
    if k<=3*m:return 1
    if k<=4*m:return 2
    return 3

def check(p, independent=False):
    m=(p-1)//6;M=p**4
    A=[1]
    for k in range(p-1):
        Rnum=(2*k+1)*(3*k+1)*(3*k+2)
        Rden=36*(k+1)**3
        A.append(A[-1]*Rnum*pow(Rden,-1,M)%M)
    if independent:
        for k in range(p):
            direct=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,M)%M
            assert A[k]==direct,(p,k)
    C=[-pow(18,-1,p),pow(36,-1,p),-pow(36,-1,p),pow(18,-1,p)]
    for k in range(1,p):
        prod=A[k]*A[p-k]%M
        assert prod%p**3==0,(p,k,'valuation')
        assert prod//p**3%p == C[band(k,m)]*pow(k,-3,p)%p,(p,k,'R4')
    W3=sum((6*k+1)*A[k] for k in range(4*m+1,p))%M
    assert W3%p**3==0
    G3=sum((6*h-1)*pow(18*h**3*A[h],-1,p) for h in range(1,2*m+1))%p
    assert W3//p**3%p==G3,(p,'G3')
    assert A[p-1]//p**3%p==p-1,(p,'terminal')
    assert ((6*p-5)*A[p-1]//p**3)%p==5%p,(p,'last weight')
    return G3

if __name__=='__main__':
    ps=primes_upto(2000)
    checked=0
    for p in ps:
        z=check(p, p in (7,13,19,37,73,109,181,373,997))
        checked+=p-1
        if p in (7,13,19,37,73,109,181,373,997):
            print('p=',p,'W3/p3=',z)
    print('PASS',len(ps),'primes',checked,'ordered pairs',len(ps),'grade3 sums')
