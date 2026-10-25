#!/usr/bin/env python3
"""R287 auxiliary BRC: independent exact-integer checks, not an infinite theorem prover."""
from collections import defaultdict
from math import comb
from json import dumps
from pathlib import Path

TRANS = {
    0: {0: (2, -1, -1), 1: (2, 1, -1)},
    1: {0: (0, -1, -1), 1: (0, 1, -1)},
    2: {0: (1, 1, 1), 1: (2, 1, -1)},
}
def apply(word):
    q, eps, k, clean, last = 0, 1, 0, True, 1
    increments = []
    for bit in word:
        before = eps
        qnew, eta, c = TRANS[q][bit]
        eps, k = eta * eps, eta * k + c
        inc = before * eta * c
        assert inc == (before if bit == 0 else -before)
        increments.append(inc)
        clean &= not (last == 0 and bit == 0)
        q, last = qnew, bit
    return q, eps, k, clean, tuple(increments)

def fibs(N):
    a = [0, 1]
    for _ in range(2, N + 1):
        a.append(a[-1] + a[-2])
    return a

word_count = 0
for n in range(16):
    seen = set()
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        key = apply(bits)[-1]
        assert key not in seen
        seen.add(key)
        word_count += 1

state = {(0, 1, 0, 1): 1}
F = fibs(261)
levels = 261
coefficients_checked = 0
support_checked = 0
binomial_checked = 0
last_high_cone_peak = None
for n in range(levels):
    P = defaultdict(int)
    for (q, e, k, last), count in state.items():
        if q == 0:
            P[e, k] += count
    total = sum(P.values())
    if n == 0:
        assert total == 1
    else:
        delta = (3, -1, -3, 1)[n % 4]
        formula = (F[n] + 2 * F[n - 1] + delta) // 5
        assert (F[n] + 2 * F[n - 1] + delta) % 5 == 0
        assert total == formula, (n, total, formula)
    top = max(P.values(), default=0)
    for (e, k), c in P.items():
        assert abs(k) <= n and (k - n) % 2 == 0
        support_checked += 1
        assert c <= comb(n, (n + e * k) // 2)
        binomial_checked += 1
        if n >= 10 and 3 * abs(k) >= 2 * n and c == top:
            last_high_cone_peak = n
    coefficients_checked += len(P)
    ns = defaultdict(int)
    for (q, e, k, last), count in state.items():
        for bit in (0, 1):
            if bit == 0 and last == 0:
                continue
            nq, eta, c = TRANS[q][bit]
            ns[nq, e * eta, eta * k + c, bit] += count
    state = ns

assert 6**6 * 50**6 < 79**6 * 5**5
N, K = 900, 12
base_margin = sum(comb(N, j) * 79**(K - j) for j in range(K + 1)) - 60 * (N + 1) * 79**K
assert base_margin > 0
assert 80 * (N + 1) > 79 * (N + 2)
result = {
    "status": "PASS", "model": "positive_ordered_six_edge_clean_BRC_auxiliary",
    "source_word_injection": {"exhaustive_lengths": [0, 15], "words": word_count},
    "independent_DP": {"lengths": [0, levels - 1], "effect_fibres_checked": coefficients_checked,
                       "support_checked": support_checked, "binomial_envelope_checked": binomial_checked,
                       "total_clean_reset_exact_formula_checked": levels,
                       "highest_observed_peak_in_two_thirds_cone_at_n_ge_10": last_high_cone_peak},
    "exact_certificates": {
        "entropy_rational_base_margin": 79**6 * 5**5 - 6**6 * 50**6,
        "truncated_binomial_900_12_margin": str(base_margin),
        "ratio_900_to_901_margin": 80*(N+1)-79*(N+2),
        "theorem_n0": 900, "outer_cone": "3*abs(k)>=2*n"
    },
    "infinite_statement_support": "written_combinatorial_and_rational_induction_proof_not_DP_extrapolation",
    "formal_checker": "not_run", "independent_driver_review": "not_run"
}
Path(__file__).with_name("EXACT_EVIDENCE.json").write_text(dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(dumps(result, ensure_ascii=False, indent=2))
