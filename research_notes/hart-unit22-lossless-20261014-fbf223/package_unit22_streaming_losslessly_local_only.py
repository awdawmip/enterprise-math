#!/usr/bin/env python3
"""Byte custody only: no scientific imports or parsing of measurement JSON."""
import gzip
import hashlib
import json
import os
import stat
import tarfile
import time
from datetime import datetime, timezone
from pathlib import Path

D = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
ROOT_PROOF = Path('/workspace/em-research-continuation-20261014/publication/ROOT_UNIT22_NEW_RAW_INDEPENDENT_ARITHMETIC_AND_PREFIX_COST_PROOF.json')
ROOT_INTERPRETATION = ROOT_PROOF.with_name('ROOT_UNIT22_PAID_PREFIX_DOMINANCE_INTERPRETATION.md')
SOURCES = [
    ('de291f8c527f11a7ddce7f30105b58d25c531779', 'research_notes/HART_UNIT22_NEAR56_R2_PREGEN_CODE_20261014_FBF223.json', 'OWN_NEAR56_CODE_SOURCE_CONNECTED_ACTUAL_FULL_COLD.json', 198416, '517fb70241cdcae03c1beac58772a254ff473013c32472bcd583744b5703a1ce', '3bdf91b00af090716a9b4ca2e662533e415c51ac'),
    ('9c0ea61508391d759bd48cc857f4c41eda19224a', 'research_notes/HART_UNIT22_NEAR56_ORDERED_CORPUS_PREEXECUTION_20261014_FBF223.json', 'OWN_NEAR56_CORPUS_SOURCE_CONNECTED_ACTUAL_FULL_COLD.json', 39622, 'b06d550fc7986d2839b5f6768d6f34dc7063a3b7a28fcc2c36c002779cc80d20', '44204248cdd1349833f935287b252bfc975a181b'),
    ('f4c633ccbb2ec08ad9df25ff93668c13f4bf1f82', 'research_notes/HART_UNIT22_CORPUS_SINGLE_KEY_CORRECTION_20261014_FBF223.json', 'OWN_NEAR56_CORPUS_CORRECTION_SOURCE_CONNECTED_ACTUAL_FULL_COLD.json', 15339, '944fd0c69d01828c0da841ec59768462fa47a45ef9c4502b7642085226bd9a82', '1d2971d34b4fda2e9fc48002bee245630dabb0d5'),
]

def utc():
    return datetime.now(timezone.utc).isoformat()

def exclusive_json(path, value):
    body = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    with path.open('xb') as f:
        f.write(body)
        f.flush()
        os.fsync(f.fileno())
    fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    return body

