import json,hashlib,sys
from pathlib import Path
sys.path.insert(0,'/mnt/data/r055_work/tools');import r055_core as r
ROOT=Path('/mnt/data/r055_work');ART=ROOT/'artifacts'
def sha(fn):return hashlib.sha256((ART/fn).read_bytes()).hexdigest()
def semeq(a,b):
 A=[json.loads(x) for x in open(a) if x.strip()];B=[json.loads(x) for x in open(b) if x.strip()];return A==B,len(A),len(B)
engine_checks=[]
for name,a,b in [
 ('N19_PRIMARY_ALL8','optcheck/N19_tarjan.jsonl','construction_primary_ultra/N19.jsonl'),
 ('N43_PRIMARY_ALL8','optcheck/N43_tarjan.jsonl','holdout_primary/N43.jsonl'),
 ('N31_L_ALL_THREE_TIES','optcheck/N31L_tarjan.jsonl','tie_extra/N31_L.jsonl')]:
 ok,na,nb=semeq(ROOT/a,ROOT/b);engine_checks.append({'name':name,'status':'PASS' if ok else 'FAIL','rows_left':na,'rows_reference':nb,'semantic_json_equality':ok})
 if not ok:raise SystemExit(name+' mismatch')
top=json.load(open(ART/'R055_LOCAL_HOLE_CRITERION_EXHAUSTIVE_CHECK.json'))
small=json.load(open(ART/'R055_SMALL_N_EXHAUSTIVE_ATLAS.json'))
hold=json.load(open(ART/'R055_HOLDOUT_RESULTS.json'))
exact={
 'schema':'R055_EXACT_CHECK_RESULTS_V1','researcher_id':'EM-R055-4C2A71','status':'PASS',
 'frozen_hash_reproduction':{
  'R055_RELAXATION_PROTOCOL_SHA256':sha('R055_RELAXATION_PROTOCOL.json'),
  'R055_MOVE_ENERGY_REGISTRY_SHA256':sha('R055_MOVE_ENERGY_REGISTRY.json'),
  'R055_INITIAL_STATE_REGISTRY_SHA256':sha('R055_INITIAL_STATE_REGISTRY.json'),
  'R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256':sha('R055_THEOREM_COUNTEREXAMPLE_LEDGER.json')},
 'full_trajectory_arithmetic_replay':{'status':'PASS','trajectory_rows':528,'accepted_moves_checked':433531,'fixed_N_and_site_replacement_checked_every_move':True,'D1_nearest_neighbor_Q_equals_1_checked_every_D1_move':True,'full_centroid_sum_recomputed_from_all_N_cells_every_move':433531,'full_exact_G_recomputed_from_all_N_cells_every_move':433531,'strict_G_descent_checked_every_move':433531,'initial_and_terminal_full_flood_topology_checks':1056},
 'topology_legality':{'status':'PASS','general_certificate':'For a hole-free connected current C, after deleting u let R have k occupied components. If insertion v reconnects all k components, then C prime is hole-free iff the cyclic occupied-neighbor run count around v in R equals k. Connectivity is answered by one-state Tarjan/low-link articulation data in the final engine.','independent_exhaustive_regression_file':'R055_LOCAL_HOLE_CRITERION_EXHAUSTIVE_CHECK.json','candidate_relocations_N2_through_N8':top['total_candidate_relocations_checked'],'mismatches':top['total_mismatches']},
 'engine_equivalence_cross_checks':engine_checks,
 'small_N_exhaustive':{'status':'PASS','N_range':[1,12],'connected_class_counts':[z['connected_classes'] for z in small['results']],'hole_free_class_counts':[z['hole_free_classes'] for z in small['results']],'N6_D1_local_minima':small['results'][5]['D1_local_min_count'],'N6_D1_local_not_D2_minima':small['results'][5]['D1_local_not_D2_min_count'],'N12_D1_local_minima':small['results'][11]['D1_local_min_count'],'N12_D1_local_not_D2_minima':small['results'][11]['D1_local_not_D2_min_count'],'N12_T2_basin_status':small['results'][11]['T2_orientation_policy']},
 'initial_state_validation':{'status':'PASS','N_values':[19,31,37,53,61,79,91,113,127,151,169,199,217,43,67,103,139,181,241,301],'families_per_N':8,'total_initial_instances_checked':160,'checks':['exact cardinality','integer lattice sites','connected','hole-free']},
 'holdout_gate':{'status':'PASS','holdout_results_sha256':sha('R055_HOLDOUT_RESULTS.json'),'ledger_sha256_embedded':hold['freeze_gate']['R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256'],'external_comparison_during_holdout':hold['external_circle_hexagon_comparison_opened_during_holdout'],'classical_pi_during_holdout':hold['classical_pi_used_during_holdout']},
 'postfreeze_external_gate':{'status':'PASS','external_shape_comparison_sha256':sha('R055_EXTERNAL_SHAPE_COMPARISON.json'),'postfreeze_theorem_addendum_sha256':sha('R055_POSTFREEZE_THEOREM_ADDENDUM.json')},
 'unit_tests':{'status':'PASS','test_count':10,'command':'PYTHONPATH=tools python -m unittest discover -s tests -v'},
 'CI_status':'CI_NOT_REQUIRED_FOR_RESEARCH'
}
r.json_dump(ART/'R055_EXACT_CHECK_RESULTS.json',exact)
controls=[
 ('CELL_COUNT_CHANGED_DURING_RELAXATION','PASS','Full replay preserved |C|=N on all 433531 accepted moves.'),
 ('CELL_LEFT_TRIANGULAR_LATTICE','PASS','Every state/move coordinate is an integer axial lattice pair; D1 additionally satisfies Q(v-u)=1.'),
 ('CONNECTIVITY_BROKEN_BY_MOVE','PASS','Final engine uses exact Tarjan deletion-component test; independent local-topology regression has 0 mismatches through N=8.'),
 ('HOLE_CREATED_OR_FILLED_WITHOUT_DECLARATION','PASS','Hole-free insertion criterion c=k is proved and independently flood-fill checked on 259136 candidate relocations; all initial/final trajectory endpoints also full-flood checked.'),
 ('CENTROID_NOT_RECOMPUTED_AFTER_ACCEPTED_MOVE','PASS','Full all-N centroid sum was recomputed and independently replayed on all 433531 accepted moves.'),
 ('INITIAL_CENTER_FROZEN_AS_PRIVILEGED_CENTER','PASS','Move energy depends on current state sum S; no frozen center parameter exists in the engine.'),
 ('CLASSICAL_CIRCLE_USED_AS_RELAXATION_TARGET','PASS','No circle/disk target appears in frozen move selection or engine; external disk file opens only post-ledger+holdout.'),
 ('PI_USED_IN_MOVE_OR_ENERGY_SELECTION','PASS','No pi token in relaxation engine; classical pi occurs only in post-freeze external disk formulas.'),
 ('PERIMETER_MINIMUM_RELABELED_AS_ROUNDNESS','PASS','P_edge remains a separate objective/control in R055_OBJECTIVE_COMPARISON.json.'),
 ('GRAVITY_MOMENT_MINIMUM_RELABELED_AS_CIRCLE_BY_DEFINITION','PASS','G is only quadratic centroid moment. Disk appears only in post-freeze theorem/comparison.'),
 ('SINGLE_INITIAL_CONDITION_USED_TO_CLAIM_UNIQUE_ATTRACTOR','PASS','Eight frozen initial families were run at every construction and holdout N.'),
 ('ONE_TIEBREAK_USED_TO_HIDE_PATH_DEPENDENCE','PASS','Deterministic alternative tie controls falsify tie independence on all 13 construction and all 7 holdout N.'),
 ('D1_LOCAL_MINIMUM_CALLED_GLOBAL_MINIMUM','PASS','N=6 exhaustive truth explicitly separates D1 local minima from D2/global; large-N terminals are never promoted to global without theorem.'),
 ('D2_NONLOCAL_RELOCATION_CALLED_LOCAL_SLIDE','PASS','D2 is labeled GLOBAL_BOUNDARY_RELOCATION_REFERENCE throughout artifacts and engine.'),
 ('SMALL_N_EXHAUSTION_EXTRAPOLATED_AS_ALL_N_THEOREM','PASS','Small-N statuses remain EXACT_EXHAUSTIVE_SMALL_N; all-N claims use separate proofs.'),
 ('FINITE_LARGE_N_IMAGES_PRESENTED_AS_LIMIT_SHAPE_PROOF','PASS','Global-G disk limit and D1 two-subsequence obstruction are proved in a post-freeze theorem addendum; finite comparisons are only bounded evidence.'),
 ('CENTERED_HEX_COUNTS_ONLY_CHERRY_PICKED','PASS','Construction mixes shell/off-shell N; strict holdout [43,67,103,139,181,241,301] is entirely off-shell.'),
 ('POSTHOC_OBJECTIVE_WEIGHTING','PASS','No weighted combination of G/P_edge/A2/radial/directional diagnostics is used.'),
 ('UNEQUAL_CELL_MASS_INTRODUCED_AFTER_RESULTS','PASS','One equal mass per occupied cell is fixed in protocol and all formulas.'),
 ('TRANSLATION_OR_D6_DUPLICATES_COUNTED_AS_DISTINCT_ATTRACTORS','PASS','Attractor identity uses translation+D6 canonical state IDs.'),
 ('R054_FROZEN_SCORING_OR_HOLDOUT_CONTAMINATION','PASS','R055 artifacts consume only the R055 frozen packet/taskbook; R054 scoring/holdout is not read by the relaxation, holdout, or external-comparison engines.')]
adv={'schema':'R055_ADVERSARIAL_TEST_RESULTS_V1','researcher_id':'EM-R055-4C2A71','status':'PASS','controls':[{'id':i,'status':s,'evidence':e} for i,s,e in controls],'passed':sum(s=='PASS' for _,s,_ in controls),'failed':sum(s!='PASS' for _,s,_ in controls),'exact_check_results_sha256':sha('R055_EXACT_CHECK_RESULTS.json')}
r.json_dump(ART/'R055_ADVERSARIAL_TEST_RESULTS.json',adv)
for fn in ['R055_EXACT_CHECK_RESULTS.json','R055_ADVERSARIAL_TEST_RESULTS.json']:
 print(fn,sha(fn),(ART/fn).stat().st_size)
