#!/usr/bin/env python3
"""Exact external elliptic differential gauge; not native H0/B0.

Uses the companion Q(sqrt2)/Fp2 theorem checker, preserving its field law.
"""
import json
from d25_cm_twist_216_2304_checker_20261103 import field_ops

rows = []
for p in (13, 19, 37, 43, 109, 373):
    mul, _, chi = field_ops(p)
    d, z, one = (0, 3 % p), (0, 0), (1, 0)
    def times(x, y):
        a, b = x
        c, e = y
        ac, be = mul(a, c), mul(mul(b, e), d)
        ae, bc = mul(a, e), mul(b, c)
        return (((ac[0] + be[0]) % p, (ac[1] + be[1]) % p),
                ((ae[0] + bc[0]) % p, (ae[1] + bc[1]) % p))
    def power(x, n):
        result = (one, z)
        while n:
            if n & 1:
                result = times(result, x)
            x = times(x, x)
            n //= 2
        return result
    u, q = (z, one), p*p
    eps = chi(d)
    uq = power(u, q)
    assert uq == (z, (eps % p, 0))
    assert power(u, q*q) == u
    rows.append(dict(p=p, q=q, chi_d=eps, u_q=[list(v) for v in uq],
                     u_in_base_field=(eps == 1),
                     scalar_differential_gauge="omega4=u^-1 omega3",
                     gauge_semilinear_ratio=eps))
print(json.dumps(dict(
    status="EXACT_Fp2_QUADRATIC_EXTENSION_GAUGE_PASS",
    source="EXTERNAL_CM_E3_E4_NOT_NATIVE_H0_B0",
    theorem="u^q=chi_Fp2(d)*u and omega4=u^-1 omega3 for u^2=d=3sqrt2",
    cases=rows), indent=2))
