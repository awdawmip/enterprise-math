#!/usr/bin/env python3
"""R284BL: exact standard-library checks of the extension-field Port decoder.
Run: python R284BL_extension_field_port_checker.py
Only exact finite-field arithmetic; this tests fixtures, not the general theorem.
"""
import itertools
import json
import random
from collections import Counter

P = 101
SEED = 20261120


def det(a, p=P):
    n = len(a)
    if n == 0:
        return 1
    b = [[x % p for x in row] for row in a]
    prod = 1
    for k in range(n):
        j = next((r for r in range(k, n) if b[r][k]), None)
        if j is None:
            return 0
        if j != k:
            b[k], b[j] = b[j], b[k]
            prod = -prod
        piv = b[k][k]
        prod = prod * piv % p
        inv = pow(piv, -1, p)
        for i in range(k + 1, n):
            factor = b[i][k] * inv % p
            for t in range(k + 1, n):
                b[i][t] = (b[i][t] - factor * b[k][t]) % p
            b[i][k] = 0
    return prod % p


def source(C, x, p=P):
    n = len(C)
    DminusC = [[((x[i-1] if i else 0) if i == j else 0) - C[i][j]
                for j in range(n)] for i in range(n)]
    h = det(DminusC, p)
    w = []
    for i in range(n):
        sub = [row[:i] + row[i+1:] for row in DminusC[1:]]
        w.append(((-1)**i * det(sub, p)) % p)
    return h, w, DminusC


def direct_polynomial_det(C, x, p=P):
    """Independent Leibniz expansion over F_p[t], without using cofactor identities."""
    n = len(C)
    ans = [0] * (n+1)
    for perm in itertools.permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        fac = sign
        for i in range(1,n):
            fac *= ((x[i-1] if perm[i] == i else 0) - C[i][perm[i]])
        j = perm[0]
        if j == 0:
            ans[n] += fac
            ans[0] += fac * (-C[0][0])
        else:
            ans[0] += fac * (-C[0][j])
            ans[j] += fac    # z_j = -t**j => row0,j = -C0j + t**j
    return [v % p for v in ans]


