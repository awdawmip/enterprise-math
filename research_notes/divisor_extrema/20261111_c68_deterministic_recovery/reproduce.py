"""Recompute C68 certificates in a temporary directory and compare their bytes."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parent

def jobs(model, prior):
    native = str(model / 'inherited')
    checks = str(model / 'checks')
    joint = str(prior / 'joint')
    return [
        ('decoder/region', 'decoder/verify_region', ['--last-c', '28', '--jobs', '2', '--output', '{output}']),
        ('decoder/native_check', 'decoder/native_check', ['--prior', joint]),
        ('decoder/disconnected', 'decoder/disconnected', []),
        ('decoder/extended/region_29_32', 'decoder/extended/extend_region', ['--first', '29', '--last', '32']),
        ('decoder/extended/region_33_34', 'decoder/extended/extend_region', ['--first', '33', '--last', '34']),
        ('decoder/extended/clip_controls', 'decoder/extended/check_clip', ['--last', '34']),
        ('density/density', 'density/density_certificate', []),
        ('twoblocks/stock_shift', 'twoblocks/stock_shift', ['--native', native, '--c67-joint', joint]),
        ('twoblocks/two_block_census', 'twoblocks/two_block_census', []),
        ('arithmetic/moving_gap', 'arithmetic/moving_gap', ['--c64', checks]),
        ('arithmetic/macroscopic', 'arithmetic/macroscopic', ['--c64', checks, '--c67', joint, '--native-root', native]),
        ('surplus/native_columns', 'surplus/native_columns', ['--native-root', native]),
        ('surplus/all_stocks_budget5', 'surplus/terminal_words', ['--budget', '5']),
        ('surplus/census_3_4', 'surplus/terminal_words', ['--r', '3', '--total', '4']),
        ('surplus/census_4_3', 'surplus/terminal_words', ['--r', '4', '--total', '3']),
        ('surplus/census_5_2', 'surplus/terminal_words', ['--r', '5', '--total', '2']),
        ('surplus/precision', 'surplus/precision', []),
        ('surplus/scalar_budget5', 'surplus/scalar_words', ['--budget', '5']),
        ('inverse/incidence', 'inverse/incidence_inverse', ['--checks', checks, '--inherited', native, '--prior', str(prior/'inverse'), '--output', '{output}']),
        ('conditioning/first_order', 'conditioning/first_order', ['--budget', '24']),
    ]

def check(entry):
    output, script, arguments = entry
    reference = ROOT / (output + '.json')
    with TemporaryDirectory() as directory:
        destination = Path(directory) / 'result.json'
        args = [str(destination) if x == '{output}' else x for x in arguments]
        cmd = [sys.executable, str(ROOT / (script + '.py')), *args]
        if '{output}' in arguments:
            subprocess.run(cmd, check=True)
            actual = destination.read_bytes()
        else:
            actual = subprocess.check_output(cmd)
        if actual != reference.read_bytes():
            raise ValueError(f'certificate differs: {reference}')
    print('OK', output, flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', type=Path, default=ROOT.parent/'C64')
    parser.add_argument('--prior', type=Path, default=ROOT.parent/'C67')
    parser.add_argument('--group', help='Only run this directory, e.g. density, surplus, decoder/extended.')
    parser.add_argument('--jobs', type=int, default=1)
    args = parser.parse_args()
    entries = jobs(args.model.resolve(), args.prior.resolve())
    expected = {str((ROOT / (item[0]+'.json')).relative_to(ROOT)) for item in entries}
    actual = {str(path.relative_to(ROOT)) for path in ROOT.rglob('*.json')}
    if expected != actual:
        raise ValueError(f'certificate list mismatch: {expected ^ actual}')
    selected = [i for i in entries if args.group is None or i[0].startswith(args.group+'/')]
    if not selected:
        parser.error('group contains no certificate')
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        list(pool.map(check, selected))
