#!/usr/bin/env python3
"""Exact D25 quartic-twisted CM-exchange check; Python standard library only."""
from math import comb

def add(x,y,m): return ((x[0]+y[0])%m,(x[1]+y[1])%m)
def mul(x,y,m): return ((x[0]*y[0]+2*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
def sc(k,x,m): return (k*x[0]%m,k*x[1]%m)
def sig(x,m): return (x[0]%m,(-x[1])%m)
def inv(x,m):
    n=(x[0]*x[0]-2*x[1]*x[1])%m
    z=pow(n,-1,m)
    return (x[0]*z%m,-x[1]*z%m)

def coeffs(p):
    m=p**3; n=p-1
    c=sc(pow(108,-1,m),(2,-1),m)
    pw=[(1,0)]
    for j in range(1,(n+2)//3+1): pw.append(mul(pw[-1],c,m))
    a=(0,0); b=(0,0); i2=pow(2,-1,m)
    for j in range(n//3+1):
        a=add(a,sc(comb(2*j,j)*comb(n-j,2*j),pw[j],m),m)
    for j in range(1,(n+2)//3+1):
        b=add(b,sc(comb(2*j,j)*comb(n-j+1,2*j-1)*i2,pw[j],m),m)
    assert a[0]%p==a[1]%p==0
    return a,b

def sq(b,c,m):
    return (mul(b,sig(c,m),m),mul(c,sig(b,m),m))

def run(p,gamma):
    assert pow(2,(p-1)//2,p)==p-1 and pow(p-3,(p-1)//2,p)==1
    m2=p*p; a,b=coeffs(p)
    A=(a[0]//p%p,a[1]//p%p); B0=(b[0]%p,b[1]%p)
    beta=sc(pow(72,-1,p),(4,-1),p)
    B=mul(inv(beta,p),B0,p)
    assert mul(A,B0,p)==beta and mul(A,B,p)==(1,0)
    assert mul(gamma,gamma,p)==(p-1,0)
    At=mul(gamma,A,p); Bt=mul(gamma,B,p)
    assert mul(At,Bt,p)==(p-1,0)
    div=sig(At,p); c=sc(p,div,m2)
    qt=sq(Bt,c,m2); assert qt==((m2-p,0),(m2-p,0))
    c0=sc(p,sig(A,p),m2); ut=sq(B,c0,m2)
    assert ut==((p,0),(p,0))
    wrong=sq(Bt,sc(p,At,m2),m2)
    assert wrong!=((m2-p,0),(m2-p,0))
    At_op=sc(-1,At,p); Bt_op=sc(-1,Bt,p)
    opposite=sq(Bt_op,sc(-p,div,m2),m2)
    assert opposite==qt
    return A,B0,beta,B,gamma,At,Bt,div,c,qt,ut,wrong

def main():
    for p,g in ((19,(0,3)),(373,(104,0))):
        A,B0,beta,B,gamma,At,Bt,div,c,qt,ut,wrong=run(p,g)
        print(f"p={p}: A={A}; b={B0}; beta={beta}; Bcm={B}; gamma={gamma}")
        print(f"p={p}: Atilde={At}; Btilde={Bt}; divided={div}; lower-left={c}")
        print(f"p={p}: quartic-square={qt[0]}; untwisted-square={ut[0]}; no-sigma={wrong}")
    print("PASS_EXACT_COEFFICIENT_STREAMS_MOD_P3_AT_P19_P373")
    print("PASS_A_TIMES_BCM_EQUALS_ONE_AT_P19_P373")
    print("PASS_QUARTIC_TWISTED_PRODUCT_MINUS_ONE_AT_P19_P373")
    print("PASS_SEMILINEAR_SQUARE_MINUS_P_MOD_P2_AT_P19_P373")
    print("PASS_UNTWISTED_SQUARE_PLUS_P_MOD_P2_AT_P19_P373")
    print("PASS_NO_SIGMA_NEGATIVE_CONTROL_AT_P19_P373")
    print("PASS_OPPOSITE_QUARTIC_GAUGE_PRESERVES_SQUARE_AT_P19_P373")
    print("PASS_D25_QUARTIC_TWISTED_SEMILINEAR_CM_EXCHANGE_P19_P373")

if __name__=="__main__": main()