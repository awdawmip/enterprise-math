"""R287: independent exact finite checks for two all-length algebraic lemmas.

Only the GF identities and positivity-of-formal-series arguments prove infinite claims;
this script checks their coefficients and raw six-edge BRC source words exactly.
"""
import json
from collections import defaultdict

N = 600
L = 140
K = 24
HDEG = L // 2 + 3
TRANSITIONS = (
    ((2, -1, -1), (2, 1, -1)),
    ((0, -1, -1), (0, 1, -1)),
    ((1, 1, 1), (2, 1, -1)),
)


def multiply(a, b, degree):
    result = [0] * (degree + 1)
    for i, ai in enumerate(a[:degree + 1]):
        if ai:
            for j, bj in enumerate(b[:degree + 1 - i]):
                if bj:
                    result[i + j] += ai * bj
    return result


# h=y^4+(y+2*y^2+y^3+y^4)*h+y*(1+y)^2*h^2.
h = [0] * (HDEG + 1)
for degree in range(1, HDEG + 1):
    h[degree] = int(degree == 4)
    h[degree] += sum(weight * h[degree - offset]
                     for offset, weight in ((1, 1), (2, 2), (3, 1), (4, 1))
                     if degree >= offset)
    for offset, weight in ((1, 1), (2, 2), (3, 1)):
        if degree >= offset:
            h[degree] += weight * sum(
                h[j] * h[degree - offset - j]
                for j in range(degree - offset + 1)
            )
assert h[:4] == [0] * 4 and all(z > 0 for z in h[4:])
one = [1] + [0] * HDEG
v = multiply([1, 1], [1 + h[0]] + h[1:], HDEG)
u2 = multiply(v, v, HDEG)  # u(x)^2 = x^2*u2(x^2)

states = {(0, 1, 0, False): 1}
raw_words_checked = 0
reflection_checks = 0
reflection_strict = 0
families = {(eps, m): [] for eps in (1, -1) for m in range(1, K + 3)}
neg_witnesses = {}
base_ranges = {(1, 13): 0, (1, 14): 0, (-1, 11): 0, (-1, 12): 0}

for n in range(N + 1):
    P = defaultdict(int)
    for (q, eps, k, last_zero), count in states.items():
        if q == 0:
            P[(eps, k)] += count

    if n <= 14:
        raw = defaultdict(int)
        for word in range(1 << n):
            q, eps, k, last_zero = 0, 1, 0, False
            for bitpos in range(n - 1, -1, -1):
                bit = (word >> bitpos) & 1
                if last_zero and bit == 0:
                    break
                q, eta, step = TRANSITIONS[q][bit]
                eps, k, last_zero = eta * eps, eta * k + step, bit == 0
            else:
                if q == 0:
                    raw[(eps, k)] += 1
        assert dict(raw) == dict(P), (n, 'raw mismatch')
        raw_words_checked += 1 << n

    if n <= L:
        for key in families:
            families[key].append(P[(key[0], -key[1])])

    for k in range(1, n + 1):
        for eps in (1, -1):
            gap = P[(eps, -k)] - P[(eps, k)]
            if eps == 1:
                j = (n - k - 2) // 2
                strict = n >= k + 2 and (n - k) % 2 == 0 and (j <= k - 1 or j >= 4)
            elif k == 1:
                strict = n == 7 or (n >= 13 and n % 2 == 1)
            else:
                j = (n - k - 2) // 2
                strict = n >= k + 2 and (n - k) % 2 == 0 and (k >= 3 or j != 1)
            assert gap >= 0 and (gap > 0) == strict, (n, eps, k, gap, strict)
            reflection_checks += 1
            reflection_strict += int(gap > 0)

    for eps, m in base_ranges:
        if n >= m and (n - m) % 2 == 0:
            base_ranges[(eps, m)] += 1
            assert P[(eps, -m)] >= P[(eps, -m - 2)], ('base finite witness failure', n, eps, m)

    if (eps_m := {23: (1, 11), 24: (1, 12), 19: (-1, 9), 20: (-1, 10)}.get(n)):
        eps, m = eps_m
        left, right = P[(eps, -m)], P[(eps, -m - 2)]
        assert left < right
        neg_witnesses[f'{eps}:{m}:{n}'] = [left, right, left - right]

    nxt = defaultdict(int)
    for (q, eps, k, last_zero), count in states.items():
        for bit, (qnext, eta, step) in enumerate(TRANSITIONS[q]):
            if last_zero and bit == 0:
                continue
            nxt[(qnext, eta * eps, eta * k + step, bit == 0)] += count
    states = nxt

kernel_checks = 0
for eps in (1, -1):
    for m in range(1 if eps == 1 else 2, K + 1):
        source = families[(eps, m)]
        target = families[(eps, m + 2)]
        for n in range(L + 1):
            predicted = sum(
                u2[j] * source[n - 2 - 2 * j]
                for j in range((n - 2) // 2 + 1)
            ) if n >= 2 else 0
            assert target[n] == predicted, ('kernel mismatch', eps, m, n)
            kernel_checks += 1

result = {
    'schema': 'EM_R287_SHARP_REFLECTION_AND_TAIL_LADDER_V1',
    'method': 'raw words; independent six-edge exact DP; positive formal-series recursion',
    'integer_arithmetic': 'Python unbounded signed integers',
    'max_raw_word_length': 14,
    'raw_words_checked': raw_words_checked,
    'max_dp_length': N,
    'sharp_reflection_support_checks': reflection_checks,
    'strict_reflection_cases': reflection_strict,
    'tail_kernel_exact_checks': kernel_checks,
    'kernel_max_length': L,
    'candidate_base_series_checked_only_through_length': N,
    'candidate_base_length_layer_counts': {f'{e}:{m}': count for (e, m), count in base_ranges.items()},
    'negative_tail_witnesses': neg_witnesses,
    'scope_warning': 'finite base-series positivity checks do NOT establish coefficientwise all-length positivity',
    'status': 'PASS',
}
print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
