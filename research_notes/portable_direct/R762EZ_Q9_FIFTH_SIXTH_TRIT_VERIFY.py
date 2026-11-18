#!/usr/bin/env python3
"""R762EZ: exact integer q=9 full-three-coordinate BRC, h=5 and h=6."""
import hashlib
import json

Q = 9
BRANCHES = ((0, 0, 0), (1, 0, 0), (0, 0, 1),
            (1, 1, 0), (0, 1, 1), (1, 1, 1))
CASES = ((5, 1458, 20, 486), (6, 4374, 22, 1458))
ORDER = 127
F = lambda n: max(0, n // 3 - 2)
LAST = max(T + N + ORDER - 1 for h, T, N, prev in CASES)
K = F(LAST) + 6
MOD = 3 ** K

def index(x, y, z):
    return (x * Q + y) * Q + z

SHIFTS = [tuple(index((x - a) % Q, (y - b) % Q, (z - c) % Q)
                for x in range(Q) for y in range(Q) for z in range(Q))
          for a, b, c in BRANCHES]

def witness(a, b):
    i = next(i for i in range(Q ** 3) if a[i] != b[i])
    return {"index": i, "xyz": [i // 81, (i // 9) % 9, i % 9],
            "left": a[i], "right": b[i]}

def calculate():
    v = [0] * (Q ** 3)
    v[0] = 1
    s = []
    powers = [3 ** i for i in range(K + 1)]
    for n in range(LAST + 1):
        assert sum(v) % MOD == pow(6, n, MOD), ("mass", n)
        divisor = powers[F(n)]
        assert all(x % divisor == 0 for x in v), ("divisibility", n)
        s.append(tuple((x // divisor) % 729 for x in v))
        if n < LAST:
            v = [sum(v[p[i]] for p in SHIFTS) % MOD
                 for i in range(Q ** 3)]
    result = {"schema": "R762EZ_Q9_H5_H6_EXACT_V1",
              "model": "six-named positive BRC; complete (Z/9Z)^3",
              "q": Q, "recurrence_order": ORDER,
              "last_power": LAST, "fixed_modulus_exponent": K,
              "mass_checks": LAST + 1,
              "divisibility_checks": (LAST + 1) * Q ** 3,
              "cases": [], "status": "PASS"}
    for h, T, N, prev in CASES:
        p = 3 ** h
        def state(n):
            return tuple(x % p for x in s[n])
        for n in range(N, N + ORDER):
            assert state(n) == state(n + T), ("period_window", h, n)
        old = state(N - 1)
        new = state(N - 1 + T)
        assert old != new, ("sharp_preperiod", h)
        earlier = next(n for n in range(N, N + ORDER)
                       if state(n) != state(n + prev))
        pairs = ((state(n), state(n + T)) for n in range(N, N + ORDER))
        digest = hashlib.sha256()
        for left, right in pairs:
            for x in left + right:
                digest.update(x.to_bytes(2, "little"))
        result["cases"].append({"h": h, "modulus": p,
            "minimum_eventual_period": T, "exact_preperiod": N,
            "window_start": N, "window_end": N + ORDER - 1,
            "compared_full_vectors": ORDER,
            "compared_coefficients": ORDER * Q ** 3,
            "exclude_previous_period": {"n": earlier,
                "compare_n": earlier + prev,
                **witness(state(earlier), state(earlier + prev))},
            "preperiod_sharp": {"n": N - 1,
                "compare_n": N - 1 + T, **witness(old, new)},
            "window_pairs_le_uint16_sha256": digest.hexdigest()})
    return result

if __name__ == "__main__":
    print(json.dumps(calculate(), sort_keys=True, indent=2))
