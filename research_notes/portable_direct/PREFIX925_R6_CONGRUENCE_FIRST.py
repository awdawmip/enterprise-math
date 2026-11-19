#!/usr/bin/env python3
"""Independent congruence-first exact mass for PREFIX-925's two symmetric observers.

Pure Python integers; computes all labeled zero/flip trace-pair classes.
The bit-window kernel is the verified PREFIX-918 formula, with distinct
parameter traversal from PREFIX925_R6_KSWEEP_MASS.cpp.
"""
import json
from math import gcd, lcm

P=32
N=1 << P
PAIR=(464773,304985)

def ones(z,j):
    h=1 << j
    q,r=divmod(z,2*h)
    return q*h+max(0,r-h)

def high(z,hi,lo,u,v,shift):
    h=1 << hi
    q,r=divmod(z,2*h)
    length=min(h,max(0,r-u*h))
    hit=ones(shift+length,lo)-ones(shift,lo)
    return q*(h//2)+(hit if v else length-hit)

def overlap(l1,h1,l2,h2):
    return max(0,min(h1,h2)-max(l1,l2))

def same(i,A,u,v,L):
    h=1 << i
    period=2*h
    shift=A%period
    def tail(z):
        return sum(overlap(u*h,min((u+1)*h,z),v*h-shift+s*period,(v+1)*h-shift+s*period) for s in (0,1))
    q,r=divmod(L,period)
    return q*tail(period)+tail(r)

def kernel(A,i,j,eps,eta):
    L=N-A
    u=(eps==-1)
    v=(eta==-1)
    if i>j:return high(L,i,j,u,v,A)
    if i<j:return high(N,j,i,v,u,-A)-high(A,j,i,v,u,-A)
    return same(i,A,u,v,L)

def masses(a,b):
    assert gcd(a,b)==1
    inv=pow(a,-1,b)
    K=(N-1)//a
    classes=[0]*4
    fibers=0
    for i in range(P):
        for j in range(P):
            for eps in (-1,1):
                for eta in (-1,1):
                    rhs=eps*(1<<i)-eta*(1<<j)
                    k=(rhs*inv)%b
                    for kk in range(k if k else b,K+1,b):
                        A=kk*a
                        D=A-rhs
                        assert D%b==0
                        c=kernel(A,i,j,eps,eta)
                        if c==0:continue
                        fibers+=1
                        idx=0 if (i>j and D>0) else 1 if i>j else 2 if i<j else 3
                        classes[idx]+=c
    same_start=(N//2)*sum((P-d)*int(((1<<d)-1)%b==0)+
                           (P-d)*int(((1<<d)+1)%b==0) for d in range(1,P))
    mixed=0
    mixed_fibers=0
    for i in range(P):
        h=1 << i
        for s in (1,-1):
            k0=(-s*h*inv)%b
            for k in range(k0 if k0 else b,K+1,b):
                A=k*a
                r=A%(2*h)
                tau=min(r,2*h-r)
                w=N-A-s*tau
                assert w>=0
                mixed+=w
                mixed_fibers+=(w>0)
    v=lcm(a,b)
    count=(N-1)//v
    zz=count*N-v*count*(count+1)//2
    return {'a':a,'b':b,'zero_zero':zz,'zero_flip':mixed,
            'zero_flip_positive_fibers':mixed_fibers,
            'two_flip_classes':classes,'two_flip_same_start':same_start,
            'two_flip_positive_fibers':fibers,
            'two_flip_total':sum(classes)+same_start,
            'total':zz+mixed+sum(classes)+same_start}

if __name__=='__main__':
    forward=masses(*PAIR)
    reverse=masses(*PAIR[::-1])
    assert forward['total']==reverse['total']==59228731470
    assert forward['two_flip_classes']==[29257670556,0,29257670556,197492246]
    assert forward['zero_flip']==515898112 and forward['two_flip_positive_fibers']==113
    print(json.dumps({'schema':'PREFIX925_CONGRUENCE_FIRST_EXACT_V1','method':'modular-inverse-first parameter enumeration',
                      'forward':forward,'reverse':reverse,'time_reversal_total_equal':True,
                      'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d'},indent=2,sort_keys=True))
