#!/usr/bin/env python3
"""Exact-author verification of GH-90 for p=4d+3 primes; no native experiment."""

def primes_below(n):
    sieve=bytearray(b'\x01')*n
    sieve[:2]=b'\x00\x00'
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n:i]=b'\x00'*(((n-1-i*i)//i)+1)
    return [i for i in range(7,n) if sieve[i] and i%4==3]

def plus(a,b,p):
    v=[0]*max(len(a),len(b))
    for i,x in enumerate(a):v[i]=(v[i]+x)%p
    for i,x in enumerate(b):v[i]=(v[i]+x)%p
    return v

def scale(a,s,p):return [(x*s)%p for x in a]
def shift(a):return [0]+a

def multiply(a,b,p):
    if not a or not b:return []
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%p
    return v

def theta(a,p):return [i*x%p for i,x in enumerate(a)]
def eval_poly(a,z,p):
    t=0
    for c in a[::-1]:t=(t*z+c)%p
    return t

def trunc0(v):
    while len(v)>1 and v[-1]==0:v.pop()
    return v

def Bpoly(X,Y,p):
    # GH-84 signed concomitant B(X,Y)
    q4=pow(4,-1,p);q16=pow(16,-1,p)
    X1=theta(X,p);X2=theta(X1,p)
    Y1=theta(Y,p);Y2=theta(Y1,p)
    def one_minus_z(V):return plus(V,scale(shift(V),-1,p),p)
    base=plus(plus(multiply(Y,X2,p),scale(multiply(Y1,X1,p),-1,p),p),multiply(Y2,X,p),p)
    part1=one_minus_z(base)
    YX1=multiply(Y,X1,p)
    part2=plus(scale(YX1,-3*q4,p),scale(shift(YX1),q4,p),p)
    Y1X=multiply(Y1,X,p)
    part3=plus(scale(Y1X,3*q4,p),scale(shift(Y1X),-5*q4,p),p)
    YX=multiply(Y,X,p)
    part4=plus(scale(YX,2*q16,p),scale(shift(YX),-7*q16,p),p)
    return trunc0(plus(plus(part1,part2,p),plus(part3,part4,p),p))

def source(p):
    d=(p-3)//4
    c=[1];h=[1]
    for j in range(d):
        c.append(c[-1]*pow(4*j+1,3,p)*pow((4*j+2)*(4*j+3)*(4*j+4),-1,p)%p)
        h.append(h[-1]*pow(4*j+3,3,p)*pow((4*j+4)*(4*j+5)*(4*j+6),-1,p)%p)
    return d,c,h

def Btheta_explicit(p,d,c,h):
    # The integral is a finite original-source convolution, not a jet evaluation.
    q4=pow(4,-1,p);q8=pow(8,-1,p)
    b=[0]*(2*d+2)
    for i in range(d+1):
        for j in range(d+1):
            n=i+j+1
            b[n]=(b[n]+c[i]*h[j]*pow(j+3*q4,3,p)*pow(n,-1,p))%p
    for j in range(1,d+1):
        n=d+1+j
        b[n]=(b[n]+c[d]*q8*j*h[j]*pow(n,-1,p))%p
    return trunc0(b)

def check(p, scan_all=False):
    d,S,U=source(p);Y=theta(U,p)
    b=Bpoly(S,Y,p)
    rhs=Btheta_explicit(p,d,S,U)
    assert b==rhs,('POLYNOMIAL_COEFFICIENTS',p,b,rhs)
    # Check the full Lagrange differential identity independently.
    U1=theta(U,p);U2=theta(U1,p)
    q4=pow(4,-1,p);q8=pow(8,-1,p)
    F=plus(plus(theta(U2,p),scale(U2,9*q4,p),p),plus(scale(U1,27*pow(16,-1,p),p),scale(U,27*pow(64,-1,p),p),p),p) # (theta+3/4)^3 U
    forcing=scale([0]*(d+1)+U1,S[d]*q8,p)
    deriv=theta(b,p)
    right=plus(shift(multiply(S,F,p)),forcing,p)
    assert trunc0(deriv)==trunc0(right),('THETA_B',p)
    if scan_all:
        values=range(2,p)
    else:
        values=[9%p] if 9%p not in (0,1) else []
    nroot=0
    trace=[]
    nonzero=None
    U2=theta(theta(U,p),p)
    S1=theta(S,p)
    for a in values:
        if eval_poly(U,a,p)==0 and eval_poly(U1,a,p)==0:
            E=eval_poly(U2,a,p)
            assert E,('ROOT_MULT_GT_2',p,a)
            identity=(E*((a-1)*eval_poly(S1,a,p)+a*eval_poly(S,a,p)))%p
            assert eval_poly(b,a,p)==identity,('ROOT_OBSERVER',p,a,eval_poly(b,a,p),identity)
            if (a-1)*eval_poly(S1,a,p)+a*eval_poly(S,a,p) and nonzero is None:
                if ((a-1)*eval_poly(S1,a,p)+a*eval_poly(S,a,p))%p:
                    nonzero=[p,a,eval_poly(S,a,p),eval_poly(S1,a,p),E,eval_poly(b,a,p)]
            if a==9%p:
                T=(8*eval_poly(S1,a,p)+eval_poly(S,a,p))%p
                assert E*T%p==(eval_poly(b,a,p)-8*E*eval_poly(S,a,p))%p
                trace=[p,d,eval_poly(S,a,p),eval_poly(U,a,p),E,eval_poly(b,a,p),T]
            nroot+=1
    return nroot,trace,len(b),nonzero

if __name__=='__main__':
    ps=primes_below(2000)
    roots=0
    traces=[]
    wit=None
    for p in ps:
        rr,tt,n,w=check(p,scan_all=True)
        if w is not None and wit is None:wit=w
        roots+=rr
        if tt and p in (23,47,71,167):traces.append(tt)
    print('PASS_GH90_COMPLETE_SIGNED_CONCOMITANT_AND_FINITE_CONVOLUTION',len(ps),'primes p<2000')
    print('PASS_GH90_ALL_ORDINARY_DOUBLE_ROOT_FIBERS',roots,'root fibers')
    print('SPECIAL_TARGET_SAMPLES[p,d,S,U,E,Btheta,T]:',traces)
    print('NONZERO_ORDINARY_FIBER_WITNESS[p,a,S,thetaS,E,Btheta]:',wit)
