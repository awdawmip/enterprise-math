"""Recompute C69 certificates with the supplied C67 and C68 source directories."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys


def commands(folder, prior, model, workers):
    for path in sorted(folder.glob('*/*.json')):
        section, name = path.parent.name, path.stem
        aliases = {
            ('arithmetic', 'controls'): 'verify_density',
            ('cert', 'native'): 'native_control',
            ('depthtwo', 'density_one'): 'verify_density_one',
        }
        script = aliases.get((section, name), name)
        switches = []
        if section == 'cert' and name.startswith('column_'):
            data = json.loads(path.read_text())
            lo, hi = data['stock_interval']
            script = 'column_certificate'
            switches = ['--first', lo, '--last', hi, '--depth', data['depth'],
                        '--model', model / 'decoder', '--jobs', workers]
        elif (section, name) in {('arithmetic', 'controls'), ('cert', 'native'), ('depthtwo', 'density_one'), ('singleh', 'singleh_rank')}:
            switches = ['--prior', prior / 'joint']
        elif section == 'cert' and name in {'three_stocks', 'unbounded'}:
            switches = ['--prior', model / 'twoblocks']
        yield path, [sys.executable, str(path.with_name(script + '.py')), *map(str, switches)]


def main():
    root = Path(__file__).resolve().parent
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--prior', type=Path, default=root.parent / 'C67')
    cli.add_argument('--model', type=Path, default=root.parent / 'C68')
    cli.add_argument('--group', default='', help='Match the relative certificate path prefix')
    cli.add_argument('--jobs', type=int, default=3, help='Concurrent sharded cases per large certificate')
    cli.add_argument('--parallel', type=int, default=1, help='Certificates run in parallel')
    options = cli.parse_args()
    selected = [(p, cmd) for p, cmd in commands(root, options.prior.resolve(), options.model.resolve(), options.jobs)
                if str(p.relative_to(root)).startswith(options.group)]
    if not selected:
        cli.error('no certificates match the requested group')
    def check(item):
        path, command = item
        value = subprocess.run(command, check=True, stdout=subprocess.PIPE).stdout
        if value != path.read_bytes():
            raise ValueError('certificate differs: ' + str(path))
        print('OK', path.relative_to(root), flush=True)
    with ThreadPoolExecutor(max_workers=options.parallel) as pool:
        list(pool.map(check, selected))

if __name__ == '__main__':
    main()
