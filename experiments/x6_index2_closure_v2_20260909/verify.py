#!/usr/bin/env python3
"""Exact finite certificate for the X6 index-2 closure continuation.

Run from an EM checkout: python experiments/x6_index2_closure_v2_20260909/verify.py
No floating-point acceptance tests. The infinite bound is proved in the note;
its finite regressions here do not substitute for that proof. Reuses the existing
finite_symmetry module unchanged, rather than introducing a new symmetry tool.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import sys
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, gcd, isqrt, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math import finite_symmetry as fs

D = 6
PAIRS = tuple(combinations(range(D), 2))
I = tuple(tuple(int(i == j) for j in range(D)) for i in range(D))


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def span(rows):
    ans = {0}
    for row in rows:
        ans |= {x ^ row for x in tuple(ans)}
    return frozenset(ans)


def bitdot(a: int, b: int) -> int:
    return (a & b).bit_count() % 2


def matchings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for b in xs[1:]:
        rest = tuple(x for x in xs if x not in (a, b))
        for tail in matchings(rest):
            yield ((a, b),) + tail


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(D))
                       for j in range(D)) for i in range(D))


def tr(a):
    return sum(a[i][i] for i in range(D))


def gram(a):
    return mm(tuple(zip(*a)), a)


def delta(a):
    g = gram(a)
    return D * tr(mm(g, g)) - tr(g) ** 2


def mul_scalar(k, a=I):
    return tuple(tuple(k * x for x in row) for row in a)


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(r, s)) for r, s in zip(a, b))


def h(pair):
    a = [list(row) for row in I]
    i, j = pair
    a[i][i], a[i][j], a[j][i], a[j][j] = 1, 1, 1, -1
    return tuple(map(tuple, a))


def gauss_binom(n, k, p):
    ans = Fraction(1)
    for j in range(1, k + 1):
        ans *= Fraction(p ** (n - k + j) - 1, p ** j - 1)
    require(ans.denominator == 1, "Gaussian binomial was nonintegral")
    return ans.numerator


def valuations(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def sum_two_squares(q):
    return any(isqrt(q-a*a)**2 == q-a*a for a in range(isqrt(q)+1))


def first_isotropic_power(n):
    answer = 1
    for p, e in valuations(n).items():
        modulus = 6 if p % 4 == 3 else 3
        answer = lcm(answer, modulus // gcd(modulus, e))
    return answer


def run():
    source = Path(inspect.getfile(fs)).read_bytes()
    source_blob = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
    require(source_blob == "ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2", "frozen symmetry source changed")
    ms = tuple(matchings(tuple(range(D))))
    require(len(ms) == 15, "matching census")
    codes = {span((1 << i) | (1 << j) for i, j in m): m for m in ms}
    planes = {span(rows) for rows in combinations(range(1, 64), 3) if len(span(rows)) == 8}
    self_dual = {w for w in planes if all(bitdot(x, y) == 0 for x in w for y in w)}
    require(len(planes) == 1395 and self_dual == set(codes), "binary subspace classification")

    # Independent complete norm-2 frame check: every vector has two +/-1 entries.
    # Quotient only by vector sign and frame order for this stated observer.
    lines = []
    for i, j in PAIRS:
        for sign in (-1, 1):
            v = [0] * D
            v[i], v[j] = 1, sign
            lines.append(tuple(v))
    def dot(v, w):
        return sum(x * y for x, y in zip(v, w))
    frames = []
    def visit(chosen, candidates):
        if len(chosen) == D:
            frames.append(chosen)
            return
        if len(chosen) + len(candidates) < D:
            return
        for pos, k in enumerate(candidates):
            visit(chosen + (k,), tuple(j for j in candidates[pos + 1:]
                                      if dot(lines[k], lines[j]) == 0))
    visit((), tuple(range(len(lines))))
    require(len(frames) == 15, "complete orthogonal frame census")

    # Each chain has W1 < W2 < W3, with dimensions 1,2,3 in the dual parity space.
    branch_rows = []
    flag_total = 0
    for mask in range(1, 64):
        endpoints = [w for w in codes if mask in w]
        nflags = 0
        for w in endpoints:
            middle = {span((mask, b)) for b in w if b not in (0, mask)}
            require(len(middle) == 3, "F2^3 flag multiplicity")
            nflags += len(middle)
        branch_rows.append((mask.bit_count(), len(endpoints), nflags))
        flag_total += nflags
    require(flag_total == 315, "full flag census")
    by_weight = []
    expected = {1:(6,0,0),2:(15,3,9),3:(20,0,0),4:(15,3,9),5:(6,0,0),6:(1,15,45)}
    for weight in range(1, 7):
        rows = [r for r in branch_rows if r[0] == weight]
        counts = {(r[1], r[2]) for r in rows}
        require(len(counts) == 1, "orbit counts not constant")
        e, f = next(iter(counts))
        require((len(rows),e,f) == expected[weight], "unexpected branch row")
        by_weight.append(dict(weight=weight, branches=len(rows), endpoints_per_branch=e, flags_per_branch=f))

    # Existing T7 implementation performs the symmetry audit unchanged.
    perms = tuple(permutations(range(D)))
    def act_mask(p, a):
        return sum(1 << p[i] for i in range(D) if a & (1 << i))
    mask_actions = {p: {a: act_mask(p, a) for a in range(1,64)} for p in perms}
    orbits = fs.orbit_partition(tuple(range(1,64)), mask_actions)
    require(sorted(map(len, orbits)) == [1,6,6,15,15,20], "T7 orbit audit")
    fixed = fs.global_fixed_points(tuple(range(1,64)), mask_actions)
    require(fixed == frozenset({63}), "T7 fixed parity branch")
    match_actions = {p: {m: tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in m)) for m in ms} for p in perms}
    require(fs.canonical_choice_obstruction(ms, match_actions), "T7 matching-choice obstruction")
    require(len(fs.stabilizer(ms, match_actions, ms[0])) == 48, "matching stabilizer")

    # All 15^3 words in the explicitly declared pair-H packet, not all lattice chains.
    hs = {pair:h(pair) for pair in PAIRS}
    require(all(delta(a) == 8 for a in hs.values()), "one-step minimal defect")
    good = []
    for word in product(PAIRS, repeat=3):
        a = mm(hs[word[2]], mm(hs[word[1]], hs[word[0]]))
        closed = gram(a) == mul_scalar(2)
        disjoint = len(set(sum((tuple(pair) for pair in word), ()))) == 6
        require(closed == disjoint, "pair-word iff matching failed")
        if closed:
            good.append(word)
    require(len(good) == 90, "pair-word closure census")
    require(delta(mm(h((0,1)), mm(h((0,1)),h((0,1))))) == 392, "same-defect counterexample")

    future = mm(h((4,5)), h((2,3)))
    observer_outputs = [delta(mm(future,h(pair))) for pair in ((0,1),(2,3))]
    require(observer_outputs == [0,56], "fixed-future scalar-defect witness")

    # The general multiplier classification is sourced from Conway-Rains-Sloane.
    # Check its repetition-index corollary against direct sum-of-two-square tests.
    for n in range(1, 513):
        vp = valuations(n)
        admissible = []
        for r in range(1, 7):
            if all((r*e) % 3 == 0 for e in vp.values()):
                q = 1
                for p,e in vp.items():
                    q *= p ** (r*e//3)
                if sum_two_squares(q):
                    admissible.append(r)
        require(admissible and min(admissible) == first_isotropic_power(n), "first isotropic power")

    # Exact finite regressions for the proved arbitrary-block infinite law.
    a = I
    checked = 0
    for block in range(60):
        for pair in ms[block % len(ms)]:
            a = mm(h(pair), a)
            checked += 1
            t, s = divmod(checked, 3)
            g = gram(a)
            alpha = 2 ** t
            if s == 0:
                require(g == mul_scalar(alpha), "macro closure regression")
            else:
                zero = mm(sub(g,mul_scalar(alpha)),sub(g,mul_scalar(2*alpha)))
                require(zero == mul_scalar(0) and tr(g) == (6+2*s)*alpha, "prefix spectrum regression")
                require(delta(a) == 8 * alpha**2, "prefix defect regression")
    # Canonical representatives only for the declared one-block residue observer.
    for m,w in codes.items():
        pairs = w
        digits = [sum(bit << pairs[j][0] for j, bit in enumerate(bits)) for bits in product((0,1), repeat=3)]
        checks = [(1<<i)|(1<<j) for i,j in pairs]
        residues = {tuple(bitdot(d,c) for c in checks) for d in digits}
        require(len(residues) == 8, "radix transversal is not bijective")

    return {
        "schema":"EM_X6_INDEX2_CLOSURE_CERTIFICATE_V2",
        "status":"PASS_EXACT_FINITE_CHECKS_NOT_INDEPENDENT_REVIEW",
        "source_snapshot":"cf224163a9fe5ea4f3ac6d8dd5e13f1b771daf44",
        "research_activity_id":"RA-X6COUNT-3B06CF3EC023",
        "report_path":"research_notes/x6_index2_complete_closure_and_bounded_doubling_20260909.md",
        "reuse":{"resolution":"REUSE_EXECUTED", "method":"T7_FINITE_SYMMETRY_EQUIVARIANCE", "path":"src/enterprise_math/finite_symmetry.py", "git_blob_sha1":source_blob},
        "binary_dimension3_subspaces":len(planes),
        "binary_self_dual_subspaces":len(self_dual),
        "unoriented_unordered_norm2_frames":len(frames),
        "ordered_signed_norm2_frames":len(frames)*factorial(6)*2**6,
        "isotropic_endpoint_lattices":len(ms),
        "all_index8_sublattices":gauss_binom(8,3,2),
        "by_first_branch_weight":by_weight,
        "all_three_step_index2_chains":63**3,
        "closing_chains":flag_total,
        "closing_chain_fraction":str(Fraction(flag_total,63**3)),
        "uniform_endpoint_closing_fraction":str(Fraction(len(ms),gauss_binom(8,3,2))),
        "pair_packet_words_checked":15**3,
        "pair_packet_closing_words":len(good),
        "pair_packet_closing_fraction":str(Fraction(len(good),15**3)),
        "unique_S6_fixed_index2_mask":63,
        "S6_fixed_matching_count":0,
        "matching_stabilizer_order":48,
        "repeated_same_pair_three_step_delta":392,
        "fixed_future_scalar_defect_witness":{"current_defects":[8,8], "same_future_outputs":observer_outputs},
        "first_isotropic_power_values":{str(n):first_isotropic_power(n) for n in (1,2,3,4,5,6,8,9,27,64)},
        "first_isotropic_power_integers_checked":512,
        "general_multiplier_classification":"Conway-Rains-Sloane, Theorem 2: q is a sum of two integer squares",
        "bounded_doubling_prefixes_checked":checked,
        "max_exact_macro_scale_squared_checked":2**60,
        "infinite_claim_evidence":"proof in report; finite prefixes are regressions only"
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
