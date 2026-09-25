"""Scoped BRC execution tests. No new classical/scipy/high-precision baseline.

Both exhaustive comparisons and symbolic computations go through registered
BRC action-germ interfaces. This is implementation cross-checking, NOT
independent mathematical review or revalidation of all historical experiments.
"""
from fractions import Fraction as F
from dataclasses import replace
from pathlib import Path
from itertools import product, permutations
import json, hashlib, random, sys
import pytest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import matrix,mm,inv,eye,Affine
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_carry_peak import _atoms,compile_carry_peak,peak_probability
from enterprise_math.heartbeat_peak_quotient import peak_observation_chain,passage_prefix
from enterprise_math.heartbeat_congruence_lift import _normalize_frame,verify_lifted_peak_frame,packet_matching_problem
from enterprise_math.heartbeat_weighted_kernel_lift import *
REPORT={}

def block(a):
 return matrix([[a[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])
I=eye(6);J=block(((0,1),(1,0)));T=block(((1,1),(0,1)))

def packet(actions,weights=None,counts=None):
 if weights is None:weights=[F(1,len(actions))]*len(actions)
 if counts is None:counts=[1]*len(actions)
 return ControlPacket.from_edges(1,0,1,[(0,0,w,Affine(a,(0,)*6),n) for a,w,n in zip(actions,weights,counts)])

def split_packet(q=1):
 e=block(((1,2**q),(0,1)));v=mm(mm(J,T),J)
 return packet([T,mm(T,e),v,mm(v,mm(mm(J,e),J))],[F(1,6),F(1,3),F(1,4),F(1,4)])

def changing_packet(p=2):
 s=block(((1,0),(p,1)))
 return packet([mm(mm(s,T),inv(s)) if k==1 else T for k in range(2)])

def chart(s=I,p=2):
 return repeated_pair_chart(p,_normalize_frame(s,p,1)[1])

def literal_frames(pkt,s,p,m,dirs):
 c=max(__import__('enterprise_math.heartbeat_switching_carry',fromlist=['linear_carry_spread']).linear_carry_spread(a,p) for _s,_t,_w,a,_n in _atoms(pkt))
 s,_=_normalize_frame(s,p,m+c);ok=[]
 for coefficients in product(range(p),repeat=len(dirs)):
  f=tuple(tuple(s[i][j]+p**(m+c)*sum(a*d[i][j] for a,d in zip(coefficients,dirs))%p**(m+c+1) for j in range(6)) for i in range(6))
  f=_normalize_frame(f,p,m+c+1)[0]
  try:verify_lifted_peak_frame(pkt,f,p,m+2)
  except ValueError:continue
  ok.append(f)
 return set(ok)

def test_01_source_pins():
 pins={'heartbeat_congruence_lift.py':'3909cc89b97b5e3a14fb0f1f18d85d19b7a390f9',
 'heartbeat_peak_orbits.py':'6f5a35851ed7cfef08fe34bb209fbd29c9b4b0dc',
 'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
 'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
 'heartbeat_carry_peak.py':'44bde8bbff397adf8aec80fcb2bffa79c6e272e9'}
 for name,digest in pins.items():
  raw=(ROOT/'src/enterprise_math'/name).read_bytes()
  assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==digest
 REPORT['inherited_source_pins']=pins

def test_02_original_mass_aggregation():
 p=split_packet(2);before=repr(p);coarse=packet_germ_classes(p,2,1);fine=packet_germ_classes(p,2,3)
 assert len(coarse)==2 and all(c.mass==F(1,2) for c in coarse)
 assert sorted(c.mass for c in fine)==[F(1,6),F(1,4),F(1,4),F(1,3)]
 assert sorted(i for c in fine for i in c.atom_ids)==list(range(4)) and repr(p)==before
 REPORT['mass_split']={'coarse_mass':['1/2','1/2'],'fine_masses':['1/6','1/3','1/4','1/4']}

def test_03_beyond_atomic_matching():
 p=split_packet(2);atoms=_atoms(p);possible=0
 for pi in permutations(range(4)):
  try:
   problem=packet_matching_problem(p,2,pi)
   # With unit unipotent actions all projective seed scalars at mod2 are1.
   problem.seed(J,[1]*4,1);possible+=1
  except ValueError:pass
 assert possible==0
 c=lift_weighted_kernel(p,J,2,1,correction_chart=chart(J));assert c.count and c.verify(p)
 for f in c.all_frames():verify_lifted_peak_frame(p,f,2,3)
 REPORT['atom_vs_mass']={'atomic_seed_matchings':possible,'weighted_next_frames':c.count}

def test_04_mass_obstruction():
 p=split_packet(1);c=lift_weighted_kernel(p,J,2,1)
 assert c.status=='MASS_SPLIT_OBSTRUCTION' and c.count==0 and c.obstruction and c.verify(p)
 assert len(c.families)==0
 REPORT['mass_obstruction_without_solving']=True

def test_05_precision_lifetime():
 checks=0
 for q in range(1,5):
  p=split_packet(q)
  for m in range(1,q+1):
   c=lift_weighted_kernel(p,J,2,m,correction_chart=chart(J))
   assert (c.count==0)==(m==q)
   assert set(c.all_frames())==literal_frames(p,J,2,m,chart(J));checks+=1
 REPORT['lifetime_BRC_fiber_checks']=checks

def test_06_changing_match_affine_union():
 p=changing_packet();c=lift_weighted_kernel(p,I,2,1,correction_chart=chart())
 assert c.status=='COMPLETE' and c.count==8 and sorted(f.system.count for f in c.families)==[4,4]
 assert len(c.affine_space.basis)==3 and c.verify(p)
 assert set(c.all_frames())==literal_frames(p,I,2,1,chart())
 REPORT['changing_matchings']={'families':[4,4],'consolidated_count':8,'dimension':3}

def test_07_full_X6_symbolic():
 p=changing_packet();c=lift_weighted_kernel(p,I,2,1)
 assert c.count==524288 and len(c.affine_space.basis)==19
 assert [f.system.count for f in c.families]==[262144,262144]
 assert c.verify(p)
 rng=random.Random(260926)
 for _ in range(12):
  theta=tuple(rng.randrange(2) for _ in c.affine_space.basis)
  certify_repaired_frame(p,c,theta)
 with pytest.raises(ValueError,match='FRAME_LIMIT'):c.all_frames(limit=100)
 REPORT['full_X6']={'count':c.count,'dimension':19,'family_counts':[262144,262144],'sampled_BRC_rechecks':12,'enumerated_all':False}

def test_08_random_small_BRC_fibers():
 rng=random.Random(38976);checks=0;literal=0
 for prime in (2,3):
  for _ in range(8):
   acts=[block(((1,rng.randint(0,4)),(0,1))),block(((1,0),(rng.randint(0,4),1)))]
   w=F(rng.randint(1,5),6);p=packet(acts,[w,1-w])
   dirs=chart(I,prime)
   c=lift_weighted_kernel(p,I,prime,1,correction_chart=dirs,max_matchings=24)
   assert set(c.all_frames(limit=1000))==literal_frames(p,I,prime,1,dirs)
   checks+=1;literal+=prime**len(dirs)
 REPORT['literal_BRC_crosschecks']={'fibers':checks,'candidates':literal}

def test_09_joint_obstruction():
 p=packet([T,block(((3,1),(0,1)))],[F(1,3),F(2,3)])
 c=lift_weighted_kernel(p,T,2,1,correction_chart=chart(T))
 assert c.status=='JOINT_OBSTRUCTION' and c.count==0 and c.families and c.verify(p)
 assert all(f.system.obstruction for f in c.families)
 REPORT['joint_equation_obstruction']=True

def test_10_budget_is_not_no_lifts():
 p=changing_packet();c=lift_weighted_kernel(p,I,2,1,correction_chart=chart(),max_matchings=1)
 assert c.status=='MATCHING_LIMIT' and c.count is None and c.affine_space is None and c.candidate_matchings==2
 assert c.verify(p)
 with pytest.raises(ValueError,match='MATCHING_LIMIT'):c.all_frames()
 REPORT['matching_budget_retains_unknown']=True

def test_11_packet_tamper():
 p=changing_packet();c=lift_weighted_kernel(p,I,2,1,correction_chart=chart())
 with pytest.raises(ValueError):c.verify(p.at(3))
 with pytest.raises(ValueError):replace(c,coarse_matching=(999,)).verify(p)
 with pytest.raises(ValueError):replace(c,affine_space=replace(c.affine_space,rank=99)).verify(p)

def test_12_original_count_not_frame_count():
 p=packet([T,T],[F(1,8),F(1,4)],[4,2]);before=repr(p)
 cs=packet_germ_classes(p,2,1)
 assert len(cs)==1 and cs[0].mass==1 and len(cs[0].atom_ids)==2
 c=lift_weighted_kernel(p,I,2,1,correction_chart=chart());certify_repaired_frame(p,c)
 assert repr(p)==before and sum(n for _s,_t,_w,_a,n in _atoms(p))==6
 REPORT['multiplicity_preserved']=6

def test_13_no_port_collapsing():
 p=ControlPacket.from_edges(2,0,1,[(0,0,F(1,2),Affine(T,(0,)*6),1),(0,1,F(1,2),Affine(T,(0,)*6),1),(1,1,1,Affine(T,(0,)*6),1)])
 c=packet_germ_classes(p,2,1)
 assert len(c)==3 and {(x.source,x.target) for x in c}=={(0,0),(0,1),(1,1)}
 assert lift_weighted_kernel(p,I,2,1,correction_chart=chart()).count

def test_14_affine_offsets_retained_not_observed():
 p=ControlPacket.from_edges(1,0,1,[(0,0,F(1,2),Affine(T,(0,)*6),1),(0,0,F(1,2),Affine(T,(1,0,0,0,0,0)),1)])
 c=packet_germ_classes(p,2,1);assert len(c)==1 and c[0].mass==1
 assert len(p.blocks[0][2].entries)==2
 assert lift_weighted_kernel(p,I,2,1,correction_chart=chart()).count

def test_15_actual_threshold_witness():
 p=split_packet(1);atoms=_atoms(p)
 L=block(((4,0),(0,1)));tail=block(((1,-1),(0,8)))
 values=[];prefixes=[]
 for conjugated in (False,True):
  actions=[mm(mm(J,a),J) if conjugated else a for _s,_t,_w,a,_n in atoms]
  q=ControlPacket.from_edges(4,0,1,[(0,1,1,Affine(L,(0,)*6),1)]+[(1,2,w,Affine(a,(0,)*6),n) for a,(_s,_t,w,_orig,n) in zip(actions,atoms)]+[(2,3,1,Affine(tail,(0,)*6),1),(3,3,1,Affine.identity(6),1)])
  model=compile_carry_peak(q,2,3,max_states=30)
  assert model.complete
  value=peak_probability(q,model);values.append(str(value.exact))
  pref=passage_prefix(peak_observation_chain(q,model),5);prefixes.append([str(x) for x in pref])
  assert pref[:3]==(0,0,0) and pref[4:]==(0,0) and pref[3]==value.exact
 assert values==['5/6','3/4']
 REPORT['actual_BRC_first_hit']={'threshold':3,'first_tick':3,'original_risk':values[0],'invalid_shallow_replacement_risk':values[1],'difference':'1/12','prefixes':prefixes,'preparation_spread':2}

def test_16_tower_rebuilds_refinement():
 p=split_packet(3)
 result=lift_weighted_tower(p,[J],2,1,4,correction_chart=chart(J),max_frames=100)
 assert result['status']=='NO_LIFTS' and result['depth']==4
 REPORT['tower']={'status':result['status'],'layers':result['layers']}

def test_17_tower_keeps_symbolic_frontier():
 p=changing_packet();out=lift_weighted_tower(p,[I],2,1,2,max_frames=10)
 assert out['status']=='FRAME_LIMIT' and out['frontier'][0].count==524288 and out['frames']
 assert out['frontier'][0].affine_space

def test_18_domain_rejections():
 p=changing_packet()
 tests=[lambda:lift_weighted_kernel(p,I,4,1),lambda:lift_weighted_kernel(p,I,2,0),
 lambda:lift_weighted_kernel(p,I,2,1,max_matchings=0),lambda:lift_weighted_kernel(p,I,2,1,correction_chart=()),
 lambda:lift_weighted_kernel(p,I,2,1,correction_chart=[I]),lambda:lift_weighted_kernel(p,I,2,1,correction_chart=chart()+chart()),
 lambda:lift_weighted_kernel(p.at(0),((1,0),(0,1)),2,1),
 lambda:lift_weighted_kernel(ControlPacket.from_edges(1,0,1,[(0,0,F(1,2),Affine.identity(6),1)]),I,2,1)]
 for call in tests:
  with pytest.raises((ValueError,TypeError,IndexError)):call()
 REPORT['domain_rejections']=len(tests)

def test_19_empty_tower():
 assert lift_weighted_tower(changing_packet(),[],2,1,2)['status']=='NO_LIFTS'
 assert lift_weighted_tower(changing_packet(),[I],2,1,1)['status']=='COMPLETE'
 with pytest.raises(ValueError):lift_weighted_tower(changing_packet(),[I],2,2,1)

def test_20_uniform_full_fiber_dimensions():
 p=changing_packet()
 first=lift_weighted_kernel(p,I,2,1,correction_chart=chart())
 # Choose another known coarse stabilizer; charts are the same block subgroup.
 other=lift_weighted_kernel(p,T,2,1,correction_chart=chart(T))
 assert first.count==other.count==8
 assert other.verify(p)
 REPORT['two_liftable_coarse_fibers']=[first.count,other.count]


def test_21_BRC_online_replay_after_mass_lift():
 from enterprise_math.heartbeat_peak_orbits import Frame,FiniteFrameGroup,certify_peak_symmetry,compile_orbit_peak,orbit_observation_chain
 from enterprise_math.heartbeat_peak_quotient import passage_law
 u=block(((2,0),(0,1)));v=block(((1,0),(0,2)));e=block(((1,4),(0,1)))
 actions=(u,mm(u,e),v,mm(v,mm(mm(J,e),J)))
 weights=(F(1,12),F(1,6),F(1,8),F(1,8))
 pkt=ControlPacket.from_edges(2,0,1,[(0,0,w,Affine(a,(0,)*6),1) for a,w in zip(actions,weights)]+[(0,1,F(1,2),Affine.identity(6),1),(1,1,1,Affine.identity(6),1)])
 lift=lift_weighted_kernel(pkt,J,2,1,correction_chart=chart(J))
 assert J in lift.all_frames()
 assert lift.verify(pkt)
 group=FiniteFrameGroup.generated(2,2,[Frame((0,1),J)])
 certificate=certify_peak_symmetry(pkt,group,3,mode='threshold')
 orbit=compile_orbit_peak(pkt,certificate,max_states=30)
 raw=compile_carry_peak(pkt,2,3,max_states=30)
 small=orbit_observation_chain(pkt,orbit);full=peak_observation_chain(pkt,raw)
 assert passage_prefix(small,25)==passage_prefix(full,25)
 law=passage_law(small);original_law=passage_law(full)
 from enterprise_math.heartbeat_peak_orbits import raw_to_orbit_labels
 labels=raw_to_orbit_labels(raw.states,orbit)+(len(orbit.states),len(orbit.states)+1)
 for field in ('probability','first_time_mass','conditional_time'):
  assert tuple(getattr(law,field)[j] for j in labels)==getattr(original_law,field)
 assert law.probability[0]==F(1,26) and law.conditional_time[0]==F(45,13)
 REPORT['online_reuse']={'raw_states':len(raw.states),'orbit_states':len(orbit.states),'risk':str(law.probability[0]),'conditional_mean':str(law.conditional_time[0]),'prefix_coefficients':26,'lift_count':lift.count}


def test_22_mass_defect_bound():
 from enterprise_math.heartbeat_peak_orbits import threshold_action_equivalent
 pkt=split_packet(1);c=lift_weighted_kernel(pkt,J,2,1,correction_chart=chart(J))
 bound=mass_split_defect_bound(pkt,c)
 assert bound=={0:F(1,6)}
 # A second BRC germ observer computes the actual projected measure defect.
 def actual(frame):
  g=matrix(frame);ginv=inv(g);bins=[]
  for moved in (False,True):
   for source,target,w,a,n in _atoms(pkt):
    image=mm(mm(g,a),ginv) if moved else a
    for entry in bins:
     if (source,target)==tuple(entry[:2]) and threshold_action_equivalent(image,entry[2],2,3):
      entry[3+int(moved)]+=w*n;break
    else:
     bins.append([source,target,image,F(0) if moved else w*n,w*n if moved else F(0)])
  return sum((abs(e[3]-e[4]) for e in bins),F(0))/2
 assert actual(J)==bound[0]
 for theta in product(range(2),repeat=3):
  dirs=chart(J)
  frame=tuple(tuple(J[i][j]+2*sum(t*d[i][j] for t,d in zip(theta,dirs)) for j in range(6)) for i in range(6))
  assert actual(frame)>=bound[0]
 REPORT['mass_defect_bound']={'lower_bound':'1/6','attained_at_J':True,'checked_frame_fiber':8,'observable':'fine action-germ distribution, not peak risk'}

def test_23_zero_mass_bound_is_not_liftability():
 pkt=packet([T,block(((3,1),(0,1)))],[F(1,3),F(2,3)])
 c=lift_weighted_kernel(pkt,T,2,1,correction_chart=chart(T))
 assert c.status=='JOINT_OBSTRUCTION' and mass_split_defect_bound(pkt,c)=={0:F(0)}
 REPORT['zero_mass_defect_still_joint_obstruction']=True

if __name__=='__main__':
 code=pytest.main([__file__,'-q'])
 mod=sys.modules.get('test_heartbeat_weighted_kernel_lift')
 data={'status':'PASS' if code==0 else 'FAIL','new_tests':23,'checks':mod.REPORT,
 'scope':'Typed BRC execution only; no ordinary reference dynamics; no physical/native residual attribution; no independent mathematical review'}
 out=ROOT/'research_notes/heartbeat_weighted_kernel_lift_20260926_3F0C88'
 out.mkdir(parents=True,exist_ok=True);(out/'RESULTS.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 raise SystemExit(code)
