#!/usr/bin/env python3
"""GH-110: exact F_3347 zero-fiber and S_1673 monodromy certificate.

Portable author-side calculation; no Enterprise Math native claim/run implied.
All arithmetic uses Python integers and modular inverses; no floating point.
Build R from its reflected hypergeometric input and G independently from
Legendre's three-term recurrence, then check GH-108 derivative identity.
"""
from math import comb

P=3347
M=(P-3)//8
D=2*M
N=(P-1)//2


def trim(v):
    v=v[:]
    while len(v)>1 and v[-1]==0:
        v.pop()
    return v


def evaluate(v,x):
    y=0
    for c in reversed(v):
        y=(y*x+c)%P
    return y


def derivative(v):
    return [(i*v[i])%P for i in range(1,len(v))]


def product(a,b):
    w=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            w[i+j]=(w[i+j]+x*y)%P
    return w


def modulus(a,b):
    a,b=trim(a),trim(b)
    if b==[0]:
        raise ZeroDivisionError('zero polynomial')
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b) and a!=[0]:
        x=(a[-1]*inv)%P
        off=len(a)-len(b)
        for j,y in enumerate(b):
            a[off+j]=(a[off+j]-x*y)%P
        a=trim(a)
    return a


def gcd(a,b):
    a,b=trim(a),trim(b)
    while b!=[0]:
        a,b=b,modulus(a,b)
    unit=pow(a[-1],-1,P)
    return [(x*unit)%P for x in a]


def legendre_even(n):
    if n==0:
        return [1]
    a,b=[1],[0,1]
    for j in range(1,n):
        out=[0]*(len(b)+1)
        for i,x in enumerate(b):
            out[i+1]=(out[i+1]+(2*j+1)*x)%P
        for i,x in enumerate(a):
            out[i]=(out[i]-j*x)%P
        inv=pow(j+1,-1,P)
        a,b=b,[(x*inv)%P for x in out]
    assert all(b[i]==0 for i in range(1,n+1,2))
    return b[::2]


def hasse_G():
    E=legendre_even(D)
    G=[0]*(M+1)
    for j,e in enumerate(E):
        for k in range(j+1):
            G[M-j+k]=(G[M-j+k]+e*comb(j,k)*(-1)**(j-k))%P
    return G


def reflected_R():
    h=1
    R=[0]*(N+1)
    for j in range(D+1):
        R[D+1+j]=((8*j+5)*h*pow(D+1+j,-1,P))%P
        if j<D:
            h=(h*pow(4*j+3,3,P)*pow((4*j+4)*(4*j+5)*(4*j+6),-1,P))%P
    return R


def main():
    G=hasse_G()
    A=[((16*i+5)*g)%P for i,g in enumerate(G)]
    R=reflected_R()
    C=comb(3*M+1,M)%P
    assert (M,D,N,C)==(418,836,1673,3073)
    assert len(G)==M+1 and G[-1]==1 and G[0]==C
    assert len(R)==N+1 and R[0]==0
    # Independent-source check: reflected recurrence R vs Legendre/Hasse G.
    rhs=product(G,A)
    inv_c2=pow(C*C,-1,P)
    assert derivative(R)==[0]*D+[(x*inv_c2)%P for x in rhs]
    assert gcd(G,A)==[1]
    gcd_RG=gcd(R,G)
    gcd_RA=gcd(R,A)
    gcd_AAp=gcd(A,derivative(A))
    assert gcd_RG==[1],gcd_RG
    assert gcd_RA==[P-9,1],gcd_RA
    assert gcd_AAp==[1],gcd_AAp
    R9,G9,A9,A9prime=evaluate(R,9),evaluate(G,9),evaluate(A,9),evaluate(derivative(A),9)
    R9second=evaluate(derivative(derivative(R)),9)
    assert (R9,G9,A9,R9second)==(0,3333,0,2331)
    assert A9prime != 0
    q=D+1
    assert (q,N-q-2)==(837,834)
    from math import gcd as integer_gcd
    assert q>N//2 and integer_gcd(q,N)==1 and q%2==1
    print('PASS_GH110_BACKEND_INDEPENDENT_RECONSTRUCTION p=',P,'m=',M,'d=',D,'N=',N,'Dcomb=',C)
    print('PASS_GH110_DERIVATIVE_IDENTITY Dcomb^2 * Rprime == z^d * G * A')
    print('PASS_GH110_GCD_RG=',gcd_RG,'GCD_RA=',gcd_RA,'GCD_A_Aprime=',gcd_AAp)
    print('PASS_GH110_AT_NINE: R G A Aprime Rsecond =',R9,G9,A9,A9prime,R9second)
    print('ZERO_FIBER_CYCLE_TYPE=(837)(2)(1^834)')
    print('GROUP_DEDUCTION=primitive_plus_transposition_=>_S1673')
    print('ALL PASS')

if __name__=='__main__':main()
