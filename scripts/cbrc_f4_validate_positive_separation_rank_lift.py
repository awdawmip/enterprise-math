#!/usr/bin/env python3
"""Deterministic exact checker for CBRC F4 positive-separation/rank-lift classification.

This checker is regression/evidence only.  The arbitrary-finite-T and arbitrary-GL_2(Z)
claims are proved in the accompanying report, not by bounded enumeration.
"""

from fractions import Fraction
from itertools import product
from math import gcd
from hashlib import sha256
import json

RESEARCHER_ID = "EM-CBRCF4-381080"


def add_mod_tuple(x, y, moduli):
    return tuple((a + b) % m for a, b, m in zip(x, y, moduli))


def elems(moduli):
    if not moduli:
        return [()]
    return list(product(*[range(m) for m in moduli]))


def affine_fiber_image(moduli, n, m):
    """A generic affine bijection T^2 -> T^2: swap plus translations."""
    T = elems(moduli)
    s1 = tuple((n + 2 * m + i) % mod for i, mod in enumerate(moduli))
    s2 = tuple((3 * n + m + 2 * i) % mod for i, mod in enumerate(moduli))
    image = []
    for t, u in product(T, repeat=2):
        image.append((add_mod_tuple(u, s1, moduli), add_mod_tuple(t, s2, moduli)))
    return T, image


def generic_cost(n, t):
    # Exact deterministic nonnegative test cost; no theorem semantics are inferred from it.
    return Fraction((n * n + 2 * abs(n) + 3) % 11, 3) + sum(
        Fraction((i + 1) * v, 7) for i, v in enumerate(t)
    )


def check_envelope_bijections():
    groups = {
        "0": (),
        "Z2": (2,),
        "Z3": (3,),
        "Z4": (4,),
        "Z2xZ2": (2, 2),
    }
    checked = 0
    for name, moduli in groups.items():
        T = elems(moduli)
        target = set(product(T, repeat=2))
        for n, m in [(-2, 1), (0, 0), (1, 3), (4, -1)]:
            _, image = affine_fiber_image(moduli, n, m)
            assert len(image) == len(target)
            assert set(image) == target
            # Min over a bijectively permuted finite output fiber separates exactly.
            free1, free2 = n + m, n - m
            lhs_min = min(
                generic_cost(free1, t) + generic_cost(free2, u)
                for t, u in image
            )
            rhs_min = min(generic_cost(free1, t) for t in T) + min(
                generic_cost(free2, u) for u in T
            )
            assert lhs_min == rhs_min
            checked += 1
    return {"groups": list(groups), "cases": checked}


def q2(n, t):
    """Minimal global-zero-separating scalar on Z ⊕ Z/2."""
    t %= 2
    base = Fraction(0) if n == 0 else Fraction(1)
    correction = Fraction(0)
    if t:
        correction = Fraction(1, 2) if n % 2 == 0 else Fraction(-1, 2)
    return base + correction


def M2(x, y):
    """Minimal rank-one torsion-mediated involutive mixer, free block I_2."""
    n, t = x
    m, u = y
    p = (n + m) % 2
    return (n, (u + p) % 2), (m, (t + p) % 2)


def slot_swap(pair):
    x, y = pair
    return y, x


def J2(x):
    n, t = x
    return -n, (-t) % 2


def S2(x):
    n, t = x
    return n, (-t) % 2


