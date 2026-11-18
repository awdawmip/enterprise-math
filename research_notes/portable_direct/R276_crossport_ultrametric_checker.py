#!/usr/bin/env python3
"""R276: exact 13-adic feedback phase and arbitrarily deep small cross-edge tests."""
from fractions import Fraction as F
import json

def v13(x):
    x=F(x)
    if not x: return None
    n,d=abs(x.numerator), x.denominator
    ans=0
    while n%13==0: n//=13;ans+=1
    while d%13==0: d//=13;ans-=1
    return ans

def mod13(x):
    x=F(x)
    assert v13(x)>=0
    n,d=x.numerator,x.denominator
    while n%13==0 and d%13==0: n//=13;d//=13
    return n%13*pow(d%13,-1,13)%13

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def calculate(P,u):
    a=c=F(1,4); b=d=F(2,1+P)
    assert F(1,2)<1 and b+u<1 and u>0
    w=[[F(0),a,c],[b,F(0),u],[d,u,F(0)]]
    A=[[F(int(i==j))-w[i][j] for j in range(3)] for i in range(3)]
    D=det3(A)
    assert D==1-a*b-c*d-u*u-a*u*d-c*u*b
    S=(1-u*u)/D
    assert S==det3([[A[1][1],A[1][2],F(0)],
                    [A[2][1],A[2][2],F(0)],
                    [F(0),F(0),F(1)]])/D
    return D,S

amplification=[]
for t in range(1,9):
    P=13**t
    for h in range(1,7):
        M=1+13**h
        u=F(P,M*(1+P))
        D,S=calculate(P,u)
        assert D==F(P*(M-1)*(M+P*(M+1)),M*M*(1+P)**2)
        assert v13(D)==t+h and v13(S)==-(t+h)
        assert mod13(13**(t+h)*S)==1
        amplification.append([t,h,t+h,1])

generic=[]
for t in range(1,9):
    for r in range(1,9):
        if r==t: continue
        u=F(13**r,4*(1+13**r))
        D,S=calculate(13**t,u)
        assert v13(D)==min(t,r)
        assert v13(S)==-min(t,r)
        generic.append([t,r,min(t,r)])

print(json.dumps({'status':'PASS','prime':13,
                  'amplification_cases':len(amplification),
                  'generic_unequal_scale_cases':len(generic),
                  'amplification':amplification,'generic':generic},
                 sort_keys=True,indent=2))
