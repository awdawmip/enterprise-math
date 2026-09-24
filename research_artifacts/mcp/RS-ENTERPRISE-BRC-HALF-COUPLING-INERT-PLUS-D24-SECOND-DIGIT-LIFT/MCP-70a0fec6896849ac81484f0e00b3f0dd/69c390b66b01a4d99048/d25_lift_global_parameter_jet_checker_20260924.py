from math import gcd

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def inv(a, mod):
    return pow(a % mod, -1, mod)

def check_prime(p):
    assert p % 24 in (13, 19)
    m = (p-1)//6
    n = 2*m
    M = p**3

    fact = [1]*p
    H1 = [0]*p
    H2 = [0]*p
    for j in range(1, p):
        fact[j] = fact[j-1]*j % M
        ij = inv(j, M)
        H1[j] = (H1[j-1] + ij) % M
        H2[j] = (H2[j-1] + ij*ij) % M

    q = 1
    rf13 = 1
    rfn = 1
    W = 0
    U0 = U1 = U2 = 0
    c = []

    for k in range(p):
        if k:
            j = k-1
            q = q*((2*j+1)*(3*j+2) % M) % M
            q = q*inv(12*(j+1)**3, M) % M
            rf13 = rf13*(3*j+1)*inv(3, M) % M
            rfn = rfn*(-n+j) % M

        ck = (6*k+1)*q % M
        c.append(ck)
        W = (W + ck*rf13) % M

        if k <= n:
            uk = ck*rfn % M
            A = (H1[n]-H1[n-k]) % M
            B = (H2[n]-H2[n-k]) % M
            U0 = (U0 + uk) % M
            U1 = (U1 + uk*A) % M
            U2 = (U2 + uk*(A*A-B)) % M

    d = []
    for r in range(1, 4*m+1):
        d.append(c[n+r]*fact[n]*fact[r-1] % M)

    # Global second-order parameter-jet identity.
    rhs = U0
    rhs -= p*inv(3, M)*U1
    rhs += p*p*inv(18, M)*U2
    rhs += p*inv(3, M)*sum(d[:2*m])
    rhs += p*p*inv(9, M)*sum(
        d[r-1]*(H1[r-1]-H1[n]) for r in range(1, m+1)
    )
    assert rhs % M == W

    # Exact valuation strata of the single tail chain.
    vals = []
    for z in d:
        if z % p:
            vals.append(0)
        elif z % (p*p):
            vals.append(1)
        elif z % (p**3):
            vals.append(2)
        else:
            vals.append(3)
    assert vals == [0]*m + [1]*m + [2]*(2*m)

    # Exact cross-multiplied recurrence for d_{r+1}/d_r.
    for r in range(1, 4*m):
        num = 3*r*(p+3*r+1)*(2*p+6*r+1)*(2*p+6*r+5)
        den = 4*(p+3*r+2)**3*(2*p+6*r-1)
        assert (d[r]*den - d[r-1]*num) % M == 0

    # The two valuation jumps occur at r=m and r=2m.
    assert d[m-1] % p != 0 and d[m] % p == 0
    assert d[2*m-1] % (p*p) != 0 and d[2*m] % (p*p) == 0

targets = [p for p in range(5, 5000) if p % 24 in (13, 19) and is_prime(p)]
for p in targets:
    check_prime(p)

print({
    "status": "PASS",
    "target_primes": len(targets),
    "class13": sum(p % 24 == 13 for p in targets),
    "class19": sum(p % 24 == 19 for p in targets),
    "max_prime": max(targets),
    "checks": [
        "global_jet_mod_p3",
        "tail_valuation_strata",
        "tail_ratio",
        "two_jump_edges",
    ],
})
