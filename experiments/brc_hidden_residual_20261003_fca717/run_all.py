#!/usr/bin/env python3
"""Recompute hidden statistics and verify overlaps without rerunning old suites."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def main():
    for name in ('hidden_plane', 'hidden_correlated', 'hidden_dynamics'):
        subprocess.run([sys.executable, str(HERE/f'{name}.py')], check=True)
    plane, correlated, dynamics = [json.loads((HERE/f'{name}_results.json').read_text())
                                  for name in ('hidden_plane', 'hidden_correlated', 'hidden_dynamics')]
    iid = next(c for c in correlated['cases'] if c['rho'] == '0')
    native = {r['n']: r for r in dynamics['multiplicative_noise']['rows']}
    cross_checks = 0
    for row in iid['rows']:
        other = native[row['n']]
        for a, b in [('hidden_second', 'hidden_squared_norm'), ('hidden_kappa4_contraction', 'hidden_kappa4_radial'),
                     ('hidden_standardized_kappa4', 'hidden_gamma4')]:
            assert F(row[a]) == F(other[b])
            cross_checks += 1
    route = {r['n']: r for r in plane['routing_cases'][0]['rows']}
    osc = next(c for c in dynamics['reused_oscillators'] if c['c'] == '1')
    for row in osc['rows']:
        other = route[row['n']]
        for a, b in [('hidden_squared_norm', 'hidden_squared_spread'), ('hidden_kappa4_radial', 'hidden_kappa4_contraction'),
                     ('hidden_gamma4', 'hidden_normalized_kappa4')]:
            assert F(row[a]) == F(other[b])
            cross_checks += 1
    out = dict(status='PASS', horizon=128,
               scope=dict(correlated_sign_parameters=6, finite_window_lengths=3, integrated_noise=1,
                          multiplicative_noise=1, existing_oscillator_hidden_statistics=5,
                          old_planar_law_preserving_axis_routings=3, new_directed_response_coupling=1),
               scope_note='20 configurations with overlaps; 128 hidden-statistic timepoints each. Prior oscillator full moment suites were reused, not rerun.',
               cross_module_exact_equalities=cross_checks,
               plane_exact_assertions=plane['exact_check_calls'], plane_counters=plane['checks'],
               correlated_counters=correlated['checks'], correlated_independent_words=correlated['independent_axis_word_checks'],
               dynamics_exact_assertions=dynamics['checks_total'], dynamics_counters=dynamics['checks_by_category'],
               source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.glob('*.py'))},
               results_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.glob('*_results.json'))})
    (HERE/'summary.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    plot(plane, correlated, dynamics)
    print(json.dumps(dict(status='PASS', cross_module_exact_equalities=cross_checks, summary=str(HERE/'summary.json'))))


def plot(plane, correlated, dynamics):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 10, 'svg.hashsalt': 'brc-hidden-residual'})
    fig, axs = plt.subplots(2, 2, figsize=(11.5, 8), layout='constrained')
    widths = [F(0), F(4, 3), F(2), F(10, 3)]
    for offset, rho in enumerate(('-1', '0', '1')):
        case = next(c for c in correlated['cases'] if c['rho'] == rho)
        law = dict((F(q), F(p)) for q, p in next(r for r in case['short_full_distribution'] if r['n'] == 2)['hidden_squared_width_law'])
        axs[0, 0].bar([i+.23*(offset-1) for i in range(4)], [float(law.get(q, F())) for q in widths], width=.23, label=f'Correlation {rho}')
    axs[0, 0].set(xticks=range(4), xticklabels=['0', '4/3', '2', '10/3'], xlabel='Hidden squared norm at step 2', ylabel='Exact probability',
                  title='Same second/fourth moments, different distributions')
    for rho in ('-1/2', '0', '1/2', '1'):
        rows = next(c['rows'] for c in correlated['cases'] if c['rho'] == rho)
        axs[0, 1].loglog([r['n'] for r in rows], [float(F(r['hidden_kappa6_contraction'])) for r in rows], 'o-', label=f'Correlation {rho}')
    axs[0, 1].set(title='Sixth cumulant recovers the sign correlation', xlabel='Step n', ylabel='Hidden sixth cumulant contraction')
    base = next(c['rows'] for c in correlated['cases'] if c['rho'] == '0')
    series = [(base, 'hidden_second', 'Hidden native displacement'),
              (dynamics['windows'][2]['rows'], 'hidden_squared_norm', 'Hidden window (L=8)'),
              (dynamics['integrated_noise']['rows'], 'hidden_squared_norm', 'Hidden integrated response'),
              (plane['directed_coupling']['rows'], 'hidden_response_squared_spread', 'Hidden response with directed coupling')]
    for rows, key, label in series:
        positive = [r for r in rows if F(r[key]) > 0]
        axs[1, 0].loglog([r['n'] for r in positive], [float(F(r[key])) for r in positive], 'o-', label=label)
    axs[1, 0].set(title='Absolute hidden spread can grow or saturate', xlabel='Step n', ylabel='Hidden mean squared norm (typed quantities)')
    rows = plane['hidden_returns']['rows']
    axs[1, 1].semilogx([r['n'] for r in rows], [float(F(r['n_squared_hidden_zero_probability'])) for r in rows], 'o-', label='Exact n^2 P(H=0)')
    axs[1, 1].axhline(plane['hidden_returns']['asymptotic_constant_decimal'], color='gray', linestyle='--', label='3 / pi^2 (proved limit)')
    axs[1, 1].set(title='Hidden readout-kernel return has a time inverse square law', xlabel='Step n', ylabel='Scaled hidden return probability')
    for ax in axs.flat:
        ax.legend(fontsize=8)
        ax.grid(True, alpha=.2)
    fig.suptitle('Hidden residuals in native X6: exact matched-model review\nProjection rank is not spatial dimension; response amplitudes are not Cell positions', fontsize=13)
    fig.savefig(HERE/'hidden_comparison.svg', metadata={'Date': None})
    fig.savefig(HERE/'hidden_comparison.png', dpi=170)
    plt.close(fig)


if __name__ == '__main__':
    main()
