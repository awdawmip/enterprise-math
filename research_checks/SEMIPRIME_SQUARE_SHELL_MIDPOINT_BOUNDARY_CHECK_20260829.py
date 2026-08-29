#!/usr/bin/env python3
"""Exact/reproducible checks for RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION.

Standard-library only.  The exhaustive census covers every odd nonsquare
semiprime p*q <= 10^7 with distinct odd primes p<q.
"""
from __future__ import annotations

import bisect
import json
import math
from dataclasses import dataclass

N_MAX = 10_000_000
EXPECTED_COUNT = 1_555_366
EXPECTED = {
    "u_logT": 0.007396541311027859,
    "u_TA0": -0.00021884091597129568,
    "u_logratio": 0.0026841966118056936,
    "u_logJp": 0.01759633089976119,
    "gap_logT": 0.052660459997740335,
    "gap_TA0": 0.041608227429015855,
    "gap_logratio": 0.026642424632977862,
    "gap_logJp": 0.1139426530102694,
}
COUNTEREXAMPLES = (
    (9917459, 3079, 3221, 3149, 5041, 0),
    (9917461, 1009, 9829, 3149, 5039, 2269),
    (9990157, 3119, 3203, 3160, 1764, 0),
    (9990159, 3, 3330053, 3160, 1762, 1661867),
    (5157223, 2203, 2341, 2270, 218, 1),
    (9979063, 1013, 9851, 3158, 218, 2273),
)


def sieve(n: int) -> list[int]:
    a = bytearray(b"\x01") * (n + 1)
    a[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if a[p]:
            a[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(a) if flag]


@dataclass
class Corr:
    n: int = 0
    sx: float = 0.0
    sy: float = 0.0
    sxx: float = 0.0
    syy: float = 0.0
    sxy: float = 0.0

    def add(self, x: float, y: float) -> None:
        self.n += 1
        self.sx += x
        self.sy += y
        self.sxx += x * x
        self.syy += y * y
        self.sxy += x * y

    def value(self) -> float:
        n = float(self.n)
        vx = self.sxx - self.sx * self.sx / n
        vy = self.syy - self.sy * self.sy / n
        cov = self.sxy - self.sx * self.sy / n
        return cov / math.sqrt(vx * vy)


def main() -> int:
    primes = sieve(N_MAX // 3 + 100)
    small_limit = math.isqrt(N_MAX) + 100
    small_primes = primes[: bisect.bisect_right(primes, small_limit)]

    cs = {name: Corr() for name in EXPECTED}
    count = 0
    bridge_failures = 0
    shell_failures = 0
    multik_failures = 0
    observed_examples: dict[int, tuple[int, int, int, int, int]] = {}

    for i, p in enumerate(primes):
        if p < 3:
            continue
        if p * p > N_MAX:
            break
        j_end = bisect.bisect_right(primes, N_MAX // p)
        for q in primes[i + 1 : j_end]:
            N = p * q
            s = math.isqrt(N)
            A0 = s + 1
            a = N - s * s
            b = A0 * A0 - N
            L = 2 * s + 1
            D = b - a
            A = (p + q) // 2
            B = (q - p) // 2
            T = A - A0

            if a + b != L or 4 * N - 1 != L * L - 2 * D:
                shell_failures += 1
            if B * B != b + 2 * A0 * T + T * T:
                bridge_failures += 1

            # pi(s)-pi(p), using the precomputed prime list only as an oracle label.
            pi_s = bisect.bisect_right(small_primes, s)
            pi_p = bisect.bisect_right(small_primes, p)
            Jp = pi_s - pi_p

            j = bisect.bisect_right(small_primes, s)
            prevp = small_primes[j - 1]
            nextp = small_primes[j]
            gap = (s - prevp) + (nextp - s)

            u = b / L
            logT = math.log1p(T)
            tnorm = T / A0
            logr = math.log(q / p)
            logJ = math.log1p(Jp)

            cs["u_logT"].add(u, logT)
            cs["u_TA0"].add(u, tnorm)
            cs["u_logratio"].add(u, logr)
            cs["u_logJp"].add(u, logJ)
            cs["gap_logT"].add(gap, logT)
            cs["gap_TA0"].add(gap, tnorm)
            cs["gap_logratio"].add(gap, logr)
            cs["gap_logJp"].add(gap, logJ)

            # Deterministic sparse audit of the task's exact multi-k transport law.
            if count % 4093 == 0:
                D1 = D
                for k in (2, 3, 5, 7, 11, 16, 31):
                    sk = math.isqrt(k * N)
                    Lk = 2 * sk + 1
                    ak = k * N - sk * sk
                    bk = (sk + 1) * (sk + 1) - k * N
                    Dk = bk - ak
                    rhs = k * D1 + (Lk * Lk - k * L * L + 1 - k) // 2
                    if Dk != rhs:
                        multik_failures += 1

            if N in {x[0] for x in COUNTEREXAMPLES}:
                observed_examples[N] = (p, q, s, b, T)

            count += 1

    got = {name: corr.value() for name, corr in cs.items()}
    max_corr_error = max(abs(got[k] - EXPECTED[k]) for k in EXPECTED)

    example_failures = []
    for N, p, q, s, b, T in COUNTEREXAMPLES:
        if observed_examples.get(N) != (p, q, s, b, T):
            example_failures.append(N)

    result = {
        "schema": "SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK_V1",
        "N_max": N_MAX,
        "count": count,
        "expected_count": EXPECTED_COUNT,
        "shell_identity_failures": shell_failures,
        "bridge_identity_failures": bridge_failures,
        "multik_transport_failures": multik_failures,
        "counterexample_failures": example_failures,
        "correlations": got,
        "max_correlation_error": max_corr_error,
        "status": "PASS"
        if (
            count == EXPECTED_COUNT
            and shell_failures == 0
            and bridge_failures == 0
            and multik_failures == 0
            and not example_failures
            and max_corr_error < 1e-8
        )
        else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
