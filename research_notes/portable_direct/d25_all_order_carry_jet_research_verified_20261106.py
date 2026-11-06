#!/usr/bin/env python3
"""Exact finite-field source-jet certificate: modular integer arithmetic only.
D25 labelled radial polynomial; independent coefficient recurrence and Newton power sums.
"""
from math import isqrt

P = 5113
M = (P-1)//6
R = 6
A, B, C = 2*M, 3*M, 4*M

def modinv(x):
    return pow(x % P, -1, P)

fac = [1]*(P)
for j in range(1,P): fac[j] = fac[j-1]*j % P
ifac = [modinv(fac[-1])]*(P)
for j in range(P-1,0,-1): ifac[j-1]=ifac[j]*j%P

def choose(n,j):
    return fac[n]*ifac[j]%P*ifac[n-j]%P if 0 <= j <= n else 0

# Independent method A: direct multiplication of C(a+z,j), C(c+z,j)
def mul_linear(f, constant, invj, degree):
    out=[0]*(degree+1)
    for k in range(degree+1):
        out[k]=(constant*f[k]+(f[k-1] if k else 0))*invj%P
    return out

# Independent method B: Newton sums of invertible source factors, with one zero factor in carry.
def esym_from_power_sums(psum, degree):
    es=[1]+[0]*degree
    for r in range(1,degree+1):
        es[r]=sum(((-1)**(k-1))*es[r-k]*psum[k] for k in range(1,r+1))*modinv(r)%P
    return es

a_poly=[1]+[0]*R
c_poly=[1]+[0]*R
pow_bino=1
w=1
inv2=modinv(2)
headsA=[0]*(R+1)
tailsA=[0]*(R+1)
headsB=[0]*(R+1)
tailsB=[0]*(R+1)
psum=[0]*(R+1)
for j in range(B+1):
    # Already after (j) factors; power sums omit a zero factor when it is present.
    ee=esym_from_power_sums(psum,R)
    if j<=A:
        amp=w*choose(A,j)%P*choose(B,j)%P*choose(C,j)%P
        termsB=[amp*ee[r]%P for r in range(R+1)]
    else:
        E=(-1 if ((j-A-1)%2) else 1)*fac[A]*fac[j-A-1]%P*ifac[j]%P
        amp=w*choose(B,j)%P*choose(C,j)%P*E%P
        termsB=[0]+[amp*ee[r-1]%P for r in range(1,R+1)]
    conv=[sum(a_poly[k]*c_poly[r-k] for k in range(r+1))%P for r in range(R+1)]
    ampA=(6*j+1)*w*choose(B,j)%P
    termA=[ampA*conv[r]%P for r in range(R+1)]
    termsB=[(6*j+1)*v%P for v in termsB]
    if termsB != termA:
        raise AssertionError(f'Disagreement at j={j}: {termA=} {termsB=}')
    for r in range(R+1):
        if j<=A:
            headsA[r]=(headsA[r]+termA[r])%P
            headsB[r]=(headsB[r]+termsB[r])%P
        else:
            tailsA[r]=(tailsA[r]+termA[r])%P
            tailsB[r]=(tailsB[r]+termsB[r])%P
    if j==B: break
    # Update the coefficient polynomials for j+1.
    a_poly=mul_linear(a_poly,A-j,modinv(j+1),R)
    c_poly=mul_linear(c_poly,C-j,modinv(j+1),R)
    # Update reciprocals: the a-j=0 factor at j=A is precisely the one-carry zero.
    if A!=j:
        ia=modinv(A-j)
        powa=1
        for r in range(1,R+1):
            powa=powa*ia%P
            psum[r]=(psum[r]+powa)%P
    ic=modinv(C-j)
    powc=1
    for r in range(1,R+1):
        powc=powc*ic%P
        psum[r]=(psum[r]+powc)%P
    w=w*(-inv2)%P

assert headsA==headsB and tailsA==tailsB
coeffs=[(x+y)%P for x,y in zip(headsA,tailsA)]
assert coeffs[:4]==[0,0,0,3783],coeffs[:4]
assert headsA[2]==3519 and tailsA[2]==1594
assert headsA[3]==4774 and tailsA[3]==4122
print('p=',P,'m=',M,'degree=',R)
print('head',headsA)
print('carry',tailsA)
print('coefficients',coeffs)
print('two independent exact finite-field methods PASS, all j<=3m')

# A third, independent readout: evaluate the unexpanded original weighted
# source sum at z=p*t for t=0..R modulo p^(R+1). The s-th finite difference
# divided by s! p^s recovers the exact coefficient [z^s] modulo p.
from math import comb, factorial
MOD=P**(R+1)
invs=[0]+[pow(j,-1,MOD) for j in range(1,B+1)]
winc=-pow(2,-1,MOD)%MOD

def weighted_sum(t):
    aa=cc=bb=w=1
    out=0
    for j in range(B+1):
        out=(out+(6*j+1)*w*bb*aa*cc)%MOD
        if j == B: break
        invj=invs[j+1]
        aa=aa*(A+P*t-j)*invj%MOD
        cc=cc*(C+P*t-j)*invj%MOD
        bb=bb*(B-j)*invj%MOD
        w=w*winc%MOD
    return out

points=[weighted_sum(t) for t in range(R+1)]
for r in range(R+1):
    diff=sum((-1)**(r-t)*comb(r,t)*points[t] for t in range(r+1))%MOD
    assert diff%(P**r)==0
    reconstructed=(diff//(P**r))*pow(factorial(r),-1,P)%P
    assert reconstructed==coeffs[r], (r,reconstructed,coeffs[r])
print('third method: 7 full original sums modulo p^7 recover all jets PASS')
