#!/usr/bin/env python3
"""D25 author-side first-digit source checks and finite-field Clausen squares.

Exact F_p arithmetic. The mod-p cross-family / character claims are checks
over a FINITE domain, not a universal proof. Polynomial-square identities
are proven from Clausen's formal-series identity at specified prime classes.
"""
from math import comb, isqrt
from collections import defaultdict

LIMIT=10000
SQUARE_LIMIT=3000
RAW_SAMPLE={5,7,11,13,17,19,23,37,41,73,97,373}

def primes(N):
    sieve=bytearray(b'\1')*(N+1)
    sieve[:2]=b'\0\0'
    for j in range(2,isqrt(N)+1):
        if sieve[j]:sieve[j*j::j]=bytearray((N-j*j)//j+1)
    return [p for p in range(5,N+1) if sieve[p]]

def polynomials(p):
    # 3F2(1/2,1/3,2/3;1,1;x) and 3F2(1/2,1/4,3/4;1,1;x).
    sa=(p-1)//3;sb=(p-1)//4
    a=[1]*(sa+1);b=[1]*(sb+1)
    for k in range(sa):
        a[k+1]=a[k]*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*(k+1)**3,-1,p)%p
    for k in range(sb):
        b[k+1]=b[k]*(4*k+1)*(4*k+2)*(4*k+3)*pow(64*(k+1)**3,-1,p)%p
    return a,b

def square_root_poly(p,family):
    if family=='216':
        assert p%6==1
        h=(p-1)//6
        pairs=lambda k:((6*k+1)*(3*k+1),18*(k+1)**2)
    else:
        assert p%8 in (1,3)
        h=(p-1)//8
        pairs=lambda k:((8*k+1)*(8*k+3),64*(k+1)**2)
    f=[1]*(h+1)
    for k in range(h):
        n,d=pairs(k);f[k+1]=f[k]*n*pow(d,-1,p)%p
    return f

def verify_square(p,target,root):
    coeff=[0]*len(target)
    for i,ri in enumerate(root):
        for j,rj in enumerate(root):
            coeff[i+j]=(coeff[i+j]+ri*rj)%p
    assert coeff==target,(p,coeff,target)
    return len(target)

def eval_poly(coeff,x,p):
    result=0
    for c in reversed(coeff):result=(result*x+c)%p
    return result

def raw_original(p,k,family):
    if family=='216':
        return comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,p)%p
    return comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,p)%p

def main():
    groups=defaultdict(lambda:{'primes':0,'A_zero':0,'B_zero':0,'inert':0})
    sq216=sq2304=coeff216=coeff2304=rawcount=0
    examples={}
    for p in primes(LIMIT):
        a,b=polynomials(p)
        two=pow(2,-1,p);nine=pow(9,-1,p)
        A=eval_poly(a,two,p);B=eval_poly(b,nine,p)
        Ma=sum(k*c*pow(two,k,p) for k,c in enumerate(a))%p
        Mb=sum(k*c*pow(nine,k,p) for k,c in enumerate(b))%p
        eps3=1 if pow(-3,(p-1)//2,p)==1 else -1
        eps6=1 if pow(-6,(p-1)//2,p)==1 else -1
        row=groups[p%24];row['primes']+=1
        row['A_zero']+=int(A==0);row['B_zero']+=int(B==0)
        row['inert']+=int(eps6==-1)
        assert A==eps3*B%p,(p,A,B,eps3)
        assert (A==0)==(eps6==-1),(p,A,eps6)
        assert (B==0)==(eps6==-1),(p,B,eps6)
        assert (A+6*Ma)%p==0,(p,A,Ma)
        assert (B+8*Mb)%p==0,(p,B,Mb)
        if p<=SQUARE_LIMIT and p%6==1:
            f=square_root_poly(p,'216')
            coeff216+=verify_square(p,a,f);sq216+=1
            assert A==eval_poly(f,two,p)**2%p
        if p<=SQUARE_LIMIT and p%8 in (1,3):
            f=square_root_poly(p,'2304')
            coeff2304+=verify_square(p,b,f);sq2304+=1
            assert B==eval_poly(f,nine,p)**2%p
        if p in RAW_SAMPLE:
            for k in range(len(a)):
                assert raw_original(p,k,'216')==a[k]*pow(two,k,p)%p,(p,k,'216')
                rawcount+=1
            for k in range(len(b)):
                assert raw_original(p,k,'2304')==b[k]*pow(nine,k,p)%p,(p,k,'2304')
                rawcount+=1
            examples[p]={'class24':p%24,'A216':A,'B2304':B,
                         'Ma216':Ma,'Mb2304':Mb,
                         'chi_minus3':eps3,'chi_minus6':eps6}
    print('PASS exact all-prime finite checks:',sum(x['primes'] for x in groups.values()),'primes (5..10000)')
    print('class24 (primes, A_zero, B_zero, inert):',dict(sorted(groups.items())))
    print('PASS Clausen 216 polynomial primes/coefficients:',sq216,coeff216)
    print('PASS Clausen 2304 polynomial primes/coefficients:',sq2304,coeff2304)
    print('PASS independent raw original binomial coefficients:',rawcount)
    print('examples:',dict(sorted(examples.items())))

if __name__=='__main__':main()
