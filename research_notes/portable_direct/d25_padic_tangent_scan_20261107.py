"""Fast labelled-source derivative modulo p^2; auxiliary D25, not native p373 lift."""
from math import isqrt

def primes(n):
    s=bytearray(b'\x01')*(n+1);s[0:2]=b'\x00\x00'
    for k in range(2,isqrt(n)+1):
        if s[k]:s[k*k::k]=b'\x00'*len(s[k*k::k])
    return [i for i in range(7,n+1) if s[i] and i%6==1]

def tangent_mod(p,s=2):
    m=(p-1)//6;a=2*m;b=3*m;c=4*m;M=p**s
    inv=[0]*(c+1); inv[1]=1
    for i in range(2,c+1):
        inv[i]=(-(M//i)*inv[M%i])%M
    fact=[1]*(b+1);invfact=[1]*(b+1)
    for i in range(1,b+1):fact[i]=fact[i-1]*i%M
    invfact[-1]=pow(fact[-1],-1,M)
    for i in range(b,0,-1):invfact[i-1]=invfact[i]*i%M
    H=[0]*(c+1)
    for i in range(1,c+1):H[i]=(H[i-1]+inv[i])%M
    B_b=1;B_a=1;B_c=1;w2=1;inv2=pow(2,-1,M);N=0;R=0
    for j in range(b+1):
        w=(6*j+1)*w2*B_b%M
        if j<=a:
            deriv=B_a*B_c*(H[a]-H[a-j]+H[c]-H[c-j])%M
            N=(N+w*deriv)%M
        else:
            deriv=fact[a]*(-1)**(j-a-1)*fact[j-a-1]*invfact[j]*B_c%M
            R=(R+w*deriv)%M
        if j<b:
            q=inv[j+1]
            B_b=B_b*(b-j)*q%M
            B_c=B_c*(c-j)*q%M
            if j<a:B_a=B_a*(a-j)*q%M
            w2=w2*(-inv2)%M
    return N,R,(N+R)%M

if __name__=='__main__':
    checked=primes(10000)
    anomalies=[]
    for p in checked:
        n,r,t=tangent_mod(p)
        if t%p: raise AssertionError(('first digit unexpected',p,n,r,t))
        if t==0:anomalies.append(p)
    print('checked',len(checked),'up to 10000; p^2-tangent zero primes',anomalies)
    for p in (7,13,19,31,37,73,109,211,229,373,5113):
        n,r,t=tangent_mod(p)
        print(p,'normal',n,'carry',r,'total',t,'second digit',t//p)
