#!/usr/bin/env python3
"""Certified finite signed-transport budgets from the existing coarse certificate.

No road is recomputed.  Input charge intervals have denominator 10**60.
Transport amounts are exact nonnegative integer multiples of 10**-60 and
never exceed certified positive mass or certified negative capacity.
All reported energies and norm budgets use outward integer arithmetic.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'rh_joint_certificate'))
from certify_joint_energy import (  # noqa: E402
    SCALE, DIGITS, ZERO, A, B, interval_from_record, record, isum,
    positive, neg, add, sub, scale, square, sqrt_interval, ceildiv,
    energy, green_apply,
)

OUT = Path(__file__).resolve().parent
INPUT = ROOT / 'rh_joint_certificate/joint_energy_certificate.json'


def make_plan(nodes, charges, mode):
    """Feasible partial transport; ordering is only a candidate selection rule."""
    pos = {i: max(m[0], 0) for i, m in enumerate(charges) if m[0] > 0}
    negs = {i: max(-m[1], 0) for i, m in enumerate(charges) if m[1] < 0}
    pairs = [(abs(nodes[i] - nodes[j]), i, j) for i in pos for j in negs]
    if mode == 'nearest':
        pairs.sort()
    elif mode == 'left_to_right':
        pairs.sort(key=lambda p: (nodes[p[1]], nodes[p[2]]))
    elif mode == 'right_to_left':
        pairs.sort(key=lambda p: (-nodes[p[1]], -nodes[p[2]]))
    else:
        raise ValueError(mode)
    plan = []
    for _, i, j in pairs:
        t = min(pos[i], negs[j])
        if t:
            plan.append((i, j, t))
            pos[i] -= t
            negs[j] -= t
    return plan


def green_line(x, n):
    """Integer coefficients (a,b) for (B-A)G(n,x)=a*n+b."""
    return (B-x, -A*(B-x)) if n <= x else (-(x-A), B*(x-A))


def add_segment(events_a, events_b, lo, hi, a, b, amount):
    if lo > hi or not amount:
        return
    events_a[lo] += a * amount
    events_b[lo] += b * amount
    events_a[hi+1] -= a * amount
    events_b[hi+1] -= b * amount


def add_green(events_a, events_b, x, amount):
    a, b = green_line(x, x)
    add_segment(events_a, events_b, A+1, x, a, b, amount)
    a, b = green_line(x, x+1)
    add_segment(events_a, events_b, x+1, B-1, a, b, amount)


def add_positive_difference(events_a, events_b, x, y, amount):
    """Exact integer-lattice positive part of one Green difference."""
    cuts = sorted({A, x, y, B-1})
    previous = A
    for end in cuts[1:]:
        lo, hi = previous+1, end
        previous = end
        if lo > hi:
            continue
        ax, bx = green_line(x, lo)
        ay, by = green_line(y, lo)
        a, b = ax-ay, bx-by
        if a > 0:
            lo = max(lo, (-b)//a + 1)
        elif a < 0:
            hi = min(hi, (b-1)//(-a))
        elif b <= 0:
            continue
        add_segment(events_a, events_b, lo, hi, a, b, amount)


def envelope(nodes, charges, plan):
    outgoing, incoming = [0]*len(nodes), [0]*len(nodes)
    for i, j, t in plan:
        assert t >= 0
        outgoing[i] += t
        incoming[j] += t
    for i, m in enumerate(charges):
        assert outgoing[i] <= max(m[0], 0)
        assert incoming[i] <= max(-m[1], 0)
    ea_lo, eb_lo, ea_hi, eb_hi = ([0]*(B+1) for _ in range(4))
    remaining = []
    for i, (x, m) in enumerate(zip(nodes, charges)):
        p = positive(m)
        r = p[0]-outgoing[i], p[1]-outgoing[i]
        remaining.append(r)
        assert r[0] >= 0
        add_green(ea_lo, eb_lo, x, r[0])
        add_green(ea_hi, eb_hi, x, r[1])
    for i, j, t in plan:
        add_positive_difference(ea_lo, eb_lo, nodes[i], nodes[j], t)
        add_positive_difference(ea_hi, eb_hi, nodes[i], nodes[j], t)
    answer = [ZERO]*(B+1)
    al = bl = ah = bh = 0
    for n in range(A+1, B):
        al += ea_lo[n]
        bl += eb_lo[n]
        ah += ea_hi[n]
        bh += eb_hi[n]
        vl, vh = al*n+bl, ah*n+bh
        assert 0 <= vl <= vh
        answer[n] = vl//(B-A), ceildiv(vh, B-A)
    return answer, remaining


def dyadic_prefix_diagnostics(nodes, charges):
    """Complete signed coarse populations, no sampling or removal of negatives."""
    result = []
    X = A
    while X < B:
        ids = [i for i, x in enumerate(nodes) if X <= x < min(2*X, B)]
        if not ids:
            X *= 2
            continue
        Fk = ZERO
        l1 = l2 = ZERO
        records = []
        for k, i in enumerate(ids):
            Fk = add(Fk, charges[i])
            if k+1 < len(ids):
                gap = nodes[ids[k+1]]-nodes[i]
                absF = (0 if Fk[0] <= 0 <= Fk[1] else min(abs(Fk[0]), abs(Fk[1])),
                        max(abs(Fk[0]), abs(Fk[1])))
                l1 = add(l1, scale(absF, gap))
                l2 = add(l2, scale(square(Fk), gap))
            records.append({'node': nodes[i], 'prefix': record(Fk)})
        width = nodes[ids[-1]]-nodes[ids[0]]
        # K_y <= sqrt(2)*sqrt(y), ||G_x-G_y|| <= sqrt(2)*|x-y|/sqrt(X).
        sqrt2 = sqrt_interval(scale((SCALE, SCALE), 2))
        sqrty = sqrt_interval((nodes[ids[-1]]*SCALE, nodes[ids[-1]]*SCALE))
        invsqrtX = sqrt_interval(scale((SCALE, SCALE), F(1, X)))
        from certify_joint_energy import mul
        bound = mul(sqrt2, add(mul(positive(Fk), sqrty), mul(l1, invsqrtX)))
        result.append({'X': X, 'first': nodes[ids[0]], 'last': nodes[ids[-1]],
                       'count': len(ids), 'total_mass': record(Fk),
                       'prefix_L1_with_gap': record(l1),
                       'prefix_L2_squared_with_gap': record(l2),
                       'M_positive_times_sqrt_X': record(mul(positive(Fk), sqrt_interval((X*SCALE,X*SCALE)))),
                       'prefix_Abel_root_bound_theta_half': record(bound),
                       'prefixes': records})
        X *= 2
    return result


def main():
    start = time.perf_counter()
    source = json.loads(INPUT.read_text())
    results = []
    for partition in source['partitions']:
        entry = {'beta': partition['beta'], 'block_count': partition['block_count']}
        for road in ('q', 'Q'):
            item = partition[road]
            nodes = item['nodes'][1:-1]
            charges = [interval_from_record(r) for r in item['signed_coarse_charges']]
            values = [interval_from_record(r) for r in item['node_values']]
            affine = [ZERO]*(B+1)
            for n in range(A, B+1):
                affine[n] = add(scale(values[0], F(B-n, B-A)),
                                scale(values[-1], F(n-A, B-A)))
            rhs = [ZERO]*(B+1)
            prhs = [ZERO]*(B+1)
            for x, m in zip(nodes, charges):
                rhs[x], prhs[x] = m, positive(m)
            signed = green_apply(rhs, A, B)
            unsigned = green_apply(prhs, A, B)
            local_root = sqrt_interval(interval_from_record(item['local_positive_energy_interior']))
            candidates = []
            for mode in ('nearest', 'left_to_right', 'right_to_left'):
                plan = make_plan(nodes, charges, mode)
                V, remaining = envelope(nodes, charges, plan)
                # Strict interval check of the pointwise domination, allowing the
                # vanishingly small overlap arising from shared input intervals.
                assert all(signed[n][0] <= V[n][1] for n in range(A+1, B))
                assert all(V[n][0] <= unsigned[n][1] for n in range(A+1, B))
                combined = [ZERO]*(B+1)
                for n in range(A+1, B):
                    combined[n] = add(affine[n], V[n])
                Venergy = energy(V, A+1, B-1)
                combined_energy = energy(combined, A+1, B-1, 'positive')
                budget = add(sqrt_interval(combined_energy), local_root)
                candidates.append({'method': mode, 'pair_count': len(plan),
                    'matched_mass': record((sum(t for _,_,t in plan),)*2),
                    'unmatched_positive_mass': record(isum(remaining)),
                    'total_transport_distance_mass': record((sum(t*abs(nodes[i]-nodes[j]) for i,j,t in plan),)*2),
                    'envelope_energy': record(Venergy),
                    'endpoint_plus_envelope_positive_energy': record(combined_energy),
                    'root_budget_with_actual_local': record(budget),
                    'squared_budget_with_actual_local': record(square(budget)),
                    'transport_plan': [{'positive_node': nodes[i], 'negative_node': nodes[j],
                                        'amount_integer_over_10_pow_60': str(t)} for i,j,t in plan]})
            best = min(candidates, key=lambda c: int(c['squared_budget_with_actual_local']['integer_bounds'][1]))
            diagnostics = dyadic_prefix_diagnostics(nodes, charges)
            abel = isum(interval_from_record(d['prefix_Abel_root_bound_theta_half']) for d in diagnostics)
            entry[road] = {'old_positive_coarse_energy': item['green_of_positive_charges_energy_interior'],
                           'old_positive_budget_squared': item['squared_endpoint_plus_positive_charges_plus_local_norm_budget'],
                           'old_signed_interpolation_budget_squared': item['squared_signed_plus_local_norm_budget'],
                           'candidates': candidates, 'selected_method': best['method'],
                           'selected_budget_squared': best['squared_budget_with_actual_local'],
                           'dyadic_prefix_diagnostics': diagnostics,
                           'sum_dyadic_Abel_root_bounds': record(abel)}
            print(json.dumps({'beta': partition['beta'], 'road': road,
                              'selected': best['method'],
                              'budget_squared': best['squared_budget_with_actual_local']['upper'],
                              'seconds': round(time.perf_counter()-start, 2)}), flush=True)
        results.append(entry)
    answer = {'status': 'CERTIFIED_FINITE_SIGNED_TRANSPORT_UPPER_BOUNDS',
        'scope': 'Same complete rational-node road and Q=q+P_256; no independent-road or asymptotic claim.',
        'window': {'A': A, 'B': B, 'theta': '1/2', 'endpoints': 'actual, separately retained'},
        'arithmetic': {'method': 'outward integer intervals', 'scale': str(SCALE),
                       'transport_amounts': 'exact, feasible on every enclosed source'},
        'input': {'path': str(INPUT.relative_to(ROOT)), 'sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest()},
        'partitions': results,
        'cost': {'seconds': time.perf_counter()-start,
                 'road_recomputations': 0,
                 'envelope_algorithm': 'piecewise affine event sweep, O(N+J+number_of_pairs) arithmetic after plan selection'}}
    (OUT/'signed_transport_certificate.json').write_text(json.dumps(answer, ensure_ascii=False, separators=(',',':'))+'\n')


if __name__ == '__main__':
    main()
