#!/usr/bin/env python3
"""Adjacent-cutoff check using the already constructed complete-road arrays."""
import json
import pickle
import time
from certify_joint_energy import (
    A, B, OUT, F, ZERO, Elementary, linear_sieve, add, sub, neg, rat,
    mul, scale, divide, record, energy, cross, isum,
    green_apply, intersects, main as build_main,
)


def main():
    started = time.perf_counter()
    path = OUT / '_scratch_arrays.pkl'
    if not path.exists():
        build_main()
    with path.open('rb') as handle:
        cache = pickle.load(handle)
    original = json.loads((OUT / 'joint_energy_certificate.json').read_text())
    D, kappa, q = cache['D'], cache['kappa'], cache['q']
    max_cutoff = 512
    _, mu = linear_sieve(max_cutoff)
    c = [ZERO] * (max_cutoff + 1)
    for d in range(1, max_cutoff + 1):
        if mu[d]:
            for n in range(d, max_cutoff + 1, d):
                c[n] = add(c[n], scale(sub(D[n // d], kappa[n // d]), mu[d]))
    elementary = Elementary()
    harmonic = [ZERO]
    for n in range(1, B + 1):
        harmonic.append(add(harmonic[-1], rat(F(1, n))))
    def direct_P(cutoff, n):
        return isum(mul(c[d], add(
            scale(sub(sub(harmonic[n], harmonic[n // d]), elementary.log_integer(d)), F(n, d)),
            rat(F(d - 1 - 2 * (n % d), 2 * d)))) for d in range(2, cutoff + 1))
    results = []
    for cutoff in (128, 256, 512):
        if cutoff == 256:
            P, Q = cache['P'], cache['Q']
            additions = 0
            origin = 'reused certified main arrays'
        else:
            mean = isum(scale(c[d], F(1, d)) for d in range(2, cutoff + 1))
            numerator = [neg(mean)] * (B + 1)
            additions = 0
            for d in range(2, cutoff + 1):
                for n in range(d, B + 1, d):
                    numerator[n] = add(numerator[n], c[d])
                    additions += 1
            rhs = [ZERO] + [scale(numerator[n], F(1, n)) for n in range(1, B + 1)]
            P = green_apply(rhs, A, B, direct_P(cutoff, A), direct_P(cutoff, B))
            Q = [ZERO] * (B + 1)
            for n in range(A, B + 1):
                Q[n] = add(q[n], P[n])
            for n in range(A + 1, B):
                assert intersects(sub(scale(P[n], 2), add(P[n - 1], P[n + 1])), rhs[n])
            assert intersects(P[(A + B) // 2], direct_P(cutoff, (A + B) // 2))
            origin = 'new Green reconstruction from cached complete roads'
        qE, PE, QE, qP = energy(q), energy(P), energy(Q), cross(q, P)
        assert intersects(QE, add(add(qE, scale(qP, 2)), PE))
        Qpositive, qpositive = energy(Q, mode='positive'), energy(q, mode='positive')
        results.append({'H': cutoff, 'origin': origin,
                        'P_at_A': record(P[A]), 'P_at_B': record(P[B]),
                        'P_full_square_energy': record(PE),
                        'cross_q_P': record(qP),
                        'Q_full_square_energy': record(QE),
                        'Q_positive_square_energy': record(Qpositive),
                        'Q_to_q_positive_energy_ratio': record(divide(Qpositive, qpositive)),
                        'correction_divisor_sieve_additions': additions})
    output = {
        'status': 'AUTHOR_STRICT_ADJACENT_CUTOFF_CHECK_PASSED',
        'window': {'A': A, 'B': B, 'theta': '1/2', 'weight': '1/n^2'},
        'question': 'Whether the observed nondecrease is confined to H=256; this is a sensitivity check, not an optimization.',
        'scope': 'Exactly three neighboring dyadic cutoffs on one previously fixed finite family/window; no asymptotic conclusion.',
        'arithmetic': 'Outward integer intervals divided by 10**60; complete-road arrays reused.',
        'complete_road_reconstruction_repeated': False,
        'q_positive_square_energy': original['energies']['q']['positive_square_energy'],
        'results': results,
        'validation': {'new_cutoffs_source_identity_every_interior_integer': True,
                       'new_cutoffs_midpoint_harmonic_cross_check': True,
                       'full_square_cross_identity_every_cutoff': True},
        'elapsed_seconds_diagnostic_only': time.perf_counter() - started,
    }
    target = OUT / 'cutoff_sensitivity.json'
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    for item in results:
        print(json.dumps({'H': item['H'], 'P_energy': item['P_full_square_energy']['lower'],
                          'cross': item['cross_q_P']['lower'],
                          'Q_positive': item['Q_positive_square_energy']['lower'],
                          'Q_to_q_ratio': item['Q_to_q_positive_energy_ratio']['lower']}), flush=True)


if __name__ == '__main__':
    main()
