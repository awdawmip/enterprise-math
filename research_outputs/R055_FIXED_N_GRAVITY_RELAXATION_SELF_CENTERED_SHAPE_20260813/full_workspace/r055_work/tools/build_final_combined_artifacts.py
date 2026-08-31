import json,sys,hashlib
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,'/mnt/data/r055_work/tools');import r055_core as r
ROOT=Path('/mnt/data/r055_work');ART=ROOT/'artifacts'
CONS=[19,31,37,53,61,79,91,113,127,151,169,199,217];HOLD=[43,67,103,139,181,241,301]
def loads(p):return [json.loads(x) for x in open(p) if x.strip()]
def primary(N,reg):
 if reg=='construction':return loads(ROOT/f'construction_primary_ultra/N{N}.jsonl')
 p=ROOT/f'holdout_primary/N{N}.jsonl'
 if N==301:p=ROOT/'holdout_primary/N301_complete.jsonl'
 return loads(p)
def refs(N,reg):return loads(ROOT/f'{"construction_refs" if reg=="construction" else "holdout_refs"}/N{N}.jsonl')
def ties(N,reg):
 rows=[]
 if reg=='construction':
  ps=ROOT/f'tie_strip/N{N}.jsonl'; extras=[ROOT/f'tie_extra/N{N}_L.jsonl'] if N in (31,217) else []
 else:
  ps=ROOT/f'holdout_ties/strip/N{N}.jsonl'; ep=ROOT/f'holdout_ties/extra/N{N}_L.jsonl';extras=[ep] if ep.exists() else []
 for z in loads(ps):
  if z['tie_break']!='T0_CANONICAL_MIN':rows.append(z)
 for ep in extras:
  for z in loads(ep):
   if z['tie_break']!='T0_CANONICAL_MIN':rows.append(z)
 return rows
cp=[];cr=[];ct=[];hp=[];hr=[];ht=[]
for N in CONS:cp+=primary(N,'construction');cr+=refs(N,'construction');ct+=ties(N,'construction')
for N in HOLD:hp+=primary(N,'holdout');hr+=refs(N,'holdout');ht+=ties(N,'holdout')
traj={'schema':'R055_RELAXATION_TRAJECTORIES_V2','researcher_id':'EM-R055-4C2A71',
 'frozen_hashes':{'relaxation_protocol':'aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683','move_energy_registry':'83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb','initial_state_registry':'5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2','theorem_counterexample_ledger':'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660'},
 'construction_primary_D1':cp,'construction_D2_primary_references':cr,'construction_alternative_tie_controls':ct,
 'holdout_primary_D1':hp,'holdout_D2_primary_references':hr,'holdout_alternative_tie_controls':ht,
 'counts':{'construction_primary_D1':len(cp),'construction_D2_primary_references':len(cr),'construction_alternative_tie_controls':len(ct),'holdout_primary_D1':len(hp),'holdout_D2_primary_references':len(hr),'holdout_alternative_tie_controls':len(ht)},
 'engine':'r055_dynamics_exact.cpp; exact-equivalent Tarjan/low-link legality cache; accepted trajectories cross-checked against flood-fill/reference engine on N19, N43 and multi-tie N31 L witness',
 'move_record_format':'[u_a,u_b,v_a,v_b,delta_G,G_after,centroid_sum_a_after,centroid_sum_b_after]','centroid_rule':'full all-N sum recomputation after every accepted move; g=S/N','external_shape_target_used':False,'classical_pi_used':False}
r.json_dump(ART/'R055_RELAXATION_TRAJECTORIES.json',traj)

def C(z,field='final_state'):return frozenset(map(tuple,z[field]))
def entry(z,reg,arm):
 cc=r.canonical_state(C(z));return {'N':z['N'],'regime':reg,'arm':arm,'dynamics':z['dynamics'],'tie_break':z['tie_break'],'initial_family':z['initial_family'],'source':z['source'],'terminal_state_id':r.state_id(cc),'terminal_canonical':[list(x) for x in cc],'terminal_G':z['terminal_G'],'move_count':z['move_count'],'diagnostics':r.diagnostics(C(z))}
