#!/usr/bin/env python3
"""Call exact frozen signed_brc source, from an EM checkout or local evidence pack."""
import hashlib
import importlib.util
from math import comb
from pathlib import Path

THIS = Path(__file__).resolve()
CANDIDATES = (
    THIS.parents[2] / 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py',
    THIS.with_name('pinned_signed_brc.py'),
)
SRC = next((p for p in CANDIDATES if p.is_file()), None)
if SRC is None:
    raise FileNotFoundError('frozen signed_brc.py missing: use EM checkout or evidence pack')
raw = SRC.read_bytes()
actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
expected = '300a96e3dc24bf6fff73743037a0347a8bc83176'
assert actual == expected, (actual, expected)
spec = importlib.util.spec_from_file_location('pinned_signed_brc', SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
checks = 0
for q in range(1, 5):
    for n in (3*q, 4*q, 4*q+1):
        for k in (0, q, 2*q, 3*q, 4*q):
            if k > n:
                continue
            endpoint = (n-2*k, 0, 0, 0, 0, 0)
            count = m.endpoint_multiplicity(n, endpoint)
            assert count >= comb(n, k) and count > 0, (q,n,k,count)
            checks += 1
print('PASS original frozen signed_brc.endpoint_multiplicity')
print('source_git_blob='+actual)
print('capacity_checks=', checks)
