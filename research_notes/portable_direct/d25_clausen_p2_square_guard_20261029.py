#!/usr/bin/env python3
"""Exact p-adic polynomial Clausen guard. Author-side research, not H0/B0."""
from math import comb


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


def audit(p):
    assert p >= 7 and p % 6 == 1 and isprime(p)
    m = (p - 1) // 6
    modulus = p**3
    f = [1]  # _3F_2(1/3,1/2,2/3;1,1;z), degree p-1
    h = [1]  # _2F_1(1/6,1/3;1;z), degree p-1
    for n in range(p - 1):
        d3 = 18 * (n + 1)**3
        d2 = 18 * (n + 1)**2
        f.append(f[-1] * (3*n+1)*(2*n+1)*(3*n+2) * pow(d3, -1, modulus) % modulus)
        h.append(h[-1] * (6*n+1)*(3*n+1) * pow(d2, -1, modulus) % modulus)
    assert all(v % (p*p) == 0 for v in h[2*m+1:])
    assert all(v % (p*p*p) == 0 for v in f[4*m+1:])
    # The polynomial equality (not just equality at one evaluation point).
    hh = h[:2*m+1]
    conv = [sum(hh[k]*hh[n-k] for k in range(max(0, n-2*m), min(n,2*m)+1)) % modulus for n in range(p)]
    assert all((f[n]-conv[n]) % (p*p) == 0 for n in range(p))
    first = (f[2*m+1] - conv[2*m+1]) % modulus
    assert first % (p*p) == 0 and first % modulus != 0
    assert first == (2*h[2*m+1]) % modulus
    g = [h[k] % p for k in range(m + 1)]
    q = [0] * p
    for j in range(2*m+1, p):
        q[j] = (h[j] // (p*p)) % p
    # Exact third-digit defect, with original degree n<p retained.
    for n in range(p):
        r = (f[n]-conv[n]) % modulus
        predicted = 2*sum(g[i]*q[n-i] for i in range(m+1) if 2*m+1 <= n-i < p) % p
        assert r == (p*p*predicted) % modulus
    half = pow(2, -1, modulus)
    theta_h = sum(n*hh[n]*pow(half,n,modulus) for n in range(len(hh))) % modulus
    val_h = sum(hh[n]*pow(half,n,modulus) for n in range(len(hh))) % modulus
    f_value = sum(f[n]*pow(half,n,modulus) for n in range(p)) % modulus
    w_value = sum((6*n+1)*f[n]*pow(half,n,modulus) for n in range(p)) % modulus
    assert (f_value-val_h*val_h) % (p*p) == 0
    assert (w_value-val_h*(val_h+12*theta_h)) % (p*p) == 0
    if p % 24 in (13, 19):
        assert val_h % p == 0
        assert theta_h % p != 0  # finite observation; root simplicity proved separately
        assert f_value % (p*p) == 0
        assert (w_value//p) % p == (12*(val_h//p)*theta_h) % p
    # At a finite-field root, unrestricted G(z)J(z) vanishes, but the
    # n>=p overflow remains a nonzero signed third-digit source.
    boundary = None
    if p in (13, 19, 373):
        root = sum(g[i]*pow(half,i,p) for i in range(m+1)) % p
        assert root == 0
        tail = sum(g[i]*q[j]*pow(half,i+j,p) for i in range(m+1)
                   for j in range(2*m+1,p) if i+j >= p) % p
        tail_weight = sum((1+6*(i+j))*g[i]*q[j]*pow(half,i+j,p)
                          for i in range(m+1) for j in range(2*m+1,p) if i+j >= p) % p
        companion = sum(q[j]*pow(half,j,p) for j in range(2*m+1,p)) % p
        delta = ((f_value-val_h*val_h) % modulus)//(p*p)
        w_delta = ((w_value-val_h*(val_h+12*theta_h))%modulus)//(p*p)
        assert delta == (-2*tail) % p
        assert w_delta == (12*(theta_h%p)*companion-2*tail_weight) % p
        boundary = delta, tail, w_delta, tail_weight, companion
    # Independent original-binomial arithmetic for selected p.
    if p in (7,13,19,37,43,73,373):
        original = sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,modulus) for n in range(p)) % modulus
        assert original == w_value
    return first//(p*p), val_h%(p*p), theta_h%p, w_value, boundary


def main():
    ps = [p for p in range(7, 800) if p % 6 == 1 and isprime(p)]
    for p in ps:
        audit(p)
    p = 373
    k,h,th,w,boundary = audit(p)
    assert (k,h,th,w) == (138,8952,294,373)
    print(f"PASS_D25_CLAUSEN_P2_POLYNOMIAL {len(ps)} primes 7<=p<800; coefficientwise mod p^2; exact first p^3 obstruction")
    assert boundary == (241, 66, 1, 98, 252)
    print(f"P373: first missing coefficient at n=125 = {k}*373^2 mod 373^3; H(1/2) mod p^2={h}; theta_H mod p={th}; weighted_A mod p^3={w}")
    print(f"P373: unweighted defect/tail={boundary[0]}/{boundary[1]}; weighted defect/overflow={boundary[2]}/{boundary[3]}; J(1/2)={boundary[4]}")


if __name__ == "__main__":
    main()
