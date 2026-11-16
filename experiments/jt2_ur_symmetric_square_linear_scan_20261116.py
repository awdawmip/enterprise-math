#!/usr/bin/env python3
"""Exact independent O(m) symmetric-square Legendre JT2 UR scanner.

For primes p == 13 or 19 (mod 24), m=(p-1)//6.
All calculations are integer modular arithmetic. Coefficients of Q=P_{2m}(sqrt Y)
are constructed modulo p^2 from its second-order differential equation.
Coefficients of Q^2 modulo p are constructed via the third-order symmetric-square
ODE, not coefficient convolution. No assumption of epsilon=0 is used.
"""
import argparse
import csv
import sys

def primes_upto(n):
    prime = bytearray(b"\x01") * (n+1)
    prime[:2] = b"\x00\x00"
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            prime[i*i:n+1:i] = b"\x00" * (((n-i*i)//i)+1)
    return (i for i in range(5,n+1) if prime[i] and i%24 in (13,19))

def evaluate(p):
    m=(p-1)//6
    P=p*p
    N=4*m+1
    # Every integer in 1..N is coprime to p; one inverse modulo p^2.
    prefixes=[1]*(N+1)
    for i in range(1,N+1):
        prefixes[i]=prefixes[i-1]*i%P
    inv=[0]*(N+1)
    product_inv=pow(prefixes[N], -1, P)
    for i in range(N,0,-1):
        inv[i]=product_inv*prefixes[i-1]%P
        product_inv=product_inv*i%P

    c0=(-1 if m%2 else 1)%P
    for i in range(1,m+1):
        c0=c0*(m+i)*inv[i]%P
    c0=c0*pow(4,-m,P)%P

    half=inv[2]; halfp=half%p
    ypower=1
    derivative_power=1
    value=0
    derivative=0
    c=c0
    c1=None
    for j in range(m+1):
        value=(value+c*ypower)%P
        if j:
            derivative=(derivative+j*(c%p)*derivative_power)%p
            derivative_power=derivative_power*halfp%p
        ypower=ypower*half%P
        if j<m:
            c=c*(j-m)*(2*j+2*m+1)*inv[j+1]*inv[2*j+1]%P
            if j==0: c1=c
    if value%p:
        return (p,m,value%p,-1,-1,derivative,-1)

    # Symmetric-square ODE recurrence for b_r=[Y^r]Q(Y)^2:
    # (r+2)(r+1)(2r+3)b_{r+2}
    # +4(r+1)(C-(r+1)^2)b_{r+1}
    # +(2r+1)(r(r+1)-2C)b_r = 0, C=m(2m+1).
    C=m*(2*m+1)
    b0=(c0%p)**2%p
    b1=2*(c0%p)*(c1%p)%p
    J=b0
    J=(J+b1*halfp*(inv[3]%p))%p
    half_power=halfp*halfp%p
    left,right=b0,b1
    for r in range(2*m-1):
        num=(4*(r+1)*(C-(r+1)**2)*right +
             (2*r+1)*(r*(r+1)-2*C)*left)
        new=(-num*inv[r+2]*inv[r+1]*inv[2*r+3])%p
        J=(J+half_power*new*(inv[2*r+5]%p))%p
        half_power=half_power*halfp%p
        left,right=right,new
    u=value//p
    epsilon=(18*u*derivative-2*J-3)%p
    return (p,m,value%p,J,u,derivative,epsilon)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--limit",type=int,default=20000)
    parser.add_argument("--csv",action="store_true")
    args=parser.parse_args()
    total=cmfail=nonzero=0
    out=csv.writer(sys.stdout, lineterminator="\n") if args.csv else None
    if out: out.writerow(("p","m","CM0","J","u","d","epsilon"))
    for p in primes_upto(args.limit):
        rec=evaluate(p)
        total+=1
        cmfail+=(rec[2]!=0)
        nonzero+=(rec[6]!=0)
        if out: out.writerow(rec)
    print(f"SUMMARY hi={args.limit} total={total} cmfails={cmfail} e_nonzero={nonzero}",file=sys.stderr)

if __name__=="__main__":
    main()
