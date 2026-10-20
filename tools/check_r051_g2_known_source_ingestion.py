#!/usr/bin/env python3
import argparse, hashlib, json, urllib.request
from pathlib import Path

EXPECTED_PROTOCOL_SHA = "be4eaaac5e2425f6ff3c2b617603ab0bd9e8dc2dd0b243dbccc0e2e26c1912d8"
EXPECTED_K1_SHA = "486fbc54eac9e091e071ff1bed7170bcde41c20166a6070ec625baaa7bcac934"
EXPECTED_G1_HEAD = "b6fbf431a3c76c4a437acf97cb7a784762e524ab"
EXPECTED_G1_TARGET = "58b5bcd03cf7070008b2f97a3457d376f566355e1848933317f57a5d2edcc498"
EXPECTED_R049_TARGET = "e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c"
ATTACKS = ["SOURCE_HASH_NOT_VERIFIED", "NUMERIC_VALUES_READ_BEFORE_SCHEMA_SPLIT_FREEZE", "CANDIDATE_INFORMATION_USED_FOR_SOURCE_SELECTION", "CANDIDATE_INFORMATION_USED_FOR_COLUMN_SELECTION", "CANDIDATE_INFORMATION_USED_FOR_SPLIT", "MODEL_OR_DERIVED_COLUMN_PROMOTED_TO_MEASUREMENT", "PLOT_DIGITIZATION_AS_RAW_DATA", "HEADER_ONLY_DATASET_EXISTENCE_PROMOTED_TO_E4", "SAME_OBSERVATION_USED_FOR_CONSTRUCTION_AND_HOLDOUT", "TOLERANCE_INVENTED_WITHOUT_SOURCE", "SOURCE_TABLE_ROUNDING_IGNORED", "UNIT_CONVERSION_DOUBLE_COUNT", "PRESSURE_FAMILY_STRETCHED_FOR_AVAILABLE_DATA", "BLOCK_B_ONE_REALIZATION_ONLY_PROMOTED_TO_PRESSURE_E4", "GENERATION1_TARGET_MUTATED", "CLASSICAL_PI_NUMERIC_SELECTION"]
ALLOWED_TERMINAL = {"E4_ELIGIBLE_TARGET","E3_ONLY_CONSTRUCTION_DATA_NO_INDEPENDENT_HOLDOUT","QUANTITATIVE_DATA_NO_SOURCE_GROUNDED_PASSFAIL","SOURCE_FILE_ACQUIRED_BUT_MEASURED_CARRIER_INELIGIBLE","SOURCE_ACQUISITION_FAILED","REPLACEMENT_REJECTED"}
K1_URL = "https://data.nist.gov/od/ds/7CAEA9D04EC628DEE05324570681AF372008/AWG_LSNA_25KHz.csv"

def sha256_file(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def verify_k1_sidecar(path):
    raw=Path(path).read_bytes()
    if raw != EXPECTED_K1_SHA.encode('ascii'):
        raise ValueError('NIST K1 sidecar bytes do not exactly equal expected main CSV SHA-256')
    return True

def download_k1_exact(dest):
    dest=Path(dest)
    with urllib.request.urlopen(K1_URL, timeout=120) as r, dest.open('wb') as w:
        while True:
            b=r.read(1024*1024)
            if not b: break
            w.write(b)
    got=sha256_file(dest)
    if got != EXPECTED_K1_SHA:
        dest.unlink(missing_ok=True)
        raise ValueError(f'K1 source hash mismatch: {got}')
    return got

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))

def check(root):
    root=Path(root); errors=[]
    protocol=root/'R051_G2_SOURCE_SCHEMA_AND_SPLIT_PROTOCOL.json'
    if sha256_file(protocol)!=EXPECTED_PROTOCOL_SHA: errors.append('schema/split protocol hash mismatch')
    man=load(root/'R051_G2_QUANTITATIVE_HOLDOUT_MANIFEST.json')
    if man['generation1_head']!=EXPECTED_G1_HEAD or man['generation1_target_sha256']!=EXPECTED_G1_TARGET or man['r049_target_sha256']!=EXPECTED_R049_TARGET:
        errors.append('immutable anchor mismatch')
    for fn,expected in man['artifact_hashes'].items():
        p=root/fn
        if not p.exists(): errors.append('missing '+fn); continue
        got='sha256:'+sha256_file(p)
        if got!=expected: errors.append(f'hash mismatch {fn}')
    canon=json.dumps(man['artifact_hashes'], ensure_ascii=False, sort_keys=True, separators=(',',':')).encode('utf-8')
    if hashlib.sha256(canon).hexdigest()!=man['R051_GENERATION2_QUANTITATIVE_TARGET_SHA256']:
        errors.append('generation-2 target hash mismatch')
    atlas=load(root/'R051_G2_QUANTITATIVE_ENGINEERING_ATLAS.json')
    if atlas['target_rows'] or atlas['e4_eligible_row_count']!=0: errors.append('zero-row freeze violated')
    splits=load(root/'R051_G2_CONSTRUCTION_HOLDOUT_SPLITS.json')
    if splits['instantiated_splits'] or splits['construction_observation_count'] or splits['holdout_observation_count']:
        errors.append('split instantiated despite zero-row protocol')
    receipts=load(root/'R051_G2_SOURCE_RECEIPTS.json')
    for s in receipts['receipts']:
        if s['terminal_status'] not in ALLOWED_TERMINAL: errors.append('invalid terminal status '+s['source_id'])
    k1=next(x for x in receipts['receipts'] if x['source_id']=='K1_NIST_PDR_AWG_LSNA_25KHZ')
    if k1['main_file_acquired'] or k1['main_file_exact_byte_sha256_verified'] or k1['source_native_numeric_rows_parsed']:
        errors.append('K1 metadata/sidecar incorrectly promoted')
    leak=load(root/'R051_G2_TARGET_LEAKAGE_AUDIT.json')
    if leak['generation1_mutated'] or leak['forbidden_candidate_surfaces_intentionally_accessed'] or leak['calibration_run']:
        errors.append('leakage firewall violation')
    if not leak['prefreeze_numeric_exposure_events']: errors.append('prefreeze exposure event missing')
    adv=load(root/'R051_G2_ADVERSARIAL_TEST_RESULTS.json')
    if {x['attack'] for x in adv['tests']} != set(ATTACKS): errors.append('required attack set mismatch')
    if any(not x['verdict'].startswith('PASS') for x in adv['tests']): errors.append('adversarial defense failure')
    return errors

def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest='cmd', required=False)
    c=sub.add_parser('check'); c.add_argument('root', nargs='?', default='research_outputs/R051')
    s=sub.add_parser('verify-k1-sidecar'); s.add_argument('path')
    d=sub.add_parser('download-k1'); d.add_argument('dest')
    args=ap.parse_args()
    cmd=args.cmd or 'check'
    if cmd=='check':
        errs=check(getattr(args,'root','research_outputs/R051'))
        if errs:
            for e in errs: print('FAIL:',e)
            raise SystemExit(1)
        print('R051_G2_CHECK_PASS')
    elif cmd=='verify-k1-sidecar':
        verify_k1_sidecar(args.path); print('R051_G2_K1_SIDECAR_PASS')
    elif cmd=='download-k1':
        print(download_k1_exact(args.dest))
if __name__=='__main__': main()
