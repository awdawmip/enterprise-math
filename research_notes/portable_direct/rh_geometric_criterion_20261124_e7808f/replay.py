#!/usr/bin/env python3
"""Replay the four current branches into a separate output directory."""
from pathlib import Path
import argparse
import importlib.metadata
import importlib.util
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
OLD_NAME = 'riemann_cumulative_haar_20261123'
HELPER = 'dependencies/certify_fast_harmonic_energy.py'
BRANCHES = {
    'geometric_compute': {
        'script':'certify_geometric_tents.py',
        'certificate':'geometric_tent_certificate.json',
        'source_inputs':['fixed_geometry.json'],
        'old_inputs':[HELPER,'prefix_compute/fixed_matched_family.json',
                      'inputs/rh_partial_frontier_20261122/sparse_sample_observations.json'],
    },
    'geometric_criterion': {
        'script':'certify_geometric_criterion.py',
        'certificate':'geometric_criterion_certificate.json',
        'source_inputs':['fixed_input.json'], 'old_inputs':[HELPER],
    },
    'one_sided_mellin': {
        'script':'verify_mellin_interface.py',
        'certificate':'mellin_interface_certificate.json',
        'source_inputs':['PROOF.md'], 'old_inputs':[HELPER],
        'copy_legacy_layout':True, 'sympy':True,
    },
    'geometric_green': {
        'script':'verify_geometric_green.py',
        'certificate':'geometric_green_certificate.json',
        'source_inputs':['fixed_green_cases.json'], 'old_inputs':[],
    },
}


def make_plan(name, old, output):
    spec = BRANCHES[name]
    source = ROOT/name
    destination = output/'next'/name
    required = [source/spec['script']]
    required += [source/p for p in spec['source_inputs']]
    required += [old/p for p in spec['old_inputs']]
    missing = [str(p) for p in required if not p.is_file()]
    if missing:
        raise ValueError('Missing files for '+name+':\n'+'\n'.join(missing))
    copies = []
    script = source/spec['script']
    if spec.get('copy_legacy_layout'):
        # This unmodified script resolves its helper through HERE.parents[1].
        # Reproduce that directory relation inside output, including PROOF.md.
        copies = [(source/spec['script'],destination/spec['script']),
                  (source/'PROOF.md',destination/'PROOF.md'),
                  (old/HELPER,output/'prior'/'extracted'/OLD_NAME/HELPER)]
        script = destination/spec['script']
    certificate = destination/spec['certificate']
    command = [sys.executable,'-B',str(script)]
    if name == 'geometric_compute':
        command += ['--prior',str(old),'--geometry',str(source/'fixed_geometry.json'),
                    '--output',str(certificate)]
    elif name == 'geometric_criterion':
        command += ['--prior',str(old),'--input',str(source/'fixed_input.json'),
                    '--output',str(certificate)]
    elif name == 'geometric_green':
        command += ['--output',str(certificate)]
    return {'branch':name,'directory':str(destination),'certificate':str(certificate),
            'command':command,'required_files':list(map(str,required)),
            'copies':[[str(a),str(b)] for a,b in copies]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--branch',nargs='+',choices=['all',*BRANCHES],default=['all'],
                        help='one or more branches; default: all')
    parser.add_argument('--prior',type=Path,
                        default=ROOT/'prior'/'riemann_directed_local_20261124',
                        help='complete previous 20261124 package, containing prior/'+OLD_NAME)
    parser.add_argument('--output',type=Path,required=True,
                        help='separate output directory, e.g. /tmp/riemann-next-replay')
    parser.add_argument('--check',action='store_true',
                        help='check paths and dependencies only; no calculations or files written')
    args = parser.parse_args()
    if 'all' in args.branch and args.branch != ['all']:
        parser.error('Use --branch all alone, or name selected branches.')
    names = list(BRANCHES) if args.branch == ['all'] else list(dict.fromkeys(args.branch))
    prior = args.prior.expanduser().resolve()
    old = prior/'prior'/OLD_NAME
    output = args.output.expanduser().resolve()
    if output == ROOT or ROOT in output.parents or output == prior or prior in output.parents:
        parser.error('--output must be outside the current and previous source packages.')
    versions = {'python':sys.version.split()[0]}
    if any(BRANCHES[n].get('sympy') for n in names):
        if importlib.util.find_spec('sympy') is None:
            parser.error('one_sided_mellin requires SymPy in the selected Python environment.')
        versions['sympy'] = importlib.metadata.version('sympy')
    try:
        plans = [make_plan(n,old,output) for n in names]
    except ValueError as exc:
        parser.error(str(exc))
    if args.check:
        print(json.dumps({'status':'PATHS_AND_DEPENDENCIES_CHECKED_NO_CALCULATIONS',
                          'versions':versions,'previous_package':str(prior),
                          'numerical_dependency_package':str(old),'plans':plans},indent=2))
        return

    output.mkdir(parents=True,exist_ok=True)
    report = {'status':'RUNNING','versions':versions,'source_package':str(ROOT),
              'previous_package':str(prior),'branches':[]}
    report_path = output/'replay_run.json'
    for plan in plans:
        destination = Path(plan['directory'])
        destination.mkdir(parents=True,exist_ok=True)
        for a,b in plan['copies']:
            target = Path(b)
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(a,target)
        print('Running '+plan['branch'],flush=True)
        started = time.perf_counter()
        result = subprocess.run(plan['command'],cwd=destination,capture_output=True,text=True)
        (destination/'stdout.txt').write_text(result.stdout)
        (destination/'stderr.txt').write_text(result.stderr)
        row = {'branch':plan['branch'],'command':plan['command'],
               'exit_code':result.returncode,'seconds':time.perf_counter()-started,
               'certificate':plan['certificate'],
               'certificate_present':Path(plan['certificate']).is_file()}
        report['branches'].append(row)
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip(),file=sys.stderr)
        if result.returncode or not row['certificate_present']:
            report['status'] = 'FAILED'
            report_path.write_text(json.dumps(report,indent=2)+'\n')
            raise SystemExit(result.returncode or 1)
    report['status'] = 'ALL_SELECTED_BRANCHES_COMPLETED'
    report_path.write_text(json.dumps(report,indent=2)+'\n')
    print('Saved replay outputs to '+str(output))


if __name__ == '__main__':
    main()
