"""Exact p-adic tests on the original AP Laplacian cofactor; standard library."""
from fractions import Fraction
from math import comb, factorial, lcm, prod, isqrt
from hashlib import sha256
import json


def bareiss(a):
    a = [row[:] for row in a]
    sign, old = 1, 1
    for k in range(len(a)-1):
        pivot = next((i for i in range(k,len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        v = a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                num = v*a[i][j]-a[i][k]*a[k][j]
                a[i][j], rem = divmod(num,old)
                assert not rem
        old = v
    return sign*a[-1][-1]


def minor(m, field):
    size = 2*m-1
    a = [[0]*size for _ in range(size)]
    w = [(-1)**i*comb(m-1,i) for i in range(m)]
    for i in range(m):
        for j in range(m):
            c = w[i]*w[j]*field(i,j)
            a[i][i] += c
            if j < m-1:
                a[m+j][m+j] += c
                a[i][m+j] -= c
                a[m+j][i] -= c
    return a


def q0(m):
    n,b = m-1,m*m
    return Fraction(n**n*m**(n*(n+3)+m)*factorial(n)**(2*m)
                    *(3*b+1)*prod(comb(n,j)**2 for j in range(m)),2*factorial(2*b))


def residue(a, mod):
    return a.numerator * pow(a.denominator,-1,mod) % mod


def valuation(a, p):
    if a == 0:
        return float("inf")
    def exp(n):
        v = 0
        while n % p == 0:
            n //= p
            v += 1
        return v
    return exp(a.numerator)-exp(a.denominator)


def exact_coefficients(m):
    # Each edge coefficient denominator divides L. L^(2m-1) q is integral.
    n,b = m-1,m*m
    d = n*(2*m-3)
    L = lcm(*range(1,m**3+1))
    def at(t):
        c = [(-t)**s*comb(n,s) for s in range(m)]
        def field(i,j):
            return sum(v*(L//(1+i+m*j+b*s)) for s,v in enumerate(c))
        val, rem = divmod(bareiss(minor(m,field)), t**n)
        assert not rem
        return val
    diffs = [at(t) for t in range(1,d+2)]
    ans, basis = [0]*(d+1), [1]
    for j in range(d+1):
        coefficient, rem = divmod(diffs[0],factorial(j))
        assert not rem
        for k,bk in enumerate(basis):
            ans[k] += coefficient*bk
        basis = [0]+basis
        for k in range(len(basis)-1):
            basis[k] -= (j+1)*basis[k+1]
        diffs = [v-u for u,v in zip(diffs,diffs[1:])]
    assert sum(coeff*(-1)**k for k,coeff in enumerate(ans)) == at(-1)
    normalized = [Fraction(x,L**(2*m-1)) for x in ans]
    assert normalized[0] == q0(m) and normalized[-1]
    return normalized


def q_mod(m,p,u,j):
    """q(pu) modulo p^j from the original matrix, with u a unit."""
    assert p > 2*m*m and u % p
    n,b = m-1,m*m
    prec = p**(n+j)
    coeff = [comb(n,s)*(-p*u)**s for s in range(m)]
    def field(i,h):
        value = 0
        for s, a in enumerate(coeff):
            den = 1+i+m*h+b*s
            while den % p == 0:
                assert a % p == 0
                a //= p
                den //= p
            value += (a % prec) * pow(den,-1,prec)
        return value % prec
    mat = minor(m,field)
    det = bareiss([[z % prec for z in row] for row in mat]) % prec
    stripped, rem = divmod(det,p**n)
    assert not rem
    return stripped*pow(u,-n,p**j) % (p**j)


def critical(m):
    p = 3*m*m+1
    c0 = residue(q0(m)/p,p)
    def read(u,j):
        a = q_mod(m,p,u,j+1)
        assert a % p == 0
        return a//p
    f1, f2 = read(1,1), read(2,1)
    c2 = (f2-2*f1+c0)*pow(2,-1,p) % p
    c1 = (f1-c0-c2) % p
    def poly(u):
        return (c0+c1*u+c2*u*u) % p
    tests = sorted({1,2,3,4,7,p//2,p-2,p-1})
    assert all(read(u,1)==poly(u) for u in tests)
    roots = []
    for u in range(p):
        if poly(u) == 0:
            slope = (c1+2*c2*u) % p
            assert slope
            second = read(u,2)
            assert second % p == 0
            lift = u+p*(-(second//p)*pow(slope,-1,p) % p)
            assert read(lift,2) == 0
            roots.append({"u_mod_p":u,"u_mod_p_squared":lift,
                          "q_pu_mod_p_cubed":p*second,"Qprime_mod_p":slope})
    assert all(q_mod(m,p,u,2) % p == 0 for u in tests)
    disc = (c1*c1-4*c0*c2) % p
    if c2:
        symbol = pow(disc,(p-1)//2,p)
        assert symbol and len(roots) == (2 if symbol == 1 else 0)
    return {"m":m,"p":p,"Q_mod_p":[c0,c1,c2],"discriminant_mod_p":disc if c2 else None,
            "roots":roots, "extra_unit_tests":tests}


def main():
    out = []
    for m in range(2,7):
        coeff = exact_coefficients(m)
        horizon = max(3*m*m+1,m**3)+20
        primes = [p for p in range(2*m*m+1,horizon+1)
                  if not any(p%i == 0 for i in range(2,isqrt(p)+1))]
        assert primes
        checked_bounds = 0
        for p in primes:
            first = (p-1)//(m*m)
            nu0 = int(p==3*m*m+1)
            assert valuation(coeff[0],p)==nu0
            for k,x in enumerate(coeff):
                floor = k//(first-1) if first < m else 0
                assert valuation(x,p) >= -floor
                checked_bounds += 1
            for u in (1,2):
                if u%p:
                    exact = sum(c*(p*u)**k for k,c in enumerate(coeff))
                    assert q_mod(m,p,u,3) == residue(exact,p**3)
        payload = "\n".join(f"{c.numerator}/{c.denominator}" for c in coeff)
        out.append({"m":m,"degree":len(coeff)-1,"prime_count":len(primes),
                    "coefficient_bounds":checked_bounds,"coefficients_sha256":sha256(payload.encode()).hexdigest()})
    crit = [critical(m) for m in (2,6,12,16)]
    assert [r["Q_mod_p"] for r in crit] == [[12,5,0],[104,44,49],[333,183,419],[286,625,656]]
    print(json.dumps({"independent_full_rational_interpolation":out,"critical":crit},
                     ensure_ascii=False,sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
