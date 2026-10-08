#!/usr/bin/env python3
"""Derived cross-module counts and illustrative plots, not independent evidence."""
from pathlib import Path
import json
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent


def main():
    w = json.loads((HERE/'weighted_results.json').read_text())
    m = json.loads((HERE/'markov_results.json').read_text())
    audit = json.loads((HERE/'audit_results.json').read_text())
    weighted_rows = sum(x['data_rows'] for x in w['trajectory_files'])
    markov_rows = sum(x['rows'] for x in m['cases'])
    summary = {
        'status': 'COMPLETED_WITH_RESEARCH_INTERNAL_AUDIT',
        'evidence_level': 'Declared synthetic models; finite deterministic evaluations plus model-specific derivations. No empirical physical law or formal Driver acceptance.',
        'prior_source_commit': '46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c',
        'counts': {'weighted_parameter_paths': len(w['paths']), 'weighted_rows': weighted_rows,
                   'markov_parameter_paths': len(m['cases']), 'markov_rows': markov_rows,
                   'total_parameter_paths': len(w['paths'])+len(m['cases']),
                   'total_deterministic_time_rows': weighted_rows+markov_rows,
                   'markov_undefined_gamma_rows': sum(x['undefined_rows'] for x in m['cases'])},
        'counting_note': 'Rows within and across paths are dependent deterministic model evaluations, not independent experiments. Reused controls are included. Two mechanism families receive parameter/horizon extensions; no expansion of the prior 11-family count is claimed.',
        'audit_file': 'audit_results.json',
        'audit_status': audit.get('status'),
        'source_files': ['weighted_results.json', 'markov_results.json', 'INDEPENDENT_REVIEW.md'],
        'full_data': 'Per-parameter CSV gzip shards listed in module results and manifest.json; all integer times retained.'
    }
    (HERE/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    plt.rcParams.update({'svg.hashsalt':'brc-fit-20261002-9d72ac','font.size':10})
    fig, axs = plt.subplots(2,2,figsize=(12,8),layout='constrained')
    desired = {'-0.75','-0.5','-0.4','-0.25','0','1'}
    for case in w['paths']:
        if str(case['p']) not in desired:
            continue
        rows = case['samples']
        n = [r['n'] for r in rows]
        g = [abs(float(r['gamma4'])) for r in rows]
        axs[0,0].loglog(n,g,label='p='+str(case['p']))
        dyadic = [(r['n'], abs(float(r['gamma4']))) for r in rows if r['n'] & (r['n']-1) == 0]
        slopes = [(math.log(dyadic[i-1][1]/dyadic[i][1])/math.log(2)) for i in range(1,len(dyadic))]
        axs[0,1].semilogx([r[0] for r in dyadic[1:]],slopes,label='p='+str(case['p']))
    axs[0,0].set(title='Weighted independent signs: sampled trajectories',xlabel='Time n',ylabel='Absolute standardized fourth cumulant')
    axs[0,1].set(title='Finite-interval time slopes drift near thresholds',xlabel='Time n',ylabel='Dyadic secant exponent (n/2 to n)')
    critical = None
    for case in m['cases']:
        expr = case['rho_expression']
        is_critical = case.get('critical_offset') in ('0',0) or case['id']=='critical'
        if is_critical:
            critical = case
        if expr not in ('-0.5','0','0.5') and not is_critical:
            continue
        rows = [r for r in case['samples'] if r['gamma4'] is not None]
        axs[1,0].semilogx([r['n'] for r in rows],[r['n']*float(r['gamma4']) for r in rows],label=expr)
    axs[1,0].set(title='Correlated signs: signed leading coefficient',xlabel='Time n',ylabel='n times standardized fourth cumulant')
    axs[1,0].axhline(0,color='grey',lw=.6)
    if critical:
        rows = [r for r in critical['samples'] if r['n']>=4 and r['gamma4'] is not None]
        axs[1,1].semilogx([r['n'] for r in rows],[r['n']**2*float(r['gamma4']) for r in rows],label='critical rho = sqrt(3)-2')
    axs[1,1].axhline(-3,color='black',linestyle='--',label='derived limit -3')
    axs[1,1].set(title='Isolated cancellation leaves inverse-square time term',xlabel='Time n',ylabel='n squared times standardized fourth cumulant')
    for ax in axs.flat:
        ax.grid(alpha=.2)
        ax.legend(fontsize=8)
    fig.suptitle('BRC residual fitting: declared synthetic models, no physical-distance claim')
    fig.savefig(HERE/'fit_overview.png',dpi=150)
    fig.savefig(HERE/'fit_overview.svg',metadata={'Date':None})
    plt.close(fig)
    print(json.dumps(summary['counts']))


if __name__ == '__main__':
    main()
