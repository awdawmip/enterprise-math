#!/usr/bin/env python3
"""Two-moment signed condensation, from the existing coarse source certificate.

The packet delta_x-alpha delta_L-beta delta_R has the positive, compactly
supported Green image G_[L,R](.,x).  Sign cancellation is done before each
eliminated coefficient is positive-parted.  No road is recomputed.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'rh_joint_certificate'))
from certify_joint_energy import (  # noqa: E402
    SCALE, ZERO, A, B, interval_from_record, record, isum, positive, add, sub,
    scale, square, sqrt_interval, energy, green_apply, intersects,
)

OUT = Path(__file__).resolve().parent
INPUT = ROOT / 'rh_joint_certificate/joint_energy_certificate.json'


def packets_by_halving(nodes, charges):
    current = list(nodes)
    mass = {x: m for x, m in zip(nodes, charges)}
    levels = []
    while len(current) > 2:
        retained = current[::2]
        if retained[-1] != current[-1]:
            retained.append(current[-1])
        keep = set(retained)
        packets = []
        for k in range(1, len(current)-1):
            x = current[k]
            if x in keep:
                continue
            L, R = current[k-1], current[k+1]
            t = mass[x]
            packets.append((L, x, R, t))
            mass[L] = add(mass[L], scale(t, F(R-x, R-L)))
            mass[R] = add(mass[R], scale(t, F(x-L, R-L)))
            del mass[x]
        levels.append(packets)
        current = retained
    return levels, [(x, mass[x]) for x in current]


def packet_values(packet, positive_only=False):
    L, x, R, t = packet
    if positive_only:
        t = positive(t)
    if t == ZERO:
        return
    for n in range(L+1, R):
        numerator = (n-L)*(R-x) if n <= x else (x-L)*(R-n)
        yield n, scale(t, F(numerator, R-L))


def negative_first(nodes, charges):
    """Repeated certified negative-node deletion; final nonnegative part is safe.

    Selection is an illustrative, deterministic algorithm, not an optimum claim.
    The inputs have no numerically ambiguous signs on this finite certificate.
    """
    current = list(nodes)
    mass = {x: m for x, m in zip(nodes, charges)}
    deleted = []
    while True:
        selected = next((k for k in range(1, len(current)-1)
                         if mass[current[k]][1] <= 0), None)
        if selected is None:
            break
        k = selected
        L, x, R = current[k-1:k+2]
        t = mass[x]
        deleted.append((L, x, R, t))
        mass[L] = add(mass[L], scale(t, F(R-x, R-L)))
        mass[R] = add(mass[R], scale(t, F(x-L, R-L)))
        del mass[x]
        current.pop(k)
    rhs = [ZERO]*(B+1)
    for x in current[1:-1]:
        rhs[x] = positive(mass[x])
    return green_apply(rhs, A, B), deleted, [(x, mass[x]) for x in current]


def records(packets):
    return [{'L': L, 'x': x, 'R': R, 'signed_elimination_charge': record(t)}
            for L, x, R, t in packets]


def main():
    start = time.perf_counter()
    source = json.loads(INPUT.read_text())
    outputs = []
    for partition in source['partitions']:
        part = {'beta': partition['beta'], 'block_count': partition['block_count']}
        for road in ('q', 'Q'):
            item = partition[road]
            nodes = item['nodes']
            charges = [ZERO]+[interval_from_record(r) for r in item['signed_coarse_charges']]+[ZERO]
            ends = [interval_from_record(r) for r in (item['node_values'][0], item['node_values'][-1])]
            affine = [ZERO]*(B+1)
            for n in range(A, B+1):
                affine[n] = add(scale(ends[0], F(B-n,B-A)), scale(ends[1], F(n-A,B-A)))
            rhs, prhs = [ZERO]*(B+1), [ZERO]*(B+1)
            for x, m in zip(nodes, charges):
                rhs[x], prhs[x] = m, positive(m)
            signed, coarse_positive = green_apply(rhs,A,B), green_apply(prhs,A,B)
            levels, end_charges = packets_by_halving(nodes, charges)
            unsigned_levels, _ = packets_by_halving(nodes, [positive(m) for m in charges])
            U, reconstructed, unsigned_reconstructed = ([ZERO]*(B+1) for _ in range(3))
            level_records = []
            for level, packets in enumerate(levels):
                v = [ZERO]*(B+1)
                for packet in packets:
                    for n, value in packet_values(packet):
                        reconstructed[n] = add(reconstructed[n], value)
                    for n, value in packet_values(packet, True):
                        v[n] = add(v[n], value)
                        U[n] = add(U[n], value)
                for packet in unsigned_levels[level]:
                    for n, value in packet_values(packet):
                        unsigned_reconstructed[n] = add(unsigned_reconstructed[n], value)
                level_records.append({'level': level+1, 'packets': records(packets),
                    'packet_count': len(packets),
                    'certified_nonpositive_count': sum(t[1] <= 0 for _,_,_,t in packets),
                    'certified_positive_count': sum(t[0] > 0 for _,_,_,t in packets),
                    'positive_level_energy': record(energy(v,A+1,B-1)),
                    'support_interior_disjoint': True})
            assert all(intersects(reconstructed[n],signed[n]) for n in range(A+1,B))
            assert all(intersects(unsigned_reconstructed[n],coarse_positive[n]) for n in range(A+1,B))
            assert all(signed[n][0] <= U[n][1] for n in range(A+1,B))
            assert all(U[n][0] <= coarse_positive[n][1] for n in range(A+1,B))
            # The interval-compatibility checks supplement the exact algebraic
            # domination theorem. They do not independently prove it by separation.
            local_root = sqrt_interval(interval_from_record(item['local_positive_energy_interior']))
            end_root = sqrt_interval(interval_from_record(item['endpoint_positive_energy_interior']))
            combined = [add(U[n], affine[n]) for n in range(B+1)]
            combined_energy = energy(combined,A+1,B-1,'positive')
            budget = add(sqrt_interval(combined_energy),local_root)
            level_triangle = isum(sqrt_interval(interval_from_record(l['positive_level_energy']))
                                  for l in level_records)
            full_level_budget = add(add(end_root,level_triangle),local_root)
            upper_hull, deleted, retained = negative_first(nodes,charges)
            hull_plus_end = [add(upper_hull[n],affine[n]) for n in range(B+1)]
            hull_energy = energy(hull_plus_end,A+1,B-1,'positive')
            hull_budget = add(sqrt_interval(hull_energy),local_root)
            part[road] = {
                'multiscale_positive_envelope_energy': record(energy(U,A+1,B-1)),
                'true_endpoint_plus_multiscale_envelope_positive_energy': record(combined_energy),
                'squared_multiscale_budget_with_actual_local': record(square(budget)),
                'sum_level_norms': record(level_triangle),
                'squared_level_triangle_budget_with_actual_local': record(square(full_level_budget)),
                'levels': level_records,
                'final_boundary_charges_zero_Green_image': [{'x':x,'charge':record(m)} for x,m in end_charges],
                'negative_first': {
                    'deleted_nonpositive_packets': records(deleted),
                    'retained_nodes': [{'x':x,'charge':record(m)} for x,m in retained],
                    'endpoint_plus_envelope_positive_energy': record(hull_energy),
                    'squared_budget_with_actual_local': record(square(hull_budget))},
                'old_positive_budget_squared': item['squared_endpoint_plus_positive_charges_plus_local_norm_budget'],
                'old_signed_interpolation_budget_squared': item['squared_signed_plus_local_norm_budget'],
                'checks': {'complete_signed_reconstruction_enclosures_intersect': True,
                           'complete_positive_reconstruction_enclosures_intersect': True,
                           'domination_proof': 'algebraic theorem; interval compatibility checked'}}
            print(json.dumps({'beta': partition['beta'], 'road':road,
                'multiscale_squared_budget': part[road]['squared_multiscale_budget_with_actual_local']['upper'],
                'negative_first_squared_budget': part[road]['negative_first']['squared_budget_with_actual_local']['upper'],
                'seconds': round(time.perf_counter()-start,2)}),flush=True)
        outputs.append(part)
    result = {'status':'CERTIFIED_FINITE_SIGNED_MULTISCALE_UPPER_BOUNDS',
        'scope':'same complete road; deterministic source condensation; no asymptotic arithmetic condition proved',
        'window':{'A':A,'B':B,'theta':'1/2'},
        'arithmetic':'outward integer intervals with denominator 10**60',
        'input':{'path':str(INPUT.relative_to(ROOT)),'sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest()},
        'partitions':outputs,
        'cost':{'seconds':time.perf_counter()-start,'road_recomputations':0,
                'packet_count_per_hierarchy':'one per original internal coarse node',
                'packet_value_work':'O((B-A) log J); level supports disjoint'}}
    (OUT/'multiscale_elimination_certificate.json').write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n')


if __name__=='__main__':
    main()
