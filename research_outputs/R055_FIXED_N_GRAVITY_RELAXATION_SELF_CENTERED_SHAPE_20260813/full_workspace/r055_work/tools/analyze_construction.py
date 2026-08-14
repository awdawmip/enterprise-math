import json,glob,os
from pathlib import Path
from fractions import Fraction
import r055_core as r
ROOT=Path('/mnt/data/r055_work')
Ns=[19,31,37,53,61,79,91,113,127,151,169,199,217]
shell=set([19,37,61,91,127,169,217])

def loadp(N):return [json.loads(x) for x in open(ROOT/f'construction_primary_ultra/N{N}.jsonl')]
def loadr(N):return [json.loads(x) for x in open(ROOT/f'construction_refs/N{N}.jsonl')]
def C(row,field='final_state'):return frozenset(map(tuple,row[field]))
def cid(row):return r.state_id(r.canonical_state(C(row)))
def cc(row):return r.diagnostics(C(row))['centroid_class']
def frac(d):return Fraction(d['num'],d['den'])
rows=[]
for N in Ns:
    p=loadp(N); refs=loadr(N)
    initial_refs=[x for x in refs if x['source']=='INITIAL']
    terminal_refs=[x for x in refs if x['source']=='D1_PRIMARY_TERMINAL']
    byfam_p={x['initial_family']:x for x in p}
    byfam_dt={x['initial_family']:x for x in terminal_refs}
    improved=[]
    for fam,x in byfam_p.items():
        y=byfam_dt[fam]
        if y['terminal_G']<x['terminal_G']:improved.append(fam)
    # tie witness files
    tiefile=ROOT/f'tie_strip/N{N}.jsonl'
    ties=[json.loads(x) for x in open(tiefile)]
    tie_family='ELONGATED_STRIP'
    if len({cid(x) for x in ties})==1:
        tie_family='L_SHAPE_OR_WEDGE';ties=[json.loads(x) for x in open(ROOT/f'tie_extra/N{N}_L.jsonl')]
    rows.append({
      'N':N,'regime':'CENTERED_HEX_SHELL_COUNT' if N in shell else 'OFF_SHELL',
      'D1_primary_terminal_class_count':len({cid(x) for x in p}),
      'D1_primary_terminal_G_values':sorted({x['terminal_G'] for x in p}),
      'D1_primary_centroid_class_count':len({tuple(cc(x)['canonical_residue']) for x in p}),
      'D1_primary_centroid_classes':sorted({(tuple(cc(x)['canonical_residue']),cc(x)['d6_stabilizer_size']) for x in p}),
      'D1_terminals_improved_by_D2_count':len(improved),'D1_terminals_improved_by_D2_families':improved,
      'D2_from_initial_terminal_class_count':len({cid(x) for x in initial_refs}),
      'D2_from_initial_terminal_G_values':sorted({x['terminal_G'] for x in initial_refs}),
      'D2_from_D1_terminal_class_count':len({cid(x) for x in terminal_refs}),
      'D2_from_D1_terminal_G_values':sorted({x['terminal_G'] for x in terminal_refs}),
      'tie_break_dependence_witnessed':len({cid(x) for x in ties})>1,
      'tie_break_witness_family':tie_family,
      'tie_break_witness':[{x['tie_break']: {'terminal_G':x['terminal_G'],'terminal_state_id':cid(x)}} for x in ties],
    })

# objective monotonicity counterexamples across primary trajectories
wanted={'P_edge':None,'A2':None,'boundary_squared_radius_dispersion':None,'six_direction_boundary_imbalance':None}
for N in Ns:
  if all(wanted.values()):break
  for tr in loadp(N):
    state=C(tr,'initial_state'); prev=r.diagnostics(state)
    for mv in tr['moves']:
      u=(mv[0],mv[1]);v=(mv[2],mv[3]); state=frozenset((state-{u})|{v}); cur=r.diagnostics(state)
      for key in wanted:
        if wanted[key] is not None:continue
        if key=='P_edge': worsened=cur[key]>prev[key]
        else: worsened=frac(cur[key])>frac(prev[key])
        if worsened:
          wanted[key]={'N':N,'family':tr['initial_family'],'step_G_after':mv[5],'move':[mv[0],mv[1],mv[2],mv[3]],'before':prev[key],'after':cur[key]}
      prev=cur
      if all(wanted.values()):break
    if all(wanted.values()):break

obj={'schema':'R055_CONSTRUCTION_CLASSIFICATION_V1','rows':rows,'objective_monotonicity_counterexamples':wanted}
r.json_dump(ROOT/'artifacts/R055_CONSTRUCTION_CLASSIFICATION.json',obj)
print(json.dumps(rows,indent=2))
print('counterexamples',json.dumps(wanted,indent=2))
