#!/usr/bin/env python3
"""Author's exact mod-p verification of BOTH mod-six Clausen observer branches.
Not a Source Result or independently reviewed native calculation.
"""
import math

def primes(limit):
    a=bytearray(b'\x01')*(limit+1)
    a[:2]=b'\x00\x00'
    for j in range(2,math.isqrt(limit)+1):
        if a[j]: a[j*j:limit+1:j]=b'\x00'*(((limit-j*j)//j)+1)
    return [i for i in range(2,limit+1) if a[i]]

def direct(p):
    e=int(p%6==5)
    m=(p-1-4*e)//6
    n=2*m+e
    A=B=0
    for k in range(m+1):
        v=math.comb(m,k)*math.comb(n,k)*pow(2,-k,p)%p
        A=(A+v)%p
        B=(B+(1-6*e+12*k)*v)%p
    return A,B

def twisted(p):
    e=int(p%6==5)
    m=(p-1-4*e)//6
    assert m>=1
    n=2*m+e
    A=B=AR=BR=cnt=fixed=0
    for t in range(p):
        if (t*t+4*t+2)%p==0:fixed+=1
        if t in (0,p-1,p-2):continue
        u=(t+1)*(t+2)**2*pow(t,-1,p)%p
        v=pow(u,m,p)*pow(t+2,e,p)%p
        assert v
        w=((2-12*e)-(3+10*e)*t)*pow(t+2,-1,p)%p
        T=(-2*(t+1)*pow(t+2,-1,p))%p
        assert T not in (0,p-1,p-2)
        assert (-2*(T+1)*pow(T+2,-1,p))%p==t
        UT=(T+1)*(T+2)**2*pow(T,-1,p)%p
        VT=pow(UT,m,p)*pow(T+2,e,p)%p
        assert v*VT%p==pow(2,m+e,p)
        WT=((2-12*e)-(3+10*e)*T)*pow(T+2,-1,p)%p
        assert WT==((4+4*e)*t+(5-2*e))%p
        A=(A+v)%p
        B=(B+v*w)%p
        vi=pow(v,-1,p)
        AR=(AR+vi)%p
        BR=(BR+vi*WT)%p
        cnt+=1
    assert A==pow(2,m+e,p)*AR%p
    assert B==pow(2,m+e,p)*BR%p
    assert fixed==(2 if pow(2,(p-1)//2,p)==1 else 0)
    c=(-pow(2,-n,p))%p
    return A*c%p,B*c%p,cnt,fixed

def run(limit=2500):
    assert direct(5)==(1,0) # endpoint: do not remove t=-1,-2
    counts={0:0,1:0}; tcount=0
    for p in primes(limit):
        if p<=5:continue
        e=int(p%6==5)
        got=direct(p)
        a,b,n,f=twisted(p)
        assert got==(a,b),(p,got,(a,b))
        counts[e]+=1
        tcount+=n
        if p in (7,11,13,17,19,23,157,373):
            print("witness",p,e,(p-1-4*e)//6,a,b,f)
    assert counts=={0:178,1:186},counts
    assert tcount==419710,tcount
    print("PASS: 364 primes, 419710 involution tests, both-port agreement")
if __name__=="__main__":run()
