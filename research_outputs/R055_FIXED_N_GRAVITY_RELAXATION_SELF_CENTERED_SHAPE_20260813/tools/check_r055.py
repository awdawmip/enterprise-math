#!/usr/bin/env python3
import argparse,json,hashlib,sys,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; ART=ROOT/'artifacts'; sys.path.insert(0,str(ROOT/'tools'))
import r055_core as r
EXPECTED={
 'R055_RELAXATION_PROTOCOL.json':'aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683',
 'R055_MOVE_ENERGY_REGISTRY.json':'83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb',
 'R055_INITIAL_STATE_REGISTRY.json':'5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2',
 'R055_THEOREM_COUNTEREXAMPLE_LEDGER.json':'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660',
}
REQUIRED=['R055_REPORT.md','R055_RELAXATION_PROTOCOL.json','R055_MOVE_ENERGY_REGISTRY.json','R055_INITIAL_STATE_REGISTRY.json','R055_SMALL_N_EXHAUSTIVE_ATLAS.json','R055_RELAXATION_TRAJECTORIES.json','R055_TERMINAL_SHAPE_ATLAS.json','R055_CENTROID_DYNAMICS_ATLAS.json','R055_OBJECTIVE_COMPARISON.json','R055_HOLDOUT_RESULTS.json','R055_EXTERNAL_SHAPE_COMPARISON.json','R055_THEOREM_COUNTEREXAMPLE_LEDGER.json','R055_ADVERSARIAL_TEST_RESULTS.json','R055_EXACT_CHECK_RESULTS.json','R055_ARTIFACT_MANIFEST.json']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def fail(msg):raise AssertionError(msg)
def check_hashes():
 for fn,h in EXPECTED.items():
  got=sha(ART/fn)
  if got!=h: fail(f'freeze hash mismatch {fn}: {got} != {h}')
def check_gates():
 hold=sha(ART/'R055_HOLDOUT_RESULTS.json'); led=EXPECTED['R055_THEOREM_COUNTEREXAMPLE_LEDGER.json']
 ext=json.load(open(ART/'R055_EXTERNAL_SHAPE_COMPARISON.json'))
 if ext['freeze_gate']['R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256']!=led:fail('external ledger gate mismatch')
 if ext['freeze_gate']['R055_HOLDOUT_RESULTS_SHA256']!=hold:fail('external holdout gate mismatch')
 src=(ROOT/'tools/r055_dynamics_exact.cpp').read_text().lower()
 for tok in ['circle','teacher','radius','circumference','tangent','m_pi']:
  if tok in src:fail(f'forbidden relaxation target token in engine source: {tok}')
 if re.search(r'\bpi\b',src):fail('pi token in relaxation engine source')
def check_required(skip_manifest=False):
 for fn in REQUIRED:
  if skip_manifest and fn=='R055_ARTIFACT_MANIFEST.json':continue
  if not (ART/fn).exists():fail(f'missing required artifact {fn}')
def check_manifest():
 m=json.loads((ART/'R055_ARTIFACT_MANIFEST.json').read_text())
 for z in m['files']:
  p=ROOT/z['path']
  if not p.exists():fail(f"manifest missing file {z['path']}")
  if sha(p)!=z['sha256']:fail(f"manifest sha mismatch {z['path']}")
  if p.stat().st_size!=z['size_bytes']:fail(f"manifest size mismatch {z['path']}")
def check_small():
 x=json.load(open(ART/'R055_SMALL_N_EXHAUSTIVE_ATLAS.json'));res=x['results']
 counts=[z['connected_classes'] for z in res]; holes=[z['hole_free_classes'] for z in res]
 if counts!=[1,1,3,7,22,82,333,1448,6572,30490,143552,683101]:fail('connected class counts drift')
 if holes!=[1,1,3,7,22,81,331,1435,6505,30086,141229,669584]:fail('holefree class counts drift')
 n6=res[5]
 if not(n6['D1_local_min_count']==3 and n6['D1_local_not_D2_min_count']==2 and not n6['G_P_minimizer_sets_coincide']):fail('N6 obstruction drift')
def check_trajectory_arithmetic(full=True):
 x=json.load(open(ART/'R055_RELAXATION_TRAJECTORIES.json'))
 groups=[k for k,v in x.items() if isinstance(v,list)]
 total_rows=total_moves=0
 topology_endpoints=0
 for k in groups:
  for row in x[k]:
   total_rows+=1;n=row['N'];C=set(map(tuple,row['initial_state']));
   if len(C)!=n:fail(f'N mismatch {k}')
   if r.energy_fast(C)!=row['initial_G']:fail('initial G mismatch')
   S=r.sum_point(C)
   if list(S)!=row['centroid_sum_sequence'][0]:fail('initial centroid sum mismatch')
   if len(row['G_sequence'])!=row['move_count']+1 or len(row['centroid_sum_sequence'])!=row['move_count']+1 or len(row['moves'])!=row['move_count']:fail('sequence length mismatch')
   if not r.connected(frozenset(C)) or not r.hole_free(frozenset(C)):fail('invalid trajectory initial topology')
   prev=row['initial_G'];
   for i,m in enumerate(row['moves']):
    total_moves+=1;u=(m[0],m[1]);v=(m[2],m[3]);dg,Ga,Sa,Sb=m[4],m[5],m[6],m[7]
    if u not in C or v in C:fail('replacement occupancy violation')
    if row['dynamics']=='D1' and r.Q((v[0]-u[0],v[1]-u[1]))!=1:fail('D1 nonlocal move')
    C.remove(u);C.add(v)
    if len(C)!=n:fail('cell count changed')
    if full:
     S=r.sum_point(C);G=r.energy_fast(C)
     if S!=(Sa,Sb):fail('full centroid recompute mismatch')
     if G!=Ga:fail('full G recompute mismatch')
    else:
     G=Ga
    if Ga-prev!=dg or not Ga<prev:fail('delta/strict descent mismatch')
    if row['G_sequence'][i+1]!=Ga or row['centroid_sum_sequence'][i+1]!=[Sa,Sb]:fail('audit sequence mismatch')
    prev=Ga
   if sorted(map(list,C))!=sorted(row['final_state']):fail('final state mismatch')
   if not r.connected(frozenset(C)) or not r.hole_free(frozenset(C)):fail('invalid trajectory terminal topology')
   topology_endpoints+=2
 return {'trajectory_rows':total_rows,'accepted_moves':total_moves,'full_centroid_and_G_recomputations':total_moves if full else 0,'full_topology_endpoint_checks':topology_endpoints}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--quick',action='store_true');args=ap.parse_args()
 check_required(skip_manifest=False);check_hashes();check_gates();check_manifest();check_small();stats=check_trajectory_arithmetic(full=not args.quick)
 print(json.dumps({'status':'PASS','mode':'quick' if args.quick else 'full_arithmetic','stats':stats,'frozen_hashes':EXPECTED},indent=2))
if __name__=='__main__':main()
