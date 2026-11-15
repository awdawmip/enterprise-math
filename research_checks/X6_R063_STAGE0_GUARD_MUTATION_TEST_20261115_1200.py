import importlib.util, json, tempfile
from pathlib import Path
from math import comb
f=Path(__file__).with_name('X6_R063_STAGE0_NATIVE_REPLAY_ACCEPTANCE_GUARD_20261115_1200.py')
s=importlib.util.spec_from_file_location('g',f);g=importlib.util.module_from_spec(s);s.loader.exec_module(g)
with tempfile.TemporaryDirectory() as td:
 p=Path(td)
 discovery={'N':2500,'scalar_root':{'r':50},'ok':'fixture'}
 sha=g._sha(discovery)
 g.EXPECTED_DISCOVERY_SHA=sha
 discovery['discovery_snapshot_sha256']=sha
 summary={'schema':'R063_STAGE0_REPLAY_SUMMARY_V1','N':2500,'r':50,'acceptance_gates':{k:True for k in g.EXPECTED_GATES},'discovery_snapshot_sha256':sha,'C2':{'exact_set_equality':False},'C3':{'exact_set_equality':True},'C4':{'exact_set_equality':True},'one_sector_total_path_cardinality':110695538274255714208,'final_classification':'PATH_VALUED_SQUARE_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_SQUARE_NATIVE_NORMS','general_regression':{'r_range':[1,512],'combined_checker_mismatch_count':0,'rows_sha256':g.EXPECTED_ROW_SHA}}
 regression={'schema':'R063_STAGE0_GENERAL_SQUARE_REGRESSION_V1','r_range':[1,512],'tested_r_count':512,'C3_mismatch_count':0,'C4_mismatch_count':0,'combined_checker_mismatch_count':0,'rows_sha256':g.EXPECTED_ROW_SHA,'strong_result':'C3_AND_C4_EXACT_FOR_ALL_TESTED_SQUARES'}
 mismatches={'schema':'R063_STAGE0_MISMATCHES_V1','mismatch_count':0,'checker_mismatches':[],'smallest_mismatch':None}
 fiber={'N':2500,'r':50,'root_count':6,'ordered_nonnegative_component_roots':[list(x) for x in g.ROOTS]}
 paths={'N':2500,'r':50,'ordered_nonnegative_branch_count':6,'one_sector_total_path_cardinality':110695538274255714208,'branches':[{'components':list(x),'cardinality':comb(sum(x),x[0]),'word_length_path_letters_only':sum(x)} for x in g.ROOTS]}
 docs={'summary':summary,'regression':regression,'discovery':discovery,'mismatches':mismatches,'fiber':fiber,'paths':paths}
 def save():
  for key,obj in docs.items():(p/g.FILES[key]).write_text(json.dumps(obj,ensure_ascii=False))
 save();print('positive_fixture',g.verify(p))
 regression['tested_r_count']=0;save()
 try:g.verify(p)
 except ValueError as e:print('vacuous_range_rejected',e)
 regression['tested_r_count']=512;paths['branches'][2]['cardinality']=55347740058143510000;save()
 try:g.verify(p)
 except ValueError as e:print('rounded_BRC_rejected',e)
 paths['branches'][2]['cardinality']=comb(70,30);summary['acceptance_gates'].pop('SCALAR_SQRT_2500_EXACT');save()
 try:g.verify(p)
 except ValueError as e:print('missing_gate_rejected',e)
 print('PASS_X6_R063_STAGE0_GUARD_MUTATION_FIXTURES')
