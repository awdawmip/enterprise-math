"""Verify actual remote UTF-8 transport; never parse or execute scientific raw."""
from pathlib import Path
import base64
import gc
import hashlib
import json
import os
import sys
import zlib
from datetime import datetime, timezone

B = Path(__file__).resolve().parent
CHUNK = 192 * 1024


def pin(path):
    size = path.stat().st_size
    sha, blob = hashlib.sha256(), hashlib.sha1(b'blob ' + str(size).encode() + b'\0')
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            sha.update(block)
            blob.update(block)
    return {'bytes': size, 'sha256': sha.hexdigest(), 'git_blob_sha1': blob.hexdigest()}


def assert_pin(actual, expected):
    for key in ('bytes', 'sha256', 'git_blob_sha1'):
        assert actual[key] == expected[key], (key, actual[key], expected[key])


def equal_bytes(left, right):
    with left.open('rb') as a, right.open('rb') as b:
        while True:
            aa, bb = a.read(CHUNK), b.read(CHUNK)
            assert aa == bb, (str(left), str(right))
            if not aa:
                return


def finish(stream):
    stream.flush()
    os.fsync(stream.fileno())


def main():
    publication = json.loads((B / 'ROOT_UNIT20_COMPLETE_SCIENTIFIC_SOURCE_PUBLICATION_INPUT.json').read_bytes())
    fetched = json.loads((B / 'ROOT_UNIT20_SCIENTIFIC_SOURCE_ACTUAL_FETCH_METADATA.json').read_bytes())
    assert len(fetched['files']) == len(publication['files'])
    by_path = {m['path']: m for m in fetched['files']}
    verified = []
    for expected in publication['files']:
        actual = by_path[expected['path']]
        cold = Path(actual['cold_path'])
        assert_pin(pin(cold), expected)
        assert actual['actual_connector_blob'] == expected['git_blob_sha1']
        equal_bytes(cold, Path(expected['local_path']))
        verified.append({**expected, 'cold_path': str(cold)})
    manifest_item = next(m for m in verified if m['path'].endswith('/FAR48_RESULT_FRAGMENT_AND_ALL_MEMBER_MANIFEST.json'))
    manifest = json.loads(Path(manifest_item['cold_path']).read_bytes())
    assert manifest['member_count'] == publication['member_count']
    assert manifest['member_bytes'] == publication['member_bytes']
    outdir = B / 'UNIT20_SCIENCE_ACTUAL_REMOTE_BYTE_RESTORATION'
    outdir.mkdir(exist_ok=True)
    capsulepath = outdir / 'ACTUAL_FETCHED_COMPLETE_CAPSULE.json'
    with capsulepath.open('xb') as out:
        for fragment in manifest['fragments']:
            basename = Path(fragment['path']).name
            source = next(m for m in verified if Path(m['path']).name == basename)
            assert_pin(pin(Path(source['cold_path'])), fragment)
            with Path(source['cold_path']).open('rb') as stream:
                for block in iter(lambda: stream.read(CHUNK), b''):
                    out.write(block)
        finish(out)
    assert_pin(pin(capsulepath), manifest['capsule'])
    equal_bytes(capsulepath, Path(publication['capsule']['path']))
    capsule = json.loads(capsulepath.read_bytes())
    payload = capsule.pop('archive_base64')
    assert capsule['member_count'] == manifest['member_count']
    assert capsule['members'] == manifest['members']
    assert capsule['full_Task'] == 'UNFINISHED' and capsule['parent'] == 'OPEN'
    archivepath = outdir / 'ACTUAL_REMOTE_RESTORED_UTF8_ARCHIVE.json'
    decompressor = zlib.decompressobj()
    compressed_sha = hashlib.sha256()
    compressed_bytes = 0
    with archivepath.open('xb') as out:
        for offset in range(0, len(payload), CHUNK):
            block = base64.b64decode(payload[offset:offset + CHUNK], validate=True)
            compressed_sha.update(block)
            compressed_bytes += len(block)
            out.write(decompressor.decompress(block))
        out.write(decompressor.flush())
        finish(out)
    assert decompressor.eof and not decompressor.unused_data
    assert compressed_bytes == capsule['compressed_bytes']
    assert compressed_sha.hexdigest() == capsule['compressed_sha256']
    del payload, block, decompressor
    gc.collect()
    assert_pin(pin(archivepath), manifest['archive'])
    equal_bytes(archivepath, Path(publication['archive']['path']))
    # This is transport JSON. Every mathematical JSON remains an opaque string.
    with archivepath.open('r', encoding='utf-8') as stream:
        archive = json.load(stream)
    assert archive['original_count'] == manifest['member_count']
    assert archive['original_bytes'] == manifest['member_bytes']
    assert len(archive['files']) == manifest['member_count']
    assert archive['original_owner'] == 'EM-SEMIPRIME-1F8B9B'
    assert archive['original_run'] == 'RUN-02bc03dfff15c15ce7daf2f3'
    members = []
    for expected, actual in zip(manifest['members'], archive['files'], strict=True):
        for key in ('path', 'name', 'bytes', 'sha256', 'git_blob_sha1'):
            assert actual[key] == expected[key], (key, expected['path'])
        body = actual.pop('content').encode('utf-8')
        assert len(body) == expected['bytes']
        assert hashlib.sha256(body).hexdigest() == expected['sha256']
        assert hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest() == expected['git_blob_sha1']
        with Path(expected['path']).open('rb') as stream:
            for offset in range(0, len(body), CHUNK):
                assert stream.read(CHUNK) == body[offset:offset + CHUNK]
            assert not stream.read(1)
        members.append(expected)
        del body
    del archive, capsule
    gc.collect()
    raw = next(m for m in members if m['name'] == 'ONE_FAR48_STRONG_CONTROL_ACTUAL_MEASUREMENT_RAW.json')
    assert raw['bytes'] == 470406865
    assert raw['sha256'] == '7c3e8b3e4e0b7334b5cee68a2d4916f5cc6585042eeac138b9a50528141a68bb'
    proof = {'schema': 'ROOT_UNIT20_ACTUAL_SCIENTIFIC_SOURCE_COMPLETE_BYTE_COLD_VERIFICATION_V1',
        'status': 'PASS', 'verified_at': datetime.now(timezone.utc).isoformat(),
        'Source': fetched['Source'], 'source_file_count': len(verified),
        'source_bytes': sum(m['bytes'] for m in verified), 'source_files': verified,
        'capsule': pin(capsulepath), 'archive': pin(archivepath),
        'full_original_count': len(members), 'full_original_bytes': manifest['member_bytes'],
        'all_fragments_members_SHA_blob_and_currentlocal_bytes_equal': True,
        'full_first_and_only_measurement_raw_final_snapshot': raw,
        'mathematical_raw_JSON_parse_or_science_replay': False,
        'all_priority_gain_pairs': 'UNKNOWN_INCOMPLETE_PAIR_MEASUREMENTS',
        'native_mathematical_acceptance': False, 'release': False,
        'full_Task': 'UNFINISHED', 'parent': 'OPEN'}
    path = B / 'ROOT_UNIT20_SCIENTIFIC_SOURCE_FULL_COMPLETE_COLD_VERIFICATION.json'
    with path.open('x', encoding='utf-8') as stream:
        json.dump(proof, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
        finish(stream)
    print(json.dumps({'status': 'PASS', 'Source': fetched['Source'], 'proof': str(path),
        'source_file_count': len(verified), 'full_original_count': len(members),
        'full_original_bytes': manifest['member_bytes'], 'raw_bytes': raw['bytes']}))


if __name__ == '__main__':
    main()
