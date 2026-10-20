import json,glob,os,hashlib
from pathlib import Path
from fractions import Fraction
import r055_core as r
ROOT=Path('/mnt/data/r055_work'); ART=ROOT/'artifacts'
Ns=[19,31,37,53,61,79,91,113,127,151,169,199,217]

def load(path):return [json.loads(x) for x in open(path)]
def C(row,field='final_state'):return frozenset(map(tuple,row[field]))
def canon(row):return r.canonical_state(C(row))
def stateid(row):return r.state_id(canon(row))
def finaldiag(row):return r.diagnostics(C(row))
primary=[];refs=[];ties=[]
for N in Ns:
 primary += load(ROOT/f'construction_primary_ultra/N{N}.jsonl')
 refs += load(ROOT/f'construction_refs/N{N}.jsonl')
 tr=load(ROOT/f'tie_strip/N{N}.jsonl')
 ties += [x for x in tr if x['tie_break']!='T0_CANONICAL_MIN']
 if N in (31,217):
  tr=load(ROOT/f'tie_extra/N{N}_L.jsonl')
  ties += [x for x in tr if x['tie_break']!='T0_CANONICAL_MIN']
traj={
 'schema':'R055_RELAXATION_TRAJECTORIES_V1','researcher_id':'EM-R055-4C2A71',
 'frozen_hashes':{'relaxation_protocol':'aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683','move_energy_registry':'83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb','initial_state_registry':'5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2'},
 'construction_primary_D1':primary,'construction_D2_primary_references':refs,'construction_alternative_tie_controls':ties,
 'engine':'r055_dynamics_final/ultrafast exact-equivalent engine; N19 full output cross-checked against Python reference and flood-fill engine',
 'move_record_format':'moves entries are [u_a,u_b,v_a,v_b,delta_G,G_after,centroid_sum_a_after,centroid_sum_b_after]',
 'centroid_rule':'centroid_sum is recomputed from all N occupied sites after every accepted move; g=centroid_sum/N',
 'external_shape_target_used':False
}
r.json_dump(ART/'R055_RELAXATION_TRAJECTORIES.json',traj)
# terminal atlas
entries=[]
for arm,rows in [('D1_PRIMARY',primary),('D2_REFERENCE',refs),('ALT_TIE_CONTROL',ties)]:
 for z in rows:
  cc=canon(z);d=finaldiag(z)
  entries.append({'N':z['N'],'arm':arm,'dynamics':z['dynamics'],'tie_break':z['tie_break'],'initial_family':z['initial_family'],'source':z['source'],'terminal_state_id':r.state_id(cc),'terminal_canonical':[list(x) for x in cc],'terminal_G':z['terminal_G'],'move_count':z['move_count'],'diagnostics':d})
term={'schema':'R055_TERMINAL_SHAPE_ATLAS_V1','entries':entries,'shape_equivalence':'translation+D6','external_disk_hexagon_comparison_opened':False}
r.json_dump(ART/'R055_TERMINAL_SHAPE_ATLAS.json',term)
# centroid dynamics atlas
cent=[]
for arm,rows in [('D1_PRIMARY',primary),('D2_REFERENCE',refs),('ALT_TIE_CONTROL',ties)]:
 for z in rows:
  n=z['N']; ss=z['centroid_sum_sequence']; d0=(ss[0][0],ss[0][1]);d1=(ss[-1][0],ss[-1][1]);ds=(d1[0]-d0[0],d1[1]-d0[1])
  fin=C(z); cc=r.centroid_class(fin)
  cent.append({'N':n,'arm':arm,'dynamics':z['dynamics'],'tie_break':z['tie_break'],'initial_family':z['initial_family'],'source':z['source'],'centroid_sum_sequence':ss,'final_centroid_class':cc,'net_centroid_displacement_squared':r.frac_obj(Fraction(r.Q(ds),n*n))})
r.json_dump(ART/'R055_CENTROID_DYNAMICS_ATLAS.json',{'schema':'R055_CENTROID_DYNAMICS_ATLAS_V1','entries':cent,'representation':'exact axial centroid sum S_t; g_t=S_t/N'})
# objective comparison
classification=json.load(open(ART/'R055_CONSTRUCTION_CLASSIFICATION.json'))
comparisons=[]
for z in primary:
 comparisons.append({'N':z['N'],'family':z['initial_family'],'initial':r.diagnostics(C(z,'initial_state')),'terminal':r.diagnostics(C(z)),'G_strictly_decreased_every_accepted_move':all(a>b for a,b in zip(z['G_sequence'],z['G_sequence'][1:]))})
obj={'schema':'R055_OBJECTIVE_COMPARISON_V1','construction_primary_initial_terminal':comparisons,'construction_classification':classification,'small_N_objective_set_separation':{'first_N':6,'statement':'At N=6 the unique global G minimizer is one of three global P_edge minimizers, so the minimizer sets are not equal; additional set separation occurs at N=9 and N=11 through N<=12.'},'monotonicity_conclusion':'Strict decrease of G does not monotonically improve P_edge, A2, boundary squared-radius dispersion, or six-direction boundary imbalance; exact step counterexamples are recorded in construction_classification.','combined_objective_used':False,'external_circle_or_pi_used':False}
r.json_dump(ART/'R055_OBJECTIVE_COMPARISON.json',obj)
for name in ['R055_RELAXATION_TRAJECTORIES.json','R055_TERMINAL_SHAPE_ATLAS.json','R055_CENTROID_DYNAMICS_ATLAS.json','R055_OBJECTIVE_COMPARISON.json']:
 print(name,r.sha256_file(ART/name),(ART/name).stat().st_size)
