#!/usr/bin/env python3
"""Frozen R5: exact finite-field numerator/first Euler-jet witness, m=1..37.
No floating point, no packages. Produces R5_O1_MODULAR_CERTIFICATE.json.
Proof of complex nonvanishing from a nonzero mod-p primitive-root evaluation:
if Phi_d divides integer R, all reductions at primitive dth roots vanish;
if Phi_d^2 divides R, the Euler derivative also vanishes there.
A zero mod-p at d=43,m=37 is not an exact vanishing proof; see RESEARCH.md.
"""
import json
import math
from pathlib import Path

S = [
    list(range(214, 219)),
    [214, 216, 217, 218, 219, 220, 221],
    list(range(215, 222)),
    list(range(223, 291)),
    list(range(296, 313)),
]
W = [7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 32, 37, 43]
L = 229746052653717600


def prime_factors(n):
    out = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            out.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        out.append(n)
    return out


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, math.isqrt(n)+1))


def primitive_root(d):
    P = 10001
    while P % d != 1 or not is_prime(P):
        P += 1
    for b in range(2, P):
        w = pow(b, (P-1)//d, P)
        if all(pow(w, d//ell, P) != 1 for ell in prime_factors(d)):
            assert pow(w, d, P) == 1
            return P, w
    raise AssertionError("primitive d-th root not found")


def calc(m, d):
    cap = m-1
    P, w = primitive_root(d)
    xp = [pow(w, p % d, P) for p in range(315)]

    # A jet is (f, q df/dq), evaluated at q=w.
    def add(a, b):
        return ( (a[0]+b[0])%P, (a[1]+b[1])%P )
    def sub(a, b):
        return ( (a[0]-b[0])%P, (a[1]-b[1])%P )
    def mul(a, b):
        return ( a[0]*b[0]%P, (a[1]*b[0]+a[0]*b[1])%P )

    one, zero = (1,0), (0,0)

    def product_factors(ps):
        z = one
        for p in ps:
            z = mul(z, ((1-xp[p])%P, (-p*xp[p])%P))
        return z

    def single(ps):
        # [u^r] product_p (1-u*q^p)^(-1), truncated to r<=cap
        h = [one] + [zero]*cap
        for p in ps:
            t = (xp[p], p*xp[p]%P)
            for r in range(1, cap+1):
                h[r] = add(h[r], mul(t, h[r-1]))
        q = zero
        for v in h:
            q = add(q, v)
        return mul(q, product_factors(ps))

    def core_intersection(indices):
        U = sorted(set().union(*(S[i] for i in indices)))
        n = len(indices)
        dp = {(0,)*n: one}
        for p in U:
            affected = [k for k, i in enumerate(indices) if p in S[i]]
            next_dp = {}
            t = (xp[p], p*xp[p]%P)
            for counts, value in dp.items():
                limit = min(cap-counts[k] for k in affected)
                new_value = value
                for r in range(limit+1):
                    next_counts = tuple(
                        counts[k]+(r if k in affected else 0)
                        for k in range(n)
                    )
                    next_dp[next_counts] = add(
                        next_dp.get(next_counts, zero), new_value
                    )
                    new_value = mul(new_value, t)
            dp = next_dp
        q = zero
        for value in dp.values():
            q = add(q, value)
        return mul(q, product_factors(U))

    A = zero
    for mask in range(1, 8):
        indices = [i for i in range(3) if mask >> i & 1]
        term = core_intersection(indices)
        A = add(A, term) if len(indices)%2 else sub(A, term)

    B = single(S[3])
    C = single(S[4])
    R = sub(one, mul(mul(sub(one, A), sub(one, B)), sub(one, C)))
    nd = sum(p%d == 0 for p in range(214, 315))
    witness = nd>=3 and (R[0]!=0 or (nd>=4 and R[1]!=0))
    return {
        "m": m, "d": d, "p": P, "root": w, "pole": nd,
        "R0": R[0], "DR0": R[1], "witness": bool(witness)
    }


def main():
    assert math.lcm(*W) == L
    candidates = [d for d in range(1, 315)
                  if sum(p%d == 0 for p in range(214, 315)) >= 3]
    assert len(candidates) == 40 and math.lcm(*candidates) == L
    assert [d for d in candidates if d%43 == 0] == [43]

    rows = []
    for m in range(1, 38):
        current = [calc(m, d) for d in W]
        passed = [r["d"] for r in current if r["witness"]]
        assert passed == (W if m<=36 else W[:-1]), (m, passed)
        if m == 37:
            assert current[-1]["R0"] == 0
        rows.extend(current)
        print("PASS", m, len(passed), "witnesses", flush=True)

    report = {
        "schema": "R5_O1_FINITE_FIELD_FIRST_CONTRACTION_CERT_V1",
        "frozen_input":
            "enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15",
        "tested_m": list(range(1, 38)),
        "candidate_order_count": len(candidates),
        "upper_L": L,
        "m37_exact_period": L//43,
        "rows": rows
    }
    content = json.dumps(report, sort_keys=True, indent=2) + "\n"
    Path(__file__).with_name("R5_O1_MODULAR_CERTIFICATE.json").write_text(
        content, encoding="utf-8"
    )
    print("ALL CHECKS PASS; 518 finite-field jets; output size", len(content))


if __name__ == "__main__":
    main()
