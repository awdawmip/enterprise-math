"""Bounded, non-blind review of the exact frozen PFSSV implementation.

No call to its main(), no registered holdout, no 50.5-million sieve.
Outputs are diagnostics, not a replacement experiment or formal review.
"""
from pathlib import Path
import hashlib
import importlib.util
import io
import json
import math
import subprocess
import tarfile
import time

import numpy as np

ROOT = Path('D:/em/integration-pfssv-resume-20260908')
OUT = Path(__file__).parent
SOURCE = '1cac434cb9ac542a38a8e7bb6defa414fefb2e4d'
CHECKER = 'scripts/check_prime_factor_semiprime_shell_residual_validation.py'
ARTIFACT = 'research_artifacts/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION/'
TASK = 'RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION'
OWNED_SOURCE_PATHS = [
    ARTIFACT + 'discovery_freeze.json',
    ARTIFACT + 'experiment_manifest.json',
    ARTIFACT + 'result_summary.json',
    'research_execution_records/' + TASK + '/ER-7C6EAD0D84D3B0C96A12.json',
    'research_result_records/' + TASK + '/RR-3287C6124F8D8A1F0901.json',
    'research_returns/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_RETURN_20260827.md',
    CHECKER,
]
TASKBOOK = 'research_tasks/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_20260827.md'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def trial_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % d for d in range(3, math.isqrt(n) + 1, 2))


started = time.perf_counter()
before = {path: ROOT.joinpath(path).read_bytes() for path in OWNED_SOURCE_PATHS}
assert sha(before[CHECKER]) == '8772484435d77abf74e87a6f053a0edaf4fa9395bdbade93ede2413083f22140'
archive = subprocess.check_output(['git', 'archive', SOURCE, *OWNED_SOURCE_PATHS], cwd=ROOT)
with tarfile.open(fileobj=io.BytesIO(archive)) as package:
    original = {entry.name: package.extractfile(entry).read() for entry in package.getmembers() if entry.isfile()}
assert original == before
spec = importlib.util.spec_from_file_location('pfssv_frozen_checker_for_independent_review', ROOT.joinpath(CHECKER))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

