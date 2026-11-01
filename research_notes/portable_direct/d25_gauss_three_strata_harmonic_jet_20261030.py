#!/usr/bin/env python3
"""Independent Gauss coefficient p^3 three-stratum harmonic-jet check.

Author-side exact p-local arithmetic, NOT native H0/B0 benchmark or Source admission.
"""
from math import comb

def primes(n):
    a=[True]*n
    for q in range(2,int(n**.5)+1):
        if a[q]:
            a[q*q:n:q]=[False]*len(range(q*q,n,q))
    return [q for q in range(5,n) if a[q] and q%6==1]

def predicted(p):
    m=(p-1)//6; N=p**3
    H=[0]*p; J=[0]*p
    for j in range(1,p):
        x=pow(j,-1,N)
        H[j]=(H[j-1]+x)%N
        J[j]=(J[j-1]+x*x)%N
    ff=[1]*p
    for i in range(1,p): ff[i]=ff[i-1]*i%N
    invf=[pow(x,-1,N) for x in ff]
    p6=pow(6,-1,N); p3=pow(3,-1,N)
    half=pow(2,-1,N); power=1
    values=[]; port=[0,0,0]; deriv=[0,0,0]
    for n in range(p):
        if n<=m:
            B=comb(m,n)*comb(2*m,n)%N
            S1=(-(H[m]-H[m-n])*p6 - (H[2*m]-H[2*m-n])*p3)%N
            S2=((J[m]-J[m-n])*p6*p6+(J[2*m]-J[2*m-n])*p3*p3)%N
            corr=(1+p*S1+p*p*(S1*S1-S2)*pow(2,-1,N))%N
            a=B*corr%N
            k=0
        elif n<=2*m:
            T=( (-1)**(m+n)*ff[m]*ff[n-m-1]*ff[2*m]*invf[2*m-n]*invf[n]**2*p6 )%N
            S=( (H[n-m-1]-H[m])*p6-(H[2*m]-H[2*m-n])*p3 )%N
            a=p*T*(1+p*S)%N
            k=1
        else:
            U=(((-1)**m)*ff[m]*ff[2*m]*ff[n-m-1]*ff[n-2*m-1]*invf[n]**2*pow(18,-1,N))%N
            a=p*p*U%N
            k=2
        port[k]=(port[k]+a*power)%N
        deriv[k]=(deriv[k]+2*n*a*power)%N
        values.append(a)
        power=power*half%N
    return values, port, deriv

def observed(p):
    N=p**3
    a=1; data=[1]
    for n in range(p-1):
        a=(a*(6*n+1)*(3*n+1)*pow(18*(n+1)**2,-1,N))%N
        data.append(a)
    return data

def original_R(p,m,c):
    pref=weighted=r=0
    C=pow(10,-1,p)
    power=pow(2,-1,p)
    for i in range(1,m+1):
        pref=(pref+C)%p
        weighted=(weighted+i*C)%p
        B=c[i]*pow(power,i,p)%p
        r=(r+2*B*((6*i+1)*pref-6*weighted))%p
        if i<m:
            C=C*36*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
    return r

def original_weighted_A(p):
    N=p**3; a=1; out=1
    for n in range(p-1):
        num=(2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3)
        den=216*(n+1)**5
        a=a*num*pow(den,-1,N)%N
        out=(out+(6*(n+1)+1)*a)%N
    return out

def check(p):
    values,port,deriv=predicted(p)
    obs=observed(p)
    assert values==obs,(p,[(i,u,v)for i,(u,v)in enumerate(zip(values,obs)) if u!=v][:2])
    m=(p-1)//6; N=p**3
    half=pow(2,-1,N); power=1; rawp=[0,0,0]; rawd=[0,0,0]
    for n,a in enumerate(obs):
        k=0 if n<=m else 1 if n<=2*m else 2
        rawp[k]=(rawp[k]+a*power)%N
        rawd[k]=(rawd[k]+2*n*a*power)%N
        power=power*half%N
    assert port==rawp and deriv==rawd
    assert port[1]%p==0 and port[2]%p**2==0
    assert deriv[1]%p==0 and deriv[2]%p**2==0
    if p%24 in (13,19):
        M=sum(port)%N
        g=sum(deriv)%N
        assert M%p==0
        h=M//p
        R=original_R(p,m,values)
        left=(6*h*g + p*(h*h-R)-1)%(p*p)
        assert left%p==0
        A=original_weighted_A(p)
        assert (A-p)%(p*p)==0
        residual=((A-p)%N)//(p*p)
        assert left//p == residual,(p,left//p,residual)
    return (p,*(x%N for x in port),*(x%N for x in deriv))

def main():
    ps=primes(1000)
    res=[check(p) for p in ps]
    print('primes p≡1 mod 6 under 1000:',len(res))
    print('target p≡13,19 mod24:',sum(p%24 in(13,19) for p in ps))
    print('all target signed residual ports match original weighted A modulo p³: YES')
    for x in res:
        if x[0] in(7,13,19,37,43,157,373,997): print('p; G0,G1,G2; deriv0,deriv1,deriv2 mod p³',x)
    print('PASS_D25_THREE_STRATUM_HARMONIC_JET_ALL_COEFFICIENTS')

if __name__=='__main__': main()