entries=[]
for reg,groups in [('CONSTRUCTION',[(cp,'D1_PRIMARY'),(cr,'D2_REFERENCE'),(ct,'ALT_TIE_CONTROL')]),('STRICT_HOLDOUT',[(hp,'D1_PRIMARY'),(hr,'D2_REFERENCE'),(ht,'ALT_TIE_CONTROL')])]:
 for rows,arm in groups:
  for z in rows:entries.append(entry(z,reg,arm))
r.json_dump(ART/'R055_TERMINAL_SHAPE_ATLAS.json',{'schema':'R055_TERMINAL_SHAPE_ATLAS_V2','shape_equivalence':'translation+D6','entries':entries,'counts':{'total':len(entries),'unique_state_ids':len({e['terminal_state_id'] for e in entries})},'external_disk_hexagon_comparison':'stored separately in post-freeze R055_EXTERNAL_SHAPE_COMPARISON.json'})
cent=[]
for reg,groups in [('CONSTRUCTION',[(cp,'D1_PRIMARY'),(cr,'D2_REFERENCE'),(ct,'ALT_TIE_CONTROL')]),('STRICT_HOLDOUT',[(hp,'D1_PRIMARY'),(hr,'D2_REFERENCE'),(ht,'ALT_TIE_CONTROL')])]:
 for rows,arm in groups:
  for z in rows:
   n=z['N'];ss=z['centroid_sum_sequence'];d=(ss[-1][0]-ss[0][0],ss[-1][1]-ss[0][1]);cent.append({'N':n,'regime':reg,'arm':arm,'dynamics':z['dynamics'],'tie_break':z['tie_break'],'initial_family':z['initial_family'],'source':z['source'],'centroid_sum_sequence':ss,'final_centroid_class':r.centroid_class(C(z)),'net_centroid_displacement_squared':r.frac_obj(Fraction(r.Q(d),n*n))})
r.json_dump(ART/'R055_CENTROID_DYNAMICS_ATLAS.json',{'schema':'R055_CENTROID_DYNAMICS_ATLAS_V2','entries':cent,'representation':'exact axial centroid sum S_t; g_t=S_t/N; S_t recomputed from full state after each accepted move'})
# objective comparison retains no external model in prefreeze sections; links postfreeze file separately.
con=json.load(open(ART/'R055_CONSTRUCTION_CLASSIFICATION.json'));hol=json.load(open(ART/'R055_HOLDOUT_RESULTS.json'));ext=json.load(open(ART/'R055_EXTERNAL_SHAPE_COMPARISON.json'))
comparisons=[]
for reg,rows in [('CONSTRUCTION',cp),('STRICT_HOLDOUT',hp)]:
 for z in rows:comparisons.append({'regime':reg,'N':z['N'],'family':z['initial_family'],'initial':r.diagnostics(C(z,'initial_state')),'terminal':r.diagnostics(C(z)),'G_strictly_decreased_every_accepted_move':all(a>b for a,b in zip(z['G_sequence'],z['G_sequence'][1:]))})
obj={'schema':'R055_OBJECTIVE_COMPARISON_V2','prefreeze_objectives_kept_separate':True,'combined_objective_used':False,'primary_D1_initial_terminal':comparisons,'construction_classification':con,'strict_holdout_classification':hol,
 'small_N_objective_set_separation':{'first_N':6,'statement':'At N=6 the unique global G minimizer is one of three global P_edge minimizers, so the minimizer sets are not equal; further set inequality occurs at N=9 and N=11 through N<=12.'},
 'monotonicity_conclusion':'Exact construction and strict-holdout steps show strict G decrease can worsen P_edge, A2, boundary squared-radius dispersion, and six-direction boundary imbalance.',
 'postfreeze_external_comparison_ref':{'file':'R055_EXTERNAL_SHAPE_COMPARISON.json','sha256':hashlib.sha256((ART/'R055_EXTERNAL_SHAPE_COMPARISON.json').read_bytes()).hexdigest(),'unique_terminal_shapes_compared':ext['unique_terminal_shape_count']}}
r.json_dump(ART/'R055_OBJECTIVE_COMPARISON.json',obj)
for fn in ['R055_RELAXATION_TRAJECTORIES.json','R055_TERMINAL_SHAPE_ATLAS.json','R055_CENTROID_DYNAMICS_ATLAS.json','R055_OBJECTIVE_COMPARISON.json']:
 p=ART/fn;print(fn,hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size)
print('counts',traj['counts'],'terminal',len(entries),len({e['terminal_state_id'] for e in entries}))