# Independently obtained exact prime table, sufficiently long for both tiny cells.
limit = 50_500
primes = np.array([n for n in range(2, limit + 1) if trial_prime(n)], dtype=np.int64)
assert np.array_equal(checker.sieve_primes(limit), primes)
by_res = {r: primes[primes % 30 == r] for r in checker.RES30}
summary = json.loads(before[ARTIFACT + 'result_summary.json'])
cells = []
rank_maps = []
for num, den in [(1, 100), (1, 1000)]:
    X = 100_000
    cell = checker.shell_cell(primes, by_res, X, num, den, 512, checker.SEED_A + X)
    upper = X * (den + num) // den
    # Full pair list by an independent direct product comparison on trial primes.
    pairs = [(int(p), int(q)) for p in primes if int(p) ** 2 <= upper
             for q in primes if q >= p and X < int(p) * int(q) <= upper]
    assert len(pairs) == cell['pairs_raw']
    assert sum(p > 31 for p, q in pairs) == cell['pairs_p_gt_31']
    assert sum(p ** 4 > X for p, q in pairs) == cell['pairs_p4_gt_X']
    historical = next(row for row in summary['cells'] if row['X'] == X and row['eta'] == f'{num}/{den}')
    assert all(historical[key] == cell[key] for key in ['pairs_raw', 'pairs_p_gt_31', 'pairs_p4_gt_X', 'diagonal_pairs'])

    positions = []
    for p0 in primes:
        p = int(p0)
        if p * p > upper:
            break
        if p ** 4 <= X:
            continue
        lo, hi = max(p, X // p + 1), upper // p
        if lo > hi:
            continue  # Empty integer windows are a deterministic geometry filter.
        count = sum(trial_prime(q) for q in range(lo, hi + 1))
        u = math.log(p) / math.log(X)
        z = math.log(3 * u / (1 - u)) / math.log(3)
        band = min(7, max(0, math.floor((u - 0.25) / 0.25 * 8)))
        zbin = min(23, max(0, math.floor(z * 24)))
        expected = (hi - lo + 1) / math.log(math.sqrt(lo * hi))
        positions.append({'p': p, 'qlo': lo, 'qhi': hi, 'count': count,
                          'band': band, 'p_mod_30': p % 30, 'zbin': zbin,
                          'smooth_expected': expected})
    excluded = [row for row in positions if row['count'] == 0]
    assert excluded and all(row['smooth_expected'] > 0 for row in excluded)
    assert set(map(int, cell['p'])) == {row['p'] for row in positions if row['count'] > 0}
    groups = {}
    for row in positions:
        groups.setdefault((row['band'], row['p_mod_30']), []).append(row)
    mixed = [rows for rows in groups.values() if any(r['count'] == 0 for r in rows)
             and any(r['count'] > 0 for r in rows)
             and len({r['zbin'] for r in rows}) > 1]
    lost_expected = sum(row['smooth_expected'] for row in excluded)
    total_expected = sum(row['smooth_expected'] for row in positions)
    source_expected = checker.smooth_profile(cell)
    assert np.isclose(source_expected.sum(), total_expected - lost_expected)

    actual_rank = np.searchsorted(primes, cell['p'], side='right')
    code_rank = np.arange(len(cell['p']), dtype=float) / max(len(cell['p']) - 1, 1)
    normalized_true_rank = (actual_rank - actual_rank[0]) / max(int(actual_rank[-1] - actual_rank[0]), 1)
    true_rank_hist = checker.hist01(normalized_true_rank, cell['c'])
    assert not np.array_equal(code_rank, normalized_true_rank)
    assert not np.array_equal(cell['profiles']['prime_rank'], true_rank_hist)
    rank_map = {int(p): {'pi_p': int(pr), 'survivor_rank': float(r)}
                for p, pr, r in zip(cell['p'], actual_rank, code_rank, strict=True)}
    rank_maps.append(rank_map)

    row = checker.serial_row(cell, 'independent_nonblind_small_review', 10)
    assert 'profiles' not in row and 'zobs' not in row and 'znull' not in row
    assert set(cell['profiles']) == {'raw', 'small_trim', 'scale_trim', 'prime_rank', 'density_flat'}
    assert all(len(profile) == 24 for profile in cell['profiles'].values())
    cells.append({
        'X': X, 'width': f'{num}/{den}', 'upper': upper,
        'independent_direct_pair_count': len(pairs),
        'historical_integer_cell_counts_match': True,
        'eligible_nonempty_integer_windows': len(positions),
        'retained_observed_nonzero_windows': len(cell['p']),
        'deleted_zero_prime_windows': len(excluded),
        'deleted_positive_smooth_expected_mass': lost_expected,
        'smooth_mass_over_all_geometry_eligible_positions': total_expected,
        'smooth_mass_on_retained_positions': float(source_expected.sum()),
        'mixed_positive_zero_stratum_example': mixed[0] if mixed else None,
        'deleted_zero_examples': excluded[:4],
        'source_survivor_rank_is_not_normalized_true_pi_p': True,
        'source_rank_profile_differs_from_true_pi_p_profile': True,
        'global_pi_p': actual_rank.tolist(),
        'source_rank': code_rank.tolist(),
        'source_serial_keys': sorted(row),
        'omitted_profile_names': sorted(cell['profiles']),
        'omitted_profile_value_count': 120,
        'omitted_full_residual_profile_length': len(cell['zobs']),
    })

common = sorted(set(rank_maps[0]) & set(rank_maps[1]))
rank_width_changes = [{'p': p, 'wide': rank_maps[0][p], 'narrow': rank_maps[1][p]}
                      for p in common if rank_maps[0][p]['survivor_rank'] != rank_maps[1][p]['survivor_rank']]
assert rank_width_changes
assert any(cell['mixed_positive_zero_stratum_example'] is not None for cell in cells)

# The seven MR bases are adequate for these tiny inputs, but not a general
# deterministic 64-bit primality contract. This composite is a direct counterexample.
composite = 10_670_053 * 32_010_157
assert composite == 341_550_071_728_321
assert checker.is_prime_mr(composite) is True

assert all(ROOT.joinpath(path).read_bytes() == data for path, data in before.items())
result = {
    'status': 'PASS_BOUNDED_NONBLIND_REVIEW_PROBES_CONFIRMED_DESIGN_AND_OUTPUT_GAPS',
    'source_commit': SOURCE,
    'worktree_base': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
    'source_sha256': {path: sha(data) for path, data in before.items()},
    'all_seven_original_source_bytes_match_before_after': True,
    'taskbook': {'path': TASKBOOK, 'sha256': sha(ROOT.joinpath(TASKBOOK).read_bytes())},
    'numpy_version': np.__version__,
    'prime_table': {'algorithm': 'independent exact trial division; compared to original sieve', 'limit': limit, 'count': len(primes)},
    'cells': cells,
    'same_p_same_scale_rank_changes_with_width_examples': rank_width_changes[:5],
    'mr_64_bit_label_counterexample': {'n': composite, 'factors': [10_670_053, 32_010_157], 'original_is_prime_mr': True, 'scope': 'Does not invalidate the much smaller frozen q-range; refutes only the generic 64-bit description.'},
    'elapsed_seconds': time.perf_counter() - started,
    'execution_boundary': 'Two already-public discovery cells at X=100000, widths 1/100 and 1/1000, with original shell_cell and serial_row. No main(), no holdout, no original full run. No native certification or new blind test claimed. Only TEMP output written.',
}
output = OUT.joinpath('small_boundary_receipt.json')
output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode())
print(json.dumps({'status': result['status'], 'path': str(output), 'sha256': sha(output.read_bytes()),
                  'elapsed_seconds': result['elapsed_seconds'], 'cells': [{k: cell[k] for k in ['width', 'independent_direct_pair_count', 'eligible_nonempty_integer_windows', 'retained_observed_nonzero_windows', 'deleted_zero_prime_windows', 'deleted_positive_smooth_expected_mass']} for cell in cells]}, ensure_ascii=False))
