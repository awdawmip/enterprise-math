import json,sys,math,hashlib,statistics,time
from pathlib import Path
from collections import defaultdict
sys.path.insert(0,'/mnt/data/r055_work/tools')
import r055_core as r
from shapely.geometry import Polygon, Point
from shapely import union_all
from scipy.optimize import shgo
ROOT=Path('/mnt/data/r055_work');ART=ROOT/'artifacts'
SQ3=math.sqrt(3.0); CELL_AREA=SQ3/2.0; CELL_R=1/SQ3
CELL_VERTS=[(CELL_R*math.cos(math.pi/6+k*math.pi/3),CELL_R*math.sin(math.pi/6+k*math.pi/3)) for k in range(6)]
CONSTRUCTION=[19,31,37,53,61,79,91,113,127,151,169,199,217]
HOLDOUT=[43,67,103,139,181,241,301]

def loads(p): return [json.loads(x) for x in open(p) if x.strip()]
def canon_state_from_row(z): return r.canonical_state(frozenset(map(tuple,z['final_state'])))
def add_alias(store,z,arm,regime):
 C=canon_state_from_row(z); sid=r.state_id(C)
 rec=store.setdefault(sid,{'N':len(C),'canonical_state':[list(x) for x in C],'aliases':[]})
 rec['aliases'].append({'regime':regime,'arm':arm,'dynamics':z['dynamics'],'tie_break':z['tie_break'],'initial_family':z['initial_family'],'source':z['source'],'terminal_G':z['terminal_G'],'move_count':z['move_count']})
# all frozen/generated terminal shapes
shapes={}
for N in CONSTRUCTION:
 for z in loads(ROOT/f'construction_primary_ultra/N{N}.jsonl'): add_alias(shapes,z,'D1_PRIMARY','CONSTRUCTION')
 for z in loads(ROOT/f'construction_refs/N{N}.jsonl'): add_alias(shapes,z,'D2_REFERENCE','CONSTRUCTION')
 ts=loads(ROOT/f'tie_strip/N{N}.jsonl')
 for z in ts:
  if z['tie_break']!='T0_CANONICAL_MIN': add_alias(shapes,z,'ALT_TIE_CONTROL','CONSTRUCTION')
 if N in (31,217):
  for z in loads(ROOT/f'tie_extra/N{N}_L.jsonl'):
   if z['tie_break']!='T0_CANONICAL_MIN':add_alias(shapes,z,'ALT_TIE_CONTROL','CONSTRUCTION')
for N in HOLDOUT:
 pp=ROOT/f'holdout_primary/N{N}.jsonl'
 if N==301: pp=ROOT/'holdout_primary/N301_complete.jsonl'
 for z in loads(pp):add_alias(shapes,z,'D1_PRIMARY','HOLDOUT')
 for z in loads(ROOT/f'holdout_refs/N{N}.jsonl'):add_alias(shapes,z,'D2_REFERENCE','HOLDOUT')
 ts=loads(ROOT/f'holdout_ties/strip/N{N}.jsonl')
 # if strip was not a witness, extra L is the frozen control; retain both sets since both were actually run.
 for z in ts:
  if z['tie_break']!='T0_CANONICAL_MIN':add_alias(shapes,z,'ALT_TIE_CONTROL','HOLDOUT')
 ep=ROOT/f'holdout_ties/extra/N{N}_L.jsonl'
 if ep.exists():
  for z in loads(ep):
   if z['tie_break']!='T0_CANONICAL_MIN':add_alias(shapes,z,'ALT_TIE_CONTROL','HOLDOUT')

def xy(p):a,b=p;return (a+0.5*b,0.5*SQ3*b)
def geom_of(C):
 polys=[]
 for p in C:
  x,y=xy(p);polys.append(Polygon([(x+dx,y+dy) for dx,dy in CELL_VERTS]))
 return union_all(polys)
def boundary_vertices(geom):
 out=[]
 if geom.geom_type=='Polygon': polys=[geom]
 else: polys=list(geom.geoms)
 for p in polys:
  out.extend(list(p.exterior.coords)[:-1])
  for h in p.interiors:out.extend(list(h.coords)[:-1])
 return out
def hpoly(gx,gy,s,theta):return Polygon([(gx+s*math.cos(theta+k*math.pi/3),gy+s*math.sin(theta+k*math.pi/3)) for k in range(6)])
def fobj_factory(geom,A,gx,gy,s0):
 def f(x):
  th=float(x[0])%(math.pi/3); sr=float(x[1]); return geom.symmetric_difference(hpoly(gx,gy,s0*sr,th)).area/A
 return f
