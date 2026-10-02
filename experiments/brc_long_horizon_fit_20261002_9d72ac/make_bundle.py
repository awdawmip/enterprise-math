#!/usr/bin/env python3
"""Build deterministic checksummed research backup; no credentials or git internals."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EXCLUDE = {'manifest.json', 'storage_receipt.json', 'publication.json'}


def digest(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'md5': hashlib.md5(data).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}


def files():
    return sorted(p for p in HERE.iterdir()
                  if p.is_file() and p.name not in EXCLUDE)


def write_manifest():
    manifest = {'schema': 'BRC_FIT_ARTIFACT_MANIFEST_V1',
                'date_timezone': '2026-10-02 Asia/Shanghai',
                'scope': 'Experiment files only; manifest and subsequent storage/publication receipts excluded to avoid circular hashes.',
                'files': {p.name: digest(p) for p in files()}}
    (HERE/'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True)+'\n')
    return manifest


def verify():
    manifest = json.loads((HERE/'manifest.json').read_text())
    for name, expected in manifest['files'].items():
        assert digest(HERE/name) == expected, name
    assert set(manifest['files']) == {p.name for p in files()}, 'manifest inventory differs'
    return len(manifest['files'])


def bundle(destination, part_limit=90000000):
    write_manifest()
    selected = files()+[HERE/'manifest.json']
    prior = ROOT/'experiments/brc_expanded_types_20261002_fca717'
    selected += sorted(p for p in prior.iterdir() if p.is_file())
    # Capture exactly imported production package dependencies for offline reproduction.
    sys.path.insert(0, str(ROOT/'src'))
    import enterprise_math.brc_transport  # noqa: F401
    for name, module in list(sys.modules.items()):
        source = getattr(module, '__file__', None)
        if name.startswith('enterprise_math') and source:
            p = Path(source).resolve()
            if p.suffix == '.py' and p.is_relative_to(ROOT):
                selected.append(p)
    selected = sorted(set(selected))
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for p in selected:
            name = str(p.relative_to(ROOT))
            info = zipfile.ZipInfo(name, (2026, 10, 2, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED if p.suffix == '.gz' else zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, p.read_bytes())
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        for p in selected:
            assert archive.read(str(p.relative_to(ROOT))) == p.read_bytes()
    result = {'path': str(destination), 'file_count': len(selected), **digest(destination)}
    # Drive's local-file transfer gateway caps a single file at 100 MiB.
    # These are ordinary independent ZIPs: extract all parts to the same folder.
    if destination.stat().st_size > part_limit:
        groups, group, size = [], [], 0
        for p in selected:
            if group and size+p.stat().st_size > part_limit:
                groups.append(group)
                group, size = [], 0
            group.append(p)
            size += p.stat().st_size
        if group:
            groups.append(group)
        parts = []
        instructions = ('Extract ALL part ZIPs into the SAME empty directory. '
                        'Then run python experiments/brc_long_horizon_fit_20261002_9d72ac/make_bundle.py --verify. '
                        'Do not concatenate these ZIPs; each contains a disjoint subset of original files.\n')
        for index, group in enumerate(groups, 1):
            target = destination.with_name(destination.stem+f'.part{index:02d}.zip')
            with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
                archive.writestr(zipfile.ZipInfo('BACKUP_RESTORE.txt', (2026,10,2,0,0,0)), instructions)
                for p in group:
                    info = zipfile.ZipInfo(str(p.relative_to(ROOT)), (2026,10,2,0,0,0))
                    info.compress_type = zipfile.ZIP_STORED if p.suffix == '.gz' else zipfile.ZIP_DEFLATED
                    info.external_attr = 0o644 << 16
                    archive.writestr(info, p.read_bytes())
            with zipfile.ZipFile(target) as archive:
                assert archive.testzip() is None
                for p in group:
                    assert archive.read(str(p.relative_to(ROOT))) == p.read_bytes()
            assert target.stat().st_size < 104857600
            parts.append({'path': str(target), 'file_count': len(group), **digest(target)})
        result['parts'] = parts
        result['restore'] = instructions.strip()
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT.parent/'brc_fit_backup_20261002_9d72ac.zip')
    args = parser.parse_args()
    print(json.dumps({'verified_files': verify()} if args.verify else bundle(args.output), indent=2))
