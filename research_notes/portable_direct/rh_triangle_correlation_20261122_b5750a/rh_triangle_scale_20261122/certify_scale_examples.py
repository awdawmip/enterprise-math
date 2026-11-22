#!/usr/bin/env python3
"""Exact checks for auxiliary bounded-source families, not arithmetic roads.

No external packages. All source/hat/elimination/reconstruction tests are exact.
Energy enclosures round each rational term outwards to the common denominator
10**30, and are never used as finite evidence for an infinite arithmetic claim.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import time


OUT = Path(__file__).resolve().parent
ROUND_DENOMINATOR = 10**30


def rational(value):
    value = F(value)
    with localcontext() as ctx:
        ctx.prec = 22
        approximation = str(Decimal(value.numerator) / Decimal(value.denominator))
    return {
        'numerator': str(value.numerator),
        'denominator': str(value.denominator),
        'decimal_approximation': approximation,
    }


def fixed_decimal(numerator):
    quotient, remainder = divmod(numerator, ROUND_DENOMINATOR)
    return f'{quotient}.{remainder:030d}'


def energy_enclosure(numerators, common_denominator, start):
    lower = upper = nonzero = 0
    denominator_square = common_denominator**2
    for offset, numerator in enumerate(numerators):
        if not numerator:
            continue
        nonzero += 1
        n = start + offset
        denominator = denominator_square * n * n
        quotient, remainder = divmod(numerator*numerator*ROUND_DENOMINATOR,
                                   denominator)
        lower += quotient
        upper += quotient + bool(remainder)
    assert upper - lower <= nonzero
    return {
        'lower_numerator': str(lower),
        'upper_numerator': str(upper),
        'denominator': str(ROUND_DENOMINATOR),
        'lower_decimal': fixed_decimal(lower),
        'upper_decimal': fixed_decimal(upper),
        'outward_rounded_term_count': nonzero,
    }, F(lower, ROUND_DENOMINATOR), F(upper, ROUND_DENOMINATOR)


def build_case(label, X, span, h, amplitude, fine_step, family):
    """A repeated quartic bump, with all integer values and true endpoints."""
    amplitude = F(amplitude)
    assert X >= span >= h >= 4
    assert span % h == 0 and h % 4 == 0
    assert h % fine_step == 0 and fine_step >= 1
    cell_count = span // h
    node_intervals = span // fine_step
    assert node_intervals & (node_intervals - 1) == 0
    assert 0 < amplitude <= 1
    left, right = X, X+span
    qden = X*h*h*amplitude.denominator
    qnum = []
    for offset in range(span+1):
        r = offset % h
        qnum.append(amplitude.numerator*r*r*(h-r)*(h-r))
    assert qnum[0] == qnum[-1] == 0
    fnum = [0]*(span+1)
    exact_source_checks = 0
    for offset in range(1, span):
        fnum[offset] = 2*qnum[offset]-qnum[offset-1]-qnum[offset+1]
        r = offset % h
        if r:
            expected = amplitude.numerator*(-2*h*h+12*h*r-12*r*r-2)
        else:
            expected = -2*amplitude.numerator*(h-1)*(h-1)
        assert fnum[offset] == expected
        assert -2*amplitude.numerator*h*h <= expected <= amplitude.numerator*h*h
        assert abs(F(expected, qden)) <= F(4, left+offset)
        exact_source_checks += 1

    prefix_f, prefix_nf = [0], [0]
    for offset, v in enumerate(fnum):
        prefix_f.append(prefix_f[-1]+v)
        prefix_nf.append(prefix_nf[-1]+(left+offset)*v)

    def sums(lo, hi):
        if lo > hi:
            return 0, 0
        a, b = lo-left, hi-left+1
        return prefix_f[b]-prefix_f[a], prefix_nf[b]-prefix_nf[a]

    def hat_moment(L, x, R):
        fl, nfl = sums(L+1, x)
        fr, nfr = sums(x+1, R-1)
        return (F(nfl-L*fl, x-L)+F(R*fr-nfr, R-x))/qden

    nodes = list(range(left, right+1, fine_step))
    mass = {nodes[0]: F(0), nodes[-1]: F(0)}
    for k, x in enumerate(nodes[1:-1], 1):
        L, R = nodes[k-1], nodes[k+1]
        t = F(qnum[x-left]-qnum[L-left], (x-L)*qden)
        t -= F(qnum[R-left]-qnum[x-left], (R-x)*qden)
        mass[x] = t
        assert t == hat_moment(L, x, R)

    interpolation = [0]*(span+1)
    for L, R in zip(nodes, nodes[1:]):
        for n in range(L, R):
            numerator = (R-n)*qnum[L-left]+(n-L)*qnum[R-left]
            assert numerator % (R-L) == 0
            interpolation[n-left] = numerator//(R-L)
    interpolation[-1] = qnum[-1]

    reconstructed, positive_envelope = [0]*(span+1), [0]*(span+1)
    levels = []
    current = list(nodes)
    target_layer = None
    packet_count = positive_count = exact_hat_checks = 0
    while len(current) > 2:
        retained = current[::2]
        assert retained[-1] == current[-1]
        packets = []
        for k in range(1, len(current)-1, 2):
            L, x, R = current[k-1:k+2]
            t = mass[x]
            assert t == hat_moment(L, x, R)
            exact_hat_checks += 1
            packets.append((L, x, R, t))
            mass[L] += t*F(R-x, R-L)
            mass[R] += t*F(x-L, R-L)
            del mass[x]
            scaled_t = t*qden
            assert scaled_t.denominator == 1
            tn = scaled_t.numerator
            for n in range(L+1, R):
                gn = (n-L)*(R-x) if n <= x else (x-L)*(R-n)
                value_numerator = tn*gn
                assert value_numerator % (R-L) == 0
                value = value_numerator//(R-L)
                reconstructed[n-left] += value
                if t > 0:
                    positive_envelope[n-left] += value
        supports = {R-L for L, _, R, _ in packets}
        assert len(supports) == 1
        delta = supports.pop()
        sum_positive_square = sum((t*t for _, _, _, t in packets if t > 0), F(0))
        weighted = sum(((R-L)**3*t*t for L, _, R, t in packets if t > 0), F(0))
        normalized = weighted/(X*X)
        source_upper = amplitude**2*span*delta**4/(4*X**4)
        assert normalized <= source_upper
        if delta > h:
            assert all(t == 0 for _, _, _, t in packets)
        if delta == h:
            assert len(packets) == cell_count
            assert all(t == amplitude*F(h, 4*X) for _, _, _, t in packets)
            target_layer = len(levels)+1
            assert sum_positive_square == amplitude**2*F(span*h, 16*X*X)
        positive_here = sum(t > 0 for _, _, _, t in packets)
        levels.append({
            'local_level': len(levels)+1,
            'support_width': delta,
            'packet_count': len(packets),
            'positive_packet_count': positive_here,
            'zero_packet_count': sum(t == 0 for _, _, _, t in packets),
            'sum_positive_charge_square': rational(sum_positive_square),
            'scale_normalized_square_sum': rational(normalized),
            'old_condition_required_C_squared': rational(X*sum_positive_square),
            'exact_source_bound_for_normalized_sum': rational(source_upper),
        })
        packet_count += len(packets)
        positive_count += positive_here
        current = retained
    assert reconstructed == interpolation
    assert packet_count == len(nodes)-2
    assert all(i <= u for i, u in zip(interpolation, positive_envelope))

    positive_remainder = []
    remainder_source_upper_num = F(0)
    for L, R in zip(nodes, nodes[1:]):
        width = R-L
        remainder_source_upper_num += F(width**5-width, 120*X**4)*amplitude**2
        for n in range(L, R):
            value = qnum[n-left]-interpolation[n-left]
            positive_remainder.append(max(0, value))
            actual = F(value, qden)
            bound = amplitude*F((n-L)*(R-n), 2*X)
            assert actual <= bound
    positive_remainder.append(0)

    energy, elo, ehi = energy_enclosure(qnum, qden, X)
    rem_energy, rlo, rhi = energy_enclosure(positive_remainder, qden, X)
    envelope_energy, _, _ = energy_enclosure(positive_envelope, qden, X)
    scale = amplitude**2*F(span*h**4, X**4)
    analytic_lower = F(81, 524288)*scale
    analytic_upper = F(1, 256)*scale
    assert elo >= analytic_lower
    assert ehi <= analytic_upper
    assert rhi <= remainder_source_upper_num
    if family in ('full_critical', 'coarse_critical'):
        assert scale == 1
        assert all(F(int(r['scale_normalized_square_sum']['numerator']),
                     int(r['scale_normalized_square_sum']['denominator'])) <= F(1, 4)
                   for r in levels)
    if fine_step < h:
        assert target_layer is not None

    return {
        'label': label,
        'scope': 'auxiliary integer-source family; not an arithmetic road',
        'family': family,
        'X': X, 'right_endpoint': right, 'span': span, 'cell_width': h,
        'cell_count': cell_count, 'amplitude': rational(amplitude),
        'fine_step': fine_step, 'fine_interval_count': node_intervals,
        'all_integer_values_count': span+1,
        'actual_endpoint_values': ['0', '0'],
        'dyadic_block_chord': 'identically zero',
        'exact_source_checks': exact_source_checks,
        'source_min': rational(F(min(fnum[1:-1]), qden)),
        'source_max': rational(F(max(fnum[1:-1]), qden)),
        'exact_hat_moment_checks': exact_hat_checks,
        'packet_count': packet_count,
        'positive_packet_count': positive_count,
        'target_h_layer': target_layer,
        'all_coarser_than_h_charges_zero': True,
        'exact_interpolation_reconstruction': True,
        'all_local_positive_remainders_below_curvature_parabola': True,
        'critical_energy_scale_a2_span_h4_over_X4': rational(scale),
        'true_energy_interval': energy,
        'true_energy_analytic_lower': rational(analytic_lower),
        'true_energy_analytic_upper': rational(analytic_upper),
        'positive_envelope_energy_interval': envelope_energy,
        'positive_remainder_energy_interval': rem_energy,
        'positive_remainder_source_upper': rational(remainder_source_upper_num),
        'levels': levels,
        'embedding_in_length_matched_window': {
            'A': X, 'B': X*X,
            'rule': 'for full-block families extend q by zero beyond 2X',
            'scope': 'length quantifier only; not arithmetic matching',
        } if span == X else None,
    }


def main():
    begin = time.perf_counter()
    cases = []
    for s in (2, 4, 8):
        cases.append(build_case(f'critical_s{s}', s**4, s**4, s**3,
                                F(1), s**3//2, 'full_critical'))
    for s in (2, 4):
        cases.append(build_case(f'coarse_s{s}', s**8, s**8, s**7,
                                F(1, s**2), s**5, 'coarse_critical'))
    for s in (2, 4):
        cases.append(build_case(f'above_fine_threshold_s{s}', s**5, s**5,
                                s**4, F(1), s**4//2, 'above_fine_threshold'))
    for s in (2, 4, 8):
        cases.append(build_case(f'tail_critical_s{s}', s**5, s**4, s**4,
                                F(1), s**4, 'tail_critical'))
    for s in (2, 4):
        cases.append(build_case(f'tail_above_threshold_s{s}', s**6, s**5,
                                s**5, F(1), s**5, 'tail_above_threshold'))
    report = {
        'schema': 'RH_SCALE_ADAPTED_EXACT_SOURCE_EXAMPLES_V1',
        'date': '2026-11-22',
        'arithmetic_road_recomputed': False,
        'scope': 'exact auxiliary examples supporting proved general-source assertions',
        'source_filename': Path(__file__).name,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'outward_energy_denominator': str(ROUND_DENOMINATOR),
        'case_count': len(cases),
        'verified_integer_source_locations': sum(c['exact_source_checks'] for c in cases),
        'verified_packet_hat_moments': sum(c['exact_hat_moment_checks'] for c in cases),
        'cases': cases,
    }
    target = OUT/'scale_examples_certificate.json'
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    summary = {k: report[k] for k in ('case_count',
               'verified_integer_source_locations', 'verified_packet_hat_moments')}
    summary['elapsed_seconds'] = round(time.perf_counter()-begin, 3)
    print(json.dumps(summary, ensure_ascii=False))
    for c in cases:
        print(c['label'], 'E in', c['true_energy_interval']['lower_decimal'],
              c['true_energy_interval']['upper_decimal'])


if __name__ == '__main__':
    main()
