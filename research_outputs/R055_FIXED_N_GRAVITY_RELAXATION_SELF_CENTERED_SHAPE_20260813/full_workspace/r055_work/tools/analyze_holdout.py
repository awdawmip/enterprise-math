import json,sys,hashlib
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,'/mnt/data/r055_work/tools')
import r055_core as r
ROOT=Path('/mnt/data/r055_work')
Ns=[43,67,103,139,181,241,301]
FAMS=['HEX_SHELL_GROWTH','ELONGATED_STRIP','SIX_ARM_STAR','L_SHAPE_OR_WEDGE','EDEN_SEEDED_seed_550001','EDEN_SEEDED_seed_550021','EDEN_SEEDED_seed_550057','COMPACT_BFS_ALT_TIE']
def loadp(N):
 p=ROOT/f'holdout_primary/N{N}.jsonl'
 if N==301:p=ROOT/'holdout_primary/N301_complete.jsonl'
 return [json.loads(x) for x in open(p) if x.strip()]
def loadr(N):return [json.loads(x) for x in open(ROOT/f'holdout_refs/N{N}.jsonl') if x.strip()]
def C(row,field='final_state'):return frozenset(map(tuple,row[field]))
def cid(row):return r.state_id(r.canonical_state(C(row)))
def cc(row):return r.diagnostics(C(row))['centroid_class']
def frac(x): return Fraction(x['num'],x['den'])
rows=[]
for N in Ns:
 p=loadp(N);refs=loadr(N);assert len(p)==8,(N,len(p));assert len(refs)==16,(N,len(refs))
 ini=[x for x in refs if x['source']=='INITIAL'];ter=[x for x in refs if x['source']=='D1_PRIMARY_TERMINAL'];assert len(ini)==len(ter)==8
 bp={x['initial_family']:x for x in p};bt={x['initial_family']:x for x in ter}
 improved=[fam for fam in FAMS if bt[fam]['terminal_G']<bp[fam]['terminal_G']]
 tie_family='ELONGATED_STRIP';tp=ROOT/f'holdout_ties/strip/N{N}.jsonl';ties=[json.loads(x) for x in open(tp) if x.strip()]
 if len({cid(x) for x in ties})==1:
  tie_family='L_SHAPE_OR_WEDGE';ties=[json.loads(x) for x in open(ROOT/f'holdout_ties/extra/N{N}_L.jsonl') if x.strip()]
 rows.append({
  'N':N,'regime':'STRICT_HOLDOUT_OFF_SHELL',
  'D1_primary_terminal_class_count':len({cid(x) for x in p}),
  'D1_primary_terminal_G_values':sorted({x['terminal_G'] for x in p}),
  'D1_primary_centroid_class_count':len({tuple(cc(x)['canonical_residue']) for x in p}),
  'D1_primary_centroid_classes':sorted([{'canonical_residue':list(k),'d6_stabilizer_sizes':sorted(v)} for k,v in (lambda d:d)({tuple(cc(x)['canonical_residue']):set() for x in p}).items()],key=lambda z:z['canonical_residue']),
  'D1_terminals_improved_by_D2_count':len(improved),'D1_terminals_improved_by_D2_families':improved,
  'D2_from_initial_terminal_class_count':len({cid(x) for x in ini}),
  'D2_from_initial_terminal_G_values':sorted({x['terminal_G'] for x in ini}),
  'D2_from_D1_terminal_class_count':len({cid(x) for x in ter}),
  'D2_from_D1_terminal_G_values':sorted({x['terminal_G'] for x in ter}),
  'D2_combined_terminal_class_count':len({cid(x) for x in ini+ter}),
  'D2_combined_terminal_G_values':sorted({x['terminal_G'] for x in ini+ter}),
  'tie_break_dependence_witnessed':len({cid(x) for x in ties})>1,
  'tie_break_witness_family':tie_family,
  'tie_break_witness':[{'tie_break':x['tie_break'],'terminal_G':x['terminal_G'],'terminal_state_id':cid(x)} for x in ties],
 })
# fill stabilizers correctly
for row,N in zip(rows,Ns):
 p=loadp(N); d={}
 for x in p:
  z=cc(x);d.setdefault(tuple(z['canonical_residue']),set()).add(z['d6_stabilizer_size'])
 row['D1_primary_centroid_classes']=[{'canonical_residue':list(k),'d6_stabilizer_sizes':sorted(v)} for k,v in sorted(d.items())]
# objective monotonicity counterexamples wholly inside holdout primary
wanted={'P_edge':None,'A2':None,'boundary_squared_radius_dispersion':None,'six_direction_boundary_imbalance':None}
for N in Ns:
 for tr in loadp(N):
  state=C(tr,'initial_state');prev=r.diagnostics(state)
  for step,mv in enumerate(tr['moves'],1):
   u=(mv[0],mv[1]);v=(mv[2],mv[3]);state=frozenset((state-{u})|{v});cur=r.diagnostics(state)
   for key in wanted:
    if wanted[key] is not None: continue
    if key=='P_edge': bad=cur[key]>prev[key]
    else: bad=frac(cur[key])>frac(prev[key])
    if bad:wanted[key]={'N':N,'family':tr['initial_family'],'step':step,'G_after':mv[5],'move':[mv[0],mv[1],mv[2],mv[3]],'before':prev[key],'after':cur[key]}
   prev=cur
   if all(v is not None for v in wanted.values()):break
  if all(v is not None for v in wanted.values()):break
 if all(v is not None for v in wanted.values()):break
claims={
 'construction_D1_multi_attractor_survives_all_holdout_N':all(x['D1_primary_terminal_class_count']>1 for x in rows),
 'construction_tie_break_dependence_survives_all_holdout_N':all(x['tie_break_dependence_witnessed'] for x in rows),
 'D1_local_traps_detected_by_D2_on_all_holdout_N':all(x['D1_terminals_improved_by_D2_count']>0 for x in rows),
 'D2_unique_attractor_survives_holdout':all(x['D2_combined_terminal_class_count']==1 for x in rows),
 'D1_unique_centroid_class_survives_holdout':all(x['D1_primary_centroid_class_count']==1 for x in rows),
 'G_decrease_monotone_improves_all_other_diagnostics':all(v is None for v in wanted.values()),
}
obj={'schema':'R055_HOLDOUT_RESULTS_V1','status':'STRICT_HOLDOUT_COMPLETE_NO_RULE_CHANGES','holdout_N':Ns,
 'freeze_gate':{
  'R055_RELAXATION_PROTOCOL_SHA256':'aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683',
  'R055_MOVE_ENERGY_REGISTRY_SHA256':'83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb',
  'R055_INITIAL_STATE_REGISTRY_SHA256':'5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2',
  'R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256':'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660',
 },
 'rows':rows,'holdout_claim_checks':claims,'holdout_objective_monotonicity_counterexamples':wanted,
 'external_circle_hexagon_comparison_opened_during_holdout':False,'classical_pi_used_during_holdout':False}
r.json_dump(ROOT/'artifacts/R055_HOLDOUT_RESULTS.json',obj)
p=ROOT/'artifacts/R055_HOLDOUT_RESULTS.json';print('sha256',hashlib.sha256(p.read_bytes()).hexdigest())
for x in rows: print(x['N'],x['D1_primary_terminal_class_count'],x['D1_terminals_improved_by_D2_count'],x['D2_combined_terminal_class_count'],x['tie_break_dependence_witnessed'],x['D1_primary_centroid_class_count'],x['D2_combined_terminal_G_values'])
print(json.dumps(claims,indent=2));print(json.dumps(wanted,indent=2))