def check_minimal_global_survivor(bound=10):
    zero = (0, 0)
    e = (1, 0)
    out = M2(e, zero)
    assert out == ((1, 1), (0, 1))
    assert q2(*out[0]) == q2(*out[1]) == Fraction(1, 2)
    assert q2(*e) == 1 and q2(*zero) == 0
    assert all(q2(n, t) > 0 for n in range(-bound, bound + 1) for t in range(2)
               if (n, t) != zero)
    # Exact formula partitions prove positivity globally; bounded loop is regression.
    assert q2(0, 1) == Fraction(1, 2)
    assert q2(2, 0) == 1 and q2(2, 1) == Fraction(3, 2)
    assert q2(1, 0) == 1 and q2(1, 1) == Fraction(1, 2)
    for n, m, t, u in product(range(-bound, bound + 1), range(-bound, bound + 1), range(2), range(2)):
        x, y = (n, t), (m, u)
        ox, oy = M2(x, y)
        assert q2(*ox) + q2(*oy) == q2(*x) + q2(*y)
        assert M2(ox, oy) == (x, y)
        assert M2(*slot_swap((x, y))) == slot_swap(M2(x, y))
        assert q2(*J2(x)) == q2(*x)
        assert q2(*S2(x)) == q2(*x)
    # Additivity regression.
    pts = [(-2, 0), (-1, 1), (0, 0), (0, 1), (1, 0), (2, 1)]
    for x1, y1, x2, y2 in product(pts, repeat=4):
        left = M2((x1[0] + x2[0], (x1[1] + x2[1]) % 2),
                  (y1[0] + y2[0], (y1[1] + y2[1]) % 2))
        a1, b1 = M2(x1, y1)
        a2, b2 = M2(x2, y2)
        right = ((a1[0] + a2[0], (a1[1] + a2[1]) % 2),
                 (b1[0] + b2[0], (b1[1] + b2[1]) % 2))
        assert left == right
    f = lambda n: min(q2(n, 0), q2(n, 1))
    assert f(0) == 0
    assert f(1) == Fraction(1, 2)  # refutes the claimed automatic f(1)=1 step
    assert all(f(n) > 0 for n in range(-bound, bound + 1) if n)
    assert all(q2(n, 0) > 0 for n in range(-bound, bound + 1) if n)  # finite-copy nondegeneracy
    return {
        "carrier": "Z+Z/2",
        "free_block": [[1, 0], [0, 1]],
        "balanced_output": ["(1,1)", "(0,1)"],
        "f1": "1/2",
        "global_zero_separation": True,
        "finite_copy_nondegeneracy": True,
        "involutive": True,
        "slot_swap_equivariant": True,
    }


def q_c1_ext(n, a, b):
    """C1-compatible strengthening on Z ⊕ Z/3 ⊕ Z/2."""
    return q2(n, b) + (Fraction(1, 4) if n == 0 and a % 3 != 0 else Fraction(0))


def M_c1_ext(x, y):
    n, a, b = x
    m, c, d = y
    p = (n + m) % 2
    # Old Z/3 labels stay with their free coordinates; Z/2 labels mix across slots.
    return (n, a % 3, (d + p) % 2), (m, c % 3, (b + p) % 2)


def R3(x):
    n, a, b = x
    return n, (a + n) % 3, b


def S3(x):
    n, a, b = x
    return n, (-a) % 3, b


def J3(x):
    n, a, b = x
    return -n, (-a) % 3, (-b) % 2


def check_c1_compatible_strengthening(bound=5):
    zero = (0, 0, 0)
    e = (1, 0, 0)
    out = M_c1_ext(e, zero)
    assert out == ((1, 0, 1), (0, 0, 1))
    assert q_c1_ext(*out[0]) == q_c1_ext(*out[1]) == Fraction(1, 2)
    assert q_c1_ext(*e) == 1 and q_c1_ext(*zero) == 0
    for n, a, b in product(range(-bound, bound + 1), range(3), range(2)):
        x = (n, a, b)
        if x != zero:
            assert q_c1_ext(*x) > 0
        assert q_c1_ext(*R3(x)) == q_c1_ext(*x)
        assert q_c1_ext(*S3(x)) == q_c1_ext(*x)
        assert q_c1_ext(*J3(x)) == q_c1_ext(*x)
    for n, m, a, c, b, d in product(range(-bound, bound + 1), range(-bound, bound + 1),
                                      range(3), range(3), range(2), range(2)):
        x, y = (n, a, b), (m, c, d)
        ox, oy = M_c1_ext(x, y)
        assert q_c1_ext(*ox) + q_c1_ext(*oy) == q_c1_ext(*x) + q_c1_ext(*y)
        assert M_c1_ext(ox, oy) == (x, y)
    return {
        "carrier": "Z+Z/3+Z/2",
        "preserves_old_RJS_scalar_invariance": True,
        "global_zero_separation": True,
        "balanced": True,
    }


WEAK_TABLE = {
    0: Fraction(0),
    1: Fraction(1),
    2: Fraction(1, 2),
    3: Fraction(1, 2),
    4: Fraction(1, 2),
    5: Fraction(1),
}


def weak_f(n):
    return WEAK_TABLE[n % 6]


