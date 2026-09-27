"""Typed BRC-only checks of weighted germ lifts and peak observations.

No new classical/SNF/float reference run. All model evolution, certification,
branch serialization and probability readouts invoke preserved BRC interfaces.
Inputs below are explicitly declared integer Affine model arrows, not physics.
"""
from fractions import Fraction as F
from itertools import permutations, product
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
import hashlib,json,sys
import pytest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import eye,matrix,mm,Affine
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.brc_histogram import WeightHistogram,histogram_serial
from enterprise_math.heartbeat_carry_peak import _atoms,compile_carry_peak
from enterprise_math.heartbeat_peak_quotient import peak_observation_chain,passage_law,passage_prefix
from enterprise_math.heartbeat_peak_orbits import (Frame,FiniteFrameGroup,certify_peak_symmetry,
    compile_orbit_peak,orbit_observation_chain,threshold_action_equivalent)
from enterprise_math.heartbeat_switching_carry import linear_carry_spread
from enterprise_math.heartbeat_congruence_lift import packet_matching_problem,verify_lifted_peak_frame
from enterprise_math.heartbeat_weighted_germ_lift import *
REPORT={}
def block(a):return matrix([[a[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])
D=block(((2,0),(0,1)));V=block(((1,0),(0,2)));J=block(((0,1),(1,0)))
def stopped(terms):
 return ControlPacket.from_edges(2,0,1,[(0,0,w,Affine(a,(0,)*6),c) for a,w,c in terms]+
    [(0,1,F(1,2),Affine.identity(6),1),(1,1,1,Affine.identity(6),1)])
def split_packet(a=2):
 # V(I+2^a E12) is a declared integer model action; repeated on three pairs.
 return stopped(((D,F(1,4),1),(V,F(1,8),1),(block(((1,2**a),(0,2))),F(1,8),1)))
def toggling_packet(p=2,bias=False):
 if bias:
  return stopped(((D,F(1,8),1),(block(((2,4),(0,1))),F(3,8),1)))
 return stopped(tuple((block(((p,p*p*j),(0,1))),F(1,2*p),1) for j in range(p)))
@lru_cache(None)
def split_lift():
 p=split_packet();return lift_weighted_seed(p,weighted_lift_seed(p,J,2,1))
@lru_cache(None)
def toggle_lift(p=2,bias=False,budget=4096):
 k=toggling_packet(p,bias);return lift_weighted_seed(k,weighted_lift_seed(k,eye(6),p,1),max_matchings=budget)
@lru_cache(None)
def peak(split,R):
 p=split_packet() if split else stopped(((D,F(1,4),1),(V,F(1,4),1)))
 a=compile_carry_peak(p,2,R,max_states=500)
 c=peak_observation_chain(p,a)
 return p,a,c,passage_law(c)

def test_01_source_pins_and_typed_scope():
 pins={'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
 'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
 'heartbeat_congruence_lift.py':'3909cc89b97b5e3a14fb0f1f18d85d19b7a390f9',
 'heartbeat_peak_orbits.py':'6f5a35851ed7cfef08fe34bb209fbd29c9b4b0dc',
 'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9',
 'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb'}
 for name,sha in pins.items():
  data=(ROOT/'src/enterprise_math'/name).read_bytes()
  assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==sha
 scope=json.loads((ROOT/'research_notes/heartbeat_weighted_germ_lift_20260927_AD0416/SCOPE.json').read_text())
 assert scope['scientific_arithmetic_route']=='ACTUAL_TYPED_BRC_ONLY'
 REPORT['unchanged_source_blobs']=pins

def test_02_coalesce_and_refine():
 p=split_packet()
 assert [len(packet_germ_classes(p,2,m)) for m in (1,2,3)]==[3,3,4]
 assert len(_atoms(p))==5
 classes=packet_germ_classes(p,2,2)
 assert sorted(len(c.atom_indices) for c in classes)==[1,2,2]
 assert sum((w for c in classes for s,t,w in c.port_masses if s==0),F(0))==1
 REPORT['class_refinement']={'atoms':5,'germ_classes_m1_m2_m3':[3,3,4]}

def test_03_atom_bijection_is_too_strong():
 p=split_packet();valid_atom_matchings=0;valid_seeds=0
 for pi in permutations(range(len(_atoms(p)))):
  try:problem=packet_matching_problem(p,2,pi)
  except ValueError:continue
  valid_atom_matchings+=1
  try:problem.seed(J,(1,)*len(pi),1);valid_seeds+=1
  except ValueError:pass
 assert valid_seeds==0 and valid_atom_matchings==2
 assert split_lift().certified_count==2**17
 REPORT['atom_vs_mass']={'port_mass_atom_permutations':2,'valid_atom_seeds':0,'aggregate_lifts':2**17}

def test_04_full_aggregate_family():
 c=split_lift();assert c.status=='COMPLETE' and c.verify()
 assert len(c.space.basis)==17 and c.certified_count==131072
 assert len(c.components)==1
 REPORT['split_mass_family']={'free_dimensions':17,'count':c.certified_count,'components':1}

def test_05_refined_mass_signature_obstruction():
 p=split_packet();s=weighted_lift_seed(p,J,2,2);c=lift_weighted_seed(p,s)
 assert c.status=='NO_LIFTS' and c.certified_count==0 and c.verify()
 assert any(not row for row in c.adjacency)
 REPORT['refinement_obstruction']={'new_germ_depth':3,'threshold':4,'count':0,'adjacency':c.adjacency}

def test_06_torsor_joins_two_matchings():
 c=toggle_lift();assert c.verify()
 counts=[x.certificate.space.count for x in c.components]
 assert counts==[2**26,2**26]
 assert len(c.space.basis)==27 and c.certified_count==2**27
 REPORT['binary_torsor']={'component_counts':counts,'joined_dimension':27,'joined_count':c.certified_count}

def test_07_bias_removes_only_one_free_direction():
 c=toggle_lift(2,True);assert c.verify()
 assert c.certified_count==2**26 and len(c.components)==1
 REPORT['bias_dimension']={'symmetric':27,'biased':26,'not_a_no_lift':True}

def test_08_odd_prime_torsor():
 c=toggle_lift(3);assert c.verify()
 counts=[x.certificate.space.count for x in c.components]
 assert len(counts)==6 and counts.count(3**26)==3 and counts.count(0)==3
 assert c.certified_count==3**27 and len(c.space.basis)==27
 REPORT['ternary_torsor']={'matchings':6,'viable':3,'obstructed':3,'dimension':27,'count':3**27}

def test_09_partial_matching_budget_is_sound():
 empty=toggle_lift(2,False,0);part=toggle_lift(2,False,1);full=toggle_lift()
 assert empty.status=='MATCHING_LIMIT' and empty.certified_count==0
 assert part.status=='MATCHING_LIMIT' and part.certified_count==2**26
 assert part.verify() and full.status=='COMPLETE'
 assert full.certified_count==2*part.certified_count
 REPORT['matching_budget']={'zero_budget':'MATCHING_LIMIT','one_budget_known_count':2**26,'complete_count':2**27}

def test_10_symbolic_frame_budget_is_not_no_lift():
 p=split_packet();s=weighted_lift_seed(p,J,2,1)
 out=lift_weighted_family(p,[s],3,max_frames=20)
 assert out['status']=='FRAME_LIMIT' and out['frontier'][0].certified_count==2**17
 with pytest.raises(ValueError,match='FRAME_LIMIT'):out['frontier'][0].all_lifts(limit=20)
 REPORT['retained_frontier_count']=2**17

def test_11_probability_law_is_bound():
 c=toggle_lift();other=toggling_packet(2,True)
 with pytest.raises(ValueError):lift_weighted_seed(other,c.seed)
 with pytest.raises(ValueError):replace(c,complete=False).verify()
 with pytest.raises(ValueError):replace(c,space=replace(c.space,rank=999)).verify()

def test_12_domains():
 p=split_packet()
 for f in (lambda:weighted_lift_seed(p,J,4,1),lambda:weighted_lift_seed(p,J,2,0),
           lambda:weighted_lift_seed(p,((1,0),(0,1)),2,1),
           lambda:lift_weighted_seed(p,split_lift().seed,max_matchings=-1)):
  with pytest.raises((ValueError,TypeError)):f()
 assert lift_weighted_family(p,[],2)['status']=='NO_LIFTS'

def test_13_exact_peak_law_before_split():
 _,a,x,lx=peak(False,3);_,b,y,ly=peak(True,3)
 assert passage_prefix(x,24)==passage_prefix(y,24)
 assert lx.probability[x.initial]==ly.probability[y.initial]==F(1,26)
 assert lx.conditional_time[x.initial]==ly.conditional_time[y.initial]==F(45,13)
 REPORT['threshold3']={'original_states':len(a.states),'split_states':len(b.states),'risk':'1/26','conditional_time':'45/13','coefficients':25}

def test_14_probability_difference_after_split():
 _,a,x,lx=peak(False,4);_,b,y,ly=peak(True,4)
 ax,ay=passage_prefix(x,12),passage_prefix(y,12)
 assert ax[:8]==ay[:8] and ax[8]==F(7,16384) and ay[8]==F(57,131072)
 assert ay[8]-ax[8]==F(1,131072)
 assert lx.probability[x.initial]==F(1,97) and ly.probability[y.initial]==F(11717,1135289)
 REPORT['threshold4']={'original_states':len(a.states),'split_states':len(b.states),
  'original_risk':str(lx.probability[x.initial]),'split_risk':str(ly.probability[y.initial]),
  'first_different_tick':8,'original_tick8':str(ax[8]),'split_tick8':str(ay[8]),'difference_tick8':'1/131072'}

def test_15_brc_serial_path_witness():
 W=block(((1,4),(0,2)))
 trace=[];baseline=[];current=Affine.identity(6);old=Affine.identity(6)
 for a,b in zip((D,D,D,W,V,V,V,V),(D,D,D,V,V,V,V,V)):
  current=current.then(Affine(a,(0,)*6));old=old.then(Affine(b,(0,)*6))
  trace.append(linear_carry_spread(current.a,2));baseline.append(linear_carry_spread(old.a,2))
 assert trace==[1,2,3,2,1,2,3,4] and baseline==[1,2,3,2,1,0,1,2]
 weight=WeightHistogram.from_counts({1:1})
 for w,n in [(F(1,4),1)]*3+[(F(1,8),1)]+[(F(1,8),2)]*4:
  weight=histogram_serial(weight,WeightHistogram.from_counts({w:n}))
 assert weight.total_mass==F(1,131072)
 REPORT['path_witness']={'fine_word':'D D D W V V V V','new_trace':trace,'coarse_trace':baseline,
  'family':'D D D W {V,W}^4','family_positive_mass':str(weight.total_mass)}

def test_16_original_atoms_not_reweighted_by_repairs():
 p=split_packet();snapshot=repr(p);c=split_lift()
 c.instantiate((0,)*17)
 assert repr(p)==snapshot and len(_atoms(p))==5
 repeated=p.then(p.at(1))
 assert all(sum(w*n for s,t,w,a,n in _atoms(repeated) if s==k)==1 for k in range(2))
 assert [x[2] for x in _atoms(p) if x[0:2]==(0,0)].count(F(1,8))==2
 REPORT['repair_count_not_probability']=True

def test_17_online_quotient_still_executes_parent():
 p=split_packet();g=FiniteFrameGroup.generated(2,2,(Frame((0,1),J),),max_group=2)
 cert=certify_peak_symmetry(p,g,3,mode='threshold')
 auto=compile_orbit_peak(p,cert);chain=orbit_observation_chain(p,auto);law=passage_law(chain)
 assert len(auto.states)==4 and law.probability[chain.initial]==F(1,26)
 assert passage_prefix(chain,20)==passage_prefix(peak(True,3)[2],20)
 with pytest.raises(ValueError):certify_peak_symmetry(p,g,4,mode='threshold')
 REPORT['parent_online_reuse']={'raw_states':10,'orbit_states':4,'risk':'1/26','higher_threshold_rejected':True}

def test_18_splitting_weight_histogram_changes_no_mass_solution():
 p=split_packet();q=stopped(((D,F(1,8),2),(V,F(1,16),2),(block(((1,4),(0,2))),F(1,16),2)))
 a=split_lift();b=lift_weighted_seed(q,weighted_lift_seed(q,J,2,1))
 assert repr(p)!=repr(q) and a.space==b.space
 assert [c.port_masses for c in a.classes]==[c.port_masses for c in b.classes]
 assert a.certified_count==b.certified_count
 REPORT['atomic_refinement_invariance']={'same_mass_family':True,'same_raw_histogram':False}

def test_19_small_chart_full_check():
 # Only eight block-repeated corrections, but the family certificate is full X6.
 p=toggling_packet();c=toggle_lift();b=toggling_packet(2,True);cb=toggle_lift(2,True)
 def member(space,x):return all(sum(a*v for a,v in zip(row,x))%2==rhs for row,rhs in zip(space.coefficients,space.rhs))
 checked=0
 for u,v,w in product(range(2),repeat=3):
  X=block(((0,u),(v,w)));flat=tuple(int(z) for row in X for z in row)
  frame=tuple(tuple(int(eye(6)[i][j])+4*int(X[i][j]) for j in range(6)) for i in range(6))
  for packet,cert in ((p,c),(b,cb)):
   try:verify_lifted_peak_frame(packet,frame,2,3);valid=True
   except ValueError:valid=False
   assert valid==member(cert.space,flat)
   checked+=1
 assert checked==16
 REPORT['full_small_chart_crosscheck']=checked

def test_20_projective_basis_random_combinations():
 # Deterministic combinations of two certified directions; no Monte Carlo claims.
 c=toggle_lift();dimension=len(c.space.basis);checked=0
 for i in range(dimension):
  params=tuple(int(j in (i,(i+1)%dimension)) for j in range(dimension))
  lifted=c.instantiate(params)
  assert verify_lifted_peak_frame(c.packet,lifted.frame,2,3)
  checked+=1
 REPORT['additional_affine_combination_rechecks']=checked

if __name__=='__main__':
 code=pytest.main([__file__,'-q'])
 result=sys.modules.get('test_heartbeat_weighted_germ_lift').REPORT
 out=ROOT/'research_notes/heartbeat_weighted_germ_lift_20260927_AD0416'
 (out/'RESULTS.json').write_text(json.dumps({'schema':'HEARTBEAT_WEIGHTED_GERM_RESULTS_V1','status':'PASS' if code==0 else 'FAIL','new_tests':20,'checks':result},indent=2)+'\n')
 raise SystemExit(code)
