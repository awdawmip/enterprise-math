#!/usr/bin/env python3
"""Independent byte checks plus the exact Source-only integrity decoder, no math."""
from pathlib import Path
from datetime import datetime, timezone
import base64
import hashlib
import json
import subprocess
import sys
import zlib

ROOT = Path('/workspace/em-owner-resume-20261011/t6-p17-order4-own-execution-20261012')
HERE = Path(__file__).resolve().parent
DESTINATION = HERE / 'fresh-scientific-native-control-original-byte-restoration'
assert not DESTINATION.exists() and not DESTINATION.is_symlink(), 'Use a fresh exclusive restoration root'

def pin(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}

def file_pin(path):
    return {'path': str(path), **pin(Path(path).read_bytes())}

def pairs(items):
    result = {}
    for k, v in items:
        assert k not in result, 'Duplicate JSON key'
        result[k] = v
    return result

def reject(token):
    raise ValueError('Floating/nonfinite capsule/container metadata: ' + token)

def parse(raw):
    return json.loads(raw.decode('utf-8'), object_pairs_hook=pairs, parse_float=reject, parse_constant=reject)

def decode(value):
    raw = base64.b64decode(value, validate=True)
    assert base64.b64encode(raw).decode('ascii') == value, 'Noncanonical base64'
    return raw

snapshot_path = HERE / 'CLOSED_SCIENTIFIC_AND_NATIVE_CONTROL_ORIGINAL_BYTE_SNAPSHOT.json'
build_path = HERE / 'Q4_SCIENTIFIC_AND_NATIVE_CONTROL_CAPSULE_BUILD_RECEIPT.json'
snapshot, build = parse(snapshot_path.read_bytes()), parse(build_path.read_bytes())
decoder = HERE / 'unpack_lossless_source_capsule.py'
assert pin(decoder.read_bytes()) == {k: build['decoder'][k] for k in ('bytes', 'sha256', 'git_blob_sha1')}
assert pin(decoder.read_bytes())['sha256'] == '8f51f6a1236627aa45fe0267f27066052b0baeb8aa26dde99c92bd7408c536be'
expected = {p['path']: p for p in snapshot['files']}
assert len(expected) == snapshot['file_count']
independent_decoded, invocations = {}, []
for row in build['capsules']:
    capsule_path = HERE / row['path']
    raw = capsule_path.read_bytes()
    assert pin(raw) == {k: row[k] for k in ('bytes', 'sha256', 'git_blob_sha1')} and len(raw) < 1048576
    capsule = parse(raw)
    assert capsule['schema'] == 'T6_ORDER3_LOSSLESS_SOURCE_FILES_CAPSULE_V1'
    assert capsule['encoding'] == 'gzip+base64-of-UTF8-JSON-with-base64-original-files'
    compressed = decode(capsule['payload'])
    assert hashlib.sha256(compressed).hexdigest() == capsule['gzip_sha256']
    size = capsule['original_container_bytes']
    assert type(size) is int and 0 < size < 64 * 1024 * 1024
    engine = zlib.decompressobj(31)
    container = engine.decompress(compressed, size + 1)
    assert len(container) <= size and not engine.unconsumed_tail
    container += engine.flush()
    assert engine.eof and not engine.unused_data and not engine.unconsumed_tail and len(container) == size
    assert hashlib.sha256(container).hexdigest() == capsule['original_container_sha256']
    inner = parse(container)
    assert set(inner) == {'files'}
    manifest = capsule['files']
    assert capsule['file_count'] == len(manifest) == len(inner['files'])
    assert [p['path'] for p in manifest] == [p['path'] for p in inner['files']]
    for member, advertised in zip(inner['files'], manifest):
        assert set(member) == {'path', 'content_base64'} and set(advertised) == {'path', 'bytes', 'sha256', 'git_blob_sha1'}
        name = member['path']
        assert name in expected and name not in independent_decoded and advertised == expected[name]
        original = decode(member['content_base64']); original.decode('utf-8')
        assert pin(original) == {k: expected[name][k] for k in ('bytes', 'sha256', 'git_blob_sha1')}
        assert original == (ROOT / name).read_bytes()
        independent_decoded[name] = original
    stdout_path = HERE / (capsule_path.stem + '.source_decoder.stdout.json')
    stderr_path = HERE / (capsule_path.stem + '.source_decoder.stderr.log')
    command = [sys.executable, str(decoder), str(capsule_path), str(DESTINATION),
               '--expected-capsule-sha256', row['sha256']]
    completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    with stdout_path.open('xb') as f:
        f.write(completed.stdout)
    with stderr_path.open('xb') as f:
        f.write(completed.stderr)
    assert completed.returncode == 0 and completed.stderr == b''
    output = parse(completed.stdout)
    assert output['status'] == 'BYTE_CUSTODY_PASS' and output['file_count'] == len(manifest)
    assert output['scientific_functions_executed'] is output['native_or_Source_operations'] is False
    invocations.append({'command': command, 'exit_code': completed.returncode,
                        'stdout': file_pin(stdout_path), 'stderr': file_pin(stderr_path),
                        'capsule_sha256': row['sha256']})
