import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,'/mnt/data/r055_work/tools');import r055_core as r
ROOT=Path('/mnt/data/r055_work');ART=ROOT/'artifacts'
paths=[
'artifacts/R055_REPORT.md','artifacts/R055_RELAXATION_PROTOCOL.json','artifacts/R055_MOVE_ENERGY_REGISTRY.json','artifacts/R055_INITIAL_STATE_REGISTRY.json','artifacts/R055_SMALL_N_EXHAUSTIVE_ATLAS.json','artifacts/R055_RELAXATION_TRAJECTORIES.json','artifacts/R055_TERMINAL_SHAPE_ATLAS.json','artifacts/R055_CENTROID_DYNAMICS_ATLAS.json','artifacts/R055_OBJECTIVE_COMPARISON.json','artifacts/R055_HOLDOUT_RESULTS.json','artifacts/R055_EXTERNAL_SHAPE_COMPARISON.json','artifacts/R055_THEOREM_COUNTEREXAMPLE_LEDGER.json','artifacts/R055_ADVERSARIAL_TEST_RESULTS.json','artifacts/R055_EXACT_CHECK_RESULTS.json','artifacts/R055_POSTFREEZE_THEOREM_ADDENDUM.json','artifacts/R055_LOCAL_HOLE_CRITERION_EXHAUSTIVE_CHECK.json','artifacts/R055_CONSTRUCTION_CLASSIFICATION.json',
'tools/r055_core.py','tools/r055_dynamics_exact.cpp','tools/r055_dynamics_exact','tools/check_r055.py','tools/check_local_hole_criterion.py','tools/build_small_atlas.py','tools/analyze_construction.py','tools/analyze_holdout.py','tools/external_compare.py','tools/freeze_ledger.py','tools/build_postfreeze_addendum.py','tools/build_final_combined_artifacts.py','tools/build_exact_adversarial.py','tools/build_manifest.py','tools/r055_exhaustive.cpp','tools/r055_n12_basin.cpp','tools/r055_t2_oriented.cpp','tests/test_r055.py']
files=[]
for rel in paths:
 p=ROOT/rel
 if not p.exists():raise SystemExit('missing '+rel)
 files.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size_bytes':p.stat().st_size})
obj={'schema':'R055_ARTIFACT_MANIFEST_V1','researcher_id':'EM-R055-4C2A71','task_id':'RS-R055-FIXED-N-GRAVITY-RELAXATION-SELF-CENTERED-SHAPE','status':'FINAL_RESEARCH_CHECKPOINT_NOT_CANONICAL','taskbook_source':'18072ad7a3ca50728b23e0fc21478b98ed027631','packet_source':'73e48ac77f403dc468cdea3458e14d10130386e0','R054_isolation':'NO_R054_FROZEN_SCORING_OR_HOLDOUT_CONSUMED',
'frozen_hashes':{'R055_RELAXATION_PROTOCOL_SHA256':'aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683','R055_MOVE_ENERGY_REGISTRY_SHA256':'83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb','R055_INITIAL_STATE_REGISTRY_SHA256':'5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2','R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256':'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660'},
'key_postfreeze_hashes':{'R055_HOLDOUT_RESULTS_SHA256':hashlib.sha256((ART/'R055_HOLDOUT_RESULTS.json').read_bytes()).hexdigest(),'R055_EXTERNAL_SHAPE_COMPARISON_SHA256':hashlib.sha256((ART/'R055_EXTERNAL_SHAPE_COMPARISON.json').read_bytes()).hexdigest(),'R055_POSTFREEZE_THEOREM_ADDENDUM_SHA256':hashlib.sha256((ART/'R055_POSTFREEZE_THEOREM_ADDENDUM.json').read_bytes()).hexdigest()},
'counts':{'small_N_exhaustive_max_N':12,'construction_N_count':13,'holdout_N_count':7,'frozen_initial_families_per_N':8,'trajectory_records':528,'accepted_moves':433531,'unique_terminal_translation_D6_classes':205,'external_terminal_classes_compared':205,'local_hole_regression_candidates':259136,'unit_tests':10},
'checker_command':'python tools/check_r055.py','test_command':'PYTHONPATH=tools python -m unittest discover -s tests -v','CI_status':'CI_NOT_REQUIRED_FOR_RESEARCH',
'manifest_hash_convention':'R055_ARTIFACT_MANIFEST_SHA256 is SHA256 of this JSON file itself; the manifest intentionally does not list itself in files to avoid self-reference.','files':files}
r.json_dump(ART/'R055_ARTIFACT_MANIFEST.json',obj)
p=ART/'R055_ARTIFACT_MANIFEST.json';print(hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size,len(files))
