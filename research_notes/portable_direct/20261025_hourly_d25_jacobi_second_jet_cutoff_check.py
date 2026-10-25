"""Exact author checker for the D25 finite Jacobi x-jet boundary source.

Fraction checks identities in Q[z]; modular moments are integer calculations.
Neither operation constitutes a native CM/divided-power experiment.
"""
from fractions import Fraction
from math import factorial

def taylor_coefficients(m):
    """(f_k(m), f_k'(m), f_k''(m)/2) for 0<=k<=6m."""
    out = [(Fraction(1), Fraction(0), Fraction(0))]
    a, b, c = out[0]
    for k in range(6 * m):
        a0, a1, den = (k-m)*(k-2*m), 4*m-3*k, (k+1)**2
        aa = a*a0/den
        bb = (b*a0+a*a1)/den
        cc = (c*a0+b*a1+2*a)/den
        a, b, c = aa, bb, cc
        out.append((a, b, c))
    return out

def check_exact_polynomial(m):
    nmax = 6*m
    rows = taylor_coefficients(m)
    for n, (a,b,c) in enumerate(rows):
        aa,bb,cc = rows[n+1] if n<nmax else (Fraction(0),)*3
        k = (n-m)*(n-2*m)
        l0 = (n+1)**2*aa-k*a
        l1 = (n+1)**2*bb-k*b+(3*n-4*m)*a
        l2 = (n+1)**2*2*cc-k*2*c+2*(3*n-4*m)*b-4*a
        target = -20*m*m*2*rows[nmax][2] if n==nmax else 0
        assert l0 == l1 == 0 and l2 == target, (m,n,l0,l1,l2,target)
    second = 2*rows[nmax][2]
    closed = Fraction(4*(-1)**m*factorial(m)*factorial(2*m)
                      *factorial(4*m-1)*factorial(5*m-1),
                      factorial(6*m)**2)
    assert second == closed, m

def check_mod_p_jet(p):
    m=(p-1)//6
    a,b,c=1,0,0
    for k in range(p-1):
        a0=(k-m)*(k-2*m)
        a1=4*m-3*k
        inv=pow((k+1)**2,-1,p)
        aa=a*a0*inv%p
        bb=(b*a0+a*a1)*inv%p
        cc=(c*a0+b*a1+2*a)*inv%p
        a,b,c=aa,bb,cc
    assert a==b==0, (p,a,b)
    assert 2*c%p==36*pow(5,-1,p)%p, p
    assert -20*m*m*2*c%p==-4%p, p

def check_weighted_moment(p):
    modulus=p**3
    r,g,d,m2=1,0,0,0
    for n in range(p):
        g=(g+r)%modulus
        d=(d+n*r)%modulus
        m2=(m2+n*n*r)%modulus
        if n+1<p:
            numerator=(6*n+1)*(3*n+1)
            denominator=36*(n+1)**2
            r=r*numerator*pow(denominator,-1,modulus)%modulus
    assert (18*m2-9*d-g+p*p)%modulus==0, p
    h=(g+12*d)%modulus
    assert (72*m2-3*h-g+4*p*p)%modulus==0, p
    return p,g,d,m2

def main():
    for m in range(1,7):
        check_exact_polynomial(m)
    candidates=[7,13,19,31,37,43,61,67,73,79,97,103,
                109,127,139,151,157,163,181,193,211,223,229,241,
                271,277,283,307,313,331,337,349,367,373,397,
                409,421,433,439,457,463,487,499,523,541,547,
                571,577,601,607,613,619,631,643,661,673,691,
                709,727,733,739,751,757,769,787,811,823,829,
                853,859,877,883,907,919,937,967,991,997,1009,
                1013,1033,1063,1093,1327]
    def prime(n):
        return n>1 and all(n%d for d in range(2,int(n**0.5)+1))
    tested=[]
    for p in candidates:
        if p%6!=1 or not prime(p):
            continue
        check_mod_p_jet(p)
        tested.append(check_weighted_moment(p))
    assert any(p==373 for p,*_ in tested)
    assert any(p==1327 for p,*_ in tested)
    print("PASS exact-Q-polynomial m=1..6; modular-Jacobi and moment p^3",len(tested),"primes")
    for p,g,d,m2 in tested:
        if p in (13,19,373,1327):
            print(f"p={p}: g={g} d={d} M2={m2} mod p^3={p**3}")

if __name__=="__main__":
    main()
