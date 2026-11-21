"""Exact modular check of conditional C12 phase-local fiber-lift classification."""
import json
import math
import random
from pathlib import Path

MODULI = [6, 12, 24, 48, 96, 192]
SEED = 20261121
rng = random.Random(SEED)
checks = 0
mismatches = 0
examples = []


def check(condition, name):
    global checks, mismatches
    checks += 1
    if not condition:
        mismatches += 1
        if len(examples) < 10:
            examples.append(name)


def hclass(g, n):
    return sum(g) % n


def gauge(g, k, n):
    return [(g[q] + k[(q + 1) % 12] - k[q]) % n for q in range(12)]


def canonical_with_h(h, n):
    return [0] * 11 + [h % n]


def translate(g, q, steps, n):
    z = 0
    phase = q
    if steps >= 0:
        for _ in range(steps):
            z = (z + g[phase]) % n
            phase = (phase + 1) % 12
    else:
        for _ in range(-steps):
            phase = (phase - 1) % 12
            z = (z - g[phase]) % n
    return phase, z


for n in MODULI:
    for H in range(n):
        g = canonical_with_h(H, n)
        check(hclass(g, n) == H, f"H={H},n={n}")
        for q in range(12):
            check(translate(g, q, 12, n) == (q, H), f"canonical-holonomy n={n},H={H},q={q}")
            check(translate(g, q, -12, n) == (q, (-H) % n), f"reverse n={n},H={H},q={q}")
    for trial in range(300):
        g = [rng.randrange(n) for _ in range(12)]
        H = hclass(g, n)
        target = canonical_with_h(H, n)
        # Solve gauge relation target[q] = g[q] + k[q+1]-k[q].
        k = [0]
        for q in range(11):
            k.append((k[-1] + target[q] - g[q]) % n)
        check(gauge(g, k, n) == target, f"gauge-existence n={n},trial={trial}")
        check(hclass(gauge(g, k, n), n) == H, f"gauge-holonomy n={n},trial={trial}")
        for q in (0, 5, 11):
            check(translate(g, q, 12, n) == (q, H), f"arbitrary-holonomy n={n},trial={trial},q={q}")

for m in range(7):
    n = 6 * (1 << m)
    gamma = [3 if q in (5, 11) else 0 for q in range(12)]
    h = sum(gamma) % n
    order = n // math.gcd(n, h)
    check(order == (1 << m), f"gamma-winding-order m={m}")
    check(translate(gamma, 0, 12, n) == (0, h), f"gamma-holonomy m={m}")
    zero = [0] * 12
    check(translate(zero, 0, 12, n) == (0, 0), f"trivial-holonomy m={m}")
    check((h == 0) if m == 0 else (h != 0), f"distinction-at-m>=1 m={m}")

output = {
    "schema": "X6_TIME_PHASE_FIBER_IDENTIFIABILITY_CHECK_V1",
    "date": "2026-11-21",
    "research_role": "TASK_RESEARCH",
    "source_scope": "FROZEN OUTER C12 / STATIC PRINCIPAL ROOT; FIBER LIFTS ARE CONDITIONAL",
    "moduli": MODULI,
    "random_seed": SEED,
    "random_trials_per_modulus": 300,
    "checks": checks,
    "mismatches": mismatches,
    "first_mismatches": examples,
    "gamma_loop_orders": [{"m": m,"modulus":6*(1<<m),"holonomy":6%(6*(1<<m)),"loop_classes":1<<m} for m in range(7)],
    "claim_scope": "Finite test supports algebraic gauge classification; proof is separate. No physical fiber motion established.",
}
Path(__file__).with_name('x6_time_phase_fiber_classification_results_20261121.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:output[k] for k in ['checks','mismatches','moduli','gamma_loop_orders']}, ensure_ascii=False))
assert mismatches == 0, examples
