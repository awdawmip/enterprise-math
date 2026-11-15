"""Synthetic harness tests; NEVER a replay of the frozen native R063 program."""
import importlib.util
import json
from pathlib import Path
import tempfile

src=Path(__file__).with_name('X6_R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_20261116.py')
spec=importlib.util.spec_from_file_location('r063_harness',src)
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)

with tempfile.TemporaryDirectory() as t:
    root=Path(t)
    for p in h.ARTIFACTS:
        (root/p).write_text('{}\n')
    discovery={'schema':'SYNTHETIC_ONLY','input':{'N':2500}}
    d=h.sha256(h.canon(discovery))
    h.EXPECTED_DISCOVERY_DIGEST=d
    discovery['discovery_snapshot_sha256']=d
    (root/'R063_STAGE0_DISCOVERY_PHASE_FROZEN.json').write_bytes(h.canon(discovery)+b'\n')
    fake_rows_sha='a'*64
    h.EXPECTED_ROW_DIGEST=fake_rows_sha
    regression={'r_range':[1,512],'tested_r_count':512,
                'combined_checker_mismatch_count':0,
                'C3_mismatch_count':0,'C4_mismatch_count':0,
                'rows_sha256':fake_rows_sha}
    (root/'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json').write_bytes(h.canon(regression)+b'\n')
    core={'N':2500,'r':50,'discovery_snapshot_sha256':d,
          'ordered_nonnegative_component_root_count':6,
          'one_sector_total_path_cardinality':h.EXPECTED_SECTOR_BRC,
          'general_regression':{'r_range':[1,512],'rows_sha256':fake_rows_sha},
          'acceptance_gates':{g:True for g in h.EXPECTED_GATES}}
    summary={**core,'summary_core_sha256':h.sha256(h.canon(core))}
    (root/'R063_STAGE0_REPLAY_SUMMARY.json').write_bytes(h.canon(summary)+b'\n')
    (root/'R063_STAGE0_MISMATCHES.json').write_text('{"mismatch_count":0}\n')
    terminal={'status':'PASS','discovery_snapshot_sha256':d,
              'general_regression_mismatch_count':0,
              'one_sector_total_path_cardinality':h.EXPECTED_SECTOR_BRC}
    result=h.validate_outputs(root,terminal=terminal)
    assert result['full_regression_cases']==512
    print('PASS_SYNTHETIC_POSITIVE_SCHEMA_FIXTURE')
    for label,changes in [
        ('zero_cases',{'tested_r_count':0}),
        ('shorter_range',{'r_range':[1,511]}),
        ('wrong_hash',{'rows_sha256':'b'*64}),
        ('false_C3_mismatch',{'C3_mismatch_count':1}),
    ]:
        altered={**regression,**changes}
        (root/'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json').write_bytes(h.canon(altered)+b'\n')
        try:h.validate_outputs(root,terminal=terminal)
        except AssertionError:print('PASS_REJECT_'+label)
        else:raise AssertionError('mutation was accepted: '+label)
    (root/'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json').write_bytes(h.canon(regression)+b'\n')
    mutated_core={**core,'acceptance_gates':{k:(False if i==0 else True) for i,k in enumerate(h.EXPECTED_GATES)}}
    mutated_summary={**mutated_core,'summary_core_sha256':h.sha256(h.canon(mutated_core))}
    (root/'R063_STAGE0_REPLAY_SUMMARY.json').write_bytes(h.canon(mutated_summary)+b'\n')
    try:h.validate_outputs(root,terminal=terminal)
    except AssertionError:print('PASS_REJECT_FALSE_GATE_WITH_SELF_CONSISTENT_SHA')
    else:raise AssertionError('false gate accepted')
print('PASS_HARNESS_SYNTHETIC_TEST_SUITE; ORIGINAL_NATIVE_R063_NOT_EXECUTED')
