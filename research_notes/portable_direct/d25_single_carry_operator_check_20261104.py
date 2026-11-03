"""Exact finite-field check: combined Euler+original Gauss carry recurrence.
No native control-plane authorization or mathematical admission is implied.
"""
from math import comb, isqrt


def primes_upto(n):
    b = bytearray(b'\x01') * (n+1)
    b[:2] = b'\0\0'
    for i in range(2, isqrt(n)+1):
        if b[i]: b[i*i::i] = b'\0' * ((n-i*i)//i+1)
    return [i for i in range(2,n+1) if b[i]]


def verify(p):
    q = p//8
    if p%8 == 5:
        a,b,c,d=5*q+3,7*q+4,q,3*q+1
        mu_num=22
    else:
        a,b,c,d=7*q+6,5*q+4,3*q+2,q
        mu_num=26
    h=(p+1)//2
    assert a+b==(3*p-1)//2 and a+d==b+c==p-1
    assert (8*a+1)//p + (8*b+3)//p==12
    assert (8*a+1)%p==(8*b+3)%p==0
    M=p*p
    # Full exact B=(1-z)^h J, with degree h+q<p.
    js=[comb(c,k)*comb(d,k) for k in range(q+1)]
    B=[0]*p
    for i in range(h+1):
        ti=comb(h,i)*(-1 if i%2 else 1)
        for j,tj in enumerate(js):
            B[i+j]=(B[i+j]+ti*tj)%M
    # Restore C modulo p from source B and its divided-by-(1-z) prefix.
    C=[0]*p
    w=0
    inv2=pow(2,-1,p)
    mu=mu_num*pow(64,-1,p)%p
    for k in range(p-1):
        w=(w+B[k])%p
        source=(h*w+(3*k*inv2+mu)*B[k])%p
        C[k+1]=((k-a)*(k-b)*C[k]+source)*pow((k+1)**2,-1,p)%p
    # Independently form the original F_p from rising rational Pochhammer coefficients.
    F=[0]*p
    F[0]=1
    for k in range(1,p):
        F[k]=F[k-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,M)%M
    for k in range(p):
        if (B[k]+p*C[k]-F[k])%M:
            raise AssertionError((p,k,B[k],C[k],F[k]))
    z=pow(9,-1,M)
    sF=sG=sB=sGB=sC=sGC=0
    zk=1
    for k in range(p):
        sF=(sF+F[k]*zk)%M
        sG=(sG+(1+16*k)*F[k]*zk)%M
        sB=(sB+B[k]*zk)%M
        sGB=(sGB+(1+16*k)*B[k]*zk)%M
        sC=(sC+C[k]*zk)%p
        sGC=(sGC+(1+16*k)*C[k]*zk)%p
        zk=zk*z%M
    assert (sB+p*sC-sF)%M==0
    assert (sGB+p*sGC-sG)%M==0
    return p, q, mu_num, sF, sG, sB%M,sC,sGC

if __name__ == '__main__':
    tested=0
    rows=[]
    for p in primes_upto(2000):
        if p%8 not in (5,7): continue
        row=verify(p)
        tested+=1
        if p in (5,7,13,23,29,373,2053): rows.append(row)
    print('PASS prime count',tested,'full coefficient mod-p²; value+weighted observer mod-p²')
    for row in rows: print('sample',row)
