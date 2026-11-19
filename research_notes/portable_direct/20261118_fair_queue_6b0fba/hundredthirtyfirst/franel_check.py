"""Franel two-digit identities, from independent integer binomial evaluations."""
from functools import lru_cache
from math import comb, isqrt
import json


def primes(limit):
    return [p for p in range(5, limit + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def direct(n, p, precision=3):
    """Walk every binomial coefficient; keep its unit part even during carries."""
    modulus = p**precision
    u, v, result = 1, 0, 1
    for j in range(1, n + 1):
        a, b = n + 1 - j, j
        while a % p == 0:
            a //= p
            v += 1
        while b % p == 0:
            b //= p
            v -= 1
        u = u * a * pow(b, -1, modulus) % modulus
        if 3*v < precision:
            result = (result + pow(u, 3, modulus) * p**(3*v)) % modulus
    return result


def digit_data(p):
    g = [0, 1]
    for i in range(1, p - 1):
        z = (7*i*i + 7*i + 2)*g[i] + 8*i*i*g[i-1]
        g.append(z * pow((i+1)**2, -1, p) % p)
    h = [0]
    for j in range(1, p):
        h.append((h[-1] + pow(j, -1, p)) % p)
    f, slopes = [], []
    for d in range(p):
        terms = [comb(d, j)**3 for j in range(d+1)]
        f.append(sum(terms))
        slopes.append(3 * sum(t*(h[d] - h[j]) for j, t in enumerate(terms)) % p)
    return f, slopes, g


def block(p, a, b, t):
    """Sum cubes in the t-th outer binomial block after removing its common factor."""
    q = p**3
    num, den = 1, 1
    for h in range(1, b+1):
        num = num*(a*p+h) % q
        den = den*((a-t)*p+h) % q
    value = num*pow(den, -1, q) % q
    total = pow(value, 3, q)
    # Invert all t*p+j, 1 <= j <= b, with a single extended gcd.
    inverses = [1]
    for j in range(1, b+1):
        inverses.append(inverses[-1]*(t*p+j) % q)
    prod_inv = pow(inverses[-1], -1, q)
    for j in range(b, 0, -1):
        inverses[j] = inverses[j-1]*prod_inv % q
        prod_inv = prod_inv*(t*p+j) % q
    for j in range(b):
        value = value*((a-t)*p+b-j)*inverses[j+1] % q
        total += pow(value, 3, q)
    return total % q


@lru_cache(maxsize=None)
def short(p, a):
    if a >= p:
        return direct(a, p)
    return block(p, 0, a, 0)


def composite(p, a, b):
    q = p**3
    f, prev = short(p, a), short(p, a-1)
    h0, h1 = block(p, a, b, 0), block(p, a, b, 1)
    return (h0*f+(h1-h0)*pow(3*(a-1), -1, q)*a*a*(f-2*prev)) % q


def main():
    pairs = affine = echoes = literal = 0
    singular_examples = []
    rank_witness = {}
    mid_primes = []
    for p in primes(71):
        f, l, g = digit_data(p)
        bad = [b for b in range(p) if f[b] % p == 0]
        m = (p-1)//2
        for d in range(min(16, p)):
            assert direct(d, p) == f[d] % p**3
            literal += 1
        ordered = []
        for a in bad:
            row = []
            for b in bad:
                n = p*a+b
                intercept = (f[a]//p * (f[b]//p+a*l[b]) +
                             8*a*a*f[a-1]*g[b]) % p
                exact = direct(n, p)
                assert exact == p*p*intercept == composite(p, a, b)
                pairs += 1
                row.append(exact//(p*p))
                for c in (1, 2):
                    expected = f[c]*((f[a]//p+c*l[a])*(f[b]//p+a*l[b])
                                     +8*a*a*f[a-1]*g[b])
                    assert direct(c*p*p+n, p) == p*p*(expected % p)
                    affine += 1
            ordered.append(row)
            roots = [c for c in range(p) if not
                     ((f[a]//p+c*l[a])*(f[a]//p+a*l[a])-pow(-8,a,p))%p]
            if (p,a) in ((29,12),(67,23)):
                for c in [0, *roots]:
                    n=c*p*p+a*(p+1)
                    residue=direct(n,p,5)
                    v=0
                    unit=residue
                    while unit and unit%p==0:
                        v+=1
                        unit//=p
                    assert v in (2,3)
                    singular_examples.append(dict(p=p, digit=a, prefix=c,n=n,
                           first_quotient=(f[a]//p)%p, slope=l[a],
                           valuation=v, leading=unit%p, residue_mod_p5=residue))
        if p == 29:
            x,y,z = ordered
            det = (x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])
                   +x[2]*(y[0]*z[1]-y[1]*z[0]))%p
            assert det == 1
            rank_witness = dict(p=p, bad_digits=bad, matrix=ordered, determinant_mod_p=det)
        if p % 8 in (5,7):
            mid_primes.append(p)
            assert l[m] == 2*(f[m]//p)%p and 2*g[m]*f[m-1]%p==1
            prefixes = list(range(4)) + [m, p+1]
            for c in prefixes:
                n=c*p*p+(p*p-1)//2
                assert direct(n,p)==p*p*(direct(c,p,1)%p)
                echoes += 1
    native=[]
    for p in (536111,663983):
        n=(p-2)//3
        m=(p-1)//2
        u,v=short(p,n),short(p,m)
        assert u%p==v%p==0
        u,v=u//p%p,v//p%p
        fwd,rev=(composite(p,a,b) for a,b in ((n,m),(m,n)))
        assert fwd%(p*p)==rev%(p*p)==0
        fwd,rev=fwd//(p*p),rev//(p*p)
        ratio=short(p,n-1)*pow(short(p,m-1),-1,p)%p
        assert (16*ratio-9*fwd)%p==3*u*v%p
        with_prefix = [composite(p,p+a,b) for a,b in ((n,m),(m,n))]
        assert all(value%(p*p)==0 for value in with_prefix)
        qnm, qmn = [value//(p*p) for value in with_prefix]
        snm = (qnm*pow(2,-1,p)-fwd)%p
        smn = (qmn*pow(2,-1,p)-rev)%p
        assert (2*(1+2*n)*u*v - (1+2*n)*smn + 2*m*snm)%p == 0
        native.append(dict(p=p,n=n,m=m, index=p*n+m, reversed_index=p*m+n,
                     quotient_nm=fwd,quotient_mn=rev,neighbor_ratio=ratio,
                     prefix_one_nm=qnm,prefix_one_mn=qmn,
                     difference_nm=snm,difference_mn=smn,
                     u_n=u,u_m=v,product=u*v%p))
    print(json.dumps(dict(prime_range=[5,71], primes=primes(71),
               literal_single_digit_tests=literal, ordered_bad_pairs=pairs,
               extra_prefix_tests=affine, midpoint_primes=mid_primes,
               midpoint_prefix_tests=echoes, deep_digit_examples=singular_examples,
               native_double_jets=native,rank_three_witness=rank_witness),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
