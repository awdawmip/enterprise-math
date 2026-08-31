#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

ALLOWED={"E4_ELIGIBLE_TARGET","E3_ONLY_CONSTRUCTION_DATA_NO_INDEPENDENT_HOLDOUT","STRUCTURAL_ONLY_NO_NUMERIC_OBSERVATIONS","SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT","PLOT_ONLY_NOT_E4_ELIGIBLE","REPLACED_BY_NEW_CANDIDATE_BLIND_ROW"}
EXPECTED_ROWS=["A1-GMC-M48-STEP-GAGE","A2-CCRP-PMU-PHASE","A3-DR-FDTR-PUMP-PROBE","A4-BMS-CAVITY-VNA","B1A-TIBC-LIQUID-GRAVIMETRIC","B1B-TIBC-GAS-PVTT","B2A-SRIR-MIC-RECIP","B2B-SRIR-ANTENNA-3PAIR"]
ATTACKS=["CANDIDATE_INFORMATION_USED_FOR_DATA_SELECTION","CONSTRUCTION_HOLDOUT_SPLIT_AFTER_CANDIDATE_ACCESS","PLOT_DIGITIZATION_AS_RAW_DATA","MODEL_CURVE_AS_EMPIRICAL_OBSERVATION","CALCULATED_OUTPUT_AS_MEASUREMENT","TOLERANCE_INVENTED_WITHOUT_SOURCE","SAME_OBSERVATION_USED_FOR_FIT_AND_HOLDOUT","UNIT_CONVERSION_DOUBLE_COUNT","SOURCE_TABLE_ROUNDING_IGNORED","BLOCK_B_ONE_REALIZATION_ONLY_PROMOTED_TO_E4","TRAINING_SOURCE_COLLISION_NOT_AUDITED","TARGET_MUTATION_AFTER_FREEZE","CLASSICAL_PI_NUMERIC_SELECTION"]

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def check(root: Path):
    errors=[]
    man=load(root/'R051_QUANTITATIVE_HOLDOUT_MANIFEST.json')
    for fn,h in man['artifact_hashes'].items():
        p=root/fn
        if not p.exists(): errors.append(f'missing authoritative file: {fn}'); continue
        got='sha256:'+sha(p)
        if got!=h: errors.append(f'hash mismatch {fn}: {got} != {h}')
    mapping=man['artifact_hashes']
    canon=json.dumps(mapping,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
    agg=hashlib.sha256(canon).hexdigest()
    if agg!=man['R051_QUANTITATIVE_TARGET_SHA256']: errors.append('aggregate target hash mismatch')
    avail=load(root/'R051_R049_ROW_DATA_AVAILABILITY.json')
    ids=[r['row_id'] for r in avail['rows']]
    if ids!=EXPECTED_ROWS: errors.append('original row order/set mismatch')
    for r in avail['rows']:
        if r['final_row_status'] not in ALLOWED: errors.append('invalid status '+r['row_id'])
        if r['preserve_first_result']!='SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT': errors.append('preserve-first failure marker missing '+r['row_id'])
    atlas=load(root/'R051_QUANTITATIVE_ENGINEERING_ATLAS.json')
    for r in atlas['rows']:
        if r['eligibility']=='E4_ELIGIBLE_TARGET':
            req=[r['condition_index'],r['measured_numerical_values'],r['per_condition_uncertainty_or_covariance'],r['construction_subset_indices'],r['holdout_subset_indices']]
            if any(not x for x in req): errors.append('E4 row lacks required quantitative fields '+r['row_id'])
        else:
            if r['measured_numerical_values']: errors.append('non-E4 row carries target measurements '+r['row_id'])
    if atlas['e4_eligible_row_count']!=sum(r['eligibility']=='E4_ELIGIBLE_TARGET' for r in atlas['rows']): errors.append('E4 count mismatch')
    splits=load(root/'R051_CONSTRUCTION_HOLDOUT_SPLITS.json')
    for r in splits['rows']:
        if set(r['construction_indices']) & set(r['holdout_indices']): errors.append('split overlap '+r['row_id'])
    adv=load(root/'R051_ADVERSARIAL_TEST_RESULTS.json')
    got={t['attack'] for t in adv['tests']}
    if got!=set(ATTACKS): errors.append('required attack set mismatch')
    for t in adv['tests']:
        if not t['verdict'].startswith('PASS'): errors.append('kill test failed '+t['attack'])
    leak=load(root/'R051_TARGET_LEAKAGE_AUDIT.json')
    if leak['g2_content_intentionally_opened'] or leak['calibration_run'] or leak['classical_pi_numeric_selection_used']: errors.append('leakage firewall violation')
    repl=load(root/'R051_REPLACEMENT_ROW_LEDGER.json')
    if repl['replacement_selected_count']!=len(repl['new_generation_rows']): errors.append('replacement count mismatch')
    return errors

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='research_outputs/R051'); args=ap.parse_args()
    errs=check(Path(args.root))
    if errs:
        for e in errs: print('FAIL:',e)
        raise SystemExit(1)
    print('R051_CHECK_PASS')
if __name__=='__main__': main()
