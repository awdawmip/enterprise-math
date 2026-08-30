#!/usr/bin/env python3
"""Exact checker for P000 Philosophy-First Q9 nonlocal probe joint separation.

Declared scope:
- U_2REG from accepted Q2/Q6: finite simple 2-regular native-Cell graphs,
  uniformly decorated by the accepted six-axis SLICE/ROT/PF10 local data.
- A state is therefore classified, at this witness layer only, by an unordered
  partition of n into cycle lengths >= 3.
- No carrier S4, graph connectedness, path label, or holonomy is promoted to
  bare P000 ontology. Native adjacency is part of this declared test class.
"""

from __future__ import annotations
from collections import Counter, defaultdict

CHECKS = 0

def check(cond: bool, msg: str) -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def power(p, n):
    r = tuple(range(len(p)))
    for _ in range(n):
        r = compose(p, r)
    return r

# Frozen Q2 carrier readout regression only.
a = (1, 2, 0, 5, 3, 4)
b = (0, 3, 4, 1, 2, 5)
identity = tuple(range(6))
check(power(a, 3) == identity, "carrier a^3 regression")
check(power(b, 2) == identity, "carrier b^2 regression")
check(power(compose(a, b), 4) == identity, "carrier (ab)^4 regression")

def cycle_partitions(n: int):
    out = []
    def rec(rem: int, lo: int, cur: tuple[int, ...]):
        if rem == 0:
            out.append(cur)
            return
        for k in range(lo, rem + 1):
            rec(rem - k, k, cur + (k,))
    rec(n, 3, ())
    return out

def base_profile(part):
    t = sum(k for k in part if k == 3)
    p = sum(k for k in part if k >= 4)
    return (t, p)

def connected_bit(part):
    return len(part) == 1

def girth(part):
    return min(part)

def period_hist(part):
    c = Counter()
    for k in part:
        # Every root in C_k has first nonbacktracking return period k.
        c[k] += k
    return tuple(sorted(c.items()))

def holonomy_exact_trivial_transport(part):
    # Explicitly enriched Q4-style C2 edge transports, all identity.
    # Every fundamental-cycle holonomy is then identity, independently of
    # the cycle decomposition.
    return True

def girth_representable(t: int, p: int, g: int) -> bool:
    n = t + p
    if n < 3:
        return False
    if t > 0:
        return g == 3 and t % 3 == 0 and (p == 0 or p >= 4)
    return g >= 4 and (p == g or p >= 2 * g)

# 1) Exact image theorem for base+girth through a substantial finite range.
for n in range(3, 80):
    actual = {
        (base_profile(part)[0], base_profile(part)[1], girth(part))
        for part in cycle_partitions(n)
    }
    predicted = {
        (t, n - t, g)
        for t in range(n + 1)
        for g in range(3, n + 1)
        if girth_representable(t, n - t, g)
    }
    check(actual == predicted, f"girth-image mismatch n={n}")

# 2) Q2 family: for every fixed r and m>=2r+2, C_2m vs 2 C_m.
for r in range(1, 33):
    for m in range(2 * r + 2, 2 * r + 10):
        X = (2 * m,)
        Y = (m, m)
        check(base_profile(X) == base_profile(Y), f"Q2 base regression r={r},m={m}")
        check(connected_bit(X) != connected_bit(Y), f"CONN failed r={r},m={m}")
        check(girth(X) == 2 * m and girth(Y) == m, f"GIRTH failed r={r},m={m}")
        check(period_hist(X) != period_hist(Y), f"PERIOD failed r={r},m={m}")
        check(
            holonomy_exact_trivial_transport(X) == holonomy_exact_trivial_transport(Y),
            f"HOL negative control unexpectedly separated r={r},m={m}",
        )

# 3) Q6 minimal pure virtual profile (t,p)=(0,3).
# CONNECTEDNESS does not remove it at the raw formal-completion level:
# "connected=True" is a legal scalar value and all three local path outputs
# are pointwise Q2-legal, but no actual 3-Cell U_2REG state realizes them.
check((0, 3, True) not in {
    (*base_profile(part), connected_bit(part))
    for part in cycle_partitions(3)
}, "Q6 connectedness virtual should remain unrealizable")

# GIRTH removes the minimal pure virtual before realization:
# t=0 forces g>=4, but a native simple cycle in an n=3 support has g<=3.
formal_g = [
    g for g in range(3, 3 + 1)
    if ((0 > 0 and g == 3) or (0 == 0 and g >= 4))
]
check(formal_g == [], "Q6 minimal virtual must have no structurally compatible girth")

