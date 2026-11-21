#!/usr/bin/env python3
"""New strict finite checks for the noncancellable divisor-phase band.

The general growth law is proved in JOINT_VARIANCE_GROWTH.md.  This file
quantifies its mechanism for the already matched rational node family.
All certificate comparisons use integers or Fraction, without tolerance.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rh_correlation_rational.certify_matched_nodes import (  # noqa: E402
    Elementary, ONE, ZERO, SCALE, DIGITS, rat, add, sub, scale, mul,
    divide, linear_sieve,
)
from rh_correlation_phase.verify_phase_homogenization import (  # noqa: E402
    actual_coefficients, isum, jordan, output, square, variance,
)


def psi(elementary, nodes, weights, t):
    return isum(scale(sub(ONE, elementary.exp_negative(scale(t, a))), w / a)
                for a, w in zip(nodes, weights))


def main():
    start = time.monotonic()
    source = ROOT / 'rh_correlation_rational/rational_window_certificate.json'
    raw = source.read_bytes()
    previous = json.loads(raw)
    nodes = [F(x) for x in previous['node_certificate']['nodes']]
    weights = [F(x) for x in previous['node_certificate']['weights']]
    assert len(set(nodes)) == len(nodes) == len(weights)
    for j, a in enumerate(nodes):
        exact = F(1)
        for k, b in enumerate(nodes):
            if k != j:
                exact *= b / (b - a)
        assert exact == weights[j]
    assert all(F(0) < a <= F(1, 2) for a in nodes)
    assert sum(weights) == 1

    elementary = Elementary()
    Z = previous['window']['Z']
    m = len(nodes)
    lnZ = elementary.log_integer(Z)
    assert m >= 10 and lnZ[1] <= m * SCALE
    assert lnZ[0] > (m - 1) * SCALE
    assert F(11, 16) ** 5 < F(1, 6)
    K0 = F(43, 2211840)
    assert K0 * F(25, 36) * F(49, 64) > F(1, 100000)

    cutoffs = [256, 512, 1024]
    c, _, _, spf = actual_coefficients(elementary, nodes, weights, max(cutoffs))
    _, mu = linear_sieve(max(cutoffs))
    c0 = sub(scale(elementary.log_integer(2), 2), ONE)
    M = sum((1 / a for a in nodes), F(0))
    rows = []
    for H in cutoffs:
        total = variance(c, H, spf)
        high = ZERO
        high_sf = ZERO
        count_sf = 0
        for s in range(H // 2 + 1, H + 1):
            factor = F(jordan(s, 4, spf) + 10 * jordan(s, 2, spf), 720 * s * s)
            term = scale(square(c[s]), factor)
            high = add(high, term)
            if mu[s]:
                high_sf = add(high_sf, term)
                count_sf += 1
        assert count_sf * 16 >= H
        assert high[1] <= total[0]
        assert high_sf[1] <= high[0]

        lnH = elementary.log_integer(H)
        lnHalf = elementary.log_integer(H // 2)
        psiH = psi(elementary, nodes, weights, lnH)
        psiHalf = psi(elementary, nodes, weights, lnHalf)
        assert psiH[0] >= scale(lnH, F(5, 6))[1]
        assert psiHalf[0] >= scale(lnHalf, F(5, 6))[1]
        concavity_comparator = scale(psiH, F(7, 8))
        assert psiHalf[0] >= concavity_comparator[1]
        exponential_comparator = scale(
            sub(ONE, elementary.exp_negative(scale(lnH, 1 / M))), M)
        assert psiH[0] >= exponential_comparator[1]

        lower_sharp = scale(square(add(psiHalf, scale(c0, F(1, 2)))), K0 * H ** 3)
        lower_uniform = scale(square(add(psiH, c0)), F(43, 8847360) * H ** 3)
        lower_clean = scale(square(lnH), F(H ** 3, 100000))
        upper_kernel = scale(square(add(psiH, c0)), F(H ** 3, 60))
        upper_clean = scale(square(add(lnH, c0)), F(H ** 3, 60))
        assert lower_sharp[1] <= high_sf[0]
        assert lower_uniform[1] <= total[0]
        assert lower_clean[1] <= total[0]
        assert total[1] <= upper_kernel[0]
        assert total[1] <= upper_clean[0]
        normalization = scale(square(lnH), H ** 3)
        rows.append({
            'H': H,
            'squarefree_population_in_high_band': count_sf,
            'population_lower_H_over_16': str(F(H, 16)),
            'joint_variance': output(total),
            'high_band_variance': output(high),
            'high_squarefree_band_variance': output(high_sf),
            'high_band_fraction_of_total': output(divide(high, total)),
            'high_squarefree_band_fraction_of_total': output(divide(high_sf, total)),
            'normalized_variance_by_H3_logH2': output(divide(total, normalization)),
            'psi_at_logH': output(psiH),
            'psi_at_logH_over_2': output(psiHalf),
            'theorem_8_lower': output(lower_sharp),
            'theorem_9_lower': output(lower_uniform),
            'theorem_15_lower': output(lower_clean),
            'theorem_8_upper': output(upper_kernel),
            'theorem_15_upper': output(upper_clean),
            'all_interval_separations_passed': True,
        })

    dependencies = [
        source,
        ROOT / 'rh_correlation_rational/certify_matched_nodes.py',
        ROOT / 'rh_correlation_phase/verify_phase_homogenization.py',
        Path(__file__).resolve(),
        Path(__file__).with_name('JOINT_VARIANCE_GROWTH.md'),
    ]
    result = {
        'status': 'AUTHOR_PROOF_AND_NEW_STRICT_HIGH_BAND_CERTIFICATES_PASSED',
        'scope': 'complete_common_period_variance; no anchored_window_lower_bound',
        'arithmetic': 'directed_integer_intervals_and_exact_Fraction; no tolerance',
        'interval_denominator_power_of_10': DIGITS,
        'node_window': {'Z': Z, 'm': m, 'max_node': str(max(nodes))},
        'nodes_exact': [str(x) for x in nodes],
        'weights_exact': [str(x) for x in weights],
        'inverse_thickness_sum_M_exact': str(M),
        'inverse_thickness_sum_M_enclosure': output(rat(M)),
        'source_files_sha256': {
            str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in dependencies
        },
        'exact_lagrange_weights_checked': True,
        'complete_coefficient_cross_road_check_max_n': max(cutoffs),
        'rows': rows,
        'elapsed_seconds_diagnostic_only': round(time.monotonic() - start, 6),
    }
    target = Path(__file__).with_name('joint_variance_certificate.json')
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        'status': result['status'],
        'output': str(target),
        'M': result['inverse_thickness_sum_M_enclosure'],
        'rows': [{
            'H': r['H'],
            'squarefree_count': r['squarefree_population_in_high_band'],
            'V': r['joint_variance'],
            'high_band_fraction': r['high_band_fraction_of_total'],
            'high_sf_fraction': r['high_squarefree_band_fraction_of_total'],
            'normalized_V': r['normalized_variance_by_H3_logH2'],
        } for r in rows],
        'elapsed_seconds_diagnostic_only': result['elapsed_seconds_diagnostic_only'],
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
