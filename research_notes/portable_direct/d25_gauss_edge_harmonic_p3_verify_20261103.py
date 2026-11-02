#!/usr/bin/env python3
"""Direct coefficient versus independent harmonic lift, integer modular arithmetic."""
import json

def primes(n):
    a=bytearray(b'\1')*(n+1)
    a[:2]=b'\0\0'
    for j in range(2,int(n**.5)+1):
        if a[j]: a[j*j::j]=b'\0'*((n-j*j)//j+1)
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def test(p):
    r=(p-1)//6
    m=p**3
    # Independent original rational coefficient product, strip exactly two p factors.
    numerator=denominator=1
    stripped6=stripped3=0
    for k in range(p-1):
        a,b=6*k+1,3*k+1
        if a%p==0:
            assert k==r and a==p
            a//=p; stripped6+=1
        if b%p==0:
            assert k==2*r and b==p
            b//=p; stripped3+=1
        numerator=numerator*a*b%m
        denominator=denominator*18*(k+1)**2%m
    assert stripped6==stripped3==1
    U=numerator*pow(denominator,-1,m)%m

    h=H1=H2=0
    t1=t2=0
    for j in range(1,2*r+2):
        a=pow(j,-1,m)
        H2=(H2+a)%m
        t2=(t2+a*a)%m
        if j<=r+1:
            H1=(H1+a)%m
            t1=(t1+a*a)%m
    h=(H1+H2)%m
    predicted=pow(10,-1,m)*(1+p*h+p*p*(h*h*pow(2,-1,m)+2*t1*pow(3,-1,m)+5*t2*pow(6,-1,m)))%m
    assert U==predicted,(p,U,predicted)
    assert U%p==pow(10,-1,p)
    assert U%(p*p)==((1+p*h)*pow(10,-1,p*p))%(p*p)
    return dict(p=p,U_mod_p3=U,digits=[(U//p**k)%p for k in range(3)],
                h_mod_p=h%p,t1_mod_p=t1%p,t2_mod_p=t2%p)

if __name__=='__main__':
    xs=[test(p) for p in primes(2000)]
    out={'schema':'D25_GAUSS_EDGE_HARMONIC_P3_CHECK_V1','result':'PASS',
         'tested':len(xs),'domain':'prime 7<=p<=2000, p=1 mod 6',
         'independent_paths':['original coefficient with p factors stripped',
                              'first/second short harmonic sum'],
         'samples':[x for x in xs if x['p'] in (7,13,19,31,37,43,73,181,373,1171,1999)],
         'native_H0_B0':False,'math_admitted':False}
    print(json.dumps(out,indent=2))
