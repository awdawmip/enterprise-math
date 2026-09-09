"""Bounded Driver regression of the recovered, immutable scanner bytes.

The complete catalogue below is synthetic and small; it is not q=78553 data.
It joins catalogue loading, true attestation, coverage, row verification and
the actual scan using the existing scanner without changing its source.
"""
from __future__ import annotations

from bisect import bisect_left, bisect_right
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'experiments'))
import r005a_p2_gap_shadow_inversion as scanner
import r005a_p2_gap_shadow_inversion_regression as regression


def main() -> None:
    q = 47
    Q = q * q
    lo, hi = 15000, 20000
    n0, n1 = lo * lo // Q, hi * hi // Q
    primes = regression.sieve(n1 + 200)
    # The 100-floor margin contains the shadow left edge for this small case.
    G = max(b-a for a, b in zip(primes, primes[1:]) if n0-100 <= a <= n1)
    dmax = max(G-scanner.floor_width(k, Q) for k in range(lo, hi+1))
    assert dmax < 100
    threshold = scanner.required_even_gap_min(G-dmax+1, n0)
    seam = scanner.Seam(q=q, q_square=Q, gap_bound=G, h=G//2,
        k_global_fail=lo, k_q2_width=hi+1, k_last=hi, s_max=0,
        d_max_bound=dmax, floor_start=n0, floor_end=n1,
        required_gap_start_min=n0-dmax+1, required_gap_start_max=n1,
        required_complete_gap_ge=threshold, one_unit_whole_seam=False)
    rows = regression.all_gap_rows(primes, seam.required_gap_start_min, n1, threshold)
    assert rows
    metadata = regression.catalog_fixture(seam)
    metadata['source_id'] = 'DRIVER_SYNTHETIC_SMALL_COMPLETE_CATALOG_NOT_Q78553'
    metadata['rows'] = [asdict(row) for row in rows]
    metadata['rows_sha256'] = scanner.canonical_rows_sha256(rows)
    calls = []
    with tempfile.TemporaryDirectory(prefix='r005-driver-attested-') as directory:
        catalog = Path(directory) / 'synthetic_catalog.json'
        catalog.write_text(json.dumps(metadata), encoding='utf-8')
        loaded_metadata, loaded_rows = scanner.load_catalog(catalog)
        calls.append('load_catalog')
        assert loaded_metadata['completeness_attestation'] is True
        scanner.validate_catalog_for_seam(loaded_metadata, loaded_rows, seam, verify_rows=True)
        calls.append('validate_catalog_for_seam:coverage+max_bound+consecutive_rows')
        hits = scanner.scan_gap_shadows(seam, loaded_rows)
        calls.append('scan_gap_shadows')
    expected = set()
    for k in range(lo, hi+1):
        start = k*k//Q
        end = (k*k+2*k)//Q
        if bisect_left(primes, start+1) == bisect_right(primes, end):
            expected.add(k)
    assert {row['k'] for row in hits} == expected
    assert hits
    rejections = {}
    for field, value, message in (
        ('coverage_end', seam.required_gap_start_max-1, 'catalog coverage does not contain required gap-start band'),
        ('max_gap_bound_end', seam.required_gap_start_max-1, 'max-gap bound does not cover the required gap-start band'),
        ('completeness_attestation', False, 'completeness_attestation must be true'),
    ):
        changed = dict(metadata)
        changed[field] = value
        try:
            scanner.validate_catalog_for_seam(changed, rows, seam, verify_rows=True)
        except scanner.CatalogError as exc:
            assert message in str(exc)
            rejections[field] = str(exc)
        else:
            raise AssertionError(f'{field} did not fail closed')
    data = (ROOT / 'experiments/r005a_p2_gap_shadow_inversion.py').read_bytes()
    print(json.dumps({'schema': 'R005_DRIVER_ATTESTED_SCAN_PATH_REVIEW_V1',
        'reviewer_id': 'EM-DVR-81273A', 'status': 'PASS',
        'source_sha256': hashlib.sha256(data).hexdigest(),
        'actual_call_path': calls, 'completeness_attestation': True,
        'catalog_scope': 'SYNTHETIC_SMALL_FINITE_CASE_ONLY',
        'catalog_rows': len(rows), 'exact_scan_failures': len(hits),
        'brute_force_failures': len(expected), 'negative_controls': rejections,
        'q78553_catalog_supplied': False, 'q78553_frontier_extended': False}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