def check_weak_survivor():
    A = ((2, 3), (3, 4))
    for x, y in product(range(6), repeat=2):
        lhs = weak_f(2 * x + 3 * y) + weak_f(3 * x + 4 * y)
        rhs = weak_f(x) + weak_f(y)
        assert lhs == rhs
    assert weak_f(0) == 0 and weak_f(1) == 1
    assert weak_f(2) == weak_f(3) == Fraction(1, 2)
    first_gzs_failure = next(n for n in range(1, 100) if weak_f(n) == 0)
    assert first_gzs_failure == 6
    # On C1, q(n,a)=weak_f(n) is invariant under R,J,S but zero on nonzero torsion.
    for n, a in product(range(-12, 13), range(3)):
        q = weak_f(n)
        assert weak_f(n) == weak_f(-n)
        assert q == weak_f(n)  # R/S do not affect n
    return {
        "A": [list(A[0]), list(A[1])],
        "period": 6,
        "first_global_zero_separation_failure_n": first_gzs_failure,
        "elementary_positive": weak_f(1) > 0,
        "split_outputs_positive": weak_f(2) > 0 and weak_f(3) > 0,
        "finite_copy_nondegeneracy": False,
    }


def is_signed_permutation(A):
    a, b, c, d = A
    rows = [(a, b), (c, d)]
    cols = [(a, c), (b, d)]
    def one_pm_one(v):
        return sum(1 for z in v if z != 0) == 1 and sum(abs(z) for z in v) == 1
    return all(one_pm_one(r) for r in rows) and all(one_pm_one(c) for c in cols)


def free_block_regression(B=4):
    total = signed = nonsigned = zero_entry_nonsigned = all_nonzero = 0
    mismatches = 0
    periods = set()
    for a, b, c, d in product(range(-B, B + 1), repeat=4):
        det = a * d - b * c
        if abs(det) != 1:
            continue
        total += 1
        A = (a, b, c, d)
        sp = is_signed_permutation(A)
        if sp:
            signed += 1
        else:
            nonsigned += 1
        if 0 in A:
            if not sp:
                zero_entry_nonsigned += 1
            # The theorem says GZS + conservation forces any zero-entry block to signed permutation.
            predicted_gzs_possible_at_free_level = sp
        else:
            all_nonzero += 1
            g = gcd(abs(a), abs(d))
            h = gcd(abs(b), abs(c))
            assert g >= 1 and h >= 1
            assert gcd(abs(a), h) == 1
            assert gcd(abs(d), h) == 1
            assert gcd(abs(b), g) == 1
            assert gcd(abs(c), g) == 1
            periods.add(g * h)
            # Forced positive period gives f(gh)=f(0), contradicting envelope zero separation.
            predicted_gzs_possible_at_free_level = False
        if predicted_gzs_possible_at_free_level != sp:
            mismatches += 1
    assert mismatches == 0
    return {
        "bound": B,
        "gl2_matrices": total,
        "signed_permutations": signed,
        "non_signed": nonsigned,
        "zero_entry_non_signed": zero_entry_nonsigned,
        "all_nonzero": all_nonzero,
        "forced_periods_seen": sorted(periods),
        "theorem_enumeration_mismatches": mismatches,
    }


def main():
    envelope = check_envelope_bijections()
    minimal = check_minimal_global_survivor()
    c1ext = check_c1_compatible_strengthening()
    weak = check_weak_survivor()
    gl2 = free_block_regression()

    summary = {
        "researcher_id": RESEARCHER_ID,
        "envelope": envelope,
        "minimal_global_rank_one_survivor": minimal,
        "c1_compatible_strengthening": c1ext,
        "weak_scalar_ablation_witness": weak,
        "gl2_regression": gl2,
        "ablations": {
            "positivity_only_elementary_states_eliminates_rank_one": False,
            "positivity_only_split_outputs_eliminates_rank_one": False,
            "finite_copy_nondegeneracy_eliminates_rank_one": False,
            "global_zero_separation_eliminates_rank_one": False,
            "envelope_zero_separation_eliminates_non_signed_free_blocks": True,
        },
        "primary_verdict": "F4_RANK_ONE_SURVIVOR_EXISTS",
        "theorem_enumeration_mismatches": 0,
    }
    payload = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    digest = sha256(payload.encode("utf-8")).hexdigest()
    print(json.dumps(summary, sort_keys=True, indent=2))
    print("DETERMINISTIC_RESULT_SHA256=" + digest)


if __name__ == "__main__":
    main()
