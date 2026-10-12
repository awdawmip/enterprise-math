#!/usr/bin/env python3
"""Closed-set UTF8 original byte custody only; no mathematical imports/interpretation."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import base64
import gzip
import hashlib
import json
import zlib

ROOT = Path('/workspace/em-owner-resume-20261011/t6-p17-order4-own-execution-20261012')
DEST = Path(__file__).resolve().parent
OLD = Path('/workspace/em-owner-resume-20261011/t6-p17-order3-own-execution-20261012/actual-source-complete-readback-isolation/actual-source-outer/unpack_lossless_source_capsule.py')
LIMIT = 1048576
SCHEMA = 'T6_ORDER3_LOSSLESS_SOURCE_FILES_CAPSULE_V1'
ENCODING = 'gzip+base64-of-UTF8-JSON-with-base64-original-files'
AUTHORS = ['EM-DIRECT-49ADE6', 'EM-DIRECT-E1F2B6', 'EM-DIRECT-FA0C27', 'EM-DVR-4C90FB', 'EM-DVR-C1A1D9', 'EM-DVR-FBF223', 'EM-T6-B4F89F', 'EM-DVR-4CF7AF']

def pin(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}

def json_bytes(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False) + '\n').encode('utf-8')

def write_exclusive(path, raw):
    with path.open('xb') as handle:
        handle.write(raw)

fixed = [
    'CURRENT_NATIVE_EXECUTION_CONTEXT.json', 'SCIENTIFIC_SINGLE_PRODUCER_STDOUT_STDERR.log', 'PROOF_BYTE_PACK_STDOUT.json',
    'science-output/SCIENCE_INVOCATION_START.json', 'science-output/SCIENTIFIC_FRONTIER.json',
    'independent-source-only-local-proof-check/WHOLE30992_EXACT_SAVED_PROOF_CONSUMER_REPORT.json',
    'independent-source-only-local-proof-check/CONSUMER_STDOUT_STDERR.log',
    'native/RECEIPT_01_VERIFIED_FULL_READBACK_WRAPPER.json',
    'native/ACTUAL_CURRENT_Q4_SOURCE_NATIVE_SCOPE_ALL18_FULL_BYTES_VERIFIED.json',
    'native/ACTUAL_CURRENT_Q4_PRE_SCIENCE_SOURCE_NATIVE_GUARD_PASS.json',
    'native/OWN_ACTUAL_Q4_ALL12_CODE_REVIEW_SOURCE_BYTES_AND_SIX_CODE_COPY_VERIFIED.json',
    'independent-post-admission-source-packet-plan-review/LOCAL_POST_ADMISSION_SOURCE_PACKET_PLAN_REVIEW.json',
    'independent-post-admission-source-packet-plan-review/LOCAL_POST_ADMISSION_SOURCE_PACKET_PLAN_REVIEW.md',
]
for prefix in ('REQUEST', 'POST'):
    fixed += [f'native/{prefix}_{i:02}.json' for i in range(1, 8)]
missing = [p for p in fixed if not (ROOT / p).is_file()]
paths = [p for p in fixed if (ROOT / p).is_file()]
paths += ['native/' + p.name for p in sorted((ROOT / 'native').glob('RECEIPT_*_FINAL.json'))]
assert len(paths) == len(set(paths)), 'Duplicate closed original declaration'
paths.sort()
originals, manifests = {}, []
for name in paths:
    assert PurePosixPath(name).as_posix() == name and not name.startswith('/') and all(x not in ('', '.', '..') for x in name.split('/'))
    raw = (ROOT / name).read_bytes()
    raw.decode('utf-8')  # Encoding check only: no original JSON/math parse or reserialization.
    originals[name] = raw
    manifests.append({'path': name, **pin(raw)})

# Context is observed native-control metadata only; no scientific conclusion is parsed.
context = json.loads(originals['CURRENT_NATIVE_EXECUTION_CONTEXT.json'])
assert context['scientific_contributor_ids'] == AUTHORS and context['local_helper_native_identity'] == 'UNKNOWN'
assert context['shared_owner_nonblind'] is True and context['global_goal_status'] == 'OPEN'
snapshot = {
    'schema': 'T6_Q4_CLOSED_SCIENTIFIC_AND_NATIVE_CONTROL_ORIGINAL_BYTE_SNAPSHOT_V1',
    'status': 'FROZEN_LOCAL_EXACT_ORIGINALS_PROSPECTIVE_SOURCE_CUSTODY_ONLY',
    'captured_utc': datetime.now(timezone.utc).isoformat(),
    'file_count': len(manifests), 'original_total_bytes': sum(p['bytes'] for p in manifests),
    'files': manifests, 'missing_explicitly_requested_files_not_invented': missing,
    'native_FINAL_receipt_filenames_observed_at_snapshot': [p for p in paths if p.startswith('native/RECEIPT_') and p.endswith('_FINAL.json')],
    'scientific_contributor_ids': AUTHORS, 'native_helper_identity': 'UNKNOWN', 'directed_shared_owner_nonblind': True,
    'observed_actual_owner_context': {k: context[k] for k in ('task_id', 'publication_id', 'researcher_id', 'session_id', 'claim_id', 'execution_record_id', 'run_id', 'run_generation')},
    'contributor_roles_from_actual_context': context['contributor_roles'],
    'scientific_original_JSON_or_math_conclusion_interpreted': False,
    'actual_Source_publication_or_native_mathematical_acceptance_asserted': False,
    'global_goal_status': 'OPEN',
    'explicitly_excluded': ['large base64 Source captures', 'existing Source input/carrier/common/code copies',
                            'raw binary duplicated copy; fully preserved by separate Source proof manifest/parts',
                            'CASE_CLASSIFICATION_SUMMARIES local-only regenerable diagnostic'],
}
snapshot_path = DEST / 'CLOSED_SCIENTIFIC_AND_NATIVE_CONTROL_ORIGINAL_BYTE_SNAPSHOT.json'
snapshot_raw = json_bytes(snapshot)
write_exclusive(snapshot_path, snapshot_raw)

decoder_raw = OLD.read_bytes()
assert pin(decoder_raw)['sha256'] == '8f51f6a1236627aa45fe0267f27066052b0baeb8aa26dde99c92bd7408c536be'
assert len(decoder_raw) == 8467
decoder_path = DEST / 'unpack_lossless_source_capsule.py'
write_exclusive(decoder_path, decoder_raw)

def capsule(names):
    rows = [{'path': n, 'content_base64': base64.b64encode(originals[n]).decode('ascii')} for n in names]
    inner = json_bytes({'files': rows})
    assert len(inner) < 64 * 1024 * 1024
    compressed = gzip.compress(inner, compresslevel=9, mtime=0)
    outer = {
        'schema': SCHEMA, 'encoding': ENCODING, 'purpose': 'Q4_CLOSED_SCIENTIFIC_REPORTS_AND_ACTUAL_NATIVE_CONTROLS_LOSSLESS_BYTE_CUSTODY',
        'file_count': len(names), 'files': [{'path': n, **pin(originals[n])} for n in names],
        'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
        'original_container_bytes': len(inner), 'original_container_sha256': hashlib.sha256(inner).hexdigest(),
        'payload': base64.b64encode(compressed).decode('ascii'),
        'construction': {'status': 'LOCAL_BYTE_PACKAGE_NOT_YET_SOURCE_PUBLISHED',
                         'scientific_contributor_ids': AUTHORS, 'native_helper_identity': 'UNKNOWN',
                         'directed_shared_owner_nonblind': True, 'independent_consumer_author_is_not_native_decisive_reviewer': True,
                         'Root_direction_static_canonical_codec_design_author': 'EM-DVR-FBF223',
                         'Driver_fixed_input_Task_interface_author': 'EM-DVR-4CF7AF',
                         'Researcher_operator_assembly_actual_execution_author': 'EM-T6-B4F89F',
                         'genuine_F9_reviewer_not_scientific_author': True,
                         'originals_parsed_or_reserialized': False, 'scientific_or_native_operation': False,
                         'mathematical_verdict_created': False, 'global_goal_status': 'OPEN'},
    }
    return json_bytes(outer), inner, compressed

all_raw, _, _ = capsule(paths)
if len(all_raw) < LIMIT:
    groups = [paths]
else:
    # Pure-byte partitions only; an original is never cut or omitted.
    groups, current = [], []
    for name in sorted(paths, key=lambda p: (-len(originals[p]), p)):
        candidate = sorted(current + [name])
        if len(capsule(candidate)[0]) >= LIMIT:
            assert current, 'One complete original cannot fit the reused Source capsule contract; do not silently fragment it'
            groups.append(sorted(current)); current = [name]
            assert len(capsule(current)[0]) < LIMIT, 'One complete original is too large for a Source capsule'
        else:
            current = candidate
    if current:
        groups.append(sorted(current))

outer_pins, checked_paths = [], []
for i, names in enumerate(groups, 1):
    raw, inner, compressed = capsule(names)
    assert len(raw) < LIMIT
    name = f'Q4_SCIENTIFIC_AND_NATIVE_CONTROL_LOSSLESS_CAPSULE_{i:02}.json'
    write_exclusive(DEST / name, raw)
    decoder = zlib.decompressobj(31)
    decoded = decoder.decompress(compressed, len(inner) + 1) + decoder.flush()
    assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail and decoded == inner
    container = json.loads(decoded)
    assert len(container['files']) == len(names)
    for row in container['files']:
        content = base64.b64decode(row['content_base64'], validate=True)
        assert base64.b64encode(content).decode('ascii') == row['content_base64'] and content == originals[row['path']]
        checked_paths.append(row['path'])
    outer_pins.append({'path': name, **pin(raw), 'file_count': len(names),
                       'original_bytes': sum(len(originals[n]) for n in names), 'container_bytes': len(inner),
                       'gzip_bytes': len(compressed), 'member_paths': names})
assert sorted(checked_paths) == paths and len(checked_paths) == len(set(checked_paths))
assert all((ROOT / n).read_bytes() == originals[n] for n in paths), 'Original bytes changed during package construction'
report = {
    'schema': 'T6_Q4_CLOSED_SCIENTIFIC_NATIVE_CONTROL_LOSSLESS_CAPSULE_BUILD_RECEIPT_V1',
    'status': 'COMPLETE_CLOSED_ORIGINAL_BYTE_CONTAINER_ROUNDTRIP_PASS',
    'original_count': len(paths), 'original_total_bytes': sum(len(v) for v in originals.values()),
    'capsule_count': len(outer_pins), 'capsules': outer_pins, 'capsule_total_bytes': sum(x['bytes'] for x in outer_pins),
    'all_original_byte_SHA_Gitblob_UTF8_roundtrip': True, 'single_complete_CRC_gzip_member_independently_checked': True,
    'all_original_current_bytes_unchanged': True, 'missing_requested_originals': missing,
    'snapshot': {'path': snapshot_path.name, **pin(snapshot_raw)},
    'decoder': {'path': decoder_path.name, **pin(decoder_raw),
                'reused_actual_Source_commit': '9c3b36d406f43c523d9a056dd96ded059402be1a',
                'reused_actual_Source_path': 'research_artifacts/mcp/RS-T6-P17-TOTAL-ORDER3-LITERAL-PORTABLE-20261012/MCP-2b2adc7725e84b0c90908ba5db66a17f/8034b7118a2064ce7588/unpack_lossless_source_capsule.py',
                'exact_reused_bytes': True},
    'fresh_physical_Source_decoder_restoration_not_yet_executed': True,
    'scientific_producer_consumer_math_import_or_execution': False,
    'native_remote_or_Source_operation': False, 'native_helper_identity': 'UNKNOWN',
    'directed_shared_owner_nonblind': True, 'global_goal_status': 'OPEN', 'native_mathematical_verdict_created': False,
}
write_exclusive(DEST / 'Q4_SCIENTIFIC_AND_NATIVE_CONTROL_CAPSULE_BUILD_RECEIPT.json', json_bytes(report))
print(json.dumps({'status': report['status'], 'original_count': len(paths), 'original_total_bytes': report['original_total_bytes'],
                  'capsule_count': len(outer_pins), 'capsules': [{k: v for k, v in p.items() if k != 'member_paths'} for p in outer_pins],
                  'decoder': report['decoder']}))
