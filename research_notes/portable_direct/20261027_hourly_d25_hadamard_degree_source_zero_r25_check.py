#!/usr/bin/env python3
"""D25/LIFT R25 author-side exact, source-typed F_p certificate.

This checks the claimed Hadamard coefficient relation, a rank-jet source
valuation hole and polynomial interpolation degree. It neither checks native
CM/Frobenius nor replaces independent mathematical review.
"""
from math import comb, isqrt


def primes_6m1(bound=1999):
    return [p for p in range(7, bound + 1)
            if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1))]


def inverse(v, p):
    assert v % p
    return pow(v % p, -1, p)


def source_coefficients(p):
    m = (p - 1) // 6
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i-1] * i % p
    C = 3 * pow(216, 2*m, p) * pow(fact[2*m], 5, p) * inverse(fact[4*m+1], p) % p
    D = 2 * pow(2304, 2*m, p) * pow(fact[2*m], 4, p) * inverse(fact[2*m+2], p) % p
    A, B, a, b, h = [], [], [1], [1], [1]
    for r in range(1, m):
        a.append(a[-1] * 2 * pow(3*r-1, 3, p) * inverse(3*r*(6*r+1)*(3*r+1), p) % p)
        b.append(b[-1] * 32 * pow(3*r-1, 3, p) * inverse((12*r-1)*(6*r+1)*(12*r+5), p) % p)
        h.append(h[-1] * 48*r*(3*r+1)*inverse((12*r-1)*(12*r+5), p) % p)
    for r in range(m):
        j = 2*m+r
        A0 = (6*j+5) * pow(216, j, p) * pow(fact[j], 5, p)
        A0 *= inverse(fact[2*j+1]*fact[3*j-6*m+1], p)
        B0 = 2*(8*j+7) * pow(2304, j, p) * pow(fact[j], 4, p)
        B0 *= inverse(fact[4*j-6*m+2], p)
        A.append(A0 % p); B.append(B0 % p)
        assert h[r] * a[r] % p == b[r], (p,r,'Hadamard')
        assert A[-1] == C*(2*r+1)*pow(2,r,p)*a[r]%p,(p,r,'W-port')
        assert B[-1] == D*(8*r+13*inverse(3,p))*pow(9,r,p)*b[r]%p,(p,r,'S-port')
        assert A[-1] != 0,(p,r,'W-high nonzero')
        expected_zero = (p%24 == 13 and r == (p-13)//24)
        assert (B[-1] == 0) == expected_zero,(p,r,'S-hole')
    return (m, a, b, h, A, B, C, D)


def finite_difference_degree(values, p):
    row = list(values)
    diffs = []
    while row:
        diffs.append(row[0])
        row = [(row[i+1] - row[i])%p for i in range(len(row)-1)]
    return max(i for i,x in enumerate(diffs) if x), diffs


def source_integer_valuation(p, k):
    # Explicitly retain the original integer products and source weighting.
    mod=p**4
    w=(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
    s=(8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,mod)%mod
    def val(v):
        n=0
        while n<4 and v%p==0:
            n+=1; v//=p
        return n
    return val(w),val(s),w,s


def main():
    primes=primes_6m1(); assert len(primes)==148
    count=0; exceptional_degree=[]; exceptional_weight=[]
    for p in primes:
        m,a,b,h,A,B,C,D=source_coefficients(p)
        degree,diffs=finite_difference_degree(h,p)
        assert m<=2 or m-2<=degree<=m-1,(p,m,degree)
        if degree<m-1:
            exceptional_degree.append((p,m,degree))
        z=[i for i,x in enumerate(B) if x==0]
        if p%24==13:
            expected=(p-13)//24
            assert z==[expected]
            j=2*m+expected; k=p-1-j
            assert j==(3*p-7)//8 and k==(5*p-1)//8
            assert 8*k+1==5*p and 8*j+7==3*p
            exceptional_weight.append((p,k,j,A[expected]))
        else:
            assert not z
        count+=m
    assert exceptional_degree==[(19,3,1)],exceptional_degree
    for p in [7,13,19,31,37,61,181,373,733]:
        m,_,_,h,A,B,_,_=source_coefficients(p)
        jlist=list(range(2*m,3*m));r0=(p-13)//24 if p%24==13 else None
        if r0 is not None:
            k=(5*p-1)//8;vw,vs,_,_=source_integer_valuation(p,k)
            assert (vw,vs)==(2,3),(p,k,vw,vs)
            assert A[r0]!=0 and B[r0]==0
        elif p>7:
            k=3*m+1;vw,vs,_,_=source_integer_valuation(p,k)
            assert (vw,vs)==(2,2),(p,k,vw,vs)
        degree,_=finite_difference_degree(h,p)
        print('p=%d m=%d deg_h=%d U=%d M=%d S_hole_r=%s' %
              (p,m,degree,sum(A)%p,sum(B)%p,r0))
    print('PASS: %d primes, %d exact coefficient/port tests, unique S-hole classification;' % (len(primes),count))
    print('Hadamard interpolation lower bound checked; degree m-2 only at p=19 in scanned range.')
    print('All-prime theorems depend on exact recurrence/root-count and integer valuation proofs, not this finite scan.')


if __name__=='__main__':
    main()
