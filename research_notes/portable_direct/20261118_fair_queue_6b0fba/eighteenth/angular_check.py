"""Check the arithmetic interfaces of the Eisenstein angular argument.

Only integer arithmetic enters the character, Jacobi sum and additive
cyclotomic identities. Numerical Fourier summaries are finite illustrations.
"""
import cmath
import json
from math import gcd, isqrt, pi, sqrt


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def norm(x):
    a,b=x
    return a*a-a*b+b*b


def reduce_pair(x, p):
    return x[0] % p, x[1] % p


def power_mod(x, n, p):
    z = (1,0)
    while n:
        if n % 2:
            z = reduce_pair(mul(z,x),p)
        x = reduce_pair(mul(x,x),p)
        n //= 2
    return z


def is_prime(p):
    return p>=2 and all(p % d for d in range(2,isqrt(p)+1))


def convolve(x, y):
    out = [(0,0)]*len(x)
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            idx = (i+j) % len(x)
            out[idx] = add(out[idx],mul(a,b))
    return out


def scalar_in_cyclotomic(coeffs, value):
    # Subtracting the scalar leaves a multiple of 1+T+...+T^(p-1).
    c = add(coeffs[0],(-value[0],-value[1]))
    assert all(v == c for v in coeffs[1:])


def as_complex(z):
    return z[0]+z[1]*complex(-0.5,sqrt(3)/2)


def evaluate(coeffs):
    total = sum(as_complex(v)*cmath.exp(2j*pi*i/len(coeffs))
                for i,v in enumerate(coeffs))
    return total


UNITS = [(1,0),(0,1),(-1,-1)]


def split_row(gen, p):
    a,b=gen
    w=-a*pow(b,-1,p) % p
    assert (w*w+w+1) % p == 0
    symbols = {pow(w,i,p):v for i,v in enumerate(UNITS)}
    chi = [(0,0)]+[symbols[pow(t,(p-1)//3,p)] for t in range(1,p)]
    jac = (0,0)
    coeffs = [(0,0)]*p
    for t,character in enumerate(chi):
        jac = add(jac,mul(character,chi[(1-t) % p]))
        coeffs[(2*a-b)*t % p] = character
    assert gcd(2*a-b,p)==1 and jac==(-a,-b)
    if p <= 103:
        scalar_in_cyclotomic(convolve(convolve(coeffs,coeffs),coeffs),(-p*a,-p*b))
    return evaluate(coeffs)/sqrt(p)


def inert_row(q):
    chi = {reduce_pair(z,q):z for z in UNITS}
    coeffs = [(0,0)]*q
    for x in range(q):
        for y in range(q):
            if x or y:
                val=chi[power_mod((x,y),(q*q-1)//3,q)]
                i=(y-2*x) % q
                coeffs[i]=add(coeffs[i],val)
    scalar_in_cyclotomic(coeffs,(q,0))
    return 1


def prime_values(limit):
    primes = [p for p in range(2,limit+1) if is_prime(p)]
    data = []
    for p in primes:
        if p % 3 == 1:
            radius=2*isqrt(p)+2
            gens=[(a,b) for a in range(-radius,radius+1) if a%3==1
                  for b in range(-radius,radius+1) if b%3==0 and norm((a,b))==p]
            assert len(gens)==2 and (gens[0][0]-gens[0][1],-gens[0][1])==gens[1]
            data.extend((p,gen,split_row(gen,p)) for gen in gens)
        elif p % 3 == 2 and p*p<=limit:
            data.append((p*p,(-p,0),inert_row(p)))
    return data, primes


def main():
    limit = 997
    data, primes = prime_values(limit)
    checks=0
    for _, gen, g in data:
        theta=as_complex(gen)/sqrt(norm(gen))
        for m in range(-6,7):
            sign=(-1)**m
            rhs=(sign*(theta**(-m)*g).conjugate(),sign*theta**m,sign*theta**m*g)
            for offset,other in zip((-1,0,1),rhs):
                assert abs(g**(3*m+offset)-other)<1e-9
                checks+=1
    signed_sums={}
    for k in [0,1,2,3,4,6,7]:
        z=sum(g**k for _,_,g in data)
        assert abs(z.imag)<1e-9
        signed_sums[str(k)]=round(z.real,6)
    split=[p for p in primes if p%3==1]
    return dict(norm_limit=limit, split_rational_primes=len(split),
                inert_ideals=sum(p%3==2 and p*p<=limit for p in primes),
                primary_primes=len(data), exact_jacobi_checks=2*len(split),
                exact_direct_gauss_cubes=2*sum(p<=103 for p in split),
                power_identities=checks, finite_signed_real_sums=signed_sums,
                exact_inert_computation="group ring coefficients reduce to q mod Phi_q",
                analytic_scope="finite identities only; frequency bounds are proved in the note")


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
