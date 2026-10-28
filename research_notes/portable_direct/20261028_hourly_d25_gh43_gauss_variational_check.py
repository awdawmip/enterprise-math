#!/usr/bin/env python3
"""Exact modular verification of GH-43, not a formal/native proof."""


def primes_below(n):
    marked = bytearray(n)
    for k in range(2, int(n**0.5)+1):
        if not marked[k]:
            for j in range(k*k, n, k):
                marked[j] = 1
    return [k for k in range(7, n) if not marked[k] and k % 4 == 3]


def verify(p):
    d = (p-3)//4
    mod = p*p
    def inv(n):
        assert n % p
        return pow(n % mod, -1, mod)
    a = [1]
    beta = [1]
    h = [0]
    for r in range(d):
        a.append(a[-1]*(8*r+1)**2*inv(16*(4*r+3)*(r+1)) % mod)
        beta.append(beta[-1]*16*(r+1)*(4*r+3)*inv((8*r+13)**2) % mod)
        h.append((h[-1]+4*inv(8*r+13)-inv(4*r+4)-inv(4*r+3)) % p)
    gamma = [a[d-r]*inv(a[d]) % mod for r in range(d+1)]
    assert all((gamma[r]-beta[r]*(1+p*h[r])) % mod == 0 for r in range(d+1))

    # Exact terminating parameter-shifted rank-3 operator L_p modulo p^2.
    # Its coefficient at degree d+1 vanishes, not just modulo p.
    lp = []
    for n in range(d+2):
        v = 0
        if n <= d:
            v += n*((8*n+5)*inv(8)-p*inv(4))**2*gamma[n]
        if n >= 1:
            v -= n*(n-p*inv(4))*( (4*n-1)*inv(4)-p*inv(4))*gamma[n-1]
        lp.append(v % mod)
    assert all(x == 0 for x in lp), (p,"L_p",[(i,x) for i,x in enumerate(lp) if x][:5])

    # First-jet forced tangent at p=0. L_0 tildeV + L_1 V =
    # (d+1)^2 beta_d/4 * u^(d+1) modulo p.
    tangent = [beta[r]*h[r] % p for r in range(d+1)]
    coeff = []
    for n in range(d+2):
        v = 0
        if n <= d:
            v += n*(8*n+5)**2*inv(64)*tangent[n]
            v -= n*(8*n+5)*inv(16)*beta[n]
        if n >= 1:
            v -= n*n*(4*n-1)*inv(4)*tangent[n-1]
            v += n*(8*n-1)*inv(16)*beta[n-1]
        coeff.append(v % p)
    assert all(x == 0 for x in coeff[:d+1])
    assert coeff[d+1] == (d+1)**2*inv(4)*beta[d] % p
    assert coeff[d+1] != 0
    return p, coeff[d+1]


def main():
    primes = primes_below(2000)
    results = [verify(p) for p in primes]
    assert len(results) == 154
    print("PASS_GH43_EXACT_TERMINATING_PARAMETER_DEFORMATION",len(results),"primes, mod p^2")
    print("PASS_GH43_FORCED_VARIATIONAL_JET",len(results),"primes, mod p")
    print("SAMPLE_BOUNDARY",[x for x in results if x[0] in (7,11,19,43,67,127)])

if __name__ == '__main__':
    main()