def external_metrics(C):
 C=frozenset(C);N=len(C);G=r.energy_fast(C);diag=r.diagnostics(C)
 Sa=sum(a for a,b in C);Sb=sum(b for a,b in C);gx=(Sa+0.5*Sb)/N;gy=0.5*SQ3*Sb/N
 A=N*CELL_AREA; R=math.sqrt(A/math.pi); s0=math.sqrt(2*A/(3*SQ3))
 geom=geom_of(C); area_rel=abs(geom.area-A)/A
 if area_rel>1e-10: raise RuntimeError(('area mismatch',N,area_rel))
 disk=Point(gx,gy).buffer(R,quad_segs=256)
 disk_sd=geom.symmetric_difference(disk).area/A
 verts=boundary_vertices(geom)
 radial_rms=math.sqrt(sum((math.hypot(x-gx,y-gy)/R-1.0)**2 for x,y in verts)/max(1,len(verts)))
 disk_hd=geom.boundary.hausdorff_distance(disk.boundary)/R
 # upper bound e0 from deterministic equal-area orientation grid; this also safely bounds any scale capable of beating e0.
 best_ea=(1e99,0.0)
 for i in range(61):
  th=(math.pi/3)*i/60
  val=geom.symmetric_difference(hpoly(gx,gy,s0,th)).area/A
  if val<best_ea[0]:best_ea=(val,th)
 e0,theta0=best_ea
 lo=math.sqrt(max(1e-8,1-e0));hi=math.sqrt(1+e0)
 f=fobj_factory(geom,A,gx,gy,s0)
 res=shgo(f,[(0,math.pi/3),(lo,hi)],n=64,iters=1,sampling_method='simplicial')
 candidates=[(e0,theta0,1.0)]
 if getattr(res,'success',False) or math.isfinite(float(res.fun)):
  candidates.append((float(res.fun),float(res.x[0])%(math.pi/3),float(res.x[1])))
 best=min(candidates,key=lambda x:x[0]);hex_sd,th,sr=best
 hp=hpoly(gx,gy,s0*sr,th)
 hex_ea=hpoly(gx,gy,s0,theta0)
 hex_hd=geom.boundary.hausdorff_distance(hp.boundary)/R
 # RMS point-to-model-boundary for actual polygon boundary vertices.
 hex_bd_rms=math.sqrt(sum(Point(x,y).distance(hp.boundary)**2 for x,y in verts)/max(1,len(verts)))/R
 mean_r2_region=G/(N*N)+5/36
 disk_mean=R*R/2
 hex_mean=5*(s0*sr)**2/12
 return {
  'N':N,'G':G,'P_edge':diag['P_edge'],'A2':diag['A2'],'six_direction_boundary_imbalance':diag['six_direction_boundary_imbalance'],
  'cluster_union_area':geom.area,'nominal_area':A,'area_relative_numeric_error':area_rel,'equivalent_disk_radius':R,
  'disk':{'symmetric_difference_over_cluster_area':disk_sd,'hausdorff_boundary_over_disk_radius':disk_hd,'boundary_vertex_radial_rms_over_disk_radius':radial_rms,'mean_r2_uniform_model':disk_mean,'region_mean_r2_relative_error':abs(mean_r2_region-disk_mean)/disk_mean},
  'regular_hexagon_equal_area':{'orientation_rad_best_grid':theta0,'symmetric_difference_over_cluster_area':e0,'circumradius':s0},
  'regular_hexagon_best_numeric':{'optimization_status':'NUMERIC_BEST_FOUND_NOT_ANALYTIC_CERTIFICATE','method':'SHGO_simplicial_n64_plus_equal_area_grid61','orientation_rad':th,'circumradius_scale_vs_equal_area':sr,'model_area_ratio':sr*sr,'symmetric_difference_over_cluster_area':hex_sd,'hausdorff_boundary_over_disk_radius':hex_hd,'boundary_vertex_distance_rms_over_disk_radius':hex_bd_rms,'mean_r2_uniform_model':hex_mean,'region_mean_r2_relative_error':abs(mean_r2_region-hex_mean)/hex_mean},
  'region_mean_r2_including_voronoi_cell_intrinsic_5_over_36':mean_r2_region,
  'closer_by_symmetric_difference_best_hex_vs_disk':'DISK' if disk_sd<hex_sd else ('HEX' if hex_sd<disk_sd else 'TIE'),
  'closer_by_symmetric_difference_equal_area_hex_vs_disk':'DISK' if disk_sd<e0 else ('HEX' if e0<disk_sd else 'TIE'),
  'closer_by_hausdorff_best_hex_vs_disk':'DISK' if disk_hd<hex_hd else ('HEX' if hex_hd<disk_hd else 'TIE')
 }

