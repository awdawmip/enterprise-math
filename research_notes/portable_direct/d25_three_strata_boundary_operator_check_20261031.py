"""Exact three-strata zero-parameter Clausen operator: two forced boundaries.
This checks ordinary rational polynomials, not native H0/B0.
"""
from fractions import Fraction as F
from math import comb, factorial


def coefficients(l):
    m=2*l; h=3*l; q=4*l
    L=[F(0) for _ in range(q+1)]
    M=[F(0) for _ in range(q+1)]
    H=[F(0) for _ in range(q+1)]
    for n in range(m+1):
        L[n]=F((-1)**n*comb(h,n)*comb(m,n)*comb(q,n),2**n)
    for n in range(m+1,h+1):
        s=n-m-1
        M[n]=F(factorial(m)*factorial(s)*comb(h,n)*comb(q,n),3*factorial(n)*2**n)
    for n in range(h+1,q+1):
        s=n-m-1; r=n-h-1
        H[n]=F((-1)**(h+m+n)*factorial(h)*factorial(m)*factorial(s)*factorial(r)*comb(q,n),6*factorial(n)**2*2**n)
    return L,M,H


def operator(f,l):
    m=2*l;h=3*l;q=4*l
    out=[]
    for n in range(len(f)+1):
        c=f[n] if n<len(f) else 0
        d=f[n-1] if 1<=n<=len(f) else 0
        out.append(n**3*c-F((n-1-h)*(n-1-m)*(n-1-q),2)*d)
    return out


def exact(l):
    m=2*l;h=3*l
    L,M,H=coefficients(l)
    z=operator(L,l);a=operator(M,l);b=operator(H,l)
    assert all(x==0 for x in z)
    assert all(x==0 for n,x in enumerate(a) if n!=m+1)
    assert all(x==0 for n,x in enumerate(b) if n!=h+1)
    assert a[m+1]==(m+1)**3*M[m+1]
    assert b[h+1]==(h+1)**3*H[h+1]
    return len(z)*3


def primes_upto(n):
    return [x for x in range(7,n) if all(x%k for k in range(2,int(x**.5)+1))]


def modular(l,p):
    m=2*l;h=3*l;q=4*l
    fact=[1]*p
    for k in range(1,p):fact[k]=fact[k-1]*k%p
    invfact=[1]*p
    invfact[p-1]=pow(fact[p-1],-1,p)
    for k in range(p-1,0,-1):invfact[k-1]=invfact[k]*k%p
    def choose(N,n):
        if n>N:return 0
        return fact[N]*invfact[n]*invfact[N-n]%p
    inv2=pow(2,-1,p); inv3=pow(3,-1,p); inv6=pow(6,-1,p)
    powers2=[1]*(q+1)
    for n in range(1,q+1):powers2[n]=powers2[n-1]*inv2%p
    arrays=[[0]*(q+1) for _ in range(3)]
    for n in range(m+1):
        arrays[0][n]=(-1 if n%2 else 1)*powers2[n]*choose(h,n)*choose(m,n)*choose(q,n)%p
    for n in range(m+1,h+1):
        s=n-m-1
        arrays[1][n]=fact[m]*fact[s]*choose(h,n)*choose(q,n)*invfact[n]*powers2[n]*inv3%p
    for n in range(h+1,q+1):
        s=n-m-1;r=n-h-1
        arrays[2][n]=(-1 if (h+m+n)%2 else 1)*fact[h]*fact[m]*fact[s]*fact[r]*choose(q,n)*invfact[n]**2*powers2[n]*inv6%p
    count=0
    for i,g in enumerate(arrays):
        old=0
        for n in range(q+2):
            cur=g[n] if n<len(g) else 0
            y=(n**3*cur-inv2*(n-1-h)*(n-1-m)*(n-1-q)*old)%p
            expect=0
            if i==1 and n==m+1:expect=(m+1)**3*g[m+1]%p
            if i==2 and n==h+1:expect=(h+1)**3*g[h+1]%p
            assert y==expect,(p,i,n,y,expect)
            old=cur;count+=1
    return count,((m+1)**3*arrays[1][m+1]%p, (h+1)**3*arrays[2][h+1]%p)

if __name__=='__main__':
    rational_checks=sum(exact(l) for l in range(1,11))
    primes=[p for p in primes_upto(5000) if p%6==1]
    modular_checks=0
    for p in primes:
        modular_checks+=modular((p-1)//6,p)[0]
    m=124;h=186
    source373=modular(62,373)[1]
    print('rational_l',10,'rational_cells',rational_checks)
    print('p_1mod6',len(primes),'modular_cells',modular_checks)
    print('p373_start_sources_mod373', source373)
    print('PASS_D25_THREE_STRATA_TWO_IMPULSES_EXACT')