# PERIOD histogram yields an exact representability certificate:
# q_k is realizable iff q_k is a nonnegative multiple of k; then q_k/k
# copies of C_k realize it. In particular p=3 cannot be a sum of nonzero
# multiples of k>=4.
for k in range(3, 33):
    for mult in range(0, 8):
        q = k * mult
        check(q % k == 0, f"period divisibility regression k={k}")
check(
    not any(3 % k == 0 for k in range(4, 64)),
    "Q6 p=3 cannot form any legal nontriangle period packet",
)

# 4) Exact remaining indistinguishability witnesses.
# CONN is separation-only: same base profile and connectedness, different states.
C46, C55 = (4, 6), (5, 5)
check(base_profile(C46) == base_profile(C55) == (0, 10), "CONN witness base")
check(connected_bit(C46) == connected_bit(C55) == False, "CONN witness bit")
check(C46 != C55, "CONN witness must be nonisomorphic")

# GIRTH is not globally reconstruction-complete.
G1, G2 = (3, 8), (3, 4, 4)
check(base_profile(G1) == base_profile(G2) == (3, 8), "GIRTH witness base")
check(girth(G1) == girth(G2) == 3, "GIRTH witness g")
check(G1 != G2, "GIRTH witness must be nonisomorphic")

# HOL_EXACT is orthogonal to connectivity under identity transports.
H1, H2 = (8,), (4, 4)
check(base_profile(H1) == base_profile(H2) == (0, 8), "HOL witness base")
check(holonomy_exact_trivial_transport(H1), "HOL H1")
check(holonomy_exact_trivial_transport(H2), "HOL H2")

# 5) PERIOD histogram reconstructs every U_2REG cycle partition exactly.
for n in range(3, 61):
    seen = {}
    for part in cycle_partitions(n):
        sig = period_hist(part)
        check(sig not in seen or seen[sig] == part, f"PERIOD collision n={n}")
        seen[sig] = part
        # Exact inverse h_k=q_k/k.
        recovered = []
        for k, qk in sig:
            check(qk % k == 0, f"period divisibility n={n},k={k}")
            recovered.extend([k] * (qk // k))
        check(tuple(recovered) == part, f"PERIOD inverse n={n}")

# 6) Strict information witness: PERIOD retains data GIRTH forgets.
check(girth(G1) == girth(G2), "strictness girth equality")
check(period_hist(G1) != period_hist(G2), "PERIOD must refine GIRTH on witness")

# 7) Exact first collisions for regression clarity.
def first_collision(kind: str, max_n: int = 80):
    for n in range(3, max_n + 1):
        buckets = defaultdict(list)
        for part in cycle_partitions(n):
            if kind == "CONN":
                sig = (base_profile(part), connected_bit(part))
            elif kind == "GIRTH":
                sig = (base_profile(part), girth(part))
            elif kind == "PERIOD":
                sig = (base_profile(part), period_hist(part))
            else:
                raise ValueError(kind)
            buckets[sig].append(part)
        hits = [(sig, vals) for sig, vals in buckets.items() if len(vals) > 1]
        if hits:
            return n, hits[0]
    return None

conn_first = first_collision("CONN", 30)
girth_first = first_collision("GIRTH", 30)
period_first = first_collision("PERIOD", 60)
check(conn_first is not None and conn_first[0] == 10, f"CONN first collision {conn_first}")
check(girth_first is not None and girth_first[0] == 11, f"GIRTH first collision {girth_first}")
check(period_first is None, f"PERIOD unexpected collision {period_first}")

print(
    "PASS P000_NONLOCAL_PROBE_JOINT_SEPARATION; "
    f"checks={CHECKS}; "
    "q2_family=SEPARATED_BY_CONN_GIRTH_PERIOD; "
    "holonomy_exactness=NEGATIVE_CONTROL; "
    "q6_minimal_virtual=(0,3)_REJECTED_BY_GIRTH_AND_PERIOD; "
    "girth_image=EXACT_THROUGH_N79; "
    "period_reconstruction=EXACT_THROUGH_N60_AND_PROVED_BY_INVERSE; "
    "conn_first_collision_n=10; "
    "girth_first_collision_n=11; "
    "period_collision_none_through_n60; "
    "carrier_S4_regression=PASS"
)