def solve_columns(W, R, p=P):
    """Solve C W = R, with W/R specified as matrices of column vectors."""
    n = len(W)
    wrows = [[W[j][i] for j in range(n)] for i in range(n)]
    rrows = [[R[j][i] for j in range(n)] for i in range(n)]
    a = [wrows[i] + [int(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        j = next((i for i in range(k,n) if a[i][k]), None)
        if j is None:
            return None
        a[k], a[j] = a[j], a[k]
        s = pow(a[k][k], -1, p)
        a[k] = [(v * s) % p for v in a[k]]
        for i in range(n):
            if i != k:
                s = a[i][k]
                a[i] = [(u-s*v)%p for u,v in zip(a[i],a[k])]
    inv = [row[n:] for row in a]
    return [[sum(rrows[i][k] * inv[k][j] for k in range(n)) % p
             for j in range(n)] for i in range(n)]



# Exact finite-field-extension fixtures F_101[t]/(f), with deg(f)=n+1.
FIELD_POLYS = {2: (1, 1, 0, 1),
               3: (1, 1, 1, 0, 1),
               4: (5, 1, 1, 0, 0, 1),
               5: (5, 1, 1, 0, 0, 0, 1)}


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_divmod(a, b, p=P):
    a, b = trim([x % p for x in a]), trim([x % p for x in b])
    assert b
    q = [0] * max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        t = len(a)-len(b)
        c = a[-1] * inv % p
        q[t] = c
        for j in range(len(b)):
            a[t+j] = (a[t+j] - c*b[j]) % p
        a = trim(a)
    return trim(q), a


def poly_gcd(a, b, p=P):
    a,b=trim(a),trim(b)
    while b:
        a,b=b,poly_divmod(a,b,p)[1]
    if a:
        s=pow(a[-1],-1,p)
        a=[x*s%p for x in a]
    return a


def ext_mul(a, b, f, p=P):
    d=len(f)-1
    c=[0]*(2*d-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]=(c[i+j]+x*y)%p
    for k in range(2*d-2,d-1,-1):
        h=c[k]
        if h:
            for j in range(d):
                c[k-d+j]=(c[k-d+j]-h*f[j])%p
    return c[:d]


def ext_pow(x, exponent, f, p=P):
    d=len(f)-1
    a=[1]+[0]*(d-1)
    while exponent:
        if exponent&1:
            a=ext_mul(a,x,f,p)
        x=ext_mul(x,x,f,p)
        exponent>>=1
    return a


def irreducible_fixture(f, p=P):
    d=len(f)-1
    x=[0,1]+[0]*(d-2)
    q=x[:]
    powers={}
    for k in range(1,d+1):
        q=ext_pow(q,p,f,p)
        powers[k]=q[:]
    if powers[d]!=x:
        return False
    divs=[r for r in range(2,d+1) if d%r==0 and
          all(r%j for j in range(2,int(r**0.5)+1))]
    for r in divs:
        diff=[(a-b)%p for a,b in zip(powers[d//r],x)]
        if len(poly_gcd(f, diff, p))!=1:
            return False
    return True


def direct_extension_det(C, x, f, p=P):
    """Leibniz determinant performed in the actual quotient extension field."""
    n=len(C)
    d=n+1
    ans=[0]*d
    for perm in itertools.permutations(range(n)):
        parity=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[(-1 if parity%2 else 1)]+[0]*(d-1)
        for i,j in enumerate(perm):
            v=[(x[i-1] if i==j and i else 0)-C[i][j]]+[0]*(d-1)
            if i==0:
                if j==0:
                    v[n]=1  # d0=t**n
                else:
                    v[j]=1  # z_j=-t**j
            term=ext_mul(term,v,f,p)
        ans=[(a+b)%p for a,b in zip(ans,term)]
    return ans

def run():
    rng = random.Random(SEED)
    cases = {2: list(itertools.product((1, 2), repeat=4)),
             3: list(itertools.product((1, 2), repeat=9)),
             4: [tuple(rng.randint(1, 2) for _ in range(16)) for _ in range(300)],
             5: [tuple(rng.randint(1, 2) for _ in range(25)) for _ in range(100)]}
    summary = {'schema':'R284BL_EXACT_FIXTURE_V1','seed':SEED,'prime':P,
               'extension_degree_by_n':'n+1', 'cases': {}, 'arithmetic': 'exact F_101'}
    for n, population in cases.items():
        assert irreducible_fixture(FIELD_POLYS[n]), n
        rank_fail = 0
        recon = 0
        polynomial = 0
        identity = 0
        max_trials = 0
        for flat in population:
            C = [list(flat[i*n:i*n+n]) for i in range(n)]
            for trial in range(20):
                X = [[rng.randrange(P) for _ in range(n-1)] for _ in range(n)]
                W, R = [], []
                for x in X:
                    h, w, A = source(C,x)
                    ys = direct_polynomial_det(C,x)
                    assert ys == [h]+w[1:]+w[:1], (n, C,x,ys,h,w)
                    ext_y = direct_extension_det(C, x, FIELD_POLYS[n])
                    assert ext_y == ys, (n, C, x, ext_y, ys)
                    polynomial += 1
                    rhs = [((x[i-1] if i else 0) * w[i] - (h if i == 0 else 0)) % P for i in range(n)]
                    lhs = [sum(C[i][j]*w[j] for j in range(n)) % P for i in range(n)]
                    assert rhs == lhs
                    identity += 1
                    W.append(w)
                    R.append(rhs)
                got = solve_columns(W, R)
                if got is not None:
                    assert got == C, (n,C,got)
                    recon += 1
                    max_trials = max(max_trials,trial+1)
                    break
                rank_fail += 1
            else:
                raise AssertionError('Unexpected 20 consecutive rank failures')
        summary['cases'][str(n)] = {'matrices':len(population),'reconstructions_passed':recon,
          'full_polynomial_coefficients_checked':polynomial,
          'cofactor_linear_equations_checked':identity,
          'singular_batches_discarded':rank_fail,'maximum_batches_per_matrix':max_trials,
          'irreducible_polynomial_low_to_high':list(FIELD_POLYS[n]),
          'extension_field_determinant_checks':polynomial,
          'irreducibility_test':'Rabin Frobenius exact modular polynomial test'}
    print(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))

if __name__ == '__main__':
    run()
