"""Run exact certificates and declared finite-data checks for C82.

Default: re-evaluate only c = 4, 16; inspect the completed five-stock file.
Optional: --full repeats all five finite enumerations, including c = 1024.
This program checks certificates and finite computations, not analytic theorems.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import comb, isqrt
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
STOCKS = [4, 16, 64, 256, 1024]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true',
                        help='also recompute c = 64, 256, 1024 (not the default)')
    parser.add_argument('--output', type=Path, default=ROOT / 'checks.json')
    args = parser.parse_args()
    require(sys.flags.optimize == 0, 'Run without -O: certificate assertions must be enabled.')
    started = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()
    import numpy as np
    import sympy as sp
    checks = []
    report = {
        'description': 'C82 exact certificates, symbolic checks, and finite-data consistency checks',
        'scope_note': ('These checks cover the named identities, rational certificates, and finite records. '
                       'They do not constitute program verification of the analytic limit theorems.'),
        'started_utc': started,
        'environment': {
            'python': sys.version,
            'executable': sys.executable,
            'platform': platform.platform(),
            'numpy': np.__version__,
            'sympy': sp.__version__,
            'python_optimization': sys.flags.optimize,
        },
        'execution_scope': {
            'mode': 'full' if args.full else 'default',
            'stored_inventory_checked': STOCKS,
            'finite_enumerations_recomputed': STOCKS if args.full else [4, 16],
            'stored_only_enumerations': [] if args.full else [64, 256, 1024],
            'full_recalculation_command': 'python verify.py --full',
        },
        'checks': checks,
    }

    def save():
        report['elapsed_seconds'] = round(time.perf_counter() - start, 6)
        report['passed'] = sum(c['status'] == 'passed' for c in checks)
        report['failed'] = sum(c['status'] == 'failed' for c in checks)
        report['status'] = 'passed' if report['failed'] == 0 else 'failed'
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')

    def record(name, function):
        begin = time.perf_counter()
        entry = {'name': name}
        try:
            detail = function()
            entry.update(status='passed', details=detail)
        except Exception as exc:
            entry.update(status='failed', error=f'{type(exc).__name__}: {exc}')
        entry['elapsed_seconds'] = round(time.perf_counter() - begin, 6)
        checks.append(entry)
        save()
        print(f"{entry['status'].upper()}: {name}", flush=True)
        return entry['status'] == 'passed'

    def run_script(relative):
        script = ROOT / relative
        env = os.environ.copy()
        env.pop('PYTHONOPTIMIZE', None)
        completed = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                                   capture_output=True, text=True, env=env, timeout=600)
        require(completed.returncode == 0,
                f'{relative}: exit {completed.returncode}; stderr={completed.stderr}; stdout={completed.stdout}')
        return {'program': relative, 'returncode': completed.returncode,
                'stdout': completed.stdout.strip(), 'stderr': completed.stderr.strip(),
                'sha256': sha256(script)}

    certificate_path = ROOT / 'fibers/fiber_certificates.json'
    old_certificates = json.loads(certificate_path.read_text())
    old_certificate_hash = sha256(certificate_path)
    jobs = [
        ('exact_lattice_tail_constants', 'check_lattice_tail.py'),
        ('symbolic_jacobian_and_boundary_identities', 'fibers/check_jacobian.py'),
        ('rational_fiber_certificate_program', 'fibers/certify_fibers.py'),
    ]
    with ThreadPoolExecutor(max_workers=3) as pool:
        pending = [(name, pool.submit(run_script, script)) for name, script in jobs]
        for name, future in pending:
            record(name, future.result)

    def certificate_roundtrip():
        current = json.loads(certificate_path.read_text())
        require(current == old_certificates, 'Regenerated rational certificate differs from the stored JSON.')
        require(sha256(certificate_path) == old_certificate_hash,
                'Regenerated certificate serialization differs from the stored bytes.')
        return {'json_equal': True, 'byte_equal': True, 'sha256': old_certificate_hash,
                'regular_count_example_labels': [x['count'] for x in current['regular_count_examples']],
                'scope': 'Reproduced exact inequalities and interval certificates; root-count conclusions also use the analytic proof.'}
    record('rational_certificate_reproduction', certificate_roundtrip)

    finite_path = ROOT / 'finite/three_readings.json'
    before_finite_hash = sha256(finite_path)
    records = json.loads(finite_path.read_text())
    by_stock = {r['c']: r for r in records}

    def inventory():
        require([r['c'] for r in records] == STOCKS, 'Unexpected or duplicate stock inventory.')
        return {'stocks': STOCKS, 'sha256': before_finite_hash, 'records': len(records)}
    record('five_stock_inventory', inventory)

    def catalogue_counts():
        values = []
        for r in records:
            expected = comb(r['c'], 2)
            require(type(r['n']) is int and r['n'] == expected, f"Wrong catalogue count at c={r['c']}")
            values.append({'c': r['c'], 'arrangements': expected})
        return {'counts': values, 'total_arrangements': sum(x['arrangements'] for x in values)}
    record('binomial_catalogue_sizes', catalogue_counts)

    def critical_scale():
        details = []
        for r in records:
            c, b, p = r['c'], r['b'], r['p']
            require(isqrt(c) == b and b*b == c, f'Wrong b at c={c}')
            require(c & (c-1) == 0 and b & (b-1) == 0, 'Expected powers of two.')
            logc, logb = c.bit_length()-1, b.bit_length()-1
            pstar = Fraction(7, 4)*logc + Fraction(1, 2)*(logc-logb)
            require(pstar == 2*logc == p, f'Wrong exact p* at c={c}')
            require(r['L'] == 1, f'Wrong stored L at c={c}')
            require(r['interval_bits'] == 176, f'Unexpected interval precision at c={c}')
            details.append({'c': c, 'b': b, 'p_star': str(pstar), 'p': p, 'L': 1})
        return {'formula': 'p* = 7/4 log2(c) + 1/2 log2(c/b) = 2 log2(c)',
                'exact_rational_log_check': details, 'interval_bits': 176}
    record('critical_scale_L_one', critical_scale)

    expected_origins = list(product(range(2), repeat=3))
    def origin_coverage():
        for r in records:
            actual = [tuple(x['offsets_halves']) for x in r['origins']]
            require(actual == expected_origins, f"Wrong eight-origin coverage at c={r['c']}")
        return {'origins_per_stock': 8, 'total_origin_records': 8*len(records),
                'offsets_halves': [list(x) for x in expected_origins]}
    record('eight_origin_coverage', origin_coverage)

    def singleton_order():
        summaries = []
        for r in records:
            for o in r['origins']:
                for key in ('pair_0_1', 'pair_0_2', 'triple'):
                    require(type(o[key]) is int and 0 <= o[key] <= r['n'],
                            f"Invalid {key} count at c={r['c']}")
                require(o['triple'] >= o['pair_0_1'] and o['triple'] >= o['pair_0_2'],
                        f"Adding the third reading decreased unique count at c={r['c']}")
            summaries.append({'c': r['c'], **{
                key: [min(o[key] for o in r['origins']), max(o[key] for o in r['origins'])]
                for key in ('pair_0_1', 'pair_0_2', 'triple')}})
        return {'records_checked': 40, 'pairwise_inequalities_checked': 80,
                'singleton_count_ranges': summaries}
    record('triple_dominates_both_pairs', singleton_order)

    def pair_origin_independence():
        for r in records:
            for key, coordinates in [('pair_0_1', (0, 1)), ('pair_0_2', (0, 2))]:
                groups = {}
                for o in r['origins']:
                    pair = tuple(o['offsets_halves'][i] for i in coordinates)
                    require(pair not in groups or groups[pair] == o[key],
                            f"Unused origin affected {key} at c={r['c']}")
                    groups[pair] = o[key]
        return {'stocks_checked': len(records), 'pair_groups_checked': len(records)*8}
    record('unused_origin_does_not_change_pair_count', pair_origin_independence)

    sys.path.insert(0, str(ROOT / 'finite'))
    import three_readings
    original_native = three_readings.native_tail_ratios
    native_inputs = []
    def tracked_native(c, v, w):
        values = original_native(c, v, w)
        require(len(values) == 3 and all(isinstance(x, Fraction) for x in values),
                'Native reading must return three exact rational tail ratios.')
        native_inputs.append((c, v, w))
        return values
    three_readings.native_tail_ratios = tracked_native
    recalculated = {}
    for c in report['execution_scope']['finite_enumerations_recomputed']:
        def recompute(c=c):
            result = three_readings.calculate(c)
            recalculated[c] = result
            require(result == by_stock[c], f'Recomputed finite record differs at c={c}')
            return {'c': c, 'arrangements': result['n'], 'origins': len(result['origins']),
                    'native_enclosures': result['native_enclosures'], 'exact_json_record_equal': True}
        record(f'finite_recalculation_c_{c}', recompute)
    three_readings.native_tail_ratios = original_native

    def native_enclosures():
        expected = [(n, v, w) for c in (4, 16)
                    for v in range(2, c+1) for w in range(2, v+1)
                    for n in (c, c+isqrt(c), c+2*isqrt(c))]
        require(len(native_inputs) == 378, f'Expected 378 native calls, got {len(native_inputs)}')
        require(sorted(native_inputs) == sorted(expected), 'Native call coverage differs from the declared scope.')
        require(sum(recalculated[c]['native_enclosures'] for c in (4, 16)) == 378,
                'Enclosure counters disagree with executed native calls.')
        require(sum(r['native_enclosures'] for r in records) == 378,
                'Stored native-enclosure count differs.')
        return {'exact_native_calls': 378, 'c_4': 18, 'c_16': 360,
                'all_calls_returned_Fraction_values': True,
                'all_378_interval_enclosure_assertions_executed': True,
                'arrangements_recomputed_for_native_check': 126,
                'scope': 'All three physical readings for every arrangement at c=4 and c=16.'}
    record('all_378_native_rational_enclosures', native_enclosures)

    def finite_file_unchanged():
        require(sha256(finite_path) == before_finite_hash, 'Stored finite enumeration file was changed.')
        return {'sha256': before_finite_hash, 'stored_file_changed': False,
                'large_inventory_recomputed': args.full}
    record('stored_finite_file_preserved', finite_file_unchanged)
    report['finished_utc'] = datetime.now(timezone.utc).isoformat()
    report['input_program_sha256'] = {
        str(p.relative_to(ROOT)): sha256(p) for p in [
            ROOT / 'verify.py', ROOT / 'finite/three_readings.py',
            ROOT / 'finite/critical_bins.py', ROOT / 'finite/native.py']}
    save()
    print(f"{report['passed']} passed; {report['failed']} failed; mode={report['execution_scope']['mode']}", flush=True)
    return int(report['failed'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