def pin(path):
    before = path.stat()
    assert stat.S_ISREG(before.st_mode) and not path.is_symlink(), str(path)
    sha = hashlib.sha256()
    blob = hashlib.sha1(b'blob ' + str(before.st_size).encode() + b'\0')
    total = 0
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            sha.update(block)
            blob.update(block)
            total += len(block)
    after = path.stat()
    assert (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
    assert total == before.st_size
    return dict(path=str(path), bytes=total, sha256=sha.hexdigest(), git_blob_sha1=blob.hexdigest())

def shape_info(path):
    st = path.stat()
    return dict(device=st.st_dev, inode=st.st_ino, link_count=st.st_nlink, mode=stat.S_IMODE(st.st_mode), mtime_ns=st.st_mtime_ns)

class HashingWriter:
    def __init__(self, inner):
        self.inner = inner
        self.sha = hashlib.sha256()
        self.bytes = 0
    def write(self, data):
        self.sha.update(data)
        self.bytes += len(data)
        return self.inner.write(data)
    def flush(self):
        return self.inner.flush()

class HashingReader:
    def __init__(self, inner, expected_length):
        self.inner = inner
        self.sha = hashlib.sha256()
        self.blob = hashlib.sha1(b'blob ' + str(expected_length).encode() + b'\0')
        self.bytes = 0
    def read(self, amount=-1):
        data = self.inner.read(amount)
        self.sha.update(data)
        self.blob.update(data)
        self.bytes += len(data)
        return data

def main():
    t0, c0 = time.perf_counter_ns(), time.process_time_ns()
    exclusive_json(OUT / 'UNIT22_CUSTODY_PACK_STARTED.json', {
        'schema': 'UNIT22_STREAMING_BYTE_CUSTODY_START_V1', 'started_utc': utc(),
        'pid': os.getpid(), 'invocation': 1, 'science_invocations_in_this_process': 0,
        'scope': 'stream hashes, one gzip tar construction, one streaming byte verification; no raw JSON parse',
    })
    immutable = {}
    source_files = {}
    source_records = []
    for commit, source_path, local_name, size, sha, blob in SOURCES:
        path = D / local_name
        p = pin(path)
        assert (p['bytes'], p['sha256'], p['git_blob_sha1']) == (size, sha, blob)
        source = dict(commit=commit, source_path=source_path, source_file_pin=p)
        source_records.append(source)
        source_files[str(path)] = source
        doc = json.loads(path.read_text())  # small existing capsule metadata; archive never decoded
        for row in doc['full_originals_manifest']:
            identity = row['bytes'], row['sha256'], row['git_blob_sha1']
            immutable.setdefault(identity, []).append(dict(commit=commit, source_path=source_path, archive_path=row['archive_path'], original_path=row['path']))
    paths = []
    for path in sorted(D.rglob('*')):
        if OUT in path.parents or '__pycache__' in path.parts:
            continue
        if path.is_symlink():
            raise ValueError('Unexpected symlink: ' + str(path))
        if path.is_file():
            paths.append(path)
    paths += [Path(__file__).resolve(), OUT / 'launch_one_unit22_custody_pack.py', ROOT_PROOF, ROOT_INTERPRETATION]
    assert len(paths) == len(set(paths))
    members, references = [], []
    inode_cache, first_names = {}, {}
    for path in paths:
        st = path.stat()
        key = st.st_dev, st.st_ino
        if key not in inode_cache:
            inode_cache[key] = pin(path)
        p = dict(inode_cache[key], path=str(path))
        if str(path) in source_files:
            references.append(dict(**p, disposition='IMMUTABLE_SOURCE_BODY_REFERENCE', source=source_files[str(path)]))
            continue
        identity = p['bytes'], p['sha256'], p['git_blob_sha1']
        if identity in immutable:
            references.append(dict(**p, disposition='IMMUTABLE_SOURCE_MEMBER_REFERENCE', sources=immutable[identity]))
            continue
        name = ('new-unit22/' + str(path.relative_to(D))) if path.is_relative_to(D) else ('root-independent/' + path.name)
        assert not name.startswith('/') and '..' not in Path(name).parts
        row = dict(**p, archive_path=name, original_stat=shape_info(path))
        row['hardlink_to'] = first_names.get(key)
        first_names.setdefault(key, name)
        members.append(row)
    raw = next(r for r in members if Path(r['path']).name == 'ONE_NEAR56_STRONG_CONTROL_ACTUAL_MEASUREMENT_RAW.json')
    assert (raw['bytes'], raw['sha256'], raw['git_blob_sha1']) == (200755710, '42633baeea61918004159f9d9bb0caec0d6c4916e189d6017a28afedf213cfd1', '8c3f6859573624036abe1c71d502a43cf916af59')
    store = [r for r in members if 'UNIT21_IMMUTABLE_DIAGNOSTIC_CHECKPOINTS' in Path(r['path']).parts]
    assert len(store) == 107 and sum(r['hardlink_to'] is not None for r in store) == 53
    inventory = {
        'schema': 'UNIT22_NEW_RESULT_BYTE_CUSTODY_INPUT_MANIFEST_V1', 'prepared_utc': utc(),
        'science_invocations': 0, 'large_measurement_json_parses': 0,
        'members': members, 'immutable_references': references, 'immutable_sources': source_records,
        'member_count': len(members), 'logical_member_bytes': sum(r['bytes'] for r in members),
        'unique_regular_body_bytes': sum(r['bytes'] for r in members if r['hardlink_to'] is None),
        'hardlink_alias_count': sum(r['hardlink_to'] is not None for r in members),
        'store_pathnames': len(store), 'store_logical_bytes': sum(r['bytes'] for r in store),
        'emergency_spool_present': (D / 'UNIT21_EMERGENCY_LOGICAL_RAW_SPOOL.json').exists(),
        'notes': [
            'Exact current bytes already in immutable prior Source are referenced by complete identities, not re-encoded.',
            'Every store pathname including unreferenced PENDING files is retained. Tar aliases preserve original hardlink groups.',
            'No scientific module is imported, no producer/checker/summary is replayed, no large measurement JSON is parsed.',
            'Logical bytes count hardlink aliases; unique body bytes do not. Archive bytes are separately measured.',
            'Whole63 UNFINISHED; mathematical parent OPEN; all eight priority pairs UNKNOWN.',
        ],
    }
    manifest_path = OUT / 'UNIT22_NEW_RESULT_ALL_INPUTS_AND_SOURCE_REFERENCES.json'
    exclusive_json(manifest_path, inventory)
    manifest_row = dict(**pin(manifest_path), archive_path='custody/UNIT22_NEW_RESULT_ALL_INPUTS_AND_SOURCE_REFERENCES.json', hardlink_to=None, original_stat=shape_info(manifest_path))
    all_rows = members + [manifest_row]
    print(json.dumps({'phase': 'INPUTS_PINNED', 'pid': os.getpid(), 'members': len(members), 'references': len(references), 'unique_body_bytes': inventory['unique_regular_body_bytes'], 'hardlink_aliases': inventory['hardlink_alias_count'], 'manifest': pin(manifest_path)}), flush=True)
    pack_t, pack_c = time.perf_counter_ns(), time.process_time_ns()
    archive = OUT / 'UNIT22_COMPLETE_NEW_RESULT_LOSSLESS.tar.gz'
    with archive.open('xb') as target:
        with gzip.GzipFile(filename='', mode='wb', fileobj=target, mtime=0, compresslevel=6) as compressed:
            tar_writer = HashingWriter(compressed)
            with tarfile.open(fileobj=tar_writer, mode='w|', format=tarfile.PAX_FORMAT, dereference=False) as tar:
                for row in all_rows:
                    info = tarfile.TarInfo(row['archive_path'])
                    info.uid = info.gid = info.mtime = 0
                    info.mode = row['original_stat']['mode']
                    if row['hardlink_to']:
                        info.type = tarfile.LNKTYPE
                        info.linkname = row['hardlink_to']
                        info.size = 0
                        tar.addfile(info)
                    else:
                        info.size = row['bytes']
                        before = shape_info(Path(row['path']))
                        assert before == row['original_stat']
                        with open(row['path'], 'rb') as body:
                            tar.addfile(info, body)
                        assert shape_info(Path(row['path'])) == before
        target.flush()
        os.fsync(target.fileno())
    fd = os.open(OUT, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    pack_metrics = dict(wall_ns=time.perf_counter_ns() - pack_t, cpu_ns=time.process_time_ns() - pack_c)
    archive_pin = pin(archive)
    print(json.dumps({'phase': 'ARCHIVE_COMPLETE', 'archive': archive_pin, 'tar_bytes': tar_writer.bytes, 'tar_sha256': tar_writer.sha.hexdigest(), 'pack_cost': pack_metrics}), flush=True)
    verify_t, verify_c = time.perf_counter_ns(), time.process_time_ns()
    expected = {r['archive_path']: r for r in all_rows}
    verified = {}
    with archive.open('rb') as source:
        with gzip.GzipFile(fileobj=source, mode='rb') as decompressed:
            reader = HashingReader(decompressed, tar_writer.bytes)
            with tarfile.open(fileobj=reader, mode='r|') as tar:
                for info in tar:
                    assert info.name in expected and info.name not in verified
                    row = expected[info.name]
                    if row['hardlink_to']:
                        assert info.islnk() and info.linkname == row['hardlink_to']
                        result = verified[info.linkname]
                    else:
                        assert info.isfile() and info.size == row['bytes']
                        sha = hashlib.sha256()
                        blob = hashlib.sha1(b'blob ' + str(info.size).encode() + b'\0')
                        total = 0
                        member = tar.extractfile(info)
                        for block in iter(lambda: member.read(1024 * 1024), b''):
                            total += len(block)
                            sha.update(block)
                            blob.update(block)
                        result = dict(bytes=total, sha256=sha.hexdigest(), git_blob_sha1=blob.hexdigest())
                    assert all(result[k] == row[k] for k in ['bytes', 'sha256', 'git_blob_sha1']), info.name
                    verified[info.name] = result
            while reader.read(1024 * 1024):
                pass
    assert len(verified) == len(all_rows)
    assert (reader.bytes, reader.sha.hexdigest()) == (tar_writer.bytes, tar_writer.sha.hexdigest())
    proof = {
        'schema': 'UNIT22_ONE_STREAMING_ARCHIVE_FULL_BYTE_ROUNDTRIP_PROOF_V1', 'completed_utc': utc(),
        'pid': os.getpid(), 'status': 'PASS_FULL_NEW_BYTES_AND_HARDLINK_IDENTITY',
        'input_manifest': pin(manifest_path), 'archive': archive_pin,
        'tar_stream': dict(bytes=reader.bytes, sha256=reader.sha.hexdigest(), git_blob_sha1=reader.blob.hexdigest()),
        'tar_members': len(all_rows), 'new_original_members': len(members),
        'all_member_logical_bytes_including_manifest': sum(r['bytes'] for r in all_rows),
        'unique_regular_body_bytes_including_manifest': sum(r['bytes'] for r in all_rows if not r['hardlink_to']),
        'hardlink_aliases_verified': inventory['hardlink_alias_count'], 'immutable_reference_count': len(references),
        'new_original_member_pins': [{k: r[k] for k in ['path', 'archive_path', 'bytes', 'sha256', 'git_blob_sha1', 'hardlink_to']} for r in members],
        'pack_stage': pack_metrics,
        'roundtrip_stage': dict(wall_ns=time.perf_counter_ns() - verify_t, cpu_ns=time.process_time_ns() - verify_c),
        'previously_completed_before_this_proof_encode': dict(wall_ns=time.perf_counter_ns() - t0, cpu_ns=time.process_time_ns() - c0),
        'cost_scope': 'Positive postscience custody costs; proof encode/write/fsync/last receipt occur after this boundary and are not represented as free or self-hashed.',
        'scientific_execution_in_this_process': 0, 'large_measurement_json_parses': 0,
        'science_status': 'Partial six-method matrix, eight priority pairs UNKNOWN; whole63 UNFINISHED, parent OPEN',
    }
    exclusive_json(OUT / 'UNIT22_LOCAL_FULL_STREAMING_CUSTODY_ROUNDTRIP_PROOF.json', proof)
    print(json.dumps({'phase': 'PASS', 'archive': archive_pin, 'proof': pin(OUT / 'UNIT22_LOCAL_FULL_STREAMING_CUSTODY_ROUNDTRIP_PROOF.json'), 'manifest': pin(manifest_path), 'new_members': len(members), 'tar_members': len(all_rows), 'hardlink_aliases': inventory['hardlink_alias_count']}), flush=True)

if __name__ == '__main__':
    main()
