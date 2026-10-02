#!/usr/bin/env python3
"""Reproduce the finite expanded suite, ledger and illustrative plots.

Core checks use exact rational arithmetic. Matplotlib is optional and is used
only for presentation. Plotted floating point values never decide a check.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sys
import dynamics_types
import related_branches
import graph_boundaries

HERE=Path(__file__).resolve().parent


def plot(related, dynamics, graph):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':10, 'svg.hashsalt':'brc-expanded-types-20261002'})
    fig, axes=plt.subplots(2,2,figsize=(12,8),layout='constrained')
    ax=axes[0,0]
    for name, case in related['weighted_independent']['families'].items():
        rows=case['rows']
        ax.loglog([r['n'] for r in rows],[abs(float(r['gamma4'])) for r in rows],label=name)
    ax.set(title='Independent weighted sums: decay or plateau',xlabel='Step n',ylabel='Absolute standardized fourth cumulant')
    ax.legend(fontsize=8)
    ax=axes[0,1]
    for rho in ('-1/2','0','1/2','3/4'):
        case=related['markov_signs']['correlations'][rho]
        ax.semilogx([r['n'] for r in case['rows']],[float(r['n_gamma4']) for r in case['rows']],label='rho = '+rho)
    ax.axhline(0,color='grey',linewidth=.6)
    ax.set(title='Correlated signs: finite-time corrections matter',xlabel='Step n',ylabel='n times standardized fourth cumulant')
    ax.legend(fontsize=8)
    ax=axes[1,0]
    rows=dynamics['multiplicative']['rows']
    ax.plot([r['n'] for r in rows],[float(r['gamma4']) for r in rows],'o-',color='#9c2348')
    ax.set_yscale('symlog',linthresh=2)
    ax.set(title='Random multipliers: eventual growth (sampled)',xlabel='Step n',ylabel='Standardized fourth cumulant; symlog')
    ax.axhline(0,color='grey',linewidth=.6)
    ax=axes[1,1]
    for case in graph['results']:
        if case['id'].startswith('absorbing'):
            continue
        samples=case['samples_primary']
        ax.semilogy([r['t'] for r in samples],
                    [float(r['tv_to_uniform']) for r in samples],'o-',label=case['id'])
    ax.set(title='Finite graphs: periodic persistence or mixing',xlabel='Step t',ylabel='Total variation to uniform; sampled')
    ax.legend(fontsize=8)
    for ax in axes.flat:
        ax.grid(True,alpha=.2)
    fig.suptitle('BRC residuals across declared synthetic model types',fontsize=15)
    fig.savefig(HERE/'residual_types.svg',metadata={'Date':None})
    fig.savefig(HERE/'residual_types.png',dpi=150)
    plt.close(fig)


def main():
    related=related_branches.run()
    dynamics=dynamics_types.run()
    graph=graph_boundaries.run()
    (HERE/'graph_results.json').write_text(json.dumps(graph,default=graph_boundaries.serialize,indent=2)+'\n')
    # Repeated mechanism / alternative realization, not independent evidence.
    weighted=related['weighted_independent']['families']['linear_j']['rows']
    for row in dynamics['integrated_noise']['rows']:
        if row['n']>1:
            reference=weighted[row['n']-2]
            assert row['position_variance']==reference['variance']
            assert row['gamma4']==reference['gamma4']
    decay=related['weighted_independent']['families']['geometric_decay']['rows']
    growth=related['weighted_independent']['families']['geometric_growth']['rows']
    assert all(a['gamma4']==b['gamma4'] for a,b in zip(decay,growth))
    files=['related_branches.py','dynamics_types.py','graph_boundaries.py','run_all.py',
           'related_results.json','dynamics_results.json','graph_results.json']
    summary=dict(status='PASS',mechanism_families=11,
        counting_note='Families include controls. Integrated noise repeats the linear-weight mechanism. Check counters overlap; do not sum as independent experiments.',
        checks=dict(related=related['counts'],dynamics=dynamics['counts'],
            graph=dict(matrices=graph['matrices'],starts_per_matrix=graph['starts_per_matrix'],
                       exact_assertions=graph['checks_total'])),
        cross_module_checks=dict(integrated_weighted_sample_pairs=sum(r['n']>1 for r in dynamics['integrated_noise']['rows']),
                                 reciprocal_geometric_gamma_pairs=len(decay)),
        source_sha256={p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in files})
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    if '--no-plot' not in sys.argv:
        plot(related,dynamics,graph)
    print(json.dumps(summary['checks']))


if __name__=='__main__':
    main()
