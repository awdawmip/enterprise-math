#!/usr/bin/env python3
"""R551: modular resultant/interpolation certificate: k=5,...,10, half sign densities.
All claims tested over exact F_65537. Uses SymPy for exact totient/cyclotomic
polynomials and independent polynomial-resultant spot checks.
The proof notes explain why a single good-prime modular coprimality is a
valid witness for absence of characteristic-zero cyclotomic factors.
"""
from math import comb
from fractions import Fraction
from time import perf_counter
from sympy import Poly, Symbol, totient, cyclotomic_poly
P=65537
x=Symbol('x'); uvar=Symbol('u')
# 3 has exact order 65536 mod 65537; since any unit group has <=65536
# elements, this is a short elementary certificate that P is prime.
assert pow(3,65536,P)==1 and pow(3,32768,P)==P-1

def trim(a):
    while len(a)>1 and a[-1]%P==0:a.pop()
    return a

def divrem(a,b):
    a=trim(a[:]); b=trim(b[:]); n=len(b)-1
    assert b!=[0]
    if n==0: return [0],[0]
    inv=pow(b[-1],-1,P)
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        j=len(a)-len(b);z=a[-1]*inv%P;q[j]=z
        for i,v in enumerate(b): a[i+j]=(a[i+j]-z*v)%P
        a=trim(a)
    return trim(q),trim(a)

def resultant_mod(a,b):
    a=trim(a[:]);b=trim(b[:]);factor=1
    while True:
        m=len(a)-1;n=len(b)-1
        if n==0: return factor*pow(b[0],m,P)%P
        _,r=divrem(a,b)
        if r==[0]:return 0
        factor=factor*pow(-1,m*n,P)*pow(b[-1],m-(len(r)-1),P)%P
        a,b=b,r

def interpolate_consecutive(ys):
    n=len(ys);tab=ys[:];diff=[];invfactorial=1
    for j in range(n):
        if j:invfactorial=invfactorial*pow(j,-1,P)%P
        diff.append(tab[0]*invfactorial%P)
        tab=[(tab[i+1]-tab[i])%P for i in range(len(tab)-1)]
    answer=[0]*n;basis=[1]
    for j,c in enumerate(diff):
        for i,b in enumerate(basis):answer[i]=(answer[i]+c*b)%P
        if j<n-1:
            nxt=[0]*(len(basis)+1)
            for i,b in enumerate(basis):
                nxt[i]=(nxt[i]-j*b)%P
                nxt[i+1]=(nxt[i+1]+b)%P
            basis=nxt
    return trim(answer)

def gcd_mod(a,b):
    a=trim(a[:]);b=trim(b[:])
    while b!=[0]:a,b=b,divrem(a,b)[1]
    return a

def C(j):return comb(2*j,j)//(j+1)
def H(k,t):
    r=2*k+1
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(k-q)
           for q in range(min((t-1)//2,k)+1))

def choose(n,j): return comb(n,j) if 0<=j<=n else 0

def H_raw(k,t):
    r=2*k+1
    return comb(r+t,2*t)*sum(comb(r-t,h)*(choose(2*t,r-2*h)-choose(2*t,r-2*h-1))
             for h in range(r-t+1))

def charpoly_mod(k):
    d=2*k-1;p={t:Fraction(H(k,t),C(k)) for t in range(2,2*k+2)}
    a=[(-1)**(j-1)*p[j+2]/p[2] for j in range(1,d+1)]
    coeff=[Fraction(1)]+[-v for v in a]
    assert all(z.denominator%P for z in coeff) and coeff[-1]!=0
    return [z.numerator*pow(z.denominator,-1,P)%P for z in coeff][::-1]

def evaluate(a,z):
    return sum(v*pow(z,i,P) for i,v in enumerate(a))%P

def run(k):
    t0=perf_counter();Q=charpoly_mod(k);d=len(Q)-1;degree=d*d
    assert all(H(k,t)==H_raw(k,t) for t in range(2,2*k+2))
    assert Q[0]!=0 and Q[-1]==1
    QQ=Poly.from_list(Q[::-1],gens=x,modulus=P)
    values=[]
    for v in range(degree+1):
        B=[a*pow(v,d-i,P)%P for i,a in enumerate(Q)]
        values.append(resultant_mod(Q,B))
    E=interpolate_consecutive(values)
    assert len(E)==degree+1
    # independent SymPy finite-field resultant (non-Euclidean implementation)
    for v in (degree+1,degree+3):
        B=[a*pow(v,d-i,P)%P for i,a in enumerate(Q)]
        assert evaluate(E,v)==resultant_mod(Q,B)
        assert evaluate(E,v)==int(QQ.resultant(Poly.from_list(B[::-1],gens=x,modulus=P)))%P
    R=E
    for i in range(d):
        R,remainder=divrem(R,[P-1,1]);assert remainder==[0]
    D=d*(d-1)
    assert len(R)==D+1 and evaluate(R,1)!=0
    candidates=[]
    for q in range(2,2*D*D+1):
        if int(totient(q))>D:continue
        phi=Poly(cyclotomic_poly(q,uvar),uvar)
        f=[int(z)%P for z in phi.all_coeffs()][::-1]
        assert len(gcd_mod(R,f))==1, (k,q,'cyclotomic factor detected')
        candidates.append(q)
    out=(k,d,D,2*D*D,len(candidates),max(candidates),round(perf_counter()-t0,2))
    print('k=%d degree_Q=%d degree_R=%d q_bound=%d gcd_checks=%d max_candidate=%d runtime_s=%.2f' % out)
    return len(candidates)

if __name__=='__main__':
    counts=[run(k) for k in range(5,11)]
    assert counts==[147,215,300,403,528,662],counts
    print('total_exact_modular_gcd_checks',sum(counts))
    print('R551_MODULAR_CYCLOTOMIC_EXCLUSION_PASS')