entries=[];t0=time.time()
for j,(sid,rec) in enumerate(sorted(shapes.items(),key=lambda kv:(kv[1]['N'],kv[0])),1):
 C=[tuple(x) for x in rec['canonical_state']];m=external_metrics(C);entries.append({'terminal_state_id':sid,'canonical_state':rec['canonical_state'],'aliases':rec['aliases'],'metrics':m})
 if j%50==0: print(f'PROGRESS {j}/{len(shapes)} elapsed={time.time()-t0:.1f}s',file=sys.stderr,flush=True)
# controls by N: deterministic hex-shell initial and best observed frozen P_edge terminal(s)
controls=[]
byN=defaultdict(list)
for e in entries:byN[e['metrics']['N']].append(e)
for N in sorted(byN):
 vals=byN[N];minp=min(e['metrics']['P_edge'] for e in vals);best=[e['terminal_state_id'] for e in vals if e['metrics']['P_edge']==minp]
 HC=r.canonical_state(r.hex_shell_growth(N)); hm=external_metrics(HC)
 controls.append({'N':N,'best_observed_frozen_terminal_P_edge':minp,'best_observed_frozen_terminal_state_ids':best,'global_P_edge_optimality_claimed':False,'HEX_SHELL_GROWTH_control':{'state_id':r.state_id(HC),'metrics':hm}})
# exact small-N global minimizer controls
small=json.load(open(ART/'R055_SMALL_N_EXHAUSTIVE_ATLAS.json'));small_controls=[]
seen={}
for row in small['results']:
 N=row['N']; items=[]
 for typ,key in [('GLOBAL_G_MIN','global_G_minimizers'),('GLOBAL_P_EDGE_MIN','global_P_edge_minimizers')]:
  for x in row[key]:
   sid=x['state_id'];
   if sid not in seen:seen[sid]=external_metrics([tuple(p) for p in x['canonical_state']])
   items.append({'type':typ,'state_id':sid,'metrics':seen[sid]})
 small_controls.append({'N':N,'items':items})
# aggregate comparison by N and main arm aliases
summary=[]
for N in sorted(byN):
 vals=byN[N]
 def counts(field):
  d={'DISK':0,'HEX':0,'TIE':0}
  for e in vals:d[e['metrics'][field]]+=1
  return d
 summary.append({'N':N,'unique_terminal_shapes_compared':len(vals),
  'best_hex_vs_disk_symmetric_difference_counts':counts('closer_by_symmetric_difference_best_hex_vs_disk'),
  'equal_area_hex_vs_disk_symmetric_difference_counts':counts('closer_by_symmetric_difference_equal_area_hex_vs_disk'),
  'best_hex_vs_disk_hausdorff_counts':counts('closer_by_hausdorff_best_hex_vs_disk')})
obj={
 'schema':'R055_EXTERNAL_SHAPE_COMPARISON_V1','status':'POST_LEDGER_AND_POST_HOLDOUT_ONLY','researcher_id':'EM-R055-4C2A71',
 'freeze_gate':{'R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256':'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660','R055_HOLDOUT_RESULTS_SHA256':hashlib.sha256((ART/'R055_HOLDOUT_RESULTS.json').read_bytes()).hexdigest()},
 'comparison_protocol':{
  'opened_after_holdout':True,'relaxation_refit_after_comparison':False,'classical_pi_role':'ONLY equal-area external disk radius R=sqrt(A/pi) and downstream comparison normalization',
  'occupied_cell_geometry':'Voronoi regular hexagon of triangular lattice spacing 1, area sqrt(3)/2; union used only for post-freeze external comparison',
  'disk':'equal-area Euclidean disk centered at final centroid; polygon approximation uses 1024 boundary segments (quad_segs=256)',
  'regular_hexagon':'centered at final centroid; equal-area scale baseline plus deterministic numerical alignment/rescale search minimizing symmetric difference; scale search is safely bounded using |A-B| lower bound from an available equal-area candidate; numerical optimum is not promoted to an analytic global theorem',
  'second_moment':'uniform union-region mean r^2 = G/N^2 + 5/36, compared with disk R^2/2 and regular hexagon 5 s^2/12',
  'hausdorff':'Shapely polygon-boundary Hausdorff distance normalized by equal-area disk radius',
  'normalized_radial_deviation':'RMS radial error of actual cluster-union boundary vertices relative to equal-area disk radius',
  'P_edge_control':'best observed among frozen terminal shapes at same N plus deterministic HEX_SHELL_GROWTH control; no global P_edge claim at construction/holdout N'
 },
 'unique_terminal_shape_count':len(entries),'terminal_shapes':entries,'per_N_controls':controls,'small_N_exact_controls':small_controls,'per_N_summary':summary
}
r.json_dump(ART/'R055_EXTERNAL_SHAPE_COMPARISON.json',obj)
p=ART/'R055_EXTERNAL_SHAPE_COMPARISON.json';print('unique',len(entries),'sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'size',p.stat().st_size,'elapsed',time.time()-t0)
for x in summary:print(x)
