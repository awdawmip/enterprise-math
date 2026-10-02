#!/usr/bin/env python3
"""Restore one original gzip from transport fragments and verify exact bytes."""
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
EXPECTED="62a36e1d888e62acd90ceaac34d9563a234a45b9139559fe4f9533818790d9e4"


def main():
    target=HERE/'transfer_series.csv.gz'
    if target.exists():
        data=target.read_bytes()
    else:
        data=b''.join((HERE/f'transfer_series.csv.gz.part{i:02d}').read_bytes() for i in (1,2))
    if len(data)!=12661305 or hashlib.sha256(data).hexdigest()!=EXPECTED:
        raise ValueError('Original data hash mismatch; do not use or overwrite unverified data')
    if not target.exists():
        temporary=HERE/'transfer_series.csv.gz.restoring'
        temporary.write_bytes(data)
        temporary.replace(target)
    print('PASS: original gzip reconstructed/verified; 172074 recorded rows')


if __name__=='__main__':
    main()
