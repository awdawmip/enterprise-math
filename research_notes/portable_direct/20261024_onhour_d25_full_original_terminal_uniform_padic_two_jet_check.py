#!/usr/bin/env python3
"""Author arithmetic check, not the Source-native LIFT benchmark."""
from fractions import Fraction as F
from math import factorial, comb

def ordp(x, p):
    x = abs(x)
    if not x:
        return 100000000
    j = 0
    while x % p == 0:
        x //= p
        j += 1
    return j

def res(x, p, modulus):
    x = F(x)
    if not x:
        return 0
    a, b = x.numerator, x.denominator
    va, vb = ordp(a, p), ordp(b, p)
    assert va >= vb, (p, x, va, vb)
    a //= p**va
    b //= p**vb
    return pow(p, va-vb, modulus)*(a%modulus)*pow(b, -1, modulus)%modulus

def data(m):
    p = 6*m+1
    A = F(factorial(6*m), 3**(6*m)*factorial(2*m)**3)
    R, S = F(1), F(0)
    pieces = []
    D, E = F(0), F(0)
    for n in range(4*m+1):
        eps, delta = int(n>m), int(n>2*m)
        if n <= m:
            C = F((-1)**n*comb(m,n), 2**n)
        else:
            C = F((-1)**m*factorial(m)*factorial(n-m-1),
                  2**(n+1)*3**delta*factorial(n))
        jet = 1+p*D+F(p*p,2)*(D*D-E)
        source = A*(6*n+2*p-1)*R
        pieces.append((n,eps,delta,C,D,E,R,source))
        assert res(R/(p**eps)-C*jet,p,p**(3-eps)) == 0, (p,n,"jet")
        S += source
        if n < 4*m:
            R *= F((4*m+2*n+1)*(3*n+1)*(3*n+2),
                   36*(n+1)*(2*m+n+1)*(4*m+n+1))
            if n != m:
                D += F(1,2*(n-m))
                E += F(1,4*(n-m)**2)
            if n != 2*m:
                D -= F(2,3*(n-2*m))
                E -= F(8,9*(n-2*m)**2)
            D -= F(1,3*n+2)
            E -= F(1,(3*n+2)**2)
    low, high = pieces[:m+1], pieces[m+1:]
    assert sum(x[3] for x in low) == F(1,2**m)
    assert sum(x[0]*x[3] for x in low) == F(-m,2**m)
    J0 = F(1,2**m) + sum((6*n-1)*C*D for n,ep,dl,C,D,E,R,T in low) + sum((6*n-1)*C for n,ep,dl,C,D,E,R,T in high)
    J1 = sum(2*C*D+F(6*n-1,2)*C*(D*D-E) for n,ep,dl,C,D,E,R,T in low) + sum(C*(2+(6*n-1)*D) for n,ep,dl,C,D,E,R,T in high)
    formula = A*(J0+p*J1)
    assert res(S-p*formula,p,p**3) == 0, (p,"global")
    assert res(S,p,p) == 0, (p,"divisibility")
    assert res(S/p-formula,p,p*p) == 0, (p,"quotient")
    target = p*F(4,3)**(p-1)
    return dict(p=p,m=m,Sdivp=res(S/p,p,p*p),target=res(target/p,p,p*p),
                target_pass=res(S-target,p,p**3)==0)

if __name__ == "__main__":
    for p in range(7,401,6):
        if all(p%d for d in range(2,int(p**.5)+1)):
            row = data((p-1)//6)
            assert row["target_pass"], row
            if p in (13,19,211):
                print(row)
    print("PASS: all 37 primes p<=400 in class 1 mod 6, exact original terms and complete p^3 jets")
