#!/usr/bin/env python3
"""Author checks for complete bounded integer sources and invisible anchor gaps.

Only Python stdlib; exact fractions and 80-place outward integer intervals.
The previous package is read only, and its main programs are never executed.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='round8 riemann_directed_dyadic_integer_return package')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('bounded_source_anchors_certificate.json'))
    args = parser.parse_args()
    helper_path = args.previous / 'arithmetic_rigidity/certify_first_cell_and_repair.py'
    constants_path = args.previous / 'return_energy/log_energy_constants_certificate.json'
    spec = importlib.util.spec_from_file_location('r8_interval_arithmetic', helper_path)
    module = importlib.util.module_from_spec(spec)
    old_bytecode_flag = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = old_bytecode_flag
    S = module.S
    rat, add, sub = module.rat, module.add, module.sub
    mul, scale, div = module.mul, module.scale, module.div
    ceildiv, record = module.ceildiv, module.record
    old_constants = json.loads(constants_path.read_text())['constants']

    def saved(name):
        x = old_constants[name]
        assert x['denominator_power_of_10'] == 80
        return tuple(map(int, x['integer_bounds']))

    def square(x):
        assert x[0] >= 0
        return x[0]*x[0]//S, ceildiv(x[1]*x[1], S)

    def divide_by_int(x, n):
        assert n > 0
        return x[0]//n, ceildiv(x[1], n)

    def power(x, k):
        out = rat(1)
        for _ in range(k):
            out = mul(out, x)
        return out

    a = F(1, 8)
    gamma = add(saved('C_star'), saved('log_4pi'), rat(-2))
    log2, pi = saved('log_2'), saved('pi')
    log3 = module.log(rat(3))  # The sole new logarithm series.
    C = scale(sub(add(rat(1), gamma), log2), 2)
    D20 = sub(sub(scale(log3, 6), scale(log2, 4)), add(rat(2), scale(gamma, 2)))
    D2 = add(D20, rat(F(1, 32)))
    assert C[0] > 0
    assert D20[0] > rat(F(1, 2))[1]
    assert D2[0] > rat(F(2, 3))[1]
    assert D2[1] < rat(F(3, 4))[0]
    I = sub(rat(F(2329, 35)), scale(log2, 96))
    J = sub(rat(F(25, 3)), scale(log2, 12))
    assert I[0] > 0 and J[0] > 0
    slope = scale(I, a*a)
    intercept = scale(mul(C, J), 2*a)

    def dyadic_bump(n):
        if n < 2:
            return F(0)
        X = 1 << (n.bit_length()-1)
        j = n-X
        return F(j*j*(X-j)*(X-j), 8*X**3)

    source_nodes = set(range(3, 16385))
    extra_seams = []
    for k in range(2, 21):
        for n in (2**k-1, 2**k, 2**k+1):
            extra_seams.append(n)
            source_nodes.add(n)
    source_min = None
    source_max = None
    for n in sorted(source_nodes):
        delta = n*(dyadic_bump(n+1)-2*dyadic_bump(n)+dyadic_bump(n-1))
        lo, hi = 1+delta, F(n*n, n*n-1)+delta
        assert lo >= F(3, 4) and hi <= F(27, 16)
        if source_min is None or lo < source_min[1]:
            source_min = (n, lo)
        if source_max is None or hi > source_max[1]:
            source_max = (n, hi)

    C2 = square(C)
    energy_rows = []
    energy_nodes = 0
    for k in range(1, 17):
        X = 2**k
        energy = baseline = residual = rat(0)
        for j in range(X+1):
            n = X+j
            bump = F(j*j*(X-j)*(X-j), 8*X**3)
            q = add(C, rat(bump))
            energy = add(energy, divide_by_int(square(q), n*n))
            baseline = add(baseline, divide_by_int(C2, n*n))
            residual = add(residual, rat(bump*bump/(n*n)))
        center = add(scale(slope, X), intercept, scale(C2, F(1, 2*X)))
        radius = add(rat(F(131, 1536*X)*a*a),
                     scale(C, F(35, 48*X*X)*a),
                     scale(C2, F(5, 8*X*X)),
                     scale(C2, F(1, 2*X**3)))
        discrepancy = sub(energy, center)
        assert max(abs(discrepancy[0]), abs(discrepancy[1])) <= radius[0]
        assert energy[0] > baseline[1]
        energy_nodes += X+1
        energy_rows.append({
            'X': X, 'closed_integer_nodes': X+1,
            'full_positive_energy': record(energy),
            'energy_over_X': record(divide_by_int(energy, X)),
            'true_endpoint_secant_energy': record(baseline),
            'positive_residual_square': record(residual),
            'explicit_asymptotic_center': record(center),
            'explicit_remainder_radius': record(radius),
            'energy_minus_center': record(discrepancy)})

    # Exact degree-eight integer-sum identity, including h=1.
    identity_summands = 0
    for h in range(1, 513):
        numerator = sum(j**4*(h-j)**4 for j in range(1, h))
        lhs = F(numerator, h**8)
        rhs = F(h, 630)+F(20*h*h-21, 630*h**7)
        assert lhs == rhs
        identity_summands += h-1

    def uniform(X, M):
        assert X % M == 0
        return list(range(X, 2*X+1, X//M))

    grids = [[32, 33, 37, 45, 64]]
    grids += [uniform(64, M) for M in (1, 2, 4, 8, 16, 32, 64)]
    grids += [[256, 257, 259, 270, 300, 511, 512]]
    grids += [uniform(1024, M) for M in (1, 4, 16, 64, 256, 512)]
    grids += [uniform(4096, M) for M in (4, 16, 64, 256, 1024)]
    grid_rows = []
    grid_energy_nodes = grid_source_nodes = 0
    for anchors in grids:
        X, M = anchors[0], len(anchors)-1
        assert anchors[-1] == 2*X
        values = {n: F(0) for n in range(X-2, 2*X+3)}
        h5_nontrivial = 0
        for L, R in zip(anchors[:-1], anchors[1:]):
            h = R-L
            if h >= 2:
                h5_nontrivial += h**5
            for n in range(L, R+1):
                j = n-L
                values[n] = a*F(j*j*(h-j)*(h-j), X*h*h)
        assert all(values[n] == 0 for n in anchors)
        low_source, high_source = None, None
        for n in range(X-1, 2*X+2):
            delta = n*(values[n+1]-2*values[n]+values[n-1])
            lo, hi = 1+delta, F(n*n, n*n-1)+delta
            assert lo >= F(3, 4) and hi <= F(27, 16)
            low_source = lo if low_source is None else min(lo, low_source)
            high_source = hi if high_source is None else max(hi, high_source)
            grid_source_nodes += 1
        residual = rat(0)
        for n in range(X, 2*X+1):
            residual = add(residual, rat(values[n]**2/(n*n)))
            grid_energy_nodes += 1
        raw_lower = a*a*F(h5_nontrivial, 2520*X**4)
        jensen_lower = a*a*F((X-M)**5, 2520*M**4*X**4)
        upper = F(sum((R-L)**5 for L, R in zip(anchors[:-1], anchors[1:])), 64*X**4)
        assert raw_lower >= jensen_lower
        assert residual[0] >= rat(raw_lower)[1] or (residual == rat(0) and raw_lower == 0)
        assert residual[1] <= rat(upper)[0]
        grid_rows.append({'X': X, 'M_gaps': M, 'anchors': anchors,
                          'positive_residual_square': record(residual),
                          'gap_sum_lower': str(raw_lower),
                          'jensen_lower': str(jensen_lower),
                          'universal_curvature_upper': str(upper),
                          'source_enclosure_over_checked_nodes': [str(low_source), str(high_source)]})

    tau = div(scale(pi, 2), log2)
    assert tau[0] > rat(9)[1] and tau[1] < rat(10)[0]
    tau2 = square(tau)
    polynomial = add(power(tau, 4), scale(tau2, -161), rat(150))
    assert polynomial[1] < 0
    denominator = mul(log2, mul(add(rat(1), tau2),
                                  mul(add(rat(4), tau2), add(rat(9), tau2))))
    residue_im = div(scale(mul(tau, polynomial), 2*a), denominator)
    assert residue_im[1] < 0

    result = {
        'status': 'PASS',
        'author': 'EM-DIRECT-E7559A / TASK_RESEARCH',
        'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
        'scope': 'Author analytic proof and finite reproduction; not independent Review or formal Result.',
        'arithmetic': 'Exact fractions and outward integer intervals at denominator 10^80; no floating-point decisions.',
        'dependencies': [{
            'path_in_round8_package': str(p.relative_to(args.previous)),
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in (helper_path, constants_path)],
        'fixed_inputs': {'a': str(a), 'f': 'u^2*(1-u)^2',
                         'dyadic_source_node_interval': [3, 16384],
                         'extra_seam_exponents': [2, 20],
                         'energy_block_exponents': [1, 16],
                         'sum_identity_h_interval': [1, 512]},
        'constants': {'gamma': record(gamma), 'log2': record(log2), 'log3': record(log3),
                      'C': record(C), 'baseline_D2': record(D20), 'dyadic_D2': record(D2),
                      'I': record(I), 'J': record(J), 'energy_linear_coefficient_I_over_64': record(slope),
                      'energy_constant_term_CJ_over_4': record(intercept)},
        'source_checks': {'distinct_checked_integer_sources': len(source_nodes),
                          'extra_seam_nodes_requested': extra_seams,
                          'lowest_certified_source_lower': {'n': source_min[0], 'value': str(source_min[1])},
                          'highest_certified_source_upper': {'n': source_max[0], 'value': str(source_max[1])},
                          'all_n_greater_equal_2_analytic_bound': '2/3 < D_n < 27/16'},
        'energy_checks': {'number_of_blocks': len(energy_rows),
                          'closed_integer_point_evaluations': energy_nodes,
                          'rows': energy_rows},
        'sum_identity_checks': {'integer_h_values': 512, 'exact_integer_summands': identity_summands},
        'grid_checks': {'number_of_grids': len(grid_rows),
                        'closed_energy_point_evaluations': grid_energy_nodes,
                        'integer_source_checks_including_nearby_seams': grid_source_nodes,
                        'rows': grid_rows},
        'mellin_obstruction': {'tau_2pi_over_log2': record(tau),
                               'tau4_minus_161tau2_plus_150': record(polynomial),
                               'imaginary_part_of_source_residue_at_1_plus_i_tau': record(residue_im),
                               'conclusion': 'Nonreal residue excludes meromorphic continuation of Z_D through this point.'},
        'calculation_cost': {'new_logarithm_series': 1, 'new_logarithm': 'log(3)',
                             'logarithm_terms': 180, 'new_exponential_evaluations': 0,
                             'new_zeta_or_zero_evaluations': 0, 'new_prime_sieve': False,
                             'previous_program_main_executions': 0,
                             'old_actual_road_queries': 0},
        'limitations': [
            'The all-n assertions are analytic theorems; finite checks only reproduce fixed inputs and boundary cases.',
            'The model is an ordinary complete integer-source road, not the actual prime or thickness-matched road.',
            'The X/M^4 matching upper/lower order concerns positive interpolation residual squared energy.',
            'The scalar full-energy oracle statement supplies a necessary query lower bound; it does not claim a matching full-energy estimation upper bound.',
            'Point-query lower bounds apply only to the declared source class and observation model.']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output': str(args.output),
                      'source_nodes': len(source_nodes), 'dyadic_energy_points': energy_nodes,
                      'sum_identity_h': 512, 'grids': len(grid_rows),
                      'grid_energy_points': grid_energy_nodes, 'grid_source_nodes': grid_source_nodes,
                      'coefficient': record(slope), 'residue_im': record(residue_im)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
