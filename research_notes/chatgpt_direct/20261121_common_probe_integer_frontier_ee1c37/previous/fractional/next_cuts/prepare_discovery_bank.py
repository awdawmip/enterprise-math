"""Rebuild the complete discovery bank from the shipped native enumerator.

This is a candidate-generation command, not an LP or exact-cover search.
An existing complete native census can be reused with --seeds.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import sys
from collections import Counter

from discovery_common import DELIVERY_ROOT, EXPECTED_TYPES, native_module


def prepare(work, delivery_root, compiler, seed_file=None):
    if sys.byteorder != 'little':
        raise RuntimeError('The supplied native binary writer requires a little-endian host.')
    work = work.resolve()
    delivery_root = delivery_root.resolve()
    reused_seeds = seed_file is not None
    work.mkdir(parents=True, exist_ok=True)
    native = native_module(delivery_root)
    census_source = delivery_root.joinpath(
        *(['previous'] * 5), 'low', 'class_enumeration.cpp')
    expand_source = delivery_root / 'lower/genprof.cpp'
    for source in (census_source, expand_source):
        if not source.is_file():
            raise FileNotFoundError(source)
    if seed_file is None:
        census = work / 'census'
        subprocess.run([compiler, '-std=c++20', '-O3', '-mpopcnt',
                        str(census_source), '-o', str(census)], check=True)
        observations = work / 'observations.bin'
        native.observation_file(observations)
        seed_file = work / 'seeds'
        print('Enumerating the complete native class census.', flush=True)
        with (work / 'census.log').open('w') as log:
            subprocess.run([str(census), str(observations), str(seed_file)],
                           stdout=log, check=True)
    else:
        seed_file = seed_file.resolve()
        if not seed_file.is_file():
            raise FileNotFoundError(seed_file)
    needed = work / 'needed'
    with seed_file.open() as source, needed.open('w') as out:
        for line in source:
            if tuple(map(int, line.split(' ', 2)[:2])) in EXPECTED_TYPES:
                out.write(line)
    caps = {size: max(cost for s, cost in EXPECTED_TYPES if s == size)
            for size, _ in EXPECTED_TYPES}
    (work / 'caps').write_text(' '.join(str(caps.get(s, 0)) for s in range(14)) + '\n')
    (work / 'linear').write_text(''.join(
        ' '.join(map(str, row)) + '\n' for row in native.symmetries()[0]))
    expand = work / 'genprof'
    subprocess.run([compiler, '-std=c++20', '-O3', '-mpopcnt',
                    str(expand_source), '-o', str(expand)], check=True)
    temporary_bank = work / 'bank.partial'
    receipt = subprocess.check_output(
        [str(expand), str(work / 'linear'), str(needed),
         str(work / 'caps'), str(temporary_bank)], text=True)
    (work / 'bank.log').write_text(receipt)
    rows = list(struct.iter_unpack('<QQII', temporary_bank.read_bytes()))
    counts = Counter((tag % 256, cost) for _, _, cost, tag in rows)
    assert dict(counts) == EXPECTED_TYPES, dict(counts)
    assert len({lo + (hi << 64) for lo, hi, _, _ in rows}) == len(rows)
    bank = work / 'bank'
    temporary_bank.replace(bank)
    manifest = {
        'complete_types': [{'size': s, 'cost': c, 'count': counts[s, c]}
                           for s, c in sorted(counts)],
        'rows': len(rows),
        'bank_sha256': hashlib.sha256(bank.read_bytes()).hexdigest(),
        'census_source_sha256': hashlib.sha256(census_source.read_bytes()).hexdigest(),
        'expansion_source_sha256': hashlib.sha256(expand_source.read_bytes()).hexdigest(),
        'used_existing_seed_file': reused_seeds,
    }
    (work / 'discovery_bank_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'bank': str(bank), **manifest}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True,
                        help='directory for the rebuilt bank and native census intermediates')
    parser.add_argument('--delivery-root', type=Path, default=DELIVERY_ROOT)
    parser.add_argument('--cxx', default='c++', help='C++ compiler executable')
    parser.add_argument('--seeds', type=Path,
                        help='reuse a complete native low/class_enumeration.cpp census')
    args = parser.parse_args()
    prepare(args.work, args.delivery_root, args.cxx, args.seeds)
