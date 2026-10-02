#!/usr/bin/env python3
"""Recompute all matched replays, cross-check overlap, and render a figure."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def main():
    for name in ('weighted_return', 'correlated', 'oscillation'):
        subprocess.run([sys.executable, str(HERE/f'{name}_replay.py')], check=True)
    weighted, correlated, oscillation = [json.loads((HERE/f'{name}_results.json').read_text())
                                         for name in ('weighted_return', 'correlated', 'oscillation')]
    wr = {r['n']: r for r in weighted['weighted']['families']['equal']['rows']}
    cr = {r['n']: r for c in correlated['cases'] if c['rho'] == '0' for r in c['rows']}
    ore = {r['t']: r for c in oscillation['cases'] if c['c'] == '1' for r in c['rows']}
    common = sorted(set(wr) & set(cr) & set(ore))
    for n in common:
        assert F(wr[n]['full_six_response_normalized']) == F(cr[n]['full_gamma4']) == F(ore[n]['full_Z_gamma']) == -F(1, 3*n)
        assert F(wr[n]['response_squared_spread']) == F(cr[n]['full_msd']) == F(ore[n]['full_Z_squared_response']) == n
    out = dict(status='PASS', horizon=128,
               scope='4 weighted families, 6 sign correlations, 3 original oscillators and 2 hidden-response alternatives; matched scalar/planar return laws',
               cross_module_common_times=common, cross_module_exact_checks=2*len(common),
               checks=dict(weighted=weighted['weighted']['checks'], returns=weighted['returns']['checks'],
                           correlated=correlated['checks'], oscillation=oscillation['checks_by_category']),
               source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in sorted(HERE.glob('*.py'))},
               numerical_results_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                         for p in sorted(HERE.glob('*_results.json'))})
    (HERE/'summary.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    plot(weighted, correlated, oscillation)
    print(json.dumps(dict(status='PASS', cross_module_exact_checks=2*len(common), summary=str(HERE/'summary.json'))))


def plot(weighted, correlated, oscillation):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    matplotlib.rcParams.update({'font.size': 10, 'svg.hashsalt': 'brc-matched-x6'})
    fig, axs = plt.subplots(2, 2, figsize=(11.5, 8), layout='constrained')
    data = weighted['returns']['rows']
    for key, label in [('old_scalar_return', 'Old scalar return'), ('old_plane_return', 'Old planar return'), ('full_X6_return', 'Complete native X6 return')]:
        axs[0, 0].loglog([r['step'] for r in data], [float(F(r[key])) for r in data], label=label)
    axs[0, 0].set(title='Same old walks, different return events', xlabel='Step n (even)', ylabel='Exact return probability')
    data = next(c['rows'] for c in correlated['cases'] if c['rho'] == '-1')
    even = [r for r in data if r['n'] % 2 == 0]
    for key, label in [('scalar_variance', 'Old scalar variance = 0'), ('full_msd', 'Native X6 mean squared displacement')]:
        axs[0, 1].plot([r['n'] for r in even], [float(F(r[key])) for r in even], 'o-', label=label)
    axs[0, 1].set(title='Alternating signs: hidden spread survives', xlabel='Step n (even)', ylabel='Squared displacement')
    data = next(c['rows'] for c in correlated['cases'] if c['rho'] == '-1/2')
    for key, label in [('scalar_gamma4', 'Old scalar: n times normalized cumulant'), ('full_gamma4', 'Full X6: n times normalized contraction')]:
        axs[1, 0].semilogx([r['n'] for r in data], [r['n']*float(F(r[key])) for r in data], 'o-', label=label)
    axs[1, 0].axhline(0, color='gray', linewidth=.8)
    axs[1, 0].set(title='Correlation -1/2: fourth-order signs differ', xlabel='Step n', ylabel='Scaled fourth-order statistic')
    for case in (oscillation['cases'][0], *oscillation['cases'][3:]):
        data = case['rows']
        axs[1, 1].semilogy([r['t'] for r in data], [float(F(r['hidden_K_Z_squared_response'])) for r in data], 'o-', label=f"Hidden gain {case['hidden_gain']}")
    axs[1, 1].set(title='Identical old damped response, different hidden response', xlabel='Step n', ylabel='Hidden response squared amplitude')
    for ax in axs.flat:
        ax.grid(True, alpha=.2)
        ax.legend(fontsize=8)
    fig.suptitle('Matched prior BRC studies recomputed in native X6\nDeclared lifts; response amplitudes are distinct from native Cell positions', fontsize=13)
    fig.savefig(HERE/'comparison.svg', metadata={'Date': None})
    fig.savefig(HERE/'comparison.png', dpi=170)
    plt.close(fig)


if __name__ == '__main__':
    main()
