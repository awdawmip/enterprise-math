#!/usr/bin/env python3
"""Exact integer certificate of the CM(−24) fixed x=1/9 fiber and first jet."""
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):
    r=[0]*max(len(a),len(b))
    for i,v in enumerate(a):r[i]+=v
    for i,v in enumerate(b):r[i]+=v
    return trim(r)
def mult(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return trim(r)
def scalar(a,k):return trim([k*x for x in a])
def der(a):return trim([i*a[i] for i in range(1,len(a))] or [0])
def power(a,n):
    r=[1]
    for i in range(n):r=mult(r,a)
    return r
q=[1,-140,294,-140,1]
N=scalar(mult([0,1],power([1,-1],2)),16)
D=power([1,1],4)
B=[1,-6,1]
assert add(scalar(N,9),scalar(D,-1))==scalar(q,-1)
assert D==list(reversed(D))
n=N+[0]*(5-len(N));assert n==list(reversed(n))
jac=add(mult(der(N),D),scalar(mult(N,der(D)),-1))
assert jac==scalar(mult(mult([1,-1],B),power([1,1],3)),16)
L=[0,16,0,-16]
assert mult(L,jac)==scalar(mult(mult(N,B),D),16)
a=list(q)
for k in range(len(a)-1,1,-1):
    z=a[k];a[k]=0;a[k-1]+=6*z;a[k-2]-=z
assert trim(a)==[512,-3072]
assert 512*512*(1-6*6+36)==2**18
print('EXACT_PASS x=1/9 quartic fiber reciprocal ports Jacobian first-jet and resultant')
