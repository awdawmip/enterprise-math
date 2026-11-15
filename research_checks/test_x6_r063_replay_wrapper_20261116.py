import importlib.util, tempfile, json
from pathlib import Path
spec=importlib.util.spec_from_file_location('runner',str(Path(__file__).with_name('X6_R063_PINNED_SAME_OBJECT_REPLAY_RUNNER_20261116.py')))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
assert len(m.SOURCES)==6 and len(m.EXPECTED_GATES)==17 and len(m.REQUIRED_OUTPUTS)==13
assert m.git_blob_sha1(b'abc')=='f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f'
with tempfile.TemporaryDirectory() as td:
  root=Path(td); repo=root/'repo'; (repo/'scripts/r063_stage0_checker_parts').mkdir(parents=True)
  for path in m.SOURCES:
    p=repo/path;p.write_text('intentionally WRONG fixture source\n')
  try:
    m.check_sources(repo)
    raise AssertionError('wrong pinned bytes accepted')
  except AssertionError as e:
    assert 'FROZEN_SOURCE_BLOB_MISMATCH' in str(e)
  out=root/'out';out.mkdir()
  for name in m.REQUIRED_OUTPUTS:(out/name).write_text('{}\n')
  discovery={'input':{'N':2500},'generated_component_roots':[[0,50]]}
  dsha=m.canonical_sha256(discovery);m.EXPECTED_DISCOVERY_SHA=dsha
  discovery['discovery_snapshot_sha256']=dsha
  reg={'r_range':[1,512], 'tested_r_count':512, 'combined_checker_mismatch_count':0,'C3_mismatch_count':0, 'C4_mismatch_count':0,'rows_sha256':'TEST_DIGEST','C2_failure_count':484}
  m.EXPECTED_ROWS_SHA='TEST_DIGEST'
  gates={name:True for name in m.EXPECTED_GATES}
  summary={'acceptance_gates':gates,'N':2500,'r':50,'discovery_snapshot_sha256':dsha,'ordered_nonnegative_component_root_count':6,'one_sector_total_path_cardinality':m.EXPECTED_SECTOR_BRC,'general_regression':{'r_range':[1,512], 'rows_sha256':'TEST_DIGEST','combined_checker_mismatch_count':0}}
  summary['summary_core_sha256']=m.canonical_sha256(summary)
  values={'R063_STAGE0_DISCOVERY_PHASE_FROZEN.json':discovery,'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json':reg,'R063_STAGE0_REPLAY_SUMMARY.json':summary,'R063_STAGE0_MISMATCHES.json':{'mismatch_count':0},'R063_STAGE0_COMPONENT_ROOT_FIBER.json':{'root_count':6, 'C3_exact':True,'C4_exact':True},'R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json':{'one_sector_total_path_cardinality':m.EXPECTED_SECTOR_BRC,'branches':[{'cardinality':m.EXPECTED_SECTOR_BRC}]},'R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json':{'node_id_uniqueness':True}}
  for name,val in values.items():(out/name).write_text(json.dumps(val))
  res=m.audit_outputs(out,{})
  assert res['acceptance_gate_count']==17
  summary['acceptance_gates']['PATHIFICATION_FORMULA_EXACT']=False
  summary['summary_core_sha256']=m.canonical_sha256({k:v for k,v in summary.items() if k!='summary_core_sha256'})
  (out/'R063_STAGE0_REPLAY_SUMMARY.json').write_text(json.dumps(summary))
  try:m.audit_outputs(out,{})
  except AssertionError:pass
  else:raise AssertionError('false gate accepted')
  summary['acceptance_gates']['PATHIFICATION_FORMULA_EXACT']=True
  summary['summary_core_sha256']=m.canonical_sha256({k:v for k,v in summary.items() if k!='summary_core_sha256'})
  (out/'R063_STAGE0_REPLAY_SUMMARY.json').write_text(json.dumps(summary))
  reg['tested_r_count']=0
  (out/'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json').write_text(json.dumps(reg))
  try:m.audit_outputs(out,{})
  except AssertionError:pass
  else:raise AssertionError('empty regression count accepted')
print('PASS_WRAPPER_SYNTHETIC_TESTS: correct 17 gate fixture accepted; wrong blob, false gate, vacuous 512 count rejected; ORIGINAL_BENCHMARK_NOT_EXECUTED')
