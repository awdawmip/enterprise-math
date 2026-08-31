#!/usr/bin/env python3
"""R025 exact multi-layer collapse dynamics laboratory.

All theorem-critical arithmetic uses Python integers and fractions.Fraction.
Floating point is used only for optional display/regression summaries.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import log
import argparse
import csv
import json
import time
from typing import Iterable, Sequence

POLICIES = (
    "ALWAYS_DOWN", "ALWAYS_UP", "NEAREST", "FARTHEST",
    "PRNG_50_50", "STOCHASTIC_UNBIASED",
    "ALTERNATING_DOWN_FIRST", "ALTERNATING_UP_FIRST",
)


def floor_root(n: int, p: int) -> int:
    if n < 0:
        raise ValueError("natural-state engine requires n >= 0")
    if p < 1:
        raise ValueError("p must be >= 1")
    if n < 2 or p == 1:
        return n
    # Binary search with a safe bit-length upper bound.
    hi = 1 << ((n.bit_length() + p - 1) // p)
    lo = hi >> 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        q = mid ** p
        if q <= n:
            lo = mid
        else:
            hi = mid
    if hi ** p <= n:
        return hi
    return lo


def bracket(n: int, p: int) -> tuple[int, int, int, int, int, int, bool]:
    k = floor_root(n, p)
    L = k ** p
    exact = (L == n)
    U = n if exact else (k + 1) ** p
    G = U - L
    d = n - L
    u = U - n
    return k, L, U, G, d, u, exact


def ceil_root(n: int, p: int) -> int:
    k = floor_root(n, p)
    return k if k ** p == n else k + 1


def counter_digest(seed: int, trajectory_id: str, layer: int, attempt: int, block: int) -> bytes:
    payload = f"R025|{seed}|{trajectory_id}|{layer}|{attempt}|{block}".encode("utf-8")
    return sha256(payload).digest()


def counter_bit(seed: int, trajectory_id: str, layer: int) -> int:
    return counter_digest(seed, trajectory_id, layer, 0, 0)[0] & 1


def exact_uniform_below(modulus: int, seed: int, trajectory_id: str, layer: int) -> tuple[int, int, int]:
    """Deterministic counter-based rejection sampler, exact modulo a hash-bit idealization.

    Returns (sample, rejection_count, bits_per_attempt). No modulo bias is introduced.
    This is an empirical pseudorandom implementation; theorem claims use ideal probabilities.
    """
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    blocks = max(1, (modulus.bit_length() + 255) // 256)
    B = 1 << (256 * blocks)
    limit = B - (B % modulus)
    attempt = 0
    while True:
        raw = b"".join(counter_digest(seed, trajectory_id, layer, attempt, b) for b in range(blocks))
        z = int.from_bytes(raw, "big")
        if z < limit:
            return z % modulus, attempt, 256 * blocks
        attempt += 1


def choose_endpoint(n: int, p: int, policy: str, *, layer: int = 0,
                    seed: int = 0, trajectory_id: str = "0",
                    alpha: Fraction | None = None) -> tuple[int, str, int, int]:
    k, L, U, G, d, u, exact = bracket(n, p)
    if exact:
        return n, "EXACT", 0, 0
    if policy == "ALWAYS_DOWN":
        return L, "L", 0, 0
    if policy == "ALWAYS_UP":
        return U, "U", 0, 0
    if policy == "NEAREST":
        return (L, "L", 0, 0) if d <= u else (U, "U", 0, 0)
    if policy == "FARTHEST":
        return (U, "U", 0, 0) if d <= u else (L, "L", 0, 0)
    if policy == "PRNG_50_50":
        bit = counter_bit(seed, trajectory_id, layer)
        return (U, "U", 0, 1) if bit else (L, "L", 0, 1)
    if policy == "STOCHASTIC_UNBIASED":
        z, rejects, bits = exact_uniform_below(G, seed, trajectory_id, layer)
        # P(U)=d/G; exactly d residues select U.
        return (U, "U", rejects, bits) if z < d else (L, "L", rejects, bits)
    if policy == "ALTERNATING_DOWN_FIRST":
        return choose_endpoint(n, p, "ALWAYS_DOWN" if layer % 2 == 0 else "ALWAYS_UP",
                               layer=layer, seed=seed, trajectory_id=trajectory_id)
    if policy == "ALTERNATING_UP_FIRST":
        return choose_endpoint(n, p, "ALWAYS_UP" if layer % 2 == 0 else "ALWAYS_DOWN",
                               layer=layer, seed=seed, trajectory_id=trajectory_id)
    if policy == "PHASE_THRESHOLD":
        if alpha is None or alpha < 0 or alpha > 1:
            raise ValueError("PHASE_THRESHOLD requires alpha in [0,1]")
        # Frozen rule: phi < alpha -> L, else U. Equality goes U.
        return (L, "L", 0, 0) if Fraction(d, G) < alpha else (U, "U", 0, 0)
    raise ValueError(f"unknown policy {policy}")


def apply_operation(state: int, M: int, operation_id: str) -> int:
    if operation_id == "IDENTITY":
        return state
    if operation_id == "PHYSICAL_ADD_1":
        return state + M
    if operation_id == "INTEGER_SCALE_2":
        return 2 * state
    raise ValueError(f"unknown operation {operation_id}")


@dataclass(frozen=True)
class LayerRow:
    trajectory_id: str
    initial_value_num: int
    initial_value_den: int
    initial_precision: int
    layer: int
    precision_M: int
    refinement_ratio_r: int
    exponent_p: int
    operation_id: str
    policy_id: str
    seed: int
    pre_operation_state: int
    pre_collapse_state: int
    root_index_k: int
    lower_L: int
    upper_U: int
    gap_G: int
    lower_offset_d: int
    upper_offset_u: int
    phase_num: int
    phase_den: int
    selected_endpoint: str
    post_collapse_state: int
    signed_coordinate_error: int
    absolute_coordinate_error: int
    signed_physical_error_num: int
    signed_physical_error_den: int
    exact_power_before_collapse: bool
    branch_count_before: int
    branch_count_after: int
    recoalescence_count: int
    state_bit_length: int
    rng_rejections: int = 0
    rng_bits_per_attempt: int = 0


@dataclass(frozen=True)
class TrajectorySummary:
    trajectory_id: str
    policy_id: str
    final_value_num: int
    final_value_den: int
    total_signed_drift_num: int
    total_signed_drift_den: int
    cumulative_abs_displacement_num: int
    cumulative_abs_displacement_den: int
    max_excursion_num: int
    max_excursion_den: int
    ambiguous_layer_count: int
    exact_hit_count: int
    terminal_state_count: int
    max_state_bit_length: int


def run_trajectory(n0: int, p_schedule: Sequence[int], r_schedule: Sequence[int], policy: str,
                   *, M0: int = 1, seed: int = 0, trajectory_id: str = "0",
                   alpha: Fraction | None = None, operation_id: str = "IDENTITY") -> tuple[list[LayerRow], TrajectorySummary]:
    depth = len(p_schedule)
    if depth == 0:
        raise ValueError("depth must be positive")
    if len(r_schedule) != max(0, depth - 1):
        raise ValueError("r_schedule must have depth-1 entries")
    if M0 <= 0 or n0 < 0:
        raise ValueError
    s = n0
    M = M0
    initial = Fraction(n0, M0)
    rows: list[LayerRow] = []
    total_drift = Fraction(0, 1)
    total_abs = Fraction(0, 1)
    max_excursion = Fraction(0, 1)
    ambiguous = exact_hits = 0
    max_bits = s.bit_length()
    final = initial
    for t, p in enumerate(p_schedule):
        r = r_schedule[t] if t < depth - 1 else 1
        a = apply_operation(s, M, operation_id)
        k, L, U, G, d, u, exact = bracket(a, p)
        if exact:
            phase = Fraction(0, 1)
            exact_hits += 1
        else:
            phase = Fraction(d, G)
            ambiguous += 1
        y, side, rejects, rng_bits = choose_endpoint(a, p, policy, layer=t, seed=seed,
                                                      trajectory_id=trajectory_id, alpha=alpha)
        cerr = y - a
        perr = Fraction(cerr, M)
        total_drift += perr
        total_abs += abs(perr)
        final = Fraction(y, M)
        max_excursion = max(max_excursion, abs(final - initial))
        max_bits = max(max_bits, a.bit_length(), y.bit_length())
        rows.append(LayerRow(
            trajectory_id=trajectory_id,
            initial_value_num=n0, initial_value_den=M0, initial_precision=M0,
            layer=t, precision_M=M, refinement_ratio_r=r, exponent_p=p,
            operation_id=operation_id, policy_id=(f"PHASE_THRESHOLD_{alpha.numerator}_{alpha.denominator}" if policy == "PHASE_THRESHOLD" else policy),
            seed=seed, pre_operation_state=s, pre_collapse_state=a,
            root_index_k=k, lower_L=L, upper_U=U, gap_G=G,
            lower_offset_d=d, upper_offset_u=u,
            phase_num=phase.numerator, phase_den=phase.denominator,
            selected_endpoint=side, post_collapse_state=y,
            signed_coordinate_error=cerr, absolute_coordinate_error=abs(cerr),
            signed_physical_error_num=perr.numerator, signed_physical_error_den=perr.denominator,
            exact_power_before_collapse=exact,
            branch_count_before=1, branch_count_after=1, recoalescence_count=0,
            state_bit_length=max(a.bit_length(), y.bit_length()),
            rng_rejections=rejects, rng_bits_per_attempt=rng_bits,
        ))
        if t < depth - 1:
            s = r * y
            M = r * M
    summary = TrajectorySummary(
        trajectory_id=trajectory_id, policy_id=rows[0].policy_id,
        final_value_num=final.numerator, final_value_den=final.denominator,
        total_signed_drift_num=total_drift.numerator, total_signed_drift_den=total_drift.denominator,
        cumulative_abs_displacement_num=total_abs.numerator, cumulative_abs_displacement_den=total_abs.denominator,
        max_excursion_num=max_excursion.numerator, max_excursion_den=max_excursion.denominator,
        ambiguous_layer_count=ambiguous, exact_hit_count=exact_hits,
        terminal_state_count=1, max_state_bit_length=max_bits,
    )
    return rows, summary


@dataclass(frozen=True)
class BRCLayer:
    layer: int
    precision_M: int
    refinement_ratio_r: int
    exponent_p: int
    support_before: tuple[int, ...]
    support_after: tuple[int, ...]
    raw_endpoint_count: int
    branch_creation_count: int
    duplicate_collision_count: int
    exact_parent_count: int
    ambiguous_parent_count: int
    support_width_coordinate: int
    support_width_physical_num: int
    support_width_physical_den: int


def run_all_endpoints(n0: int, p_schedule: Sequence[int], r_schedule: Sequence[int], *, M0: int = 1, operation_id: str = "IDENTITY") -> list[BRCLayer]:
    depth = len(p_schedule)
    if len(r_schedule) != max(0, depth - 1):
        raise ValueError
    support = {n0}
    M = M0
    out: list[BRCLayer] = []
    for t, p in enumerate(p_schedule):
        r = r_schedule[t] if t < depth - 1 else 1
        raw: list[int] = []
        exact_parents = ambiguous_parents = 0
        for n in sorted(support):
            astate = apply_operation(n, M, operation_id)
            _, L, U, _, _, _, exact = bracket(astate, p)
            if exact:
                raw.append(astate); exact_parents += 1
            else:
                raw.extend((L, U)); ambiguous_parents += 1
        after = set(raw)
        width = max(after) - min(after) if after else 0
        out.append(BRCLayer(
            layer=t, precision_M=M, refinement_ratio_r=r, exponent_p=p,
            support_before=tuple(sorted(support)), support_after=tuple(sorted(after)),
            raw_endpoint_count=len(raw),
            branch_creation_count=max(0, len(raw) - len(support)),
            duplicate_collision_count=len(raw) - len(after),
            exact_parent_count=exact_parents, ambiguous_parent_count=ambiguous_parents,
            support_width_coordinate=width,
            support_width_physical_num=Fraction(width, M).numerator,
            support_width_physical_den=Fraction(width, M).denominator,
        ))
        if t < depth - 1:
            support = {r * y for y in after}
            M *= r
        else:
            support = after
    return out


def geometric_endpoint_set(n: int, p: int) -> set[int]:
    _, L, U, _, _, _, exact = bracket(n, p)
    return {n} if exact else {L, U}


def apply_word(n0: int, word: Sequence[int], r_schedule: Sequence[int], policy: str, *, M0: int = 1,
               alpha: Fraction | None = None) -> Fraction:
    rows, summary = run_trajectory(n0, word, r_schedule, policy, M0=M0, alpha=alpha,
                                   trajectory_id=f"word-{n0}-{word}-{r_schedule}-{policy}")
    return Fraction(summary.final_value_num, summary.final_value_den)


def p_power_free_kernel(r: int, p: int) -> tuple[int, int]:
    """Unique r=a^p*d with d p-power-free; returns (a,d)."""
    x = r
    a = 1
    d = 1
    q = 2
    while q * q <= x:
        e = 0
        while x % q == 0:
            x //= q
            e += 1
        if e:
            a *= q ** (e // p)
            d *= q ** (e % p)
        q += 1
    if x > 1:
        d *= x
    assert a ** p * d == r
    return a, d

def frac_json(q: Fraction) -> dict[str, int]:
    return {"num": q.numerator, "den": q.denominator}


def minimal_counterexample_h4(max_p: int = 8, max_a: int = 8, max_n: int = 500):
    for p in range(2, max_p + 1):
        for a in range(2, max_a + 1):
            ap = a ** p
            for n in range(max_n + 1):
                for pol in ("ALWAYS_DOWN", "ALWAYS_UP", "NEAREST", "FARTHEST"):
                    left = choose_endpoint(ap * n, p, pol)[0]
                    right = ap * choose_endpoint(n, p, pol)[0]
                    if left != right:
                        return {"p": p, "a": a, "n": n, "policy": pol, "lhs": left, "rhs": right}
    return None


def minimal_counterexample_h6(max_p: int = 8, max_r: int = 200, max_k: int = 100):
    for p in range(2, max_p + 1):
        for r in range(2, max_r + 1):
            a, d = p_power_free_kernel(r, p)
            if a == 1:
                continue
            for k in range(1, max_k + 1):
                for pol in ("ALWAYS_DOWN", "ALWAYS_UP", "NEAREST", "FARTHEST"):
                    lhs = Fraction(choose_endpoint(r * (k ** p), p, pol)[0], r)
                    rhs = Fraction(choose_endpoint(d * (k ** p), p, pol)[0], d)
                    if lhs != rhs:
                        return {"p": p, "r": r, "a": a, "d": d, "k": k, "policy": pol,
                                "lhs": frac_json(lhs), "rhs": frac_json(rhs)}
    return None


def check_brc_interval_funnel(p: int, r: int, max_A: int = 80, max_B: int = 80) -> tuple[bool, dict | None]:
    if not (1 <= r < 2 ** p):
        raise ValueError("funnel claim only in r < 2^p regime")
    for A in range(max_A + 1):
        for B in range(A, max_B + 1):
            raw = set()
            for k in range(A, B + 1):
                n = r * (k ** p)
                lo = floor_root(n, p); hi = ceil_root(n, p)
                raw.add(lo); raw.add(hi)
            loA = floor_root(r * (A ** p), p)
            hiB = ceil_root(r * (B ** p), p)
            expected = set(range(loA, hiB + 1))
            if raw != expected:
                return False, {"p": p, "r": r, "A": A, "B": B,
                               "actual": sorted(raw), "expected": sorted(expected)}
    return True, None


def search_order_defects(max_n: int = 200, max_p: int = 8, max_r: int = 12):
    policies = ["ALWAYS_DOWN", "ALWAYS_UP", "NEAREST", "FARTHEST",
                "ALTERNATING_DOWN_FIRST", "ALTERNATING_UP_FIRST"]
    results = {}
    for pol in policies:
        witness = None
        for n in range(max_n + 1):
            if witness: break
            for r in range(1, max_r + 1):
                if witness: break
                for p in range(2, max_p + 1):
                    if witness: break
                    for q in range(p + 1, max_p + 1):
                        a = apply_word(n, (p, q), (r,), pol)
                        b = apply_word(n, (q, p), (r,), pol)
                        if a != b:
                            witness = {"n": n, "r": r, "p": p, "q": q,
                                       "pq": frac_json(a), "qp": frac_json(b),
                                       "defect": frac_json(a - b),
                                       "comparable": (q % p == 0 or p % q == 0)}
                            break
        results[pol] = witness
    return results


def exhaustive_reference(max_n=500, p_values=range(2,7), r_values=range(1,13), depth=8):
    """Attack exact candidate laws over the full frozen small box without storing every row."""
    t0 = time.perf_counter()
    counts = {
        "trajectory_prefixes_checked": 0,
        "layer_transitions_checked": 0,
        "h1_violations": 0, "h2_violations": 0, "h3_violations": 0,
        "h5_violations": 0,
        "near_far_recoalescence_cases": 0,
        "max_brc_support": 0,
        "max_state_bit_length": 0,
    }
    first = {}
    thresholds = [Fraction(1,4), Fraction(1,2), Fraction(3,4)]
    for n0 in range(max_n + 1):
        for p in p_values:
            for r in r_values:
                ps = [p] * depth
                rs = [r] * (depth - 1)
                # Deterministic trajectories, including phase thresholds.
                det = {}
                for pol in ("ALWAYS_DOWN","ALWAYS_UP","NEAREST","FARTHEST",
                            "ALTERNATING_DOWN_FIRST","ALTERNATING_UP_FIRST"):
                    rows, _ = run_trajectory(n0, ps, rs, pol, trajectory_id=f"ref-{n0}-{p}-{r}-{pol}")
                    det[pol] = rows
                    counts["max_state_bit_length"] = max(counts["max_state_bit_length"], *(x.state_bit_length for x in rows))
                phase_rows = []
                for a in thresholds:
                    rows, _ = run_trajectory(n0, ps, rs, "PHASE_THRESHOLD", alpha=a,
                                             trajectory_id=f"ref-{n0}-{p}-{r}-T-{a}")
                    phase_rows.append((a, rows))
                brc = run_all_endpoints(n0, ps, rs)
                counts["max_brc_support"] = max(counts["max_brc_support"], *(len(x.support_after) for x in brc))
                near_prev = far_prev = None
                for t in range(depth):
                    counts["trajectory_prefixes_checked"] += 1
                    counts["layer_transitions_checked"] += 1
                    down = det["ALWAYS_DOWN"][t].post_collapse_state
                    up = det["ALWAYS_UP"][t].post_collapse_state
                    # H1: deterministic endpoint selectors and full BRC support stay in envelope.
                    vals = [det[p0][t].post_collapse_state for p0 in det]
                    vals += [rows[t].post_collapse_state for _, rows in phase_rows]
                    vals += list(brc[t].support_after)
                    if not all(down <= v <= up for v in vals):
                        counts["h1_violations"] += 1
                        first.setdefault("h1", {"n":n0,"p":p,"r":r,"layer":t,"down":down,"up":up,"vals":vals})
                    # H2 physical monotonicity, compare post-collapse physical values across layers.
                    if t > 0:
                        prevM = det["ALWAYS_DOWN"][t-1].precision_M
                        M = det["ALWAYS_DOWN"][t].precision_M
                        prevD = Fraction(det["ALWAYS_DOWN"][t-1].post_collapse_state, prevM)
                        curD = Fraction(down, M)
                        prevU = Fraction(det["ALWAYS_UP"][t-1].post_collapse_state, prevM)
                        curU = Fraction(up, M)
                        if curD > prevD or curU < prevU:
                            counts["h2_violations"] += 1
                            first.setdefault("h2", {"n":n0,"p":p,"r":r,"layer":t})
                    # H3 single-input complement checked on every near input and every far input separately.
                    for row in (det["NEAREST"][t], det["FARTHEST"][t]):
                        if not row.exact_power_before_collapse:
                            near = choose_endpoint(row.pre_collapse_state, p, "NEAREST")[0]
                            far = choose_endpoint(row.pre_collapse_state, p, "FARTHEST")[0]
                            _, L,U,G,_,_,_ = bracket(row.pre_collapse_state,p)
                            if abs(near-row.pre_collapse_state)+abs(far-row.pre_collapse_state) != G or near+far != L+U:
                                counts["h3_violations"] += 1
                                first.setdefault("h3", {"n":n0,"p":p,"r":r,"layer":t,"state":row.pre_collapse_state})
                    # Track later near/far recoalescence after an earlier divergence.
                    nv = det["NEAREST"][t].post_collapse_state
                    fv = det["FARTHEST"][t].post_collapse_state
                    if t > 0 and near_prev != far_prev and nv == fv:
                        counts["near_far_recoalescence_cases"] += 1
                        first.setdefault("near_far_recoalesce", {"n":n0,"p":p,"r":r,"layer":t,"state":nv})
                    near_prev, far_prev = nv, fv
                # H5 only applies when r is a perfect p-th power.
                ar = floor_root(r,p)
                if ar**p == r:
                    for pol in ("ALWAYS_DOWN","ALWAYS_UP","NEAREST","FARTHEST"):
                        rows = det[pol]
                        if any(not x.exact_power_before_collapse for x in rows[1:]):
                            counts["h5_violations"] += 1
                            first.setdefault("h5", {"n":n0,"p":p,"r":r,"policy":pol})
    counts["runtime_seconds"] = time.perf_counter() - t0
    return counts, first


def precision_scaling_table(xs=(Fraction(1,1), Fraction(3,2), Fraction(7,3)), p_values=range(2,17)):
    rows=[]
    for x in xs:
        b=x.denominator
        # Exact same physical target using M=b*10^j.
        Ms=[b*(10**j) for j in range(1,9)]
        for p in p_values:
            vals=[]
            for M in Ms:
                N=M*x
                assert N.denominator==1
                n=N.numerator
                k,L,U,G,d,u,exact=bracket(n,p)
                W=Fraction((k+1)**p-k**p, M)
                vals.append((M,k,W))
            # float slopes display-only.
            xx=[log(M) for M,_,_ in vals[-5:]]
            yy=[log(float(W)) for _,_,W in vals[-5:]]
            xm=sum(xx)/len(xx); ym=sum(yy)/len(yy)
            slope=sum((a-xm)*(b0-ym) for a,b0 in zip(xx,yy))/sum((a-xm)**2 for a in xx)
            rows.append({"x_num":x.numerator,"x_den":x.denominator,"p":p,
                         "slope_display":slope,"theory_slope":-1/p,
                         "M_first":vals[0][0],"M_last":vals[-1][0],
                         "W_first_num":vals[0][2].numerator,"W_first_den":vals[0][2].denominator,
                         "W_last_num":vals[-1][2].numerator,"W_last_den":vals[-1][2].denominator,
                         "k_last":vals[-1][1]})
    return rows


def exponent_phase_rows(n_values=(2,3,7,8,15,16,31,32,100,500,10_000), pmax=32):
    rows=[]
    for n in n_values:
        for p in range(2,pmax+1):
            k,L,U,G,d,u,exact=bracket(n,p)
            near=choose_endpoint(n,p,"NEAREST")[0]
            far=choose_endpoint(n,p,"FARTHEST")[0]
            rows.append({"n":n,"p":p,"k":k,"L":L,"U":U,"G":G,"d":d,"u":u,
                         "phase_num":0 if exact else Fraction(d,G).numerator,
                         "phase_den":1 if exact else Fraction(d,G).denominator,
                         "down_up_spread":U-L,
                         "nearest_abs_error":abs(near-n),"farthest_abs_error":abs(far-n),
                         "stochastic_variance_coord":d*u,
                         "exact":exact,
                         "k1_threshold_p": n.bit_length() if n>1 else None})
    return rows


def brc_phase_table(p_values=range(2,9), r_values=range(1,17), depth=12, n0_values=(2,3,10,50)):
    rows=[]
    for p in p_values:
        for r in r_values:
            max_card=0; total_collisions=0; total_raw=0
            final_cards=[]
            for n0 in n0_values:
                layers=run_all_endpoints(n0,[p]*depth,[r]*(depth-1))
                max_card=max(max_card,*(len(x.support_after) for x in layers))
                total_collisions+=sum(x.duplicate_collision_count for x in layers)
                total_raw+=sum(x.raw_endpoint_count for x in layers)
                final_cards.append(len(layers[-1].support_after))
            a=floor_root(r,p); aligned=(a**p==r)
            rows.append({"p":p,"r":r,"r_lt_2p":r<2**p,"aligned_p_power":aligned,
                         "max_live_support":max_card,"final_card_max":max(final_cards),
                         "final_card_min":min(final_cards),
                         "collision_ratio_num":total_collisions,
                         "collision_ratio_den":total_raw if total_raw else 1})
    return rows


def random_ensemble(n0:int,p_schedule:Sequence[int],r_schedule:Sequence[int],policy:str,seeds:Iterable[int]):
    finals=[]
    for seed in seeds:
        _,s=run_trajectory(n0,p_schedule,r_schedule,policy,seed=seed,trajectory_id=f"ens-{policy}-{n0}-{seed}")
        finals.append(Fraction(s.final_value_num,s.final_value_den))
    N=len(finals)
    mean=sum(finals,Fraction(0,1))/N
    var=sum(((x-mean)**2 for x in finals), Fraction(0,1))/N
    return {"N":N,"mean":frac_json(mean),"variance":frac_json(var),
            "min":frac_json(min(finals)),"max":frac_json(max(finals))}


def exact_probability_distribution(n0: int, p_schedule: Sequence[int], r_schedule: Sequence[int], law: str, *, M0: int = 1, operation_id: str = "IDENTITY") -> dict:
    """Exact ideal probability propagation for 50/50 or distance-weighted laws."""
    if law not in ("HALF", "UNBIASED"):
        raise ValueError("law must be HALF or UNBIASED")
    if len(r_schedule) != max(0, len(p_schedule)-1):
        raise ValueError
    dist = {n0: Fraction(1,1)}
    M = M0
    cumulative_expected_conditional_variance = Fraction(0,1)
    for t,p in enumerate(p_schedule):
        nxt: dict[int,Fraction] = {}
        for state, prob in dist.items():
            astate = apply_operation(state, M, operation_id)
            _,L,U,G,d,u,exact = bracket(astate,p)
            if exact:
                nxt[astate] = nxt.get(astate,Fraction(0,1)) + prob
            elif law == "HALF":
                nxt[L] = nxt.get(L,Fraction(0,1)) + prob*Fraction(1,2)
                nxt[U] = nxt.get(U,Fraction(0,1)) + prob*Fraction(1,2)
            else:
                nxt[L] = nxt.get(L,Fraction(0,1)) + prob*Fraction(u,G)
                nxt[U] = nxt.get(U,Fraction(0,1)) + prob*Fraction(d,G)
                cumulative_expected_conditional_variance += prob*Fraction(d*u, M*M)
        if t < len(p_schedule)-1:
            r = r_schedule[t]
            dist = {r*y: pr for y,pr in nxt.items()}
            M *= r
        else:
            dist = nxt
    vals=[(Fraction(state,M),prob) for state,prob in dist.items()]
    mean=sum((x*prob for x,prob in vals),Fraction(0,1))
    var=sum((((x-mean)**2)*prob for x,prob in vals),Fraction(0,1))
    return {
        "distribution": {str(k): [v.numerator,v.denominator] for k,v in sorted(dist.items())},
        "precision_M": M,
        "mean": frac_json(mean),
        "variance": frac_json(var),
        "expected_conditional_variance_sum": frac_json(cumulative_expected_conditional_variance),
        "support_cardinality": len(dist),
    }


def operation_robustness_probe(max_n: int = 100, p_values=range(2,7), r_values=range(1,7), depth: int = 6):
    result = {}
    for op in ("PHYSICAL_ADD_1", "INTEGER_SCALE_2"):
        h1_bad = None
        h2_bad = None
        h5_bad = None
        for n0 in range(max_n+1):
            if h1_bad and h2_bad and h5_bad:
                break
            for p in p_values:
                if h1_bad and h2_bad and h5_bad:
                    break
                for r in r_values:
                    ps=[p]*depth; rs=[r]*(depth-1)
                    det={}
                    for pol in ("ALWAYS_DOWN","ALWAYS_UP","NEAREST","FARTHEST"):
                        det[pol]=run_trajectory(n0,ps,rs,pol,trajectory_id=f"op-{op}-{n0}-{p}-{r}-{pol}",operation_id=op)[0]
                    for t in range(depth):
                        D=det["ALWAYS_DOWN"][t].post_collapse_state; U=det["ALWAYS_UP"][t].post_collapse_state
                        if h1_bad is None:
                            vals=[det[pol][t].post_collapse_state for pol in det]
                            if not all(D<=v<=U for v in vals):
                                h1_bad={"n":n0,"p":p,"r":r,"layer":t,"operation":op,"values":vals,"down":D,"up":U}
                        if h2_bad is None and t>0:
                            pm=det["ALWAYS_DOWN"][t-1].precision_M; cm=det["ALWAYS_DOWN"][t].precision_M
                            prev=Fraction(det["ALWAYS_DOWN"][t-1].post_collapse_state,pm); cur=Fraction(D,cm)
                            if cur>prev:
                                h2_bad={"n":n0,"p":p,"r":r,"layer":t,"operation":op,"prev":frac_json(prev),"cur":frac_json(cur)}
                    ar=floor_root(r,p)
                    if h5_bad is None and ar**p==r:
                        for pol in ("ALWAYS_DOWN","ALWAYS_UP","NEAREST","FARTHEST"):
                            if any(not x.exact_power_before_collapse for x in det[pol][1:]):
                                h5_bad={"n":n0,"p":p,"r":r,"operation":op,"policy":pol}
                                break
        result[op]={"h1_counterexample":h1_bad,"h2_counterexample":h2_bad,"h5_counterexample":h5_bad}
    return result


def write_csv(path:str, rows:list[dict]):
    if not rows: return
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out-dir",default="data/r025")
    ap.add_argument("--reference",action="store_true")
    args=ap.parse_args()
    import os
    os.makedirs(args.out_dir,exist_ok=True)
    summary={}
    if args.reference:
        counts,first=exhaustive_reference()
        summary["exhaustive_reference"]={"counts":counts,"first_witnesses":first}
    summary["minimal_counterexample_h4"]=minimal_counterexample_h4()
    summary["minimal_counterexample_h6"]=minimal_counterexample_h6()
    summary["order_defects"]=search_order_defects()
    # Exhaustively attack exact BRC interval funnel in a broad root-index box.
    funnel={}
    for p in range(2,9):
        bad=None
        checked=0
        for r in range(1,min(32,2**p)):
            ok,w=check_brc_interval_funnel(p,r,40,40)
            checked+=1
            if not ok:
                bad=w; break
        funnel[str(p)]={"checked_r":checked,"counterexample":bad}
    summary["brc_interval_funnel_attack"]=funnel
    # Random ensemble comparisons.
    random_cmp=[]
    for n0,p,r,depth in [(3,2,2,12),(10,3,2,12),(50,5,3,12),(500,8,5,12)]:
        ps=[p]*depth; rs=[r]*(depth-1)
        random_cmp.append({"n0":n0,"p":p,"r":r,"depth":depth,
                           "prng_50_50":random_ensemble(n0,ps,rs,"PRNG_50_50",range(512)),
                           "stochastic_unbiased":random_ensemble(n0,ps,rs,"STOCHASTIC_UNBIASED",range(512))})
    summary["random_ensembles"]=random_cmp
    with open(f"{args.out_dir}/R025_MACHINE_SUMMARY.json","w",encoding="utf-8") as f:
        json.dump(summary,f,indent=2,ensure_ascii=False)
    write_csv(f"{args.out_dir}/R025_PRECISION_SCALING.csv",precision_scaling_table())
    write_csv(f"{args.out_dir}/R025_EXPONENT_PHASE.csv",exponent_phase_rows())
    write_csv(f"{args.out_dir}/R025_BRC_PHASE.csv",brc_phase_table())

if __name__ == "__main__":
    main()