assert set(independent_decoded) == set(expected)
written = sorted(p.relative_to(DESTINATION).as_posix() for p in DESTINATION.rglob('*') if p.is_file())
assert written == sorted(expected) and all(not p.is_symlink() for p in DESTINATION.rglob('*'))
roundtrip = []
for name, advertised in sorted(expected.items()):
    restored = (DESTINATION / name).read_bytes()
    assert restored == independent_decoded[name] == (ROOT / name).read_bytes()
    assert pin(restored) == {k: advertised[k] for k in ('bytes', 'sha256', 'git_blob_sha1')}
    roundtrip.append(advertised)
receipt = {
    'schema': 'T6_Q4_FRESH_SOURCE_DECODER_CLOSED_ORIGINAL_BYTE_RESTORATION_RECEIPT_V1',
    'status': 'INDEPENDENT_COMPLETE_BYTE_DECODE_AND_EXACT_SOURCE_UNPACKER_FRESH_RESTORATION_PASS',
    'verified_utc': datetime.now(timezone.utc).isoformat(),
    'restored_original_count': len(roundtrip), 'restored_original_bytes': sum(p['bytes'] for p in roundtrip),
    'members': roundtrip, 'fresh_exclusive_destination': str(DESTINATION),
    'independent_strict_JSON_canonical_base64_single_complete_CRC_gzip_inventory_check': True,
    'independent_decoder_vs_exact_Source_decoder_vs_all_current_originals_byte_SHA_Gitblob_equal': True,
    'originals_unchanged_before_build_after_build_after_restore': True,
    'missing_requested_originals_not_invented': snapshot['missing_explicitly_requested_files_not_invented'],
    'exact_Source_decoder': file_pin(decoder), 'invocations': invocations,
    'snapshot': file_pin(snapshot_path), 'builder_receipt': file_pin(build_path),
    'helper_native_identity': 'UNKNOWN', 'directed_shared_owner_nonblind': True,
    'scientific_contributor_ids': snapshot['scientific_contributor_ids'],
    'scientific_original_content_or_math_conclusion_interpreted': False,
    'producer_consumer_math_execution_or_import': False,
    'native_remote_or_Source_operation': False,
    'actual_Source_custody_or_native_mathematical_acceptance_created': False,
    'global_goal_status': 'OPEN',
}
receipt_path = HERE / 'Q4_FRESH_EXCLUSIVE_SCIENTIFIC_NATIVE_CONTROL_BYTE_RESTORATION_RECEIPT.json'
with receipt_path.open('x', encoding='utf-8') as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False); f.write('\n')
references = {
    'schema': 'T6_Q4_FROZEN_LOCAL_SCIENTIFIC_NATIVE_CONTROL_PUBLICATION_REFERENCES_V1',
    'status': 'LOCAL_EXACT_BYTE_PACKAGE_READY_NOT_SOURCE_PUBLISHED',
    'closed_original_count': len(roundtrip), 'closed_original_bytes': sum(p['bytes'] for p in roundtrip),
    'closed_original_snapshot_pin': file_pin(snapshot_path),
    'capsules_for_actual_parent_publication_plan': [{'path': str(HERE / p['path']),
                                                  **{k: p[k] for k in ('bytes', 'sha256', 'git_blob_sha1')},
                                                  'member_count': p['file_count']} for p in build['capsules']],
    'capsule_total_bytes': sum(p['bytes'] for p in build['capsules']),
    'exact_portable_decoder_local_pin': file_pin(decoder),
    'decoder_exact_prior_actual_Source_reference': {k: build['decoder'][k] for k in ('reused_actual_Source_commit', 'reused_actual_Source_path', 'sha256', 'git_blob_sha1')},
    'Source_publication_all_originals_scientific_claim_is_prospective_only': True,
    'package_tools_and_receipts_local_support_pins': [file_pin(p) for p in [Path(__file__), HERE / 'build_scientific_and_native_control_lossless_capsules.py', build_path, receipt_path]],
    'scientific_contributor_ids': snapshot['scientific_contributor_ids'], 'helper_native_identity': 'UNKNOWN',
    'directed_shared_owner_nonblind': True, 'Root_design_credit': 'EM-DVR-FBF223',
    'no_math_native_or_Source_operation_or_identity_borrowed': True,
    'excluded_nonadopted_or_previously_Source_inputs_and_diagnostics': snapshot['explicitly_excluded'],
    'global_goal_status': 'OPEN',
}
references_path = HERE / 'Q4_CLOSED_SCIENTIFIC_NATIVE_CONTROL_FROZEN_PUBLICATION_REFERENCES.json'
with references_path.open('x', encoding='utf-8') as f:
    json.dump(references, f, indent=2, ensure_ascii=False); f.write('\n')
print(json.dumps({'status': receipt['status'], 'original_count': len(roundtrip),
                  'original_total_bytes': receipt['restored_original_bytes'],
                  'receipt': file_pin(receipt_path), 'frozen_references': file_pin(references_path)}))
