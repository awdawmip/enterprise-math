#!/usr/bin/env python3
"""Exact finite checks of the all-integer dyadic-length spectral gap.

The general theorem is proved by the companion parity induction.  This file
checks the complete rational quadratic-form identities and a few new weighted
source/mesh compositions.  It imports no old certificate and queries no road.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json


def powers(h):
    result, d = [], 1
    while d < h:
        result.append(d)
        d *= 2
    return result


def laplacian(h, lengths):
    matrix = [[F(0) for _ in range(h)] for _ in range(h)]
    for d in lengths:
        for i in range(h-d):
            j = i+d
            matrix[i][i] += 1
            matrix[j][j] += 1
            matrix[i][j] -= 1
            matrix[j][i] -= 1
    return matrix


def residual(h):
    matrix = laplacian(h, powers(h))
    for i in range(h):
        for j in range(h):
            matrix[i][j] -= 2*(F(i == j)-F(1, h))
    return matrix


def matrix_checks():
    sizes = (1, 2, 3, 4, 5, 7, 8, 9, 15, 16, 17,
             31, 32, 33, 63, 64, 65, 127, 128, 129)
    matrices = {h: residual(h) for h in sizes}
    rows, entries = [], 0
    for h in sizes:
        a, b = (h+1)//2, h//2
        lhs = matrices[h]
        if h == 1:
            assert lhs == [[F(0)]]
            rows.append({'h': 1, 'lengths': [], 'zero_base_case': True})
            entries += 1
            continue
        contrast = [F(1, a) if i % 2 == 0 else -F(1, b) for i in range(h)]
        assert sum(contrast) == 0
        prefixes, running = [], F(0)
        for c in contrast[:-1]:
            running += c
            prefixes.append(running)
        q = sum((s*s for s in prefixes), F(0))
        k = F(2*a*b, h)
        expected_q = F(1, b) if a == b else F(h, 3*a*b)
        assert q == expected_q and k*q <= 1
        slack = 1/q-k
        assert slack == (F(0) if a == b else F(a*b, h))
        rhs = laplacian(h, (1,))
        even, odd = list(range(0, h, 2)), list(range(1, h, 2))
        for indices, shorter in ((even, a), (odd, b)):
            for i, ii in enumerate(indices):
                for j, jj in enumerate(indices):
                    rhs[ii][jj] += matrices[shorter][i][j]
        for i in range(h):
            for j in range(h):
                rhs[i][j] -= k*contrast[i]*contrast[j]
                assert lhs[i][j] == rhs[i][j]
                entries += 1
        # The covariance proof is independent of the chosen test vector.
        # This exact identity also checks the telescoping orientation directly.
        z = [F((i*i+3*i+1) % 11-5, i+1) for i in range(h)]
        delta = sum((c*v for c, v in zip(contrast, z)), F(0))
        differences = [z[i]-z[i+1] for i in range(h-1)]
        assert delta == sum((s*d for s, d in zip(prefixes, differences)), F(0))
        bridge = sum((d*d for d in differences), F(0))-k*delta*delta
        sos = sum(((prefixes[i]*differences[j]-prefixes[j]*differences[i])**2
                   for i in range(h-1) for j in range(i+1, h-1)), F(0))/q
        sos += slack*delta*delta
        assert bridge == sos >= 0
        rows.append({'h': h, 'lengths': powers(h), 'even_size': a, 'odd_size': b,
                     'prefix_square_sum': str(q), 'between_mean_coefficient': str(k),
                     'extra_square_coefficient': str(slack),
                     'complete_quadratic_matrix_identity': True,
                     'exact_square_sum_identity': True})
    return {'sizes': list(sizes), 'complete_matrix_identities': len(sizes),
            'matrix_entries_checked': entries, 'rows': rows,
            'uniform_sharpness': {'h': 2, 'vector': ['1', '-1'],
                                   'variance': '2', 'dyadic_edge_energy': '4'}}


def green(L, R, x, n):
    return F((min(x, n)-L)*(R-max(x, n)), R-L)


def variance(v):
    mean = sum(v, F(0))/len(v)
    return sum(((z-mean)**2 for z in v), F(0))


def interpolate(nodes, values, n):
    if n == nodes[-1]:
        return values[-1]
    for j, (a, b) in enumerate(zip(nodes, nodes[1:])):
        if a <= n < b:
            return F(b-n, b-a)*values[j]+F(n-a, b-a)*values[j+1]
    raise AssertionError(n)


def local_source_check(L, R, source, nodes):
    h = R-L
    A, B = [F(0)], [F(0)]
    for n in range(L+1, R):
        A.append(A[-1]+source[n])
        B.append(B[-1]+source[n]/n)
    intervals = {d: sum(((A[i+d]-A[i])**2 for i in range(h-d)), F(0))
                 for d in powers(h)}
    sparse_sum = sum(intervals.values(), F(0))
    va, vb = variance(A), variance(B)
    assert va <= sparse_sum/2
    assert vb <= F(R, L*L*(L+1))*va
    values = [sum((green(L, R, x, n)*source[n]/n for n in range(L+1, R)), F(0))
              for x in nodes]
    df = sum(((v-u)**2/F(b-a)
              for a, b, u, v in zip(nodes, nodes[1:], values, values[1:])), F(0))
    energy = sum((max(interpolate(nodes, values, n), F(0))**2/F(n*n)
                  for n in range(L, R+1)), F(0))
    c_geometry = F(h*h, 8*L*L)
    coefficient = c_geometry*F(R, 2*L*L*(L+1))
    upper = coefficient*sparse_sum
    assert df <= vb
    assert energy <= c_geometry*df <= c_geometry*vb <= upper
    return {'L': L, 'R': R, 'nodes': list(nodes), 'lengths': powers(h),
            'positive_square_energy': str(energy), 'sparse_interval_square_sum': str(sparse_sum),
            'geometry_constant_used': str(c_geometry), 'transfer_coefficient': str(coefficient),
            'sparse_transfer_upper': str(upper)}, intervals


def source_checks():
    rows = []
    for h in (2, 3, 5, 6, 9, 17, 33):
        L, R = 2*h+1, 3*h+1
        sources = {
            'positive': {n: F(1) for n in range(L+1, R)},
            'signed_blocks': {n: F(1 if n-L <= h//2 else -1) for n in range(L+1, R)},
            'signed_rational': {n: F((n*n+3*n) % 11-5, 7) for n in range(L+1, R)}}
        meshes = {tuple(sorted({L, L+1, L+h//3, R-1, R})),
                  (L, L+h//2, R)}
        for name, source in sources.items():
            for nodes in sorted(meshes):
                row, _ = local_source_check(L, R, source, nodes)
                row['source_pattern'] = name
                rows.append(row)
    # Two new nonuniform coarse partitions distinguish power-of-two and odd H.
    X, Y = 37, 74
    source = {n: F(n % 5-1, 3) for n in range(X+1, Y)}
    global_prefix = [F(0)]
    for n in range(X+1, Y):
        global_prefix.append(global_prefix[-1]+source[n])
    multi = []
    for cuts in ((37, 42, 51, 58, 74), (37, 42, 51, 57, 74)):
        H = max(b-a for a, b in zip(cuts, cuts[1:]))
        global_intervals = {d: sum(((global_prefix[i+d]-global_prefix[i])**2
                                    for i in range(Y-X-d)), F(0))
                            for d in powers(H)}
        local_sums = {d: F(0) for d in powers(H)}
        total_energy = F(0)
        for L, R in zip(cuts, cuts[1:]):
            nodes = tuple(sorted({L, L+1, (L+R)//2, R}))
            row, intervals = local_source_check(L, R, source, nodes)
            total_energy += F(row['positive_square_energy'])
            for d, value in intervals.items():
                local_sums[d] += value
        assert all(local_sums[d] <= global_intervals[d] for d in powers(H))
        upper = F(H*H, 8*X**4)*sum(global_intervals.values(), F(0))
        K = max(value/F(X*d) for d, value in global_intervals.items())
        selberg_upper = K*F(H*H*sum(powers(H)), 8*X**3)
        assert total_energy <= upper <= selberg_upper <= K*F(H**3, 4*X**3)
        multi.append({'coarse_nodes': list(cuts), 'max_length': H, 'shared_lengths': powers(H),
                      'actual_positive_square_energy': str(total_energy),
                      'sparse_global_upper': str(upper), 'finite_K': str(K),
                      'sparse_K_upper': str(selberg_upper),
                      'center_coverage_verified': True})
    return {'local_source_mesh_cases': len(rows), 'local_cases': rows,
            'nonuniform_multi_cell_cases': multi}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('sparse_length_results.json'))
    args = parser.parse_args()
    matrices = matrix_checks()
    sources = source_checks()
    result = {'schema': 'EM_ALL_INTEGER_DYADIC_LENGTH_GAP_V1', 'status': 'PASS',
              'author': 'EM-DIRECT-E7559A / TASK_RESEARCH',
              'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
              'status_scope': 'Author exact finite checks; the unbounded theorem is proved by parity induction. No independent Review or formal Result.',
              'arithmetic': 'Python Fraction only; no floating eigenvalue decisions.',
              'old_certificate_reruns': 0, 'road_queries': 0, 'prime_sieves': 0,
              'matrix_checks': matrices, 'weighted_source_checks': sources}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS',
                      'complete_matrix_identities': matrices['complete_matrix_identities'],
                      'matrix_entries_checked': matrices['matrix_entries_checked'],
                      'local_source_mesh_cases': sources['local_source_mesh_cases'],
                      'multi_cell_cases': len(sources['nonuniform_multi_cell_cases']),
                      'old_certificate_reruns': 0}, ensure_ascii=False))


if __name__ == '__main__':
    main()
